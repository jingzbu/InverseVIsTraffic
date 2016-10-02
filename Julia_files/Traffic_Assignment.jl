@everywhere include("load_network.jl")

@everywhere using Graphs

@everywhere function create_graph(start_node, end_node)
    @assert Base.length(start_node)==Base.length(end_node)

    no_node = max(maximum(start_node), maximum(end_node))
    no_arc = Base.length(start_node)

    graph = simple_inclist(no_node)
    for i=1:no_arc
        add_edge!(graph, start_node[i], end_node[i])
    end
    return graph
end


@everywhere function get_vector(state, origin, destination, link_dic)
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


ta_data = load_ta_network("Sioux Falls")


# unpacking data from ta_data
network_name = ta_data.network_name

number_of_zones = ta_data.number_of_zones
number_of_nodes = ta_data.number_of_nodes
first_thru_node = ta_data.first_thru_node
number_of_links = ta_data.number_of_links

start_node = ta_data.start_node
end_node = ta_data.end_node
capacity = ta_data.capacity
link_length = ta_data.link_length

free_flow_time = ta_data.free_flow_time
B = ta_data.B
power = ta_data.power
speed_limit = ta_data.speed_limit
toll = ta_data.toll
link_type = ta_data.link_type
number_of_zones = ta_data.number_of_zones
total_od_flow = ta_data.total_od_flow
travel_demand = ta_data.travel_demand
od_pairs = ta_data.od_pairs

toll_factor = ta_data.toll_factor
distance_factor = ta_data.distance_factor

best_objective = ta_data.best_objective


# preparing a graph
graph = create_graph(start_node, end_node)
link_dic = sparse(start_node, end_node, 1:number_of_links)


@everywhere function BPR(x)
    # travel_time = free_flow_time .* ( 1.0 + B .* (x./capacity).^power )
    # generalized_cost = travel_time + toll_factor *toll + distance_factor * link_length
    # return generalized_cost

    bpr = similar(x)
    for i=1:length(bpr)
        bpr[i] = free_flow_time[i] * ( 1.0 + B[i] * (x[i]/capacity[i])^power[i] )
        bpr[i] += toll_factor *toll[i] + distance_factor * link_length[i]
    end
    return bpr
end


@everywhere function objective(x)
    # value = free_flow_time .* ( x + B.* ( x.^(power+1)) ./ (capacity.^power) ./ (power+1))
    # return sum(value)

    sum = 0
    for i=1:length(x)
        sum += free_flow_time[i] * ( x[i] + B[i]* ( x[i]^(power[i]+1)) / (capacity[i]^power[i]) / (power[i]+1))
        sum += toll_factor *toll[i] + distance_factor * link_length[i]
    end
    return sum
end


@everywhere function all_or_nothing_single(travel_time)
    state = []
    path = []
    x = zeros(size(start_node))

    for r=1:size(travel_demand)[1]
        # for each origin node r, find shortest paths to all destination nodes
        state = dijkstra_shortest_paths(graph, travel_time, r)

        for s=1:size(travel_demand)[2]
            # for each destination node s, find the shortest-path vector
            # load travel demand
            x = x + travel_demand[r,s] * get_vector(state, r, s, link_dic)
        end
    end

    return x
end


# # parallel computing version
@everywhere function all_or_nothing_parallel(travel_time)
    state = []
    path = []
    vv = zeros(size(start_node))
    x = zeros(size(start_node))

    x = x + @parallel (+) for r=1:size(travel_demand)[1]
        # for each origin node r, find shortest paths to all destination nodes
        # if there is any travel demand starting from node r.
        vv = zeros(size(start_node))

        if sum(travel_demand, 2)[r] > 0.0
            state = dijkstra_shortest_paths(graph, travel_time, r)

            for s=1:size(travel_demand)[2]
                # for each destination node s, find the shortest-path vector
                # v = get_vector(state, r, s, start_node, end_node)

                if travel_demand[r,s] > 0.0
                    # load travel demand
                    vv = vv + travel_demand[r,s] * get_vector(state, r, s, link_dic)
                end
            end

        end

        vv
    end

    return x
end


@everywhere function all_or_nothing(travel_time)
    if nprocs() > 1 # if multiple CPU processes are available
        all_or_nothing_parallel(travel_time)
    else
        all_or_nothing_single(travel_time)
        # when nprocs()==1, using @parallel just adds unnecessary setup time. I guess.
    end
end


# Finding a starting feasible solution
travel_time = BPR(zeros(number_of_links))
xl = all_or_nothing(travel_time)


max_iter_no = 1e10
l = 1
average_excess_cost = 1
tol = 1e-7

while l < max_iter_no
    # Finding yl
    travel_time = BPR(xl)
    yl = all_or_nothing(travel_time)
    xl = xl + (yl - xl)/ (l + 1)
    l = l + 1
    
    # Average Excess Cost
    average_excess_cost = ( dot(xl, travel_time) - dot(yl, travel_time) ) / dot(xl, travel_time)
    
    if average_excess_cost < tol
        break
    end
end


print(xl)







