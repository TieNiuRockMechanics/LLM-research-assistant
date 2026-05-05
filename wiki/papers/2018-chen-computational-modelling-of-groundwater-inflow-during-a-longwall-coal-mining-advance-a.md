---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2018-chen-computational-modelling-of-groundwater-inflow-during-a-longwall-coal-mining-advance-a"
title: "Computational Modelling of Groundwater Inflow During a Longwall Coal Mining Advance: A Case Study from the Shanxi Province, China."
status: "draft"
source_pdf: "data/papers/Computational Modelling of Groundwater Inflow During a Longwall Coal Mining Advance A Case Study from the Shanxi Province, China.pdf"
collections:
citation: "Chen, Yuedu, et al. \"Computational Modelling of Groundwater Inflow During a Longwall Coal Mining Advance: A Case Study from the Shanxi Province, China.\" *Rock Mechanics and Rock Engineering*, 2018, doi:10.1007/s00603-018-1603-1. Accessed 2 Feb. 2026."
indexed_texts: "13"
indexed_chars: "63731"
nonempty_source_blocks: "13"
compiled_source_blocks: "13"
compiled_source_chars: "63154"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.990946"
coverage_status: "full-index"
source_signature: "4ff333e6e0bca64c845eff811485a95d145ca83f"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T00:50:50"
---

# Computational Modelling of Groundwater Inflow During a Longwall Coal Mining Advance: A Case Study from the Shanxi Province, China.

## One-line Summary
This study compares three computational modeling approaches (Darcy, Biot poroelastic, and Biot with stress-dependent permeability) to predict groundwater inflow into a longwall coal mine in Shanxi, China, finding that incorporating permeability changes due to mining-induced stress best matches field data.

## Research Question
How do different computational modeling approaches, ranging from basic Darcy flow to full Biot poroelasticity with stress-dependent permeability alterations, compare in estimating groundwater inflow into an advancing longwall coal mine excavation, and what are the causes of differences in their results? [Chen 2018, pp. 2-3]

## Study Area / Data
The case study focuses on the No. 18112 longwall working face of the Xiegou Coal Mine, located in the northwest of the Shanxi province, China. The mine is in the northern part of the Hedong coal field. The geological setting is a slightly inclined monoclonal structure with a dip of about 8° to the west. The coal-bearing strata are within Carboniferous-Permian sequences, and the study targets the No. 8 coal seam with a dip angle of 7° and an average thickness of 5.95 m. The main aquifers influencing the hydrogeology are the karst aquifer of the Majiagou formation, sandstone aquifers of the Taiyuan, Xiashihezi, and Shanxi formations, and an alluvial porous aquifer in the Quaternary. The regional groundwater flow direction is from east to west. [Chen 2018, pp. 5-6]

## Methods
Three computational modeling approaches were developed using the COMSOL™ Multiphysics Code:
1.  **Approach I (Basic Darcy):** Assumes purely Darcy flow with constant, stress-independent permeability. Effective permeabilities for strata above and below the coal seam were calculated using weighted harmonic and horizontal means. [Chen 2018, pp. 4-5]
2.  **Approach II (Full Biot Poroelastic):** Uses Biot's classical poroelastic theory (equations 1-7) to model coupled hydro-mechanical behavior, but assumes permeability is unaffected by mining-induced stress changes. [Chen 2018, pp. 4-5]
3.  **Approach III (Biot with Permeability Alterations):** Extends Approach II by incorporating stress-dependent permeability changes. Permeability evolves according to an exponential relationship (Eq. 8) with the first invariant of the effective stress tensor and pore pressure. [Chen 2018, pp. 4-5, 9-10]

A three-dimensional finite element model of the simplified geological setting was developed. The model domain was 600 m × 400 m × 197 m, representing half of the working face due to symmetry. The excavation was simulated in 13 steps over a 200 m advance length. Boundary conditions included a constant hydraulic head at the top surface and zero pressure/traction on the excavation surface. [Chen 2018, pp. 6-9]

