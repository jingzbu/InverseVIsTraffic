# read in arc data

type Arc
    initNode::Int 
    termNode::Int 
    capacity::Float64
    freeflowtime::Float64
    flow::Float64
    flow_car::Float64
    flow_truck::Float64
end

Arc(initNode::Int, termNode::Int, capacity::Float64,freeflowtime::Float64) = 
    Arc(initNode, termNode, capacity, freeflowtime, 0., 0., 0.)

function arcData(arc_file)
    arcs = Dict{(Int, Int), Arc}()
    file = open(arc_file)
    inHeader=true
    for line in eachline(file)
        if inHeader
            inHeader = !contains(line, "Init node")
            continue
        end
        vals = split(line, )
        arcs[(int(vals[1]), int(vals[2]))] = Arc(int(vals[1]), int(vals[2]), float(vals[3]), float(vals[5]))
    end
    close(file) 
    return arcs
end

# add flow data to arcs
function observFlow(arc_file, tapFlowDic)
    arcs = arcData(arc_file)
    ix = 0 
    for key in keys(arcs)
        arcs[key].flow = 1.0 * tapFlowDic["car"][key] + 2.0 * tapFlowDic["truck"][key]
        arcs[key].flow_car = tapFlowDic["car"][key]
        arcs[key].flow_truck = tapFlowDic["truck"][key]
    end
    return arcs
end

# read in initial demand data
srand(2016)
function iniDemand(trip_file, flag=0)
    file = open(trip_file)
    demands = Dict{}()
    demandsCar = Dict{}()
    demandsTruck = Dict{}()
    s = 0
    for line in eachline(file)
        if contains(line, "Origin")
            s = int(split(line)[2])
        else
            pairs = split(line, ";")
            for pair in pairs
                if !contains(pair, "\n")
                    pair_vals = split(pair, ":")
                    t, demand = int(pair_vals[1]), float(pair_vals[2])
                    demandsCar[(s,t)] = demand * 0.8  # demands for cars
		    demandsTruck[(s,t)] = demand * 0.2  # demands for trucks
                    if flag == 1
                        # perturb the ground truth demands slightly 
                        # with perturbation factor uniformly distributed on [.8, 1.2)
                        pert_fac = 1 + 0.2 * (1 - 2 * rand())
                        demandsCar[(s,t)] = demand * pert_fac * 0.8  # demands for cars
			demandsTruck[(s,t)] = demand * pert_fac * 0.2  # demands for trucks
                    end
		    demands["car"] = demandsCar
  		    demands["truck"] = demandsTruck
                end
            end
        end
    end                
    close(file)
    return demands
end

function demandsDicToVec(demandsDic)
    demandsVec = zeros(length(odPairLabel_))
    for i = 1:length(demandsVec)
        demandsVec[i] = demandsDic[(odPairLabel_["$i"][1], odPairLabel_["$i"][2])]
	demandsVec[i] = demandsDic[(odPairLabel_["$i"][1], odPairLabel_["$i"][2])]
    end
    return demandsVec
end

function demandsVecToDic(demandsVec)
    demandsDic = Dict{(Int64,Int64), Float64}()
    for i = 1:numNodes
        demandsDic[(i, i)] = 0
    end
    for i = 1:length(demandsVec)
        demandsDic[(odPairLabel_["$i"][1], odPairLabel_["$i"][2])] = demandsVec[i]
    end
    return demandsDic
end

# obtain important parameters of the network

include("load_network_uni-class.jl")

function paraNetwork(nameNetwork)
    ta_data = load_ta_network(nameNetwork)
    numNodes = maximum(map(pair->pair[1], keys(demandsDict[0]["car"])))
    start_node = ta_data.start_node
    capacity = ta_data.capacity
    free_flow_time = ta_data.free_flow_time
    numLinks = size(start_node)[1]
    numODpairs = numNodes * (numNodes - 1)
    return numNodes, numLinks, numODpairs, capacity, free_flow_time, ta_data
