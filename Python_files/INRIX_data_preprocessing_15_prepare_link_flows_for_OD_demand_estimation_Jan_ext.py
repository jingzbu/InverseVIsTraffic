#!/usr/bin/env python


__author__ = "Jing Zhang"
__email__ = "jingzbu@gmail.com"
__status__ = "Development"


from util import *

road_seg_inr_capac = zload('../temp_files/road_seg_inr_capac_ext.pkz')

# load tmc-day-ave_speed data for AM peak of January
tmc_day_speed_dict_Jan_AM = zload('../temp_files/Jan_AM/tmc_day_speed_dict_ext.pkz')

# load tmc-day-ave_speed data for MD of January
tmc_day_speed_dict_Jan_MD = zload('../temp_files/Jan_MD/tmc_day_speed_dict_ext.pkz')

# load tmc-day-ave_speed data for PM peak of January
tmc_day_speed_dict_Jan_PM = zload('../temp_files/Jan_PM/tmc_day_speed_dict_ext.pkz')

# load tmc-day-ave_speed data for NT of January
tmc_day_speed_dict_Jan_NT = zload('../temp_files/Jan_NT/tmc_day_speed_dict_ext.pkz')


tmc_day_capac_flow_minute_dict = {}

for i in range(len(road_seg_inr_capac.tmc)):
    for day in range(32)[1:]:
        tmc = road_seg_inr_capac.tmc[i]
        road_num = road_seg_inr_capac.road_num[i]
        shape_length = road_seg_inr_capac.shape_length[i]
        day = day
        AB_AM_capac = road_seg_inr_capac.AB_AM_capac[i]
        AB_MD_capac = road_seg_inr_capac.AB_MD_capac[i]
        AB_PM_capac = road_seg_inr_capac.AB_PM_capac[i]
        AB_NT_capac = road_seg_inr_capac.AB_NT_capac[i]
        AM_ave_speed = tmc_day_speed_dict_Jan_AM[tmc + str(day)].ave_speed()
        MD_ave_speed = tmc_day_speed_dict_Jan_MD[tmc + str(day)].ave_speed()
        PM_ave_speed = tmc_day_speed_dict_Jan_PM[tmc + str(day)].ave_speed()
        NT_ave_speed = tmc_day_speed_dict_Jan_NT[tmc + str(day)].ave_speed()
        AM_speed_minute = tmc_day_speed_dict_Jan_AM[tmc + str(day)].speed
        MD_speed_minute = tmc_day_speed_dict_Jan_MD[tmc + str(day)].speed
        PM_speed_minute = tmc_day_speed_dict_Jan_PM[tmc + str(day)].speed
        NT_speed_minute = tmc_day_speed_dict_Jan_NT[tmc + str(day)].speed
        tmc_day_capac_flow_minute = RoadSegInrCapacFlowMinuteExt(tmc, road_num, shape_length, day, \
                                                  AB_AM_capac, AB_MD_capac, \
                                                  AB_PM_capac, AB_NT_capac, \
                                                  AM_ave_speed, MD_ave_speed, \
                                                  PM_ave_speed, NT_ave_speed, \
                                                  AM_speed_minute, MD_speed_minute, \
                                                  PM_speed_minute, NT_speed_minute)
        assert(len(tmc_day_capac_flow_minute.AM_flow_minute()) == 120)
        assert(len(tmc_day_capac_flow_minute.MD_flow_minute()) == 120)
        assert(len(tmc_day_capac_flow_minute.PM_flow_minute()) == 120)
        assert(len(tmc_day_capac_flow_minute.NT_flow_minute()) == 120)
        tmc_day_capac_flow_minute_dict[tmc + str(day)] = tmc_day_capac_flow_minute

#zdump(tmc_day_capac_flow_minute_dict, '../temp_files/tmc_day_capac_flow_minute_dict_Jan_ext.pkz')

link_with_capac_list = list(zload('../temp_files/links_with_capac_ext.pkz'))


import numpy as np

day = 1

link_with_capac = link_with_capac_list[0]

AM_flow_minute = list(sum([np.array(tmc_day_capac_flow_minute_dict[tmc + str(day)].AM_flow_minute()) \
                                   * tmc_length_dict_ext[tmc] / tmc_day_speed_dict_Jan_AM[tmc + str(day)].speed \
                              for tmc in link_with_capac.tmc_set]) / \
                      sum([np.ones(len(tmc_day_capac_flow_minute_dict[tmc + str(day)].AM_flow_minute())) * \
                           tmc_length_dict_ext[tmc] / tmc_day_speed_dict_Jan_AM[tmc + str(day)].speed \
                              for tmc in link_with_capac.tmc_set]))

