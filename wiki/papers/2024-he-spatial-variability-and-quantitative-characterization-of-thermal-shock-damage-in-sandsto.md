---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2024-he-spatial-variability-and-quantitative-characterization-of-thermal-shock-damage-in-sandsto"
title: "Spatial Variability and Quantitative Characterization of Thermal Shock Damage in Sandstone under Different Cooling Temperatures."
status: "draft"
source_pdf: "data/papers/2025 - Spatial variability and quantitative characterization of thermal shock damage in sandstone under different cooling temperatures.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "He, Shuixin, et al. \"Spatial Variability and Quantitative Characterization of Thermal Shock Damage in Sandstone under Different Cooling Temperatures.\" *Journal of Rock Mechanics and Geotechnical Engineering*, 2024, doi:10.1016/j.jrmge.2024.10.017. Accessed 2026."
indexed_texts: "17"
indexed_chars: "84929"
nonempty_source_blocks: "17"
compiled_source_blocks: "17"
compiled_source_chars: "85259"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.003886"
coverage_status: "full-index"
source_signature: "89727a0c641429ffb3a6753e7c2858309682adfb"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:21:15"
---

# Spatial Variability and Quantitative Characterization of Thermal Shock Damage in Sandstone under Different Cooling Temperatures.

## One-line Summary
This study uses micro-CT scanning to quantify the spatial variability of thermal shock damage in sandstone heated to 600°C and cooled in water at 20°C, 60°C, and 100°C, finding that damage is most severe near the surface and significantly enhanced by the boiling phase transition at 100°C.

## Research Question
How can thermal shock damage in rock be quantitatively characterized while accounting for its spatial variability, and what are the specific effects of cooling water temperature and the boiling phase transition on this damage? [He 2024, pp. 1-1]

## Study Area / Data
Sandstone blocks were collected from a Cretaceous outcrop in Dongguan, Guangdong Province. Cylindrical specimens (Ф25 mm × 50 mm) were drilled from uniform, defect-free sections. The sandstone's primary constituents are quartz (31.6%), plagioclase (41.1%), clay minerals (26.3%, including illite and chlorite), and potassium feldspar (1%). [He 2024, pp. 3-4]

## Methods
1.  **Sample Preparation & Treatment:** Sandstone specimens were dried, heated to 600°C at 5°C/min in a muffle furnace, held for 120 minutes, and then rapidly cooled in a constant-temperature water bath at 20°C, 60°C, or 100°C for 60 minutes. [He 2024, pp. 3-4]
2.  **Micro-CT Scanning:** A Nano Voxel-4000 system scanned the central 15 mm height of specimens at 160 kV, 140 mA, with a 10 μm pixel size. Data underwent filtering and beam hardening correction before threshold segmentation to distinguish pores from the solid matrix. [He 2024, pp. 4-5]
3.  **Spatial Analysis:** The 3D digital core was converted into 2D data by extracting cylindrical surfaces at varying radii. Planar porosity and 2D fractal dimension (via box-counting) were calculated for slices at different radial distances from the specimen center. [He 2024, pp. 5-6]
4.  **Damage Quantification:** A critical radius (Rc) was identified where porosity transitions from decreasing to increasing. The damage factor (φP) was defined as φP = (P2 - P1)/P1, where P2 is actual porosity and P1 is the predicted porosity (from linear fitting in the unaffected zone) at a given radius. A similar approach using the fractal dimension (φFD) was also applied. [He 2024, pp. 10-11]

