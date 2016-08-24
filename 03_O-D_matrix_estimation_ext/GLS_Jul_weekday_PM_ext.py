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
with open('../temp_files/link_day_minute_Jul_dict_ext_JSON_insert_links.json', 'r') as json_file:
    link_day_minute_Jul_dict_ext_JSON = json.load(json_file)

# week_day_Jul_list = [2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 16, 22, 18, 19, 20, 23, 24, 25, 26, 27, 30, 31]
week_day_Jul_list = [2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 16, 22, 18, 19, 20, 23, 24, 25, 26, 27, 30]

link_day_minute_Jul_list = []
for link_idx in range(74):
    for day in week_day_Jul_list: 
        for minute_idx in range(120):
            key = 'link_' + str(link_idx) + '_' + str(day)
            link_day_minute_Jul_list.append(link_day_minute_Jul_dict_ext_JSON[key] ['PM_flow_minute'][minute_idx])

# print(len(link_day_minute_Jul_list))

x = np.matrix(link_day_minute_Jul_list)
x = np.matrix.reshape(x, 74, 2520)
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


OD_pair_label_dict_ = zload('../temp_files/OD_pair_label_dict__ext.pkz')
OD_pair_label_dict = zload('../temp_files/OD_pair_label_dict_ext.pkz')


L = 462  # dimension of xi

# od pair correspondence
OD_pair_label_dict_MA_small = zload('../temp_files/OD_pair_label_dict__MA.pkz')


with open('../temp_files/OD_demand_matrix_Jul_weekday_PM.json', 'r') as json_file:
    demandsSmall = json.load(json_file)

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
    # Q = adj_PSD(Q_).real  # Ensure Q to be PSD
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
    with open('../temp_files/OD_demand_matrix_Jul_weekday_PM_ext.txt', 'w') as the_file:
        for idx in range(len(lam_list)):
            key = str(idx)
            the_file.write("%d,%d,%f\n" %(OD_pair_label_dict_[key][0], OD_pair_label_dict_[key][1], lam_list[idx]))

    with open('../temp_files/OD_demand_matrix_Jul_weekday_PM_ext.json', 'w') as json_file:
        json.dump(lam_dict, json_file)
