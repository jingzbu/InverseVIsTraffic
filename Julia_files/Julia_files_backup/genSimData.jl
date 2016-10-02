## File that runs the entire cross-val analysis and dumps it for the traffic stuff


#include("fitTraffic.jl")
#using PyPlot


##########
#Generate the simulated data
##########
numData = 1; sigma = .05
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

#srand(8675309)
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
