---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2015-zhao-thm-thermo-hydro-mechanical-coupled-mathematical-model-of-fractured-media-and-numerica"
title: "THM (Thermo-hydro-mechanical) Coupled Mathematical Model of Fractured Media and Numerical Simulation of a 3D Enhanced Geothermal System at 573 K and Buried Depth 6000 e7000 M."
status: "draft"
source_pdf: "data/papers/201501.THM (Thermo-hydro-mechanical) coupled mathematical model of fractured media and numerical simulation of a 3D enhanced geothermal system at 573 K and buried depth 6000-7000 M.pdf"
collections:
citation: "Zhao, Yangsheng, et al. “THM (Thermo-hydro-mechanical) Coupled Mathematical Model of Fractured Media and Numerical Simulation of a 3D Enhanced Geothermal System at 573 K and Buried Depth 6000 e7000 M.” *Energy*, 2015, pp. 1–13, doi:10.1016/j.energy.2015.01.030."
indexed_texts: "11"
indexed_chars: "50715"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "50947"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004575"
coverage_status: "full-index"
source_signature: "1b9449a197fce1252e81576f834a128ab3e41bdf"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:02:52"
---

# THM (Thermo-hydro-mechanical) Coupled Mathematical Model of Fractured Media and Numerical Simulation of a 3D Enhanced Geothermal System at 573 K and Buried Depth 6000 e7000 M.

## One-line Summary
This study establishes a 3D THM coupled model for fractured media to simulate HDR geothermal extraction at 573 K and 6000-7000 m depth, finding that temperature, pressure, and fracture aperture evolve significantly over a 9-year operation, with exponential decline in heat extraction and substantial energy recovery potential.

## Research Question
How do temperature, stress, seepage, and fracture aperture fields evolve during HDR geothermal extraction under THM coupling at high temperature (573 K) and depth (6000-7000 m), and what are the implications for system output and lifespan? [Zhao 2015, pp. 1-2]

## Study Area / Data
The study is based on the Tengchong geothermal field in Yunnan, China, characterized by a geothermal gradient of 50 K/km and a buried depth of 6250-6750 m. The numerical model simplifies the system to a 5.0 × 5.0 × 5.0 km³ cube at a depth of 4 km, incorporating two parallel vertical fractures 500 m apart and injection/production wells. [Zhao 2015, pp. 3-4]

## Methods
A three-dimensional THM coupled mathematical model for fractured media was developed. The model uses a dual-media approach (matrix rock block and fracture) and is solved using the finite element method (FEM) with hexahedral eight-node isoparametric elements for the rock matrix and eight-node Goodman joint elements for fractures. A combination of coarse (50 m × 50 m × 50 m) and fine (down to 5 m × 5 m × 5 m) grids was employed to balance accuracy and computational load. [Zhao 2015, pp. 3-4]

## Key Findings
1.  The rock mass temperature near the injection well decreased from an initial 573 K to 423 K after 9 years of operation. [Zhao 2015, pp. 1-2]
2.  The initial water pressure gradient in the fracture near the injection well was 0.17 MPa/m, decreasing to 0.052 MPa/m after 1 year. [Zhao 2015, pp. 1-2]
3.  The fracture aperture tripled from its initial value over the 9-year period, causing the permeability coefficient to increase ninefold. [Zhao 2015, pp. 1-2]
4.  The amount of extracted geothermal energy declined exponentially with time, following the formula Q = 1114.6e^(-0.1112t). The total extracted energy over 9 years was 5977 MWa. [Zhao 2015, pp. 11-12]
5.  After stopping extraction, the geothermal reservoir recovered 3815.5 MWa of energy over 4 years, accounting for 63.8% of the total energy extracted during the 9-year operation. [Zhao 2015, pp. 11-12]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Rock mass temperature decreased from 573 K to 423 K after 9 years. | [Zhao 2015, pp. 1-2] | Tengchong field model, 573 K initial temp, 9-year extraction. | Temperature decline near injection well. |
| Initial fracture pressure gradient of 0.17 MPa/m decreased to 0.052 MPa/m after 1 year. | [Zhao 2015, pp. 1-2] | Injection well pressure 27.3 MPa, production well 9.8 MPa. | Gradient stabilizes after ~1 year. |
| Fracture aperture tripled; permeability coefficient increased ninefold. | [Zhao 2015, pp. 1-2] | Initial aperture 50 mm, 9-year operation. | Aperture growth logarithmic, stabilizing after ~3 years. |
| Extracted heat Q = 1114.6e^(-0.1112t); total 5977 MWa over 9 years. | [Zhao 2015, pp. 11-12] | Constant pressure mining system. | Exponential decline in output. |
| Reservoir recovered 3815.5 MWa (63.8% of extracted) in 4 years post-extraction. | [Zhao 2015, pp. 11-12] | Extraction stopped after 9 years. | Rapid recovery, especially in first year (37% of total extracted). |

