
using PyCall
unshift!(PyVector(pyimport("sys")["path"]), "");
@pyimport GLS_Apr_weekday_PM

# x = GLS_Apr_weekday_PM.x; # sample matrix, each column is a link flow vector sample; number_of_links * K
# S = GLS_Apr_weekday_PM.S; # sample covariance matrix
# A = GLS_Apr_weekday_PM.A; # link_route incidence matrix
P = GLS_Apr_weekday_PM.P; # route_choice_probability_matrix
# Q = GLS_Apr_weekday_PM.Q; 
L = GLS_Apr_weekday_PM.L; # dimension of xi
number_of_routes = GLS_Apr_weekday_PM.number_of_routes;
number_of_links = GLS_Apr_weekday_PM.number_of_links;

# A = sparse(A);
P = sparse(P);
# Q = sparse(Q);

# K = size(x, 2)

# inv_S = inv(S)

# A_t = transpose(A)

# b = sum([A_t * inv_S * x[:, k] for k = 1:K])

using JuMP

# model = Model(solver=IpoptSolver())

# @variable(model, xi[1:L] >= 0)

# # Set objective: (K/2) xi' * Q * xi - b' * xi
# obj = 0
# for i = 1:L
#     for j = 1:L
#         obj += (1.0 / 2) * K * xi[i] * Q[i, j] * xi[j]
#     end
# end
# for l = 1:L
#     obj += - b[l] * xi[l]
# end

# @NLobjective(model, Min, obj) 

# solve(model)

# xi_list = getvalue(xi)

xi_list = GLS_Apr_weekday_PM.xi_list

mGLSJulia = Model()

@variable(mGLSJulia, lam[1:size(P,1)] >= 0)

@variable(mGLSJulia, p[1:size(P,1), 1:size(P,2)] >= 0)

for i = 1:size(P,1)
    for j = 1:size(P,2)
        if P[i,j] == 0
            @constraint(mGLSJulia, p[i,j] == 0)
        end
    end
end
            
for i = 1:size(P,1)
    @NLconstraint(mGLSJulia, sum{p[i,j], j = 1:size(P,2)} == 1)
end

for l = 1:L
    @NLconstraint(mGLSJulia, sum{p[i,l] * lam[i], i = 1:size(P,1)} == xi_list[l])
end
    
@NLobjective(mGLSJulia, Min, sum{p[1,j], j = 1:size(P,2)})  # play no actual role, but could not use zero objective

solve(mGLSJulia)

getvalue(lam)

getobjectivevalue(mGLSJulia)
