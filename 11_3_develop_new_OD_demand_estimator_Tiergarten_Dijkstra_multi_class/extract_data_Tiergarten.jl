using JSON

demandsDict = Dict{}()
# get ground truth demands, indexed by 0
demandsDict[0] = iniDemand("../data_original/Tiergarten_trips.txt")
# get initial demands, indexed by 1
demandsDict[1] = iniDemand("../data_original/Tiergarten_trips.txt", 1)

numNodes, numLinks, numODpairs, capacity, free_flow_time, ta_data = paraNetwork("Tiergarten")
link_label_dict, link_label_dict_, link_length_dict = furInfo()

start_node = ta_data.start_node
end_node = ta_data.end_node

#load OD pair labels
odPairLabel = readstring("../temp_files/od_pair_label_dict_Tiergarten_refined.json")
odPairLabel = JSON.parse(odPairLabel)

odPairLabel_ = readstring("../temp_files/od_pair_label_dict__Tiergarten_refined.json")
odPairLabel_ = JSON.parse(odPairLabel_)

#load node-link incidence
nodeLink = readstring("../temp_files/node_link_incidence_Tiergarten.json");
nodeLink = JSON.parse(nodeLink);
