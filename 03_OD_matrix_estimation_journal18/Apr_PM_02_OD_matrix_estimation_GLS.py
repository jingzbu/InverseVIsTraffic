from util import *
from util_data_storage_and_load import *
import numpy as np
from numpy.linalg import inv
from scipy.sparse import csr_matrix, csc_matrix
import json

with open('../temp_files/new_route_dict_journal.json', 'r') as json_file:
    new_route_dict = json.load(json_file)

number_of_routes = len(new_route_dict)

link_label_dict = zload('../temp_files/link_label_dict_journal.pkz')

number_of_links = len(link_label_dict)

# implement GLS method to estimate OD demand matrix
def GLS(x, A, L):
    """
    x: sample matrix, each column is a link flow vector sample; number_of_links * K
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

    A_t = A.transpose()

    Q_ = A_t * inv_S * A
    Q_ = Q_.real
    #Q = adj_PSD(Q_).real  # Ensure Q to be PSD
    Q = Q_

    #print("rank of Q is: \n")
    #print(matrix_rank(Q))
    #print("sizes of Q are: \n")
    #print(np.size(Q, 0))
    #print(np.size(Q, 1))

    b = sum([A_t * inv_S * x[:, k] for k in range(K)])
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

    #model.setParam('OutputFlag', False)
    model.optimize()

    xi_list = []
    for v in model.getVars():
        # print('%s %g' % (v.varName, v.x))
        xi_list.append(v.x)
    # print('Obj: %g' % obj.getValue())
    return xi_list

# implement GLS method to estimate OD demand matrix
def GLS_with_known_P(x, A, P, L):
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

    A_t = A.transpose()
    P_t = P.transpose()

    # PA'
    PA_t = P * A_t

    # AP_t
    AP_t = PA_t.transpose()

    Q_ = PA_t * inv_S * AP_t
    Q_ = Q_.real
    #Q = adj_PSD(Q_).real  # Ensure Q to be PSD
    Q = Q_

    b = sum([PA_t * inv_S * x[:, k] for k in range(K)])


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

# load link_route incidence matrix
A = zload('../temp_files/link_route_incidence_matrix_journal.pkz')
A = A.todense()

# load link counts data
with open('../temp_files/link_day_minute_Apr_dict_journal_JSON.json', 'r') as json_file:
    link_day_minute_Apr_dict_JSON = json.load(json_file)

week_day_Apr_list = [2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20, 23, 24, 25, 26, 27, 30]
# week_day_Apr_list = [9, 10, 11, 12, 13]

feasible_link_dict = zload('../temp_files/feasible_link_dict_journal.pkz')

link_day_minute_Apr_list = []
for link_idx in [feasible_link_dict[idx] for idx in range(len(feasible_link_dict))]:
    for day in week_day_Apr_list:
        for minute_idx in range(120):
            key = 'link_' + str(link_idx) + '_' + str(day)
            link_day_minute_Apr_list.append(link_day_minute_Apr_dict_JSON[key] ['PM_flow_minute'][minute_idx])

x = np.matrix(link_day_minute_Apr_list)
x = np.matrix.reshape(x, len(feasible_link_dict), 2520)
# x = np.matrix.reshape(x, len(feasible_link_dict), 600)

# print(np.size(x,0), np.size(x,1))

x = np.nan_to_num(x)
# print(np.size(x,0), np.size(x,1))

# y = np.array(np.transpose(x))
# y = y[np.all(y != 0, axis=1)]
# x = np.transpose(y)
# x = np.matrix(x)

# print(np.size(x,0), np.size(x,1))
# print(x[:,:2])
# print(np.size(A,0), np.size(A,1))

# load logit_route_choice_probability_matrix
P = zload('../temp_files/OD_pair_route_incidence_journal.pkz')
P = P.todense()

L = np.size(P, 1)  # dimension of xi
assert(L == number_of_routes)

# xi_list = GLS(x, A, number_of_routes)
lam_list = GLS_with_known_P(x, A, P, number_of_routes)
