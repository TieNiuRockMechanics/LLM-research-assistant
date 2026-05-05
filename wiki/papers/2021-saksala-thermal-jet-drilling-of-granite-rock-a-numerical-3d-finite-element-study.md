---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-saksala-thermal-jet-drilling-of-granite-rock-a-numerical-3d-finite-element-study"
title: "Thermal Jet Drilling of Granite Rock: A Numerical 3D Finite-Element Study."
status: "draft"
source_pdf: "data/papers/花岗岩岩石的热喷射钻孔 三维有限元数值研究 Thermal jet drilling of granite rock a numerical 3D finite-element study.pdf"
collections:
citation: "Saksala, Timo, et al. \"Thermal Jet Drilling of Granite Rock: A Numerical 3D Finite-Element Study.\" *Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences*, vol. 379, 2021, 20200128, doi:10.1098/rsta.2020.0128."
indexed_texts: "13"
indexed_chars: "60739"
nonempty_source_blocks: "13"
compiled_source_blocks: "13"
compiled_source_chars: "61023"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004676"
coverage_status: "full-index"
source_signature: "cd20d1dcef8356260500ce95d7e537dc12433161"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T11:32:50"
---

# Thermal Jet Drilling of Granite Rock: A Numerical 3D Finite-Element Study.

## One-line Summary
This paper presents a validated 3D finite-element model using a damage-viscoplasticity material law to simulate thermal jet drilling of granite via thermal spallation, demonstrating that heating-forced cooling cycles are a viable method for drilling in hot rock mass.

## Research Question
How can a three-dimensional numerical model be developed to simulate the thermal spallation process in granite during thermal jet drilling, and what are the effects of process parameters and rock heterogeneity on drilling efficiency? [Saksala 2021, pp. 1-2]

## Study Area / Data
The numerical study focuses on Balmoral granite. Material properties for constituent minerals (quartz, feldspars, biotite) are sourced from literature [Saksala 2021, pp. 5-5]. The model is validated against experimental data from dynamic Brazilian disc tests on intact and plasma jet-treated Balmoral granite samples [Saksala 2021, pp. 6-8].

## Methods
A coupled thermo-mechanical problem is solved using the finite element method with an explicit time-stepping scheme [Saksala 2021, pp. 3-5]. Rock is modeled as a viscoplastic damaging material using a modified Drucker-Prager criterion with a Rankine tensile cut-off [Saksala 2021, pp. 2-3]. Rock heterogeneity is represented by random clusters of finite elements assigned properties of different minerals [Saksala 2021, pp. 5-5]. Extreme mass scaling (up to 10,000-fold density) is applied to the mechanical part to allow for computationally feasible time steps [Saksala 2021, pp. 9-10].

## Key Findings
The numerical model successfully predicts the thermal shock weakening effect on the dynamic tensile strength of granite, validating the approach [Saksala 2021, pp. 9-10]. Heterogeneity significantly facilitates the thermal spallation process [Saksala 2021, pp. 10-12]. A simulation with a 3 MW m⁻² thermal flux for 0.1 s predicts a theoretical rate of penetration of approximately 300 mm min⁻¹ [Saksala 2021, pp. 12-13]. Heating-forced cooling cycles are shown to be a viable and economical drilling method when the rock mass is initially hot [Saksala 2021, pp. 13-15].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Model predicts dynamic indirect tensile strength of intact Balmoral granite as 30 MPa, within experimental bounds of 29 ± 3 MPa. | [Saksala 2021, pp. 9-10] | Dynamic Brazilian disc test simulation. | Validates the mechanical part of the model. |
| Model predicts a 20% weakening (to 25.6 MPa) in dynamic tensile strength after plasma jet treatment, consistent with experimental upper limit of 26 MPa. | [Saksala 2021, pp. 9-10] | Plasma jet treatment at 1.25 MW m⁻² followed by dynamic BD test. | Indirect validation of the thermal-mechanical coupling. |
| Heterogeneous rock simulation shows tensile damage exceeding 0.9 in a volume of 167.5 mm³ after one heating pulse. | [Saksala 2021, pp. 10-12] | 3 MW m⁻² flux for 0.1 s, heterogeneous material. | Basis for rate of penetration estimate. |
| A second heating pulse on pre-damaged rock increases the volume of highly damaged elements to 310.7 mm³. | [Saksala 2021, pp. 12-13] | Sequential heating pulses, heterogeneous material. | Demonstrates cumulative damage effect. |
| Heating (2 MW m⁻²) followed by forced water cooling on rock at 200°C initial temperature induces significant tensile damage. | [Saksala 2021, pp. 13-15] | Heating-cooling cycle, hot rock mass. | Shows viability of method for hot rock drilling. |

