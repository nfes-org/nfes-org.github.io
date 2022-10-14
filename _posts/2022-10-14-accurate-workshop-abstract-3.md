---
tags: workshop2022abstract
title: "Accurate reservoir description and well placement using distance data, zone logs and depth to fluid contact (Pål Dahle, Norwegian Computing Center)"
presentation_date: 2022-11-01
---
#### Presenter
**Pål Dahle** from Norwegian Computing Center
#### Co-authors
Ariel Almendral Vazquez and Audun Sektnan
## Abstract
Traditionally, static and dynamic models have been made from a deterministic structure model. This means that one set of surfaces and faults have been used to represent the reservoir. By making high and low cases of important reservoir surfaces it has been possible to span parts of the uncertainty, giving, for instance, lower and upper bounds for gross rock volumes. Since the real uncertainty is nonlinear, these bounds do not represent the true uncertainty.  



Over the last two decades, methods where the structure model is made stochastically have been developed. With these methods, input and output data are represented by probability distributions rather than fixed values. Even though such approaches have been used in oil and gas industry for many years, it is only recently that they have gathered real traction. Since uncertainty is an integrated part of these methods, consistent surface prediction uncertainties and volume uncertainties are produced.



We have developed a stochastic approach for surface gridding, where all input data are modeled as uncertain. This includes time interpretation maps, velocity models and isochores, as well as well data like picks, zone logs, resistivities (DDR) and the true vertical depth of the well. Each surface is modeled as a sum of intervals, and each interval is modeled as a trend plus an uncertainty term.



Our method is Bayesian and uses kriging for the interpolation. The conditioning to zone logs uses the stochastic model to calculate constrained surface points for the surface above and below the well. These points may be regarded as auto-generated pseudo well picks. The resistivities provide measures of the distance from the well to a contrast. Rather than using these distances to make pseudo-well picks, they are used directly as distances in the algorithm. This allows well paths to be repositioned based on, for instance, the observed distance to an oil-water contact.



Using real data, we show how surfaces change as different kinds of data are included in the gridding, and how the uncertainties of these data affect the result. We also show that a consistent handling of the well depth uncertainty may be crucial for a correct description of the reservoir. This has consequences for well planning, well landing as well as volume uncertainty studies. Eventually, we do a simulated well drilling that illustrates how this stochastic approach can be used for geosteering.
## Biography
Pål works as  is a Senior Researcher at the Norwegian Computing Center. He holds a PhD in Quantum Chemistry from the University of Oslo, and has been working with uncertainty modelling in the gas and oil industry over the last 20 years. The main focus has been on stochastic methods, in particular in relation with seismic inversion and structural modelling.