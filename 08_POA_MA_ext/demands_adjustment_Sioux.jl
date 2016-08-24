type Arc
    initNode::Int 
    termNode::Int 
    capacity::Float64
    freeflowtime::Float64
    flow::Float64
end

Arc(initNode::Int, termNode::Int, capacity::Float64, freeflowtime::Float64) = 
    Arc(initNode, termNode, capacity, freeflowtime, 0.)

## Solve an inverse tarffic problem over polynomials of degree at most d

## Optionally use a regularizer from the poly kernel

using JuMP
using Gurobi
using Graphs
using Roots


polyEval(coeffs, pt) = sum([coeffs[i] * pt^(i-1) for i = 1:length(coeffs)])  

polyEval(coeffs::Array{Float64, 1}, pt) = sum([coeffs[i] * pt^(i-1) for i = 1:length(coeffs)]) 

bpacost(flow::Float64, capacity::Float64, freeflowtime::Float64) = freeflowtime*(1 + .15 * (flow/capacity)^4)
bpacost(flow::Float64, arc) = bpacost(flow, arc.capacity, arc.freeflowtime)
bpacost(arc::Arc) = bpacost(arc.flow, arc)

function setUpFitting(deg::Int, c::Float64)

	m = Model(solver=GurobiSolver(OutputFlag=false))
    
	@defVar(m, coeffs[1:deg+1])
	@defVar(m, Calphas[1:deg+1])

	#build the graham matrix; cf. Ref. [21] (Regularization Networks and Support Vector Machines), page 47
	samples = linspace(0, 1, deg + 1)
	k(x,y) = (c + x*y)^deg
	K = [ k(x,y) for x = samples, y=samples]
	K = convert(Array{Float64, 2}, K)
	#assert(rank(K) == deg+1)
    
	C = chol(K + 1e-6* eye(deg+1))
	for i=1:deg + 1
		@addConstraint(m, polyEval(coeffs, samples[i]) == sum{C[j, i] * Calphas[j], j=1:deg+1})
	end
    
	@defVar(m, reg_term >= 0)
	reg_term_ = QuadExpr(Calphas[:], Calphas[:], ones(deg+1), AffExpr())
    
	@addConstraint(m, reg_term >= reg_term_)
    
	return m, coeffs, reg_term

end

function fixCoeffs(m, fcoeffs, coeffs)
	for (fc, c) in zip(fcoeffs, coeffs[:])
		@addConstraint(m, fc == c)
	end
end

function addResid(m, coeffs, ys, demands, arcs, scaling)
    @defVar(m, resid)
	@defVar(m, dual_cost)
	@defVar(m, primal_cost)

	@addConstraint(m, dual_cost == sum{demands[(s,t)] * (ys[(s,t), t] - ys[(s,t), s]), (s,t)=keys(demands)})  
	@addConstraint(m, primal_cost == sum{a.flow * a.freeflowtime * polyEval(coeffs, a.flow/a.capacity), a=values(arcs)})

	@addConstraint(m, resid >= (dual_cost - primal_cost) / scaling )
	@addConstraint(m, resid >= (primal_cost - dual_cost) / scaling )
	return resid
end

function addIncreasingCnsts(m, coeffs, arcs; TOL=0.)
	sorted_flows = sort([a.flow / a.capacity for a in values(arcs)])
	@addConstraint(m, polyEval(coeffs, 0) <= polyEval(coeffs, sorted_flows[1]))
	for i = 2:length(sorted_flows)
		@addConstraint(m, polyEval(coeffs, sorted_flows[i-1]) <= polyEval(coeffs, sorted_flows[i]) + TOL)
	end
    @addConstraint(m, coeffs[1] == 1)
end

#equates the total cost of the network to the true total cost
function normalize(m, coeffs, tot_true_cost::Float64, arcs)
	@addConstraint(m, 
		sum{a.freeflowtime * a.flow * polyEval(coeffs, a.flow / a.capacity), a=values(arcs)} == tot_true_cost)
end

function normalize(m, coeffs, scaled_flow::Float64, cost::Float64)
	@addConstraint(m, polyEval(coeffs, scaled_flow) == cost)
end

function normalize(m, coeffs, scaled_flows::Array{Float64, 1}, avgCost::Float64)
    @addConstraint(m, sum{polyEval(coeffs, f), f=scaled_flows} == avgCost * length(scaled_flows))
end

function addNetworkCnsts(m, coeffs, demands, arcs, numNodes)
	@defVar(m, ys[keys(demands), 1:numNodes])
	for k = keys(arcs)
		a = arcs[k]
		rhs = a.freeflowtime * polyEval(coeffs, a.flow/a.capacity)
		for od in keys(demands)
			@addConstraint(m, ys[od, k[2]] - ys[od, k[1]] <= rhs)
		end
	end
	return ys