## Key Findings
- The basic Darcy model (Approach I) predicted a constant maximum flow rate of 21.9 × 10⁻³ m³/h at the excavation corners, which did not match field observations of increasing inflow. [Chen 2018, pp. 10-12, 16-17]
- The full Biot poroelastic model (Approach II) showed that vertical stress relief zones form in the strata above and below the middle of the stope, while stress increases occur in the front, back, and sides of the excavation. [Chen 2018, pp. 10-12]
- The model incorporating permeability changes (Approach III) indicated that significant permeability increases develop in the de-stressed (caving) zone, with permeability decreasing further away from the excavation. This pattern aligns with stress alterations. [Chen 2018, pp. 12-14]
- Comparison with field data showed Approach III had the smallest relative variation (Qδ from -8% to 23%), outperforming Approaches I (20-60%) and II (81-147%). [Chen 2018, pp. 14-16]
- Sensitivity analysis revealed that the stress sensitivity coefficient β in the permeability-stress relationship is critical. A value of 3β provided the best fit to field data, suggesting it is more suitable for predictions than the base β. [Chen 2018, pp. 14-16]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Maximum flow rate from Darcy model is 21.9 × 10⁻³ m³/h at excavation corners and remains constant. | [Chen 2018, pp. 10-12] | Approach I, monitoring plane X=78 m within coal seam. | Contrasts with field data showing increasing inflow. |
| Vertical stress variation rate (σR) shows a five-stage process (increase-decrease-increase-decrease-stabilization) along monitoring lines. | [Chen 2018, pp. 10-12] | Approach II, monitoring lines on floor (X=0, Z=0) and roof (X=0, Z=157). | Confirms stress transfer from excavated area to surrounding rock. |
| Permeability variation rate (KR) is highest in the de-stressed zone and diminishes with distance from excavation. | [Chen 2018, pp. 12-14] | Approach III, monitoring lines on floor (X=0, Z=40) and roof (X=0, Z=157). | Permeability increase is closely related to stress decrease. |
| Relative variation (Qδ) for Approach III ranges from -8% to 23%, compared to 20-60% for I and 81-147% for II. | [Chen 2018, pp. 14-16] | Comparison of computational results (Qc) with field measurements (Qf). | Approach III provides the best prediction of fluid influx. |
| Sensitivity analysis shows Qδ decreases with increasing stress sensitivity coefficient β; 3β is optimal. | [Chen 2018, pp. 14-16] | Different magnitudes of β (0.01β to 3β) were tested. | Critical parameter for accurate fluid influx prediction. |
| Permeability-stress relationship for coal follows K = 1.4445 exp{-0.1224I₁ + 0.2017p} m². | [Chen 2018, pp. 9-10] | Laboratory data from a coal specimen from an adjacent mine. | Used for Approach III; Biot coefficient α ≈ 0.55. |
| Permeability-stress relationship for fine sandstone follows K = 8.1804 exp{-0.04136I₁} m². | [Chen 2018, pp. 9-10] | Laboratory investigations on fine sandstone. | Used for Approach III. |

## Limitations
- Material parameters for some rocks (e.g., coal) were obtained from published literature rather than site-specific testing. [Chen 2018, pp. 9-10]
- The model assumes homogeneous and isotropic mechanical and hydraulic properties for all strata. [Chen 2018, pp. 9-10]
- The excavation process is simplified; the model assumes hydraulic head and stress reach steady state at the end of each excavation step, and geometry changes due to mining are not considered. [Chen 2018, pp. 6-9]
- The model only simulates the first 200 m of excavation advance due to computational constraints and data availability, not the full 3.8 km length. [Chen 2018, pp. 6-9]
- The stress-dependent permeability relationship (Eq. 8) is based on an effective permeability from axial flow tests, not general anisotropy. [Chen 2018, pp. 4-5]

## Assumptions / Conditions
- The geological structures are simple and stable with no major faults or collapse columns. [Chen 2018, pp. 5-6]
- The initial in situ stress state is geostatic, with lateral stresses governed by the elastic Poisson's ratio. [Chen 2018, pp. 6-9]
- The initial hydrostatic head prior to mining corresponds to the ground elevation (1050 m). [Chen 2018, pp. 6-9]
- The Ordovician confined aquifer is remote and does not contribute to water influx in the modeled area. [Chen 2018, pp. 5-6]
- The permeability of the coal seam and strata follows an exponential relationship with the first invariant of effective stress and pore pressure (Eq. 8). [Chen 2018, pp. 4-5]

