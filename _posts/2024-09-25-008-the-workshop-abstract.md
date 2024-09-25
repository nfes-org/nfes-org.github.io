---
tags: workshop2024abstract
title: "The fusion of traditional geosteering and deterministic resistivity inversion. Can we squeeze more from existing data? (Danil Nemushchenko, ROGII)"
presentation_date: 2024-11-12
---
#### Presenter
**Danil Nemushchenko** from ROGII
#### Co-authors
nan
## Abstract
With the increasing complexity of geosteering processes and the growing number of challenging wells, effective well placement has become critically dependent on advanced remote boundary mapping techniques, such as the use of azimuthal resistivity logging tools. These tools are now almost indispensable for keeping the borehole within the desired zone. Traditionally, the interpretation of azimuthal resistivity data is carried out by the tool vendor and is independent of the geosteering interpretation created using other methods, such as basic correlation techniques or image log interpretation. As a result, in situations, where resistivity inversion and basic correlation with image log interpretation provide conflicting opinions, the engineer relies more on resistivity data than on other geological data, which can mislead and potentially result in errors or lost reservoir footage.

Our paper presents a new method and inversion algorithm that integrates multiple geosteering methods into a single framework, allowing resistivity data to incorporate both standard logging correlations and image interpretations in the inversion process. The unique feature of this approach is that the input model for the inversion calculation accounts not only for the resistivity profile with the parameters of layer thickness and anisotropy, but also considers apparent dip angles, faults, and lateral changes in thickness and properties from the geosteering interpretation. This technology enables a complete integration of previously independent methods into one and uses basic correlation methods to enhance the inversion of azimuthal data.

Additionally, this inversion approach is hybrid, as it continuously compares the input model with established parameters (a deterministic approach) and, when it is impossible to reproduce the given model, switches to a stochastic approach, which is a data-driven algorithm. This allows the geosteering engineer to use two main inversion approaches simultaneously.

The presentation will focus on the implementation of the described algorithm on synthetic examples as well as actual data.


## Biography
Head of geosteering department and product owner of inversion in ROGII. Danil holds an MSc degree in Geology from Novosibirsk State University. He has over 12 years’ experience in well placement. He has worked in conventional and unconventional projects around the globe. Prior to joining ROGII he has worked with major service companies such as Schlumberger and Baker Hughes. Danil has worked with almost all types of MWD & LWD tools including high-tier deep azimuthal resistivity tools.