end

############
#Read in the demand file
file = open("../data_original/SiouxFalls_trips.txt")
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
            end
        end
    end
end                
close(file)

############
#read in the arc files
arcs = Dict{(Int, Int), Arc}()
file = open("../data_original/SiouxFalls_net.txt")
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

###########
#read in the initial flows
file = open("../data_original/SiouxFallsFlow.txt")
ix = 0; 
for line in eachline(file)
    ix +=1
    if ix ==1
        continue
    end
    vals = split(line)
    arcs[(int(vals[1]), int(vals[2]))].flow = float(vals[3])
end
close(file)

##########
# Set up demand data and flow data
##########

flow_data = Array(Float64, length(arcs))
flows = Dict{(Int64,Int64), Float64}()
demand_data = Dict{(Int, Int), Array{Float64, 1}}()

numNodes = maximum(map(pair->pair[1], keys(demands)))
g = simple_inclist(numNodes, is_directed=true)
vArcs = Arc[]
for arc in values(arcs)
    add_edge!(g, arc.initNode, arc.termNode) 
    push!(vArcs, arc)
end

for odpair in keys(demands)
    if ! haskey(demand_data, odpair)
        demand_data[odpair] = [demands[odpair], ]
    else
        push!(demand_data[odpair], demands[odpair])
    end
end

flow_data = [a.flow::Float64 for a in vArcs]

for a in vArcs
    flows[(a.initNode, a.termNode)] = a.flow
end

#flows

using JSON

#load node-link incidence
nodeLink = readall("../temp_files/node_link_incidence_Sioux.json");
nodeLink = JSON.parse(nodeLink);

link_label_dict = readall("../temp_files/link_label_dict_Sioux.json");
link_label_dict = JSON.parse(link_label_dict);

link_label_dict["1"]

int(split(link_label_dict["1"], ',')[1]), int(split(link_label_dict["1"], ',')[2])

flows[int(split(link_label_dict["1"], ',')[1]), int(split(link_label_dict["1"], ',')[2])]

#string(1)

function addResid_(m, coeffs, ys, demands_, demands, arcs, scaling)
    @defVar(m, resid)
	@defVar(m, dual_cost)
	@defVar(m, primal_cost)

    for (s,t)=keys(demands)
        @addConstraint(m, demands_[(s,t)] >= 0)
    end

	@addConstraint(m, dual_cost == sum{demands_[(s,t)] * (ys[(s,t), t] - ys[(s,t), s]), (s,t)=keys(demands)})  
	@addConstraint(m, primal_cost == sum{a.flow * a.freeflowtime * polyEval(coeffs, a.flow/a.capacity), a=values(arcs)})

	@addConstraint(m, resid >= (dual_cost - primal_cost) / scaling )
	@addConstraint(m, resid >= (primal_cost - dual_cost) / scaling )
	return resid
end

##########
#Fitting Funcs
##########

function train_cy(lam::Float64, deg::Int, c::Float64, demands, flow_data, arcs; fcoeffs=nothing)
    numNodes = maximum(map(pair->pair[1], keys(arcs)))
    m, coeffs, reg_term = setUpFitting(deg, c)
    
    addIncreasingCnsts(m, coeffs, arcs, TOL=1e-8)  #uses the original obs flows

    avgCost = mean( [bpacost(a.flow, a.capacity, 1.0) for a in values(arcs)] )
    normalize(m, coeffs, [a.flow / a.capacity for a in values(arcs)], avgCost)


    resids = Variable[]
    

    #copy the flow data over to the arcs
    for (ix, a) in enumerate(vArcs)
        a.flow = flow_data[ix]
    end

    #Dual Feasibility
    ys = addNetworkCnsts(m, coeffs, demands, arcs, numNodes)

    #add the residual for this data point
    push!(resids, addResid(m, coeffs, ys, demands, arcs, 1e6))


    if fcoeffs != nothing
        fixCoeffs(m, fcoeffs, coeffs)
    end
    @setObjective(m, Min, sum{resids[i], i = 1:length(resids)} + lam*reg_term)
    solve(m)
    return [getValue(coeffs[i]) for i =1:length(coeffs)], getValue(ys), getValue(resids)
end

#nodeLink["0-75"]

#demands

outfile = open("../temp_files/demands_Sioux.json", "w")

JSON.print(outfile, demands)

close(outfile)

##########
#Fitting Funcs
##########

