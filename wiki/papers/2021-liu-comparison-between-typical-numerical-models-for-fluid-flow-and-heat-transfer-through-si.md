---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-liu-comparison-between-typical-numerical-models-for-fluid-flow-and-heat-transfer-through-si"
title: "Comparison between Typical Numerical Models for Fluid Flow and Heat Transfer through Single Rock Fractures."
status: "draft"
source_pdf: "data/papers/Comparison between typical numerical models for fluid flow and heat transfer through single rock fractures.pdf"
collections:
citation: "Liu, Guihong, et al. \"Comparison between Typical Numerical Models for Fluid Flow and Heat Transfer through Single Rock Fractures.\" *Computers and Geotechnics*, vol. 138, 2021, p. 104341. doi:10.1016/j.compgeo.2021.104341."
indexed_texts: "11"
indexed_chars: "50400"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "45696"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.906667"
coverage_status: "full-index"
source_signature: "9f3d36c4d68b31182b0be5337cb56a0cf551e54f"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:34:17"
---

# Comparison between Typical Numerical Models for Fluid Flow and Heat Transfer through Single Rock Fractures.

## One-line Summary
This study compares 3D, quasi-3D (Q3D), and 2D numerical models for simulating fluid flow and heat transfer in single rock fractures, finding that 2D models cannot capture channeling flow in artificial fractures and proposing an empirical function to correct their heat transfer coefficient estimates.

## Research Question
The main aims are to systematically investigate the differences between 3D and 2D numerical models for rock fractures in terms of fluid flow and heat transfer behaviors and properties, and to correct possible errors in the calculated properties using 2D models with respect to 3D models [Liu 2021, pp. 1-2].

## Study Area / Data
The numerical models were built using scanned point clouds of a single Brazilian tensile fracture in granite collected from outcrops in Gonghe basin, Qinghai, China [Liu 2021, pp. 2-2]. Two fracture types were studied: artificial fractures with two real fracture surfaces, and hypothetical fractures created by duplicating the upper surface downwards by a vertical displacement of 50 μm [Liu 2021, pp. 2-2]. The model sizes were 20 mm in length, 10 mm in width, and 10 mm in height [Liu 2021, pp. 2-2].

## Methods
Numerical models (3D, Q3D, 2D) were constructed using COMSOL™ [Liu 2021, pp. 2-2]. The 3D models used tetrahedral elements with over 30,000,000 elements, and the 2D models used about 40,000 triangle elements [Liu 2021, pp. 2-2]. Governing equations for fluid flow (conservation of mass and momentum) and heat transfer (conservation of energy in fluid and rock matrix) were solved [Liu 2021, pp. 2-3]. Fluid properties (density, viscosity, specific heat, thermal conductivity) were temperature-dependent [Liu 2021, pp. 2-3]. Steady fluid flow and transient heat transfer simulations were performed for flow rates of 0.2–3 ml/min [Liu 2021, pp. 3-5]. The equivalent hydraulic aperture was calculated using the cubic law from the linear portion of the pressure gradient vs. flow rate curve [Liu 2021, pp. 3-5]. The heat transfer coefficient was calculated using a defined formula [Liu 2021, pp. 3-5].

## Key Findings
1.  Channeling flow is the most significant difference between artificial and hypothetical fractures; 2D models cannot capture this or the resulting non-uniform thermal fronts in artificial fractures [Liu 2021, pp. 5-7, 13-16].
2.  The equivalent hydraulic aperture of the 3D artificial fracture (27.5 μm) is much lower than that of the hypothetical fracture (42.8 μm) due to channeling flow [Liu 2021, pp. 5-7]. Using 2D models for artificial fractures leads to potential biases of 45–82% in hydraulic aperture [Liu 2021, pp. 5-7].
3.  The relationship between heat transfer coefficient (h) and flow rate (q) in a single rock fracture can be described by a logarithmic function: h = a ln(q) + b [Liu 2021, pp. 5-7].
4.  The heat transfer coefficients from 2D and 3D models can be correlated by an empirical function involving the ratio of their heat transfer surface areas (A_f) and a correction factor (α): h_3D = (1 + α) * (A_f2D / A_f3D) * h_2D [Liu 2021, pp. 12-13].
5.  With increasing numbers of computational elements, Q3D model results (channeling flow, thermal fronts) become more similar to 3D model results, but differences in pressure gradients and heat transfer coefficients persist [Liu 2021, pp. 7-12, 13-16].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Channeling flow dominates in artificial fractures but not in hypothetical fractures. | [Liu 2021, pp. 5-7] | Low, medium, and high flow rates (0.2, 1.5, 3.0 ml/min). | Streamlines are non-uniform and discontinuous in cross-sections of 3D artificial fracture models. |
| 2D models cannot capture discontinuous thermal fronts in cross-sections of 3D artificial fracture models. | [Liu 2021, pp. 5-7] | Transient heat transfer simulations. | 2D models give similar thermal fronts as 3D models for hypothetical fractures. |
| Equivalent hydraulic aperture (e_h) for 3D artificial fracture is 27.5 μm; for hypothetical fracture is 42.8 μm. | [Liu 2021, pp. 5-7] | Calculated from linear portion of ∇p vs. q curve using cubic law. | Both fractures have a mechanical aperture of 50 μm. |
| Mean e_h from 2D models of artificial fracture is 5–15 μm, with a bias of 45–82% vs. 3D model. | [Liu 2021, pp. 5-7] | 9 cross-sections per fracture type. | Bias is only ~4% for hypothetical fractures. |
| Heat transfer coefficient (h) increases with flow rate (q) and follows h = a ln(q) + b with R² ≥ 0.98. | [Liu 2021, pp. 5-7] | Flow rates 0.2–3 ml/min. | Relationship holds for 2D, 3D, and Q3D models. |
| Empirical correction: h_3D = (1 + α) * (A_f2D / A_f3D) * h_2D. | [Liu 2021, pp. 12-13] | Artificial fracture: α = -4.4%; Hypothetical fracture: α = +0.6%. | Allows estimation of 3D heat transfer coefficients from 2D model results. |
| Q3D models with finer meshes better approximate 3D model results for flow and heat transfer. | [Liu 2021, pp. 7-12] | Q3D models with 496 to 11,654 computational elements. | Differences remain due to neglecting vertical tortuosity. |

