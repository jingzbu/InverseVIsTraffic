using DataFrames, Resampling


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