# print(tmc, tmc_length_dict_ext[tmc], tmc_day_speed_dict_Jan_AM[tmc + str(day)].speed[0:5]) 

# print(np.array(tmc_day_capac_flow_minute_dict[tmc + str(day)].AM_flow_minute())[0:5])

# print(AM_flow_minute[0:5])

# aa = [1., 2., 3.]
# bb = [0.1, 0.2, 4.0]

# print(np.array(aa) / bb)
# print(sum([np.array(aa), np.array(bb)]))

tmc_day_capac_flow_dict = zload('../temp_files/tmc_day_capac_flow_dict_Jan_ext.pkz')


link_day_minute_Jan_dict = {}

for day in range(32)[1:]:
    i = 0
    for link_with_capac in link_with_capac_list:
        AM_flow = sum([tmc_day_capac_flow_dict[tmc + str(day)].AM_flow() * tmc_length_dict_ext[tmc] / \
                       tmc_day_speed_dict_Jan_AM[tmc + str(day)].ave_speed() \
                       for tmc in link_with_capac.tmc_set]) / \
                  sum([tmc_length_dict_ext[tmc] / tmc_day_speed_dict_Jan_AM[tmc + str(day)].ave_speed() \
                       for tmc in link_with_capac.tmc_set])
        MD_flow = sum([tmc_day_capac_flow_dict[tmc + str(day)].MD_flow() * tmc_length_dict_ext[tmc] / \
                       tmc_day_speed_dict_Jan_MD[tmc + str(day)].ave_speed() \
                       for tmc in link_with_capac.tmc_set]) / \
                  sum([tmc_length_dict_ext[tmc] / tmc_day_speed_dict_Jan_MD[tmc + str(day)].ave_speed() \
                       for tmc in link_with_capac.tmc_set])
        PM_flow = sum([tmc_day_capac_flow_dict[tmc + str(day)].PM_flow() * tmc_length_dict_ext[tmc] / \
                       tmc_day_speed_dict_Jan_PM[tmc + str(day)].ave_speed() \
                       for tmc in link_with_capac.tmc_set]) / \
                  sum([tmc_length_dict_ext[tmc] / tmc_day_speed_dict_Jan_PM[tmc + str(day)].ave_speed() \
                       for tmc in link_with_capac.tmc_set])
        NT_flow = sum([tmc_day_capac_flow_dict[tmc + str(day)].NT_flow() * tmc_length_dict_ext[tmc] / \
                       tmc_day_speed_dict_Jan_NT[tmc + str(day)].ave_speed() \
                       for tmc in link_with_capac.tmc_set]) / \
                  sum([tmc_length_dict_ext[tmc] / tmc_day_speed_dict_Jan_NT[tmc + str(day)].ave_speed() \
                       for tmc in link_with_capac.tmc_set])
        AM_flow_minute = list(sum([np.array(tmc_day_capac_flow_minute_dict[tmc + str(day)].AM_flow_minute()) \
                                   * tmc_length_dict_ext[tmc] / tmc_day_speed_dict_Jan_AM[tmc + str(day)].speed \
                                  for tmc in link_with_capac.tmc_set]) / \
                              sum([np.ones(len(tmc_day_capac_flow_minute_dict[tmc + str(day)].AM_flow_minute())) \
                                   * tmc_length_dict_ext[tmc] / tmc_day_speed_dict_Jan_AM[tmc + str(day)].speed \
                                  for tmc in link_with_capac.tmc_set]))
        MD_flow_minute = list(sum([np.array(tmc_day_capac_flow_minute_dict[tmc + str(day)].MD_flow_minute()) \
                                   * tmc_length_dict_ext[tmc] / tmc_day_speed_dict_Jan_MD[tmc + str(day)].speed \
                                  for tmc in link_with_capac.tmc_set]) / \
                              sum([np.ones(len(tmc_day_capac_flow_minute_dict[tmc + str(day)].MD_flow_minute())) \
                                   * tmc_length_dict_ext[tmc] / tmc_day_speed_dict_Jan_MD[tmc + str(day)].speed \
                                  for tmc in link_with_capac.tmc_set]))
        PM_flow_minute = list(sum([np.array(tmc_day_capac_flow_minute_dict[tmc + str(day)].PM_flow_minute()) \
                                   * tmc_length_dict_ext[tmc] / tmc_day_speed_dict_Jan_PM[tmc + str(day)].speed \
                                  for tmc in link_with_capac.tmc_set]) / \
                              sum([np.ones(len(tmc_day_capac_flow_minute_dict[tmc + str(day)].PM_flow_minute())) \
                                   * tmc_length_dict_ext[tmc] / tmc_day_speed_dict_Jan_PM[tmc + str(day)].speed \
                                  for tmc in link_with_capac.tmc_set]))
        NT_flow_minute = list(sum([np.array(tmc_day_capac_flow_minute_dict[tmc + str(day)].NT_flow_minute()) \
                                   * tmc_length_dict_ext[tmc] / tmc_day_speed_dict_Jan_NT[tmc + str(day)].speed \
                                  for tmc in link_with_capac.tmc_set]) / \
                              sum([np.ones(len(tmc_day_capac_flow_minute_dict[tmc + str(day)].NT_flow_minute())) \
                                   * tmc_length_dict_ext[tmc] / tmc_day_speed_dict_Jan_NT[tmc + str(day)].speed \
                                  for tmc in link_with_capac.tmc_set]))
        link_with_capac_new = Link_with_Free_Flow_Time_Minute_Ext(link_with_capac.init_node, link_with_capac.term_node, \
                                                       link_with_capac.tmc_set, \
                                                       link_with_capac.AM_capac, \
                                                       link_with_capac.MD_capac, \
                                                       link_with_capac.PM_capac, \
                                                       link_with_capac.NT_capac, \
                                                       link_with_capac.free_flow_time, \
                                                       link_with_capac.length, \
                                                       AM_flow, MD_flow, PM_flow, NT_flow, \
                                                       AM_flow_minute, MD_flow_minute, \
                                                       PM_flow_minute, NT_flow_minute)
        link_day_minute_Jan_dict['link_' + str(i) + '_' + str(day)] = link_with_capac_new
        i = i + 1

