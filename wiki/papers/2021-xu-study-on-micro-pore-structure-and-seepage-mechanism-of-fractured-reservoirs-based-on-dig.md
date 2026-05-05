---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-xu-study-on-micro-pore-structure-and-seepage-mechanism-of-fractured-reservoirs-based-on-dig"
title: "Study on Micro-Pore Structure and Seepage Mechanism of Fractured Reservoirs Based on Digital Core: Taking Buried Hill of JZ Oil Field as an Example."
status: "draft"
source_pdf: "data/papers/基于数字岩心的变质岩裂缝储层围观渗流机理研究——以JZ油田潜山为例_徐静.pdf"
collections:
citation: "Xu, Jing, et al. “Study on Micro-Pore Structure and Seepage Mechanism of Fractured Reservoirs Based on Digital Core: Taking Buried Hill of JZ Oil Field as an Example.” *Journal of Shaanxi University of Science & Technology*, vol. 39, no. 4, Aug. 2021, pp. 96-102. DOI:10.19481/j.cnki.issn2096-398x.2021.04.015. Accessed 2026."
indexed_texts: "4"
indexed_chars: "18816"
nonempty_source_blocks: "4"
compiled_source_blocks: "4"
compiled_source_chars: "17975"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.955304"
coverage_status: "full-index"
source_signature: "b06ea5a14f26922096eae212cf2beb229cf5f99a"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T11:14:49"
---

# Study on Micro-Pore Structure and Seepage Mechanism of Fractured Reservoirs Based on Digital Core: Taking Buried Hill of JZ Oil Field as an Example.

## One-line Summary
This study uses digital core technology to classify matrix reservoir space types in the JZ buried hill fractured reservoir and quantitatively characterize their microscopic seepage mechanisms through two-phase flow simulation.

## Research Question
The research addresses the lack of effective methods for studying microscopic matrix reservoir space types and seepage characteristics in buried hill fractured reservoirs, which leads to unclear understanding of key issues such as whether the matrix can produce oil [Xu 2021, pp. 1-2].

## Study Area / Data
The study focuses on the buried hill of the JZ Oil Field. Core samples were selected from wells JZ-2, JZ-5, and JZ-C3 at different depths and reservoir segments. A total of 9 samples were used for multi-scale CT scanning [Xu 2021, pp. 2-4].

## Methods
The methodology involves:
1.  **Digital Core Construction:** Using X-ray CT scanning and stereoscopic imaging to build 3D digital core models at multiple scales (full core at 0.5 mm resolution, 25 mm plug at 13 μm, and 5 mm plug at 2 μm) [Xu 2021, pp. 2-4].
2.  **Pore Network Extraction:** Applying image segmentation and the maximum ball algorithm to extract pore-throat network models from the 3D images [Xu 2021, pp. 4-7].
3.  **Property Calculation:** Calculating porosity and absolute permeability using Darcy's law and the linear Stokes equation, with a three-stage upscaling method [Xu 2021, pp. 4-7].
4.  **Seepage Simulation:** Conducting single-phase and oil-water two-phase flow simulations using a molecular dynamics method to study microscopic seepage laws and obtain relative permeability curves [Xu 2021, pp. 1-2, 4-7].

## Key Findings
1.  Based on multi-scale digital core experiments, the matrix reservoir space types in the JZ buried hill are classified into four categories: dissolution pore type, dissolution cave type, micro-fracture type, and bedrock [Xu 2021, pp. 1-2, 4-7].
2.  Two-phase flow simulations yielded relative permeability curves for each matrix type, quantitatively characterizing their microscopic seepage characteristics [Xu 2021, pp. 1-2].
3.  The pore structure and physical parameters described by digital core are basically consistent with conventional experimental results in the area [Xu 2021, pp. 1-2].
4.  Different matrix reservoir space types show significant differences in seepage characteristics. Micro-fracture type reservoirs have a smaller two-phase region and faster water phase permeability increase compared to pore and cave types [Xu 2021, pp. 4-7].
5.  Micro-fractures are identified as the main seepage channels in the matrix reservoir space [Xu 2021, pp. 7-7].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Matrix reservoir space types are divided into: dissolution pore type, dissolution cave type, micro-fracture type, and bedrock. | [Xu 2021, pp. 1-2] | Based on multi-scale digital core experiments on several cores from JZ oil field buried hill. | Classification is based on pore network model characteristics. |
| Digital core calculated porosity (2.7%~10.4%) is within the range of conventional experimental results. | [Xu 2021, pp. 4-7] | Comparison of JZ-2 well samples. | Some calculated values are lower due to sample selection bias towards denser sections and the smaller scale of digital core analysis. |
| For micro-fracture type core 1-2 (JZ-2 well), irreducible water saturation is ~0.1, and both oil and water relative permeability can reach 1.0. | [Xu 2021, pp. 4-7] | Two-phase flow simulation on a pore network model with 3.2% porosity and 2.4% connected porosity. | Oil phase permeability has a linear relationship with saturation in most regions. |
| For dissolution cave type core 4-2 (JZ-C3 well), irreducible water saturation is ~0.15, critical water saturation is ~0.4, and maximum water relative permeability is 0.2-0.25. | [Xu 2021, pp. 4-7] | Two-phase flow simulation. | The maximum oil relative permeability can reach 1.0. |
| Micro-fracture scale distribution, aperture, and fracture network structure are important factors affecting reservoir connectivity. | [Xu 2021, pp. 4-7] | Comparison of relative permeability curves from cores 1-2 and 1-4 (both micro-fracture type). | Core 1-4 has a two-phase region half that of 1-2 and an equal permeability point about 0.4 times that of 1-2. |

