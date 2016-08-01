#!/usr/bin/env python


__author__ = "Jing Zhang"
__email__ = "jingzbu@gmail.com"
__status__ = "Development"

from util_data_storage_and_load import *

# number of nodes
n = 22


from collections import defaultdict


# number of links
m = 74

# create link labels
# create a dictionary mapping directed links to labels
link_label_dict = {}
link_label_dict_ = {}

link_list = ['1->2','2->1','1->3','3->1','2->3','3->2','2->4','4->2','3->6',
'6->3','4->6','6->4','4->7','7->4','4->18','18->7','18->4','7->18','4->5','5->4',
'6->7','7->6','5->8','8->5','5->9','9->5','7->9','9->7','7->11','11->7','9->10',
'10->9','8->10','10->8','10->11','11->10','8->12','12->8','10->13','13->10','11->14',
'14->11','12->13','13->12','12->19','19->13','19->12','13->19','12->20','20->13',
'20->12','13->20','13->14','14->13','13->21','21->14','21->13','14->21','12->15',
'15->12','13->15','15->13','13->16','16->13','14->16','16->14','14->22','22->16',
'22->14','16->22','15->17','17->15','16->17','17->16']

for i in range(m):
    link_label_dict[str(i)] = link_list[i]

for i in range(m):
    link_label_dict_[link_list[i]] = i

zdump(link_label_dict, '../temp_files/link_label_dict_ext.pkz')
zdump(link_label_dict_, '../temp_files/link_label_dict_ext_.pkz')
