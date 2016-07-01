using JuMP
using Gurobi

polyEval(coeffs, pt) = sum([coeffs[i] * pt^(i-1) for i = 1:length(coeffs)])  

function facto(m::Int64)
    factori = 1
    for j = 1:m
        factori = factori * j
    end
    return factori
end

function comb(n::Int64, m::Int64)
    combi = facto(n) / (facto(m) * facto(n-m))
    return int(combi)
end

function setUpFitting(deg::Int64, c::Float64)
    
    normCoeffs = Array(Float64, deg+1)
    for i=1:deg + 1
        normCoeffs[i] = comb(deg, i-1) * c^(deg-i+1)
    end

	m = Model(solver=GurobiSolver(OutputFlag=false))
    
	@defVar(m, coeffs[1:deg+1])

	return m, coeffs, normCoeffs

end

function addResid(m, coeffs, ys, demands, arcs, scaling)
    @defVar(m, resid)
	@defVar(m, dual_cost)
	@defVar(m, primal_cost)

	@addConstraint(m, dual_cost == sum{demands[(s,t)] * (ys[(s,t), t] - ys[(s,t), s]), (s,t)=keys(demands)})  
	@addConstraint(m, primal_cost == sum{a.flow * a.freeflowtime * polyEval(coeffs, a.flow/a.capacity), a=values(arcs)})
	@addConstraint(m, resid >= (primal_cost - dual_cost) / scaling )

	return resid
end

function addIncreasingCnsts(m, coeffs, arcs)
	sorted_flows = sort([a.flow / a.capacity for a in values(arcs)])
	for i = 2:length(sorted_flows)
		@addConstraint(m, polyEval(coeffs, sorted_flows[i-1]) <= polyEval(coeffs, sorted_flows[i]))
	end
end

function normalize(m, coeffs)
    @addConstraint(m, coeffs[1] == 1)
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


##########
#Fitting Funcs
##########

function train(lam::Float64, deg::Int, c::Float64, demands, arcs; fcoeffs=nothing)
    numNodes = maximum(map(pair->pair[1], keys(arcs)))
    m, coeffs, normCoeffs = setUpFitting(deg, c)
    
    addIncreasingCnsts(m, coeffs, arcs)  #uses the original obs flows

    normalize(m, coeffs)

    resids = Variable[]

    vArcs = Arc[]
    for arc in values(arcs)
        push!(vArcs, arc)
    end
    
    flow_data = [a.flow::Float64 for a in vArcs]

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
    
    @setObjective(m, Min, sum{resids[i], i = 1:length(resids)} 
                            + lam * sum{coeffs[i] * coeffs[i] / normCoeffs[i], i=1:deg + 1})
    solve(m)
    
    return [getValue(coeffs[i]) for i =1:length(coeffs)], getValue(ys), getValue(resids)
end
