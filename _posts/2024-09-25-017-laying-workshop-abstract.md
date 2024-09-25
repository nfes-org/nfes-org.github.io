---
tags: workshop2024abstract
title: "Laying the Foundation for Generative AI-Enhanced Geosteering: The Complete DISTINGUISH Workflow (Sergey Alyaev, NORCE)"
presentation_date: 2024-11-12
---
#### Presenter
**Sergey Alyaev** from NORCE
#### Co-authors
K. Fossum, H.E. Djecta, J. Tveranger and A. Elsheikh
## Abstract
Traditional geosteering decisions rely on rapid, manual interpretation of Logging-While-Drilling (LWD) data, manual comparison with offset wells, and pre-drill uncertainty assessments. Given the ever-accelerating pacing of drilling operations, time constraints are gradually making this approach more challenging and error-prone. Thus, the geo-energy industry strives for a geosteering workflow that continually captures and updates the subsurface uncertainty.

 

We present “DISTINGUISH”: a real-time, AI-driven workflow designed to transform geosteering by integrating Generative Adversarial Networks (GANs) for geological parameterization, ensemble methods for model updating, and global optimization for complex decision-making during directional drilling operations. The DISTINGUISH framework relies on offline training of a GAN model to reproduce relevant geology realizations and a Forward Neural Network (FNN) to model LWD tools’ response for a given geomodel. The online phase of the workflow starts with an ensemble of Gaussian model vectors, mapped to geomodel realizations by the GAN and then converted to synthetic LWD measurements by the FNN. The ensemble of predictions is then compared to the actual LWD data and subsequently updated by an ensemble-Kalman filter-like method. A discrete dynamic programming (DDP) algorithm, informed by GANs, enables complex decision optimization beyond simple decision trees and greedy choices.

 

In this presentation, we show an early but complete version of the workflow. It features the stepwise reduction of GAN-geomodel uncertainty around and ahead of the bit, informed by real-time LWD data with a DDP-optimization-based decision support system. This iterative updating process enhances predictive models of geology ahead of drilling and ultimately leads to better steering decisions.

 

DISTINGUISH workflow represents a new and different approach to digitalizing geosteering, combining advanced modeling, real-time optimization, and AI to improve subsurface navigation and optimize well placement. Its ability to update and refine uncertainty in geomodels positions it as a critical technology for the future of drilling operations across various domains, fulfilling industry expectations for enhanced decision-making workflows.
## Biography
Sergey Alyaev is a Senior Researcher at NORCE Energy working on interdisciplinary research within machine learning uncertainty quantification and geosciences. Among 34 papers he has co-authored since 2021, 24 developed new ML methods and their applications to geosciences and uncertainty quantification. He is coordinating efforts in geosteering at NORCE and leads a geosteering GIP “DISTINGUISH” and epics in “DigiWells” center. 