function train_cd(lam::Float64, deg::Int, c::Float64, ys, flow_data, flows, nodeLink, arcs; fcoeffs=nothing)
    numNodes = maximum(map(pair->pair[1], keys(arcs)))
    m, coeffs, reg_term = setUpFitting(deg, c)
    
    addIncreasingCnsts(m, coeffs, arcs, TOL=1e-8)  #uses the original obs flows

    avgCost = mean( [bpacost(a.flow, a.capacity, 1.0) for a in values(arcs)] )
    normalize(m, coeffs, [a.flow / a.capacity for a in values(arcs)], avgCost)

    resids = Variable[]
    

    #copy the flow data over to the arcs
    for (ix, a) in enumerate(vArcs)
        a.flow = flow_data[ix]
    end

    for k = keys(arcs)
		a = arcs[k]
		rhs = a.freeflowtime * polyEval(coeffs, a.flow/a.capacity)
		for od in keys(demands)
			@addConstraint(m, ys[od, k[2]] - ys[od, k[1]] <= rhs)
		end
	end

    @defVar(m, demands_[keys(demands)])
    
    for (s,t) = keys(demands)
        @addConstraint(m, demands_[(s,t)] >= 0)
        @addConstraint(m, demands_[(s,t)] - demands[(s,t)] <= demands[(s,t)] * 0.05)
        @addConstraint(m, demands[(s,t)] - demands_[(s,t)] <= demands[(s,t)] * 0.05)
    end
    
    numLinks = length(flows)  # number of links
    @defVar(m, odLinkFlow[keys(demands), 1:numLinks])
    for (s,t) = keys(demands)
        for k = 1:numLinks
            @addConstraint(m, odLinkFlow[(s,t), k] >= 0)
        end
    end
    
    for k = 1:numLinks
        linkFlowPartial = sum([odLinkFlow[(s,t), k] for (s,t) = keys(demands)])
        key = (int(split(link_label_dict["$(k-1)"], ',')[1]), int(split(link_label_dict["$(k-1)"], ',')[2]))
        @addConstraint(m, linkFlowPartial == flows[key])
    end

    for l = 1:numNodes
        for (s,t) = keys(demands)
            if s == t
                @addConstraint(m, demands_[(s,t)] == 0)
            else
                odLinkFlowPartial = sum([nodeLink["$(l-1)-$(k-1)"] * odLinkFlow[(s,t), k] for k = 1:numLinks])
                if (l == s)
                    @addConstraint(m, odLinkFlowPartial + demands_[(s,t)] == 0)
                elseif (l == t)
                    @addConstraint(m, odLinkFlowPartial - demands_[(s,t)] == 0)
                else
                    @addConstraint(m, odLinkFlowPartial == 0)
                end
            end
        end
    end
    
    #add the residual for this data point
    push!(resids, addResid_(m, coeffs, ys, demands_, demands, arcs, 1e6))

    if fcoeffs != nothing
        fixCoeffs(m, fcoeffs, coeffs)
    end
    @setObjective(m, Min, sum{resids[i], i = 1:length(resids)} + lam*reg_term)
    solve(m)
    return [getValue(coeffs[i]) for i =1:length(coeffs)], getValue(demands_), getValue(resids)
end

#demands[(1, 1)]

#include("trafficCval.jl")

coeffs_dict = Dict{(Int64,Float64,Float64),Array{Float64,1}}()

deg = 6
c = 3.41
lam = 1.

demands_0 = copy(demands)

fcoeffs, ys, resids = train_cy(lam, deg, c, demands_0, flow_data, arcs)
coeffs_dict[(deg, c, lam)] = fcoeffs

fcoeffs, demands_, resides_ = train_cd(lam, deg, c, ys, flow_data, flows, nodeLink, arcs)
for (s,t) = keys(demands)
    demands_0[(s,t)] = demands_[(s,t)]
end
coeffs_dict[(deg, c, lam)] = fcoeffs

using PyPlot

true_coeffs = [1, 0, 0, 0, .15]

fcoeffs = coeffs_dict[(6, 3.41, 1.)]

xs = linspace(0, 2, 20)
zs_true = map(x->polyEval(true_coeffs, x), xs)

zs = map(x->polyEval(fcoeffs, x), xs)

plot(xs, zs_true, "s-g", label="True")

plot(xs, zs, "^-m", label="deg=6")
legend(loc="upper left",fancybox="true") 

grid("on")
xlim(-0.1, 1.6);
ylim(0.9, 2.0);

font1 = ["family"=>"serif","color"=>"darkred","weight"=>"normal","size"=>14]
xlabel("Scaled Flow", fontdict=font1)
ylabel("Scaled Cost", fontdict=font1)

savefig("fitting_Sioux.pdf")

#demands_0

#demands

