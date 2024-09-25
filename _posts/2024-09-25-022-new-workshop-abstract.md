---
tags: workshop2024abstract
title: "New Multi-dimensional Inversion Workflow for Mapping Complex 3D Reservoir Geometry Using Ultra-Deep Azimuthal Resistivity (Gleb Dyatlov, Baker Hughes)"
presentation_date: 2024-11-12
---
#### Presenter
**Gleb Dyatlov** from Baker Hughes
#### Co-authors
Yuriy Antonov, Anna Astrakova, Alexey Bondarenko,  Dzhalil Khabibulin, Sergey Martakov, Nikita Tropin, Nikolay Velker, Warren Fernandes, David Holbrough (Baker Hughes), Michael Rabinovich (bp)
## Abstract
Increasing complexity in terms of resistivity distribution of geosteered reservoirs creates higher demands on both resistivity tools and inversion algorithms. The inversion workflow needs to deliver a high-resolution reservoir model to be used for navigation and mapping. Current 1D model approximations do not always resolve the formation complexity, thus higher dimensionality (up to 3D) approaches are needed. Finally, advanced 3D visualization is required to display and understand all features of the resulting reservoir model.

Starting with 1.5D model approximation performed for a well section, we then employ several classes of 2D models (from simple parametric models to cell-based resistivity distribution with controlled resolution) where 1D inversion is not sufficient to resolve the complex environment. Ultimately, we obtain a sequence of 2D models that delivers a 3D representation of reservoir structure based on the ultra-deep azimuthal resistivity (UDAR) data. Elements such as gradient-based optimization and random scanning of the model domain including artificial neural networks (ANN), special spatial regularization, and routines to estimate depth of detection (DoD) in 3D space and confidence are combined. 

The new inversion workflow deals with multi resolution measurements and a large volume of investigation in a staged approach. First, we analyze the challenge of multi-dimensional inversion from the limited set of measurements acquired in one borehole. Then, we demonstrate the performance of the workflow on several benchmarks including 2D and 3D benchmarks provided by the Standardization for Deep Azimuthal Resistivity (SDAR) workgroup. The new inversion can resolve both longitudinal changes in geology, e.g. crossing faults, and transverse heterogeneities, e.g. approaching a fault or waterfront at any angle. Also, we present comparisons of the results obtained for different configurations of ultra-deep azimuthal resistivity tools, based on compensated 3-coil measurements or 2-coil absolute measurements. By applying optimized models and methods in the integrated workflow we can complete different goals in reservoir navigation and mapping and fully utilize all available data. At all stages, comprehensive 3D visualization provides various representations of the inversion results, including curtain section, transverse views, and DoD envelopes indicating reliable resolution range.

This is a new 2D-3D inversion workflow which can handle changing orientation of features such as fault planes as well as resistivity distributions covering all scenarios: longitudinal, transverse, or geological changes at any angle. This facilitates more accurate saturation distribution for geostatic modelling. The forward solvers for all models are fast enough for repetitive computations using analytical gradients. Flexible implementation in a single-CPU to multi-GPU framework enables modern HPC capabilities for high performance real-time application.


## Biography
Gleb Dyatlov is a senior scientist at Baker Hughes since 2008. His research interests include modeling, inversion, and interpretation of logging-while-drilling resistivity measurements and software development. Before joining Baker Hughes, Gleb worked at Sobolev Institute of Mathematics, Novosibirsk State University, and University of Washington, Seattle. Gleb received an M.S. (1993) in Mathematics from Novosibirsk State University and a Ph.D. (1997) from Sobolev Institute of Mathematics.