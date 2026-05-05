---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2000-nanjo-spatial-distribution-of-aftershocks-and-the-fractal-structure-of-active-fault-systems"
title: "Spatial Distribution of Aftershocks and the Fractal Structure of Active Fault Systems."
status: "draft"
source_pdf: "data/papers/Spatial distribution of aftershocks and the fractal structure of active fault systems.pdf"
collections:
citation: "Nanjo, Kazuyoshi, and Hiroyuki Nagahama. \"Spatial Distribution of Aftershocks and the Fractal Structure of Active Fault Systems.\" *Pure and Applied Geophysics*, vol. 157, 2000, pp. 575-588."
indexed_texts: "7"
indexed_chars: "32884"
nonempty_source_blocks: "7"
compiled_source_blocks: "7"
compiled_source_chars: "33037"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004653"
coverage_status: "full-index"
source_signature: "785f97e106b515d0de4db27be4a59e1ae506a264"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:34:33"
---

# Spatial Distribution of Aftershocks and the Fractal Structure of Active Fault Systems.

## One-line Summary
This study finds a positive correlation between the fractal dimension of aftershock spatial distributions and the fractal dimension of pre-existing active fault systems, suggesting that aftershock clustering is constrained by the fractal structure of the faults.

## Research Question
What is the relationship between the fractal dimension of aftershock spatial distributions and the fractal dimension of the pre-existing active fault systems in which they occur? [Nanjo 2000, pp. 1-2]

## Study Area / Data
The study analyzes 14 aftershock sequences following large earthquakes in Japan. Earthquake data are from the 'SEIS-PC' file, including events with magnitude M ≥ M0. Data on active faults are from 'Active Faults in Japan', which defines faults active during the Quaternary. Active submarine faults within aftershock regions were also included. [Nanjo 2000, pp. 5-7]

## Methods
1.  **Fractal dimension of aftershock spatial distribution (D2):** Estimated using the two-point correlation integral C(l) for epicentral distributions. D2 is the slope of the log-log plot of C(l) vs. distance l. [Nanjo 2000, pp. 7-10]
2.  **Fractal dimension of active fault systems (D0):** Estimated using the box-counting method. D0 is the slope of the log-log plot of the number of boxes N(r) vs. box size r needed to cover the fault system. [Nanjo 2000, pp. 7-10]
3.  **Aftershock definition:** Events in swarms around the main shock, tentatively within the next 1000 days. The aftershock region is defined as the smallest rectangle containing all aftershock epicenters. [Nanjo 2000, pp. 5-7]

## Key Findings
1.  Epicentral distributions of aftershocks for 12 of the 14 sequences exhibit fractal properties, with D2 values ranging from 1.68 to 1.94. [Nanjo 2000, pp. 7-10]
2.  The pre-existing active fault systems in the 14 aftershock regions exhibit fractal behavior, with D0 values ranging from 0.86 to 1.48. [Nanjo 2000, pp. 7-10]
3.  Excluding two sequences, a positive correlation is found between D2 and D0, expressed as D2 = (0.72 ± 0.02)D0 + (0.91 ± 0.02). This indicates that aftershock distributions become less clustered (higher D2) with increasing fractal dimension of the active fault system (higher D0). [Nanjo 2000, pp. 10-12]
4.  The correlation between D2 and D0 shows no dependence on the magnitude of the main shock. [Nanjo 2000, pp. 10-12]
5.  The results support the implication from a theoretical model that fractal properties of aftershocks are constrained by the fractal structure of pre-existing fracture systems. [Nanjo 2000, pp. 12-13]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Positive correlation between D2 and D0: D2 = (0.72 ± 0.02)D0 + (0.91 ± 0.02). | [Nanjo 2000, pp. 10-12] | Excludes Tottori and Eastern Tottori prefecture sequences due to low reliability. | Correlation is independent of main-shock magnitude. |
| Estimated D2 values range from 1.68 to 1.94 for 12 aftershock sequences. | [Nanjo 2000, pp. 7-10] | Epicentral distributions of aftershocks. | Two sequences (Central Gifu, Eastern Yamanashi) did not show scale invariance. |
| Estimated D0 values range from 0.86 to 1.48 for 14 active fault systems. | [Nanjo 2000, pp. 7-10] | Active fault systems within defined aftershock regions. | Maximum D0 (1.48) is close to the reported upper limit of ~1.5 for rock fracture geometry. |
| The correlation supports the implication of Hirata's (1986) model. | [Nanjo 2000, pp. 12-13] | Model where aftershocks are produced by a random walk on a pre-existing fracture system. | Model directly connects the Omori exponent p to the fractal dimension of the fracture system. |

