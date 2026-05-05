---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2018-gong-quantitative-prediction-of-sub-seismic-faults-and-their-impact-on-waterflood-performan"
title: "Quantitative Prediction of Sub-Seismic Faults and Their Impact on Waterflood Performance: Bozhong 34 Oilfield Case Study."
status: "draft"
source_pdf: "data/papers/Quantitative prediction of sub-seismic faults and their impact on waterflood performance Bozhong 34 oilfield case study.pdf"
collections:
citation: "Gong, Lei, et al. “Quantitative Prediction of Sub-Seismic Faults and Their Impact on Waterflood Performance: Bozhong 34 Oilfield Case Study.” *Journal of Petroleum Science and Engineering*, 2018, doi:10.1016/j.petrol.2018.09.049."
indexed_texts: "10"
indexed_chars: "48114"
nonempty_source_blocks: "10"
compiled_source_blocks: "10"
compiled_source_chars: "47427"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.985721"
coverage_status: "full-index"
source_signature: "56d63767584918312b70823545f62571f1d55471"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:43:25"
---

# Quantitative Prediction of Sub-Seismic Faults and Their Impact on Waterflood Performance: Bozhong 34 Oilfield Case Study.

## One-line Summary
This study develops a method combining fractal geometry and 3D geo-mechanical simulation to quantitatively predict sub-seismic faults and analyzes their impact on waterflood performance and remaining oil distribution in the Bozhong 34 Oilfield.

## Research Question
How can the number, size, orientation, and location of sub-seismic faults be quantitatively predicted, and what is their influence on water injection development and remaining oil distribution?

## Study Area / Data
The study focuses on the Bozhong 34-2 oilfield within the Bozhong 34 oilfield, located in the Huanghekou sag of the Bohai Bay Basin, China [Gong 2018, pp. 4-6]. The primary target is the second Member of Shahejie Formation (Es2), with a burial depth of 3200-3400 m, porosity of 11.2%-17.1%, and permeability of 8.9-449 mD [Gong 2018, pp. 4-6]. Data includes 3-D seismic data for fault interpretation, core plug samples from well B1 for rock mechanical parameters, and dynamic production data from 21 production wells and 5 injection wells [Gong 2018, pp. 4-6, 10-12].

## Methods
The methodology integrates two main approaches:
1.  **Fault Fractal Growth Model:** Extrapolates the power-law distribution of seismic fault parameters (length, throw, frequency) to predict the number and size of sub-seismic faults [Gong 2018, pp. 6-8].
2.  **3-D Geo-mechanical Simulation:** Uses the Boundary Element Method (BEM) to simulate the disturbed stress field near seismic faults. The preferred failure orientation and Maximum Coulomb Shear Stress (MCSS) are calculated using the Coulomb failure criterion to constrain the occurrence and location of sub-seismic faults [Gong 2018, pp. 6-8, 8-10].
A marked-point process stochastic technique is then used to generate the final distribution model of sub-seismic faults [Gong 2018, pp. 8-10].

## Key Findings
- Sub-seismic faults can be effectively predicted by combining fractal theory and 3-D geo-mechanical simulation [Gong 2018, pp. 14-15].
- The size (throw) of sub-seismic faults impacts waterflood response time; faults with a throw larger than 6.5 m show a significant positive correlation with longer response times [Gong 2018, pp. 10-12].
- The orientation of sub-seismic faults relative to injection/production lines controls waterflood flow paths and remaining oil distribution. Faults perpendicular to flow act as barriers, while faults parallel to flow can accelerate water breakthrough [Gong 2018, pp. 12-14, 14-15].
- Three flooded areas (P1, B10-P2, P3-B4) were identified in the Es2 formation, consistent with drilling reports [Gong 2018, pp. 12-14].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Fault length and maximum throw follow a power-law distribution (e.g., D = 0.0056×L^1.3 for NE-SW faults). | [Gong 2018, pp. 8-10] | Based on interpreted seismic faults in the Es2 formation. | Equations 5 and 7 provide the specific models for each fault set. |
| The number of faults follows a power-law cumulative frequency distribution (e.g., NL = 15865×L^-1.5 for NE-SW faults). | [Gong 2018, pp. 8-10] | Extrapolated from seismic data using central straight segment of log-log plot. | Equations 6 and 8 provide the specific models. |
| Sub-seismic fault throw >6.5 m correlates with increased waterflood response time. | [Gong 2018, pp. 10-12] | Statistical analysis of dynamic production data from the Bozhong 34-2 oilfield. | Larger faults create sealing networks, acting as barriers. |
| A sub-seismic fault between wells P3 and B4 deviated injected water, causing early water breakthrough at well B6. | [Gong 2018, pp. 12-14] | Analysis of injection/production relationships and predicted fault distribution. | Demonstrates fault control on flow path. |
| Sub-seismic faults perpendicular to injection/production lines create sharp pressure gradients and enrich remaining oil on the production side. | [Gong 2018, pp. 12-14] | Numerical simulation results. | Parallel faults shorten response time but leave remaining oil on both sides. |

