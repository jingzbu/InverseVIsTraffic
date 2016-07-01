using JuMP

function TAP(demands)

    #load OD pair labels
    odPairLabel = readall("od_pair_label_dict_Sioux_simp_refined.json")
    odPairLabel = JSON.parse(odPairLabel)

    odPairLabel_ = readall("od_pair_label_dict__Sioux_simp_refined.json")
    odPairLabel_ = JSON.parse(odPairLabel_)

    #load link labels
    linkLabel = readall("link_label_dict_Sioux_simp.json")
    linkLabel = JSON.parse(linkLabel)

    linkLabel_ = readall("link_label_dict_Sioux_simp_.json")
    linkLabel_ = JSON.parse(linkLabel_)

    #load node-link incidence
    nodeLink = readall("node_link_incidence_Sioux_simp.json")
    nodeLink = JSON.parse(nodeLink)

    start_node = ta_data.start_node

    demandsVec = zeros(length(odPairLabel_))

    for i = 1:length(demandsVec)
        demandsVec[i] = demands[(odPairLabel_["$i"][1], odPairLabel_["$i"][2])]
    end

    # m = Model(solver=GurobiSolver(OutputFlag=false))
    m = Model()

    @defVar(m, linkFlow[1:numLinks])

    @defVar(m, odLinkFlow[keys(demands), 1:numLinks])
    for (s,t) = keys(demands)
        for k = 1:numLinks
            @addConstraint(m, odLinkFlow[(s,t), k] >= 0)
        end
    end

    for k = 1:numLinks
        linkFlowPartial = sum([odLinkFlow[(s,t), k] for (s,t) = keys(demands)])
        @addConstraint(m, linkFlowPartial == linkFlow[k])
    end

    for l = 1:numNodes
        for (s,t) = keys(demands)
            if s != t
                odLinkFlowPartial = sum([nodeLink["$(l-1)-$(k-1)"] * odLinkFlow[(s,t), k] for k = 1:numLinks])
                if (l == s)
                    @addConstraint(m, odLinkFlowPartial + demands[(s,t)] == 0)
                elseif (l == t)
                    @addConstraint(m, odLinkFlowPartial - demands[(s,t)] == 0)
                else
                    @addConstraint(m, odLinkFlowPartial == 0)
                end
            end
        end
    end

    @defNLExpr(f, sum{free_flow_time[a]*linkFlow[a] + .03*free_flow_time[a]*((linkFlow[a])^5)/((capacity[a])^4), 
        a = 1:numLinks})
#     @defNLExpr(f, sum{free_flow_time[a]*linkFlow[a] + .15*free_flow_time[a]*((linkFlow[a])^2)/(capacity[a]), 
#         a = 1:numLinks})

    @setNLObjective(m, Min, f)

    TT = STDOUT # save original STDOUT stream
    redirect_stdout()
    solve(m)
    redirect_stdout(TT) # restore STDOUT

    tapFlowVect = getValue(linkFlow)

    tapFlows = Dict{(Int64,Int64),Float64}()

    for i = 1:length(ta_data.start_node)
        key = (ta_data.start_node[i], ta_data.end_node[i])
        tapFlows[key] = tapFlowVect[i]
    end

#    getObjectiveValue(m)

    return tapFlows, tapFlowVect
end
