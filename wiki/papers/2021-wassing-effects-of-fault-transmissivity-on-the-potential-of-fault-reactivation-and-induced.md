---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-wassing-effects-of-fault-transmissivity-on-the-potential-of-fault-reactivation-and-induced"
title: "Effects of Fault Transmissivity on the Potential of Fault Reactivation and Induced Seismicity: Implications for Understanding Induced Seismicity at Pohang EGS."
status: "draft"
source_pdf: "data/papers/Effects of fault transmissivity on the potential of fault reactivation and induced seismicity Implications for understanding induced seismicity at Pohang EGS.pdf"
collections:
citation: "Wassing, B. B. T., et al. \"Effects of Fault Transmissivity on the Potential of Fault Reactivation and Induced Seismicity: Implications for Understanding Induced Seismicity at Pohang EGS.\" *Geothermics*, vol. 91, 2021, article 101976. doi:10.1016/j.geothermics.2020.101976. Accessed 2026."
indexed_texts: "11"
indexed_chars: "52712"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "50185"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.95206"
coverage_status: "full-index"
source_signature: "9e7550d325e7102e832c8a015054610a77ce34fe"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:41:32"
---

# Effects of Fault Transmissivity on the Potential of Fault Reactivation and Induced Seismicity: Implications for Understanding Induced Seismicity at Pohang EGS.

## One-line Summary
A 3D hydro-mechanical model demonstrates that fault transmissivity controls the relative contribution of pore pressure diffusion and poroelasticity to fault loading, influencing the spatio-temporal pattern of induced seismicity, with implications for the Pohang EGS site.

## Research Question
How do the hydromechanical properties of faults, particularly transmissivity, affect the relative contributions of pore pressure diffusion and poroelastic effects to fault loading and the resulting patterns of induced seismicity during and after hydraulic stimulation? [Wassing 2021, pp. 1-2]

## Study Area / Data
The study uses the Pohang Enhanced Geothermal System (EGS) site in Southeast Korea as a conceptual basis. The site features two injection wells, PX-1 and PX-2, targeting fractured granodiorites at depths of ~4.2-4.3 km. A low-permeability fault structure is interpreted to exist between the wells, with PX-1 in the hanging wall and PX-2 in the footwall. A magnitude Mw 5.5 earthquake occurred on November 15, 2017, on a nearby fault structure. Data includes well test analyses, injection parameters (rates up to 47 L/s, pressures up to 89 MPa), cumulative injection volumes (~12,800 m³), and seismic event locations linked to stimulation phases. [Wassing 2021, pp. 2-3]

## Methods
A 3D hydro-mechanical model coupling TOUGHREACT (for multiphase flow) and FLAC3D (for geomechanics) was employed. The model incorporates Dieterich’s rate-and-state formulation for earthquake nucleation rates. A conceptual model was built with a fault, damage zone, and matrix. Fault transmissivity was varied by changing fault core permeability (open, partially sealing, sealing). Sensitivity analyses were performed on damage zone properties (stiffness, permeability, width). Coulomb stress changes (Δτ_cs) were calculated to separate the direct pore pressure effect (μΔP) from poroelastic stress contributions (Δτ_s - μΔσ_n). Injection of 2000 m³ of water at 10 L/s for ~55 hours was simulated. [Wassing 2021, pp. 3-4]

## Key Findings
1.  Fault transmissivity strongly influences the spatio-temporal pattern of Coulomb stresses and induced seismicity. [Wassing 2021, pp. 7-8]
2.  For low-transmissivity (sealing) faults, poroelastic effects contribute significantly to fault loading, especially after shut-in, leading to prolonged post-shut-in seismicity. [Wassing 2021, pp. 5-6, 7-8]
3.  For high-transmissivity (open) faults, direct pore pressure diffusion dominates, causing seismicity to peak early during injection and decline rapidly after shut-in. [Wassing 2021, pp. 5-6]
4.  The location of slip localization (within the fault core vs. at the core-damage zone interface) critically affects the relative importance of pore pressure diffusion versus poroelasticity. [Wassing 2021, pp. 6-7]
5.  A damage zone with low transmissivity (low permeability or small width) magnifies both direct pore pressure and poroelastic loading on the fault, increasing seismicity rates. [Wassing 2021, pp. 7-8]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Poroelastic effects can significantly contribute to fault loading, specifically in cases of low fault transmissivity. | [Wassing 2021, pp. 1-2] | Conceptual model with varying fault permeability. | Key conclusion from modeling. |
| For a sealing fault, seismicity rates before shut-in are slow and limited to the upper fault segment; after shut-in, the lower segment shows increased seismicity rates for a prolonged period. | [Wassing 2021, pp. 5-6] | Slip localization within the fault core. | Demonstrates delayed seismicity due to poroelastic effects. |
| The presence of a sealing fault structure close to the injection well can increase the relative contribution of poroelasticity to fault loading. | [Wassing 2021, pp. 7-8] | General finding from model scenarios. | Implication for sites like Pohang. |
| Low damage zone transmissivity (low permeability or small width) magnifies direct pore pressure and poroelastic loading, resulting in higher Coulomb stresses and seismic event rates before shut-in. | [Wassing 2021, pp. 7-8] | Sensitivity analysis on damage zone properties. | Highlights importance of damage zone characterization. |
| The choice of slip localization has a large effect on the relative contribution of pore pressure diffusion and poroelastic deformation to fault loading. | [Wassing 2021, pp. 6-7] | Comparison of slip in fault core vs. core-damage zone interface. | Major source of model uncertainty. |

