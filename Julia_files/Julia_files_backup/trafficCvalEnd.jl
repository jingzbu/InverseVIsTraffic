df = DataFrame()
df[:A] = 1:numData

lamb_grid = [10. .^(-7:1)]
c_grid = linspace(1, 5, 6)  # This choice of c_grid yields no distinguishable difference. Try: c_grid = 2. .^(1:5)
deg_grid = [2:6]    #2 is a pretty meaningless choice.  drop to 3.
N = length(lamb_grid) * length(c_grid) * length(deg_grid)

res = Array(Float64, N, 5)
ix = 1
for l in lamb_grid
    for c in c_grid
        for d in deg_grid
            train(df) = train(df[:A], l, d, c, demand_data, flow_data, arcs)
            test(df, fit) = test(fit, df[:A], demand_data, flow_data, arcs, g, vArcs)
            rtrain, rtest = kfold_crossvalidate(df, train, test, 5)
            
            res[ix, 1] = l
            res[ix, 2] = c
            res[ix, 3] = float(d)
            res[ix, 4] = mean(rtest) / 1e6
            res[ix, 5] = std(rtest) / 1e6
            ix +=1

            show(res)
        end
    end
end

writetable("trafficCVal.csv", DataFrame(res))
