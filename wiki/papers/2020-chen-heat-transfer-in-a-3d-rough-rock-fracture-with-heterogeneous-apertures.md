---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-chen-heat-transfer-in-a-3d-rough-rock-fracture-with-heterogeneous-apertures"
title: "Heat Transfer in a 3D Rough Rock Fracture with Heterogeneous Apertures."
status: "draft"
source_pdf: "data/papers/Heat transfer in a 3D rough rock fracture with heterogeneous apertures.pdf"
collections:
citation: "Chen, Yuedu, and Zhihong Zhao. \"Heat Transfer in a 3D Rough Rock Fracture with Heterogeneous Apertures.\" *International Journal of Rock Mechanics & Mining Sciences*, vol. 134, 2020, p. 104445. doi:10.1016/j.ijrmms.2020.104445. Accessed 2026."
indexed_texts: "13"
indexed_chars: "64275"
nonempty_source_blocks: "13"
compiled_source_blocks: "13"
compiled_source_chars: "60011"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.93366"
coverage_status: "full-index"
source_signature: "7e89db3bfc40ddc2767bfcc2814f0cb963f68846"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T00:53:23"
---

# Heat Transfer in a 3D Rough Rock Fracture with Heterogeneous Apertures.

## One-line Summary
This study uses 3D numerical simulations to investigate how stress-induced changes in fracture geometry affect fluid flow and convective heat transfer in rough rock fractures, finding that heterogeneous apertures significantly alter flow patterns and heat transfer efficiency compared to idealized models.

## Research Question
How do stress-induced alterations in the geometry (void spaces and contact areas) of a 3D rough rock fracture affect the coupled fluid flow and convective heat transfer processes, and how do these behaviors compare to those in idealized parallel plate and hypothetical rough fractures? [Chen 2020, pp. 1-2]

## Study Area / Data
The study uses a cubic granite sample with a side length of 50 mm containing a single rough fracture artificially produced via a Brazilian tensile test. The upper and lower fracture surfaces were measured using a 3D blue light scanner. The sample was subjected to normal compressive stresses of 0, 0.5, 1, 4, 8, and 16 MPa, and the resulting fracture displacements were measured. A subset of the fracture (x = [20, 30] mm, y = [15, 35] mm) was used for 3D modeling to reduce computational cost. [Chen 2020, pp. 6-7]

## Methods
- **Numerical Modeling:** Steady-state coupled fluid flow and heat transfer simulations were performed using the finite element code COMSOL™. [Chen 2020, pp. 4-6]
- **Governing Equations:** Fluid flow was modeled using the Navier-Stokes and continuity equations for incompressible flow. Heat transport in the rock matrix was governed by conduction, and in the fluid by convection and conduction, assuming local thermal equilibrium at the fluid-rock interface. [Chen 2020, pp. 4-6]
- **Fracture Models:** Three types of 3D fracture models were constructed for each stress level: (1) an **artificial fracture** based on scanned surfaces, (2) a **hypothetical rough fracture** with uniform aperture equal to the initial mechanical aperture of the artificial fracture, and (3) a **parallel plate fracture** with the same mean aperture. [Chen 2020, pp. 6-7]
- **Simulation Setup:** At each stress level, simulations were run for three injection velocities (0.03, 0.15, 0.5 m/s). Boundary conditions included constant velocity inlet, atmospheric pressure outlet, no-slip and impervious fracture walls, constant temperature (393.15 K) on upper/lower boundaries, and adiabatic lateral boundaries. [Chen 2020, pp. 7-9]
- **Heat Transfer Coefficient Calculation:** The overall heat transfer coefficient (h) was calculated from the heat absorbed by the fluid and the average temperature difference between the solid surface and the fluid. [Chen 2020, pp. 4-6]
- **Empirical Model Development:** A power-law relationship was proposed to describe the normalized heat transfer coefficient as a function of normalized hydraulic aperture. [Chen 2020, pp. 10-11]

