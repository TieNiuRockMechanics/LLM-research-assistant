---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-chen-convective-heat-transfer-of-water-flow-in-intersected-rock-fractures-for-enhanced-geot-4609083c"
title: "Convective Heat Transfer of Water Flow in Intersected Rock Fractures for Enhanced Geothermal Extraction."
status: "draft"
source_pdf: "data/papers/Convective heat transfer of water flow in intersected rock fractures for enhanced geothermal extraction.pdf"
collections:
citation: "Chen, Yuedu, et al. \"Convective Heat Transfer of Water Flow in Intersected Rock Fractures for Enhanced Geothermal Extraction.\" *Journal of Rock Mechanics and Geotechnical Engineering*, 2021, doi:10.1016/j.jrmge.2021.05.005. Accessed 2026."
indexed_texts: "14"
indexed_chars: "67079"
nonempty_source_blocks: "14"
compiled_source_blocks: "14"
compiled_source_chars: "65593"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.977847"
coverage_status: "full-index"
source_signature: "bb5ccb8ddb432808f100800474fc26d0ebebc318"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:35:43"
---

# Convective Heat Transfer of Water Flow in Intersected Rock Fractures for Enhanced Geothermal Extraction.

## One-line Summary
This study uses 3D numerical simulations to investigate how the geometry of intersected dead-end fractures (DEFs) affects convective heat transfer and geothermal heat extraction efficiency.

## Research Question
How do the geometric characteristics of intersected dead-end fractures (DEFs)—including intersected angle, aperture, length, and connectivity—influence the convective heat transfer behavior and heat recovery performance in enhanced geothermal systems? [Chen 2021, pp. 1-2]

## Study Area / Data
The study uses constructed 3D numerical models of intersected rock fractures. The surface geometries of the main flow fracture (MFF) and dead-end fracture (DEF) are upscaled from scanning data of laboratory-scale Brazilian-induced tensile and natural granite fractures, respectively. [Chen 2021, pp. 4-5] The computational domain is a 2 m cubic model with an initial constant temperature of 423.15 K (approximating a reservoir at ~4000 m depth). Water at 313.15 K is injected at a constant velocity. [Chen 2021, pp. 4-5]

## Methods
The study performs flow-through heat transfer simulations by solving coupled hydrothermal equations. The fluid flow is modeled using the Stokes' equation (suitable for low Reynolds number flow), and heat transfer is governed by convection-conduction in the fluid and conduction in the rock. [Chen 2021, pp. 3-4] The models assume an impermeable granite matrix, local thermal equilibrium (LTE) at the fracture-fluid interface, and negligible inertial forces. [Chen 2021, pp. 3-4] Three modeling scenarios were designed to investigate the effects of: (I) intersected angles (20°, 55°, 90°, 125°, 155°), (II) DEF aperture (0.082 mm to 0.432 mm) and length (2 mm to 15 mm), and (III) DEF connectivity (single, three unconnected, seven connected). [Chen 2021, pp. 5-7] Simulations were run for 240 hours with a time step of 0.3 hours. [Chen 2021, pp. 5-7] Output parameters include the average outlet water temperature (T_out) and total heat production (Q). [Chen 2021, pp. 7-8]

## Key Findings
1.  Annular streamlines form in rough DEFs, leading to an elliptical distribution of the cold front, unlike in plate (smooth) fractures. [Chen 2021, pp. 7-8]
2.  Fluid flow in rough DEFs enhances heat transfer compared to plate DEFs. Simulations using plate fractures misestimate temperature evolution and heat production. [Chen 2021, pp. 8-10]
3.  Both the outlet temperature increment (ΔT_out) and heat production ratio (Q_r) are largest at an intersected angle of 90° and decline as the angle decreases. [Chen 2021, pp. 10-12]
4.  Increasing the length of intersected DEFs is beneficial to heat production, while increasing their aperture is not needed. [Chen 2021, pp. 10-12]
5.  Solely increasing the number of unconnected DEFs induces little increase in heat extraction. Significant improvement requires connecting DEFs to the MFF to form a flow network. [Chen 2021, pp. 10-12]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Annular streamlines in rough DEF cause an ellipse distribution of the cold front. | [Chen 2021, pp. 7-8] | Intersected angle 90°, injection velocity 0.002 m/s | Observed in temperature distribution plots. |
| ΔT_out and Q_r are largest at 90° intersected angle and decline with decreasing angle. | [Chen 2021, pp. 10-12] | Rough fracture models, various injection velocities | Compared to a baseline at 30°. |
| Increasing DEF length from 2 mm to 15 mm increases ΔT_out and Q_r. | [Chen 2021, pp. 10-12] | Fixed aperture (0.082 mm), various injection velocities | Attributed to higher flow velocity and increased heat transfer area. |
| Increasing DEF aperture from 0.082 mm to 0.432 mm causes ΔT_out and Q_r to decrease then stabilize. | [Chen 2021, pp. 10-12] | Fixed length (15 mm), various injection velocities | Attributed to lower flow velocity within larger apertures. |
| Model M2 (7 connected DEFs) shows significantly higher ΔT_out and Q_r than M0 (1 DEF) or M1 (3 unconnected DEFs). | [Chen 2021, pp. 10-12] | Various injection velocities | Demonstrates the critical role of connectivity. |

