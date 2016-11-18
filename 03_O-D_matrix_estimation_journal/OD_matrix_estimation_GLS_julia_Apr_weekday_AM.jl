
using PyCall
unshift!(PyVector(pyimport("sys")["path"]), "");
@pyimport GLS_Apr_weekday_AM

xi_list = GLS_Apr_weekday_AM.xi_list
P = GLS_Apr_weekday_AM.P
L = GLS_Apr_weekday_AM.L  # dimension of xi

size(P, 1), size(P, 2)

using JuMP

mGLSJulia = Model()

@defVar(mGLSJulia, lam[1:size(P,1)] >= 0)

@defVar(mGLSJulia, p[1:size(P,1), 1:size(P,2)] >= 0)

for i = 1:size(P,1)
    for j = 1:size(P,2)
        if P[i,j] == 0
            @addConstraint(mGLSJulia, p[i,j] == 0)
        end
    end
end
            
for i = 1:size(P,1)
    @addNLConstraint(mGLSJulia, sum{p[i,j], j = 1:size(P,2)} == 1)
end

for l = 1:L
    @addNLConstraint(mGLSJulia, sum{p[i,l] * lam[i], i = 1:size(P,1)} == xi_list[l])
end
    
@setNLObjective(mGLSJulia, Min, sum{p[1,j], j = 1:size(P,2)})  # play no actual role, but could not use zero objective

solve(mGLSJulia)

getValue(lam)

getObjectiveValue(mGLSJulia)

GLS_Apr_weekday_AM.saveDemandVec(getValue(lam))


