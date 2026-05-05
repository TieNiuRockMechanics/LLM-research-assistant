---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2015-tang-numerical-model-for-the-cracking-behaviour-of-heterogeneous-brittle-solids-subjected-t"
title: "Numerical Model for the Cracking Behaviour of Heterogeneous Brittle Solids Subjected to Thermal Shock."
status: "draft"
source_pdf: "data/papers/非均质脆性材料热冲击作用下的裂纹行为的数值模拟-唐世斌.pdf"
collections:
citation: "Tang, S.B., et al. \"Numerical Model for the Cracking Behaviour of Heterogeneous Brittle Solids Subjected to Thermal Shock.\" *International Journal of Solids and Structures*, 2015, doi:10.1016/j.ijsolstr.2015.10.012."
indexed_texts: "14"
indexed_chars: "69379"
nonempty_source_blocks: "14"
compiled_source_blocks: "14"
compiled_source_chars: "67424"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.971821"
coverage_status: "full-index"
source_signature: "7fb0b20c5c183eade899f6a4fa4dfe9f24a15d36"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T11:20:05"
---

# Numerical Model for the Cracking Behaviour of Heterogeneous Brittle Solids Subjected to Thermal Shock.

## One-line Summary
A finite element model incorporating material heterogeneity via Weibull distribution and continuum damage mechanics is developed to simulate the initiation, propagation, and pattern formation of thermal shock-induced cracks in brittle solids.

## Research Question
How does the heterogeneity of brittle materials influence the initiation, propagation, and final pattern of cracks when subjected to rapid thermal shock, and what is the role of thermal conductivity in this process?

## Study Area / Data
The numerical model is applied to simulate thermal shock experiments on 99% Al2O3 ceramics conducted by Jiang et al. (2012). The computational domain for these simulations is a half-specimen (10mm x 25mm) meshed with 100,000 elements [Tang 2015, pp. 19-21]. The model is also discussed in the context of rock engineering applications, such as thermal fracturing during cold fluid injection into reservoirs [Tang 2015, pp. 5-8].

## Methods
The methodology is a coupled thermo-mechanical finite element method (FEM) framework.
*   **Heterogeneity Modeling:** Material heterogeneity at the mesoscopic level is represented by assigning tensile strength and elastic modulus to elements according to a Weibull distribution, controlled by a homogeneity index *m* [Tang 2015, pp. 8-10].
*   **Thermal Analysis:** Transient heat conduction is solved using Fourier's law with the backward difference method (η=1.0) for unconditional stability [Tang 2015, pp. 10-13].
*   **Mechanical Analysis & Damage:** Thermal stresses are calculated from the temperature field. Crack initiation and propagation are modeled using continuum damage mechanics (CDM). Damage occurs when the minimum principal stress in a meso-element exceeds its tensile strength, following a brittle-plastic damage evolution law [Tang 2015, pp. 13-16].
*   **Coupling:** The model accounts for the effect of damage on thermal properties: fully damaged internal elements are treated as insulators (λ≈0), while surface cracks increase local thermal conductivity [Tang 2015, pp. 16-19].

## Key Findings
1.  The model successfully captures the formation of parallel, approximately equally spaced surface cracks in brittle solids under thermal shock, consistent with experimental observations [Tang 2015, pp. 19-21, 27-29].
2.  The number of initiated cracks increases and the spacing between them decreases with higher initial specimen temperature [Tang 2015, pp. 19-21, 27-29].
3.  The initiated cracks can be classified into different hierarchical levels based on their length [Tang 2015, pp. 20-21, 27-29].
4.  The cracking pattern depends on the material's thermal conductivity (λ). Higher λ results in a smaller thermal gradient, fewer initiated surface cracks, and less distinct hierarchical levels in the crack pattern [Tang 2015, pp. 26-28, 29].
5.  Material heterogeneity causes inhomogeneous stress distribution, leading to initially disordered micro-failures that later organize into characteristic patterns due to elastic interactions between crack tips [Tang 2015, pp. 22-24, 25-26].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Crack patterns from numerical simulations match experimental results for Al2O3 ceramics at T0=300-600°C. | [Tang 2015, pp. 19-21] | Quenching of 99% Al2O3 ceramic specimens. | Comparison shown in Fig. 6 of the paper. |
| Total crack numbers from simulations are slightly larger than experimental counts. | [Tang 2015, pp. 19-21] | All tested initial temperatures. | Attributed to difficulty identifying tiny experimental cracks and minor differences in boundary conditions. |
| Crack lengths form three hierarchical levels in both experiments and simulations. | [Tang 2015, pp. 20-21] | All tested initial temperatures. | Numbers of long and middle-length cracks agree well; short crack counts diverge at higher T0. |
| Increasing thermal conductivity (λ) from 31 to 100 Wm⁻¹K⁻¹ reduces the number of surface cracks and obscures hierarchical levels. | [Tang 2015, pp. 26-28] | Initial temperature T0=300°C. | Demonstrates the controlling role of λ on crack pattern. |
| Heterogeneity (m=1.5) induces significant shear stress (~2.5 MPa) even under uniform heating and free expansion. | [Tang 215, pp. 12-13] | Uniform temperature increase from 0°C to 20°C. | Contrasts with zero stress in a homogeneous model, highlighting the importance of heterogeneity. |

