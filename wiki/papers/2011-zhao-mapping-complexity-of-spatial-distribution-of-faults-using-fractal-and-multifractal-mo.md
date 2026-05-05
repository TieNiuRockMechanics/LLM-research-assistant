---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2011-zhao-mapping-complexity-of-spatial-distribution-of-faults-using-fractal-and-multifractal-mo"
title: "Mapping Complexity of Spatial Distribution of Faults Using Fractal and Multifractal Models: Vectoring towards Exploration Targets."
status: "draft"
source_pdf: "data/papers/Mapping complexity of spatial distribution of faults using fractal and multifractal models vectoring towards exploration targets.pdf"
collections:
citation: "Zhao, Jiangnan, et al. \"Mapping Complexity of Spatial Distribution of Faults Using Fractal and Multifractal Models: Vectoring towards Exploration Targets.\" *Computers & Geosciences*, vol. 37, no. 12, 2011, pp. 1958-1966."
indexed_texts: "8"
indexed_chars: "38210"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "38374"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004292"
coverage_status: "full-index"
source_signature: "7bed65eedbe83a8642b1813aaf3d8c013430e24a"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T01:05:00"
---

# Mapping Complexity of Spatial Distribution of Faults Using Fractal and Multifractal Models: Vectoring towards Exploration Targets.

## One-line Summary
Fractal and multifractal analyses of fault spatial distributions in the Gejiu mining district, China, reveal that complexity indices correlate with Sn orebody sizes and can vector towards exploration targets.

## Research Question
The study investigates whether fractal and multifractal models can effectively characterize the complexity of fault spatial distributions and whether this complexity relates to the distribution and size of mineral resources, specifically Sn deposits.

## Study Area / Data
The study focuses on the eastern part of the Gejiu mining area, Yunnan Province, China, which contains world-class Sn and Cu deposits. The area is divided into four Sn fields: Malage, Gaosong, Laochang, and Kafang. The primary data consists of mapped faults (based on 1:50,000 scale maps) covering approximately 600 km², which are mainly NW-trending and NE-trending sets [Zhao 2011, pp. 1-2].

## Methods
The methodology employs fractal and multifractal analyses:
1.  **Fractal Analysis (Box-Counting Method):** Fault maps are converted into raster maps with varying cell sizes (r). The cumulative number of cells containing faults, N(r), is counted. A log-log plot of N(r) versus r is constructed, and the fractal dimension (D) is obtained as the slope of the linear regression, following the power-law relationship N(r) ∝ r^(-D) [Zhao 2011, pp. 2-4].
2.  **Multifractal Analysis:** The total length of faults within each cell, m(e), is used to calculate the partition function w_q(e). If multifractal, w_q(e) and cell size e follow a power-law relationship w_q(e) ∝ e^(τ(q)). The mass exponent τ(q) is used to derive the singularity index α(q) and the multifractal spectrum f(α) [Zhao 2011, pp. 2-4].
3.  **Spatial Mapping:** Fractal dimensions are calculated for 1x1 km² grid cells across the study area using box sizes of 1, 0.5, 0.25, and 0.125 km. The resulting D values are interpolated to create a contour map of fault complexity [Zhao 2011, pp. 4-6].

