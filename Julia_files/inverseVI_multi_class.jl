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
    return convert(Int, combi)
end

function setUpFitting(deg::Int64, c::Float64)
    
    normCoeffs = Array(Float64, deg+1)
    for i=1:deg + 1
        normCoeffs[i] = comb(deg, i-1) * c^(deg-i+1)
    end

    m = Model(solver=GurobiSolver(OutputFlag=false))
    
    @variable(m, coeffs[1:deg+1])

    return m, coeffs, normCoeffs

end

function addResid(m, coeffs, ys_car, ys_truck, demands_car, demands_truck, arcs, scaling)
    @variable(m, resid)
    @variable(m, dual_cost)
    @variable(m, dual_cost_car)
    @variable(m, dual_cost_truck)
    @variable(m, primal_cost)
    @variable(m, primal_cost_car)
    @variable(m, primal_cost_truck)

    @constraint(m, dual_cost_car == sum(demands_car[(s,t)] * (ys_car[(s,t), t] - ys_car[(s,t), s]) for (s,t)=keys(demands_car)))  
    @constraint(m, dual_cost_truck == sum(demands_truck[(s,t)] * (ys_truck[(s,t), t] - ys_truck[(s,t), s]) for (s,t)=keys(demands_truck)))  
    @constraint(m, dual_cost == dual_cost_car + dual_cost_truck)
    
    @constraint(m, primal_cost_car == sum(a.flow_car * 1.0 * a.freeflowtime * polyEval(coeffs, a.flow/a.capacity) for a=values(arcs)))
    @constraint(m, primal_cost_truck == sum(a.flow_truck * 1.1 * a.freeflowtime * polyEval(coeffs, a.flow/a.capacity) for a=values(arcs)))
    @constraint(m, primal_cost == primal_cost_car + primal_cost_truck)
                   
    @constraint(m, resid >= (primal_cost - dual_cost) / scaling)
    @constraint(m, resid >= 0)
    return resid
end

function addIncreasingCnsts(m, coeffs, arcs)
	sorted_flows = sort([a.flow / a.capacity for a in values(arcs)])
	for i = 2:length(sorted_flows)
		@constraint(m, polyEval(coeffs, sorted_flows[i-1]) <= polyEval(coeffs, sorted_flows[i]))
	end
end

function normalize(m, coeffs)
    @constraint(m, coeffs[1] == 1)
    sample_points = linspace(0,1,20)
    for i = 1:length(sample_points)
        @constraint(m, polyEval(coeffs, sample_points[i]) >= 1.0)
    end
end

function addNetworkCnsts(m, coeffs, demands_car, demands_truck, arcs, numNodes)
    @variable(m, ys_car[keys(demands_car), 1:numNodes])
    @variable(m, ys_truck[keys(demands_truck), 1:numNodes])
    for k = keys(arcs)
	a = arcs[k]
	rhs = a.freeflowtime * polyEval(coeffs, a.flow/a.capacity)
	for od in keys(demands_car)
	    @constraint(m, ys_car[od, k[2]] - ys_car[od, k[1]] <= 1.0 * rhs)
	end
	for od in keys(demands_truck)
	    @constraint(m, ys_truck[od, k[2]] - ys_truck[od, k[1]] <= 1.1 * rhs)
	end
    end
return ys_car, ys_truck
end

##########
#Fitting Funcs
##########

function train(lam::Float64, deg::Int, c::Float64, demands_car, demands_truck, arcs)
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
    ys_car, ys_truck = addNetworkCnsts(m, coeffs, demands_car, demands_truck, arcs, numNodes)

    #add the residual for this data point
    push!(resids, addResid(m, coeffs, ys_car, ys_truck, demands_car, demands_truck, arcs, 1e6))
    
    @objective(m, Min, sum(resids[i] for i = 1:length(resids))
                            + lam * sum(coeffs[i] * coeffs[i] / normCoeffs[i] for i=1:deg + 1))
    solve(m)
    
    return [getvalue(coeffs[i]) for i =1:length(coeffs)], getobjectivevalue(m)
end