## Key Variables / Parameters
- **Permeability (K):** Hydraulic conductivity of the geological media, which changes with stress in Approach III. [Chen 2018, pp. 4-5]
- **Stress Sensitivity Coefficient (β):** Critical parameter in the exponential permeability-stress relationship (Eq. 8). Sensitivity analysis showed 3β is optimal. [Chen 2018, pp. 14-16]
- **Biot Coefficient (α):** Relates pore pressure to effective stress; α ≈ 0.55 for the coal seam. [Chen 2018, pp. 9-10]
- **Vertical Stress Variation Rate (σR):** Ratio of post-mining to pre-mining vertical stress, used to characterize stress relief. [Chen 2018, pp. 10-12]
- **Permeability Variation Rate (KR):** Logarithmic measure of permeability change due to mining. [Chen 2018, pp. 12-14]
- **Flow Influx (Q):** Volumetric flow rate of groundwater into the excavation, calculated via surface integration (Eq. 16). [Chen 2018, pp. 14-16]

## Reusable Claims
- Incorporating stress-dependent permeability changes into a Biot poroelastic model significantly improves the prediction of groundwater inflow into longwall coal mine excavations compared to models with constant permeability. [Chen 2018, pp. 14-16]
- The stress sensitivity coefficient (β) in the exponential permeability-stress relationship is a critical parameter for modeling fluid influx; a value of 3β provided the best fit to field data in this case study. [Chen 2018, pp. 14-16]
- Mining-induced stress relief leads to significant permeability increases in the de-stressed (caving) zone, with permeability decreasing further from the excavation. [Chen 2018, pp. 12-14]
- The maximum groundwater flow rate in a basic Darcy model occurs at the excavation corners and remains constant, failing to capture the increasing inflow observed in the field. [Chen 2018, pp. 10-12, 16-17]

## Candidate Concepts
- [[Biot poroelasticity]]
- [[Stress-induced permeability alteration]]
- [[Longwall mining]]
- [[Groundwater inflow]]
- [[Hydro-mechanical coupling]]
- [[Finite element modeling]]
- [[Effective stress]]
- [[Aquifer depressurization]]

## Candidate Methods
- [[Computational modeling]]
- [[Finite element method]]
- [[Sensitivity analysis]]
- [[Darcy's law]]
- [[Poroelastic constitutive model]]
- [[Exponential permeability-stress relationship]]

## Connections To Other Work
- The study builds on Biot's classical poroelastic theory (Biot 1941) for modeling coupled hydro-mechanical behavior. [Chen 2018, pp. 2-3]
- It references prior field studies on mine water inflow, aquifer level fluctuations, and hydraulic conductivity changes due to longwall mining (e.g., Wang and Park 2003; Zhang et al. 2010; Özgen Karacan and Goodman 2009). [Chen 2018, pp. 1-2]
- The modeling approaches are compared to previous numerical studies using conventional groundwater flow models (e.g., Doulati Ardejani et al. 2003; Rapantova et al. 2007) and poroelastic models (e.g., Kim et al. 1997; Guo et al. 2009). [Chen 2018, pp. 2-3]
- The use of COMSOL™ Multiphysics for poromechanics with stress-dependent properties is documented in works by Selvadurai and Suvorov (2012, 2014) and others. [Chen 2018, pp. 9-10]
- The stress-dependent permeability relationship (Eq. 8) follows the general form presented by Zhao (2010). [Chen 2018, pp. 4-5]

## Open Questions
- How would incorporating anisotropy and heterogeneity in rock properties affect the modeling results?
- What is the long-term evolution of groundwater inflow and permeability after mining ceases?
- How applicable are the findings and the optimal stress sensitivity coefficient (3β) to other geological settings and coal mines?
- Can more advanced laboratory techniques accurately measure the full anisotropic tensor of permeability alteration under stress?

## Source Coverage
All 13 non-empty indexed fragments were processed. The compiled source blocks total 13, with 63,154 characters compiled from 63,731 indexed characters, resulting in a coverage ratio by characters of 0.990946. The coverage status is full-index.