## Limitations
1.  The study is limited to coupled hydrothermal modeling; thermoelastic or poroelastic effects are not considered. [Chen 2021, pp. 12-13]
2.  Model sizes (2 m) and time scales (10 days) are small; upscaling findings to real subsurface projects is an important future issue. [Chen 2021, pp. 12-13]
3.  The connectivity between injection and production wells within the fracture network is not discussed. [Chen 2021, pp. 12-13]

## Assumptions / Conditions
1.  The granite matrix is impermeable; fractures are the main channel for heat and fluid flow. [Chen 2021, pp. 3-4]
2.  Local thermal equilibrium (LTE) is assumed at the fracture-fluid interface. [Chen 2021, pp. 3-4]
3.  Inertial forces are neglected (Stokes' flow). [Chen 2021, pp. 3-4]
4.  Hydraulic and thermal properties of water vary with temperature; granite properties are constant. [Chen 2021, pp. 5-7]

## Key Variables / Parameters
*   **Intersected Angle:** Angle between the main flow fracture (MFF) and dead-end fracture (DEF). [Chen 2021, pp. 5-7]
*   **Mechanical Aperture:** The aperture of the DEF. [Chen 2021, pp. 5-7]
*   **Length of DEF:** The length of the intersected dead-end fracture. [Chen 2021, pp. 5-7]
*   **Connectivity:** The number and connection state of DEFs (unconnected vs. connected to MFF). [Chen 2021, pp. 5-7]
*   **Injection Velocity:** The constant velocity of the injected water. [Chen 2021, pp. 5-7]
*   **ΔT_out:** Increment of average outlet water temperature (T_out - T_0). [Chen 2021, pp. 7-8]
*   **Q_r:** Ratio of total heat production (Q/Q_0). [Chen 2021, pp. 7-8]

## Reusable Claims
*   **Condition:** For water flow in intersected rough rock fractures at low Reynolds numbers. **Claim:** The convective heat transfer efficiency is maximized when the intersected angle between the main flow path and a dead-end branch is 90°. [Chen 2021, pp. 10-12]
*   **Condition:** For enhancing heat extraction in a fractured geothermal reservoir. **Claim:** Extending the reactivated length of intersected natural fractures is beneficial, whereas increasing their aperture is not necessary. [Chen 2021, pp. 10-12]
*   **Condition:** For designing hydraulic stimulation in geothermal reservoirs. **Claim:** Simply increasing the number of intersected dead-end fractures provides minimal benefit; significant heat production gains require creating flow connectivity between these fractures and the main flow path. [Chen 2021, pp. 10-12]

## Candidate Concepts
*   [[Enhanced Geothermal System (EGS)]]
*   [[Dead-end fracture (DEF)]]
*   [[Main flow fracture (MFF)]]
*   [[Fracture network connectivity]]
*   [[Convective heat transfer]]
*   [[Cold front]]
*   [[Channeling flow]]
*   [[Hydrothermal coupling]]

## Candidate Methods
*   [[3D numerical simulation]]
*   [[Navier-Stokes equations (Stokes' flow)]]
*   [[Energy conservation equation]]
*   [[Hydrothermal coupling]]
*   [[Sensitivity analysis]]
*   [[Model verification against analytical solution]]

## Connections To Other Work
The study builds on and references numerous prior works on heat transfer in fractured geothermal reservoirs, including studies on the effects of fracture network distribution [Ma et al. 2020; Zhang et al. 2019c], fracture density [Shi et al. 2019a], and fracture roughness [Ma et al. 2018; He et al. 2019]. [Chen 2021, pp. 2-3] It specifically addresses a gap identified in previous research: most studies treated fractures as smooth plates or hypothetical rough fractures with uniform apertures, neglecting the heterogeneous apertures of real rock fractures. [Chen 2021, pp. 2-3]

## Open Questions
1.  How do thermoelastic and poroelastic deformations affect the heat transfer process in intersected rough fractures? [Chen 2021, pp. 12-13]
2.  How can the findings be upscaled to real, larger-scale subsurface fracture networks? [Chen 2021, pp. 12-13]
3.  How does the connectivity between injection and production wells within the fracture network influence performance? [Chen 2021, pp. 12-13]

## Source Coverage
All 14 non-empty indexed fragments were processed. The compiled source blocks total 14, with a compiled character count of 65,593 out of a total indexed character count of 67,079, resulting in a coverage ratio by characters of 0.977847. The coverage status is "full-index".
