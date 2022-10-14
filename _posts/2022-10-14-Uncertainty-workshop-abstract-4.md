---
tags: workshop2022abstract
title: "Uncertainty analysis of Supervised ML predictions applied to lithology classification in Geosteering (Alina Shashel, University of Stavanger)"
presentation_date: 2022-11-01
---
#### Presenter
**Alina Shashel** from University of Stavanger
#### Co-authors
Dan Sui and Jie Cao (UiS)
## Abstract
Geosteering demands a thorough survey of the lithological properties of the surrounding geological strata. Drill bit and drill string performances are the earliest signals to determine formations' characteristics. Implementing automated lithology identification using machine learning (ML) would enhance the quality of the geosteering operation due to its powerful data analysis competency via learning from data, identifying data patterns, and making logical decisions in an automatic manner. This paper investigated the extent to which various supervised ML classification algorithms can be utilized to recognize the lithological features of drilled formations.



Supervised ML models were trained using preprocessed real-time drilling data from the Volve field located in the central part of the North Sea. The data included nine wells with a total of about 200K tagged observations and the accompanying measured parameters at various depths within the wells. The ML algorithms were tested on the selected unseen dataset representing a new well with a minority of samples presented in the dataset.



When testing a model on the seen dataset, there is most likely an evident risk that the trained model would not perform satisfactorily on new wells. The progress in ML algorithms application provides an incentive for more study on model trustworthiness, model vulnerability and model robustness. Moreover, most ML algorithms are thought of as "black box" models, meaning that the process by which variables are integrated to form predictions cannot be seen or transparently understood. Hence, it is required to quantify the uncertainties in models' performance and analyze the inputs severity to outputs to apply ML to real-life classification problems successfully.



Within the scope of this research, feature sensitivity, uncertainty analysis and vulnerability analysis, as well as dataset selection and measurement, were applied to investigate the reliability of ML models. A novel Black Box Metamodel approach and Bayesian Neural Networks (BNN) were employed to compute aleatoric (data) uncertainties and epistemic (model) uncertainties.



With respect to lithology classification tasks, it is more crucial to estimate the probability that an observation belongs to a specific class. Consequently, the Probability Calibration techniques were used in modeling to improve the quality of the quantified uncertainties.

The paper has proven the efficiency of ML applications in lithology classification that will benefit the geosteering and drilling operations. Since the research questions the trust in ML models and reveals the hidden algorithms’ drawbacks, it can contribute to further development of data-driven applications in the Oil and Gas industry.


## Biography
Alina obtained a bachelor's degree in oil and gas engineering from Gubkin University, Russia. In June 2022, she graduated from the University of Stavanger in June 2022 with a master's degree in petroleum engineering. At the moment, she works as a reservoir engineer at Equinor Research Center in Trondheim. 

During the master's studies, Alina mainly focused on the applications of artificial intelligence techniques and uncertainty analysis in the oil and gas industry. 

The paper Alina is willing to present is based on her master thesis research.