# based on https://github.com/chkwon/TrafficAssignment.jl

include("load_network_uni-class.jl")

using Graphs

function create_graph(start_node, end_node)
    @assert Base.length(start_node)==Base.length(end_node)

    no_node = max(maximum(start_node), maximum(end_node))
    no_arc = Base.length(start_node)

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

ta_data = load_ta_network("Sioux Falls");

# ta_data.travel_demand;

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
# travel_demand = ta_data.travel_demand
od_pairs = ta_data.od_pairs

toll_factor = ta_data.toll_factor
distance_factor = ta_data.distance_factor

best_objective = ta_data.best_objective

travel_demand = zeros(24, 24)

for (s,t)=keys(demands)
    travel_demand[s,t] = demands_0[(s,t)]
end

# preparing a graph
graph = create_graph(start_node, end_node)
link_dic = sparse(start_node, end_node, 1:number_of_links);

function BPR(x)
    bpr = similar(x)
    for i=1:length(bpr)
        bpr[i] = free_flow_time[i] * polyEval(fcoeffs, x[i]/capacity[i])
#         bpr[i] = free_flow_time[i] * ( 1.0 + B[i] * (x[i]/capacity[i])^power[i] )
    end
    return bpr
end

function all_or_nothing(travel_time)
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

# Finding a starting feasible solution
travel_time = BPR(zeros(number_of_links))
xl = all_or_nothing(travel_time);

max_iter_no = 1e3
l = 1
#average_excess_cost = 1
tol = 1e-6

while l < max_iter_no
    l += 1
    
    xl_old = xl
    
    # Finding yl
    travel_time = BPR(xl)
    
    yl = all_or_nothing(travel_time)
    
    assert(yl != xl)
    
    xl = xl + (yl - xl)/l
    
    xl_new = xl
    
    relative_gap = norm(xl_new - xl_old, 1) / norm(xl_new, 1)

#     if l % 500 == 0
#         print("l = $l------------------------------------------------\n")
#         print("relative_gap is $relative_gap\n")
#     end

    if relative_gap < tol 
        print("l = $l------------------------------------------------\n")
        print("relative_gap is $relative_gap\n")
        break
    end
    
end

tapFlows = Dict{(Int64,Int64),Float64}()

for i = 1:length(ta_data.start_node)
    key = (ta_data.start_node[i], ta_data.end_node[i])
    tapFlows[key] = xl[i]
end

#tapFlows

#flows

#fcoeffs

function sa(x, a)  # calculate the partial derivatives of c_a w.r.t. x_a
    assert(a <= length(x) && a >= 1)
    n = length(fcoeffs)
    dcdx = 0
    for i=2:n
        dcdx += (i-1) * fcoeffs[i] * (x[a]/capacity[a])^(i-2)
    end
    dcdx *= free_flow_time[a]/capacity[a]
    return dcdx
end

x = zeros(size(start_node))
for k = 1:length(x)
    key = (int(split(link_label_dict["$(k-1)"], ',')[1]), int(split(link_label_dict["$(k-1)"], ',')[2]))
    x[k] = tapFlows[key]
end

x

## Obtain $\left( {\frac{{\partial {c_a}\left( {{g^l}} \right)}}{{\partial {v_a}}};a \in \mathcal{A}} \right)$ 

saVec = similar(x)
for a = 1:length(x)
    saVec[a] = sa(x, a)
end

# saVec[1:5]

#load OD pair-route incidence
odPairRoute = readall("../temp_files/od_pair_route_incidence_Sioux.json");
odPairRoute = JSON.parse(odPairRoute);

#load link-route incidence
linkRoute = readall("../temp_files/link_route_incidence_Sioux.json");
linkRoute = JSON.parse(linkRoute);

#load OD pair labels
odPairLabel = readall("../temp_files/od_pair_label_dict_Sioux.json");
odPairLabel = JSON.parse(odPairLabel);

odPairLabel_ = readall("../temp_files/od_pair_label_dict__Sioux.json");
odPairLabel_ = JSON.parse(odPairLabel_);

# express the demand data as vector (array)

demandsVec = zeros(length(demands))

for i = 1:length(demandsVec)
    demandsVec[i] = demands_0[(odPairLabel_["$i"][1], odPairLabel_["$i"][2])]
end

demandsVec[1:5]

# convert the demand data into dictionary

demandsDict = similar(demands)

for key = keys(demands)
    demandsDict[key] = demandsVec[odPairLabel["($(key[1]), $(key[2]))"]]
end

# "1-200" in keys(odPairRoute)

numLinks = size(start_node)[1]
numRoutes = length(odPairRoute)
numODpairs = numNodes * (numNodes - 1)