## Limitations
- The boundary between seismic and sub-seismic faults is difficult to define and is affected by seismic resolution, depth, and lithology [Gong 2018, pp. 2-4].
- The 3-D geo-mechanical model assumes formations are homogeneous, isotropic, and linear-elastic [Gong 2018, pp. 6-8].
- The right truncation point for fitting the power-law distribution of fault frequency is difficult to determine and is related to faults extending beyond the target area [Gong 2018, pp. 8-10].

## Assumptions / Conditions
- Fault and fracture systems exhibit self-similarity and follow power-law (fractal) distributions over a wide range of scales [Gong 2018, pp. 6-8].
- The rock mechanical parameters are uniform throughout the modeled strata [Gong 2018, pp. 6-8].
- The direction of the minimum principal stress is perpendicular to the fault strikes for normal faults, based on Anderson's model [Gong 2018, pp. 10-12].

## Key Variables / Parameters
- **Fault Throw (D):** Maximum vertical displacement on a fault.
- **Fault Length (L):** Horizontal extent of a fault.
- **Maximum Coulomb Shear Stress (MCSS):** Represents the probability of shear failure at a point.
- **Response Time:** Time from water injection start to observable production increase.
- **Power-law Exponents (C1, C2):** Slopes of the linear relationships in log-log plots for fault size vs. throw and fault size vs. frequency.

## Reusable Claims
- In reservoirs with normal faults, the number and size of sub-seismic faults can be predicted by extrapolating the power-law distribution of seismic fault parameters [Gong 2018, pp. 6-8].
- The location and orientation of sub-seismic faults can be constrained by simulating the disturbed stress field near seismic faults and applying the Coulomb failure criterion [Gong 2018, pp. 6-8].
- Sub-seismic faults with a throw greater than 6.5 m significantly increase waterflood response time by acting as flow barriers [Gong 2018, pp. 10-12].
- The impact of sub-seismic faults on waterflood performance depends on the angle between fault strike and injection/production line direction [Gong 2018, pp. 12-14].

## Candidate Concepts
- [[Sub-seismic faults]]
- [[Fractal geometry]]
- [[3D geo-mechanical simulation]]
- [[Waterflood performance]]
- [[Remaining oil distribution]]
- [[Reservoir heterogeneity]]
- [[Power-law distribution]]

## Candidate Methods
- [[Fault fractal growth model]]
- [[Boundary Element Method (BEM)]]
- [[Coulomb failure criterion]]
- [[Marked-point process stochastic technique]]
- [[Numerical reservoir simulation]]

## Connections To Other Work
- The study builds on the fault fractal growth model first proposed by King (1983) [Gong 2018, pp. 6-8].
- It applies the 3-D geo-mechanical simulation approach for sub-seismic fault prediction developed by Maerten et al. (2006) [Gong 2018, pp. 6-8].
- The work discusses the impact of sub-seismic faults on fluid flow, referencing studies on fault sealing mechanisms like cataclasis and clay smearing (e.g., Fossen and Bale, 2007; Schueller et al., 2013) [Gong 2018, pp. 2-4].

## Open Questions
- How can the right truncation point for the fault frequency power-law distribution be more objectively determined?
- How do variations in lithology and mechanical stratigraphy within the reservoir affect the accuracy of the homogeneous, isotropic model assumption?
- What is the precise boundary (in terms of seismic resolution) between seismic and sub-seismic faults for a given geological setting?

## Source Coverage
All 10 non-empty indexed fragments were processed. The compiled source blocks total 47,427 characters from an indexed total of 48,114 characters, resulting in a coverage ratio of 0.985721 by character count. The coverage status is full-index.
