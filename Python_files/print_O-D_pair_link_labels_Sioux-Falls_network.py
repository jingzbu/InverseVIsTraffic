#!/usr/bin/env python


__author__ = "Jing Zhang"
__email__ = "jingzbu@gmail.com"
__status__ = "Development"

from util_data_storage_and_load import *

# number of nodes
n = 24

# create O-D pair labels
# create a dictionary mapping O-D pairs to labels
OD_pair_label_dict = {}
OD_pair_label_dict_ = {}
with open('../temp_files/O-D_pair_labels_Sioux-Falls_network.txt', 'w') as the_file:
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

zdump(OD_pair_label_dict, '../temp_files/OD_pair_label_dict_Sioux-Falls_network.pkz')
zdump(OD_pair_label_dict_, '../temp_files/OD_pair_label_dict__Sioux-Falls_network.pkz')


from collections import defaultdict


# number of links
m = 76

# create link labels
# create a dictionary mapping directed links to labels
link_label_dict = {}
link_label_dict_ = {}

link_list = ['1->2','1->3','2->1','2->6','3->1','3->4','3->12','4->3','4->5', 
'4->11','5->4','5->6','5->9','6->2','6->5','6->8','7->8','7->18','8->6','8->7',
'8->9','8->16','9->5','9->8','9->10','10->9','10->11','10->15','10->16','10->17','11->4',
'11->10','11->12','11->14','12->3','12->11','12->13','13->12','13->24','14->11','14->15',
'14->23','15->10','15->14','15->19','15->22','16->8','16->10','16->17','16->18',
'17->10','17->16','17->19','18->7','18->16','18->20','19->15','19->17','19->20',
'20->18','20->19','20->21','20->22','21->20','21->22','21->24','22->15','22->20',
'22->21','22->23','23->14','23->22','23->24','24->13', '24->21', '24->23']

for i in range(m):
    link_label_dict[str(i)] = link_list[i]

for i in range(m):
    link_label_dict_[link_list[i]] = i

zdump(link_label_dict, '../temp_files/link_label_dict_Sioux-Falls_network.pkz')
zdump(link_label_dict_, '../temp_files/link_label_dict_Sioux-Falls_network_.pkz')
