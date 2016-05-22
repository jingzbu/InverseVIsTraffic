from util_data_storage_and_load import *
import numpy as np
from numpy.linalg import inv, matrix_rank
from numpy import linalg as LA
from gurobipy import *


try:
    from load_dicts import tmc_length_dict, tmc_ref_speed_dict, tmc_length_dict_ext, tmc_ref_speed_dict_ext
except ImportError:
    print "No dicts found; please check load_dicts..."

# define a function converting speed to flow, based on Greenshield's model
def speed_to_flow(capac, ref_speed, speed):
    free_speed = ref_speed
    if speed > free_speed or capac < 0:
	return 0
    return 4 * capac * speed / free_speed - 4 * capac * (speed ** 2) / (free_speed ** 2)

# obtain the number of days plus 1 for each month
def days(month):
    if month == 1:
        return 32
    elif month == 4:
        return 31
    elif month == 7:
        return 32
    elif month == 10:
        return 32
    else:
        raise IOError("Invalid input; please input another month.")

# convert the month number to string
def month_to_str(month):
    if month == 1:
        return 'Jan'
    elif month == 4:
        return 'Apr'
    elif month == 7:
        return 'Jul'
    elif month == 10:
        return 'Oct'
    else:
        raise IOError("Invalid input; please input another month.")

def adj_PSD(Sigma):
    # Ensure Sigma to be symmetric
    Sigma = (1.0 / 2) * (Sigma + np.transpose(Sigma))

    # Ensure Sigma to be positive semi-definite
    D, V = LA.eig(Sigma)
    D = np.diag(D)
    Q, R = LA.qr(V)
    for i in range(0, np.size(Sigma,0)):
        if D[i, i] < 1e-3:
            D[i, i] = 1e-3
    Sigma = np.dot(np.dot(Q, D), LA.inv(Q))
    return Sigma

# compute sample covariance matrix S for estimating OD demand matrix
def samp_cov(x):
    """
    x: sample matrix, each column is a link flow vector sample; 24 * K
    K: number of samples
    S: sample covariance matrix
    ----------------
    return: S
    ----------------
    """
    x = np.matrix(x)
    K = np.size(x, 1)
    x_mean = sum(x[:,k] for k in range(K)) / K
    S = sum(np.dot(x[:,k] - x_mean, np.transpose(x[:,k] - x_mean)) for k in range(K)) / (K - 1)
    S = adj_PSD(S)
    return S

# implement GLS method to estimate OD demand matrix
def GLS(x, A, P, L):
    """
    x: sample matrix, each column is a link flow vector sample; 24 * K
    A: path-link incidence matrix
    P: logit route choice probability matrix
    L: dimension of lam
    ----------------
    return: lam
    ----------------
    """
    K = np.size(x, 1)
    S = samp_cov(x)

    print("rank of S is: \n")
    print(matrix_rank(S))
    print("sizes of S are: \n")
    print(np.size(S, 0))
    print(np.size(S, 1))

    inv_S = inv(S)

    A_t = np.transpose(A)
    P_t = np.transpose(P)
    # PA'
    PA_t = np.dot(P, A_t)

    print("rank of PA_t is: \n")
    print(matrix_rank(PA_t))
    print("sizes of PA_t are: \n")
    print(np.size(PA_t, 0))
    print(np.size(PA_t, 1))

    # AP_t
    AP_t = np.transpose(PA_t)

    Q_ = np.dot(np.dot(PA_t, inv_S), AP_t)
    # Q = adj_PSD(Q_)  # Ensure Q to be PSD
    Q = Q_

    print("rank of Q is: \n")
    print(matrix_rank(Q))
    print("sizes of Q are: \n")
    print(np.size(Q, 0))
    print(np.size(Q, 1))

    b = sum([np.dot(np.dot(PA_t, inv_S), x[:, k]) for k in range(K)])

    model = Model("OD_matrix_estimation")

    lam = []
    for l in range(L):
        lam.append(model.addVar(name='lam_' + str(l)))

    model.update() 

    # Set objective: (K/2) lam' * Q * lam - b' * lam
    obj = 0
    for i in range(L):
        for j in range(L):
            obj += (1.0 / 2) * K * lam[i] * Q[i, j] * lam[j]
    for l in range(L):
        obj += - b[l] * lam[l]
    model.setObjective(obj)

    # Add constraint: lam >= 0
    for l in range(L):
        model.addConstr(lam[l] >= 0)

    model.update() 

    model.setParam('OutputFlag', False)
    model.optimize()

    lam_list = []
    for v in model.getVars():
        # print('%s %g' % (v.varName, v.x))
        lam_list.append(v.x)
    # print('Obj: %g' % obj.getValue())
    return lam_list

