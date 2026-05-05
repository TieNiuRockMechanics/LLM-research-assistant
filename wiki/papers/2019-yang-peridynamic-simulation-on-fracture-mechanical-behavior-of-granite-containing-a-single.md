---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-yang-peridynamic-simulation-on-fracture-mechanical-behavior-of-granite-containing-a-single"
title: "Peridynamic Simulation on Fracture Mechanical Behavior of Granite Containing a Single Fissure after Thermal Cycling Treatment."
status: "draft"
source_pdf: "data/papers/Peridynamic simulation on fracture mechanical behavior of granite containing a single fissure after thermal cycling treatment.pdf"
collections:
citation: "Yang, Zhen, et al. \"Peridynamic Simulation on Fracture Mechanical Behavior of Granite Containing a Single Fissure after Thermal Cycling Treatment.\" *Computers and Geotechnics*, 2019, doi:10.1016/j.compgeo.2019.103414. Accessed 2026."
indexed_texts: "17"
indexed_chars: "82056"
nonempty_source_blocks: "17"
compiled_source_blocks: "17"
compiled_source_chars: "82378"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.003924"
coverage_status: "full-index"
source_signature: "f710c661cf7ef142e168fabe87bb1bb69f717096"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T01:11:29"
---

# Peridynamic Simulation on Fracture Mechanical Behavior of Granite Containing a Single Fissure after Thermal Cycling Treatment.

## One-line Summary
This study uses a fully coupled ordinary state-based peridynamic method to simulate the thermal-mechanical fracturing behavior of granite containing a single fissure after thermal cycling treatment, proposing a new method for modeling heterogeneity and investigating the combined effects of temperature and fissure angle on crack evolution.

## Research Question
How does thermal cycling treatment affect the fracture mechanical behavior, including stress-strain response, crack initiation, propagation, coalescence, and ultimate failure modes, of granite containing a single pre-existing fissure with various inclination angles under subsequent uniaxial compression?

## Study Area / Data
The numerical models are based on granite specimens with dimensions of length L = 80 mm and height H = 160 mm, containing a single pre-existing opening fissure with a width of 1.5 mm and length of 20 mm [Yang 2019, pp. 8-10]. The fissure inclination angle (βa) is varied from 0° to 90° at intervals of 15° [Yang 2019, pp. 13-16]. Mineral compositions and their thermal expansion coefficients are sourced from experimental data on granite specimens [Yang 2019, pp. 10-11, 13-16].

## Methods
The study employs the fully coupled ordinary state-based peridynamic (OSB-PD) thermomechanics framework [Yang 2019, pp. 2-3]. A new method using a shuffle algorithm (Knuth-Durstenfeld) is proposed to accurately reflect mineral compositions and simulate the heterogeneity of rock materials [Yang 2019, pp. 10-11]. The thermal cycling treatment consists of three stages: infrared radiation heating, constant temperature, and natural cooling, simulated using a multi-rate explicit time integration scheme [Yang 2019, pp. 5-6, 11-13]. A "no fail zone" is applied in boundary layers to reduce unexpected thermal shock cracks [Yang 2019, pp. 16-17]. Subsequent uniaxial compression is simulated using forward difference time integration [Yang 2019, pp. 5-6]. Parameter calibration is performed via benchmark tests for transient heat conduction and crack propagation [Yang 2019, pp. 6-10].

