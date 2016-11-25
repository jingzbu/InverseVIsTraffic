using PyCall
unshift!(PyVector(pyimport("sys")["path"]), "");
@pyimport Compute_Jacobian_MA_journal
@pyimport GLS_Apr_weekday_PM_journal

numNodes = Compute_Jacobian_MA_journal.numNodes;
numLinks = Compute_Jacobian_MA_journal.numLinks;
numODpairs = Compute_Jacobian_MA_journal.numODpairs;
numZones = Compute_Jacobian_MA_journal.numZones
od_pairs = Compute_Jacobian_MA_journal.od_pairs;
link_list_js = Compute_Jacobian_MA_journal.link_list_js;
link_length_list = Compute_Jacobian_MA_journal.link_length_list;

flow_observ = GLS_Apr_weekday_PM_journal.x_

include("../Julia_files/initia_data.jl");
include("prepare_data_MA_journal.jl");
include("extract_data_MA_journal.jl");
include("../Julia_files/tap_MSA.jl");
include("../Julia_files/inverseVI.jl");
include("../Julia_files/demands_adjustment_gradi.jl");

# demandsDict_ = readall("../08_develop_new_OD_demand_estimator_MA_Dijkstra_uni_class_Apr_weekend_journal/results/demandsDict.json");
# demandsDict_ = JSON.parse(demandsDict_);

# demandsDict_

# demandsDict__ = demandsDict_["24"]

# _demandsDict__ = Dict()

# for key_ in keys(demandsDict__)
#     key = (int(split(split(key_, ",")[1], "(")[2]),int(split(split(key_, ",")[2], ")")[1]))
#     _demandsDict__[key] = demandsDict__[key_]
# end

# _demandsDict__

# demandsDict[0] = _demandsDict__;
# demandsDict[1] = _demandsDict__;

demandsDict[0] == demandsDict[1]

demandsDiffDict[1] = norm(demandsDicToVec(demandsDict[1]) - demandsDicToVec(demandsDict[0]))/
                     norm(demandsDicToVec(demandsDict[0]));

demandsDiffDict[1]

