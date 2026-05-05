---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2015-llanos-numerical-model-of-the-habanero-geothermal-reservoir-australia"
title: "Numerical Model of the Habanero Geothermal Reservoir, Australia."
status: "draft"
source_pdf: "data/papers/Numerical model of the Habanero geothermal reservoir, Australia.pdf"
collections:
citation: "Llanos, Ella María, et al. \"Numerical Model of the Habanero Geothermal Reservoir, Australia.\" *Geothermics*, vol. 53, 2015, pp. 308-319. *ScienceDirect*, doi:10.1016/j.geothermics.2014.07.008. Accessed 2026."
indexed_texts: "9"
indexed_chars: "43953"
nonempty_source_blocks: "9"
compiled_source_blocks: "9"
compiled_source_chars: "43945"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.999818"
coverage_status: "full-index"
source_signature: "129f24a5f5c167e4ba415a96b69179f81e67771f"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:34:34"
---

# Numerical Model of the Habanero Geothermal Reservoir, Australia.

## One-line Summary
A TOUGH2 reservoir model was developed and calibrated for the Habanero Enhanced Geothermal System (EGS) in Australia to simulate natural state conditions and forecast production performance under various well layouts and flow rates.

## Research Question
How can a numerical model be developed and calibrated for the Habanero EGS reservoir to evaluate different well layouts and production scenarios for optimal long-term heat extraction? [Llanos 2015, pp. 1-2]

## Study Area / Data
The study focuses on the Habanero Enhanced Geothermal System (EGS) located in the Cooper Basin, northeast South Australia. The reservoir is the sub-horizontal Habanero fault within the Innamincka Granite, at depths between 4205 m and 4420 m. The model was built using data from hydraulic stimulation events (2003, 2005, 2012), downhole temperature profiles from well Habanero 1 (H01), stable closed-loop production/injection data from August 2013, and results from two tracer tests (H01-H03 in 2009 and H01-H04 in 2013). [Llanos 2015, pp. 1-2, 2-3, 3-5]

## Methods
A 3D numerical reservoir model was constructed using the TOUGH2 simulator. The model grid (4 km x 5 km x 5 km) consisted of 9 horizontal layers with 72,000 cells (50 m x 50 m). The grid was aligned with the eastern boundary fault and tilted 10° to the west-south-west to account for gravity effects on the inclined fault. A 1D natural state model was first used to calibrate rock thermal properties and basal heat flux against H01 temperature data. The 3D model's permeability was calibrated using production/injection pressure data, and porosity was calibrated by simulating the two field tracer tests. The calibrated model was then used to forecast 20-year production for four well layouts (staggered line drive, inverted 4-spot, regular 5-spot, east-west SLD) at circulation rates of 25, 35, and 45 kg/s per well. [Llanos 2015, pp. 1-2, 2-3, 3-5, 5-7, 7-8]

## Key Findings
- The calibrated model indicated a permeability anisotropy ratio of 2:1 (ky:kx) within the stimulated fault zone, consistent with the elongated shape of the seismic cloud. [Llanos 2015, pp. 5-7]
- Within the existing seismic cloud, the 4-spot well layout was identified as the most optimum for balancing short-term temperature and long-term extensibility. [Llanos 2015, pp. 1-2, 8-11]
- For a larger-scale development with an extended seismic cloud, the east-west staggered line drive (E-W SLD) layout provided the best temperature performance. [Llanos 2015, pp. 8-11, 11-11]
- Extending the stimulated reservoir area through further hydraulic stimulation is shown to be valuable, as it can deliver approximately 10°C higher production temperatures and ~3 PJ of additional energy over 20 years compared to the existing cloud. [Llanos 2015, pp. 8-11]
- Gravity and permeability anisotropy significantly influence fluid flow and thermal sweep patterns in the tilted fault reservoir. [Llanos 2015, pp. 5-7, 8-11]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| The reservoir is defined by the extent of the stimulated seismic cloud. | [Llanos 2015, pp. 1-2] | Post-hydraulic stimulation | The Habanero fault zone. |
| A 1D natural state model calibrated thermal properties to match H01 temperature data. | [Llanos 2015, pp. 2-3] | Steady-state, no mass flow | Used to set thermal conductivity for layers 5-9. |
| Permeability of stimulated zone calibrated to 800 mD (x,y) using production/injection data. | [Llanos 2015, pp. 3-5] | Stable closed-loop circulation, Aug 2013 | Transmissivity of 4000 mD·m. |
| Porosity of stimulated zone calibrated to 1.4% by matching H01-H04 tracer test. | [Llanos 2015, pp. 3-5, 5-7] | Tracer test simulation, anisotropic permeability | Also required 58 mD (y) and 29 mD (x) for damaged zone. |
| A 2:1 permeability anisotropy (ky:kx) matches the seismic cloud elongation. | [Llanos 2015, pp. 5-7] | Base case model | ky=1200 mD, kx=600 mD for stimulated zone. |
| The 4-spot layout is most optimum within the existing seismic cloud. | [Llanos 2015, pp. 1-2, 8-11] | Six-well patterns, 20-year forecast | Balances short-term temperature and long-term extensibility. |
| The E-W SLD layout provides the best temperature performance in an extended seismic cloud. | [Llanos 2015, pp. 8-11, 11-11] | Hypothetical extended reservoir | Temperatures remain fairly flat over 20 years. |
| Extending the seismic cloud can yield ~10°C higher production temperatures. | [Llanos 2015, pp. 8-11] | Comparison of existing vs. extended cloud | Delivers approximately 3 PJ more energy over 20 years. |

