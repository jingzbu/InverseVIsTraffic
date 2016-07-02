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

function solveJacob(i_th, tapFlowVec, fcoeffs, capacity, free_flow_time, numLinks, numODpairs, numRoutes, linkRoute, odPairRoute)
    assert(i_th >= 1 && i_th <= numODpairs)
    
    saVec = saVect(tapFlowVec, fcoeffs, capacity, free_flow_time)

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

function jacobian(tapFlowVec, fcoeffs, capacity, free_flow_time, numLinks, numODpairs, 
    numRoutes, linkRoute, odPairRoute)
    jacob = @parallel vcat for i=1:numODpairs
        solveJacob(i, tapFlowVec, fcoeffs, capacity, free_flow_time, numLinks, 
        numODpairs, numRoutes, linkRoute, odPairRoute)
    end
    jacob = reshape(jacob, numODpairs, numLinks)
    return jacob
end

# compute the gradient
function gradient(tapFlowVec, observFlowVec, jacob, numODpairs, numLinks)
    gradi = zeros(numODpairs)
    for i = 1:numODpairs
        gradi[i] = sum([2 * (tapFlowVec[j] - observFlowVec[j]) * jacob[i, j] for j = 1:numLinks])
    end
    return gradi
end

# compute a descent direction
function descDirec(tapFlowVec, observFlowVec, jacob, numODpairs, numLinks)
    gradi = gradient(tapFlowVec, observFlowVec, jacob, numODpairs, numLinks)
    h = similar(gradi)
    for i = 1:length(gradi)
        h[i] = -1 * gradi[i]
    end
    return h
end

# compute a search direction
function searchDirec(demandsVec, descDirect, epsilon_1)
    h = descDirect
    h_ = similar(h)
    for i = 1:length(h)
            if (demandsVec[i] > epsilon_1) || (demandsVec[i] <= epsilon_1 && h[i] > 0)
            h_[i] = h[i]
        else
            h_[i] = 0
        end
    end
    return h_
end

# line search
function thetaMax(demandsVec, searchDirect)
    h_ = searchDirect
    thetaList = Float64[]
    for i = 1:length(h_)
        if h_[i] < 0
            push!(thetaList, - demandsVec[i]/h_[i])
        end
    end
    theta_max = minimum(thetaList)
    return theta_max
end
