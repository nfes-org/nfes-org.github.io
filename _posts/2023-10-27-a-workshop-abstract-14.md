---
tags: seminar2023abstract
title: "A machine learned near-well model in OPM (Peter von Schultzendorff, Universitetet i Bergen)"
presentation_date: 2023-11-01
---
#### Presenter
**Peter von Schultzendorff** from Universitetet i Bergen
#### Co-authors
Jakub Wiktor Both, Jan Martin Nordbotten (both UiB), Tor Harald Sandve, David Landa Marban, Birane Kane (all NORCE)
## Abstract
Large-scale commercial implementation of CO2 storage is considered a necessary mitigation strategy in most future emission scenarios. CO2 storage operations are subject to many regulatory, operational, and economical constraints. Among these, pressure build-up during injection can be a limiting factor for the maximal possible injection rate and hence for the quality of a storage site. Thus, it is of both theoretical and practical interest to accurately model well pressures when conducting reservoir simulations of potential CO2 storage sites.

When modeling reservoirs, the largest pressure gradients occur in the near-well regions. However, grid sizes are typically in the hundreds of meters and do not capture the pressure and flux variations in close proximity to the well. To compensate for this discrepancy, near-well models are employed. Well-known methods are, e.g., the Peaceman well model and its various extensions or, more explicitly, local grid refinement around the wells. These techniques have different limitations, as they are in the first instance only accurate in simplified flow regimes, while in the second instance fine grid resolutions may be needed for accurate results.

Here, we introduce a proof-of-concept for a machine learned near-well model and its integration into the open-source reservoir simulator OPM, which addresses these challenges. The key idea is to obtain a data-driven inflow-performance relation that is more accurate than the Peaceman model, while retaining the same computational complexity. Fine-scale ensemble simulations of the near-well region are conducted to form a training dataset. Afterward, a neural network is trained on the data and integrated into OPM. In large-scale simulations, the new near-well model offers both high fidelity to fine-scale results and fast inference.

This work lays the groundwork for a flexible new approach to near-well modeling. Trained on data from fine-scale simulations, neural networks enable fast, accurate and versatile modeling of the inflow-performance relation.


## Biography
I am a second year PhD student in the Porous Media Group at the University of Bergen. 

My PhD project is titled "Iterative Coupling of Physics-Based and Data-Driven Models in Reservoir Modeling" and is part of the Center for Sustainable Subsurface Resources (CSSR, https://cssr.no/). In the future, reservoir simulations will make more and more use of data-driven models, with a focus lying on machine learning models. Simultaneously, the coupling of both multiple physical phenomena, and the coupling of different spatial areas, will become an increasing point of focus. One objective of the CSSR is to combine the data-driven and the physics-based models, i.e., for a given coupled problem to solve one sub-problem with machine learning and the other with a physics-based model.

However, there exists little mathematical theory on how such a coupling can be done robustly, s.t. the combined algorithm converges to the correct solution. Furthermore, no general framework for such a pipeline exists. The goal of my PhD project is to fill this gap, i.e., to research and develop stable and robust solvers that solve some sub-problems with classical physics-based models, whereas other sub-problems are solved with a data-driven model.

Before starting the PhD, I got a B.Sc. in mathematics in Göttingen, Germany and a M.Sc. in mathematics in Hannover, Germany. During the master, I started to focus on applied mathematics and wrote my thesis under supervision of Prof. Dr. Thomas Wick on "Physics-Informed Neural Networks Applied to Phase-Field Fracture Models".

Additionally, during my master, I worked as a student assistant on the integration of deep learning models in the context of automatization of farming tasks at the Laser Zentrum Hannover.

The work on the machine-learned near-well model I aim to present at the NFES Formation Evaluation Workshop 2023 started this summer during the CEMRACS 2023 workshop.