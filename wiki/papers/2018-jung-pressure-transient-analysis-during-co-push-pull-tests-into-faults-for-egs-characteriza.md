---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2018-jung-pressure-transient-analysis-during-co-push-pull-tests-into-faults-for-egs-characteriza"
title: "Pressure transient analysis during CO₂ push-pull tests into faults for EGS characterization."
status: "draft"
source_pdf: "data/papers/Pressure transient analysis during CO2 push-pull tests into faults for EGS characterization.pdf"
collections:
citation: "Jung, Yoojin, et al. \"Pressure transient analysis during CO₂ push-pull tests into faults for EGS characterization.\" *Geothermics*, vol. 75, 2018, pp. 180–191. doi:10.1016/j.geothermics.2018.05.004."
indexed_texts: "11"
indexed_chars: "54910"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "55148"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004334"
coverage_status: "full-index"
source_signature: "20aabbc056f37aa9342c162fcccb2f27349475ec"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:41:19"
---

# Pressure transient analysis during CO₂ push-pull tests into faults for EGS characterization.

## One-line Summary
This study evaluates the feasibility of using pressure transient monitoring during CO₂ push-pull tests to characterize faults in Enhanced Geothermal Systems (EGS), finding that pressure data are most sensitive to fault gouge permeability.

## Research Question
Can pressure transient analysis during CO₂ push-pull tests complement active seismic and wireline well logging for characterizing faults and fractures in Enhanced Geothermal Systems (EGS)? [Jung 2018, pp. 1-2]

## Study Area / Data
The study uses a simplified 2D numerical model based on the Desert Peak geothermal field in Nevada, USA. The model includes a single dipping fault zone consisting of a slip plane, fault gouge, and damage zone, bounded by surrounding country rock matrix. [Jung 2018, pp. 2-2] The reservoir temperature is 207–218 °C. [Jung 2018, pp. 2-2]

## Methods
A 2D numerical model was developed using TOUGH2/ECO2N V2.0 to simulate two-phase flow of CO₂ and water during push-pull injection-withdrawal cycles. [Jung 2018, pp. 2-2] Sensitivity analysis and inverse modeling were performed using iTOUGH2-PEST. [Jung 2018, pp. 2-2] The model simulated a 4-day CO₂ injection (push) period followed by a 4-day withdrawal (pull) period at a constant pressure differential of ±0.3 MPa. [Jung 2018, pp. 2-3] Monitoring wells were placed at 50 m, 100 m, and 200 m above the injection well along the fault gouge. [Jung 2018, pp. 3-4]

## Key Findings
1.  The pressure transient at monitoring wells shows unique traits due to multiphase flow conditions developed by CO₂ injection, varying sensitively with the arrival of the CO₂ plume and the degree of CO₂ saturation. [Jung 2018, pp. 1-2]
2.  Sensitivity analysis shows the pressure transient is most sensitive to fault gouge permeability. [Jung 2018, pp. 1-2]
3.  The maximum pressure increase observed during the push period can be larger than the injection-induced pressure change at the well due to the formation of a low-density CO₂ gas column. [Jung 2018, pp. 4-7]
4.  Inverse modeling reveals that fault gouge permeability can be best estimated with pressure transient data alone; adding CO₂ saturation data does not significantly improve the accuracy of the inversion. [Jung 2018, pp. 1-2, 10-11]
5.  Pressure transients are strongly influenced by multiphase flow conditions, making them more complex than those from a water push-pull test. [Jung 2018, pp. 11-11]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Pressure transient is most sensitive to fault gouge permeability. | [Jung 2018, pp. 1-2] | Sensitivity analysis of 2D fault model. | Total scaled sensitivity for pressure at MW 200m during push period: 105.1 for fault gouge vs. 4.3 for damage zone and 5.6 for matrix. |
| Fault gouge permeability is most accurately estimated using pressure transient data. | [Jung 2018, pp. 10-11] | Inverse modeling of synthetic data. | Estimated log(k_fltgg) = -11.67 (true value -11.70) using pressure data alone at MW 200m. |
| Adding CO₂ saturation data does not significantly improve inversion accuracy for fault gouge permeability. | [Jung 2018, pp. 10-11] | Inverse modeling with pressure and saturation data. | Estimated log(k_fltgg) = -11.77 using both data types at MW 200m, slightly worse than pressure-only result. |
| Pressure increase in fault can exceed injection overpressure due to gas column formation. | [Jung 2018, pp. 4-7] | Forward simulation of CO₂ push. | Maximum ΔP observed (~0.85 MPa) > ΔP_inj (0.3 MPa). |
| CO₂ recovery during pull period is very low (1.7%). | [Jung 2018, pp. 3-4] | Forward simulation of CO₂ push-pull. | Buoyancy drives CO₂ upward, out of the well's capture zone. |
| Pressure transient is sensitive to top boundary conditions (fault connectivity). | [Jung 2018, pp. 9-10] | Sensitivity analysis with open, closed, and semi-closed top boundaries. | Pressure bounces back at late times for closed/semi-closed tops. |

