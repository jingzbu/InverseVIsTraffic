from util import *
import numpy as np
from numpy.linalg import inv
import json

# load link counts data
with open('../temp_files/link_day_minute_Apr_dict_ext_JSON_insert_links_adjusted.json', 'r') as json_file:
    link_day_minute_Apr_dict_JSON = json.load(json_file)

week_day_Apr_list = [2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20, 23, 24, 25, 26, 27, 30]

link_day_minute_Apr_list = []
for link_idx in range(74):
    for day in week_day_Apr_list: 
        for minute_idx in range(120):
            key = 'link_' + str(link_idx) + '_' + str(day)
            link_day_minute_Apr_list.append(link_day_minute_Apr_dict_JSON[key] ['PM_flow_minute'][minute_idx])

# print(len(link_day_minute_Apr_list))

x = np.matrix(link_day_minute_Apr_list)
x = np.matrix.reshape(x, 74, 2520)

x = np.nan_to_num(x)
y = np.array(np.transpose(x))
y = y[np.all(y != 0, axis=1)]
x = np.transpose(y)
x = np.matrix(x)

link_day_Apr_list = []
for link_idx in range(74):
    for day in range(31)[1:]: 
        key = 'link_' + str(link_idx) + '_' + str(day)
        link_day_Apr_list.append(link_day_minute_Apr_dict_JSON[key] ['PM_flow'])

# print(len(link_day_minute_Apr_list))

x_ = np.matrix(link_day_Apr_list)
x_ = np.matrix.reshape(x_, 74, 30)

x_ = np.nan_to_num(x_)
y_ = np.array(np.transpose(x_))
y_ = y_[np.all(y_ != 0, axis=1)]
x_ = np.transpose(y_)
x_ = np.matrix(x_)