## Limitations
*   The numerical model cannot capture every detail of the complex microstructure of real brittle materials, even with Weibull distribution [Tang 2015, pp. 19-21].
*   Boundary conditions in simulations may not perfectly replicate experimental conditions, leading to minor discrepancies (e.g., crack distribution near corners) [Tang 2015, pp. 19-21].
*   Maximum simulated crack lengths are somewhat shorter than experimental observations, possibly due to the blunt crack tip representation in the model [Tang 2015, pp. 20-21].
*   The model assumes isotropic material properties (αx=αy, λx=λy) [Tang 2015, pp. 10-13].
*   Radiation heat transfer through damaged volumes is disregarded [Tang 2015, pp. 16-19].

## Assumptions / Conditions
*   Material heterogeneity is statistically represented by a Weibull distribution for strength and elastic modulus [Tang 2015, pp. 8-10].
*   Damage in meso-elements is isotropic and governed by a maximum tensile stress criterion [Tang 2015, pp. 13-16].
*   The coefficient of thermal expansion (CTE) degrades to zero for damaged elements [Tang 2015, pp. 16-19].
*   For thermal conductivity: fully damaged internal elements are insulators (λ≈0), while surface-damaged elements have enhanced conductivity [Tang 2015, pp. 16-19].
*   Material properties (e.g., E, λ, α) for the ceramic simulations are constant over the temperature range (up to 600°C) [Tang 2015, pp. 19-21].

## Key Variables / Parameters
*   **Homogeneity Index (m):** Weibull shape parameter controlling material heterogeneity. Higher *m* means more homogeneous material [Tang 2015, pp. 8-10].
*   **Thermal Conductivity (λ):** Governs the temperature gradient and significantly influences crack number and pattern [Tang 2015, pp. 26-28].
*   **Initial Temperature (T0):** The starting temperature before quenching. Higher T0 leads to more cracks and narrower spacing [Tang 2015, pp. 19-21].
*   **Tensile Strength (σt):** Assigned to elements via Weibull distribution; threshold for damage initiation [Tang 2015, pp. 8-10, 13-16].
*   **Convective Heat Transfer Coefficient (hc):** Defines the rate of heat exchange with the quenching medium (e.g., water) [Tang 2015, pp. 19-21].
*   **Damage Variable (d):** Ranges from 0 (undamaged) to 1 (fully damaged), reducing element stiffness [Tang 2015, pp. 13-16].

## Reusable Claims
*   In heterogeneous brittle solids under thermal shock, the number of initiated surface cracks increases and their spacing decreases with increasing initial temperature [Tang 2015, pp. 19-21, 27-29].
*   The thermal conductivity of a brittle material is a key determinant of its thermal shock cracking pattern; higher conductivity leads to fewer, less hierarchically organized cracks [Tang 2015, pp. 26-28, 29].
*   Material heterogeneity, even under uniform temperature change and free expansion, can induce significant internal stresses (e.g., shear stress) that drive crack initiation [Tang 2015, pp. 12-13].
*   The evolution of thermal conductivity must be coupled with mechanical damage to accurately model thermal shock cracking, as cracks act as either barriers or conduits for heat flow [Tang 2015, pp. 16-19, 29].

## Candidate Concepts
*   [[Thermal shock]]
*   [[Heterogeneous brittle solids]]
*   [[Continuum damage mechanics]]
*   [[Weibull distribution]]
*   [[Crack pattern formation]]
*   [[Hierarchical cracking]]
*   [[Thermo-mechanical coupling]]
*   [[Finite Element Method]]

## Candidate Methods
*   [[Finite Element Method (FEM)]]
*   [[Weibull statistical distribution]]
*   [[Continuum Damage Mechanics (CDM)]]
*   [[Coupled thermo-mechanical analysis]]
*   [[Meso-scale numerical modeling]]

## Connections To Other Work
*   The model is validated against experimental crack patterns in Al2O3 ceramics from Jiang et al. (2012) [Tang 2015, pp. 19-21].
*   The study references foundational work on thermal shock fracture criteria by Kingery (1955) [Tang 2015, pp. 4-5].
*   It discusses applications in rock engineering, citing work on thermal cracking in reservoirs by Kim and Kemeny (2009) and Izadi and Elsworth (2013) [Tang 2015, pp. 5-8].
*   The damage mechanics approach extends methods proposed by Mazars and Pijaudier-Cabot (1989) for concrete and Cerrolaza and Garcia (1997) for rock [Tang 2015, pp. 15-16].

## Open Questions
*   How would the model perform for 3D geometries or more complex boundary conditions?
*   Can the model be extended to account for anisotropic thermal and mechanical properties?
*   How does the presence of moisture or pore pressure, relevant in rock and some ceramics, interact with the modeled thermal shock cracking?
*   What is the quantitative relationship between the Weibull modulus *m* and the resulting crack spacing or hierarchical levels?

## Source Coverage
All 14 non-empty indexed fragments were processed. The compiled source blocks total 14, covering 67,424 characters out of 69,379 indexed characters, achieving a coverage ratio of 0.971821 by characters. The coverage status is full-index.