# define a function converting rough flow vector to feasible flow vector 
# (satisfying flow conservation law)
def flow_conservation_adjustment(y_0):
    L = len(y_0)  # dimension of flow vector x
    assert(L == 24)

    # y_0 = x[:,1]  # initial flow vector

    model = Model("Flow_conservation_adjustment")

    y = []
    for l in range(L):
        y.append(model.addVar(name='y_' + str(l)))

    model.update() 

    # Set objective: ||y-y_0||^2
    obj = 0
    for l in range(L):
        obj += (y[l] - y_0[l]) * (y[l] - y_0[l])
    model.setObjective(obj)

    # Add nonnegative constraint: y >= 0
    for l in range(L):
        model.addConstr(y[l] >= 0)
    # Add flow conservation constraints
    model.addConstr(y[1] + y[3] == y[0] + y[2])
    model.addConstr(y[0] + y[5] + y[7] == y[1] + y[4] + y[6])
    model.addConstr(y[2] + y[4] + y[9] + y[11] == y[3] + y[5] + y[8] + y[10])
    model.addConstr(y[6] + y[13] + y[17] == y[7] + y[12] + y[16])
    model.addConstr(y[8] + y[12] + y[15] + y[19] == y[9] + y[13] + y[14] + y[18])
    model.addConstr(y[10] + y[14] + y[21] == y[11] + y[15] + y[20])
    model.addConstr(y[18] + y[20] + y[23] == y[19] + y[21] + y[22])
    model.addConstr(y[16] + y[22] == y[17] + y[23])

    model.update() 

    model.setParam('OutputFlag', False)
    model.optimize()

    y = []
    for v in model.getVars():
        # print('%s %g' % (v.varName, v.x))
        y.append(v.x)
    # print('Obj: %g' % obj.getValue())
    return y

# for the extended network
def flow_conservation_adjustment_ext(y_0):
    L = len(y_0)  # dimension of flow vector x
    assert(L == 74)

    # y_0 = x[:,1]  # initial flow vector

    model = Model("Flow_conservation_adjustment_ext")

    y = []
    for l in range(L):
        y.append(model.addVar(name='y_' + str(l)))

    model.update() 

    # Set objective: ||y-y_0||^2
    obj = 0
    for l in range(L):
        obj += (y[l] - y_0[l]) * (y[l] - y_0[l])
    model.setObjective(obj)

    # Add nonnegative constraint: y >= 0
    for l in range(L):
        model.addConstr(y[l] >= 0)
    # Add flow conservation constraints
    model.addConstr(y[1] + y[3] == y[0] + y[2])  # node 1
    model.addConstr(y[0] + y[5] + y[7] == y[1] + y[4] + y[6])  # node 2
    model.addConstr(y[2] + y[4] + y[9] == y[3] + y[5] + y[8])  # node 3
    model.addConstr(y[6] + y[11] + y[13] + y[16] + y[19] == y[7] + y[10] + y[12] + y[14] + y[18])  # node 4
    model.addConstr(y[18] + y[23] + y[25] == y[19] + y[22] + y[24])  # node 5
    model.addConstr(y[8] + y[10] + y[21] == y[9] + y[11] + y[20])  # node 6
    model.addConstr(y[12] + y[15] + y[20] + y[27] + y[29] == y[13] + y[17] + y[21] + y[26] + y[28])  # node 7
    model.addConstr(y[22] + y[33] + y[37] == y[23] + y[32] + y[36])  # node 8
    model.addConstr(y[24] + y[26] + y[31] == y[25] + y[27] + y[30])  # node 9
    model.addConstr(y[30] + y[32] + y[35] + y[39] == y[31] + y[33] + y[34] + y[38])  # node 10
    model.addConstr(y[28] + y[34] + y[41] == y[29] + y[35] + y[40])  # node 11
    model.addConstr(y[36] + y[43] + y[46] + y[45] + y[50] == y[37] + y[42] + y[44] + y[47] + y[48])  # node 12
    model.addConstr(y[38] + y[42] + y[45] + y[49] + y[53] + y[56] + y[61] + y[63] == y[39] + y[43] + y[47] + y[51] + y[52] + y[54] + y[60] + y[62])  # node 13
    model.addConstr(y[40] + y[52] + y[55] + y[65] + y[68] == y[41] + y[53] + y[57] + y[64] + y[66])  # node 14
    model.addConstr(y[58] + y[60] + y[71] == y[59] + y[61] + y[70])  # node 15
    model.addConstr(y[62] + y[64] + y[67] + y[73] == y[63] + y[65] + y[69] + y[72])  # node 16
    model.addConstr(y[70] + y[72] == y[71] + y[73])  # node 17
    model.addConstr(y[14] + y[17] == y[15] + y[16])  # node 18
    model.addConstr(y[44] + y[47] == y[45] + y[46])  # node 19
    model.addConstr(y[48] + y[51] == y[49] + y[50])  # node 20
    model.addConstr(y[54] + y[57] == y[55] + y[56])  # node 21
    model.addConstr(y[66] + y[69] == y[67] + y[68])  # node 22

    model.update() 

    model.setParam('OutputFlag', False)
    model.optimize()

    y = []
    for v in model.getVars():
        # print('%s %g' % (v.varName, v.x))
        y.append(v.x)
    # print('Obj: %g' % obj.getValue())
    return y