end

function tapFlowVecToLinkCostDict(tapFlowVec, fcoeffsInvVI)
    linkCostVecCar = 1.0 * BPR(1.0 * tapFlowVec[1,:] + 2.0 * tapFlowVec[2,:], fcoeffsInvVI)
    linkCostVecTruck = 1.1 * BPR(1.0 * tapFlowVec[1,:] + 2.0 * tapFlowVec[2,:], fcoeffsInvVI)

    temp_dict_car = Dict{}()
    temp_dict_truck = Dict{}()
    for i = 1:length(linkCostVecCar)
        temp_dict_car["$(i-1)"] = linkCostVecCar[i]
	temp_dict_truck["$(i-1)"] = linkCostVecTruck[i]
    end

    linkCostDict = Dict{}()
    linkCostDict["car"] = temp_dict_car
    linkCostDict["truck"] = temp_dict_truck

    return linkCostDict
end

# calculate od Pair - route choice probability matrix P

function odPairRouteProb(tau, route_cost_vec, OD_pair_route_dict, numODpairs, numRoutes)
    P = zeros((numODpairs, numRoutes))
    for i in 1:numODpairs
        for r in OD_pair_route_dict["$(i-1)"]
    #         println(r)
    #         break
            # P[i, r] = 1
            P[i, r+1] = exp(- tau * route_cost_vec[r+1]) / sum([exp(- tau * route_cost_vec[j+1]) 
                for j in OD_pair_route_dict["$(i-1)"]])
        end
    end

    # maximum(P[9,:])

    P_dict = Dict{}()
    for i in 1:numODpairs
        for j in 1:numRoutes
            key = "$(i)-$(j)"
            if (P[i, j] > 1e-15)
                P_dict[key] = P[i, j]
            end
        end
    end
    return P_dict
end

function lengthRouteVec(linkCostDic)
    routeCostVec = Float64[]

    the_file = open("../temp_files/path-link_incidence_Sioux-Falls.txt", "r")

    while (line=readline(the_file)) != ""
        if contains(line, "->")
            node_list = Int64[]
            link_list = String[]
            for i in split(line[1:end-1], "->")
                push!(node_list, int64(i))
            end
            for i in 1:length(node_list)-1
                push!(link_list, "$(node_list[i]),$(node_list[i+1])")
            end

    #         link_label_dict_[link]
            routeCost = sum([linkCostDic[string(link_label_dict_[link])] for link in link_list])
            push!(routeCostVec, routeCost)
    #         println(line)
    #         println(split(line[1:end-1], "->"))

    #         println(node_list)
    #         println(link_list)
    #         break
        end
    end  
    return routeCostVec
end

# obtain further info of the network

using JSON

function furInfo()
    
    #get number of routes
    numRoutes = readall("../temp_files/numRoutes_Sioux.json")
    numRoutes = JSON.parse(numRoutes)

    #load OD pair-route incidence
    odPairRoute = readall("../temp_files/od_pair_route_incidence_Sioux.json")
    odPairRoute = JSON.parse(odPairRoute)

    #load link-route incidence
    linkRoute = readall("../temp_files/link_route_incidence_Sioux.json")
    linkRoute = JSON.parse(linkRoute)

    link_label_dict = readall("../temp_files/link_label_dict_Sioux.json")
    link_label_dict = JSON.parse(link_label_dict)

    link_label_dict_ = readall("../temp_files/link_label_dict_Sioux_.json")
    link_label_dict_ = JSON.parse(link_label_dict_)

    link_length_dict = readall("../temp_files/link_length_dict_Sioux.json")
    link_length_dict = JSON.parse(link_length_dict)

    OD_pair_route_dict = readall("../temp_files/OD_pair_route_dict_Sioux.json")
    OD_pair_route_dict = JSON.parse(OD_pair_route_dict)
    
    return numRoutes, odPairRoute, linkRoute, link_label_dict, link_label_dict_, link_length_dict, OD_pair_route_dict
end
