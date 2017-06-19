using JuMP
using Gurobi


# compute the gradient
function gradient(gamma1, gamma2, demandsVecCar, demandsVecCar0, demandsVecTruck, demandsVecTruck0, tapFlowVec, observFlowVec, jacob, numODpairs, numLinks)
    gradi = zeros(2, numODpairs)
    for i = 1:numODpairs
        gradi[1, i] = 2 * gamma1 * (demandsVecCar[i] - demandsVecCar0[i]) + 2 * gamma2 * sum([(tapFlowVec[1, j] - observFlowVec[1, j]) * jacob[i, j, 1] for j = 1:numLinks]) 
        gradi[2, i] = 2 * gamma1 * (demandsVecTruck[i] - demandsVecTruck0[i]) + 2 * gamma2 * sum([(tapFlowVec[2, j] - observFlowVec[2, j]) * jacob[i, j, 2] for j = 1:numLinks]) 
    end
    return gradi
end

# compute a descent direction
function descDirec(gamma1, gamma2, demandsVecCar, demandsVecCar0, demandsVecTruck, demandsVecTruck0, tapFlowVec, observFlowVec, jacob, numODpairs, numLinks)
    gradi = gradient(gamma1, gamma2, demandsVecCar, demandsVecCar0, demandsVecTruck, demandsVecTruck0, tapFlowVec, observFlowVec, jacob, numODpairs, numLinks)
    h = similar(gradi)
    for k = 1:size(gradi)[1]
        for i = 1:size(gradi)[2]
                h[k, i] = -1 * gradi[k, i]
        end
    end
    return h
end

# compute a search direction
function searchDirec(demandsVecCar, demandsVecTruck, descDirect, epsilon_1)
    h = descDirect
    h_ = similar(h)
    for i = 1:size(h)[2]
        if (demandsVecCar[i] > epsilon_1) || (demandsVecCar[i] <= epsilon_1 && h[1, i] > 0)
            h_[1, i] = h[1, i]
        else
            h_[1, i] = 0
        end
        if (demandsVecTruck[i] > epsilon_1) || (demandsVecTruck[i] <= epsilon_1 && h[2, i] > 0)
            h_[2, i] = h[2, i]
        else
            h_[2, i] = 0
        end
    end
    return h_
end

# line search
function thetaMax(demandsVecCar, demandsVecTruck, searchDirect)
    h_ = searchDirect
    thetaList = Float64[]
    for i = 1:size(h_)[2]
        if h_[1, i] < 0
            push!(thetaList, - demandsVecCar[i]/h_[1, i])
        end
        if h_[2, i] < 0
            push!(thetaList, - demandsVecTruck[i]/h_[2, i])
        end
    end
    theta_max = minimum(thetaList)
    return theta_max
end

# Armijo line search and update
function objF(gamma1, gamma2, demandsVecCar, demandsVecCar0, demandsVecTruck, demandsVecTruck0, fcoeffs)
    demandsDicCar = demandsVecToDic(demandsVecCar)
    demandsDicTruck = demandsVecToDic(demandsVecTruck)
    tapFlowVec = tapMSA_Multi(demandsDicCar, demandsDicTruck, fcoeffs)[2]
    return gamma1 * sum([(demandsVecCar[i] - demandsVecCar0[i])^2 for i = 1:length(demandsVecCar)]) + gamma1 * sum([(demandsVecTruck[i] - demandsVecTruck0[i])^2 for i = 1:length(demandsVecTruck)]) + gamma2 * sum([(tapFlowVec[1, j] - tapFlowVecDict[0][1, j])^2 for j = 1:numLinks]) + gamma2 * sum([(tapFlowVec[2, j] - tapFlowVecDict[0][2, j])^2 for j = 1:numLinks])
end     

function armijo(gamma1, gamma2, objFunOld, demandsVecCarOld, demandsVecTruckOld, demandsVecCar0, demandsVecTruck0, fcoeffs, searchDirec, thetaMax, Theta, N)
    demandsVecCarList = Array{Float64}[]
    demandsVecTruckList = Array{Float64}[]
    objFunList = Float64[]
    push!(demandsVecCarList, demandsVecCarOld)
    push!(demandsVecTruckList, demandsVecTruckOld)
    push!(objFunList, objFunOld)
    for n = 0:N
        demandsVecCarNew = similar(demandsVecCarOld)
        demandsVecTruckNew = similar(demandsVecTruckOld)
        for i = 1:length(demandsVecCarOld)
            demandsVecCarNew[i] = demandsVecCarOld[i] + (thetaMax/(Theta^n)) * searchDirec[1, i] 
        end
        for i = 1:length(demandsVecTruckOld)
            demandsVecTruckNew[i] = demandsVecTruckOld[i] + (thetaMax/(Theta^n)) * searchDirec[2, i] 
        end
    	push!(demandsVecCarList, demandsVecCarNew)
    	push!(demandsVecTruckList, demandsVecTruckNew)
    	push!(objFunList, objF(gamma1, gamma2, demandsVecCarNew, demandsVecCar0, demandsVecTruckNew, demandsVecTruck0, fcoeffs))
    end
    idx = indmin(objFunList)
    objFunNew = objFunList[idx]
    assert(objFunNew <= objFunOld)
    return demandsVecCarList[idx], demandsVecTruckList[idx], objFunNew
end
