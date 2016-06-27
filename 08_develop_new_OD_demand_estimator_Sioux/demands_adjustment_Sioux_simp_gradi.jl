using JSON

type Arc
    initNode::Int 
    termNode::Int 
    capacity::Float64
    freeflowtime::Float64
    flow::Float64
end

Arc(initNode::Int, termNode::Int, capacity::Float64, freeflowtime::Float64) = 
    Arc(initNode, termNode, capacity, freeflowtime, 0.)

### Prepare data

############
#Read in the demand file
file = open("../data_original/SiouxFalls_trips_simp.txt")
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
file = open("../data_original/SiouxFalls_net_simp.txt")
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
file = open("../data_original/flows_converge_simp.txt")
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
using Graphs

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

tapFlows = flows

include("load_network_uni-class.jl")

ta_data = load_ta_network("Sioux_simp");

start_node = ta_data.start_node;
capacity = ta_data.capacity
free_flow_time = ta_data.free_flow_time

numLinks = size(start_node)[1];
numODpairs = numNodes * (numNodes - 1);

numRoutes = readall("numRoutes.json");
numRoutes = JSON.parse(numRoutes);

#load OD pair-route incidence
odPairRoute = readall("od_pair_route_incidence_Sioux_simp.json");
odPairRoute = JSON.parse(odPairRoute);

#load link-route incidence
linkRoute = readall("link_route_incidence_Sioux_simp.json");
linkRoute = JSON.parse(linkRoute);

link_label_dict = readall("link_label_dict_Sioux_simp.json");
link_label_dict = JSON.parse(link_label_dict);

fcoeffs = [1, 0, 0, 0, .15]

using JuMP
using Gurobi

## Obtain $\left( {\frac{{\partial {c_a}\left( {{g^l}} \right)}}{{\partial {v_a}}};a \in \mathcal{A}} \right)$ 

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

saVec = similar(x)
for a = 1:length(x)
    saVec[a] = sa(x, a)
end

# solve [P2]
function solveJacob(i_th)
    assert(i_th >= 1 && i_th <= numODpairs)
    
    jacobi = Model(solver=GurobiSolver(OutputFlag=false))

    @defVar(jacobi, d[1:numLinks])
    @defVar(jacobi, x[1:numRoutes])

    for i=1:numODpairs
        sumLamX = 0
        for j=1:numRoutes
            if "$(i)-$(j)" in keys(odPairRoute)
                sumLamX += x[j]
            end
        end
        if i == i_th
            @addConstraint(jacobi, sumLamX == 1)
        else
            @addConstraint(jacobi, sumLamX == 0)
        end
    end

    for i=1:numLinks
        sumDeltaX = 0
        for j=1:numRoutes
            if "$(i)-$(j)" in keys(linkRoute)
                sumDeltaX += x[j]
            end
        end
        @addConstraint(jacobi, sumDeltaX == d[i])
    end

    @setObjective(jacobi, Min, sum{saVec[i] * (d[i])^2, i = 1:length(numLinks)})

    solve(jacobi)

    return getValue(d)
end

numRoutes