## Limitations
The continuum damage approach may not perfectly capture discrete macrocrack formation seen in high-rate mechanical loading [Saksala 2021, pp. 9-10]. The model assumes small deformations [Saksala 2021, pp. 3-5]. The explicit time integration scheme is conditionally stable, requiring mass scaling which alters the dynamic response [Saksala 2021, pp. 3-5, 9-10]. The linear temperature dependence of most mechanical properties is an approximation [Saksala 2021, pp. 5-6].

## Assumptions / Conditions
- Small deformation theory is applied [Saksala 2021, pp. 3-5].
- Convection at rock boundaries is ignored due to short heating times (<1 s) [Saksala 2021, pp. 3-5].
- Mechanical heat production (dissipation) is negligible compared to external flux [Saksala 2021, pp. 3-5].
- Young's modulus, tensile/compressive strengths, and thermal conductivity are linearly dependent on temperature up to 600°C [Saksala 2021, pp. 5-6].
- Specific heat capacity is assumed constant [Saksala 2021, pp. 5-6].
- Only tensile damage affects thermal conductivity [Saksala 2021, pp. 5-6].

## Key Variables / Parameters
- **Thermal flux intensity (qₙ):** Ranged from 1.0 to 3.5 MW m⁻² in simulations [Saksala 2021, pp. 8-9, 10-12].
- **Heating duration:** 0.1 s for thermal drilling simulations [Saksala 2021, pp. 10-12].
- **Mass scaling factor:** 10,000-fold density increase used for mechanical part [Saksala 2021, pp. 9-10].
- **Material properties:** Temperature-dependent Young's modulus, strengths, and conductivity; constant Poisson's ratio, density, specific heat, fracture energies, and viscosity parameters (see Table 1) [Saksala 2021, pp. 5-5].
- **Damage variables:** Tensile (ωₜ) and compressive (ωc) scalar damage variables [Saksala 2021, pp. 2-3].

## Reusable Claims
- Thermal jet drilling exploiting heating-forced cooling cycles is a viable method when drilling in hot rock mass, as sufficient damage can be achieved with lower initial heating [Saksala 2021, pp. 13-15].
- Rock heterogeneity, modeled as random mineral clusters, significantly enhances the thermal spallation process and damage patterns [Saksala 2021, pp. 10-12].
- The explicit finite-element model with extreme mass scaling can reliably simulate the coupled thermo-mechanical problem of thermal spallation for short-duration, high-intensity heating [Saksala 2021, pp. 9-10].
- The predicted rate of penetration for thermal jet drilling in granite, based on 3D simulation, can be on the order of 300 mm min⁻¹ under specific conditions (3 MW m⁻², 0.1 s pulse) [Saksala 2021, pp. 12-13].

## Candidate Concepts
- [[thermal spallation]]
- [[damage-viscoplasticity model]]
- [[finite element method]]
- [[coupled thermo-mechanical problem]]
- [[rock heterogeneity]]
- [[explicit time integration]]
- [[mass scaling]]
- [[dynamic Brazilian disc test]]
- [[heating-cooling cycle drilling]]

## Candidate Methods
- [[explicit time-stepping scheme]]
- [[extreme mass scaling]]
- [[random mineral cluster modeling]]
- [[Drucker-Prager with Rankine cut-off]]
- [[Lagrange multiplier contact]]

## Connections To Other Work
The study builds upon and validates against the experimental work of Mardoukhi et al. (2017) on plasma jet treatment of granite [Saksala 2021, pp. 6-8]. It addresses the limitation of previous axisymmetric numerical studies by providing a full 3D analysis [Saksala 2021, pp. 1-2]. The material model is a modified version of that presented by Saksala (2010) [Saksala 2021, pp. 2-3]. The work is contextualized within other non-mechanical drilling methods like plasma jet, electro-pulse, and microwave drilling [Saksala 2021, pp. 1-2].

## Open Questions
- The resolution of available 3D X-ray tomography was insufficient to detect internal microcracks predicted by the model in treated samples [Saksala 2021, pp. 9-10].
- Further optimization of process parameters (flux intensity, duration, jet movement) for maximum drilling efficiency is implied but not fully explored [Saksala 2021, pp. 1-2].
- The model's applicability to other rock types beyond granite requires investigation.

## Source Coverage
All 13 non-empty indexed fragments were processed. The compiled source blocks total 13, with a compiled character count of 61,023, achieving a coverage ratio of 1.0 by blocks and 1.004676 by characters, confirming full-index coverage.
