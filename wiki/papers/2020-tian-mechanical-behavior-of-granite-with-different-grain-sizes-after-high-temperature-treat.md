---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-tian-mechanical-behavior-of-granite-with-different-grain-sizes-after-high-temperature-treat"
title: "Mechanical Behavior of Granite with Different Grain Sizes After High-Temperature Treatment by Particle Flow Simulation."
status: "draft"
source_pdf: "data/papers/Mechanical Behavior of Granite with Different Grain Sizes After High-Temperature Treatment by Particle Flow Simulation.pdf"
collections:
citation: "Tian, Wen-Ling, et al. “Mechanical Behavior of Granite with Different Grain Sizes After High-Temperature Treatment by Particle Flow Simulation.” *Rock Mechanics and Rock Engineering*, vol. 53, 2020, pp. 1791–1807. doi:10.1007/s00603-019-02005-1."
indexed_texts: "12"
indexed_chars: "55918"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "55442"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.991488"
coverage_status: "full-index"
source_signature: "dd95cf2fa549a3d3318d7f2304209bf1de6bf41e"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:32:20"
---

# Mechanical Behavior of Granite with Different Grain Sizes After High-Temperature Treatment by Particle Flow Simulation.

## One-line Summary
This study uses a 2D particle flow code (PFC2D) cluster model to simulate and analyze how grain size influences the mechanical behavior and crack evolution of granite after high-temperature treatment, finding that coarse-grained granite exhibits more visible macro-cracks but a lower reduction in strength compared to fine-grained granite.

## Research Question
How does grain size affect the mechanical behavior, crack distribution, and failure modes of granite specimens after exposure to high temperatures, and what are the implications for the selection of granite as a host rock for high-level radioactive waste repositories? [Tian 2020, pp. 1-2]

## Study Area / Data
The granite simulated was excavated from Quanzhou City, Fujian Province, China. [Tian 2020, pp. 4-6] The numerical specimen dimensions were 160 mm in height and 80 mm in width. The particle radius was uniformly distributed between 0.3 and 0.48 mm, generating approximately 22,501 particles. [Tian 2020, pp. 3-4] The mineral composition, based on X-ray diffraction (XRD), was calcite (42.9%), illite (11.4%), biotite (23%), and quartz (22.7%). [Tian 2020, pp. 3-4]

## Methods
A cluster model in PFC2D was used, where a cluster is a set of adjacent bonded particles. The cluster size was controlled by the parameter Sc (maximum number of particles in a cluster), with values of 5, 10, 15, and 20 used to represent different grain sizes. [Tian 2020, pp. 2-3] The heating process was simulated by incrementing temperature uniformly by 5 °C per step until equilibrium. The phase transition of quartz at 573 °C was simulated by expanding particle radius by a factor of 1.0046 upon heating and shrinking by 0.9954 upon cooling. [Tian 2020, pp. 3-4] Micro-parameters were calibrated using a trial-and-error method to match the macro-behavior (stress-strain curves, strength, elastic modulus) of experimental granite at room temperature and after heating. Intra-cluster bond strength was set to double the inter-cluster strength. [Tian 2020, pp. 3-4]

## Key Findings
1.  Grain size significantly affects crack distribution after heating. Macro-cracks are more easily observed in coarse-grained granite (larger Sc) specimens after high-temperature treatment, while the number of inter-cracks decreases with increasing grain size. [Tian 2020, pp. 6-9]
2.  When temperature T ≥ 600 °C, no main cracks were observed in compressed specimens; ultimate failure was dominated by thermally induced cracks, and isolated grains could be seen in coarse-grained specimens. [Tian 2020, pp. 9-10]
3.  The reduction in uniaxial compressive strength (σs) and elastic modulus (E) due to heating was lower for coarse-grained granite specimens than for fine-grained specimens at the same temperature. [Tian 2020, pp. 10-12]
4.  During compression, cracks propagate more easily along grain boundaries. In fine-grained specimens, macro-crack initiation and propagation were observed, while in coarse-grained specimens, failure occurred via coalescence of thermally induced cracks. [Tian 2020, pp. 12-15]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Macro-cracks are observed more easily in coarse-grained specimens after thermal treatment. | [Tian 2020, pp. 6-9] | T = 300 °C to 600 °C, Sc = 5 vs. Sc = 20 | Longer grain boundaries provide paths for crack propagation. |
| The number of inter-granular cracks decreases with increasing grain size. | [Tian 2020, pp. 6-9] | Uncompressed specimens, T = 150 °C to 900 °C | Quantitative data from micro-crack counting. |
| At T ≥ 600 °C, ultimate failure modes are dominated by thermally induced cracks. | [Tian 2020, pp. 9-10] | Compressed specimens, T ≥ 600 °C | No main cracks observed; isolated grains in coarse granite. |
| Reduction in uniaxial compressive strength is lower for coarse-grained granite. | [Tian 2020, pp. 10-12] | T = 300 °C to 900 °C, Sc = 5, 10, 15, 20 | e.g., at T=600°C, reduction is 66.2% for Sc=5 and 58.2% for Sc=20. |
| Stress-strain curves show a sudden drop after peak for T ≤ 450 °C, but a gradual decrease for T > 600 °C. | [Tian 2020, pp. 4-6] | Experimental and numerical results | Behavior change linked to thermal damage level. |
| Tensile force concentrates at tips of thermally induced cracks during loading. | [Tian 2020, pp. 12-15] | Specimens heated to 450 °C, Sc=5 and Sc=20 | Observed in parallel bond force field evolution. |

