
using JSON
using JuMP

using PyCall
unshift!(PyVector(pyimport("sys")["path"]), "");
@pyimport GLS_Apr_weekday_PM_journal

include("../Julia_files/load_network_uni_class.jl")

numLinks = 258;  # number of links
numNodes = 74;  # number of nodes

# #load OD pair-route incidence
# odPairRoute = readstring("od_pair_route_incidence_MA_journal.json");
# odPairRoute = JSON.parse(odPairRoute);

# #load link-route incidence
# linkRoute = readstring("link_route_incidence_MA_journal.json");
# linkRoute = JSON.parse(linkRoute);
# #load OD pair labels
# odPairLabel = readstring("od_pair_label_dict_MA_refined_journal.json");
# odPairLabel = JSON.parse(odPairLabel);

odPairLabel_ = Dict()
idx = 1
for origi = 1:numNodes
    for desti = 1:numNodes
        if origi != desti
            odPairLabel_["$(idx)"] = [origi,desti]
            idx += 1
        end
    end
end

odPairLabel_

# #load link labels
# linkLabel = readstring("link_label_dict_MA_journal.json");
# linkLabel = JSON.parse(linkLabel);

# linkLabel_ = readstring("link_label_dict_MA__journal.json");
# linkLabel_ = JSON.parse(linkLabel_);

#load node-link incidence
nodeLink = readstring("../temp_files/node_link_incidence_MA_journal.json");
nodeLink = JSON.parse(nodeLink);

ta_data = load_ta_network("MA_journal_Apr_PM");

nodeLink

deg = 8
c = 0.5
lam = 10000.0

coeffs_dict_Apr_PM_ = readstring("../temp_files/coeffs_dict_Apr_PM.json")
coeffs_dict_Apr_PM_ = JSON.parse(coeffs_dict_Apr_PM_)
fcoeffs = coeffs_dict_Apr_PM_["($(deg),$(c),$(lam),1)"]

println(fcoeffs)

capacity = ta_data.capacity;
free_flow_time = ta_data.free_flow_time;

function socialObj(linkFlowVec)
    objVal = sum([free_flow_time[a] * fcoeffs[1] * linkFlowVec[a] + 
        free_flow_time[a] * fcoeffs[2] * linkFlowVec[a]^2 / capacity[a] + 
        free_flow_time[a] * fcoeffs[3] * linkFlowVec[a]^3 / capacity[a]^2 + 
        free_flow_time[a] * fcoeffs[4] * linkFlowVec[a]^4 / capacity[a]^3 + 
        free_flow_time[a] * fcoeffs[5] * linkFlowVec[a]^5 / capacity[a]^4 + 
        free_flow_time[a] * fcoeffs[6] * linkFlowVec[a]^6 / capacity[a]^5 + 
        free_flow_time[a] * fcoeffs[7] * linkFlowVec[a]^7 / capacity[a]^6 + 
        free_flow_time[a] * fcoeffs[8] * linkFlowVec[a]^8 / capacity[a]^7 + 
        free_flow_time[a] * fcoeffs[9] * linkFlowVec[a]^9 / capacity[a]^8 for a = 1:numLinks])
    return objVal
end

function POA_MA_Apr_PM_journal_alt(day)

    demandsDict = readstring("../08_develop_new_OD_demand_estimator_MA_Dijkstra_uni_class_Apr_PM_journal/results/demandsDictFixed$(day)_journal.json");
    demandsDict = JSON.parse(demandsDict);

    # demands = demandsDict["$(length(demandsDict)-1)"]

    demands = demandsDict
    
    demands_ = Dict()

    for key in keys(demands)
        key_ = (parse(Int, split(split(key, ',')[1], '(')[2]),parse(Int, split(split(key, ',')[2], ')')[1]))
        demands_[key_] = demands[key]
    end

#     odPairLabel_;

    demandsVec = zeros(5402)

    for i = 1:length(demandsVec)
        demandsVec[i] = demands["($(odPairLabel_["$i"][1]),$(odPairLabel_["$i"][2]))"]
    end

#     demandsVec

#     for key=keys(odPairRoute)
#         if contains(key, "5402-")
#             println(key)
#         end
#     end

#     linkRoute;



    # fcoeffs = [1, 0, 0, 0, .15]
    
    # m = Model(solver=GurobiSolver(OutputFlag=false))
    m = Model()

    @variable(m, linkFlow[1:numLinks])

    @variable(m, odLinkFlow[keys(demands_), 1:numLinks])
    for (s,t) = keys(demands_)
        for k = 1:numLinks
            @constraint(m, odLinkFlow[(s,t), k] >= 0)
        end
    end

    for k = 1:numLinks
        linkFlowPartial = sum([odLinkFlow[(s,t), k] for (s,t) = keys(demands_)])
        @constraint(m, linkFlowPartial == linkFlow[k])
    end

    for l = 1:numNodes
        for (s,t) = keys(demands_)
            if s != t
                odLinkFlowPartial = sum([nodeLink["$(l-1)-$(k-1)"] * odLinkFlow[(s,t), k] for k = 1:numLinks])
                if (l == s)
                    @constraint(m, odLinkFlowPartial + demands_[(s,t)] == 0)
                elseif (l == t)
                    @constraint(m, odLinkFlowPartial - demands_[(s,t)] == 0)
                else
                    @constraint(m, odLinkFlowPartial == 0)
                end
            end
        end
    end

    @NLexpression(m, f, sum{free_flow_time[a] * fcoeffs[1] * linkFlow[a] + 
        free_flow_time[a] * fcoeffs[2] * linkFlow[a]^2 / capacity[a] +
        free_flow_time[a] * fcoeffs[3] * linkFlow[a]^3 / capacity[a]^2 +
        free_flow_time[a] * fcoeffs[4] * linkFlow[a]^4 / capacity[a]^3 +
        free_flow_time[a] * fcoeffs[5] * linkFlow[a]^5 / capacity[a]^4 +
        free_flow_time[a] * fcoeffs[6] * linkFlow[a]^6 / capacity[a]^5 +
        free_flow_time[a] * fcoeffs[7] * linkFlow[a]^7 / capacity[a]^6 +
        free_flow_time[a] * fcoeffs[8] * linkFlow[a]^8 / capacity[a]^7 +
        free_flow_time[a] * fcoeffs[9] * linkFlow[a]^9 / capacity[a]^8, a = 1:numLinks})

    @NLobjective(m, Min, f)

    solve(m)

    println(getvalue(linkFlow))

    getobjectivevalue(m)

    flows = Dict()

    for i = 1:length(ta_data.start_node)
        key = (ta_data.start_node[i], ta_data.end_node[i])
        flows[key] = getvalue(linkFlow)[i]
    end

#     flows

    # getvalue(linkFlow)

    # getobjectivevalue(m)

    flow_user = GLS_Apr_weekday_PM_journal.x_
    
    println(socialObj(flow_user[:, day])/getobjectivevalue(m))
    
    return socialObj(flow_user[:, day])/getobjectivevalue(m)
end

# week_day_Apr_list = [2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20, 23, 24, 25, 26, 27, 30]
week_day_Apr_list = [2]

poaDictAprPM_journal = Dict()

# for day in week_day_Apr_list
#     poaDictAprPM[day] = POA_MA_Apr_PM_journal(day)
# end

for day in week_day_Apr_list
    poaDictAprPM_journal[day] = POA_MA_Apr_PM_journal_alt(day)
end

outfile = open("./results/poaDictAprPM_journal.json", "w")

JSON.print(outfile, poaDictAprPM_journal)

close(outfile)

poaDictAprPM_journal