## Key Findings
1.  The ductility property of the rock material increases with increasing testing temperature [Yang 2019, pp. 19-21].
2.  Thermal crack evolution does not end with the heating stage; cracks continue to propagate and coalesce during the cooling stage [Yang 2019, pp. 19-21].
3.  After thermal treatment, the crack initiation pattern shifts from tensile wing cracks or secondary tensile cracks to being dominated by anti-tensile wing cracks [Yang 2019, pp. 19-21].
4.  Under 600°C treatment, numerous thermal microcracks initiate radially around the fissure, propagate, and coalesce throughout the specimen. During loading, these cracks connect anti-tensile wing cracks into reticulate cracks, leading to a notable tensile failure mode [Yang 2019, pp. 19-21].
5.  Under 300°C treatment, thermal microcracks are radially distributed around the fissure and converge into damage zones during cooling. During loading, anti-tensile wing cracks initiate asymmetrically, followed by secondary shear and anti-shear cracks [Yang 2019, pp. 19-21].
6.  The combination of temperature and fissure angle influences peak strength, peak strain, and crack evolution processes [Yang 2019, pp. 13-16, 19-21].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Thermal microcracks induced by incompatible mineral expansion coalesce throughout the specimen under 600°C treatment. | [Yang 2019, pp. 11-13] | Granite specimen, 1000°C peak temperature, thermal cycling. | Simulated using proposed heterogeneity method. |
| Peak strength decreases and peak strain increases as treatment temperature increases from 20°C to 600°C. | [Yang 2019, pp. 16-17] | Fissured granite (βa = 45°), uniaxial compression after thermal cycling. | Agreement with experimental results [2]. |
| Crack initiation shifts from tensile wing cracks to anti-tensile wing cracks after thermal treatment. | [Yang 2019, pp. 19-21] | Fissured granite, uniaxial compression after thermal cycling. | Inhibited tensile crack initiation. |
| Under 600°C, thermal cracks connect anti-tensile wing cracks into reticulate cracks during loading. | [Yang 2019, pp. 19-21] | Fissured granite (βa = 45°), uniaxial compression after 600°C treatment. | Notable tensile failure mode observed. |
| Under 300°C, anti-tensile wing cracks initiate asymmetrically, followed by secondary shear and anti-shear cracks. | [Yang 2019, pp. 19-21] | Fissured granite (βa = 15°), uniaxial compression after 300°C treatment. | Crack surfaces are smoother than at 600°C. |
| The "no fail zone" with specified depths effectively eliminates thermal shock cracks. | [Yang 2019, pp. 16-17] | Numerical model for uniaxial compression after thermal cycling. | Depth: 30mm (top/bottom), 15mm (left/right). |
| PD simulation parameters (E=36 GPa, υ=0.3, G0=50 J/m²) calibrated to match experimental stress-strain curve. | [Yang 2019, pp. 8-10] | Fissured granite (βa=30°), uniaxial compression at room temperature. | Horizon δ=2.4 mm, non-local ratio m=3 adopted. |

## Limitations
1.  The peridynamic model is incapable of simulating the initial non-linear deformation caused by the closure of original microcracks, pores, and voids [Yang 2019, pp. 16-17].
2.  Neither the shuffle algorithm nor Weibull's distribution can simulate the realistic microstructure of the rock material; if sample homogeneity is poor, simulated thermal crack distribution may differ from experiments [Yang 2019, pp. 11-13].
3.  The generation of a non-uniform temperature gradient between the specimen surface and core is inevitable in the simulation, making undesirable thermal shock cracks difficult to control without a "no fail zone" [Yang 2019, pp. 16-17].
4.  The "no fail zone" set during the thermal process has a weak "confining pressure" effect on the thermal damage zone during the subsequent loading process [Yang 2019, pp. 16-17].
5.  Macroscopic frictional-contact behaviors across cracks are not included in the continuous-body PD model [Yang 2019, pp. 4-5].

## Assumptions / Conditions
1.  Material properties (Young's modulus, Poisson's ratio, thermal conductivity, specific heat capacity) are assumed to be temperature-independent [Yang 2019, pp. 11-13].
2.  The emissivity (ε) is assumed to be 1 (ideal heat source) for radiation boundary conditions [Yang 2019, pp. 3-4].
3.  The enhancement of overall strength by the "no fail zone" is neglected [Yang 2019, pp. 16-17].
4.  The heating rate is controlled (e.g., 5°C/s) to generate a more homogeneous thermal field and avoid thermal shock, though this is constrained by the critical thermal time step in simulations [Yang 2019, pp. 16-17].
5.  The thermal cycling treatment process includes infrared radiation heating, constant temperature, and natural cooling stages [Yang 2019, pp. 11-13].

## Key Variables / Parameters
*   **Temperature (T):** Treatment temperatures of 20°C (room temperature), 300°C, and 600°C [Yang 2019, pp. 13-16].
*   **Fissure Inclination Angle (βa):** Varied from 0° to 90° at 15° intervals [Yang 2019, pp. 13-16].
*   **Mineral Contents & Thermal Expansion Coefficients:** Quartz, Muscovite, Labradorite, Hornblende with specific percentages and coefficients [Yang 2019, pp. 10-11, 13-16].
*   **Fracture Energy (G₀):** Calibrated to 50 J/m² [Yang 2019, pp. 8-10].
*   **Young's Modulus (E):** 36 GPa [Yang 2019, pp. 8-10].
*   **Poisson's Ratio (υ):** 0.3 [Yang 2019, pp. 8-10].
*   **Horizon Size (δ):** 2.4 mm [Yang 2019, pp. 8-10].
*   **Non-local Ratio (m):** 3 [Yang 2019, pp. 8-10].
*   **"No Fail Zone" Depth (ΔΘ):** 30 mm (top/bottom), 15 mm (left/right) [Yang 2019, pp. 16-17].