## Key Findings
1.  Thermal shock damage is spatially variable, confined to a shallow depth beneath the surface, with severity increasing near the boundary. The critical depth of damage (LD) was largest for 100°C water (26.23% of specimen radius), followed by 20°C (14.754%) and 60°C (9.836%). [He 2024, pp. 17-17]
2.  Cooling in 100°C boiling water caused substantially more thermal shock damage than cooling in 20°C or 60°C water. This is attributed to the boiling phase transition, which significantly enhances the convective heat transfer coefficient. [He 2024, pp. 1-1, 14-15]
3.  For the entire specimen, damage from the heating stage (Dh) is significantly greater than damage from the thermal shock cooling stage (Dc). However, near the boundary, thermal shock damage can exceed heating damage, especially at 100°C. [He 2024, pp. 15-17]
4.  The influence of thermal shock diminishes as specimen size increases, as the proportion of the damaged area relative to the total area decreases. [He 2024, pp. 15-15]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Volumetric porosity increased from 8.093% (untreated) to 11.373%, 11.018%, and 11.525% after cooling in 20°C, 60°C, and 100°C water, respectively. | [He 2024, pp. 4-5] | Sandstone heated to 600°C. | The increase for 100°C cooling was highest. |
| The 3D fractal dimension increased from 2.578 (untreated) to 2.644, 2.631, and 2.651 after cooling in 20°C, 60°C, and 100°C water, respectively. | [He 2024, pp. 5-6] | Sandstone heated to 600°C. | Pattern mirrors porosity changes. |
| Maximum planar porosity at the specimen boundary was 12.056%, 11.487%, and 14.635% for 20°C, 60°C, and 100°C cooling, respectively. | [He 2024, pp. 6-9] | Sandstone heated to 600°C. | 100°C cooling produced the highest boundary porosity. |
| Paired sample t-tests showed statistically significant differences in porosity between 100°C and 60°C cooling (P=0.0048) and between 100°C and 20°C cooling (P=0.017) in the thermal shock damage zone. | [He 2024, pp. 6-9] | Radii greater than the critical radius. | Confirms the distinct effect of 100°C cooling. |
| The convective heat transfer coefficient for boiling water (h2) is at least an order of magnitude greater than for water at ambient temperature (h1). | [He 2024, pp. 14-15] | Citing reference data. | Explains the enhanced damage at 100°C. |
| The calculated relative temperature gradients for 20°C, 60°C, and 100°C cooling were in the ratio 1.074 : 1 : (2.405 to 168.35). | [He 2024, pp. 14-15] | Based on heat transfer theory. | The large range for 100°C reflects the variable convective coefficient during boiling. |
| The total change in porosity (ΔP) due to thermal shock was 504.277, 359.247, and 2507.441 for 20°C, 60°C, and 100°C cooling, respectively. | [He 2024, pp. 10-11] | Integrated over the thermal shock damage zone. | Quantifies cumulative damage. |

## Limitations
1.  The sampling method (extracting cylindrical surfaces) somewhat overlooks information regarding radial pore connectivity, which is critical for permeability analysis. [He 2024, pp. 15-15]
2.  The study focuses on a single preheating temperature (600°C) and a specific sandstone type. Generalizability to other rock types and temperature ranges requires further investigation. [He 2024, pp. 3-4]
3.  The method assumes that the spatial distribution of pores in sandstone at high temperature (600°C) is uniform, which is inferred but not directly measured. [He 2024, pp. 10-11]

## Assumptions / Conditions
1.  The sandstone specimens are homogeneous and isotropic in their initial state. [He 2024, pp. 3-4]
2.  A heating rate of 5°C/min does not induce significant fractures due to temperature gradients, implying uniform heating damage. [He 2024, pp. 10-11]
3.  The thermal shock damage zone is defined as the region from the critical radius (Rc) to the specimen's outer boundary. [He 2024, pp. 10-11]
4.  The influence of thermal radiation is negligible compared to heat conduction and convection during the cooling process. [He 2024, pp. 14-15]

