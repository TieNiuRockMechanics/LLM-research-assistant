---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-chen-modeling-of-flow-characteristics-in-3d-rough-rock-fracture-with-geometry-changes-under"
title: "Modeling of Flow Characteristics in 3D Rough Rock Fracture with Geometry Changes under Confining Stresses."
status: "draft"
source_pdf: "data/papers/Modeling of flow characteristics in 3D rough rock fracture with geometry changes under confining stresses.pdf"
collections:
citation: "Chen, Yuedu, et al. \"Modeling of Flow Characteristics in 3D Rough Rock Fracture with Geometry Changes under Confining Stresses.\" *Computers and Geotechnics*, vol. 130, 2021, 103910. doi:10.1016/j.compgeo.2020.103910. Accessed 2026."
indexed_texts: "16"
indexed_chars: "76761"
nonempty_source_blocks: "16"
compiled_source_blocks: "16"
compiled_source_chars: "71548"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.932088"
coverage_status: "full-index"
source_signature: "f904f32486fa377241154eaadc56d058f01c26bd"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T01:06:31"
---

# Modeling of Flow Characteristics in 3D Rough Rock Fracture with Geometry Changes under Confining Stresses.

## One-line Summary
This study uses 3D models of real rock fractures, whose geometries are measured under increasing confining stress, to simulate fluid flow via the Navier-Stokes equations, revealing how stress-induced changes in voids and contacts increase flow heterogeneity and non-Darcy behavior.

## Research Question
How do the alterations in void spaces and asperity contacts within a 3D rough rock fracture, caused by increasing confining stresses, affect the internal flow characteristics, including streamlines, pressure distribution, and the onset of non-Darcy flow? [Chen 2021, pp. 1-1]

## Study Area / Data
The study uses an artificially tensile fractured sandstone sample cored from the Permian Carboniferous strata in Shanxi Province, China. [Chen 2021, pp. 7-9] A series of fracture geometries were measured during hydraulic tests at increasing confining stresses (0 to 20 MPa) using a servo-controlled tri-axial system. [Chen 2021, pp. 7-9] The 3D fracture apertures and contact areas were determined using a point-cloud matching method and 3D scanner. [Chen 2021, pp. 9-11]

## Methods
- **Fracture Modeling:** 3D real fracture models were built from measured surface geometries at different confining stress levels (2, 4, 6, 8, 10, 12, 16, 20 MPa) using COMSOL Multiphysics. [Chen 2021, pp. 11-12]
- **Flow Simulation:** The steady, incompressible Navier-Stokes equations were solved for each fracture model. [Chen 2021, pp. 3-5] Four injection flow rates (3.33E-8 to 3.33E-5 m³/s) were applied at the inlet, with zero pressure at the outlet and no-slip, impervious conditions on fracture walls. [Chen 2021, pp. 11-12]
- **Simplifications:** To manage computational cost, simulations were performed on a 1/9 scale segment of the full fracture, justified by a scale-independence analysis of transmissivity. [Chen 2021, pp. 11-12] Contact areas were assigned a small aperture (10 μm) to avoid geometric errors. [Chen 2021, pp. 11-12]
- **Validation:** Simulated normalized apparent transmissivity was compared with experimental data from hydraulic tests. [Chen 2021, pp. 12-14]
- **Analysis:** Flow characteristics (velocity, streamlines, pressure) were analyzed. Non-Darcy flow was characterized using the Forchheimer equation and critical Reynolds number (Re_c). [Chen 2021, pp. 5-7]

