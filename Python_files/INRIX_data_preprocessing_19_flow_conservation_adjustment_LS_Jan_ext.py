#!/usr/bin/env python


__author__ = "Jing Zhang"
__email__ = "jingzbu@gmail.com"
__status__ = "Development"


from util import *

import numpy as np
from numpy.linalg import inv

# load the original link counts data

import json

with open('../temp_files/link_day_minute_Jan_dict_ext_JSON.json', 'r') as json_file:
    link_day_minute_Jan_dict_JSON = json.load(json_file)

AM_flow_list = []
MD_flow_list = []
PM_flow_list = []
NT_flow_list = []
AM_flow_minute_list = []
MD_flow_minute_list = []
PM_flow_minute_list = []
NT_flow_minute_list = []
for link_idx in range(64):
    for day in range(32)[1:]: 
        key = 'link_' + str(link_idx) + '_' + str(day)
        AM_flow_list.append(link_day_minute_Jan_dict_JSON[key] ['AM_flow'])
        MD_flow_list.append(link_day_minute_Jan_dict_JSON[key] ['MD_flow'])
        PM_flow_list.append(link_day_minute_Jan_dict_JSON[key] ['PM_flow'])
        NT_flow_list.append(link_day_minute_Jan_dict_JSON[key] ['NT_flow'])
        for minute_idx in range(120):
            AM_flow_minute_list.append(link_day_minute_Jan_dict_JSON[key] ['AM_flow_minute'][minute_idx])
            MD_flow_minute_list.append(link_day_minute_Jan_dict_JSON[key] ['MD_flow_minute'][minute_idx])
            PM_flow_minute_list.append(link_day_minute_Jan_dict_JSON[key] ['PM_flow_minute'][minute_idx])
            NT_flow_minute_list.append(link_day_minute_Jan_dict_JSON[key] ['NT_flow_minute'][minute_idx])

x_AM_flow = np.matrix(AM_flow_list)
x_AM_flow = np.matrix.reshape(x_AM_flow, 64, 31)
x_AM_flow = np.nan_to_num(x_AM_flow)

x_MD_flow = np.matrix(MD_flow_list)
x_MD_flow = np.matrix.reshape(x_MD_flow, 64, 31)
x_MD_flow = np.nan_to_num(x_MD_flow)

x_PM_flow = np.matrix(PM_flow_list)
x_PM_flow = np.matrix.reshape(x_PM_flow, 64, 31)
x_PM_flow = np.nan_to_num(x_PM_flow)

x_NT_flow = np.matrix(NT_flow_list)
x_NT_flow = np.matrix.reshape(x_NT_flow, 64, 31)
x_NT_flow = np.nan_to_num(x_NT_flow)

x_AM_flow_minute = np.matrix(AM_flow_minute_list)
x_AM_flow_minute = np.matrix.reshape(x_AM_flow_minute, 64, 3720)
x_AM_flow_minute = np.nan_to_num(x_AM_flow_minute)

x_MD_flow_minute = np.matrix(MD_flow_minute_list)
x_MD_flow_minute = np.matrix.reshape(x_MD_flow_minute, 64, 3720)
x_MD_flow_minute = np.nan_to_num(x_MD_flow_minute)

x_PM_flow_minute = np.matrix(PM_flow_minute_list)
x_PM_flow_minute = np.matrix.reshape(x_PM_flow_minute, 64, 3720)
x_PM_flow_minute = np.nan_to_num(x_PM_flow_minute)

x_NT_flow_minute = np.matrix(NT_flow_minute_list)
x_NT_flow_minute = np.matrix.reshape(x_NT_flow_minute, 64, 3720)
x_NT_flow_minute = np.nan_to_num(x_NT_flow_minute)

print(link_day_minute_Jan_dict_JSON['link_0_1'] ['AM_flow_minute'][0])

y_AM_flow = []
y_MD_flow = []
y_PM_flow = []
y_NT_flow = []

for j in range(np.size(x_AM_flow, 1)):
    y_AM_flow_0 = x_AM_flow[:,j]  # initial flow vector
    y_MD_flow_0 = x_MD_flow[:,j]  # initial flow vector
    y_PM_flow_0 = x_PM_flow[:,j]  # initial flow vector
    y_NT_flow_0 = x_NT_flow[:,j]  # initial flow vector

    y_AM_flow.append(flow_conservation_adjustment_ext(y_AM_flow_0))
    y_MD_flow.append(flow_conservation_adjustment_ext(y_MD_flow_0))
    y_PM_flow.append(flow_conservation_adjustment_ext(y_PM_flow_0))
    y_NT_flow.append(flow_conservation_adjustment_ext(y_NT_flow_0))

y_AM_flow_minute = []
y_MD_flow_minute = []
y_PM_flow_minute = []
y_NT_flow_minute = []

