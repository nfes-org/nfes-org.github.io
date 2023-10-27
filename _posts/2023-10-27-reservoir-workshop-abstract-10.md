---
tags: seminar2023abstract
title: "Reservoir Fluid Typing from Standard Mud Gas - A Machine Learning Approach (Alexandra Cely, Equinor ASA)"
presentation_date: 2023-11-01
---
#### Presenter
**Alexandra Cely** from Equinor ASA
#### Co-authors
Artur Siedlecki, Artur Liashenko, Tao Yang and Sandrine Donnadieu
## Abstract
Standard mud gas data is part of the basic mudlogging service and is used mainly for safety monitoring. Although the data is available for all wells, it is not used for reservoir fluid typing due to poor prediction accuracy. We recently developed a new manual method and significantly improved the reservoir fluid typing accuracy from standard mud gas data. However, there is a strong business for an automatic method to enable reservoir fluid interpretation while drilling.

A machine learning method has been developed based on a well-established standard mud gas database. The standard mud gas compositions contain methane, ethane, and propane components with reasonable quality measurements. The butane and pentane compositions in the standard mud gas are low and sometimes close to the detection limit. Therefore, we only use methane to propane compositions in the machine learning algorithm. It is particularly challenging to predict reservoir fluid type accurately based on only three gas components. For that reason, we introduce additional data sources to increase the prediction accuracy: a large in-house reservoir fluid database and petrophysical logs.

The machine learning algorithm extracts critical reservoir fluid information specifically for a known field by utilizing the geospatial location and the existing reservoir fluid database. When combined with the standard mud gas database, the reservoir fluid typing accuracy increased from 50-60% to nearly 80%. Petrophysical logs are the main tool in the industry to identify the reservoir fluid type. When combining the petrophysical logs with the machine learning model already with satisfactory performance, the final reservoir fluid type prediction accuracy is about 80%. Given the difficulties of distinguishing oil or gas for near-critical fluids or volatile oil, the current prediction accuracy is sufficient for industry applications.

The innovation created significant business opportunities based on the standard mud gas, which has been regarded as not applicable data for accurate reservoir fluid typing for many decades. The new method makes accurate reservoir fluid typing possible for real-time well decisions like well placement, completion, and sidetracking. In addition, the new method can add lots of value for well integrity, maturating production targets, and cost-efficient Plug and Abandonment (P&A) in the overburden


## Biography
Alexandra Cely is a principal reservoir engineer at Equinor who holds a master’s degree in env. offshore engineering with a chemistry major from the University of Stavanger. She started at Equinor in 2012 as a flow assurance engineer working on field development
projects and joined the PVT and fluid analysis group in 2019. Alexandra is the leading researcher on the fluid property prediction from the cuttings project and is currently responsible for the thermodynamic correction of the standard mud gas data. Alexandra was selected as an SPWLA distinguish speaker for the 2024 season for the work conducted on estimating reservoir oil viscosity using mud gas logging and cuttings.