## Key Findings
1.  Simulated normalized apparent transmissivity matched experimental data well and decreased nonlinearly with increasing confining stress. [Chen 2021, pp. 12-14]
2.  Stress-induced geometry changes increased the heterogeneity of flow characteristics (velocity, streamlines, pressure) in 3D fractures. Streamlines became more channeled and tortuous under high stress. [Chen 2021, pp. 14-17]
3.  The increase in contact area under stress enhanced the non-linearity of pressure drop along the fracture. [Chen 2021, pp. 14-17]
4.  Eddy flows, which cause local pressure fluctuations and non-Darcy behavior, formed around contact regions and in variable apertures. Their range decreased under high confining stress due to reduced aperture and sharp geometries. [Chen 2021, pp. 17-17]
5.  The critical Reynolds number (Re_c) for the onset of non-Darcy flow increased as hydraulic aperture decreased (from 0.165 mm to 0.035 mm), indicating that stress-induced geometry changes delay significant inertial effects. [Chen 2021, pp. 17-18]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Simulated transmissivity matches experimental data and decreases exponentially with confining stress. | [Chen 2021, pp. 12-14] | Injection rates of 3.33E-8 and 3.33E-7 m³/s; confining stress 2-20 MPa. | Validates the use of N-S equations for 3D real fractures under stress. |
| Flow velocity is non-uniform, with high-velocity zones in large apertures dependent on contact distribution. | [Chen 2021, pp. 14-17] | Confining stress 6 MPa; injection rate 3.33E-8 m³/s (Re=2.22). | Contrasts with 2D models; shows 3D spatial dependence. |
| Streamlines become more channeled and tortuous with increasing confining stress. | [Chen 2021, pp. 14-17] | Injection rate 3.33E-8 m³/s (Re=2.22); stress from 2 to 20 MPa. | Contact locations are the main cause of streamline deviation. |
| Water pressure decreases non-linearly along fracture profiles; non-linearity increases with confining stress. | [Chen 2021, pp. 14-17] | Profile X=24; injection rate 3.33E-8 m³/s (Re=2.22); stress 2-20 MPa. | Contact regions bring high resistance, reducing pressure decay. |
| Eddy flow range decreases with increasing confining stress. | [Chen 2021, pp. 17-17] | Same region in fracture; injection rate 3.33E-5 m³/s (Re=2220); stress 2-20 MPa. | Reduced aperture and sharp geometries under high stress weaken eddy formation. |
| Critical Reynolds number (Re_c) increases as hydraulic aperture decreases. | [Chen 2021, pp. 17-18] | Hydraulic aperture range 0.035-0.165 mm. | Delay in significant inertial effects due to geometry changes under stress. |

## Limitations
- The study considers only one-way coupling (stress effect on apertures), not the full hydro-mechanical coupling where fluid pressure affects fracture deformation. [Chen 2021, pp. 18-18]
- Contact areas were assigned a small fixed aperture (10 μm) for computational reasons, which is a simplification. [Chen 2021, pp. 11-12]
- Elastic and plastic deformation between micro-asperities were not considered; aperture changes were based on uniform closure. [Chen 2021, pp. 18-18]
- Simulations were performed on a 1/9 scale segment of the fracture, not the entire sample. [Chen 2021, pp. 11-12]

## Assumptions / Conditions
- Fracture closure is accommodated only by compression of contacting asperities, conforming to the "bed of nails" model. [Chen 2021, pp. 9-11]
- Measured fracture closure is distributed uniformly over the whole fracture surface. [Chen 2021, pp. 9-11]
- Overlapping asperities are assumed to be contacting asperities; surface deformation is not considered. [Chen 2021, pp. 9-11]
- Fluid flow is steady, incompressible, isothermal, and single-phase Newtonian. [Chen 2021, pp. 3-5]
- The fracture geometry is static during flow simulation (no hydro-mechanical coupling). [Chen 2021, pp. 11-12]