##### define classes

# define a road segment class corresponding to the original filtered shape file
# Inr indicates INRIX
class RoadSegInr(object):
    def __init__(self, tmc, road_num, shape_length):
        self.tmc = tmc
        self.road_num = road_num
        self.shape_length = shape_length

# define a road segment capacity class corresponding to the capacity file
class RoadSegCapac(object):
    def __init__(self, road_invent, length, route_num, AB_AM_capac, \
                 AB_MD_capac, AB_PM_capac, AB_NT_capac):
        self.road_invent = road_invent
        self.length = length
        self.route_num = route_num
        self.AB_AM_capac = AB_AM_capac
        self.AB_MD_capac = AB_MD_capac
        self.AB_PM_capac = AB_PM_capac
        self.AB_NT_capac = AB_NT_capac

# define a derived road segment capacity class corresponding to the capacity file
# with info of "number of lanes"
class RoadSegCapacLane(RoadSegCapac):
    def __init__(self, road_invent, length, route_num, AB_AM_capac, \
                 AB_MD_capac, AB_PM_capac, AB_NT_capac, AB_AM_lane, \
		 AB_MD_lane, AB_PM_lane, AB_NT_lane):
	RoadSegCapac.__init__(self, road_invent, length, route_num, AB_AM_capac, \
                 AB_MD_capac, AB_PM_capac, AB_NT_capac)
        self.AB_AM_lane = AB_AM_lane
        self.AB_MD_lane = AB_MD_lane
        self.AB_PM_lane = AB_PM_lane
        self.AB_NT_lane = AB_NT_lane

# define a lookup class corresponding to the lookup table file
class LookUp(object):
    def __init__(self, road_inv_ID, tmc):
        self.road_inv_ID = road_inv_ID
        self.tmc = tmc

# define a derived road segment class containing the capacity info
class RoadSegInrCapac(RoadSegInr):
    def __init__(self, tmc, road_num, shape_length, AB_AM_capac, \
                 AB_MD_capac, AB_PM_capac, AB_NT_capac):
        RoadSegInr.__init__(self, tmc, road_num, shape_length)
        self.AB_AM_capac = AB_AM_capac
        self.AB_MD_capac = AB_MD_capac
        self.AB_PM_capac = AB_PM_capac
        self.AB_NT_capac = AB_NT_capac

# define a class containing tmc, day, and speed
class TMC_Day_Speed(object):
    def __init__(self, tmc, day, speed, travel_time):
        self.tmc = tmc
        self.day = day
        self.speed = speed
        self.travel_time = travel_time
    def ave_speed(self):
        return sum([self.speed[i] * self.travel_time[i] for i in range(len(self.speed))]) / sum(self.travel_time)