## Key Variables / Parameters
*   **Cooling Water Temperature (T_water):** 20°C, 60°C, 100°C.
*   **Preheating Temperature:** 600°C.
*   **Planar Porosity (P_s):** Ratio of pore area to total area on a 2D slice.
*   **Volume Porosity (P_v):** Ratio of pore volume to total volume in the 3D digital core.
*   **Fractal Dimension (FD):** Quantifies pore network complexity; 2D FD for slices, 3D FD for the whole core.
*   **Critical Radius (R_c):** Radius where porosity transitions from decreasing to increasing, marking the inner boundary of the thermal shock damage zone.
*   **Critical Depth of Thermal Shock Damage (L_D):** Distance from the specimen surface to the critical radius (L_D = R_max - R_c).
*   **Damage Factor (φ_P, φ_FD):** Relative change in porosity or fractal dimension due solely to thermal shock.

## Reusable Claims
1.  **Condition:** For sandstone preheated to 600°C and cooled in water. **Claim:** Thermal shock damage is spatially heterogeneous, with the most severe damage occurring near the convective heat transfer boundary. **Limitation:** The exact depth of the damage zone depends on cooling conditions and rock properties. [He 2024, pp. 1-1, 10-11]
2.  **Condition:** When comparing cooling media at different temperatures. **Claim:** The boiling phase transition of the cooling medium (e.g., water at 100°C) causes a disproportionate increase in thermal shock damage compared to non-boiling conditions, due to a significant increase in the convective heat transfer coefficient. **Limitation:** The magnitude of the coefficient increase is highly variable. [He 2024, pp. 14-15]
3.  **Condition:** For the entire rock specimen. **Claim:** The cumulative damage from the high-temperature heating stage is greater than the cumulative damage from the subsequent thermal shock cooling stage. **Limitation:** This relationship reverses near the specimen boundary under intense cooling conditions (e.g., boiling water). [He 2024, pp. 15-17]
4.  **Condition:** For geometrically similar specimens. **Claim:** The overall impact of thermal shock on a specimen diminishes as its size increases, because the proportion of the damaged surface zone relative to the total volume decreases. [He 2024, pp. 15-15]

## Candidate Concepts
*   [[Thermal shock damage]]
*   [[Spatial variability]]
*   [[Micro-CT scanning]]
*   [[Porosity]]
*   [[Fractal dimension]]
*   [[Convective heat transfer coefficient]]
*   [[Phase transition]]
*   [[Critical depth]]
*   [[Damage factor]]

## Candidate Methods
*   [[Micro-CT image analysis]]
*   [[Box-counting fractal dimension]]
*   [[Spatial gradient analysis]]
*   [[Paired sample t-test]]
*   [[Heat transfer theory modeling]]

## Connections To Other Work
*   Builds on the concept of spatial distribution gradient of damage introduced by Fan et al. (2020) for granite, but applies it to porous sandstone with a more refined sampling method. [He 2024, pp. 2-3]
*   Addresses the limitation of traditional damage indices (e.g., based on wave velocity or Young's modulus) that cannot separate heating damage from thermal shock damage and ignore spatial variability. [He 2024, pp. 1-2]
*   Corroborates findings from Kang et al. (2021) that heating causes more overall damage than thermal shock, but refines the conclusion by incorporating spatial analysis. [He 2024, pp. 15-17]
*   Aligns with studies showing liquid nitrogen causes more severe thermal shock than water or air, by demonstrating that the boiling phase transition of water also drastically increases damage. [He 2024, pp. 2-3]

## Open Questions
1.  How does the spatial variability of thermal shock damage influence the evolution of permeability and fluid flow pathways in rock?
2.  Can the proposed quantitative characterization method be reliably applied to other rock types (e.g., granite, limestone) with different mineralogies and pore structures?
3.  What is the precise quantitative relationship between the convective heat transfer coefficient during boiling and the resulting thermal shock damage parameters?
4.  How do cyclic thermal shock treatments affect the progressive development of spatial damage patterns?

## Source Coverage
All 17 non-empty indexed fragments were processed. The compiled source blocks total 17, with a compiled character count of 85,259, achieving a coverage ratio of 1.003886 by characters relative to the indexed texts. The coverage status is full-index.
