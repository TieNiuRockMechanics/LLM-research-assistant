---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-liu-coupled-thermo-hydro-mechanical-modelling-for-geothermal-doublet-system-with-3d-fractal"
title: "Coupled Thermo-Hydro-Mechanical Modelling for Geothermal Doublet System with 3D Fractal Fracture."
status: "draft"
source_pdf: "data/papers/Coupled thermo-hydro-mechanical modelling for geothermal doublet system with 3D fractal fracture.pdf"
collections:
citation: "Liu, Jia, et al. \"Coupled Thermo-Hydro-Mechanical Modelling for Geothermal Doublet System with 3D Fractal Fracture.\" *Applied Thermal Engineering*, vol. 200, 2022, p. 117716."
indexed_texts: "15"
indexed_chars: "71231"
nonempty_source_blocks: "15"
compiled_source_blocks: "15"
compiled_source_chars: "66942"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.939787"
coverage_status: "full-index"
source_signature: "32103143d849648c9618dd38626843c01972c6cc"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T00:53:02"
---

# Coupled Thermo-Hydro-Mechanical Modelling for Geothermal Doublet System with 3D Fractal Fracture.

## One-line Summary
This study develops a coupled thermo-hydro-mechanical (THM) model to investigate the impact of 3D fractal fracture geometry on thermal breakthrough in a geothermal doublet system, using a thin elastic layer assumption for fracture deformation.

## Research Question
How does the complex geometry of a 3D fractal fracture, acting as a preferential flow path, influence the thermal breakthrough and heat recovery efficiency in a geothermal doublet system under coupled thermo-hydro-mechanical conditions?

## Study Area / Data
The study is a numerical simulation of a geothermal reservoir. The target reservoir volume is 500 × 500 × 500 m³ containing a 3D fractal fracture and two wells (injection and production) [Liu 2022, pp. 7-9]. The model parameters are listed in Table 1 of the paper [Liu 2022, pp. 7-9].

## Methods
A coupled THM model is developed where the fracture is treated as a thin elastic layer within the bedrock [Liu 2022, pp. 1-1]. The 3D fractal fracture surfaces are generated using the multivariate Weierstrass-Mandelbrot function [Liu 2022, pp. 4-6]. The geothermal wells are modeled using a pseudo 3D borehole (1D line element) approach [Liu 2022, pp. 4-6]. The model is implemented in COMSOL Multiphysics, using modules for Darcy's Law, Heat Transfer in Porous Media, and Solid Mechanics, with specific features for fracture flow and thin elastic layers [Liu 2022, pp. 6-6]. The model is validated against analytical solutions for 1D thermo-hydro coupling, radial flow through a rigid fracture, and a THM coupling problem for a deformable fracture [Liu 2022, pp. 6-7].

## Key Findings
1.  The thin elastic layer assumption is robust for modeling fracture opening and closing under coupled THM conditions [Liu 2022, pp. 1-1].
2.  Fracture permeability evolution is heterogeneous and related to the fractal dimension, in-situ stress, and well layout [Liu 2022, pp. 1-1].
3.  Cool water in a fracture with a larger fractal dimension interacts more fully with the bedrock, influencing thermal breakthrough [Liu 2022, pp. 1-1].
4.  Thermal stress causes bedrock shrinkage and fracture opening, while water absorption causes bedrock swelling and fracture compression, significantly affecting permeability [Liu 2022, pp. 14-15].
5.  Higher injection pressure increases fracture opening and flow velocity, accelerating thermal breakthrough [Liu 2022, pp. 10-13].
6.  The joint action of in-situ stress and fracture inclination seriously affects fracture opening and closing [Liu 2022, pp. 14-15].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| The thin elastic layer assumption is remarkably robust for modelling fracture opening and closing under coupling conditions. | [Liu 2022, pp. 1-1] | THM coupling model for geothermal doublet system. | Conclusion from model development and validation. |
| Fracture permeability evolution presents heterogeneity related to fractal dimension, in-situ stress, and geothermal wells layout. | [Liu 2022, pp. 1-1] | Numerical simulations with varying parameters. | Key finding from sensitivity analysis. |
| Cool water in fracture with larger fractal dimension can interact with the bedrock more fully and further affect the thermal breakthrough. | [Liu 2022, pp. 1-1] | Simulations with fractal dimensions from 2.0 to 2.5. | Observed from temperature breakthrough curves and isosurfaces. |
| Thermal stress causes bedrock shrinkage and fracture opening; bedrock swelling due to water absorption compresses the fracture. | [Liu 2022, pp. 14-15] | Analysis of coupled THM processes. | Mechanism explaining permeability changes. |
| Higher injection pressure impels the fracture to open and increases flow velocity, accelerating thermal breakthrough. | [Liu 2022, pp. 10-13] | Sensitivity analysis with injection pressures of 20, 30, and 40 MPa. | Result from parameter study. |
| The influence of in-situ stress on fracture permeability depends on the change of normal and shear stresses on the fracture surface. | [Liu 2022, pp. 13-14] | Simulations with varying in-situ stress magnitudes and directions. | Conclusion from stress sensitivity analysis. |

## Limitations
The research uses a theoretically generated fractal fracture, and for practical geothermal reservoirs, site-specific data should be applied to the modelling [Liu 2022, pp. 14-15]. The study focuses on a single fracture and does not consider chemical reactions [Liu 2022, pp. 14-15].