# define a derived road segment class containing the average flow info
class RoadSegInrCapacFlow(RoadSegInrCapac):
    def __init__(self, tmc, road_num, shape_length, day,
		 AB_AM_capac, AB_MD_capac, AB_PM_capac, AB_NT_capac, \
		 AM_ave_speed, MD_ave_speed, PM_ave_speed, NT_ave_speed):
        RoadSegInrCapac.__init__(self, tmc, road_num, shape_length, \
				 AB_AM_capac, AB_MD_capac, AB_PM_capac, AB_NT_capac)
        self.day = day
        self.AM_ave_speed = AM_ave_speed
        self.MD_ave_speed = MD_ave_speed
        self.PM_ave_speed = PM_ave_speed
	self.NT_ave_speed = NT_ave_speed
    def AM_flow(self):
	return speed_to_flow(self.AB_AM_capac, tmc_ref_speed_dict[self.tmc], self.AM_ave_speed)
    def MD_flow(self):
	return speed_to_flow(self.AB_MD_capac, tmc_ref_speed_dict[self.tmc], self.MD_ave_speed)
    def PM_flow(self):
	return speed_to_flow(self.AB_PM_capac, tmc_ref_speed_dict[self.tmc], self.PM_ave_speed)
    def NT_flow(self):
	return speed_to_flow(self.AB_NT_capac, tmc_ref_speed_dict[self.tmc], self.NT_ave_speed)

# define a derived road segment class containing the average flow info, for the extended map
class RoadSegInrCapacFlowExt(RoadSegInrCapac):
    def __init__(self, tmc, road_num, shape_length, day,
		 AB_AM_capac, AB_MD_capac, AB_PM_capac, AB_NT_capac, \
		 AM_ave_speed, MD_ave_speed, PM_ave_speed, NT_ave_speed):
        RoadSegInrCapac.__init__(self, tmc, road_num, shape_length, \
				 AB_AM_capac, AB_MD_capac, AB_PM_capac, AB_NT_capac)
        self.day = day
        self.AM_ave_speed = AM_ave_speed
        self.MD_ave_speed = MD_ave_speed
        self.PM_ave_speed = PM_ave_speed
	self.NT_ave_speed = NT_ave_speed
    def AM_flow(self):
	return speed_to_flow(self.AB_AM_capac, tmc_ref_speed_dict_ext[self.tmc], self.AM_ave_speed)
    def MD_flow(self):
	return speed_to_flow(self.AB_MD_capac, tmc_ref_speed_dict_ext[self.tmc], self.MD_ave_speed)
    def PM_flow(self):
	return speed_to_flow(self.AB_PM_capac, tmc_ref_speed_dict_ext[self.tmc], self.PM_ave_speed)
    def NT_flow(self):
	return speed_to_flow(self.AB_NT_capac, tmc_ref_speed_dict_ext[self.tmc], self.NT_ave_speed)

## define a derived road segment class containing the "instaneous" flow (for each minute) info 
## for purpose of estimating the O-D demand matrix 
class RoadSegInrCapacFlowMinute(RoadSegInrCapacFlow):
    def __init__(self, tmc, road_num, shape_length, day,
		 AB_AM_capac, AB_MD_capac, AB_PM_capac, AB_NT_capac, \
		 AM_ave_speed, MD_ave_speed, PM_ave_speed, NT_ave_speed, \
		 AM_speed_minute, MD_speed_minute, PM_speed_minute, NT_speed_minute):
        RoadSegInrCapacFlow.__init__(self, tmc, road_num, shape_length, day, \
				 AB_AM_capac, AB_MD_capac, AB_PM_capac, AB_NT_capac, \
				 AM_ave_speed, MD_ave_speed, PM_ave_speed, NT_ave_speed)
	self.AM_speed_minute = AM_speed_minute
	self.MD_speed_minute = MD_speed_minute
	self.PM_speed_minute = PM_speed_minute
	self.NT_speed_minute = NT_speed_minute
    def AM_flow_minute(self):
	AM_flow_minute_list = []
	for i in range(len(self.AM_speed_minute)):
	    AM_flow_minute_list.append(speed_to_flow(self.AB_AM_capac, tmc_ref_speed_dict[self.tmc], self.AM_speed_minute[i]))
	return AM_flow_minute_list
    def MD_flow_minute(self):
	MD_flow_minute_list = []
	for i in range(len(self.MD_speed_minute)):
	    MD_flow_minute_list.append(speed_to_flow(self.AB_MD_capac, tmc_ref_speed_dict[self.tmc], self.MD_speed_minute[i]))
	return MD_flow_minute_list
    def PM_flow_minute(self):
	PM_flow_minute_list = []
	for i in range(len(self.PM_speed_minute)):
	    PM_flow_minute_list.append(speed_to_flow(self.AB_PM_capac, tmc_ref_speed_dict[self.tmc], self.PM_speed_minute[i]))
	return PM_flow_minute_list
    def NT_flow_minute(self):
	NT_flow_minute_list = []
	for i in range(len(self.NT_speed_minute)):
	    NT_flow_minute_list.append(speed_to_flow(self.AB_NT_capac, tmc_ref_speed_dict[self.tmc], self.NT_speed_minute[i]))
	return NT_flow_minute_list

