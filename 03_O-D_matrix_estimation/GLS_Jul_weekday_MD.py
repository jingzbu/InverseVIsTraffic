from util import *

# implement GLS method to estimate OD demand matrix
def GLS(x, A, L):
    """
    x: sample matrix, each column is a link flow vector sample; 24 * K
    A: path-link incidence matrix
    P: logit route choice probability matrix
    L: dimension of xi
    ----------------
    return: xi
    ----------------
    """
    K = np.size(x, 1)
    S = samp_cov(x)

    #print("rank of S is: \n")
    #print(matrix_rank(S))
    #print("sizes of S are: \n")
    #print(np.size(S, 0))
    #print(np.size(S, 1))

    inv_S = inv(S).real

    A_t = np.transpose(A)

    Q_ = np.dot(np.dot(A_t, inv_S), A)
    #Q = adj_PSD(Q_).real  # Ensure Q to be PSD
    Q = Q_

    #print("rank of Q is: \n")
    #print(matrix_rank(Q))
    #print("sizes of Q are: \n")
    #print(np.size(Q, 0))
    #print(np.size(Q, 1))

    b = sum([np.dot(np.dot(A_t, inv_S), x[:, k]) for k in range(K)])
    # print(b[0])
    # assert(1==2)

    model = Model("OD_matrix_estimation")

    xi = []
    for l in range(L):
        xi.append(model.addVar(name='xi_' + str(l)))

    model.update() 

    # Set objective: (K/2) xi' * Q * xi - b' * xi
    obj = 0
    for i in range(L):
        for j in range(L):
            obj += (1.0 / 2) * K * xi[i] * Q[i, j] * xi[j]
    for l in range(L):
        obj += - b[l] * xi[l]
    model.setObjective(obj)

    # Add constraint: xi >= 0
    for l in range(L):
        model.addConstr(xi[l] >= 0)
        #model.addConstr(xi[l] <= 5000)
    #fictitious_OD_list = zload('../temp_files/fictitious_OD_list')
    #for l in fictitious_OD_list:
        #model.addConstr(xi[l] == 0)
    model.update() 

    model.setParam('OutputFlag', False)
    model.optimize()

    xi_list = []
    for v in model.getVars():
        # print('%s %g' % (v.varName, v.x))
        xi_list.append(v.x)
    # print('Obj: %g' % obj.getValue())
    return xi_list

import numpy as np
from numpy.linalg import inv
import json

# load logit_route_choice_probability_matrix
P = zload('../temp_files/OD_pair_route_incidence_MA.pkz')
P = np.matrix(P)

# print(np.size(P,0), np.size(P,1))

# load path-link incidence matrix
A = zload('../temp_files/path-link_incidence_matrix_MA.pkz')

# load link counts data
with open('../temp_files/link_day_minute_Jul_dict_JSON.json', 'r') as json_file:
    link_day_minute_Jul_dict_JSON = json.load(json_file)

week_day_Jul_list = [2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20, 23, 24, 25, 26, 27, 30, 31]


link_day_minute_Jul_list = []
for link_idx in range(24):
    for day in week_day_Jul_list: 
        for minute_idx in range(120):
            key = 'link_' + str(link_idx) + '_' + str(day)
            link_day_minute_Jul_list.append(link_day_minute_Jul_dict_JSON[key] ['MD_flow_minute'][minute_idx])

# print(len(link_day_minute_Jul_list))

x = np.matrix(link_day_minute_Jul_list)
x = np.matrix.reshape(x, 24, 2640)

x = np.nan_to_num(x)
y = np.array(np.transpose(x))
y = y[np.all(y != 0, axis=1)]
x = np.transpose(y)
x = np.matrix(x)

# print(np.size(x,0), np.size(x,1))
# print(x[:,:2])
# print(np.size(A,0), np.size(A,1))

L = np.size(P,1)  # dimension of xi

xi_list = GLS(x, A, L)

# write estimation result to file
def saveDemandVec(lam_list):
    lam_dict = {}
    n = 8  # number of nodes
    with open('../temp_files/OD_demand_matrix_Jul_weekday_MD.txt', 'w') as the_file:
        idx = 0
        for i in range(n + 1)[1:]:
            for j in range(n + 1)[1:]:
                if i != j: 
                    key = str(idx)
                    lam_dict[key] = lam_list[idx]
                    the_file.write("%d,%d,%f\n" %(i, j, lam_list[idx]))
                    idx += 1

    with open('../temp_files/OD_demand_matrix_Jul_weekday_MD.json', 'w') as json_file:
        json.dump(lam_dict, json_file)
