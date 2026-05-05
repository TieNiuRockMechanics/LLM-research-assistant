---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2017-ritter-growing-faults-in-the-lab-insights-into-the-scale-dependence-of-the-fault-zone-evolu"
title: "Growing Faults in the Lab: Insights into the Scale Dependence of the Fault Zone Evolution Process."
status: "draft"
source_pdf: "data/papers/Growing Faults in the Lab Insights Into the Scale Dependence of the Fault Zone Evolution Process.pdf"
collections:
citation: "Ritter, Malte C., et al. \"Growing Faults in the Lab: Insights into the Scale Dependence of the Fault Zone Evolution Process.\" *Tectonics*, doi:10.1002/2017TC004787. Accessed 2026."
indexed_texts: "14"
indexed_chars: "66833"
nonempty_source_blocks: "14"
compiled_source_blocks: "14"
compiled_source_chars: "67198"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.005461"
coverage_status: "full-index"
source_signature: "8f1c611ce3b560d6565c3c8dc532922c08ddbd59"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:21:25"
---

# Growing Faults in the Lab: Insights into the Scale Dependence of the Fault Zone Evolution Process.

## One-line Summary
Analog sandbox experiments demonstrate that the work required for fault propagation scales approximately with the square of fault system length, supporting dynamic similarity to natural fault growth and identifying diffuse deformation as the primary energy sink analogous to natural damage zones.

## Research Question
To what extent can the dynamics of strain localization and fault zone formation observed in analog sandbox experiments be extrapolated to natural prototypes, and specifically, how does the work of fault propagation (Wprop) scale with fault system length (l)?

## Study Area / Data
The study uses analog sandbox experiments conducted in two laboratory setups: a custom-built strike-slip shear box and a ring-shear tester (RST). The analog material is quartz sand (type G23T) with a mean grain size of 300 µm [Accessed 2026, pp. 4-7]. The strike-slip experiments used sand packs 50 mm high and 750 mm wide, with fault system lengths (l) of 200 mm, 300 mm, and 400 mm [Accessed 2026, pp. 7-9]. The RST experiments used blade distances (l) of 24.4 mm, 48.8 mm, and 97.6 mm [Accessed 2026, pp. 7-9].

## Methods
1.  **Experimental Setups:** A strike-slip shear box induced deformation by pushing part of a sand pack against a stationary back-wall, with a low-viscosity silicone paste layer minimizing basal traction [Accessed 2026, pp. 4-7]. A ring-shear tester (RST) sheared an annular sand sample between a rotating cell and a stationary lid equipped with radial blades [Accessed 2026, pp. 7-9].
2.  **Monitoring:** Surface deformation in strike-slip experiments was captured by a digital camera and analyzed using Digital Image Correlation (DIC) to calculate displacement fields and vorticity [Accessed 2026, pp. 7-9, 12-14]. Force sensors recorded the pushing force (strike-slip) or torque (RST) [Accessed 2026, pp. 7-9].
3.  **Quantification:** The work of fault propagation (Wprop) was defined as the area under the hardening-weakening peak in the shear force vs. displacement curve, normalized to fault height [Accessed 2026, pp. 9-12]. The volume of deformed material (V) was measured from DIC data by counting pixels exceeding a deformation threshold, distinguishing between diffuse and localized deformation using Otsu's algorithm [Accessed 2026, pp. 12-14].

## Key Findings
1.  **Scaling of Work:** The work of fault propagation (Wprop) increases non-linearly with fault system length (l). A power-law fit to the combined dataset yields Wprop = 10(2) J m⁻¹ (l/l₀)^2.3(2), where l₀ is unit length [Accessed 2026, pp. 16-19]. This is approximately quadratic and consistent with theoretical predictions for natural faults [Accessed 2026, pp. 1-4, 16-19].
2.  **Energy Sink:** Wprop is directly proportional to the volume of diffusely deformed material (Vdiff), with a constant work per volume of about 55 J m⁻³ [Accessed 2026, pp. 19-22, 24-27]. This identifies diffuse deformation as the main energy sink during fault formation.
3.  **Strain Evolution:** Deformation begins diffusely and localizes onto discrete shear zones. The volume of localized deformation per fault length is constant, while the volume including diffuse deformation increases over-proportionally with l [Accessed 2026, pp. 12-14].
4.  **Dynamic Similarity:** The scaling of Wprop with l² in the models is consistent with estimates for natural fault zones, supporting the dynamic similarity of sandbox experiments [Accessed 2026, pp. 22-24, 24-27].
5.  **Weakening:** The relative force drop during weakening (ΔF) is independent of l but differs between setups (mean 0.19 for RST, 0.43 for strike-slip) due to differences in fault geometry (single vs. double fault evolution) [Accessed 2026, pp. 14-16].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Wprop scales with l^2.3 in sandbox experiments. | [Accessed 2026, pp. 16-19] | Quartz sand (G23T), normal loads ~500 Pa, l from 24.4 mm to 400 mm. | Power-law fit to combined RST and strike-slip data. |
| Wprop is proportional to volume of diffuse deformation (Vdiff). | [Accessed 2026, pp. 19-22, 24-27] | Same as above. | Work per volume of diffuse deformation is ~55 J m⁻³. |
| Diffuse deformation precedes localization and its volume increases non-linearly with l. | [Accessed 2026, pp. 12-14] | Strike-slip experiments, l = 200, 300, 400 mm. | Measured via DIC and pixel thresholding. |
| Relative weakening (ΔF) is independent of l. | [Accessed 2026, pp. 14-16] | RST and strike-slip setups. | ΔF differs between setups due to fault geometry. |
| Scaling of Wprop in models is numerically similar to estimates for natural faults (e.g., Punchbowl fault). | [Accessed 2026, pp. 22-24] | Using scaling factors from Ritter et al. [2016]. | Model Wprop scaled to nature yields 3.5 x 10¹² J m⁻¹, within range of natural estimates. |