## define a derived road segment class containing the "instaneous" flow (for each minute) info 
## for purpose of estimating the O-D demand matrix 
## for the extended map
class RoadSegInrCapacFlowMinuteExt(RoadSegInrCapacFlow):
    def __init__(self, tmc, road_num, shape_length, day,
		 AB_AM_capac, AB_MD_capac, AB_PM_capac, AB_NT_capac, \
		 AM_ave_speed, MD_ave_speed, PM_ave_speed, NT_ave_speed, \
		 AM_speed_minute, MD_speed_minute, PM_speed_minute, NT_speed_minute):
        RoadSegInrCapacFlow.__init__(self, tmc, road_num, shape_length, day, \
				 AB_AM_capac, AB_MD_capac, AB_PM_capac, AB_NT_capac, \
				 AM_ave_speed, MD_ave_speed, PM_ave_speed, NT_ave_speed)
	self.AM_speed_minute = AM_speed_minute
	self.MD_speed_minute = MD_speed_minute
	self.PM_speed_minute = PM_speed_minute
	self.NT_speed_minute = NT_speed_minute
    def AM_flow_minute(self):
	AM_flow_minute_list = []
	for i in range(len(self.AM_speed_minute)):
	    AM_flow_minute_list.append(speed_to_flow(self.AB_AM_capac, tmc_ref_speed_dict_ext[self.tmc], self.AM_speed_minute[i]))
	return AM_flow_minute_list
    def MD_flow_minute(self):
	MD_flow_minute_list = []
	for i in range(len(self.MD_speed_minute)):
	    MD_flow_minute_list.append(speed_to_flow(self.AB_MD_capac, tmc_ref_speed_dict_ext[self.tmc], self.MD_speed_minute[i]))
	return MD_flow_minute_list
    def PM_flow_minute(self):
	PM_flow_minute_list = []
	for i in range(len(self.PM_speed_minute)):
	    PM_flow_minute_list.append(speed_to_flow(self.AB_PM_capac, tmc_ref_speed_dict_ext[self.tmc], self.PM_speed_minute[i]))
	return PM_flow_minute_list
    def NT_flow_minute(self):
	NT_flow_minute_list = []
	for i in range(len(self.NT_speed_minute)):
	    NT_flow_minute_list.append(speed_to_flow(self.AB_NT_capac, tmc_ref_speed_dict_ext[self.tmc], self.NT_speed_minute[i]))
	return NT_flow_minute_list

# define a road link class
class Link(object):
    def __init__(self, init_node, term_node, tmc_set, AM_capac, MD_capac, \
			PM_capac, NT_capac, free_flow_time, length, \
			AM_flow, MD_flow, PM_flow, NT_flow):
	self.init_node = init_node
        self.term_node = term_node
        self.tmc_set = tmc_set
        self.AM_capac = AM_capac
        self.MD_capac = MD_capac
        self.PM_capac = PM_capac
        self.NT_capac = NT_capac
        self.free_flow_time = free_flow_time
	self.length = length
        self.AM_flow = AM_flow
        self.MD_flow = MD_flow
        self.PM_flow = PM_flow
        self.NT_flow = NT_flow

# define a road link class that is a derived class of Link
class Link_with_Free_Flow_Time(Link):
    def __init__(self, init_node, term_node, tmc_set, AM_capac, MD_capac, \
			PM_capac, NT_capac, free_flow_time, length, \
			AM_flow, MD_flow, PM_flow, NT_flow):
	Link.__init__(self, init_node, term_node, tmc_set, AM_capac, MD_capac, \
                      PM_capac, NT_capac, free_flow_time, length, \
                      AM_flow, MD_flow, PM_flow, NT_flow)
	# notice that the original length is in meters, and the speed is in mph; we calculate the time in hours
        self.free_flow_time = sum([0.000621371 * tmc_length_dict[i] / tmc_ref_speed_dict[i] for i in self.tmc_set])
	self.length = 0.000621371 * sum([tmc_length_dict[i] for i in self.tmc_set])  # in miles

