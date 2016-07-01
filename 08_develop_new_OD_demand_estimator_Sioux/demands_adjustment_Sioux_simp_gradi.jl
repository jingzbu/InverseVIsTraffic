using JuMP
using Gurobi

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

function saVect(x, fcoeffs, capacity, free_flow_time) 
    saVec = similar(x)
    for a = 1:length(x)
        saVec[a] = sa(x, a, fcoeffs, capacity, free_flow_time) 
    end
    return saVec
end

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
