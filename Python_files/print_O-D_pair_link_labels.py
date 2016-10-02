#!/usr/bin/env python


__author__ = "Jing Zhang"
__email__ = "jingzbu@gmail.com"
__status__ = "Development"

from util_data_storage_and_load import *

# number of nodes
n = 8

# create O-D pair labels
# create a dictionary mapping O-D pairs to labels
OD_pair_label_dict = {}
with open('../temp_files/O-D_pair_labels.txt', 'w') as the_file:
    label = 0
    for i in range(n + 1)[1:]:
        for j in range(n + 1)[1:]:
            if i != j: 
                key = (i, j)
                OD_pair_label_dict[str(key)] = label
                the_file.write("O-D pair (%d, %d) ---> label %d    \n" %(i, j, label))
                label = label + 1
                if label % 7 == 0:
                    the_file.write('\n')

zdump(OD_pair_label_dict, '../temp_files/OD_pair_label_dict.pkz')

# 0 <---> link_1_1, 1 <---> link_1_2, 2 <---> link_2_1, 3 <---> link_2_2
# 4 <---> link_3_1, 5 <---> link_3_2, 6 <---> link_4_1, 7 <---> link_4_2
# 8 <---> link_5_1, 9 <---> link_5_2, 10 <---> link_6_1, 11 <---> link_6_2
# 12 <---> link_7_1, 13 <---> link_7_2, 14 <---> link_8_1, 15 <---> link_8_2
# 16 <---> link_9_1, 17 <---> link_9_2, 18 <---> link_10_1, 19 <---> link_10_2
# 20 <---> link_11_1, 21 <---> link_11_2, 22 <---> link_12_1, 23 <---> link_12_2

# number of links
m = 24

# create link labels
# create a dictionary mapping directed links to labels
link_label_dict = {}
link_label_dict_ = {}

link_label_dict['0'] = '1->2'
link_label_dict['1'] = '2->1' 
link_label_dict['2'] = '1->3' 
link_label_dict['3'] = '3->1' 
link_label_dict['4'] = '2->3' 
link_label_dict['5'] = '3->2' 
link_label_dict['6'] = '2->4' 
link_label_dict['7'] = '4->2' 
link_label_dict['8'] = '3->5' 
link_label_dict['9'] = '5->3' 
link_label_dict['10'] = '3->6' 
link_label_dict['11'] = '6->3' 
link_label_dict['12'] = '4->5'
link_label_dict['13'] = '5->4' 
link_label_dict['14'] = '5->6' 
link_label_dict['15'] = '6->5' 
link_label_dict['16'] = '4->8' 
link_label_dict['17'] = '8->4' 
link_label_dict['18'] = '5->7' 
link_label_dict['19'] = '7->5' 
link_label_dict['20'] = '6->7' 
link_label_dict['21'] = '7->6' 
link_label_dict['22'] = '7->8' 
link_label_dict['23'] = '8->7' 

link_label_dict_['1->2'] = 0
link_label_dict_['2->1'] = 1
link_label_dict_['1->3'] = 2 
link_label_dict_['3->1'] = 3 
link_label_dict_['2->3'] = 4 
link_label_dict_['3->2'] = 5 
link_label_dict_['2->4'] = 6 
link_label_dict_['4->2'] = 7 
link_label_dict_['3->5'] = 8 
link_label_dict_['5->3'] = 9 
link_label_dict_['3->6'] = 10 
link_label_dict_['6->3'] = 11 
link_label_dict_['4->5'] = 12
link_label_dict_['5->4'] = 13 
link_label_dict_['5->6'] = 14 
link_label_dict_['6->5'] = 15 
link_label_dict_['4->8'] = 16 
link_label_dict_['8->4'] = 17 
link_label_dict_['5->7'] = 18 
link_label_dict_['7->5'] = 19 
link_label_dict_['6->7'] = 20 
link_label_dict_['7->6'] = 21 
link_label_dict_['7->8'] = 22 
link_label_dict_['8->7'] = 23 

zdump(link_label_dict, '../temp_files/link_label_dict.pkz')
zdump(link_label_dict_, '../temp_files/link_label_dict_.pkz')
