---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2018-bai-numerical-study-on-the-heat-transfer-characteristics-between-supercritical-carbon-dioxi"
title: "Numerical Study on the Heat Transfer Characteristics between Supercritical Carbon Dioxide and Granite Fracture Wall."
status: "draft"
source_pdf: "data/papers/Numerical-study-on-the-heat-transfer-characteristics-between-sup_2018_Geothe.pdf"
collections:
citation: "Bai, Bing, et al. \"Numerical Study on the Heat Transfer Characteristics between Supercritical Carbon Dioxide and Granite Fracture Wall.\" *Geothermics*, vol. 75, 2018. doi:10.1016/j.geothermics.2018.03.002. Accessed 2026."
indexed_texts: "8"
indexed_chars: "36571"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "36728"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004293"
coverage_status: "full-index"
source_signature: "c7e0e40b2b804fca642be635c2478e57659e2408"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T01:08:06"
---

# Numerical Study on the Heat Transfer Characteristics between Supercritical Carbon Dioxide and Granite Fracture Wall.

## One-line Summary
A 2D numerical model was developed and validated to investigate the flow and heat transfer characteristics of supercritical CO2 through straight and rough granite fractures, finding that increased roughness and flow rate improve heat transfer performance.

## Research Question
How do flow rate, fracture roughness, and the phase state of CO2 influence the heat transfer characteristics between supercritical carbon dioxide and a granite fracture wall? [Bai 2018, pp. 1-1]

## Study Area / Data
The study is a numerical investigation. The model was validated using experimental data from a straight granite fracture (Fracture A) with a 0.2 mm aperture, a specimen size of 50 mm × 50 mm, a confining temperature of 200 °C, and scCO2 pressure of 8 MPa. Simulations for rough fractures (B and C) used the same specimen dimensions and boundary conditions but with artificial inlet temperatures. [Bai 2018, pp. 2-3, 3-5, 5-6]

## Methods
A two-dimensional numerical model was developed based on the Comsol Multiphysics simulator. The model couples the Navier-Stokes equations for single-phase scCO2 flow with the heat conduction equation for the granite specimen. The physical properties of scCO2 (density, specific heat capacity, thermal conductivity, viscosity) were calculated using REFPROP9.0 and interpolated based on temperature at a constant pressure of 8.0 MPa. The model was first validated against experimental data from a straight fracture and then applied to study rough fractures. Overall Heat Transfer Coefficient (OHTC) was calculated using three different formulas from literature, and Local Heat Transfer Coefficient (LHTC) was calculated at each discretized element. [Bai 2018, pp. 1-2, 2-3, 3-5, 5-6]

## Key Findings
1.  The numerical model for scCO2 flow and heat transfer was validated, with simulated outlet temperatures showing a maximum relative deviation of 10.5% from experimental results. [Bai 2018, pp. 3-5]
2.  Increased fracture roughness or scCO2 flow rate improves the heat transfer performance. The outlet temperature of scCO2 in a rough fracture was higher than in a straight fracture under the same conditions. [Bai 2018, pp. 5-6, 8-8]
3.  The temperature of the fracture wall was always higher than that of the scCO2 at the same position, especially near the inlet. [Bai 2018, pp. 5-6]
4.  The Overall Heat Transfer Coefficient (OHTC) of scCO2 increased with the injection flow rate. [Bai 2018, pp. 5-6, 8-8]
5.  Fracture surface morphology significantly influences the Local Heat Transfer Coefficient (LHTC) distribution. LHTC exhibited a negative correlation with local waviness (Ra); sunken positions had significantly larger LHTCs than prominent positions. [Bai 2018, pp. 5-6, 8-8]
6.  The heat transfer characteristics of CO2 are closely related to its phase state. Supercritical CO2 (denser phase) showed better heat transfer performance than gaseous CO2. For scCO2, higher pressure led to better heat transfer performance. [Bai 2018, pp. 6-8, 8-8]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| The proposed 2D numerical model for scCO2 was validated against experimental data from a straight granite fracture. | [Bai 2018, pp. 3-5] | Straight fracture (A), 0.2 mm aperture, 200°C confining temp, 8 MPa pressure, flow rates 0.13-0.75 kg/h. | Maximum relative deviation between simulated and experimental outlet temperatures was 10.5%. |
| Rough fracture led to higher scCO2 outlet temperature compared to straight fracture under same simulation conditions. | [Bai 2018, pp. 5-6] | Compared straight and rough fractures at same flow rate (e.g., 0.13 kg/h). | Indicates increased roughness improves heat transfer efficiency. |
| OHTC of scCO2 increased with mass flow rate. | [Bai 2018, pp. 5-6] | Flow rates of 0.13, 0.35, 0.51, and 0.75 kg/h. | Calculated using three different OHTC formulas (Eqs. 5, 6, 7). |
| LHTC distribution is significantly influenced by fracture surface morphology and negatively correlates with local waviness (Ra). | [Bai 2018, pp. 5-6] | Rough fractures B and C. | Sunken positions exhibited much larger LHTCs than prominent positions. |
| scCO2 (denser phase) has better heat transfer performance than gaseous CO2. | [Bai 2018, pp. 6-8] | Compared scCO2 at different pressures with gaseous CO2 for a given fracture (B) and flow rate (0.75 kg/h). | OHTC and LHTC values for scCO2 were higher than for gaseous CO2. |
| For scCO2, higher pressure leads to better heat transfer performance. | [Bai 2018, pp. 6-8] | scCO2 at different pressures, same fracture and flow rate. | OHTC increased with pressure for a fixed flow rate. |

