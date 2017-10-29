using JSON

demandsDict = Dict()
# get ground trueth demands, indexed by 0
demandsDict[0] = iniDemand("../data_original/MA_trips.txt")
# get initial demands, indexed by 1
demandsDict[1] = iniDemand("../data_original/MA_trips.txt", 1)

numNodes, numLinks, numODpairs, capacity, free_flow_time, ta_data = paraNetwork("EMA_IFAC_Apr_PM")
link_label_dict, link_label_dict_, link_length_dict = furInfo()

start_node = ta_data.start_node
end_node = ta_data.end_node

#load OD pair labels
odPairLabel = readall("../temp_files/od_pair_label_dict_MA_refined.json")
odPairLabel = JSON.parse(odPairLabel)

odPairLabel_ = readall("../temp_files/od_pair_label_dict__MA_refined.json")
odPairLabel_ = JSON.parse(odPairLabel_)

#load node-link incidence
nodeLink = readall("../temp_files/node_link_incidence_MA.json");
nodeLink = JSON.parse(nodeLink);
