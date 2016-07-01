# load flows (output by TAP)

tapFlows = readall("tapFlows.json")
tapFlows = JSON.parse(tapFlows)

# save observed flows to a vector

function observFlowVec(flows, numLinks, link_label_dict)
    x_0 = zeros(numLinks)
    for k = 1:length(x_0)
        key = (int(split(link_label_dict["$(k-1)"], ',')[1]), int(split(link_label_dict["$(k-1)"], ',')[2]))
        x_0[k] = flows[key]
    end
    return x_0
end

x_0 = observFlowVec(flows, numLinks, link_label_dict)

## Obtain $\left( {\frac{{\partial {c_a}\left( {{{\boldsymbol{\lambda}}^l}} \right)}}{{\partial {x_a}}}a \in \mathcal{A}} \right)$ 

fcoeffs = [1, 0, 0, 0.15]

function sa(x, a, fcoeffs, capacity, free_flow_time)  # calculate the partial derivatives of c_a w.r.t. x_a
    assert(a <= length(x) && a >= 1)
    n = length(fcoeffs)
    dcdx = 0
    for i=2:n
        dcdx += (i-1) * fcoeffs[i] * (x[a]/capacity[a])^(i-2)
    end
    dcdx *= free_flow_time[a]/capacity[a]
    return dcdx
end

# save TAP output flows to a vector

function tapFlowVec(tapFlows, numLinks, link_label_dict)
    x = zeros(numLinks)
    for k = 1:length(x)
        key = string((int(split(link_label_dict["$(k-1)"], ',')[1]), int(split(link_label_dict["$(k-1)"], ',')[2])))
        x[k] = tapFlows[key]
    end
    return x
end

# x is TAP output flow vector

x = tapFlowVec(tapFlows, numLinks, link_label_dict)

function saVect(x, fcoeffs, capacity, free_flow_time) 
    saVec = similar(x)
    for a = 1:length(x)
        saVec[a] = sa(x, a, fcoeffs, capacity, free_flow_time) 
    end
    return saVec
end

saVec = saVect(x, fcoeffs, capacity, free_flow_time)

# solve [P2]

using JuMP
using Gurobi

function solveJacob(i_th, saVec, numLinks, numODpairs, numRoutes, linkRoute, odPairRoute)
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