## Limitations
1.  The study acknowledges that the strong heterogeneity of buried hill metamorphic rock and the poor condition of retrieved cores (severe fragmentation) limit the availability of representative samples for digital core analysis [Xu 2021, pp. 4-7].
2.  The digital core method primarily reflects the physical properties of the matrix at a microscopic scale, which is smaller than the scale of conventional core experiments [Xu 2021, pp. 4-7].

## Assumptions / Conditions
1.  The seepage simulation assumes slow, incompressible, steady-state flow for absolute permeability calculation [Xu 2021, pp. 4-7].
2.  The pore network model is assumed to have geometric parameters equivalent to the real core pore space [Xu 2021, pp. 4-7].

## Key Variables / Parameters
-   **Porosity (φ):** Total, macro (φ_macro), and micro (φ_micro) porosity [Xu 2021, pp. 4-7].
-   **Absolute Permeability:** Calculated in X, Y, Z directions [Xu 2021, pp. 4-7].
-   **Relative Permeability (K_rp):** Calculated for oil and water phases from two-phase flow simulation [Xu 2021, pp. 4-7].
-   **Irreducible Water Saturation:** Varies significantly between reservoir types (e.g., ~0.1 for micro-fracture, ~0.6-0.65 for another micro-fracture, ~0.15 for dissolution cave) [Xu 2021, pp. 4-7].
-   **Pore Network Parameters:** Pore-throat radius, throat length, shape factor, tortuosity, and connectivity function [Xu 2021, pp. 4-7].

## Reusable Claims
1.  **Claim:** Digital core technology, combining multi-scale CT scanning and pore network modeling, can effectively classify complex matrix reservoir space types in fractured reservoirs. **Condition:** Applied to the JZ buried hill metamorphic rock reservoir. **Limitation:** Sample availability and representativeness are constrained by core recovery and condition.
2.  **Claim:** Two-phase flow simulation on digital pore networks can quantitatively generate relative permeability curves for different matrix types, solving the lack of experimental data for fractured reservoir matrix. **Condition:** Using a molecular dynamics method for simulation. **Limitation:** Results are specific to the simulated pore structure and fluid properties.
3.  **Claim:** The seepage characteristics of micro-fracture type matrix are distinct from pore and cave types, characterized by a smaller two-phase region and faster water permeability increase. **Condition:** Based on comparative analysis of simulated curves from JZ field samples. **Limitation:** The specific fracture geometry (scale, aperture, network) heavily influences the results.

## Candidate Concepts
-   [[digital core technology]]
-   [[fractured reservoir]]
-   [[buried hill reservoir]]
-   [[micro-pore structure]]
-   [[seepage mechanism]]
-   [[relative permeability curve]]
-   [[pore network model]]
-   [[matrix reservoir space]]
-   [[metamorphic rock reservoir]]

## Candidate Methods
-   [[CT scanning]]
-   [[stereoscopic imaging]]
-   [[image segmentation]]
-   [[maximum ball algorithm]]
-   [[molecular dynamics simulation]]
-   [[two-phase flow simulation]]
-   [[upscaling method]]

## Connections To Other Work
The paper cites prior research on the importance of buried hill fractured reservoirs as exploration targets [Xu 2021, pp. 2-4]. It positions digital core technology as an emerging numerical simulation method that has been applied to conventional clastic reservoirs and is expanding to complex reservoirs like shale, carbonate, and tight sandstone, but notes its application to complex fractured reservoirs is still limited [Xu 2021, pp. 2-4].

## Open Questions
1.  How can the digital core method be improved to better account for the extreme heterogeneity and sample damage typical of buried hill metamorphic rocks?
2.  How do the simulated relative permeability curves at the pore scale translate to effective properties for reservoir-scale simulation?
3.  What is the impact of wettability and more complex fluid interactions on the seepage mechanisms in these specific matrix types?

## Source Coverage
All four non-empty indexed fragments were processed. The compiled source blocks total 17,975 characters from an indexed total of 18,816 characters, resulting in a coverage ratio by characters of 0.955304. The coverage ratio by blocks is 1.0. The source signature is `b06ea5a14f26922096eae212cf2beb229cf5f99a`.
