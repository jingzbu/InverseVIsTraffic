# read in arc data

type Arc
    initNode::Int 
    termNode::Int 
    capacity::Float64
    freeflowtime::Float64
    flow::Float64
end

Arc(initNode::Int, termNode::Int, capacity::Float64, freeflowtime::Float64) = 
    Arc(initNode, termNode, capacity, freeflowtime, 0.)

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
        arcs[key].flow = tapFlowDic[key]
    end
    return arcs
end

# read in initial demand data

function iniDemand(trip_file, flag=0)
    file = open(trip_file)
    demands = Dict{(Int64,Int64), Float64}()
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
                    demands[(s,t)] = demand
                    if flag == 1
                        # perturb the ground truth demands slightly 
                        # with perturbation factor uniformly distributed on [.9, 1.1)
                        pert_fac = 1 + 0.1 * (1 - 2 * rand())
                        demands[(s,t)] = demand * pert_fac
                    end
                end
            end
        end
    end                
    close(file)
    return demands
end


# obtain important parameters of the network

include("load_network_uni-class.jl")

function paraNetwork(nameNetwork)
    ta_data = load_ta_network(nameNetwork)
    numNodes = maximum(map(pair->pair[1], keys(demandsDict[0])))
    start_node = ta_data.start_node
    capacity = ta_data.capacity
    free_flow_time = ta_data.free_flow_time
    numLinks = size(start_node)[1]
    numODpairs = numNodes * (numNodes - 1)
    return numNodes, numLinks, numODpairs, capacity, free_flow_time, ta_data
end

# obtain further info of the network

using JSON

function furInfo()
    
    #get number of routes
    numRoutes = readall("numRoutes.json")
    numRoutes = JSON.parse(numRoutes)

    #load OD pair-route incidence
    odPairRoute = readall("od_pair_route_incidence_Sioux_simp.json")
    odPairRoute = JSON.parse(odPairRoute)

    #load link-route incidence
    linkRoute = readall("link_route_incidence_Sioux_simp.json")
    linkRoute = JSON.parse(linkRoute)

    link_label_dict = readall("link_label_dict_Sioux_simp.json")
    link_label_dict = JSON.parse(link_label_dict)
    
    return numRoutes, odPairRoute, linkRoute, link_label_dict
end
