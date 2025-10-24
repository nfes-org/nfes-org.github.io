---
tags: workshop2025abstract
title: "Rapid Modelling of Electromagnetic Induction Log Data using an Adaptive Born Approximation (Durra Handri Saputera, University of Bergen)"
presentation_date: 2025-11-12
---
#### Presenter
**Durra Handri Saputera** from University of Bergen
#### Co-authors
Carlos Torres-Verdin, University of Texas at Austin,  Morten Jakobsen, University of Bergen, Koen W.A. van Dongen, Delft University of Technology,  Nazanin Jahani, NORCE Norwegian Research Centre
## Abstract
1. Introduction – Motivation



Real-time formation evaluation enables geosteering by providing subsurface information that guides well trajectories during drilling. Among the available measurements, tri-axial induction logging tools are particularly powerful, as they provide multi-component electromagnetic responses that are sensitive to 3D structural conductivity/resistivity variations near the borehole. However, the computational expenses of full 3D modeling and inversion often limit their use in time-sensitive operations, such as real-time well geosteering. To reduce these costs, approximate methods such as the Born approximation are of interest. While the conventional Born approximation is efficient, it is restricted to weak-contrast media and loses accuracy in complex geological settings. This motivates the development of an adaptive Born strategy to retain efficiency while extending the range of applicability for 3D inversion.



2. Procedure – Methods



The Born approximation is based on the integral equation (IE) formulation of Maxwell’s equations, where the total electromagnetic field is expressed as the sum of a background response and a scattered field. In its conventional form, the Born approximation assumes only first-order interactions between the field and conductivity perturbations, which is valid when the true medium exhibits low contrast relative to the chosen background. However, this assumption breaks down in realistic subsurface conditions with stronger heterogeneities. To address the latter challenge, we implement an adaptive Born strategy in which the background model is not fixed but is selected adaptively based on sensitivity analysis. The sensitivity highlights local variations in conductivity that dominate the response, allowing the background to be updated accordingly, thereby improving the accuracy of simulation results. 



3. Results/Observations – Key findings



The adaptive Born approximation was first validated in a three-layer horizontally stratified medium, where results were compared against a reference 1D solution. The adaptive background selection led to noticeably improved agreement with the reference compared to the conventional Born approximation. To further assess its performance in 3D conditions, the method was applied to a model with a simple fault deformation that introduces lateral variations and structural complexity. In this case, comparisons against the full integral equation solution show that the adaptive Born approximation captures some of the 3D scattering effects more accurately than the standard Born approach. Across both tests, the adaptive strategy gives rise to a consistent improvement while maintaining the computational efficiency characteristic of Born-type methods.



4. Conclusion – Lessons and implications



This study shows that the adaptive Born approximation can serve as a useful compromise between efficiency and accuracy for borehole electromagnetic modelling. By adaptively selecting the background model based on spatial sensitivity, it improves the performance of the conventional Born approximation in both layered and faulted media, capturing some 3D effects with better agreement to reference solutions. While it does not provide the full accuracy of a complete integral equation solver, the method can offer quicker approximations that are valuable as a first step prior to computationally intensive full 3D simulations.  The proposed can help to reduce the turnaround time in applications like well geosteering, where rapid interpretation is critical. In the future, the adaptive Born approach could be further explored as an efficient tool for providing initial models before committing to inversion with full 3D simulations.



[Supporting pdf (download)](/assets/seminar_2025/illustrations/1qGgQj99sA2tIE7rd8srnF972CZU0fHGu.pdf) 
 
## Biography
Durra Handri Saputera is a PhD candidate in geophysics at the University of Bergen, Norway. His research focuses on electromagnetic induction methods for borehole applications, with expertise in 3D forward modeling and inversion techniques using the integral equation method.