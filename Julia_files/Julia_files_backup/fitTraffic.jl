## Solve an inverse tarffic problem over polynomials of degree at most d
## optionally use a regularizer from the poly kernel

using JuMP
using Gurobi
using Graphs
using Roots


polyEval(coeffs, pt) = sum([coeffs[i] * pt^(i-1) for i = 1:length(coeffs)])  #VG think about faster way to do this
polyEval(coeffs::Array{Float64, 1}, pt) = sum([coeffs[i] * pt^(i-1) for i = 1:length(coeffs)]) #separate for consts

bpacost(flow::Float64, capacity::Float64, freeflowtime::Float64) = freeflowtime*(1 + .15 * (flow/capacity)^4)
bpacost(flow::Float64, arc) = bpacost(flow, arc.capacity, arc.freeflowtime)
bpacost(arc::Arc) = bpacost(arc.obsflow, arc)

function setUpFitting(deg::Int, c, odpairs, nodes)
	m = Model(solver=GurobiSolver(OutputFlag=false))
	@defVar(m, coeffs[1:deg+1])
	@defVar(m, Calphas[1:deg+1])

	##VG Probably want to go back and redo this with an intercept term
	#build the graham matrix
	samples = linspace(0, 1, deg + 1)
	k(x,y) = (c + x*y)^deg
	K = [ k(x,y) for x = samples, y=samples]
	K = convert(Array{Float64, 2}, K)
	assert(rank(K) == deg+1)
	C = chol(K + 1e-6* eye(deg+1))
	for i=1:deg + 1
		@addConstraint(m, polyEval(coeffs, samples[i]) == 
						sum{C[j, i] * Calphas[j], j=1:deg+1})
	end
	@defVar(m, reg_term >= 0)
	reg_term_ = QuadExpr(Calphas[:], Calphas[:], ones(deg+1), AffExpr() )
	@addConstraint(m, reg_term >= reg_term_)

	return m, coeffs, reg_term
end


function fixCoeffs(m, fcoeffs, coeffs)
	for (fc, c) in zip(fcoeffs, coeffs[:])
		@addConstraint(m, fc == c)
	end
end
# function calcTrueCost(coeffs::Array{Float64, 1}, scaled_flows, free_flow_time, capacities)
# 	return sum([free_flow_time[a]*capacities[a]*scaled_flows[a]*polyEval(coeffs, scaled_flows[a]) 
# 				for a=1:length(scaled_flows)])
# end

function addResid(m, coeffs, ys, demands, arcs, scaling)
	@defVar(m, resid)
	@defVar(m, dual_cost)
	@defVar(m, primal_cost)

	@addConstraint(m, dual_cost == sum{demands[(s,t)] * (ys[(s,t), t] - ys[(s,t), s]), (s,t)=keys(demands)})  
	@addConstraint(m, primal_cost == sum{a.obsflow * a.freeflowtime * polyEval(coeffs, a.obsflow/a.capacity), a=values(arcs)})

	@addConstraint(m, resid >= (dual_cost - primal_cost) / scaling )
	@addConstraint(m, resid >= (primal_cost - dual_cost) / scaling )
	return resid
end

function addIncreasingCnsts(m, coeffs, arcs; TOL=0.)
	sorted_flows = sort([a.obsflow / a.capacity for a in values(arcs)])
	@addConstraint(m, polyEval(coeffs, 0) <= polyEval(coeffs, sorted_flows[1]))
	for i = 2:length(sorted_flows)
		@addConstraint(m, polyEval(coeffs, sorted_flows[i-1]) <= polyEval(coeffs, sorted_flows[i]) + TOL)
	end
end

#equates the total cost of the network to the true total cost
function normalize(m, coeffs, tot_true_cost::Float64, arcs)
	@addConstraint(m, 
		sum{a.freeflowtime * a.obsflow * polyEval(coeffs, a.obsflow / a.capacity), 
			a=values(arcs)} == tot_true_cost)
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
		rhs = a.freeflowtime * polyEval(coeffs, a.obsflow/a.capacity)
		for od in keys(demands)
			@addConstraint(m, ys[od, k[2]] - ys[od, k[1]] <= rhs)
		end
	end
	return ys
end

#Uses a Frank-Wolfe algorithm to solve bpa cost for the given network.
#construct the underlying graph
#Fix an ordering of the arcs... should just be pointers
function frank_wolfe(g, vArcs, demand_data, idx; TOL=1e-4, MAX_ITERS=100)
    #use the observed flows as the starting point
    flows =[a.obsflow::Float64 for a in vArcs]
    costs = [bpacost(a) for a in vArcs]
    trace = Float64[]
    for iter = 1:MAX_ITERS
        flow_dict = Dict{(Int, Int), Float64}()
        for odpair = keys(demand_data)
            #solve the shortest path problems, and update the total flow
            r = dijkstra_shortest_paths(g, costs, odpair[1] )
            currNode = odpair[2];
            while currNode != odpair[1]
                parent = r.parents[currNode]
                if ! haskey(flow_dict, (parent, currNode) )
                    flow_dict[(parent, currNode)] = demand_data[odpair][idx]  
                else
                    flow_dict[(parent, currNode)] += demand_data[odpair][idx]  
                end
                currNode = parent
            end
        end

        d = [get(flow_dict, (a.initNode, a.termNode), 0.)::Float64 for a in vArcs]

        #In the first iteration, just pull out the flows
        if iter == 1
        	flows = d
        	costs = [bpacost(flows[ix], a) for (ix, a) in enumerate(vArcs)]
        	continue
        end
        assert( dot(costs, d) <= dot(flows, costs) )
        d -= flows 
        derivFun(alpha) = sum([bpacost(flows[ix] + alpha*d[ix], a)*d[ix] for (ix, a) in enumerate(vArcs)])
        if derivFun(0) >=0 
            alpha = 0
        elseif derivFun(1) <= 0
            alpha = 1
        else
            alpha = fzero(derivFun, 0, 1)
        end
        converge_dist = alpha * norm(d) / norm(flows)
        flows += alpha * d
        push!(trace, converge_dist)
        if (iter > 1) & (converge_dist <= TOL)
            break
        else
            costs = [bpacost(flows[ix], a) for (ix, a) in enumerate(vArcs)]
        end
    end
    # VG Consider doing a polishing step to refine solution at the end...
    # Maybe solve a simplicial assignment on last several extreme pt solutions via 1st order method
    # Maybe switch over to refined step determination from fukushima paper
    return trace[length(trace)], flows
end