## Limitations
The model simplifies the complex geology of the Tengchong field into an idealized cube with two parallel fractures. The authors note a lack of practical engineering data for HDR systems at the specified high temperature and depth to validate the results. [Zhao 2015, pp. 12-13]

## Assumptions / Conditions
1.  The rock mass is a dual-media system of matrix blocks and fractures. The matrix is a homogeneous isotropic elastomer, and its water storage and permeability are neglected. [Zhao 2015, pp. 2-2]
2.  Fracture seepage follows Darcy's Law, and fracture deformation follows the joint unit model. [Zhao 2015, pp. 2-2]
3.  Water is single-phase, does not vaporize under high pressure, and its density is a function of pressure and temperature. [Zhao 2015, pp. 2-2]
4.  Heat transfer occurs via conduction and convection; radiation is neglected. [Zhao 2015, pp. 2-2]
5.  The effective stress law for fractures is σ' = σ - bA·p, where bA is the connectivity area ratio. [Zhao 2015, pp. 2-2]

## Key Variables / Parameters
-   **Temperature (T):** Initial rock mass temperature of 573 K. [Zhao 2015, pp. 1-2]
-   **Water Pressure (P):** Injection well pressure 27.3 MPa, production well pressure 9.8 MPa. [Zhao 2015, pp. 3-4]
-   **Fracture Aperture (b):** Initial value 50 mm. [Zhao 2015, pp. 7-8]
-   **Permeability Coefficient (kfi):** Related to aperture by kfi = b²/12. [Zhao 2015, pp. 2-2]
-   **Geothermal Gradient:** 50 K/km. [Zhao 2015, pp. 1-2]
-   **Buried Depth:** 6000-7000 m (modeled at 6250-6750 m). [Zhao 2015, pp. 1-2]

## Reusable Claims
-   Under THM coupling at 573 K and ~6500 m depth, the fracture aperture in an HDR reservoir can triple over a 9-year extraction period, leading to a ninefold increase in permeability and reduced seepage resistance. [Zhao 2015, pp. 1-2, 7-8]
-   The heat extraction rate from a deep HDR system declines exponentially with time, but significant thermal energy recovery (over 60% of extracted energy) can occur within 4 years of ceasing operations. [Zhao 2015, pp. 11-12]
-   The water pressure gradient in the fracture network stabilizes after approximately one year of operation under constant wellhead pressure conditions. [Zhao 2015, pp. 6-7]

## Candidate Concepts
-   [[Enhanced Geothermal System (EGS)]]
-   [[Hot Dry Rock (HDR)]]
-   [[Thermo-Hydro-Mechanical (THM) Coupling]]
-   [[Fracture Reservoir]]
-   [[Dual-Porosity Media]]
-   [[Geothermal Gradient]]

## Candidate Methods
-   [[Finite Element Method (FEM)]]
-   [[Numerical Simulation]]
-   [[Goodman Joint Element]]
-   [[Coarse and Fine Grid Discretization]]
-   [[Darcy's Law for Fracture Flow]]

## Connections To Other Work
The study compares its findings on fracture aperture evolution and pressure gradients with those of Ghassemi and Zhou [11], noting differences likely due to model simplifications and the higher temperature/depth conditions in this work. It also references studies on THM/THMC coupling by Kohl et al. [4], Taron and Elsworth [15], and Pandey et al. [10]. [Zhao 2015, pp. 1-2, 7-8]

## Open Questions
-   How would more complex fracture network geometries (beyond two parallel planes) affect the THM coupled behavior and system efficiency?
-   What is the long-term (decades to centuries) evolution of the reservoir under cyclic extraction and recovery?
-   How do chemical processes (THMC coupling) influence fracture aperture and permeability under these extreme conditions? [Zhao 2015, pp. 1-2]

## Source Coverage
All 11 non-empty indexed fragments were processed. The compiled source blocks total 11, with a compiled character count of 50,947 against an indexed character count of 50,715, yielding a coverage ratio by characters of 1.004575. The coverage status is full-index.