## Limitations
1.  Two aftershock sequences (Central Gifu and Eastern Yamanashi) did not exhibit scale invariance, so D2 could not be estimated. [Nanjo 2000, pp. 7-10]
2.  The definition of an aftershock varies among investigators; this study uses a specific temporal and spatial definition. [Nanjo 2000, pp. 5-7]
3.  The study is limited to aftershock sequences in Japan. [Nanjo 2000, pp. 5-7]
4.  The reliability of D2 estimates for the excluded Tottori and Eastern Tottori sequences was lower due to small aftershock numbers. [Nanjo 2000, pp. 10-12]

## Assumptions / Conditions
1.  Aftershocks are defined as events in swarms around the main shock within 1000 days. [Nanjo 2000, pp. 5-7]
2.  The aftershock region is approximated as the smallest rectangle containing all aftershock epicenters. [Nanjo 2000, pp. 5-7]
3.  The observable active fault systems are representative of the pre-existing fracture systems influencing aftershock distribution. [Nanjo 2000, pp. 12-13]
4.  The active fault systems exhibit statistical self-similarity (fractal structure) over the analyzed scale range. [Nanjo 2000, pp. 7-10]

## Key Variables / Parameters
*   **D2:** Correlation dimension of aftershock spatial distribution. [Nanjo 2000, pp. 7-10]
*   **D0:** Box-counting (capacity) dimension of the active fault system. [Nanjo 2000, pp. 7-10]
*   **p:** Exponent in the modified Omori formula for aftershock decay. [Nanjo 2000, pp. 1-2]
*   **b:** Exponent in the Gutenberg-Richter relation for aftershock size distribution. [Nanjo 2000, pp. 1-2]

## Reusable Claims
*   The fractal dimension of aftershock spatial distribution (D2) is positively correlated with the fractal dimension of the pre-existing active fault system (D0), indicating that aftershock clustering is constrained by the fault system's fractal structure. [Nanjo 2000, pp. 10-12]
*   The relationship between D2 and D0 is scale-invariant with respect to the main-shock magnitude. [Nanjo 2000, pp. 10-12]
*   If the fractal dimension of the active fault system reaches its upper limit (~1.5), the aftershock distribution would approach a completely random and unpredictable state (D2 ≈ 2.0). [Nanjo 2000, pp. 12-13]

## Candidate Concepts
*   [[fractal dimension]]
*   [[correlation integral]]
*   [[box-counting method]]
*   [[aftershock]]
*   [[active fault system]]
*   [[self-similarity]]
*   [[modified Omori formula]]
*   [[Gutenberg-Richter relation]]

## Candidate Methods
*   [[two-point correlation integral]]
*   [[box-counting procedure]]

## Connections To Other Work
*   Builds on and supports the theoretical model of Hirata (1986), which derived the modified Omori formula from a random walk on a pre-existing fracture system. [Nanjo 2000, pp. 1-2, 12-13]
*   Extends the findings of Nanjo et al. (1998), which found correlations between p, b, and D0. [Nanjo 2000, pp. 2-5, 12-13]
*   Relates to discussions on crustal heterogeneity by Mogi (1962, 1967) and irregularities of stress/strength by Yoshida and Mikami (1986) and Mikumo and Miyatake (1979). [Nanjo 2000, pp. 12-13]
*   Connects to the self-organized criticality model of earthquakes by Ito and Matsuzaki (1990), which incorporated Enya's (1901) idea. [Nanjo 2000, pp. 1-2, 12-13]

## Open Questions
*   Could foreshock cluster patterns (e.g., doughnut patterns) be related to the fractal structures of active fault systems? [Nanjo 2000, pp. 12-13]
*   Can the relationship between aftershock/foreshock patterns and fault fractals be used for practical earthquake prediction? [Nanjo 2000, pp. 12-13]

## Source Coverage
All 7 non-empty indexed fragments were processed. The compiled source contains 33,037 characters from the original 32,884 indexed characters, achieving a coverage ratio of 1.004653 by characters and 1.0 by blocks. The coverage status is full-index.
