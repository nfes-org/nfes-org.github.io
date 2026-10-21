---
tags: workshop2026abstract
title: "AUTOMATIC SEGMENTATION OF X-RAY MICROTOMOGRAPHY ROCK IMAGES: A NEW NMR-GUIDED WATERSHED TECHNIQUE FOR REEF ROCKS (Adam Fheed, AGH University of Krakow, Poland, Faculty of Geology, Geophysics and Environmental Protection, Department of Energy Resources.)"
presentation_date: 2026-11-04
---
#### Presenter
**Adam Fheed** from AGH University of Krakow, Poland, Faculty of Geology, Geophysics and Environmental Protection, Department of Energy Resources.
#### Co-authors
Joakim Beck, King Fahd University of Petroleum and Minerals, Dhahran, Kingdom of Saudi Arabia, College of Petroleum Engineering & Geosciences, Center for Integrative Petroleum Research; Artur Tadeusz Krzyżak, AGH University of Krakow, Poland, Faculty of Geology, Geophysics and Environmental Protection, Department of Energy Resources.
## Abstract
Introduction

Reef rocks are important hydrocarbon reservoirs and potential sites for underground gas storage. Their complex sedimentation and diagenetic alteration create heterogeneous pore networks that challenge quantitative analysis of their petrophysical parameters. Although X-ray microtomography (μCT) provides detailed 3D images, conventional binary segmentation cannot distinguish individual pores in highly connected networks. Watershed segmentation based on inverse distance maps can separate individual pores in the image but often causes over-segmentation due to numerous local minima. We address this by eliminating shallow minima in the distance maps using MATLAB’s imhmin function, controlled by a suppression threshold (H), which is calibrated by comparing μCT- and Nuclear Magnetic Resonance (NMR)-derived pore-size distributions (PSDs). The method aims to establish a semi-automatic workflow for segmenting heterogeneous carbonate pore networks and is evaluated on four selected Zechstein Limestone (Ca1) reef rocks of the Upper Permian in western Poland.



Procedure

μCT images with a 20 μm voxel size were acquired using a GE Nanotom S device. Pore masks were extracted and filtered. In MATLAB, inverse distance maps were computed using the imhmin function with suppression thresholds (H) from 1 to 10. H was calibrated by matching H-sensitive μCT pore-size distributions (PSDs) with NMR PSDs from T2 spectra generated at 0.05 T and 60 μs echo time using a Magritek Rock Core Analyzer. Assuming fast diffusion and surface-relaxation-dominated relaxation, T2 times were linearly scaled to equivalent pore radii through a factor related to surface relaxivity. μCT pore radii were estimated from volume-to-surface-area ratios (V/S), with regions volume-weighted to match NMR signal amplitudes. Wasserstein distances in logarithmic-radius space quantified differences between the PSDs. Distances across H thresholds were analyzed using least-squares fitting to identify a slope change marking stabilization. This point defined H while avoiding over-segmentation associated with simply minimizing PSD discrepancies.



Results / Observations

Across the four rocks studied, the selected separation factors ranged from H = 4 to H = 6. Interestingly, the lowest Wasserstein distances often occurred at H = 1, despite excessive subdivision of the connected pore regions. Starting from H = 1, increasing the value of the threshold reduced the number of segmented pore regions by approximately 23–37%, from 27,764–78,382 to 18,523–49,384 regions. The number-weighted mean equivalent pore radii ranged from approximately 50 to 62 μm, with standard deviations of 28–51 μm. Visual inspection supported separation along geologically valid boundaries, including fossil outlines and bioclast constrictions, revealing features such as dissolved or empty shells, interparticle porosity, and other locally developed porosity types.



Conclusion

Our methodology provides a systematic approach to improving watershed segmentation for μCT-based PSD derivation while enabling simultaneous visual inspection of pore structures. Selecting H from the stabilization of the Wasserstein discrepancy, rather than its minimum alone, can limit excessive pore subdivisions while preserving plausible geological boundaries. Although automated, the process can be time-consuming, prompting future integration with AI by using compiled segmentations from the proposed procedure as training datasets to yield rapid segmentations for the analysis of large digital-rock datasets Currently limited to specific reef carbonate types, the approach could potentially be extended to other complex rocks. It may be particularly useful for studying pore size and geometry during reservoir quality evaluation.

[Supporting pdf (download)](/assets/seminar_2026/illustrations/1BJhUyiQr5e09sDxf_526I-TQTZedtJ1m.pdf) 
 
## Biography
For over ten years, Dr. Adam Fheed has worked as a researcher in the oil and gas sector, gaining interdisciplinary expertise in carbonate sedimentology, diagenesis, and petrophysics, with a particular focus on reef reservoirs. He earned his PhD degree from AGH University of Krakow in 2019. He has developed his expertise at Polish and international institutions, including Orlen Upstream and King Fahd University of Petroleum and Minerals, where he spent nearly two years studying the effects of supercritical CO₂ on reef-rock pore structure.

He has received multiple awards, including a prestigious award from the Polish Ministry of Higher Education for scientific achievements, as well as several honorable mentions at international conferences. He has also led research projects funded through competitive scientific grants and contributed to the development of both academic and industry-oriented projects.

Dr. Fheed's primary goal is to bridge the gap between classical carbonate-rock assessment methods, such as field observations and core analysis, and petrophysical characterization. To achieve this, he has been developing advanced rock-analysis workflows involving X-ray microtomography (μCT) and magnetic resonance (MR) image analysis.