## Limitations
1.  The model uses a coarse grid in the z-direction (dz = 10 m), which causes spurious pressure oscillations and is not intended to accurately reproduce near-wellbore effects. [Jung 2018, pp. 2-3, 7-7]
2.  The impact of salinity on pressure transient is not considered; salinity and initial dissolved CO₂ concentration are assumed to be zero. [Jung 2018, pp. 2-3]
3.  The model assumes all other parameters (except permeabilities in inversion) are known and error-free. [Jung 2018, pp. 10-11]
4.  The study focuses on feasibility, not on calibrating or characterizing a real geothermal site. [Jung 2018, pp. 7-7]

## Assumptions / Conditions
1.  The fault zone consists of a slip plane, fault gouge, and damage zone with distinct hydrological properties. [Jung 2018, pp. 2-2]
2.  The injection/withdrawal well is open only in the fault gouge and slip plane. [Jung 2018, pp. 2-3]
3.  Injected CO₂ is preheated to the ambient reservoir temperature. [Jung 2018, pp. 2-3]
4.  CO₂ saturation data from well logging are available for inversion scenarios. [Jung 2018, pp. 3-4]
5.  The initial condition is hydrostatic with a water table 30 m below the surface. [Jung 2018, pp. 2-3]

## Key Variables / Parameters
-   **Fault Gouge Permeability**: The most sensitive parameter for pressure transient. Base value: 10⁻¹² m². [Jung 2018, pp. 2-3, 7-9]
-   **Damage Zone Permeability**: Base value: 10⁻¹⁵ m². [Jung 2018, pp. 2-3]
-   **Matrix Permeability**: Varies by rock type (e.g., 10⁻¹⁶ to 10⁻¹⁹ m²). [Jung 2018, pp. 2-3]
-   **Multiphase Flow Parameters**: van Genuchten parameters (λ_relp, λ_pcap), residual liquid saturation (Slr), capillary strength (P0). [Jung 2018, pp. 2-3, 7-9]
-   **Pressure Difference (ΔP)**: P - P_init, used to describe all pressure data. [Jung 2018, pp. 2-3]

## Reusable Claims
1.  **Condition**: For a fault-dominated EGS reservoir. **Limitation**: Based on a simplified 2D model. **Claim**: Pressure transient data collected during a CO₂ push-pull test are most sensitive to and can most accurately estimate the permeability of the fault gouge. [Jung 2018, pp. 1-2, 10-11]
2.  **Condition**: During CO₂ injection into a dipping fault. **Limitation**: Assumes a gas column forms. **Claim**: The pressure buildup at monitoring points above the injection interval can exceed the injection-induced pressure at the well due to the density contrast between the CO₂ gas column and the resident brine. [Jung 2018, pp. 4-7]
3.  **Condition**: When characterizing fault properties using pressure data. **Limitation**: Assumes multiphase flow parameters are uncertain. **Claim**: The added benefit of incorporating CO₂ saturation data from well logging for improving the accuracy of fault gouge permeability estimation via inversion is minor compared to using pressure transient data alone. [Jung 2018, pp. 10-11]

## Candidate Concepts
-   [[Enhanced Geothermal Systems (EGS)]]
-   [[Fault Zone]]
-   [[Fault Gouge]]
-   [[Damage Zone]]
-   [[Pressure Transient Analysis]]
-   [[CO₂ Push-Pull Test]]
-   [[Multiphase Flow]]
-   [[Supercritical CO₂]]
-   [[Geophysical Imaging]]

## Candidate Methods
-   [[TOUGH2/ECO2N]]
-   [[iTOUGH2]]
-   [[Numerical Simulation]]
-   [[Sensitivity Analysis]]
-   [[Inverse Modeling]]
-   [[Latin Hypercube Sampling]]

## Connections To Other Work
This study builds upon and evaluates a new technology for EGS characterization proposed by Borgia et al. (2015, 2017a,b), Oldenburg et al. (2016), and Zhang et al. (2015), which combines CO₂ push-pull testing with active-source geophysical imaging and well logging. [Jung 2018, pp. 1-2] The model is adapted from Borgia et al. (2017a,b). [Jung 2018, pp. 2-2]

## Open Questions
1.  How would salinity and more complex geochemistry affect the pressure transients and inversion results?
2.  Can the method be validated with field data from a real EGS site?
3.  How would a finer grid resolution, particularly in the z-direction, affect the results and mitigate the observed pressure oscillations?
4.  What is the optimal monitoring well placement and data collection frequency for field applications?

## Source Coverage
All 11 non-empty indexed fragments were processed. The compiled source blocks total 11, with a compiled character count of 55,148, representing a coverage ratio of 1.004334 by characters relative to the indexed character count of 54,910. The coverage status is full-index.