## Limitations
1.  The study only considered an artificial fracture created by Brazilian tension and a hypothetical fracture; effects of surface weathering or infilling materials were not considered [Liu 2021, pp. 12-13].
2.  Model sizes were a few centimeters, so upscaling findings to meter-scale real fractures is an important future issue [Liu 2021, pp. 12-13].
3.  In-situ stresses and fully coupled thermal-hydraulic-mechanical processes were not considered [Liu 2021, pp. 12-13].

## Assumptions / Conditions
1.  The rock matrix is assumed to be impermeable [Liu 2021, pp. 2-3].
2.  Rock properties (density: 2700 kg/m³, specific heat: 920 J/(kg·K), conductivity: 1.8 W/(m·K)) are constant during simulation [Liu 2021, pp. 2-3].
3.  Fracture apertures below 10 μm are approximately considered as contact areas in 3D models [Liu 2021, pp. 2-2].
4.  Boundary conditions: constant flow rate at inlet, atmospheric pressure at outlet, no-flow/no-slip on fracture surfaces, impermeable lateral surfaces for flow; constant temperature (100°C) on top/bottom, adiabatic lateral surfaces, injected fluid at 25°C for heat transfer [Liu 2021, pp. 2-3].

## Key Variables / Parameters
-   Flow rate (q)
-   Pressure gradient (∇p)
-   Equivalent hydraulic aperture (e_h)
-   Heat transfer coefficient (h)
-   Heat transfer surface area (A_f)
-   Non-Darcy coefficient (β)
-   Fluid density (ρ_f), viscosity (μ), specific heat (C_p,f), thermal conductivity (k_f)
-   Rock density (ρ_r), specific heat (C_p,r), thermal conductivity (k_r)
-   Temperature (T_f, T_r)

## Reusable Claims
1.  **Condition:** For fluid flow and heat transfer in a single rock fracture with a mechanical aperture of 50 μm. **Limitation:** Based on a specific granite fracture from Gonghe basin. **Claim:** The equivalent hydraulic aperture of an artificial (Brazilian tension) fracture is significantly lower than that of a hypothetical (duplicated surface) fracture due to channeling flow [Liu 2021, pp. 5-7].
2.  **Condition:** For single rock fractures under flow rates of 0.2–3 ml/min. **Limitation:** Empirical fit from numerical models. **Claim:** The relationship between the heat transfer coefficient (h) and flow rate (q) can be described by a logarithmic function: h = a ln(q) + b [Liu 2021, pp. 5-7].
3.  **Condition:** When using 2D numerical models to estimate heat transfer in rock fractures. **Limitation:** Correction factor α depends on fracture type (artificial vs. hypothetical). **Claim:** The heat transfer coefficient from a 3D model (h_3D) can be estimated from a 2D model (h_2D) using the empirical function h_3D = (1 + α) * (A_f2D / A_f3D) * h_2D [Liu 2021, pp. 12-13].

## Candidate Concepts
-   [[Single rock fracture]]
-   [[Fluid flow]]
-   [[Heat transfer]]
-   [[Numerical modeling]]
-   [[Channeling flow]]
-   [[Equivalent hydraulic aperture]]
-   [[Heat transfer coefficient]]
-   [[Artificial fracture]]
-   [[Hypothetical fracture]]
-   [[Forchheimer's law]]
-   [[Non-Darcy flow]]

## Candidate Methods
-   [[Finite element method]]
-   [[Finite volume method]]
-   [[Lattice Boltzmann method]]
-   [[3D numerical modeling]]
-   [[Quasi-3D (Q3D) modeling]]
-   [[2D numerical modeling]]
-   [[Brazilian tension test]]
-   [[Coupled thermal-hydraulic (TH) modeling]]

## Connections To Other Work
The paper references numerous studies on fluid flow and heat transfer in rock fractures, including experimental work using Brazilian tension [e.g., Bai et al. 2017; Luo et al. 2017] and synthetic fractures [Pastore et al. 2017], as well as numerical studies using 3D [e.g., Chen and Zhao 2020; Zhang et al. 2017], Q3D [e.g., Pandey et al. 2015; Guo et al. 2016], and 2D models [e.g., He et al. 2016; Bai et al. 2016]. It also cites work on nonlinear flow in fractures [e.g., Chen et al. 2015; Zhou et al. 2015] and heat transfer coefficients [Zhao 2014].

## Open Questions
1.  How can the findings be upscaled from centimeter-scale models to meter-scale real rock fractures in subsurface projects? [Liu 2021, pp. 12-13]
2.  How do in-situ stresses and fully coupled thermal-hydraulic-mechanical processes affect the comparison between model types? [Liu 2021, pp. 12-13]

## Source Coverage
All non-empty indexed fragments were processed. The compilation used 11 source blocks containing 45,696 characters, achieving a coverage ratio of 1.0 by blocks and 0.906667 by characters. The source signature is `9f3d36c4d68b31182b0be5337cb56a0cf551e54f`.