## Key Findings
1.  **Flow and Temperature Heterogeneity:** In the artificial fracture, streamlines and temperature distributions become increasingly heterogeneous with higher normal stress due to complex flow paths created by varying aperture and contact areas. The hypothetical and parallel plate models cannot capture this complexity. [Chen 2020, pp. 7-9]
2.  **Effect of Hydraulic Aperture:** The heat transfer coefficient decreases non-linearly with increasing hydraulic aperture for all three fracture types. [Chen 2020, pp. 9-10]
3.  **Comparison of Fracture Types:** For a given hydraulic aperture, the heat transfer coefficient is largest in the hypothetical fracture and smallest in the artificial fracture at low apertures. This is because surface roughness enhances heat transfer, but the channeling flow in the artificial fracture (due to contact areas) weakens it. [Chen 2020, pp. 9-10]
4.  **Empirical Model:** A power-law model (h/h_ref = βξ^(-n)) was developed to relate the normalized heat transfer coefficient (h/h_ref) to the normalized hydraulic aperture (ξ = e_h/e_0). Parameters β and n account for the effects of surface roughness and contact area/channeling, respectively. The model was validated against published experimental data. [Chen 2020, pp. 10-11, 13-14]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Streamlines and temperature distributions in artificial fractures become more heterogeneous with increasing normal stress (0-16 MPa). | [Chen 2020, pp. 7-9] | Injection velocity 0.03 m/s. | Due to increasing complexity of flow paths from aperture and contact area changes. |
| Heat transfer coefficient decreases non-linearly with increasing hydraulic aperture for all fracture types. | [Chen 2020, pp. 9-10] | Injection velocities 0.03, 0.15, 0.5 m/s. | Consistent with findings that smaller apertures lead to higher heat flux. |
| For similar hydraulic apertures, the heat transfer coefficient is highest in the hypothetical fracture and lowest in the artificial fracture at low apertures. | [Chen 2020, pp. 9-10] | Low hydraulic apertures. | Attributed to surface roughness enhancing transfer vs. channeling flow in artificial fracture reducing it. |
| The empirical model h/h_ref = βξ^(-n) fits simulation data for all three fracture types. | [Chen 2020, pp. 10-11] | All simulated stress and velocity conditions. | β quantifies roughness effect, n quantifies contact area/channeling effect. |
| The empirical model was validated using published heated flow-through experimental data. | [Chen 2020, pp. 11, 13-14] | Data from Jiang et al. (2020), collected from Bai et al. (2017), Zhao and Tso (1993), and Ma et al. (2019). | Model I from Zhao (2014) was used to back-calculate fluid temperatures. |

## Limitations
- The study focuses on **steady-state** fluid flow and heat transport; transient processes were not considered. [Chen 2020, pp. 11]
- Fracture aperture evolution under stress was simplified by removing surface overlaps ("bed of nails" model), not by solving the full elastic deformation problem. [Chen 2020, pp. 11]
- The coupling is **one-way** (stress affects aperture, which affects flow and heat); effects of fluid pressure and temperature on fracture displacement were not considered. [Chen 2020, pp. 11]
- **Turbulent flow** was not considered due to the focus on laminar flow conditions typical in deep subsurface fractures. [Chen 2020, pp. 11]
- The study uses a **lab-scale** fracture; upscaling the heat transfer coefficient to field-scale models requires further investigation. [Chen 2020, pp. 11]

## Assumptions / Conditions
- The rock matrix is **impervious** due to extremely low porosity. [Chen 2020, pp. 4-6]
- **Local thermal equilibrium** exists between the fluid and the fracture surface at local points. [Chen 2020, pp. 4-6]
- Fluid flow is **steady, incompressible, and laminar**. [Chen 2020, pp. 4-6]
- Fracture closure is caused only by **elastic deformation of surface asperities**. [Chen 2020, pp. 6-7]
- The **hydraulic aperture** (e_h) is used as the key parameter for comparing heat transfer coefficients across different fracture geometries. [Chen 2020, pp. 9-10]

## Key Variables / Parameters
- **Heat transfer coefficient (h):** Overall coefficient describing convective heat transfer from the fracture wall to the fluid. [Chen 2020, pp. 1-2]
- **Hydraulic aperture (e_h):** Aperture of a smooth parallel plate fracture that would have the same flow conductance as the rough fracture. [Chen 2020, pp. 9-10]
- **Normal stress (σ_n):** Compressive stress applied perpendicular to the fracture plane (0-16 MPa). [Chen 2020, pp. 6-7]
- **Injection velocity (v):** Velocity of fluid injected at the fracture inlet (0.03, 0.15, 0.5 m/s). [Chen 2020, pp. 7-9]
- **Normalized hydraulic aperture (ξ):** ξ = e_h / e_0, where e_0 is the initial hydraulic aperture. [Chen 2020, pp. 10-11]
- **Empirical parameters β and n:** Fitting parameters in the power-law model for heat transfer coefficient. β relates to surface roughness, n relates to contact area/channeling effects. [Chen 2020, pp. 10-11]

