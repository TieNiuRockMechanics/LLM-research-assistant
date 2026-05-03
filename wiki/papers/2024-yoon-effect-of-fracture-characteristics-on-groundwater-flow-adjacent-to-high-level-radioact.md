---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2024-yoon-effect-of-fracture-characteristics-on-groundwater-flow-adjacent-to-high-level-radioact"
title: "Effect of Fracture Characteristics on Groundwater Flow Adjacent to High-Level Radioactive Waste Repository."
status: "draft"
source_pdf: "data/papers/2024 - Effect of fracture characteristics on groundwater flow adjacent to high-level radioactive waste repository.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Yoon, Won Woo, et al. \"Effect of Fracture Characteristics on Groundwater Flow Adjacent to High-Level Radioactive Waste Repository.\" *Journal of Hydrology*, vol. 629, 2024, 130593."
indexed_texts: "22"
indexed_chars: "108857"
nonempty_source_blocks: "22"
compiled_source_blocks: "22"
compiled_source_chars: "102986"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.946067"
coverage_status: "full-index"
source_signature: "0ab392ea4ce93f4b8d878781746619b60b8c58a4"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T07:28:35"
---

# Effect of Fracture Characteristics on Groundwater Flow Adjacent to High-Level Radioactive Waste Repository.

## One-line Summary
This study uses 2-D numerical models to evaluate how fracture geometry (orientation, density, length, intersection, and aperture) affects the spatio-temporal evolution of pressure-driven and buoyancy-driven groundwater flow induced by decay heat from a hypothetical high-level radioactive waste repository in granite.

## Research Question
The study aims to quantitatively analyze the impact of geometric characteristics of fractures and fracture networks on the spatio-temporal perturbations of heat-driven groundwater and fracture flow around a high-level radioactive waste (HLW) repository [Yoon 2024, pp. 2-2].

## Study Area / Data
A hypothetical HLW repository site in South Korea, based on the Korean Reference Disposal System (KRS) model. The model is a 2-D regional-scale domain (6,000 m wide, 2,000 m deep) with the repository at a depth of 500 m in granite [Yoon 2024, pp. 2-2]. An excavation-damaged zone (EDZ) of 60 m width and 20 m height surrounds the repository, containing 9 canisters [Yoon 2024, pp. 2-2]. Boundary conditions are based on a Tóthian topography-driven groundwater flow model [Yoon 2024, pp. 2-4].

## Methods
A series of 2-D numerical models were developed using COMSOL Multiphysics® to solve coupled groundwater flow and heat transfer equations for the porous matrix and discrete fractures [Yoon 2024, pp. 4-5]. A 3-D canister-scale model was first used to simulate the temporal change in canister surface temperature, which was then applied as a boundary condition in the 2-D model [Yoon 2024, pp. 2-4]. The modeling scenarios included a homogeneous base case, single fractures with varying orientations (0°, 30°, 60°, 90°), double intersecting fractures with varying heights, positions, and intersection angles (30°, 60°, 90°), and multiple discrete fracture network (DFN) models with varying density, length distribution (power-law exponent α), length-correlated aperture, orientation of fracture sets, and matrix permeability [Yoon 2024, pp. 5-5].

