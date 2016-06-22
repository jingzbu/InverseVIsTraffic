#!/usr/bin/env python


__author__ = "Jing Zhang"
__email__ = "jingzbu@gmail.com"
__status__ = "Development"


from util import *
import numpy as np
from numpy.linalg import inv, matrix_rank
import json

# load logit_route_choice_probability_matrix
P = zload('../temp_files/logit_route_choice_probability_matrix_ext.pkz')
P = np.matrix(P)

# print(matrix_rank(P))


# print(np.size(P,0), np.size(P,1))

# load path-link incidence matrix
A = zload('../temp_files/path-link_incidence_matrix_ext.pkz')

# assert(1 == 2)

# load link counts data
with open('../temp_files/link_day_minute_Apr_dict_ext_JSON_insert_links_adjusted.json', 'r') as json_file:
    link_day_minute_Apr_dict_ext_JSON = json.load(json_file)

# week_day_Apr_list = [2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 16, 22, 18, 19, 20, 23, 24, 25, 26, 27, 30]
week_day_Apr_list = [10, 11, 12, 13, 16]

link_day_minute_Apr_list = []
for link_idx in range(74):
    for day in week_day_Apr_list: 
        for minute_idx in range(120):
            key = 'link_' + str(link_idx) + '_' + str(day)
            link_day_minute_Apr_list.append(link_day_minute_Apr_dict_ext_JSON[key] ['AM_flow_minute'][minute_idx])

# print(len(link_day_minute_Apr_list))

x = np.matrix(link_day_minute_Apr_list)
x = np.matrix.reshape(x, 74, 600)

x = np.nan_to_num(x)
y = np.array(np.transpose(x))
y = y[np.all(y != 0, axis=1)]
x = np.transpose(y)
x = np.matrix(x)

# print(np.size(x,0), np.size(x,1))
# print(x[:,:2])
# print(np.size(A,0), np.size(A,1))

L = 22 * (22 - 1)  # dimension of lam

# implement GLS method to estimate OD demand matrix
def GLS_Apr(x, A, P, L):
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

    #print("rank of S is: \n")
    #print(matrix_rank(S))
    #print("sizes of S are: \n")
    #print(np.size(S, 0))
    #print(np.size(S, 1))

    inv_S = inv(S).real

    A_t = np.transpose(A)
    P_t = np.transpose(P)
    # PA'
    PA_t = np.dot(P, A_t)

    #print("rank of PA_t is: \n")
    #print(matrix_rank(PA_t))
    #print("sizes of PA_t are: \n")
    #print(np.size(PA_t, 0))
    #print(np.size(PA_t, 1))

    # AP_t
    AP_t = np.transpose(PA_t)

    Q_ = np.dot(np.dot(PA_t, inv_S), AP_t)
    # Q = adj_PSD(Q_).real  # Ensure Q to be PSD
    Q = Q_

    #print("rank of Q is: \n")
    #print(matrix_rank(Q))
    #print("sizes of Q are: \n")
    #print(np.size(Q, 0))
    #print(np.size(Q, 1))

    b = sum([np.dot(np.dot(PA_t, inv_S), x[:, k]) for k in range(K)])
    # print(b[0])
    # assert(1==2)

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
	model.addConstr(lam[l] <= 5000)
    #fictitious_OD_list = zload('../temp_files/fictitious_OD_list')
    #for l in fictitious_OD_list:
	#model.addConstr(lam[l] == 0)
    model.update() 

    model.setParam('OutputFlag', False)
    model.optimize()

    lam_list = []
    for v in model.getVars():
        # print('%s %g' % (v.varName, v.x))
        lam_list.append(v.x)
    # print('Obj: %g' % obj.getValue())
    return lam_list

lam_list = GLS_Apr(x, A, P, L)

# write estimation result to file
n = 22  # number of nodes
with open('../temp_files/OD_demand_matrix_Apr_weekday_AM_ext.txt', 'w') as the_file:
    idx = 0
    for i in range(n + 1)[1:]:
        for j in range(n + 1)[1:]:
            if i != j: 
                the_file.write("%d,%d,%f\n" %(i, j, lam_list[idx]))
                idx += 1
