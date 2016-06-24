InverseVIsTraffic
======

This is a repository containing code for the ongoing project "Estimating cost functions in multi-class-user transportation networks via inverse optimization."

The Julia code for solving the inverse Variational Inequality problem is based on the repo [InverseVIs](https://github.com/vgupta1/InverseVIs); an important modification is the calculation of the objective function. Interested readers could find the difference [here](https://github.com/jingzbu/InverseVIsTraffic/blob/master/08_develop_new_OD_demand_estimator_MA/08_InverseVI_uni_MA_with_base_trans_python.ipynb) (cell 15) and [here](https://github.com/vgupta1/InverseVIs/blob/master/Traffic/trafficCval.jl#L149). In addition, the normalization constraint has also been updated, which, we believe, is more natural in this particualr application. Interested readers could find this constraint [here](https://github.com/jingzbu/InverseVIsTraffic/blob/master/08_develop_new_OD_demand_estimator_MA/08_InverseVI_uni_MA_with_base_trans_python.ipynb) (cell 15) and [here](https://github.com/vgupta1/InverseVIs/blob/master/Traffic/fitTraffic.jl#L84).


INRIX real data processing
====

Due to confidentiality of the data, currently the whole INRIX dataset can not be made publicly available. When dealing with this dataset, 
both Python and Julia are used.


Author
===
Jing Zhang

Jing Zhang currently is a PhD student in the Division of Systems Engineering at Boston University, working with Professor [Yannis Paschalidis](http://sites.bu.edu/paschalidis/).


Email: `jzh@bu.edu`

Homepage: http://people.bu.edu/jzh/
