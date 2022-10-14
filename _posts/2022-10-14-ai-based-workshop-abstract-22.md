---
tags: workshop2022abstract
title: "AI-based multi-modal interpretation of logs for ahead-of-bit probabilistic ROP prediction (Adrian Ambrus, NORCE Norwegian Research Centre)"
presentation_date: 2022-11-01
---
#### Presenter
**Adrian Ambrus** from NORCE Norwegian Research Centre
#### Co-authors
Sergey Alyaev, NORCE Norwegian Research Centre; Nazanin Jahani, NORCE Norwegian Research Centre; Ahmed H. Elsheikh, Heriot-Watt University 
## Abstract
Many geosteering operations rely on stratigraphy-based steering, where logs from the drilled well are matched to logs from an offset well by modifying the lateral shape of stratigraphy until a visual match between logs is obtained. Such interpretations are not unique, and averaging or picking a single interpretation can lead to errors.

An interpretation that preserves multiple modes can improve real-time geosteering decisions and rate of penetration (ROP) predictions ahead of the bit. We developed an AI method for multi-mode interpretation using a deep mixture density network (MDN). The MDN outputs a selected number of stratigraphic curves based on the current and offset well logs. We apply the MDN sequentially to track hundreds of realizations while discarding unlikely starting points. Using the offset well log, we predict the ROP along the stratigraphic curve for each realization. 

We verify the method's performance on realistic well logs and stratigraphic data from a Geosteering World Cup 2020 unconventional well. In the presence of unexpected features such as high dips and large faults, the method manages to recover the correct solution while tracking other likely modes. The tracking is real-time, with an interpretation speed of about 2600 ft/s, about two orders of magnitude faster than other current stratigraphy interpretation methods. Furthermore, a simple post-processing step provides probabilistic estimates of ROP 16ft ahead without additional inputs or training. 


## Biography
Adrian Ambrus is a senior researcher in the drilling and well modelling group at NORCE Norwegian Research Centre. Ambrus holds B.Sc and M.Sc degrees in mechanical engineering from Drexel University, U.S.A, and a Ph.D. in mechanical engineering from the University of Texas at Austin. His current research interests include modeling and optimization of drilling processes, application of statistical processing and machine learning techniques to drilling operations, and development of automated control algorithms for control of drill-string vibrations.