## Limitations
1.  The final shear zones in strike-slip experiments were often curved, potentially indicating incomplete weakening and a slight underestimation of Wprop [Accessed 2026, pp. 16-19].
2.  The assumption that a constant normal load (500 Pa) in the RST represents the average lithostatic load in the strike-slip box is an approximation, though stable sliding forces were similar [Accessed 2026, pp. 16-19].
3.  The number of experiments conducted is relatively low, which may increase the total error beyond the statistical fit uncertainty [Accessed 2026, pp. 16-19].
4.  The study focuses on strike-slip kinematics; applicability to other fault regimes (e.g., dip-slip) is not tested.

## Assumptions / Conditions
1.  Deformation of sand follows a velocity-independent rheology [Accessed 2026, pp. 9-12].
2.  The onset of dilation is equivalent to the onset of strain localization [Accessed 2026, pp. 9-12].
3.  The experimental setups provide a quasi-2D representation of fault processes [Accessed 2026, pp. 9-12].
4.  The diffuse deformation observed in sand is analogous to distributed deformation on sub-seismic-resolution faults in nature [Accessed 2026, pp. 1-4, 24-27].

## Key Variables / Parameters
-   **Fault system length (l):** The extent of the fault in the slip direction, systematically varied in experiments.
-   **Work of fault propagation (Wprop):** Work per unit fault height required to form the fault zone, measured as the area under the hardening-weakening peak.
-   **Deformed volume (V):** Total volume of material that underwent deformation, split into localized (Vloc) and diffuse (Vdiff) components.
-   **Relative weakening (ΔF):** Dimensionless measure of force drop during localization: ΔF = 1 - (Fs/Fp).

## Reusable Claims
1.  **Condition:** In analog sandbox experiments using granular materials under quasi-static, strike-slip deformation. **Claim:** The work required for fault propagation scales approximately with the square of the fault system length, following a power law with an exponent of ~2.3.
2.  **Condition:** For fault growth in granular analog materials. **Claim:** The majority of the work budget for fault formation is consumed by diffuse, distributed deformation prior to localization, not by the creation of the final discrete shear zone.
3.  **Condition:** When comparing scaled analog models to natural fault systems. **Claim:** The quadratic scaling of fault propagation work with fault length observed in sandbox experiments is consistent with theoretical and empirical estimates for natural faults, supporting dynamic similarity.
4.  **Condition:** In the evolution of a strike-slip fault system between two fixed boundaries. **Claim:** The formation of restraining bends and overlapping fault segments can occur spontaneously due to stress interactions, without requiring pre-existing inherited structures.

## Candidate Concepts
- [[strain localization]]
- [[damage zone]]
- [[dynamic similarity]]
- [[fault propagation work]]
- [[analog modeling]]
- [[distributed deformation]]
- [[restraining bend]]

## Candidate Methods
- [[analog sandbox experiments]]
- [[digital image correlation (DIC)]]
- [[ring-shear tester]]
- [[work budget analysis]]
- [[power-law scaling]]

## Connections To Other Work
-   Contrasts with the linear scaling of Wprop with l implied by Herbert et al. [2015], attributing the discrepancy to their limited range of l [Accessed 2026, pp. 16-19].
-   Supports the general framework of fault growth and energy minimization discussed in minimum-work models (e.g., Mitra and Boyer [1986]; Cooke and Madden [2014]) [Accessed 2026, pp. 4-7].
-   Extends observations of diffuse/ephemeral deformation preceding localization from previous sandbox studies (e.g., Adam et al. [2005]; Dotare et al. [2016]) by providing quantitative energy and volume scaling [Accessed 2026, pp. 1-4].
-   Uses scaling factors for strength and strain weakening from Ritter et al. [2016] to compare model results with natural fault data [Accessed 2026, pp. 22-24].

## Open Questions
1.  How does the scaling relationship change for different tectonic regimes (e.g., thrust, normal faults) or material properties?
2.  What is the precise micro-mechanical link between the volume of diffuse deformation and the work consumed?
3.  Can the succession of short-lived, differently oriented shear zones observed at experiment boundaries be identified in natural fault systems?
4.  How do inherited structures interact with the spontaneous formation of restraining bends observed in the models?

## Source Coverage
All 14 non-empty indexed fragments were processed. The compiled source blocks total 14, with a compiled character count of 67,198 against an indexed character count of 66,833, yielding a coverage ratio by characters of 1.005. The coverage status is full-index.