## Limitations
1.  The model simulates rocks as homogeneous porous media without fractures, whereas the Pohang granodiorites are fractured. Preferential flow and fracture deformation are not accounted for. [Wassing 2021, pp. 7-8]
2.  The process of slip localization in faults under ambient pressure changes is poorly understood, and the choice of slip location in the model significantly affects results. [Wassing 2021, pp. 6-7]
3.  The study is conceptual and not a fully calibrated and validated model of the Pohang EGS stimulation activities. [Wassing 2021, pp. 2-3]
4.  Chemical reaction processes were not modeled. [Wassing 2021, pp. 3-4]

## Assumptions / Conditions
1.  Initial stress conditions are in a strike-slip tectonic regime (σ_Hmax > σ_v > σ_hmin) with specific stress gradients. [Wassing 2021, pp. 3-4]
2.  Pore pressure gradients are hydrostatic initially. [Wassing 2021, pp. 3-4]
3.  Fault geometry (dip 70°, dimensions 1000m x 3000m) is based on the focal mechanism of the Pohang Mw 5.5 event. [Wassing 2021, pp. 3-4]
4.  Injection occurs at a constant rate (10 L/s) into the damage zone of the hanging wall block. [Wassing 2021, pp. 3-4]
5.  Fault friction coefficient μ is used, and the rate-and-state parameter A is assumed to be 0.001. [Wassing 2021, pp. 4-5]

## Key Variables / Parameters
-   **Fault Transmissivity:** Controlled by fault core permeability (varied from 2e-19 m² to higher/lower values). [Wassing 2021, pp. 3-4]
-   **Damage Zone Properties:** Permeability, thickness, and elastic modulus (Young's modulus). [Wassing 2021, pp. 3-4]
-   **Biot Coefficient:** Determines coupling between pore pressure and poroelastic stress/strain. [Wassing 2021, pp. 3-4]
-   **Coulomb Stress Change (Δτ_cs):** Calculated from changes in shear stress, normal stress, and pore pressure. [Wassing 2021, pp. 4-5]
-   **Relative Seismicity Rate (R):** Derived from Coulomb stressing rates using Dieterich's formulation. [Wassing 2021, pp. 4-5]
-   **Slip Localization:** Assumed either within the fault core or at the interface between the fault core and damage zone. [Wassing 2021, pp. 6-7]

## Reusable Claims
1.  **Condition:** For faults with low transmissivity (e.g., sealing faults) near fluid injection wells. **Claim:** Poroelastic effects can become a dominant contributor to fault loading, particularly after injection shut-in, leading to a prolonged period of elevated seismicity risk. [Wassing 2021, pp. 5-6, 7-8]
2.  **Condition:** When assessing induced seismicity potential at EGS sites. **Claim:** A quantitative understanding of the stress and seismicity response requires the incorporation of both pore pressure diffusion and poroelastic effects, as their relative importance is controlled by fault and damage zone transmissivity. [Wassing 2021, pp. 1-2, 7-8]
3.  **Condition:** In hydro-mechanical models of fault reactivation. **Claim:** The assumed location of slip localization (fault core vs. core-damage zone interface) is a critical parameter that significantly influences the predicted relative contributions of pore pressure and poroelasticity to fault stressing. [Wassing 2021, pp. 6-7]

## Candidate Concepts
-   [[Fault transmissivity]]
-   [[Poroelasticity]]
-   [[Pore pressure diffusion]]
-   [[Induced seismicity]]
-   [[Fault reactivation]]
-   [[Enhanced Geothermal Systems (EGS)]]
-   [[Coulomb stress change]]
-   [[Rate-and-state seismicity]]
-   [[Damage zone]]
-   [[Slip localization]]

## Candidate Methods
-   [[Coupled hydro-mechanical modeling]] (TOUGHREACT-FLAC3D)
-   [[Dieterich's rate-and-state formulation]]
-   [[Sensitivity analysis]]
-   [[Coulomb stress analysis]]

## Connections To Other Work
The study builds on and discusses findings from several related works:
-   Segall and Lu (2015) on pore pressure diffusion and poroelastic effects on Coulomb stressing rates. [Wassing 2021, pp. 1-2]
-   Chang and Segall (2016) on poroelastic stresses from injection into overlying strata affecting low-permeability basement faults. [Wassing 2021, pp. 1-2]
-   Chang and Yoon (2018) on the influence of low-permeability sealing faults on pore pressure evolution. [Wassing 2021, pp. 1-2]
-   Chang et al. (2020) on the combined effect of poroelasticity and pore pressure diffusion at Pohang. [Wassing 2021, pp. 2-3, 8-9]
-   Zbinden et al. (2020) on the dominance of direct pressure effects at the St. Gallen site. [Wassing 2021, pp. 2-3]
-   Ge et al. (2019) and Bethmann et al. (2019) on the interpretation of the Pohang fault as sealing and the distinct seismic clouds. [Wassing 2021, pp. 8-9]
-   The modeling approach follows Taron and Elsworth (2010). [Wassing 2021, pp. 2-3]

## Open Questions
1.  How do fracture deformation and changes in permeability in fractured rocks (like Pohang granodiorites) affect the relative contributions of pore pressure and poroelasticity? [Wassing 2021, pp. 7-8]
2.  What is the correct physical process governing slip localization in faults under the pressure changes induced by injection? [Wassing 2021, pp. 6-7]
3.  How do complex, sequential, and multi-well injection schemes (as occurred at Pohang) interact with fault transmissivity to influence seismicity patterns? [Wassing 2021, pp. 3-4]

## Source Coverage
All non-empty indexed fragments were processed. The compilation is based on 11 indexed source blocks containing 52,712 characters. The compiled page uses 50,185 characters from these sources, achieving a coverage ratio of 0.95206 by character count. The coverage status is "full-index".
