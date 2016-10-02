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

#print('rank of P is: ')
#print(matrix_rank(P))


# print(np.size(P,0), np.size(P,1))

# load path-link incidence matrix
A = zload('../temp_files/path-link_incidence_matrix_ext.pkz')

#print('rank of A is: ')
#print(matrix_rank(A))
# assert(1 == 2)

# load link counts data
with open('../temp_files/link_day_minute_Jan_dict_ext_JSON_insert_links_adjusted.json', 'r') as json_file:
    link_day_minute_Jan_dict_ext_JSON = json.load(json_file)

# week_day_Jan_list = [2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20, 23, 24, 25, 26, 27, 30, 31]
week_day_Jan_list = [25, 26, 27, 30, 31]

link_day_minute_Jan_list = []
for link_idx in range(74):
    for day in week_day_Jan_list: 
        for minute_idx in range(120):
            key = 'link_' + str(link_idx) + '_' + str(day)
            link_day_minute_Jan_list.append(link_day_minute_Jan_dict_ext_JSON[key] ['AM_flow_minute'][minute_idx])

# print(len(link_day_minute_Jan_list))

x = np.matrix(link_day_minute_Jan_list)
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

lam_list = GLS(x, A, P, L)

# write estimation result to file
n = 22  # number of nodes
with open('../temp_files/OD_demand_matrix_Jan_weekday_AM_ext.txt', 'w') as the_file:
    idx = 0
    for i in range(n + 1)[1:]:
        for j in range(n + 1)[1:]:
            if i != j: 
                the_file.write("%d,%d,%f\n" %(i, j, lam_list[idx]))
                idx += 1
