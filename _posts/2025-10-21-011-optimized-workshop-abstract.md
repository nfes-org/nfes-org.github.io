---
tags: workshop2025abstract
title: "Optimized Dynamic Depth Alignment Between Well Logs for Enhanced Petrophysical and Rock Physics Interpretation (Kjetil Westeng, Aker BP)"
presentation_date: 2025-11-12
---
#### Presenter
**Kjetil Westeng** from Aker BP

#### Co-authors
Peder Aursand, Frida Viset, and Yann Van Crombrugge

## Abstract
Depth alignment between different well logs is a major challenge in petrophysical and rock physics analysis, particularly when relying on multiple curves from different wireline runs or conveyance methods. Even small m isalignments can introduce significant errors in calculating elastic properties such as Vp/Vs ratio and Poisson's ratio, leading to spikes and physically implausible results. The same accounts for multimineral analysis utilizing a comprehensive set of input logs. Precise alignment is essential to reduce noise and improve the accuracy of subsurface interpretations.

We propose an optimization-based methodology to determine the optimal depth shift for aligning multiple well logs to their true relative positions. By encoding prior knowledge of depth-shift smoothness and limiting parameter complexity, our approach not only ensures physically consistent solutions but also inherently regularizes the problem against overfitting. Consequently, the formulation remains well-posed for locating a global optimum, providing both robustness and precise control over alignment accuracy.

The methodology involves the following steps:

Data Pre-processing:
- Transformation and Scaling: Convert different log measurements to a common scale and dynamic range to ensure compatibility. This process may involve techniques such as normalization, logarithmic transformations, or standardization. By applying these methods, the data is aligned in a way that enhances comparability and highlights formation changes more accurately and consistently across the various logs.
- Filtering: Apply appropriate filters to remove noise and enhance relevant signal features.
Bulk Shift Application:
- Determine and apply an initial bulk shift to achieve a coarse alignment between the logs, this improves the efficiency of the next step.

Dynamic  Depth Alignment   Optimization:
- Cost Function Definition: We define a novel cost function shown in figure 1, that considers cross-correlation between logs, penalizes large average depth shifts, and discourages abrupt changes in the depth shift (smoothness constraint).
- Optimization Solver: Utilize an optimization algorithm to minimize the cost function, resulting in the optimal set of dynamic shifts along the wellbore.

Post-Processing:
- Upscaling Shifts: Adjust the calculated shifts to match the original sampling rate of the target log.
- Resampling: Resample the target curve using the optimized depth alignment for final analysis.
 
 
Mathematical Formulation:

Let cost(C) be the cost function of the final shift matrix and
- X is the base log
- Y is the log being depth aligned to X 
- A is the absolute values of the depth shifts
- D is the absolute values of the distortion of the curve

 

![Supporting figure](/assets/seminar_2025/illustrations/akerbps-equaiton.png) 

- The first term penalizes lack of correlation between the logs. 
- The second term penalizes large overall depth shifts (α controls this penalty).
- The third term penalizes abrupt changes in depth shift between adjacent windows (β controls the smoothness constraint).

When the window size approaches the sampling rate the problem converges into a continuous optimisation challenge that can be solved by stochastic gradient-based optimization algorithms.

The methodology has been applied to more than 2,000 wells, greatly improving the alignment and s
ubsequently the quality of the dataset.   

The methodology effectively aligned different curves, including bulk density, compressional slowness, and shear slowness logs. It also demonstrated robustness when aligning datasets of varying natures, such as triple combo logs and nuclear magnetic resonance measurements.



