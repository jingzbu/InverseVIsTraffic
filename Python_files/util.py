from util_data_storage_and_load import *


try:
    from load_dicts import tmc_length_dict, tmc_ref_speed_dict
except ImportError:
    print "No dicts found; please check load_dicts..."

# define a function converting speed to flow, based on Greenshield's model
def speed_to_flow(capac, ref_speed, speed):
    free_speed = ref_speed
    if speed > free_speed:
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

from gurobipy import *

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
