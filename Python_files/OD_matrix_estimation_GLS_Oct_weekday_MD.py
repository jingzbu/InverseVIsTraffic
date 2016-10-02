#!/usr/bin/env python


__author__ = "Jing Zhang"
__email__ = "jingzbu@gmail.com"
__status__ = "Development"


from util import *

import numpy as np
from numpy.linalg import inv
import json

# load logit_route_choice_probability_matrix
P = zload('../temp_files/logit_route_choice_probability_matrix.pkz')
P = np.matrix(P)

# print(np.size(P,0), np.size(P,1))

# load path-link incidence matrix
A = zload('../temp_files/path-link_incidence_matrix.pkz')

# load link counts data
with open('../temp_files/link_day_minute_Oct_dict_JSON.json', 'r') as json_file:
    link_day_minute_Oct_dict_JSON = json.load(json_file)

week_day_Oct_list = [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 29, 30, 31]

link_day_minute_Oct_list = []
for link_idx in range(24):
    for day in week_day_Oct_list: 
        for minute_idx in range(120):
            key = 'link_' + str(link_idx) + '_' + str(day)
            link_day_minute_Oct_list.append(link_day_minute_Oct_dict_JSON[key] ['MD_flow_minute'][minute_idx])

# print(len(link_day_minute_Oct_list))

x = np.matrix(link_day_minute_Oct_list)
x = np.matrix.reshape(x, 24, 2760)

x = np.nan_to_num(x)
y = np.array(np.transpose(x))
y = y[np.all(y != 0, axis=1)]
x = np.transpose(y)
x = np.matrix(x)

# print(np.size(x,0), np.size(x,1))
# print(x[:,:2])
# print(np.size(A,0), np.size(A,1))

L = 56  # dimension of lam

lam_list = GLS(x, A, P, L)
lam_dict = {}

# write estimation result to file
n = 8  # number of nodes
with open('../temp_files/OD_demand_matrix_Oct_weekday_MD.txt', 'w') as the_file:
    idx = 0
    for i in range(n + 1)[1:]:
        for j in range(n + 1)[1:]:
            if i != j: 
		key = str(idx)
		lam_dict[key] = lam_list[idx]
                the_file.write("%d,%d,%f\n" %(i, j, lam_list[idx]))
                idx += 1

with open('../temp_files/OD_demand_matrix_Oct_weekday_MD.json', 'w') as json_file:
    json.dump(lam_dict, json_file)
