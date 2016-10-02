#!/usr/bin/env python


__author__ = "Jing Zhang"
__email__ = "jingzbu@gmail.com"
__status__ = "Development"


from util import *

link_1_1, link_1_2, link_2_1, link_2_2, link_3_1, link_3_2, \
	link_4_1, link_4_2, link_5_1, link_5_2, link_6_1, link_6_2, \
	link_7_1, link_7_2, link_8_1, link_8_2, link_9_1, link_9_2, \
	link_10_1, link_10_2, link_11_1, link_11_2, link_12_1, link_12_2 \
    = zload('../temp_files/links_with_capac.pkz')

# 0 <---> link_1_1, 1 <---> link_1_2, 2 <---> link_2_1, 3 <---> link_2_2
# 4 <---> link_3_1, 5 <---> link_3_2, 6 <---> link_4_1, 7 <---> link_4_2
# 8 <---> link_5_1, 9 <---> link_5_2, 10 <---> link_6_1, 11 <---> link_6_2
# 12 <---> link_7_1, 13 <---> link_7_2, 14 <---> link_8_1, 15 <---> link_8_2
# 16 <---> link_9_1, 17 <---> link_9_2, 18 <---> link_10_1, 19 <---> link_10_2
# 20 <---> link_11_1, 21 <---> link_11_2, 22 <---> link_12_1, 23 <---> link_12_2

link_with_capac_list = list(zload('../temp_files/links_with_capac.pkz'))

# print(len(link_with_capac_list))
# print(len(tmc_capac_dict_AM))
# print(tmc_ref_speed_dict['129+04099'])

road_seg_inr_capac = zload('../temp_files/road_seg_inr_capac.pkz')

# print(len(road_seg_inr_capac.tmc))

# load tmc-day-ave_speed data for AM peak of January
tmc_day_speed_dict_Jan_AM = zload('../temp_files/Jan_AM/tmc_day_speed_dict.pkz')

# load tmc-day-ave_speed data for MD of January
tmc_day_speed_dict_Jan_MD = zload('../temp_files/Jan_MD/tmc_day_speed_dict.pkz')

# load tmc-day-ave_speed data for PM peak of January
tmc_day_speed_dict_Jan_PM = zload('../temp_files/Jan_PM/tmc_day_speed_dict.pkz')

# load tmc-day-ave_speed data for NT of January
tmc_day_speed_dict_Jan_NT = zload('../temp_files/Jan_NT/tmc_day_speed_dict.pkz')

tmc_day_capac_flow_dict = {}

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
        tmc_day_capac_flow = RoadSegInrCapacFlow(tmc, road_num, shape_length, day, \
                                                  AB_AM_capac, AB_MD_capac, \
                                                  AB_PM_capac, AB_NT_capac, \
                                                  AM_ave_speed, MD_ave_speed, \
                                                  PM_ave_speed, NT_ave_speed)
        tmc_day_capac_flow_dict[tmc + str(day)] = tmc_day_capac_flow

# print(len(tmc_day_capac_flow_dict))

zdump(tmc_day_capac_flow_dict, '../temp_files/tmc_day_capac_flow_dict_Jan.pkz')

link_day_Jan_dict = {}

for day in range(32)[1:]:
    i = 0
    for link_with_capac in link_with_capac_list:
        #### tmc_length_dict[tmc] / tmc_day_capac_flow_dict[tmc + str(day)].ave_speed()
        AM_flow = sum([tmc_day_capac_flow_dict[tmc + str(day)].AM_flow() * tmc_length_dict[tmc] / \
                       tmc_day_speed_dict_Jan_AM[tmc + str(day)].ave_speed() \
                       for tmc in link_with_capac.tmc_set]) / \
                  sum([tmc_length_dict[tmc] / tmc_day_speed_dict_Jan_AM[tmc + str(day)].ave_speed() \
                       for tmc in link_with_capac.tmc_set])
        MD_flow = sum([tmc_day_capac_flow_dict[tmc + str(day)].MD_flow() * tmc_length_dict[tmc] / \
                       tmc_day_speed_dict_Jan_MD[tmc + str(day)].ave_speed() \
                       for tmc in link_with_capac.tmc_set]) / \
                  sum([tmc_length_dict[tmc] / tmc_day_speed_dict_Jan_MD[tmc + str(day)].ave_speed() \
                       for tmc in link_with_capac.tmc_set])
        PM_flow = sum([tmc_day_capac_flow_dict[tmc + str(day)].PM_flow() * tmc_length_dict[tmc] / \
                       tmc_day_speed_dict_Jan_PM[tmc + str(day)].ave_speed() \
                       for tmc in link_with_capac.tmc_set]) / \
                  sum([tmc_length_dict[tmc] / tmc_day_speed_dict_Jan_PM[tmc + str(day)].ave_speed() \
                       for tmc in link_with_capac.tmc_set])
        NT_flow = sum([tmc_day_capac_flow_dict[tmc + str(day)].NT_flow() * tmc_length_dict[tmc] / \
                       tmc_day_speed_dict_Jan_NT[tmc + str(day)].ave_speed() \
                       for tmc in link_with_capac.tmc_set]) / \
                  sum([tmc_length_dict[tmc] / tmc_day_speed_dict_Jan_NT[tmc + str(day)].ave_speed() \
                       for tmc in link_with_capac.tmc_set])
        link_with_capac_new = Link_with_Free_Flow_Time(link_with_capac.init_node, link_with_capac.term_node, \
                                                       link_with_capac.tmc_set, \
                                                       link_with_capac.AM_capac, \
                                                       link_with_capac.MD_capac, \
                                                       link_with_capac.PM_capac, \
                                                       link_with_capac.NT_capac, \
                                                       link_with_capac.free_flow_time, \
                                                       link_with_capac.length, \
                                                       AM_flow, MD_flow, PM_flow, NT_flow)
        link_day_Jan_dict['link_' + str(i) + '_' + str(day)] = link_with_capac_new
        i = i + 1

zdump(link_day_Jan_dict, '../temp_files/link_day_Jan_dict.pkz')

# print(link_day_Jan_dict['link_22_29'].PM_flow)
