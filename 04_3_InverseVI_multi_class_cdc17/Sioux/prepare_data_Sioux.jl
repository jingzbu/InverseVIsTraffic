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
    arcs = Dict()
    file = open(arc_file)
    inHeader=true
    for line in eachline(file)
        if inHeader
            inHeader = !contains(line, "Init node")
            continue
        end
        vals = split(line, )
        arcs[(parse(Int, vals[1]), parse(Int, vals[2]))] = Arc(parse(Int, vals[1]), parse(Int, vals[2]), 
        parse(Float64, vals[3]), parse(Float64, vals[5]))
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


# obtain important parameters of the network

include("../../Julia_files/load_network_uni_class.jl")

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