## Assumptions / Conditions
1.  Local thermal equilibrium is assumed between the fluid and the rock matrix [Liu 2022, pp. 1-2].
2.  The fracture is treated as a thin elastic layer with normal and shear stiffness [Liu 2022, pp. 3-4].
3.  Fluid properties (density, viscosity, thermal conductivity, specific heat capacity) are temperature-dependent [Liu 2022, pp. 4-6].
4.  The initial water pressure in the reservoir is 15 MPa, with injection and production pressures of 30 MPa and 5 MPa, respectively [Liu 2022, pp. 6-6].
5.  The initial temperature of bedrock and water is 100 °C, with an injection temperature of 20 °C [Liu 2022, pp. 6-6].

## Key Variables / Parameters
*   **Fractal Dimension (D):** Ranges from 2.0 (smooth) to 2.5, defining the roughness of the 3D fracture surface [Liu 2022, pp. 4-6].
*   **Elastic Modulus of Thin Elastic Layer (E_f):** Controls the mechanical stiffness of the fracture (e.g., 5, 15, 25 MPa) [Liu 2022, pp. 9-10].
*   **Elastic Modulus of Bedrock (E):** Affects stress sensitivity and bedrock-fracture interaction (e.g., 10, 30, 50 GPa) [Liu 2022, pp. 9-10].
*   **Thermal Expansion Coefficient of Bedrock (α_T):** Determines thermal stress distribution (e.g., 1.0×10⁻⁶, 3.5×10⁻⁶, 6.0×10⁻⁶ 1/K) [Liu 2022, pp. 9-10].
*   **Injection Pressure (p_inj):** Affects effective stress and fracture aperture (e.g., 20, 30, 40 MPa) [Liu 2022, pp. 10-13].
*   **Injection Temperature (T_inj):** Influences thermal stress and heat recovery rate (e.g., 0, 20, 40 °C) [Liu 2022, pp. 10-13].
*   **In-situ Stress (σ_0):** Includes vertical (σ_v) and horizontal (σ_h, σ_H) stresses, affecting fracture deformation [Liu 2022, pp. 6-6].
*   **Fracture Inclination Angle (θ):** The orientation of the fracture plane relative to the wells [Liu 2022, pp. 13-14].

## Reusable Claims
*   **Condition:** For a geothermal doublet system with a single 3D fractal fracture. **Limitation:** Under the assumption of a thin elastic layer for fracture mechanics. **Claim:** A larger fracture fractal dimension increases the interaction area between cool water and bedrock, which can influence the thermal breakthrough time, though the relationship is complex and also depends on the induced heterogeneous permeability evolution [Liu 2022, pp. 1-1, pp. 7-9].
*   **Condition:** When considering coupled THM processes in fractured geothermal reservoirs. **Limitation:** Based on numerical simulations with specific boundary conditions. **Claim:** The evolution of fracture permeability is highly sensitive to the elastic modulus of the fracture (E_f), the elastic modulus of the bedrock (E), and the thermal expansion coefficient of the bedrock (α_T), with lower E_f, lower E, and higher α_T generally leading to more significant permeability changes and earlier thermal breakthrough [Liu 2022, pp. 9-10].
*   **Condition:** For operational parameters of a geothermal doublet. **Limitation:** Within the tested range of injection pressures and temperatures. **Claim:** Increasing injection pressure accelerates thermal breakthrough by opening fractures and increasing flow velocity, while increasing injection temperature can improve heat recovery rate but also enhances fracture permeability [Liu 2022, pp. 10-13].

## Candidate Concepts
*   [[fracture reservoir]]
*   [[thin elastic layer]]
*   [[thermal breakthrough]]
*   [[fractal dimension]]
*   [[preferential flow path]]
*   [[Enhanced Geothermal System (EGS)]]
*   [[thermo-hydro-mechanical coupling]]

## Candidate Methods
*   [[Weierstrass-Mandelbrot function]]
*   [[COMSOL Multiphysics implementation]]
*   [[pseudo 3D borehole model]]
*   [[cubic law for fracture permeability]]
*   [[local thermal equilibrium assumption]]

## Connections To Other Work
The model is validated against the analytical solution of Lauwerier [41] for 1D thermo-hydro coupling [Liu 2022, pp. 6-6]. It is also compared to the numerical results of Guo et al. [9] and Vik et al. [43] for a THM coupling problem with a deformable fracture [Liu 2022, pp. 7-7]. The study builds upon prior work on THM coupling in EGS [9-16, 26-30] and the use of fractal geometry for fracture surfaces [32, 37-39].

## Open Questions
1.  How can site-specific fracture data be integrated into this modelling framework for practical reservoir assessment?
2.  How would the inclusion of chemical reactions (THMC coupling) affect the long-term evolution of fracture aperture and system efficiency?
3.  What are the optimal well locations and orientations for a given in-situ stress field and fracture geometry to maximize heat recovery and delay thermal breakthrough?

## Source Coverage
All 15 non-empty indexed fragments were processed. The compiled source blocks cover 66,942 characters out of a total of 71,231 indexed characters, resulting in a coverage ratio by characters of 0.939787. The coverage status is full-index.
