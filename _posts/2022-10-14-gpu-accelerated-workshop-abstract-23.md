---
tags: workshop2022abstract
title: "GPU-accelerated integral equation method for 3D modelling of induction logs (Durra Handri Saputera, University of Bergen)"
presentation_date: 2022-11-01
---
#### Presenter
**Durra Handri Saputera** from University of Bergen
#### Co-authors
Morten Jakobsen, University of Bergen, Sergey Alyaev, NORCE Norwegian Research Centre, Nazanin Jahani, NORCE Norwegian Research Centre, Kjersti Solberg Eikrem, NORCE Norwegian Research Centre,  Koen W.A. van Dongen, Delft University of Technology
## Abstract
The integral equation method has been applied in many studies for modelling induction logs in complex media that can have high conductivity contrast and degree of anisotropy. Without introducing many specific approximations, the electromagnetic fields can be obtained by solving the linear system arising from the discretization of the integral equations using the Krylov subspace methods iterative solver. The contraction integral equation formulation, which we have chosen, ensures the convergence of the iterative solver for any conductivity contrast and any degree of medium anisotropy. It simultaneously reduces the required number of iterations for achieving convergence within a given tolerance. To further accelerate the solver, we implemented the integral-equation method using Fast Fourier Transform (FFT) for efficient convolution integral involving the dyadic Green’s function. Finally, our implementation takes advantage of graphics processing units (GPU) to improve the computational time further through more efficient parallelization of mathematical operations, including FFT.

This study presents the result of 3D modelling induction logs in an anisotropic medium using the GPU-accelerated integral equation method. For a case with 105-106 unknowns, forward modelling results can be obtained within seconds up to a few minutes per location, depending on the model complexity, which is approximately an order of magnitude faster than the computation time without GPU. Comparison with the result from finite difference code shows a good agreement of the electromagnetic fields measured at receiver positions for a case of faulted formation with anisotropic layers.
## Biography
Durra Handri Saputera is a PhD student at the Department of Earth Science of University of Bergen. Currently working on the research of borehole electromagnetic modeling and inversion for logging while drilling scenario which is a part of DigiWells project.