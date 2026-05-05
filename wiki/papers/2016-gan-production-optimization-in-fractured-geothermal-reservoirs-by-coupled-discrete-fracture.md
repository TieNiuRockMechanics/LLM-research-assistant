---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2016-gan-production-optimization-in-fractured-geothermal-reservoirs-by-coupled-discrete-fracture"
title: "Production Optimization in Fractured Geothermal Reservoirs by Coupled Discrete Fracture Network Modeling."
status: "draft"
source_pdf: "data/papers/Production optimization in fractured geothermal reservoirs by coupled discrete fracture network modeling.pdf"
collections:
citation: "Gan, Quan, and Derek Elsworth. \"Production Optimization in Fractured Geothermal Reservoirs by Coupled Discrete Fracture Network Modeling.\" *Geothermics*, vol. 62, 2016, pp. 131-142."
indexed_texts: "10"
indexed_chars: "46321"
nonempty_source_blocks: "10"
compiled_source_blocks: "10"
compiled_source_chars: "46282"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.999158"
coverage_status: "full-index"
source_signature: "5761807c2ff63f4b69a54558556c019a295394e8"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:42:05"
---

# Production Optimization in Fractured Geothermal Reservoirs by Coupled Discrete Fracture Network Modeling.

## One-line Summary
A coupled discrete fracture network model demonstrates that stimulating parallel permeable manifolds aligned with the major principal stress direction in a fractured geothermal reservoir significantly enhances heat sweep efficiency and sustains higher electric power production over a 10-year period compared to conventional stimulation strategies.

## Research Question
How can stimulation strategies be optimized in Enhanced Geothermal Systems (EGS) with pre-existing fracture networks to maximize the magnitude and longevity of thermal recovery rates and electric power generation?

## Study Area / Data
The study uses a generic, prototypical EGS reservoir model. The reservoir dimensions are 1500 m × 1500 m × 10 m. It contains two sets of pre-existing fractures with a density of approximately 0.09 m⁻¹ and an initial permeability in the range of 10⁻¹⁷ to 10⁻¹⁶ m². The initial uniform rock temperature is 250°C (523 K), and the initial uniform pore pressure is 10 MPa. The in-situ stress state is anisotropic, with a major principal stress of 30 MPa in the E-W direction and a minor principal stress of 19.5 MPa in the N-S direction [Gan 2016, pp. 4-5].

## Methods
The study employs an equivalent continuum simulator (TF FLAC3D) that incorporates a coupled Thermal-Hydraulic-Mechanical (THM) model for discrete fracture networks. Key methodological components include:
*   **Crack Tensor Theory:** Fracture mechanical properties are represented using a crack tensor to modify the elastic compliance of the rock mass [Gan 2016, pp. 2-3].
*   **Stress-Dependent Permeability:** A permeability tensor is defined, and fracture aperture evolution is modeled using a simplified Barton-Bandis hyperbolic model for normal closure, a Coulomb failure criterion for shear dilation, and a geometrical stiffness model for fracture opening under tensile effective stress [Gan 2016, pp. 3-4].
*   **Reservoir Simulation:** The model simulates a stimulation phase followed by a production phase. Two stimulation strategies are compared: creating parallel manifolds in the E-W direction (aligned with major stress) or in the N-S direction. Production is then conducted with injection at 15 MPa and production at 7 MPa [Gan 2016, pp. 4-5].
*   **Power Calculation:** Instantaneous electric power generation is calculated as the product of production flow rate and the enthalpy difference between produced and injected water, with a heat utilization efficiency factor of 0.45 [Gan 2016, pp. 7-10].

## Key Findings
*   Stimulation that creates two parallel, hydraulically interconnected manifolds aligned with the major principal stress direction (E-W) results in the highest sustained electric power generation, reaching a peak of approximately 14 MWe and maintaining high output over 10 years [Gan 2016, pp. 7-10].
*   This optimized strategy (Case 4) yields cumulative energy recoveries a factor of 1.9 higher than for standard stimulation without manifold development [Gan 2016, pp. 1-1].
*   The orientation of pre-existing fractures critically influences stimulation effectiveness. Fractures oriented at 045° and 120° (favorably oriented for slip relative to the stress field) showed greater permeability enhancement along the E-W stimulation direction compared to fractures oriented at 020° and 135° [Gan 2016, pp. 7-10].
*   When one set of fractures has a higher friction angle (75°) and is less prone to shear failure, the output electric power is reduced due to decreased fluid flux rates [Gan 2016, pp. 7-10].
*   The optimized case (Case 4) demonstrated the most complete and uniform heat sweep, cooling the reservoir between injector and producer manifolds to the injected water temperature [Gan 2016, pp. 10-11].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Peak power generation of ~14 MWe sustained over 10 years. | [Gan 2016, pp. 7-10] | Case 4: Fractures oriented 045-120°, E-W stimulation. | Highest performance among all cases studied. |
| Cumulative energy recovery 1.9x higher than standard stimulation. | [Gan 2016, pp. 1-1] | Comparison of optimized manifold stimulation vs. conventional scenarios. | Key metric for long-term efficiency. |
| Fracture permeability enhanced by ~3 orders of magnitude after E-W stimulation. | [Gan 2016, pp. 7-10] | Fractures oriented 045-120°. | Due to ~10x increase in fracture aperture from extensile loading. |
| Fractures oriented 045-120° yield greater permeability enhancement than 020-135°. | [Gan 2016, pp. 7-10] | E-W stimulation direction. | Demonstrates importance of fracture orientation relative to stress. |
| Higher fracture friction angle (75°) reduces power output. | [Gan 2016, pp. 7-10] | Case 5: One fracture set with friction angle 75°. | Reduced shear failure potential impairs permeability enhancement. |
| Manifold stimulation creates a uniform flow field analogous to horizontal wells. | [Gan 2016, pp. 1-2] | Stimulation strategy creating parallel E-W manifolds. | Increases heat sweep efficiency. |