## Key Variables / Parameters
- **Confining Stress (σ):** Applied radially, ranging from 0 to 20 MPa. [Chen 2021, pp. 7-9]
- **Injection Flow Rate (Q):** Ranges from 3.33E-8 to 3.33E-5 m³/s. [Chen 2021, pp. 11-12]
- **Reynolds Number (Re):** Defined as Re = ρQ/(μw), ranging from 2.22 to 2220. [Chen 2021, pp. 5-7]
- **Fracture Aperture (E):** Spatially varying void space; contact defined as <10 μm. [Chen 2021, pp. 9-11]
- **Apparent Transmissivity (T_a):** Describes permeability considering inertial effects; T_a = k₀/(1+F₀). [Chen 2021, pp. 5-7]
- **Critical Reynolds Number (Re_c):** Reynolds number at the onset of non-Darcy flow (using critical E=0.1). [Chen 2021, pp. 17-18]
- **Forchheimer Coefficients (A, B):** Linear and non-linear coefficients in the Forchheimer equation. [Chen 2021, pp. 5-7]

## Reusable Claims
- **Claim:** The normalized apparent transmissivity of a 3D rough rock fracture decreases nonlinearly with increasing confining stress, and this relationship can be accurately captured by Navier-Stokes simulations using stress-altered geometries.
    - **Condition:** For the tested sandstone with artificially induced tensile fracture under radially applied confining stress up to 20 MPa.
    - **Limitation:** Based on a one-way coupled mechanical-hydraulic analysis; does not account for pore pressure effects on fracture stiffness.
- **Claim:** Increasing confining stress enhances the heterogeneity of flow characteristics (velocity, streamlines, pressure) in 3D rough fractures by altering the spatial distribution of contacts and voids.
    - **Condition:** Observed in simulations of a real fracture geometry under increasing stress.
    - **Limitation:** The study used a simplified uniform closure model for aperture change.
- **Claim:** The critical Reynolds number for the onset of non-Darcy flow in a rough fracture increases as the hydraulic aperture decreases under confining stress, due to the reduction in sharp geometries and eddy flow range.
    - **Condition:** For hydraulic apertures between 0.035 mm and 0.165 mm.
    - **Limitation:** The relationship may reverse at very small apertures where increased tortuosity from contacts dominates.

## Candidate Concepts
- [[rough fracture]]
- [[non-Darcy flow]]
- [[confining stress]]
- [[fracture aperture]]
- [[asperity contact]]
- [[eddy flow]]
- [[critical Reynolds number]]
- [[Forchheimer equation]]
- [[apparent transmissivity]]
- [[channeling flow]]
- [[tortuosity]]

## Candidate Methods
- [[Navier-Stokes equations]]
- [[point-cloud matching method]]
- [[COMSOL Multiphysics]]
- [[hydraulic flow test]]
- [[Brazilian tensile test]]
- [[Forchheimer equation fitting]]
- [[scale independence analysis]]

## Connections To Other Work
- The study builds on prior work that used 2D models or hypothetical 3D fractures, addressing the gap in modeling flow in 3D real fractures under stress. [Chen 2021, pp. 1-3]
- It validates the use of full Navier-Stokes equations over simplified Reynolds equation for complex geometries and inertial effects. [Chen 2021, pp. 1-3]
- Findings on eddy flow and non-Darcy behavior align with numerical and experimental studies by Zhang et al. (2013), Lee et al. (2014, 2015), and Zou et al. (2017a). [Chen 2021, pp. 17-17]
- The work references and extends the understanding of stress-permeability relationships from studies like Gangi (1978) and Tsang and Witherspoon (1981). [Chen 2021, pp. 9-11]

## Open Questions
- How does full hydro-mechanical coupling, where fluid pressure influences fracture deformation and contact mechanics, affect the flow characteristics? [Chen 2021, pp. 18-18]
- How does asperity degradation under high confining stress further alter aperture distribution, eddy flow, and pressure heterogeneity? [Chen 2021, pp. 18-18]
- Can the findings be extended to full-scale fracture networks or different rock types? [Chen 2021, pp. 18-18]

## Source Coverage
All 16 non-empty indexed fragments were processed. The compiled source blocks total 16, covering 71,548 characters out of 76,761 indexed characters, resulting in a coverage ratio by characters of 0.932. The coverage status is "full-index".