## Limitations
The study uses a 2D numerical model (PFC2D), which may not fully capture all three-dimensional rock behaviors. [Tian 2020, pp. 2-3] The model assumes temperature changes uniformly and sufficiently quickly to minimize thermal shock, which may differ from some experimental conditions. [Tian 2020, pp. 3-4] The calibration process is iterative and may not perfectly match all experimental data points. [Tian 2020, pp. 3-4] The model does not consider natural defects within grains, which are present in real rock and increase with grain size. [Tian 2020, pp. 15-15]

## Assumptions / Conditions
1.  Temperature changes uniformly and over a sufficiently short time to minimize thermal shock. [Tian 2020, pp. 3-4]
2.  The phase transition of quartz at 573 °C is simulated by a specific radius expansion/contraction factor. [Tian 2020, pp. 3-4]
3.  Intra-cluster bond strength is set to double the inter-cluster strength to simplify calibration. [Tian 2020, pp. 3-4]
4.  The mineral content and their linear thermal expansion coefficients are fixed based on XRD results and literature. [Tian 2020, pp. 3-4]

## Key Variables / Parameters
-   **Temperature (T):** Ranged from 25 °C (room temperature) to 900 °C. [Tian 2020, pp. 4-6]
-   **Grain Size (Sc):** Represented by cluster size parameter Sc (5, 10, 15, 20). [Tian 2020, pp. 3-4]
-   **Uniaxial Compressive Strength (σs):** Measured in MPa. [Tian 2020, pp. 10-12]
-   **Elastic Modulus (E):** Measured in GPa. [Tian 2020, pp. 10-12]
-   **Micro-crack Number:** Total, inter-granular, and intra-granular cracks counted before and after compression. [Tian 2020, pp. 6-9, 9-10]
-   **Micro-parameters:** Particle effective modulus (Ec), stiffness ratio (kn/ks), bond strengths (σn, σs, σbn, σbs), etc. [Tian 2020, pp. 4-6]

## Reusable Claims
1.  Increasing grain size leads to longer grain boundaries, providing paths for crack propagation, resulting in more observable macro-cracks in coarse-grained granite after high-temperature treatment. [Tian 2020, pp. 6-9]
2.  The number of thermally induced inter-granular cracks in granite decreases with increasing grain size, while the number of intra-granular cracks increases. [Tian 2020, pp. 6-9]
3.  For granite heated to temperatures ≥ 600 °C, the ultimate failure under compression is dominated by the coalescence of pre-existing thermally induced cracks rather than the initiation of new main cracks. [Tian 2020, pp. 9-10]
4.  Coarse-grained granite exhibits a smaller percentage reduction in uniaxial compressive strength after high-temperature treatment compared to fine-grained granite, due to the greater prominence of inter-locking and the smaller proportion of strength-reducing inter-cracks. [Tian 2020, pp. 10-12, 15-15]
5.  In numerical simulations without considering natural grain defects, uniaxial compressive strength increases with increasing grain size when micro-parameters are held constant. [Tian 2020, pp. 15-15]

## Candidate Concepts
-   [[thermal treatment]]
-   [[grain size effect]]
-   [[particle flow code]]
-   [[micro-crack distribution]]
-   [[uniaxial compressive strength]]
-   [[elastic modulus]]
-   [[high-level radioactive waste disposal]]
-   [[thermal damage]]
-   [[crack coalescence]]
-   [[inter-granular crack]]
-   [[intra-granular crack]]

## Candidate Methods
-   [[cluster model in PFC2D]]
-   [[numerical simulation of thermal cracking]]
-   [[micro-parameter calibration]]
-   [[uniaxial compression test simulation]]

## Connections To Other Work
The study references and compares its findings with several experimental works:
-   Shao et al. (2014, 2015) on Strathbogie granite with different grain sizes. [Tian 2020, pp. 2-3, 6-9]
-   Zhao et al. (2018) on the Brazilian tensile strength of granite with different grain size distributions. [Tian 2020, pp. 2-3, 10-12]
-   Huang et al. (2017) on granite containing pre-existing holes after high-temperature treatment. [Tian 2020, pp. 4-6]
-   Yang et al. (2017, 2018) on the failure mechanical behavior of granite after high-temperature treatment. [Tian 2020, pp. 4-6, 6-9]
-   Eberhardt et al. (1999) on the effects of grain size on stress-induced fracture thresholds. [Tian 2020, pp. 15-15]
-   Zhao (2016) on using particle mechanics to simulate thermally induced cracks. [Tian 2020, pp. 2-3]

## Open Questions
1.  How would a 3D cluster model affect the simulation results compared to the 2D model used? [Not confirmed by source]
2.  What is the quantitative effect of natural intra-granular defects (which increase with grain size) on the strength reduction observed experimentally? [Tian 2020, pp. 15-15]
3.  How do variations in mineral composition beyond the specific granite studied influence the grain size effect on thermal-mechanical behavior? [Not confirmed by source]

## Source Coverage
All non-empty indexed fragments were processed. The coverage audit indicates a coverage ratio by blocks of 1.0 and by characters of 0.991488, confirming full-index coverage. The compiled source blocks total 12, with 55,442 characters compiled from 55,918 indexed characters.