## Key Findings
- **Two-stage flow regime:** Heat generation induces a two-stage flow response: an early stage (<~100 years) dominated by pressure build-up causing radial groundwater flow, and a late stage (peaking ~2,000 years) dominated by temperature-induced buoyancy causing vertical flow [Yoon 2024, pp. 1-2, 7-7].
- **Fracture orientation:** Fracture flow velocity is governed by the alignment between the fracture orientation and the direction of the regional groundwater flow (radial in the early stage, vertical in the late stage) [Yoon 2024, pp. 18-19].
- **Network density:** In the early stage, higher fracture network density did not lead to an increase in average fracture flow. In the late stage, it significantly increased average flow due to more frequent and larger convection-circulating flow [Yoon 2024, pp. 1-2, 12-13].
- **Fracture length:** Long fractures serve as preferential flow pathways in the early stage and conduits for circulating flow in the late stage. The spatial distribution of long fractures causes significant uncertainty in average fracture flow during the late stage [Yoon 2024, pp. 1-2, 14-14].
- **Fracture aperture:** The heat-induced fracture flow in the late stage can be effectively mitigated in networks with small apertures, such as those estimated for the Forsmark site [Yoon 2024, pp. 14-15, 18-19].
- **Intersection angle:** A low angle of intersection between fracture sets results in low connectivity, which decelerates the average fracture flow in both early and late stages [Yoon 2024, pp. 1-2, 14-15].
- **DFN vs. DFM Model:** A discrete fracture network (DFN) model that ignores matrix flow may underestimate heat-induced fracture flow compared to a discrete fracture-matrix (DFM) model, primarily by missing early pressure-driven flow and late buoyancy-driven flow in isolated fractures [Yoon 2024, pp. 15-16].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| Early-stage pressure build-up induces radial groundwater flow, while late-stage buoyancy drives vertical flow. | [Yoon 2024, pp. 1-2] | 2-D model, KRS-like repository geometry, granite host rock, 0.1-2,000 year timeframe. | Basis for the two-stage analysis. |
| Higher fracture density (ρ₂₁ from 3.26×10⁻³ to 9.78×10⁻³ m/m²) decreased average u<sup>tot</sup><sub>f,N</sub> in the early stage but increased it in the late stage. | [Yoon 2024, pp. 12-13] | Cases 3A-3C: 500-1,500 fractures, length=80m, orientations 45°/135°. | u<sup>tot</sup><sub>f,N</sub> is total fracture flow change normalized by total length. |
| A decrease in the power-law exponent of fracture length from α=2.5 to α=1.5 (increasing the proportion of long fractures) increased the variability and magnitude of u<sup>tot</sup><sub>f,N</sub> peaks, especially in the late stage. | [Yoon 2024, pp. 14-14] | Cases 3D-3F: α=2.5, 2.0, 1.5; fracture density fixed at ~6.52×10⁻³ m/m². | Late-stage flow is highly sensitive to the geometry of individual long fractures. |
| Implementing a length-correlated aperture (based on Forsmark data) diminished the late-stage Q<sup>tot</sup><sub>f,N</sub> peak. | [Yoon 2024, pp. 14-15] | Case 3E vs. 3E_corr: aperture from lognormal distribution with a=6.3e-9, b=1.3, σ=1.0. | Suggests small apertures can mitigate thermally-driven circulation. |
| Low network connectivity from a 30° intersection angle significantly decelerated average fracture flow in both stages compared to 90° and 60° angles. | [Yoon 2024, pp. 14-15] | Cases 3G-3I: 1,000 fractures, two sets with intersection angles of 90°, 60°, 30°. | Node connectivity (n_c) was 0.7727, 0.6715, and 0.3856, respectively. |
| DFN model (no matrix flow) showed an absence of early-stage u<sup>tot</sup><sub>f,N</sub> peak and a diminished late-stage peak compared to the DFM model. | [Yoon 2024, pp. 15-16] | Case 3E (DFM) vs. Case 3J (DFN). Isolated fractures excluded in DFN model. | Highlights the role of the matrix in pressure propagation and connecting isolated fractures. |

## Limitations
- The effect of fracture groundwater flow was not considered when simulating the canister surface temperature in the precursor 3-D model [Yoon 2024, pp. 19-19].
- The 2-D model geometry is simplified, leading to potential discrepancies in fracture properties (e.g., density, connectivity enhancement rate) compared to a real 3-D site [Yoon 2024, pp. 19-20].
- The model assumes fully saturated conditions, which may overestimate build-up pressure compared to an initially unsaturated repository where volume expansion could be accommodated [Yoon 2024, pp. 19-20].
- Fracture network properties investigated are not site-specific; only one or two fracture sets with specific orientations were considered [Yoon 2024, pp. 19-20].
- The study does not account for geochemical processes, vaporization of pore water, or radionuclide transport [Yoon 2024, pp. 18-19].

## Assumptions / Conditions
- Repository geometry is based on the Korean Reference Disposal System (KRS) model with 9 canisters [Yoon 2024, pp. 1-2].
- Fracture permeability follows the cubic law (k_f = d_f² / 12f) with a roughness factor f = 1 [Yoon 2024, pp. 4-4].
- The matrix (granite) is crystalline and incompressible [Yoon 2024, pp. 6-7].
- A constant fracture aperture of 0.5 mm was used except for the correlated aperture case (3E_corr) [Yoon 2024, pp. 5-5].
- Top boundary pressure gradient is constant at 0.001; bottom and lateral boundaries are no-flow; temperature boundaries are 20°C at top and 80°C at bottom [Yoon 2024, pp. 2-4].
- The effective thermal conductivity is calculated by the weighted geometric mean of matrix and fluid conductivities [Yoon 2024, pp. 4-5].