#zdump(link_day_minute_Jan_dict, '../temp_files/link_day_minute_Jan_dict_ext.pkz')

print(link_day_minute_Jan_dict['link_0_10'].PM_flow_minute[0:10])

link_day_minute_Jan_dict_ext_JSON = {}
num_links = len(link_with_capac_list)
for link_idx in range(num_links):
    for day in range(32)[1:]:   
        key = 'link_' + str(link_idx) + '_' + str(day)
        data = {'link_idx': link_idx, 'day': day, \
             'init_node': link_day_minute_Jan_dict[key].init_node, \
             'term_node': link_day_minute_Jan_dict[key].term_node, \
             'AM_capac': link_day_minute_Jan_dict[key].AM_capac, \
             'MD_capac': link_day_minute_Jan_dict[key].MD_capac, \
             'PM_capac': link_day_minute_Jan_dict[key].PM_capac, \
             'NT_capac': link_day_minute_Jan_dict[key].NT_capac, \
             'free_flow_time': link_day_minute_Jan_dict[key].free_flow_time, \
             'length': link_day_minute_Jan_dict[key].length, \
             'AM_flow': link_day_minute_Jan_dict[key].AM_flow, \
             'MD_flow': link_day_minute_Jan_dict[key].MD_flow, \
             'PM_flow': link_day_minute_Jan_dict[key].PM_flow, \
             'NT_flow': link_day_minute_Jan_dict[key].NT_flow, \
             'AM_flow_minute': link_day_minute_Jan_dict[key].AM_flow_minute, \
             'MD_flow_minute': link_day_minute_Jan_dict[key].MD_flow_minute, \
             'PM_flow_minute': link_day_minute_Jan_dict[key].PM_flow_minute, \
             'NT_flow_minute': link_day_minute_Jan_dict[key].NT_flow_minute}
        link_day_minute_Jan_dict_ext_JSON[key] = data
        
import json

# Writing JSON data
with open('../temp_files/link_day_minute_Jan_dict_ext_JSON.json', 'w') as json_file:
    json.dump(link_day_minute_Jan_dict_ext_JSON, json_file)

with open('../temp_files/link_day_minute_Jan_dict_ext_JSON.json', 'r') as json_file:
    link_day_minute_Jan_dict_ext_JSON_ = json.load(json_file)

print(link_day_minute_Jan_dict_ext_JSON_['link_3_9'] ['AM_flow_minute'][0:10])