## Limitations
- The model's fine grid only extends to 20 km², while the Innamincka Granite reservoir extends over ~1000 km². Large Dirichlet boundary cells were used to simulate this extension. [Llanos 2015, pp. 1-2, 5-7]
- The model assumes a single-phase liquid (no flashing) in the wellbore for pressure correction. [Llanos 2015, pp. 3-5]
- The actual shape of future seismic clouds from stimulation is difficult to predict. [Llanos 2015, pp. 8-11]
- The model's top layer is planar and does not follow topography, though this is considered hydraulically irrelevant due to the lack of surface outflows. [Llanos 2015, pp. 2-3]

## Assumptions / Conditions
- The reservoir is a single, sub-horizontal fault zone (Habanero Fault) defined by the seismic cloud. [Llanos 2015, pp. 1-2]
- There is no natural convective movement, water recharge, or mass input into the reservoir. [Llanos 2015, pp. 11-11]
- The top and bottom model boundaries are closed to mass transfer. A constant heat influx is applied at the bottom. [Llanos 2015, pp. 2-3]
- The eastern boundary fault acts as a permeability barrier. [Llanos 2015, pp. 2-3]
- Tracer mixing/diffusion occurs in the wellbore before entering the reservoir, which was emulated by extending injection time in simulations. [Llanos 2015, pp. 3-5]
- Future production forecasts assume a bottom-hole re-injection temperature of 95°C. [Llanos 2015, pp. 5-7]

## Key Variables / Parameters
- **Permeability (k):** Stimulated zone: kx=600 mD, ky=1200 mD, kz=40 mD. Damaged zone (mud ring): kx=29 mD, ky=58 mD, kz=10 mD. [Llanos 2015, pp. 5-7]
- **Porosity (φ):** Stimulated zone: 1.4%. Damaged zone: 0.36%. [Llanos 2015, pp. 5-7]
- **Thermal Conductivity:** Layers 5-9: 3.3950-3.7775 W/(m·K). [Llanos 2015, pp. 2-3]
- **Heat Generation:** Granite blocks: 10 μW/m³. [Llanos 2015, pp. 2-3]
- **Basal Heat Flux:** 125 mW/m². [Llanos 2015, pp. 2-3]
- **Production/Injection Rates:** Modeled at 25, 35, and 45 kg/s per well. [Llanos 2015, pp. 5-7]
- **Well Layouts:** Staggered Line Drive (SLD), Inverted 4-spot, Regular 5-spot, East-West SLD. [Llanos 2015, pp. 5-7]

## Reusable Claims
- For EGS reservoirs in critically stressed fault zones, a permeability anisotropy ratio of 2:1 (ky:kx) can be a reasonable starting assumption when the induced seismic cloud is elongated. [Llanos 2015, pp. 5-7]
- In tilted fault-hosted EGS reservoirs, gravity significantly influences thermal sweep patterns, causing cooler fluid from up-dip injectors to migrate faster to down-dip producers. [Llanos 2015, pp. 8-11]
- Well layouts where producers and injectors are aligned with the direction of maximum permeability (e.g., 5-spot) tend to result in faster thermal breakthrough and lower long-term production temperatures. [Llanos 2015, pp. 8-11]
- Extending the stimulated volume of an EGS reservoir through further hydraulic stimulation is a valuable strategy to improve long-term production temperature and total heat recovery. [Llanos 2015, pp. 8-11]
- For a fault-hosted EGS reservoir with anisotropic permeability, a staggered line drive layout oriented perpendicular to the maximum permeability direction can provide superior thermal performance. [Llanos 2015, pp. 8-11, 11-11]

## Candidate Concepts
- [[Enhanced Geothermal System (EGS)]]
- [[Reservoir Modeling]]
- [[TOUGH2]]
- [[Permeability Anisotropy]]
- [[Hydraulic Stimulation]]
- [[Tracer Test]]
- [[Natural State Model]]
- [[Well Layout Optimization]]
- [[Seismic Cloud]]

## Candidate Methods
- [[Numerical Simulation]]
- [[History Matching]]
- [[Production Forecasting]]
- [[Thermal Sweep Analysis]]
- [[Wellbore Modeling]]

## Connections To Other Work
- The modeling methodology follows conventional geothermal reservoir modeling approaches but is applied to a unique tilted, fault-hosted EGS reservoir. [Llanos 2015, pp. 2-3]
- The study references and compares its approach to significant modeling work done at the Soultz-sous-Forêts EGS reservoir in France. [Llanos 2015, pp. 2-3]
- The work builds upon field data and operational reports from the Habanero Pilot Plant (HPP) project. [Llanos 2015, pp. 1-2]
- The concept of permeability anisotropy from shearing is supported by cited laboratory studies. [Llanos 2015, pp. 5-7]

## Open Questions
- How will the actual shape and extent of the seismic cloud evolve with future stimulations, and how will this affect the accuracy of the extended cloud forecasts?
- What are the long-term geochemical and geomechanical impacts (e.g., scaling, fault reactivation) of sustained circulation at the modeled rates?
- How would using CO2 as a working fluid instead of brine affect the reservoir performance and model predictions?
- Can the model's boundary conditions and large outer cells be refined to better capture the regional-scale pressure and temperature support?

## Source Coverage
All non-empty indexed fragments were processed. The compilation is based on 9 source blocks containing 43,945 characters, achieving a coverage ratio of 1.0 by blocks and 0.999818 by characters. The source signature is `129f24a5f5c167e4ba415a96b69179f81e67771f`.