# define a road link class that is a derived class of Link, for the extended map
class Link_with_Free_Flow_Time_Ext(Link):
    def __init__(self, init_node, term_node, tmc_set, AM_capac, MD_capac, \
			PM_capac, NT_capac, free_flow_time, length, \
			AM_flow, MD_flow, PM_flow, NT_flow):
	Link.__init__(self, init_node, term_node, tmc_set, AM_capac, MD_capac, \
                      PM_capac, NT_capac, free_flow_time, length, \
                      AM_flow, MD_flow, PM_flow, NT_flow)
	# notice that the original length is in meters, and the speed is in mph; we calculate the time in hours
        self.free_flow_time = sum([0.000621371 * tmc_length_dict_ext[i] / tmc_ref_speed_dict_ext[i] for i in self.tmc_set])
	self.length = 0.000621371 * sum([tmc_length_dict_ext[i] for i in self.tmc_set])  # in miles

# define a road link class that is a derived class of Link, containing "instaneous" flow (for each minute) info 
class Link_with_Free_Flow_Time_Minute(Link_with_Free_Flow_Time):
    def __init__(self, init_node, term_node, tmc_set, AM_capac, MD_capac, \
			PM_capac, NT_capac, free_flow_time, length, \
			AM_flow, MD_flow, PM_flow, NT_flow, \
			AM_flow_minute, MD_flow_minute, \
			PM_flow_minute, NT_flow_minute):
	Link_with_Free_Flow_Time.__init__(self, init_node, term_node, tmc_set, AM_capac, MD_capac, \
                      PM_capac, NT_capac, free_flow_time, length, \
                      AM_flow, MD_flow, PM_flow, NT_flow)
	self.AM_flow_minute = AM_flow_minute
	self.MD_flow_minute = MD_flow_minute
	self.PM_flow_minute = PM_flow_minute
	self.NT_flow_minute = NT_flow_minute

# define a road link class that is a derived class of Link, containing "instaneous" flow (for each minute) info,
# for the extended map 
class Link_with_Free_Flow_Time_Minute_Ext(Link_with_Free_Flow_Time_Ext):
    def __init__(self, init_node, term_node, tmc_set, AM_capac, MD_capac, \
			PM_capac, NT_capac, free_flow_time, length, \
			AM_flow, MD_flow, PM_flow, NT_flow, \
			AM_flow_minute, MD_flow_minute, \
			PM_flow_minute, NT_flow_minute):
	Link_with_Free_Flow_Time_Ext.__init__(self, init_node, term_node, tmc_set, AM_capac, MD_capac, \
                      PM_capac, NT_capac, free_flow_time, length, \
                      AM_flow, MD_flow, PM_flow, NT_flow)
	self.AM_flow_minute = AM_flow_minute
	self.MD_flow_minute = MD_flow_minute
	self.PM_flow_minute = PM_flow_minute
	self.NT_flow_minute = NT_flow_minute

# define a road link class that is a derived class of Link, containing sensitivity analysis info 
class Link_with_Sensitivity(Link_with_Free_Flow_Time):
    def __init__(self, init_node, term_node, tmc_set, AM_capac, MD_capac, \
			PM_capac, NT_capac, free_flow_time, length, \
			AM_flow, MD_flow, PM_flow, NT_flow, \
			fcoeffs):
	Link_with_Free_Flow_Time.__init__(self, init_node, term_node, tmc_set, AM_capac, MD_capac, \
                      PM_capac, NT_capac, free_flow_time, length, \
                      AM_flow, MD_flow, PM_flow, NT_flow)
    	self.fcoeffs = fcoeffs  # fcoeffs is the coefficients of the polynomial function g(.)
    def DV_Dc_0a(self):
	n = len(self.fcoeffs)
	term_list = []
	for i in range(n):
	    term_list.append((1.0 / (i+1)) * self.fcoeffs[i] * (self.PM_flow / self.PM_capac) ** (i+1))
	return self.PM_capac * sum(term_list)

    def DV_Dm_a(self):
	n = len(self.fcoeffs)
	term_list = []
	for i in range(n)[1:]:
	    term_list.append((float(i) / (i+1)) * self.fcoeffs[i] * (self.PM_flow / self.PM_capac) ** (i+1))
	# print(term_list)  # for debugging purpose only
	return - self.free_flow_time * sum(term_list)
