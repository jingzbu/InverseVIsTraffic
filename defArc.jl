type Arc
    initNode::Int 
    termNode::Int 
    capacity::Float64
    freeflowtime::Float64
    trueflow::Float64
    obsflow::Float64
end

Arc(initNode::Int, termNode::Int, capacity::Float64,freeflowtime::Float64) = 
    Arc(initNode, termNode, capacity, freeflowtime, 0., 0.)