for j in range(np.size(x_AM_flow_minute, 1)):
    y_AM_flow_minute_0 = x_AM_flow_minute[:,j]  # initial flow vector
    y_MD_flow_minute_0 = x_MD_flow_minute[:,j]  # initial flow vector
    y_PM_flow_minute_0 = x_PM_flow_minute[:,j]  # initial flow vector
    y_NT_flow_minute_0 = x_NT_flow_minute[:,j]  # initial flow vector

    y_AM_flow_minute.append(flow_conservation_adjustment_ext(y_AM_flow_minute_0))
    y_MD_flow_minute.append(flow_conservation_adjustment_ext(y_MD_flow_minute_0))
    y_PM_flow_minute.append(flow_conservation_adjustment_ext(y_PM_flow_minute_0))
    y_NT_flow_minute.append(flow_conservation_adjustment_ext(y_NT_flow_minute_0))

y_AM_flow = np.matrix(y_AM_flow)
y_AM_flow = np.matrix.transpose(y_AM_flow)

y_MD_flow = np.matrix(y_MD_flow)
y_MD_flow = np.matrix.transpose(y_MD_flow)

y_PM_flow = np.matrix(y_PM_flow)
y_PM_flow = np.matrix.transpose(y_PM_flow)

y_NT_flow = np.matrix(y_NT_flow)
y_NT_flow = np.matrix.transpose(y_NT_flow)

y_AM_flow_minute = np.matrix(y_AM_flow_minute)
y_AM_flow_minute = np.matrix.transpose(y_AM_flow_minute)

y_MD_flow_minute = np.matrix(y_MD_flow_minute)
y_MD_flow_minute = np.matrix.transpose(y_MD_flow_minute)

y_PM_flow_minute = np.matrix(y_PM_flow_minute)
y_PM_flow_minute = np.matrix.transpose(y_PM_flow_minute)

y_NT_flow_minute = np.matrix(y_NT_flow_minute)
y_NT_flow_minute = np.matrix.transpose(y_NT_flow_minute)

link_day_minute_Jan_dict_JSON_adjusted = {}

for link_idx in range(64):
    AM_flow = np.matrix.reshape(y_AM_flow[link_idx,:], 31, 1)
    MD_flow = np.matrix.reshape(y_MD_flow[link_idx,:], 31, 1)
    PM_flow = np.matrix.reshape(y_PM_flow[link_idx,:], 31, 1)
    NT_flow = np.matrix.reshape(y_NT_flow[link_idx,:], 31, 1)
    AM_flow_minute = np.matrix.reshape(y_AM_flow_minute[link_idx,:], 31, 120)
    MD_flow_minute = np.matrix.reshape(y_MD_flow_minute[link_idx,:], 31, 120)
    PM_flow_minute = np.matrix.reshape(y_PM_flow_minute[link_idx,:], 31, 120)
    NT_flow_minute = np.matrix.reshape(y_NT_flow_minute[link_idx,:], 31, 120)

    for day in range(32)[1:]:   
        key = 'link_' + str(link_idx) + '_' + str(day)
        data = {'link_idx': link_idx, 'day': day, \
             'init_node': link_day_minute_Jan_dict_JSON[key]['init_node'], \
             'term_node': link_day_minute_Jan_dict_JSON[key]['term_node'], \
             'AM_capac': link_day_minute_Jan_dict_JSON[key]['AM_capac'], \
             'MD_capac': link_day_minute_Jan_dict_JSON[key]['MD_capac'], \
             'PM_capac': link_day_minute_Jan_dict_JSON[key]['PM_capac'], \
             'NT_capac': link_day_minute_Jan_dict_JSON[key]['NT_capac'], \
             'free_flow_time': link_day_minute_Jan_dict_JSON[key]['free_flow_time'], \
             'length': link_day_minute_Jan_dict_JSON[key]['length'], \
             'AM_flow': np.array(AM_flow)[day-1].tolist()[0], \
             'MD_flow': np.array(AM_flow)[day-1].tolist()[0], \
             'PM_flow': np.array(AM_flow)[day-1].tolist()[0], \
             'NT_flow': np.array(AM_flow)[day-1].tolist()[0], \
             'AM_flow_minute': np.array(AM_flow_minute)[day-1].tolist(), \
             'MD_flow_minute': np.array(MD_flow_minute)[day-1].tolist(), \
             'PM_flow_minute': np.array(PM_flow_minute)[day-1].tolist(), \
             'NT_flow_minute': np.array(NT_flow_minute)[day-1].tolist()}
        link_day_minute_Jan_dict_JSON_adjusted[key] = data

# Writing JSON data
with open('../temp_files/link_day_minute_Jan_dict_ext_JSON_adjusted.json', 'w') as json_file:
    json.dump(link_day_minute_Jan_dict_JSON_adjusted, json_file)
