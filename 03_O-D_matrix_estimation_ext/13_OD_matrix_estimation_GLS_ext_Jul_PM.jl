using PyCall
unshift!(PyVector(pyimport("sys")["path"]), "");
@pyimport GLS_Jul_weekday_PM_ext

xi_list = GLS_Jul_weekday_PM_ext.xi_list
P = GLS_Jul_weekday_PM_ext.P
L = GLS_Jul_weekday_PM_ext.L  # dimension of xi

println("dimensions of P are: ")
println(size(P, 1))
println(size(P, 2))
println("--------------------")

# println("xi_list is: ")
# println(xi_list)
println("sum of xi's is: ")
println(sum(xi_list))
println("max of xi's is: ")
println(maximum(xi_list))
println("--------------------")

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

println("lam is: ")
println(getValue(lam))
println("--------------------")

println("objective value is: ")
println(getObjectiveValue(mGLSJulia))
println("--------------------")
println("End")

GLS_Jul_weekday_PM_ext.saveDemandVec(getValue(lam))
