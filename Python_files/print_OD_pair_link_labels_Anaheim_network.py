#!/usr/bin/env python


__author__ = "Jing Zhang"
__email__ = "jingzbu@gmail.com"
__status__ = "Development"

from util_data_storage_and_load import *

# number of zones
n = 38

# create O-D pair labels
# create a dictionary mapping O-D pairs to labels
OD_pair_label_dict = {}
OD_pair_label_dict_ = {}
with open('../temp_files/OD_pair_labels_Anaheim_network.txt', 'w') as the_file:
    label = 0
    for i in range(n + 1)[1:]:
        for j in range(n + 1)[1:]:
            if i != j: 
                key = (i, j)
                OD_pair_label_dict[str(key)] = label
		OD_pair_label_dict_[str(label)] = key
                the_file.write("O-D pair (%d, %d) ---> label %d    \n" %(i, j, label))
                label = label + 1
                if label % 21 == 0:
                    the_file.write('\n')

zdump(OD_pair_label_dict, '../temp_files/OD_pair_label_dict_Anaheim_network.pkz')
zdump(OD_pair_label_dict_, '../temp_files/OD_pair_label_dict__Anaheim_network.pkz')


# number of links
m = 914

# create link labels
# create a dictionary mapping directed links to labels
link_label_dict = {}
link_label_dict_ = {}

link_list = zload('../temp_files/Anaheim_link_list.pkz')

for i in range(m):
    link_label_dict[str(i)] = link_list[i]

for i in range(m):
    link_label_dict_[link_list[i]] = i

zdump(link_label_dict, '../temp_files/link_label_dict_Anaheim_network.pkz')
zdump(link_label_dict_, '../temp_files/link_label_dict_Anaheim_network_.pkz')
