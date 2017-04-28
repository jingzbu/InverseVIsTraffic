# InverseVIsTraffic

This is a repository containing all the code for our ongoing Eastern Massachusetts transportation application project.

The Julia code for solving the inverse Variational Inequality problem is based on the repository [InverseVIs](https://github.com/vgupta1/InverseVIs); an important modification is the calculation of the objective function. In addition, the normalization constraint has also been updated, which, we believe, is more natural in this particular application.


## INRIX real data processing

Due to confidentiality of the data, currently the raw INRIX dataset can not be made publicly available. When dealing with this dataset, both Python and Julia have been used.

## EMA benchmark network releasing

We have recently released our Eastern Massachusetts highway network as a benchmark dataset; see [Github](https://github.com/bstabler/TransportationNetworks/tree/master/Eastern-Massachusetts) or [Kaggle](https://www.kaggle.com/jingzbu/ematransportation). Interested readers are welcome to download the dataset and cite the following papers.


## Related publications

Jing Zhang, Sepideh Pourazarm, Christos G. Cassandras, and Ioannis Ch. Paschalidis, "***The Price of Anarchy in Transportation Networks by Estimating User Cost Functions from Actual Traffic Data***," Proceedings of the 55th IEEE Conference on Decision and Control, pp. 789-794, December 12-14, 2016, Las Vegas, NV, USA, Invited Session Paper.

Jing Zhang, Sepideh Pourazarm, Christos G. Cassandras, and Ioannis Ch. Paschalidis, "***Data-driven Estimation of Origin-Destination Demand and User Cost Functions for the Optimization of Transportation Networks***," The 20th World Congress of the International Federation of Automatic Control, July 9-14, 2017, Toulouse, France, accepted as Invited Session Paper. [arXiv:1610.09580](https://arxiv.org/abs/1610.09580#)

Jing Zhang and Ioannis Ch. Paschalidis, "***Data-Driven Estimation of Travel Latency Cost Functions via Inverse Optimization in Multi-Class Transportation Networks***," Proceedings of the 56th IEEE Conference on Decision and Control, December 12-15, 2017, Melbourne, Australia, submitted. [arXiv:1703.04010](https://arxiv.org/abs/1703.04010)

Jing Zhang, Sepideh Pourazarm, Christos G. Cassandras, and Ioannis Ch. Paschalidis, "***The Price of Anarchy in Transportation Networks: Data-Driven Evaluation and Reduction Strategies***," Proceedings of the IEEE: special issue on "Smart Cities," in preparation.


## Licensing

This code is available under the MIT License.
Copyright (c) 2016 Jing Zhang


## Author

Jing Zhang

Jing Zhang currently is a PhD student in the Division of Systems Engineering at Boston University, working with Professor [Yannis Paschalidis](http://sites.bu.edu/paschalidis/).


Email: `jzh@bu.edu`

Homepage: http://people.bu.edu/jzh/