## Key Variables / Parameters
- `u_f`: Darcy velocity in fracture [Yoon 2024, pp. 4-4]
- `u_tot_f,N`: Total change in fracture flow relative to initial conditions, summed across the network and normalized by total fracture length [Yoon 2024, pp. 11-12]
- `Q_tot_f,N`: Analogous to u_tot_f,N but for flow rate (Q_f), used when aperture varies [Yoon 2024, pp. 14-14]
- `k_f`: Fracture permeability [Yoon 2024, pp. 4-4]
- `k_m`: Medium (matrix) permeability (Base granite = 1×10⁻¹⁷ m²) [Yoon 2024, pp. 5-5]
- `α`: Exponent of the truncated power-law distribution for fracture length [Yoon 2024, pp. 13-14]
- `ρ₂₁`: Fracture density (total fracture length / domain area) [Yoon 2024, pp. 12-12]
- `n_c`: Node connectivity (total number of intersections / total number of fractures) [Yoon 2024, pp. 12-12]

## Reusable Claims
- **Claim:** In a crystalline HLW repository, heat-induced groundwater flow can be divided into an early pressure-driven phase and a late buoyancy-driven phase, with the dominant flow direction shifting from radial to vertical. **Limitation:** The duration of the early pressure phase depends on the assumed saturation state; an unsaturated initial condition could mitigate pressure build-up [Yoon 2024, pp. 19-20].
- **Claim:** Increasing fracture network density does not proportionally increase average fracture flow in the early pressure-driven stage because flow is concentrated in a few preferential pathways. **Limitation:** Modeled in 2-D with constant fracture length and permeability [Yoon 2024, pp. 12-13].
- **Claim:** Long fractures are key controllers of flow in both early and late stages, serving as preferential pathways initially and enabling large-scale convection-circulating flow later. **Limitation:** The prediction of late-stage circulating flow is highly uncertain and depends on the exact spatial distribution of long fractures [Yoon 2024, pp. 1-2, 14-14].
- **Claim:** The magnitude of late-stage buoyancy-driven fracture flow can be significantly reduced if fracture apertures are small and play a controlling role. **Limitation:** Based on one parameter set correlating fracture length to aperture from the Forsmark site [Yoon 2024, pp. 14-15].
- **Claim:** A DFN model that neglects matrix permeability (flow through the rock matrix) can underestimate total fracture flow by failing to capture pressure dissipation through the matrix and buoyancy-driven flow in isolated fractures. **Limitation:** Result is from a specific DFN realization; requires further study under general conditions [Yoon 2024, pp. 15-16].

## Candidate Concepts
- [[pressure-driven flow]]
- [[buoyancy-driven convection]]
- [[discrete fracture network (DFN)]]
- [[discrete fracture-matrix (DFM) model]]
- [[excavation-damaged zone (EDZ)]]
- [[fracture connectivity]]
- [[fracture preferential flow pathway]]
- [[convection-circulating flow]]
- [[tothian groundwater flow]]
- [[multi-barrier system]]

## Candidate Methods
- [[2-D coupled hydrothermal modeling]]
- [[COMSOL Multiphysics]]
- [[fracture length power-law distribution]]
- [[cubic law for fracture flow]]
- [[fracture length-aperture correlation]]
- [[stochastic discrete fracture network generation]]

## Connections To Other Work
- **Conceptual model:** The boundary conditions follow the Tóth (1962) conceptual model for topography-driven groundwater flow [Yoon 2024, pp. 2-4].
- **Heat-driven convection:** Occurrence of buoyancy-driven convection around the HLW repository was predicted by Harris et al. (2015), Runchal and Maini (1980), and Tsang and Pruess (1987) [Yoon 2024, pp. 6-7].
- **Fracture flow geometry:** The current work matches Vujević et al. (2014) and Vujević and Graf (2015) regarding groundwater circulation induced by convection in fractures [Yoon 2024, pp. 12-13].
- **Fracture length and flow:** The finding that long fractures primarily serve as preferential pathways is consistent with Tsang et al. (2015) [Yoon 2024, pp. 13-14].
- **Fracture length-aperture correlation:** The methodology for correlated aperture is based on the relationship defined by Follin (2008) and Joyce et al. (2014) for the Forsmark site [Yoon 2024, pp. 14-14].

## Open Questions
- What are the discrepancies in fracture network property effects (e.g., connectivity enhancement rate) between 2-D and 3-D models? [Yoon 2024, pp. 19-20]
- How would the results change under unsaturated, two-phase flow conditions, particularly the early-stage pressure build-up? [Yoon 2024, pp. 19-20]
- How do the statistical properties of a complex fracture network that can be obtained from in-situ borehole data quantitatively relate to heat-induced fracture flow? [Yoon 2024, pp. 18-19]
- How does heat-induced fracture flow alter other geochemical processes, such as seawater intrusion, and thereby impact engineered barrier performance? [Yoon 2024, pp. 18-19]

## Source Coverage
All indexed text fragments were processed. Coverage audit: indexed_texts=22, compiled_source_blocks=22, coverage_ratio_by_blocks=1.0, coverage_ratio_by_chars=0.946067. [Yoon 2024, pp. 1-20]
