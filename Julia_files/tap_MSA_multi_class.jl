using Graphs

function create_graph(start_node, end_node)
    @assert length(start_node)==length(end_node)

    no_node = max(maximum(start_node), maximum(end_node))
    no_arc = length(start_node)

    graph = simple_inclist(no_node)
    for i=1:no_arc
        add_edge!(graph, start_node[i], end_node[i])
    end
    return graph
end

function get_vector(state, origin, destination, link_dic)
    current = destination
    parent = -1
    x = zeros(Int, maximum(link_dic))

    while parent != origin
        parent = state.parents[current]

        link_idx = link_dic[parent,current]

        if link_idx != 0
            x[link_idx] = 1
        end

        current = parent
    end

    return x
end

# preparing a graph
graph = create_graph(start_node, end_node);
link_dic = sparse(start_node, end_node, 1:numLinks);

function BPR(flowVec, fcoeffs)
    bpr = similar(flowVec)
    for a = 1:length(bpr)
        bpr[a] = free_flow_time[a] * sum([fcoeffs[i] * (flowVec[a]/capacity[a])^(i-1) for i = 1:length(fcoeffs)])
        if bpr[a] < free_flow_time[a]
            bpr[a] = free_flow_time[a]
        end
    end
    return bpr
end

function all_or_nothing(travel_time, travel_demand_dict)
    state = []
    path = []
    x = zeros(size(start_node))

    for r=1:numNodes
        # for each origin node r, find shortest paths to all destination nodes
        state = dijkstra_shortest_paths(graph, travel_time, r)

        for s=1:numNodes
            # for each destination node s, find the shortest-path vector
            # load travel demand
            x = x + travel_demand_dict[(r,s)] * get_vector(state, r, s, link_dic)
        end
    end

    return x
end

function tapMSA_Multi(travel_demand_car, travel_demand_truck, fcoeffs, numIter=1000, tol=1e-6)
    
    # Finding a starting feasible solution
    travel_time = BPR(zeros(numLinks), fcoeffs);

    travel_time_car = 1.0 * BPR(zeros(numLinks), fcoeffs);
    travel_time_truck = 1.1 * BPR(zeros(numLinks), fcoeffs);

    xl_car = all_or_nothing(travel_time_car, travel_demand_car);
    xl_truck = all_or_nothing(travel_time_truck, travel_demand_truck);
    
    l = 1

    while l < numIter
        l += 1

        # Finding yl_car
        xl_car_old = xl_car
        travel_time_car = 1.0 * BPR(xl_car + 2.0 * xl_truck, fcoeffs)
        yl_car = all_or_nothing(travel_time_car, travel_demand_car);
        xl_car = xl_car + (yl_car - xl_car)/l
        xl_car_new = xl_car

        # Finding yl_truck
        xl_truck_old = xl_truck
        travel_time_truck = 1.1 * BPR(xl_car + 2.0 * xl_truck, fcoeffs)
        yl_truck = all_or_nothing(travel_time_truck, travel_demand_truck);
        xl_truck = xl_truck + (yl_truck - xl_truck)/l
        xl_truck_new = xl_truck


        relative_gap_car = norm(xl_car_new - xl_car_old, 1) / norm(xl_car_new, 1)
        relative_gap_truck = norm(xl_truck_new - xl_truck_old, 1) / norm(xl_truck_new, 1)

        if relative_gap_car < tol && relative_gap_truck < tol
            break
        end
    end
        
    tapFlows = Dict{}()
    tapFlowsCar = Dict{}()
    tapFlowsTruck = Dict{}()
    tapFlowVect = zeros(2,length(xl_car))

    for i = 1:length(ta_data.start_node)
        key = (ta_data.start_node[i], ta_data.end_node[i])
        tapFlowsCar[key] = xl_car[i]
        tapFlowsTruck[key] = xl_truck[i]
    end
    tapFlows["car"] = tapFlowsCar
    tapFlows["truck"] = tapFlowsTruck

    for j = 1:length(xl_car)
        tapFlowVect[1,j] = xl_car[j]
        tapFlowVect[2,j] = xl_truck[j]
    end

    return tapFlows, tapFlowVect

end
