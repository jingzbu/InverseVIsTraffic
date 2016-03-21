#!/usr/bin/env python


__author__ = "Jing Zhang"
__email__ = "jingzbu@gmail.com"
__status__ = "Development"


from util import *

import numpy as np
from numpy.linalg import inv

# load the original link counts data

import json

with open('../temp_files/link_day_minute_Oct_dict_JSON_adjusted.json', 'r') as json_file:
    link_day_minute_Oct_dict_JSON_adjusted = json.load(json_file)

AM_flow_list = []
MD_flow_list = []
PM_flow_list = []
NT_flow_list = []
AM_flow_minute_list = []
MD_flow_minute_list = []
PM_flow_minute_list = []
NT_flow_minute_list = []
for link_idx in range(24):
    for day in range(32)[1:]: 
        key = 'link_' + str(link_idx) + '_' + str(day)
        AM_flow_list.append(link_day_minute_Oct_dict_JSON_adjusted[key] ['AM_flow'])
        MD_flow_list.append(link_day_minute_Oct_dict_JSON_adjusted[key] ['MD_flow'])
        PM_flow_list.append(link_day_minute_Oct_dict_JSON_adjusted[key] ['PM_flow'])
        NT_flow_list.append(link_day_minute_Oct_dict_JSON_adjusted[key] ['NT_flow'])
        for minute_idx in range(120):
            AM_flow_minute_list.append(link_day_minute_Oct_dict_JSON_adjusted[key] ['AM_flow_minute'][minute_idx])
            MD_flow_minute_list.append(link_day_minute_Oct_dict_JSON_adjusted[key] ['MD_flow_minute'][minute_idx])
            PM_flow_minute_list.append(link_day_minute_Oct_dict_JSON_adjusted[key] ['PM_flow_minute'][minute_idx])
            NT_flow_minute_list.append(link_day_minute_Oct_dict_JSON_adjusted[key] ['NT_flow_minute'][minute_idx])

x_AM_flow = np.matrix(AM_flow_list)
x_AM_flow = np.matrix.reshape(x_AM_flow, 24, 31)
x_AM_flow = np.nan_to_num(x_AM_flow)

x_MD_flow = np.matrix(MD_flow_list)
x_MD_flow = np.matrix.reshape(x_MD_flow, 24, 31)
x_MD_flow = np.nan_to_num(x_MD_flow)

x_PM_flow = np.matrix(PM_flow_list)
x_PM_flow = np.matrix.reshape(x_PM_flow, 24, 31)
x_PM_flow = np.nan_to_num(x_PM_flow)

x_NT_flow = np.matrix(NT_flow_list)
x_NT_flow = np.matrix.reshape(x_NT_flow, 24, 31)
x_NT_flow = np.nan_to_num(x_NT_flow)

x_AM_flow_minute = np.matrix(AM_flow_minute_list)
x_AM_flow_minute = np.matrix.reshape(x_AM_flow_minute, 24, 3720)
x_AM_flow_minute = np.nan_to_num(x_AM_flow_minute)

x_MD_flow_minute = np.matrix(MD_flow_minute_list)
x_MD_flow_minute = np.matrix.reshape(x_MD_flow_minute, 24, 3720)
x_MD_flow_minute = np.nan_to_num(x_MD_flow_minute)

x_PM_flow_minute = np.matrix(PM_flow_minute_list)
x_PM_flow_minute = np.matrix.reshape(x_PM_flow_minute, 24, 3720)
x_PM_flow_minute = np.nan_to_num(x_PM_flow_minute)

x_NT_flow_minute = np.matrix(NT_flow_minute_list)
x_NT_flow_minute = np.matrix.reshape(x_NT_flow_minute, 24, 3720)
x_NT_flow_minute = np.nan_to_num(x_NT_flow_minute)

zz1 = x_AM_flow_minute[:,3599] 
zz = x_AM_flow[:,30] 

assert(zz1[1,0] + zz1[3,0] - (zz1[0,0] + zz1[2,0]) < 1e-5)
assert(zz1[0,0] + zz1[5,0] + zz1[7,0] - (zz1[1,0] + zz1[4,0] + zz1[6,0]) < 1e-5)
assert(zz1[2,0] + zz1[4,0] + zz1[9,0] + zz1[11,0] - (zz1[3,0] + zz1[5,0] + zz1[8,0] + zz1[10,0]) < 1e-5)
assert(zz1[6,0] + zz1[13,0] + zz1[17,0] - (zz1[7,0] + zz1[12,0] + zz1[16,0]) < 1e-5)
assert(zz1[8,0] + zz1[12,0] + zz1[15,0] + zz1[19,0] - (zz1[9,0] + zz1[13,0] + zz1[14,0] + zz1[18,0]) < 1e-5)
assert(zz1[10,0] + zz1[14,0] + zz1[21,0] - (zz1[11,0] + zz1[15,0] + zz1[20,0]) < 1e-5)
assert(zz1[18,0] + zz1[20,0] + zz1[23,0] - (zz1[19,0] + zz1[21,0] + zz1[22,0]) < 1e-5)
assert(zz1[16,0] + zz1[22,0] - (zz1[17,0] + zz1[23,0]) < 1e-5)

assert(zz[1,0] + zz[3,0] - (zz[0,0] + zz[2,0]) < 1e-5)
assert(zz[0,0] + zz[5,0] + zz[7,0] - (zz[1,0] + zz[4,0] + zz[6,0]) < 1e-5)
assert(zz[2,0] + zz[4,0] + zz[9,0] + zz[11,0] - (zz[3,0] + zz[5,0] + zz[8,0] + zz[10,0]) < 1e-5)
assert(zz[6,0] + zz[13,0] + zz[17,0] - (zz[7,0] + zz[12,0] + zz[16,0]) < 1e-5)
assert(zz[8,0] + zz[12,0] + zz[15,0] + zz[19,0] - (zz[9,0] + zz[13,0] + zz[14,0] + zz[18,0]) < 1e-5)
assert(zz[10,0] + zz[14,0] + zz[21,0] - (zz[11,0] + zz[15,0] + zz[20,0]) < 1e-5)
assert(zz[18,0] + zz[20,0] + zz[23,0] - (zz[19,0] + zz[21,0] + zz[22,0]) < 1e-5)
assert(zz[16,0] + zz[22,0] - (zz[17,0] + zz[23,0]) < 1e-5)
