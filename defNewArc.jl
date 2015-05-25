type newArc
    flag::Int
    initNode::Int
    termNode::Int 
    capacity::Float64
    freeflowtime::Float64
    trueflow::Float64
    obsflow::Float64
end

newArc(flag::Int, initNode::Int, termNode::Int, capacity::Float64,freeflowtime::Float64) = 
    newArc(flag, initNode, termNode, capacity, freeflowtime, 0., 0.)