## Limitations
*   The study uses a generic reservoir model with specific, idealized fracture network geometries and stress conditions, which may not capture the full complexity of all real-world geothermal reservoirs [Gan 2016, pp. 4-5].
*   The equivalent continuum approach, while computationally efficient, simplifies the explicit representation of individual fracture interactions compared to fully discrete models [Gan 2016, pp. 1-2].
*   The model assumes a non-boiling system and does not account for potential chemical reactions or two-phase flow effects [Gan 2016, pp. 2-3].

## Assumptions / Conditions
*   The reservoir is initially at a uniform temperature and pressure [Gan 2016, pp. 4-5].
*   The intact rock is isotropic [Gan 2016, pp. 2-3].
*   The ratio of maximum normal closure to initial fracture aperture is constant at 0.9 [Gan 2016, pp. 3-4].
*   The heat utilization efficiency for power calculation is assumed to be 0.45 [Gan 2016, pp. 7-10].
*   The system is non-boiling, with water density changes considered negligible but viscosity changes significant [Gan 2016, pp. 1-2].

## Key Variables / Parameters
*   **Initial Fracture Permeability:** 10⁻¹⁷ to 10⁻¹⁶ m² [Gan 2016, pp. 4-5].
*   **Fracture Density:** ~0.09 m⁻¹ [Gan 2016, pp. 4-5].
*   **In-situ Stress:** Major principal stress (E-W) = 30 MPa; Minor principal stress (N-S) = 19.5 MPa [Gan 2016, pp. 4-5].
*   **Fracture Friction Angle:** Varied between 35° and 75° in sensitivity analysis [Gan 2016, pp. 5-7].
*   **Injection/Production Pressure:** Injection at 15 MPa, Production at 7 MPa (8 MPa drawdown) [Gan 2016, pp. 5-7].
*   **Stimulation Rate:** 20 kg/s for 10 hours per manifold [Gan 2016, pp. 5-7].

## Reusable Claims
*   In fractured geothermal reservoirs, stimulation strategies that develop parallel, high-permeability manifolds aligned with the major principal stress direction can create a uniform flow field that significantly enhances heat sweep efficiency and long-term power production [Gan 2016, pp. 1-2, 10-11].
*   The effectiveness of hydraulic stimulation in enhancing reservoir permeability is highly sensitive to the orientation of pre-existing fractures relative to the in-situ stress field, with fractures favorably oriented for slip yielding greater permeability enhancement [Gan 2016, pp. 7-10].
*   The potential for shear failure in fractures is a critical control on stimulated reservoir permeability; reducing this potential (e.g., via higher friction angles) can limit the achievable fluid flux and power output [Gan 2016, pp. 7-10].
*   For a given reservoir volume and temperature, the cumulative energy recovery is primarily determined by the efficiency of the thermal sweep, which can be optimized through stimulation design [Gan 2016, pp. 1-2].

## Candidate Concepts
*   [[Enhanced Geothermal Systems (EGS)]]
*   [[Discrete Fracture Network (DFN)]]
*   [[Thermal-Hydraulic-Mechanical (THM) Coupling]]
*   [[Crack Tensor Theory]]
*   [[Stress-Dependent Permeability]]
*   [[Hydraulic Stimulation]]
*   [[Thermal Breakthrough]]
*   [[Heat Sweep Efficiency]]
*   [[Equivalent Continuum Model]]

## Candidate Methods
*   [[Coupled THM Numerical Simulation]]
*   [[Equivalent Continuum Modeling with Crack Tensors]]
*   [[Barton-Bandis Hyperbolic Model for Fracture Closure]]
*   [[Coulomb Failure Criterion for Shear Dilation]]
*   [[Sensitivity Analysis for Stimulation Strategy]]

## Connections To Other Work
*   Builds upon prior development of the equivalent continuum T-H-M coupled simulator TF FLAC3D [Gan 2016, pp. 1-2].
*   References and utilizes concepts from crack tensor theory by Oda (1986) [Gan 2016, pp. 2-3].
*   Compares its continuum approach to discontinuum (explicit DFN) methods cited from other studies (e.g., Ghassemi and Zhang, 2006; McClure and Horne, 2013) [Gan 2016, pp. 1-2].
*   Discusses the role of thermal contraction and seismicity in altering permeability, citing prior work by the authors (Gan and Elsworth, 2014a,b) and others (Segall and Fitzgerald, 1998) [Gan 2016, pp. 1-2].
*   Acknowledges the importance of reservoir volume and well spacing, referencing work by Vörös et al. (2007) and Sanyal et al. (2005) [Gan 2016, pp. 1-2].

## Open Questions
*   How would the optimization strategy perform in reservoirs with more complex, heterogeneous fracture network topologies or varying stress regimes?
*   What are the long-term (>10 years) geomechanical and thermal impacts of creating such stimulated manifolds, including the potential for induced seismicity?
*   How do two-phase flow (boiling) and geochemical processes affect the performance of the proposed stimulation strategy?
*   What is the optimal spacing and geometry of the parallel manifolds for different reservoir conditions?

## Source Coverage
All non-empty indexed fragments were processed. The compilation strategy was single-pass-markdown. The coverage audit indicates 10 indexed texts, 46,321 indexed characters, and 10 non-empty source blocks. All 10 source blocks were compiled, resulting in 46,282 compiled characters. The coverage ratio by blocks is 1.0, and by characters is 0.999158, confirming full-index coverage.