## Key Findings
1.  The fractal dimension (D) for all faults is 1.68, for NW-trending faults is 1.49, and for NE-trending faults is 1.42, indicating different spatial distributions [Zhao 2011, pp. 1-1].
2.  Fractal dimensions for faults in the four Sn fields are: Malage (1.38), Gaosong (1.58), Laochang (1.65), and Kafang (1.42) [Zhao 2011, pp. 1-1].
3.  A strong positive correlation exists between the fractal dimension (D) of fault distributions and the surface-projected areas of Sn orebodies (RA) and the percentage of district Sn resources (RP) [Zhao 2011, pp. 4-6].
4.  Zones with high fractal dimensions (>1.40) coincide with the surface projections of large Sn orebodies, suggesting fractal dimension maps can vector towards ore-bearing zones [Zhao 2011, pp. 6-7].
5.  Fault lengths exhibit multifractal properties. The range of the singularity index (Δα) also shows strong positive correlations with Sn deposit attributes and fault attributes [Zhao 2011, pp. 7-9].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Fractal dimension D for all faults = 1.68. | [Zhao 2011, pp. 1-1] | Eastern Gejiu mining area. | Derived from box-counting method. |
| D for NW-trending faults = 1.49; D for NE-trending faults = 1.42. | [Zhao 2011, pp. 1-1] | Eastern Gejiu mining area. | Shows different spatial distributions for different fault sets. |
| D values for Sn fields: Malage=1.38, Gaosong=1.58, Laochang=1.65, Kafang=1.42. | [Zhao 2011, pp. 1-1] | Individual Sn fields within Gejiu. | Self-similar within scale interval of 200-1000 m. |
| Strong positive correlation between D and surface-projected areas of Sn orebodies (RA). | [Zhao 2011, pp. 4-6] | Four Sn fields in Gejiu district. | Pearson's correlation coefficient = 0.95. |
| Sn orebodies at depth coincide with zones of high fractal dimensions (>1.40) at the surface. | [Zhao 2011, pp. 6-7] | Eastern Gejiu mining area. | Based on overlay of orebody projections and D contour map. |
| All values of t''(1) are less than 0, indicating multifractal distribution patterns. | [Zhao 2011, pp. 7-9] | Whole study area and each Sn field. | t''(1) is a measure of irregularity. |
| Strong positive correlation between range of singularity index (Δα) and RA. | [Zhao 2011, pp. 7-9] | Four Sn fields in Gejiu district. | Pearson's correlation coefficient = 0.86. |

## Limitations
The study is based on a single case study (Gejiu district). The fault map used has a roughly uniform level of detail, but mapping detail can vary in other areas. The fractal analysis is performed in 2D space, which may not fully capture 3D fault connectivity [Zhao 2011, pp. 2-4].

## Assumptions / Conditions
1.  The mapped faults are representative of the true fault network in the study area.
2.  The spatial distribution of faults is self-similar or invariant within the analyzed scale interval (200-1000 m for Sn fields) [Zhao 2011, pp. 4-6].
3.  High fractal dimensions indicate high interconnectivity of fault pathways, which is favorable for fluid flow and mineralization [Zhao 2011, pp. 4-6].

## Key Variables / Parameters
-   **Fractal Dimension (D):** Quantifies the complexity of the spatial distribution of faults. Ranges from 1 to 2 in 2D.
-   **Singularity Index (α):** Derived from multifractal analysis, measures local irregularity.
-   **Range of Singularity Index (Δα = α_max - α_min):** Depicts degrees of local irregularity and complexity.
-   **t''(1):** A parameter from multifractal analysis; values < 0 indicate multifractal distribution.

## Reusable Claims
-   In the Gejiu district, zones with high fractal dimensions (>1.40) of fault spatial distributions are prospective for concealed Sn orebodies [Zhao 2011, pp. 6-7].
-   The fractal dimension of fault spatial distributions correlates positively with the surface-projected area of Sn orebodies, suggesting it can indirectly reflect orebody size at depth [Zhao 2011, pp. 6-7].
-   The range of the multifractal singularity index (Δα) is positively correlated with Sn resource attributes and can be used as a vector towards ore-bearing zones [Zhao 2011, pp. 7-9].

## Candidate Concepts
-   [[Fractal dimension]]
-   [[Multifractal analysis]]
-   [[Fault complexity]]
-   [[Spatial distribution]]
-   [[Mineral prospectivity mapping]]
-   [[Fluid pathway connectivity]]

## Candidate Methods
-   [[Box-counting method]]
-   [[Multifractal modeling]]
-   [[Singularity index analysis]]
-   [[Contour mapping of fractal dimensions]]

## Connections To Other Work
The study builds on prior work applying fractal geometry to fault systems (e.g., Hirata, 1989; Walsh and Watterson, 1993) and mineral prospectivity mapping (e.g., Carranza, 2008; Zuo et al., 2009b). It specifically extends the use of multifractal models for fault analysis, as suggested by Cowie et al. (1995) and Agterberg et al. (1996) [Zhao 2011, pp. 1-1].

## Open Questions
-   How do the 3D connectivity and geometry of faults, beyond their 2D surface traces, influence the fractal and multifractal measures and their relationship to mineralization?
-   Can the observed correlations between fault complexity and Sn resources in Gejiu be generalized to other mineral districts or deposit types?

## Source Coverage
All non-empty indexed fragments were processed. The compilation is based on 8 indexed fragments containing 38,210 characters. The compiled source blocks total 8, with 38,374 characters, resulting in a coverage ratio by blocks of 1.0 and by characters of 1.004292. The coverage status is full-index.
