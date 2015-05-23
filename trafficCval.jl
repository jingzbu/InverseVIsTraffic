using DataFrames, Resampling

## File that runs the entire cross-val analysis and dumps it for the traffic stuff
type Arc
	initNode::Int
	termNode::Int 
    capacity::Float64
    freeflowtime::Float64
    trueflow::Float64
    obsflow::Float64
end

Arc(initNode::Int, termNode::Int, capacity::Float64,freeflowtime::Float64) = 
    Arc(initNode, termNode, capacity, freeflowtime, 0., 0.)

include("fitTraffic.jl")

############
#Read in the demand file
file = open("SiouxFalls_trips.txt")
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
file = open("SiouxFalls_net.txt")
inHeader=true
for line in eachline(file)
    if inHeader
        inHeader = !contains(line, "Init node")
        continue
    end
    vals = split(line, )
    arcs[(int(vals[1]), int(vals[2]))] = Arc(int(vals[1]), int(vals[2]), 
                                              float(vals[3]), float(vals[5]))
end
close(file)

###########
#read in the true costs
file = open("SiouxFallsFlow.txt")
ix = 0; test_cost = 0.0
for line in eachline(file)
    ix +=1
    if ix ==1
        continue
    end
    vals = split(line)
    arcs[(int(vals[1]), int(vals[2]))].trueflow = float(vals[3])
    test_cost += float(vals[4])
end
tot_cost = sum(map(a -> bpacost(a.trueflow, a), values(arcs) ))
assert( abs( tot_cost - test_cost) <= 1e-8 ) #note, these costs are not scaled by x!!!

##########
#Generate the simulated data
##########
numData = 20 ; sigma = .1
flow_data = Array(Float64, length(arcs), numData)
demand_data = Dict{(Int, Int), Array{Float64, 1}}()

numNodes = maximum(map(pair->pair[1], keys(demands)))
g = simple_inclist(numNodes, is_directed=true)
vArcs = Arc[]
for arc in values(arcs)
    arc.obsflow = arc.trueflow
    add_edge!(g, arc.initNode, arc.termNode) 
    push!(vArcs, arc)
end

srand(8675309)
for iRun = 1:numData
    #perturb the demand_data
    for odpair in keys(demands)
        if ! haskey(demand_data, odpair)
            demand_data[odpair] = [demands[odpair] * (1 + sigma * rand()), ]
        else
            push!(demand_data[odpair], demands[odpair] * (1  + sigma * rand()))
        end
    end
    #solve using FW and record
    conv_tol, flow_data[:, iRun] = frank_wolfe(g, vArcs, demand_data, iRun)
    println(conv_tol)
end

#Randomzie the flow data a little bit too
for i = 1:size(flow_data, 1)
    for j = 1:size(flow_data, 2)
        flow_data[i, j] *= (1 + sigma * rand() )
    end
end

##########
#Fitting Funcs
##########
#build a little train function that just takes indices
function train(indices, lam::Float64, deg::Int, c::Float64, 
                demand_data, flow_data, arcs; fcoeffs=nothing)
    numNodes = maximum(map(pair->pair[1], keys(arcs)))
    m, coeffs, reg_term = setUpFitting(deg, c, [k for k=keys(demand_data)], 1:numNodes)
    
    for a in values(arcs)
        a.obsflow = a.trueflow
    end
    addIncreasingCnsts(m, coeffs, arcs, TOL=1e-8)  #uses the original obs flows

    avgCost = mean( [bpacost(a.obsflow, a.capacity, 1.0) for a in values(arcs)] )
    normalize(m, coeffs, [a.obsflow / a.capacity for a in values(arcs)], avgCost)

    # normalize(m, coeffs, 1., bpacost(1., 1., 1.))


    resids = Variable[]
    for i = indices
        #copy the flow data over to the arcs, demand data to demands (slow)
        for (ix, a) in enumerate(vArcs)
            a.obsflow = flow_data[ix, i]
        end
        for odpair in keys(demands)
            demands[odpair] = demand_data[odpair][i]
        end
    
        #Dual Feasibility
        ys = addNetworkCnsts(m, coeffs, demands, arcs, numNodes)
        
        #add the residual for this data point
        push!(resids, addResid(m, coeffs, ys, demands, arcs, 1e6))
    end

    if fcoeffs != nothing
        fixCoeffs(m, fcoeffs, coeffs)
    end
    @setObjective(m, Min, sum{resids[i], i = 1:length(resids)} + lam*reg_term)
    solve(m)
    println(getObjectiveValue(m) - lam * getValue(reg_term) )
    return [getValue(coeffs[i]) for i =1:length(coeffs)]
end

# a function for testing.
function test(fcoeffs, indices, demand_data, flow_data, arcs, g, vArcs)
    numNodes = maximum(map(pair->pair[1], keys(arcs)))

    l1_eps = 0.
    for i = indices
        costs = [polyEval(fcoeffs, flow_data[ix, i]/a.capacity)*a.freeflowtime 
                    for (ix, a) in enumerate(vArcs)]
        primal = dot(costs, flow_data[:, i])
        
        #solve a bunch of shortest path problems to get dual cost
        dual = 0.
        for odpair = keys(demand_data)
            #solve the shortest path problems, and update the total flow
            r = dijkstra_shortest_paths(g, costs, odpair[1] )
            dual += r.dists[odpair[2]] * demand_data[odpair][i]
        end            
        l1_eps += abs(primal - dual)
    end
    return l1_eps / length(indices)
end


