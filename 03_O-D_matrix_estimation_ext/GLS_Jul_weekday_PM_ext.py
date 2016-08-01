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
with open('../temp_files/link_day_minute_Jul_dict_ext_JSON_insert_links_adjusted.json', 'r') as json_file:
    link_day_minute_Jul_dict_ext_JSON = json.load(json_file)

# week_day_Jul_list = [2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 16, 22, 18, 19, 20, 23, 24, 25, 26, 27, 30, 31]
week_day_Jul_list = [2, 3, 4, 5, 6, 9]

link_day_minute_Jul_list = []
for link_idx in range(74):
    for day in week_day_Jul_list: 
        for minute_idx in range(120):
            key = 'link_' + str(link_idx) + '_' + str(day)
            link_day_minute_Jul_list.append(link_day_minute_Jul_dict_ext_JSON[key] ['PM_flow_minute'][minute_idx])

# print(len(link_day_minute_Jul_list))

x = np.matrix(link_day_minute_Jul_list)
x = np.matrix.reshape(x, 74, 720)
x[x < 1] = 200
# x = np.nan_to_num(x)
# y = np.array(np.transpose(x))
# y = y[np.all(y != 0, axis=1)]
# x = np.transpose(y)
# x = np.matrix(x)

# print(np.size(x,0), np.size(x,1))
# print(x[:,:2])
# print(np.size(A,0), np.size(A,1))

# load node-link incidence matrix
N = zload('../temp_files/node_link_incidence_MA_ext.pkz')

N.shape

n = 22  # number of nodes
m = 74  # number of links

x_0 = [x[:,2][i, 0] for i in range(m)]

# x_0

OD_pair_label_dict = zload('../temp_files/OD_pair_label_dict_ext.pkz')

len(OD_pair_label_dict)

L = 22 * (22 - 1)  # dimension of lam

# od pair correspondence
OD_pair_label_dict_MA_small = zload('../temp_files/OD_pair_label_dict__MA.pkz')

# create a dictionary mapping nodes of small network to nodes of bigger network
nodeToNode = {}

nodeList = range(9)[1:]
nodeListExt = [1, 4, 7, 12, 13, 14, 16, 17]
for i in nodeList:
    nodeToNode[str(i)] = nodeListExt[i-1]
# nodeToNode['1'] = 1
# nodeToNode['2']

nodeToNode

odMap = {}
for i in range(len(OD_pair_label_dict_MA_small)):
    key = str(i)
    origiSmall = OD_pair_label_dict_MA_small[key][0]
    destiSmall = OD_pair_label_dict_MA_small[key][1]
    origiExt = nodeToNode[str(origiSmall)]
    destiExt = nodeToNode[str(destiSmall)]
    odMap[key] = (origiExt, destiExt)

# odMap

odIdxExt = []  # OD pair idx in the extended network corresponding to the OD pairs in smaller network

for i in range(len(odMap)):
    odIdxExt.append(OD_pair_label_dict[str(odMap[str(i)])])

with open('../temp_files/OD_demand_matrix_Jul_weekday_PM.json', 'r') as json_file:
    demandsSmall = json.load(json_file)

fictitious_OD_list = zload('../temp_files/fictitious_OD_list')

# demandsSmall

# implement GLS method to estimate OD demand matrix
def GLS_Jul(x, A, P, L):
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

    inv_S = inv(S).real

    A_t = np.transpose(A)
    P_t = np.transpose(P)
    # PA'
    PA_t = np.dot(P, A_t)

    # AP_t
    AP_t = np.transpose(PA_t)

    Q_ = np.dot(np.dot(PA_t, inv_S), AP_t)
    Q = adj_PSD(Q_).real  # Ensure Q to be PSD
#     Q = Q_

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
        #model.addConstr(lam[l] <= 5000)
    fictitious_OD_list = zload('../temp_files/fictitious_OD_list')
    for l in fictitious_OD_list:
        model.addConstr(lam[l] == 0)
        
    for j in range(len(odMap)):
        model.addConstr(lam[odIdxExt[j]] - demandsSmall[str(j)] <= 0.2 * demandsSmall[str(j)])
        model.addConstr(demandsSmall[str(j)] - lam[odIdxExt[j]] <= 0.2 * demandsSmall[str(j)])

    model.update() 

    model.setParam('OutputFlag', False)
    model.optimize()

    lam_list = []
    for v in model.getVars():
        # print('%s %g' % (v.varName, v.x))
        lam_list.append(v.x)
    # print('Obj: %g' % obj.getValue())
    return lam_list

# lam_list = GLS_Jul(x, A, P, L)

# # write estimation result to file
# n = 22  # number of nodes
# with open('../temp_files/OD_demand_matrix_Jul_weekday_PM_ext.txt', 'w') as the_file:
#     idx = 0
#     for i in range(n + 1)[1:]:
#         for j in range(n + 1)[1:]:
#             if i != j: 
#                 the_file.write("%d,%d,%f\n" %(i, j, lam_list[idx]))
#                 idx += 1

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

    inv_S = inv(S).real

    A_t = np.transpose(A)

    Q_ = np.dot(np.dot(A_t, inv_S), A)
    Q = adj_PSD(Q_).real  # Ensure Q to be PSD
    Q = Q_

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

    model.update() 

    # model.setParam('OutputFlag', False)
    model.optimize()

    xi_list = []
    for v in model.getVars():
        # print('%s %g' % (v.varName, v.x))
        xi_list.append(v.x)
    # print('Obj: %g' % obj.getValue())
    return xi_list

xi_list = GLS(x, A, L)

# write estimation result to file
def saveDemandVec(lam_list):
    lam_dict = {}
    n = 22  # number of nodes
    with open('../temp_files/OD_demand_matrix_Jul_weekday_PM_ext.txt', 'w') as the_file:
        idx = 0
        for i in range(n + 1)[1:]:
            for j in range(n + 1)[1:]:
                if i != j: 
                    key = str(idx)
                    lam_dict[key] = lam_list[idx]
                    the_file.write("%d,%d,%f\n" %(i, j, lam_list[idx]))
                    idx += 1

    with open('../temp_files/OD_demand_matrix_Jul_weekday_PM_ext.json', 'w') as json_file:
        json.dump(lam_dict, json_file)