## Limitations
1.  For the rough fracture simulations, inlet fluid temperatures were artificially set due to the absence of experimental data, though this is argued to be physically feasible. [Bai 2018, pp. 5-6]
2.  The model assumes negligible buoyancy effects due to the small density gradient in the micron-scale aperture. [Bai 2018, pp. 2-3]
3.  The pressure drop across the fracture was considered to have a minor effect on scCO2 physical parameters, which were taken as constant along the fracture length for a given pressure. [Bai 2018, pp. 2-3]
4.  The study is numerical; direct experimental validation for heat transfer in rough granite fractures with scCO2 is lacking. [Bai 2018, pp. 5-6]

## Assumptions / Conditions
1.  Single-phase scCO2 flow is assumed. [Bai 2018, pp. 2-3]
2.  The flow is laminar (Reynolds numbers below critical). [Bai 2018, pp. 3-5]
3.  Buoyancy induced by density gradients is negligible. [Bai 2018, pp. 2-3]
4.  The effect of pressure drop on scCO2 physical properties is minor. [Bai 2018, pp. 2-3]
5.  The average temperature of the inlet and outlet fracture walls equals the average temperature of the inlet and outlet fluid, a premise for using a specific OHTC formula (Eq. 7). [Bai 2018, pp. 5-6]

## Key Variables / Parameters
-   **Flow Rate (ṁ):** Mass flow rate of scCO2 (kg/h). Varied as 0.13, 0.35, 0.51, 0.75 kg/h. [Bai 2018, pp. 1-1, 3-5]
-   **Fracture Roughness:** Characterized by waviness (Ra). Influences LHTC distribution. [Bai 2018, pp. 5-6]
-   **Phase State of CO2:** Supercritical vs. gaseous. Affects heat transfer performance. [Bai 2018, pp. 6-8]
-   **Pressure:** Set at 8 MPa for main scCO2 simulations; varied to study phase effect. [Bai 2018, pp. 1-1, 6-8]
-   **Confining Temperature:** Outer wall temperature of specimen, set at 200 °C. [Bai 2018, pp. 1-1, 3-5]
-   **Overall Heat Transfer Coefficient (OHTC):** Characterizes overall heat transfer across the entire fracture. [Bai 2018, pp. 5-6]
-   **Local Heat Transfer Coefficient (LHTC):** Characterizes heat transfer at a specific position on the fracture wall. [Bai 2018, pp. 5-6]

## Reusable Claims
-   Increasing the mass flow rate of supercritical CO2 enhances the Overall Heat Transfer Coefficient (OHTC) in granite fractures. [Bai 2018, pp. 5-6, 8-8]
-   Increased surface roughness of granite fractures improves the heat transfer efficiency of flowing supercritical CO2. [Bai 2018, pp. 5-6, 8-8]
-   The Local Heat Transfer Coefficient (LHTC) for supercritical CO2 in rough granite fractures is negatively correlated with local surface waviness, with sunken positions exhibiting higher LHTCs than prominent ones. [Bai 2018, pp. 5-6, 8-8]
-   Supercritical CO2 (denser phase) demonstrates superior heat transfer performance compared to gaseous CO2 in granite fractures. [Bai 2018, pp. 6-8, 8-8]
-   For supercritical CO2, higher operating pressure leads to improved heat transfer performance in granite fractures. [Bai 2018, pp. 6-8, 8-8]

## Candidate Concepts
-   [[Supercritical carbon dioxide (scCO2)]]
-   [[Enhanced Geothermal System (EGS)]]
-   [[Hot Dry Rock (HDR)]]
-   [[Heat transfer coefficient]]
-   [[Fracture roughness]]
-   [[Rock-fluid interaction]]

## Candidate Methods
-   [[Numerical modeling (COMSOL Multiphysics)]]
-   [[Navier-Stokes equations]]
-   [[Heat conduction equation]]
-   [[REFPROP (thermophysical property database)]]
-   [[Overall Heat Transfer Coefficient (OHTC) calculation]]
-   [[Local Heat Transfer Coefficient (LHTC) calculation]]

## Connections To Other Work
-   The study builds upon and validates a 2D numerical model previously developed for water flow in granite fractures by Bai et al. (2016). [Bai 2018, pp. 1-2, 3-5]
-   It uses experimental data from Zhang et al. (2016b) for model validation in a straight granite fracture. [Bai 2018, pp. 2-3, 3-5]
-   It compares findings on scCO2 heat transfer with prior work on water and gaseous CO2 heat transfer in fractures (e.g., Bai et al., 2017; He et al., 2017). [Bai 2018, pp. 5-6, 6-8]
-   The research addresses a gap identified in the introduction regarding poorly understood heat transfer between scCO2 and granite fracture walls, especially for rough fractures. [Bai 2018, pp. 1-2]

## Open Questions
-   How do the findings from this 2D numerical study translate to more complex, 3D fracture networks in real EGS reservoirs?
-   What are the long-term effects of scCO2-granite interaction (e.g., geochemical reactions) on fracture morphology and heat transfer characteristics?
-   How do two-phase (water-CO2 mixture) conditions, relevant to Zone 2 of a CO2-EGS, affect the heat transfer process compared to single-phase scCO2?
-   Can the model be extended to incorporate non-Darcy flow effects at higher flow rates or in more complex fracture geometries?

## Source Coverage
All non-empty indexed fragments were processed. The compilation used 8 source blocks containing a total of 36,571 characters. The compiled page contains 36,728 characters, resulting in a coverage ratio by characters of 1.004. The coverage status is full-index.
