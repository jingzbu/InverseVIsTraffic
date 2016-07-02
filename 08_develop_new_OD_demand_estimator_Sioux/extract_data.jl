using JSON

demandsDict = Dict{Int64, Dict{(Int64,Int64), Float64}}()
# get ground trueth demands, indexed by 0
demandsDict[0] = iniDemand("../data_original/SiouxFalls_trips_simp.txt")
# get initial demands, indexed by 1
demandsDict[1] = iniDemand("../data_original/SiouxFalls_trips_simp.txt", 1)

numNodes, numLinks, numODpairs, capacity, free_flow_time, ta_data = paraNetwork("Sioux_simp")
numRoutes, odPairRoute, linkRoute, link_label_dict = furInfo()

start_node = ta_data.start_node
end_node = ta_data.end_node

#load OD pair labels
odPairLabel = readall("od_pair_label_dict_Sioux_simp_refined.json")
odPairLabel = JSON.parse(odPairLabel)

odPairLabel_ = readall("od_pair_label_dict__Sioux_simp_refined.json")
odPairLabel_ = JSON.parse(odPairLabel_)
