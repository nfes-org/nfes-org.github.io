---
tags: workshop2022abstract
title: "Verification of a real-time method for updating the geosteering earth model based on GAN (Kristian Fossum, NORCE Norwegian Research Centre)"
presentation_date: 2022-11-01
---
### Presenter
**Kristian Fossum** from NORCE Norwegian Research Centre
### Co-authors
Sergey Alyaev, NORCE Norwegian Research Centre;Jan Tveranger, NORCE Norwegian Research Centre;Ahmed H. Elsheikh,Heriot-Watt University 
## Abstract
The complexity and computational cost of conventional geomodelling workflows limit their applicability for formation evaluation in real-time using data acquired during drilling. We propose a workflow replacing traditional geomodels with a Generative Adversarial deep neural Network (GAN) trained to reproduce sections of complex geology. Offline training produces a fast GAN-based approximation of, in our case, fluvial geology parameterized as a 60-dimensional model vector with standard Gaussian distribution of each component. The Ensemble Randomized Maximum Likelihood (EnRML) method reduces geological and petrophysical uncertainty by integrating real-time extra-deep EM measurements into GAN-model realizations. The ensemble of updated GAN-geomodel realizations provides probabilistic forecasts of facies around and ahead of the well. 



The approximations in the EnMRL method combined with a highly non-linear GAN model may produce inaccurate or biased predictions. To test if the proposed workflow provides reliable results, we performed a statistical verification with an accurate but slow Markov Chain Monte Carlo (MCMC) method. In our testing, both the slow and the real-time methods reduce uncertainty and correctly predict major geological features up to 500 meters ahead of drill-bit. The results - demonstrated in a synthetic environment - indicate the method’s potential to improve assisted real-time formation evaluation in complex geology significantly.
## Biography
Kristian Fossum is a senior researcher in the data assimilation and optimization group at NORCE. He holds a MSc in petroleum technology and a PhD in applied mathematics, both from the University of Bergen. His research interests include ensemble-based data assimilation, inverse problems, computational statistics, data driven methods, optimization, and automated decision support.