## Reusable Claims
- **Claim:** The heat transfer coefficient in a rough rock fracture decreases non-linearly with increasing hydraulic aperture. **Condition:** For the range of apertures and flow velocities studied (e_h up to ~0.35 mm, v = 0.03-0.5 m/s). **Limitation:** Derived from simulations of a specific granite fracture under specific stress conditions. [Chen 2020, pp. 9-10]
- **Claim:** Surface roughness generally enhances the heat transfer coefficient compared to a smooth parallel plate fracture of the same hydraulic aperture. **Condition:** For fractures without significant contact areas (e.g., the hypothetical fracture model). **Limitation:** The effect can be reversed in fractures with many contact areas where channeling flow dominates. [Chen 2020, pp. 10-11]
- **Claim:** The presence of asperity contacts in a rough fracture can reduce the heat transfer coefficient below that of a parallel plate fracture due to the formation of channeling flow paths. **Condition:** Particularly evident at lower hydraulic apertures where contact areas are more prevalent. **Limitation:** The threshold aperture where this effect becomes significant depends on the specific fracture geometry and flow velocity. [Chen 2020, pp. 9-10, 11]
- **Claim:** The relationship between normalized heat transfer coefficient and normalized hydraulic aperture can be described by a power-law function: h/h_ref = βξ^(-n). **Condition:** Validated for the simulated fracture types and published experimental data. **Limitation:** Parameters β and n are empirical and may vary for different rock types or fracture generation methods. [Chen 2020, pp. 10-11, 13-14]

## Candidate Concepts
- [[Rough rock fracture]]
- [[Heterogeneous aperture]]
- [[Convective heat transfer]]
- [[Heat transfer coefficient]]
- [[Hydraulic aperture]]
- [[Channeling flow]]
- [[Local thermal equilibrium]]
- [[Geothermal reservoir]]
- [[Fracture network modeling]]
- [[Brazilian tensile test]]

## Candidate Methods
- [[3D numerical simulation]]
- [[Finite element method (COMSOL)]]
- [[Navier-Stokes equations]]
- [[Coupled flow-heat transfer modeling]]
- [[Blue light scanning]]
- [[Empirical model fitting]]
- [[Heated flow-through experiment]]

## Connections To Other Work
- The study builds on the **heated flow-through experiment** pioneered by Zhao (1987) and references numerous subsequent experimental studies on heat transfer in rock fractures (e.g., Bai et al. 2017, Ma et al. 2019, Zhang et al. 2017). [Chen 2020, pp. 1-2, 13-14]
- It addresses limitations of **2D models** and **idealized parallel plate models** used in previous numerical studies of heat transfer in fractured media. [Chen 2020, pp. 3-4]
- The empirical model is **validated against published experimental data** collected by Jiang et al. (2020). [Chen 2020, pp. 11, 13-14]
- The work is relevant to **discrete fracture network (DFN) modeling** for geothermal reservoirs, providing a more realistic heat transfer model than smooth parallel plate assumptions. [Chen 2020, pp. 1-2]

## Open Questions
- How do **transient** fluid flow and heat transport processes behave in 3D rough fractures with heterogeneous apertures? [Chen 2020, pp. 11]
- How does **full elastic deformation** of asperities (rather than the simplified "bed of nails" model) affect the evolution of aperture fields and subsequent heat transfer? [Chen 2020, pp. 11]
- How can the lab-scale heat transfer coefficient be **upscaled** to field-scale discrete fracture network models? [Chen 2020, pp. 11]
- How does **turbulent flow**, which may occur at high flow rates in rough fractures, influence the heat transfer characteristics? [Chen 2020, pp. 11]

## Source Coverage
All 13 non-empty indexed fragments were processed. The compiled source blocks total 13, with a compiled character count of 60,011 out of a total indexed character count of 64,275, resulting in a coverage ratio by characters of 0.93366. The coverage status is "full-index".