function demandsDictFixed(day)
#     day = 4  # day of April

    # observed flow vector
    xl = flow_observ[:, day]

    tapFlows = Dict{}()

    for i = 1:length(ta_data.start_node)
        key = (ta_data.start_node[i], ta_data.end_node[i])
        tapFlows[key] = xl[i]
    end

    tapFlowVect = xl;

    # get observed flow vector (corresponding to ground truth demands and ground truth costs)
    tapFlowDicDict[0], tapFlowVecDict[0] = tapFlows, tapFlowVect;

    # get arcs data corresponding to ground truth demands and flows
    arcsDict[0] = observFlow("./benchmark_data/journal_net_Apr_weekend.txt", tapFlowDicDict[0]);

    arcsDict[0]

    deg = 6
    c = 0.5
    lam = 10000.0

    coeffs_dict_Apr_weekend_ = readall("../temp_files/coeffs_dict_Apr_weekend.json")
    coeffs_dict_Apr_weekend_ = JSON.parse(coeffs_dict_Apr_weekend_)
    fcoeffs = coeffs_dict_Apr_weekend_["($(deg),$(c),$(lam),1)"]

    # fcoeffs = [1, 0, 0, .15]

    demandsVecDict[1] = demandsDicToVec(demandsDict[1]);
    objFunDict[1] = objF(demandsVecDict[1], fcoeffs);

    # get initial flow vector (corresponding to initial demands)
    tapFlowDicDict[1], tapFlowVecDict[1] = tapMSA(demandsDict[1], fcoeffs);

    demandsVecDict[0] = demandsDicToVec(demandsDict[0]);

    # get arcs data corresponding to initial demands and flows
    arcsDict[1] = observFlow("./benchmark_data/journal_net_Apr_weekend.txt", tapFlowDicDict[1]);

    linkCostDicDict[1] = tapFlowVecToLinkCostDict(tapFlowVecDict[1], fcoeffs);

    linkCostDicDict[1]["0"], link_length_list[1]

    jacobiSpiessDict[1] = Compute_Jacobian_MA_journal.jacobianSpiess(numNodes, numLinks, numODpairs, od_pairs,
                                                  link_list_js, [linkCostDicDict[1]["$(i)"] for i=0:numLinks-1]);

    # maximum number of iterations
    N = 100;

    # Armijo rule parameters
    rho = 2;
    M = 10;

    # search direction parameter
    epsilon_1 = 0;

    # stop criterion parameter
    epsilon_2 = 1e-20;

    for l = 1:N

        jacobDict[l] = jacobiSpiessDict[l]

        descDirecDict[l] = descDirec(tapFlowVecDict[l], tapFlowVecDict[0], jacobDict[l], numODpairs, numLinks);

        demandsVecDict[l] = demandsDicToVec(demandsDict[l]);

        searchDirecDict[l] = searchDirec(demandsVecDict[l], descDirecDict[l], epsilon_1);

        thetaMaxDict[l] = thetaMax(demandsVecDict[l], searchDirecDict[l]);

        demandsVecDict[l+1] = similar(demandsVecDict[0]);

        demandsVecDict[l+1], objFunDict[l+1] = armijo(objFunDict[l], demandsVecDict[l], fcoeffs, searchDirecDict[l],
        thetaMaxDict[l], rho, M);

        demandsDict[l+1] = demandsVecToDic(demandsVecDict[l+1]);

        tapFlowDicDict[l+1], tapFlowVecDict[l+1] = tapMSA(demandsDict[l+1], fcoeffs);

        arcsDict[l+1] = observFlow("./benchmark_data/journal_net_Apr_weekend.txt", tapFlowDicDict[l+1]);

        linkCostDicDict[l+1] = tapFlowVecToLinkCostDict(tapFlowVecDict[l+1], fcoeffs);

        jacobiSpiessDict[l+1] = Compute_Jacobian_MA_journal.jacobianSpiess(numNodes, numLinks, numODpairs, od_pairs,
                                                  link_list_js, [linkCostDicDict[l+1]["$(i)"] for i=0:numLinks-1]);

        demandsDiffDict[l+1] = norm(demandsVecDict[l+1] - demandsVecDict[0]) / norm(demandsVecDict[0]);

        # stopping criterion
        if (objFunDict[l] - objFunDict[l+1]) / objFunDict[1] < epsilon_2
            break
        end

        println("iteration $(l) finished...")

    end

    # normalize objective function value
    for l = 1:(length(objFunDict))
        norObjFunDict[l] = objFunDict[l] / objFunDict[1];
    end


    outfile = open("./results/demandsVecDict$(day)_journal.json", "w")

    JSON.print(outfile, demandsVecDict)

    close(outfile)

    outfile = open("./results/demandsDict$(day)_journal.json", "w")

    JSON.print(outfile, demandsDict)

    close(outfile)

    outfile = open("./results/tapFlowDicDict$(day)_journal.json", "w")

    JSON.print(outfile, tapFlowDicDict)

    close(outfile)

    outfile = open("./results/tapFlowVecDict$(day)_journal.json", "w")

    JSON.print(outfile, tapFlowVecDict)

    close(outfile)

    demandsDict[length(demandsDict)-1]

    demandsDict_ = Dict{}()

    for key in keys(demandsDict[length(demandsDict)-1])
        demandsDict_[key] = demandsDict[length(demandsDict)-1][key]
    end

    outfile = open("./results/demandsDictFixed$(day)_journal.json", "w")

    JSON.print(outfile, demandsDict_)

    close(outfile)
end

weekend_Apr_list = [1, 7, 8, 14, 15, 21, 22, 28, 29]

# weekend_Apr_list = [6]

for day in weekend_Apr_list
    demandsDictFixed(day)
    println("day $(day) finished...")
end
