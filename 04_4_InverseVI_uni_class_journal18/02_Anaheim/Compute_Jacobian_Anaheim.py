from util import *

import json

with open('./benchmark_data/Anaheim_flow.txt') as Anaheim_flow:
    Anaheim_flow_lines = Anaheim_flow.readlines()
Anaheim_links = []
i = -1
for line in Anaheim_flow_lines:
    i += 1
    if i > 0:
        Anaheim_links.append(line.split('\t')[1:3])
numLinks = i

link_list_js = [str(int(Anaheim_links[i][0])) + ',' + str(int(Anaheim_links[i][1])) for \
                i in range(len(Anaheim_links))]

link_list_pk = [str(int(Anaheim_links[i][0])) + '->' + str(int(Anaheim_links[i][1])) for \
                i in range(len(Anaheim_links))]

numNodes = max([int(Anaheim_links[i][1]) for i in range(numLinks)])

from collections import defaultdict

node_neighbors_dict = defaultdict(list)

for node in range(numNodes):
    for link in Anaheim_links:
        if node == int(link[0]):
            node_neighbors_dict[str(node)].append(int(link[1]))

with open('./benchmark_data/Anaheim_trips.txt') as Anaheim_trips:
    Anaheim_trips_lines = Anaheim_trips.readlines()

numZones = int(Anaheim_trips_lines[0].split(' ')[3])

od_pairs = []
for i in range(numZones+1)[1:]:
    for j in range(numZones+1)[1:]:
        if i != j:
            od_pairs.append([i, j])
            
numODpairs = len(od_pairs)

# create O-D pair labels
# create a dictionary mapping O-D pairs to labels

import json

OD_pair_label_dict = {}
OD_pair_label_dict_ = {}

label = 1
for i in range(numZones + 1)[1:]:
    for j in range(numZones + 1)[1:]:
        key = (i, j)
        OD_pair_label_dict[str(key)] = label
        OD_pair_label_dict_[str(label)] = key
        label += 1
        
with open('../../temp_files/od_pair_label_dict_Anaheim.json', 'w') as json_file:
    json.dump(OD_pair_label_dict, json_file)
    
with open('../../temp_files/od_pair_label_dict__Anaheim.json', 'w') as json_file:
    json.dump(OD_pair_label_dict_, json_file)


OD_pair_label_dict_refined = {}
OD_pair_label_dict_refined_ = {}

label = 1
for i in range(numZones + 1)[1:]:
    for j in range(numZones + 1)[1:]:
        if i != j:
            key = (i, j)
            OD_pair_label_dict_refined[str(key)] = label
            OD_pair_label_dict_refined_[str(label)] = key
            label += 1
        
with open('../../temp_files/od_pair_label_dict_Anaheim_refined.json', 'w') as json_file:
    json.dump(OD_pair_label_dict_refined, json_file)
    
with open('../../temp_files/od_pair_label_dict__Anaheim_refined.json', 'w') as json_file:
    json.dump(OD_pair_label_dict_refined_, json_file)
    
    
# create link labels
# create a dictionary mapping directed links to labels
link_label_dict = {}
link_label_dict_ = {}

for i in range(numLinks):
    link_label_dict[str(i)] = link_list_js[i]

for i in range(numLinks):
    link_label_dict_[link_list_js[i]] = i

with open('../../temp_files/link_label_dict_Anaheim.json', 'w') as json_file:
    json.dump(link_label_dict, json_file)
    
with open('../../temp_files/link_label_dict_Anaheim_.json', 'w') as json_file:
    json.dump(link_label_dict_, json_file)
    
# create link labels
# create a dictionary mapping directed links to labels
link_label_dict = {}
link_label_dict_ = {}

for i in range(numLinks):
    link_label_dict[str(i)] = link_list_pk[i]

for i in range(numLinks):
    link_label_dict_[link_list_pk[i]] = i

zdump(link_label_dict, '../../temp_files/link_label_dict_Anaheim_network.pkz')
zdump(link_label_dict_, '../../temp_files/link_label_dict_Anaheim_network_.pkz')

link_length_list = []
with open('./benchmark_data/Anaheim_net.txt', 'r') as f:
    read_data = f.readlines()
    flag = 0
    for row in read_data:
        if ';' in row:
            flag += 1
            if flag > 1:
                link_length_list.append(float(row.split('\t')[4]))

link_label_dict = zload('../../temp_files/link_label_dict_Anaheim_network.pkz')
link_label_dict_ = zload('../../temp_files/link_label_dict_Anaheim_network_.pkz')

import networkx as nx

def jacobianSpiess(numNodes, numLinks, numODpairs, od_pairs, link_list_js, link_length_list):
    Anaheim = nx.DiGraph()

    Anaheim.add_nodes_from(range(numNodes+1)[1:])

    Anaheim_weighted_edges = [(int(link_list_js[i].split(',')[0]), int(link_list_js[i].split(',')[1]), \
                             link_length_list[i]) for i in range(len(link_list_js))]

    Anaheim.add_weighted_edges_from(Anaheim_weighted_edges)

    path = nx.all_pairs_dijkstra_path(Anaheim)

    od_route_dict = {}
    for od in od_pairs:
        origi = od[0]
        desti = od[1]
        key = OD_pair_label_dict_refined[str((origi, desti))]
        route = str(path[origi][desti]).replace("[", "").replace(", ", "->").replace("]", "")
        od_route_dict[key] = route

    od_link_dict = {}
    for idx in range(len(od_route_dict)):
        od_link_list = []
        od_node_list = od_route_dict[idx+1].split('->')
        for i in range(len(od_node_list)):
            if i < len(od_node_list) - 1:
                od_link_list.append(link_label_dict_[od_node_list[i] + '->' + od_node_list[i+1]])
        od_link_dict[idx] = od_link_list

    jacob = np.zeros((numODpairs, numLinks))

    for i in range(numODpairs):
        for j in range(numLinks):
            if j in od_link_dict[i]:
                jacob[i, j] = 1

    return jacob

jacob = jacobianSpiess(numNodes, numLinks, numODpairs, od_pairs, link_list_js, link_length_list)