## Reusable Claims
1.  **Condition:** For granite subjected to thermal cycling treatment up to 600°C. **Limitation:** Based on numerical simulation with temperature-independent properties. **Claim:** The ductility of the material increases, and thermal crack evolution continues during the cooling stage, not just the heating stage.
2.  **Condition:** For fissured granite under uniaxial compression after thermal treatment. **Limitation:** Simulated using OSB-PD with a specific heterogeneity model. **Claim:** The crack initiation pattern shifts from tensile wing cracks to anti-tensile wing cracks.
3.  **Condition:** When using the proposed shuffle algorithm to model rock heterogeneity in PD simulations. **Limitation:** Does not capture realistic microstructure. **Claim:** The method effectively reflects mineral compositions and their thermal expansion characteristics, allowing simulation of microcracking from incompatible expansion.
4.  **Condition:** In PD simulations of thermal cycling on rock. **Limitation:** Subject to numerical constraints on heating rate. **Claim:** Implementing a "no fail zone" in boundary layers is an effective method to reduce undesirable thermal shock cracks generated by non-uniform temperature gradients.

## Candidate Concepts
*   [[Peridynamic Theory]]
*   [[Thermal Cycling Treatment]]
*   [[Fracture Mechanics]]
*   [[Rock Heterogeneity]]
*   [[Crack Coalescence]]
*   [[Thermo-Mechanical Coupling]]
*   [[Thermal Shock]]
*   [[Fissured Rock]]

## Candidate Methods
*   [[Fully Coupled Ordinary State-Based Peridynamics (OSB-PD)]]
*   [[Shuffle Algorithm for Heterogeneity]]
*   [[Multi-rate Explicit Time Integration]]
*   [[Adaptive Dynamic Relaxation (ADR)]]
*   [[Critical Energy Density Failure Criterion]]
*   [["No Fail Zone" Implementation]]

## Connections To Other Work
*   Builds upon the fully coupled OSB-PD thermomechanics framework developed by Oterkus et al. [35] and Gao and Oterkus [38] [Yang 2019, pp. 2-3].
*   Extends previous PD studies on rock fracture [25-33] and thermal cracking in rocks [36] by incorporating a more accurate heterogeneity model and full thermal cycling.
*   Compares and validates numerical results against experimental data on the mechanical behavior of fissured granite after high-temperature treatment [2] [Yang 2019, pp. 8-10, 16-17].
*   References various numerical methods for fracture simulation, including XFEM [13], damage particle methods [14], and phase-field models [17,18], highlighting the advantages of PD for handling discontinuities without external criteria [Yang 2019, pp. 1-2].
*   Discusses laboratory thermal treatment methods (convection vs. radiation) and their corresponding boundary conditions in the PD framework [Yang 2019, pp. 3-4].

## Open Questions
1.  How can the PD model be improved to simulate the initial non-linear deformation caused by the closure of pre-existing microcracks and pores?
2.  Can reconstruction techniques like X-ray computed tomography be integrated with PD to create models with realistic rock microstructures for more accurate thermal crack pattern predictions?
3.  What are the optimal parameters for the "no fail zone" (depth, application timing) to minimize its confining pressure effect while effectively eliminating thermal shock cracks?
4.  How do different cooling methods (e.g., rapid quenching vs. natural cooling) after heating affect the thermal cracking behavior and subsequent mechanical properties in the PD simulation framework?
5.  How does the model perform for 3D specimens or more complex fissure networks?

## Source Coverage
All 17 non-empty indexed fragments were processed. The compiled source blocks total 17, covering 82,378 characters from the original 82,056 indexed characters, achieving a coverage ratio of 1.003924 by characters and 1.0 by blocks. The source signature is `f710c661cf7ef142e168fabe87bb1bb69f717096`.
