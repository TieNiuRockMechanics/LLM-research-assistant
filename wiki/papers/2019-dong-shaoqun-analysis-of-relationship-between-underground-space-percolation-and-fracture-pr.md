---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-dong-shaoqun-analysis-of-relationship-between-underground-space-percolation-and-fracture-pr"
title: "Analysis of Relationship between Underground Space Percolation and Fracture Properties."
status: "draft"
source_pdf: "data/papers/2019 - 地下空间逾渗与裂缝属性的关系分析.pdf"
collections:
  - "大论文-离散裂缝网络"
citation: "Dong Shaoqun, et al. \"Analysis of Relationship between Underground Space Percolation and Fracture Properties.\" *Earth Science Frontiers*, vol. 26, no. 3, May 2019, pp. 140-146, doi:10.13745/j.esf.sf.2019.4.22, www.earthsciencefrontiers.net.cn. Accessed 2026."
indexed_texts: "6"
indexed_chars: "26931"
nonempty_source_blocks: "6"
compiled_source_blocks: "6"
compiled_source_chars: "25764"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.956667"
coverage_status: "full-index"
source_signature: "bd0f5f049d41d69443f495e8a9c8821fba2eb18a"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:13:15"
---

# Analysis of Relationship between Underground Space Percolation and Fracture Properties.

## One-line Summary
This study establishes percolation threshold equations for 2D discrete fracture networks using direct fracture parameters (length and number) to more reliably predict network connectivity for underground space evaluation.

## Research Question
How can the connectivity of underground space fracture networks be characterized more accurately and quickly by avoiding the use of indirect characterization parameters (e.g., fractal dimension) that can lead to non-unique solutions?

## Study Area / Data
The study uses numerically simulated 2D discrete fracture network (DFN) models within a 100 m × 100 m square study area. Two types of fracture networks are analyzed: one with identical fracture lengths and another with fracture lengths following an exponential distribution. Fracture orientations are completely random [Dong 2019, pp. 3-5].

## Methods
1.  **DFN Modeling:** Fracture networks are generated using a stochastic modeling method based on a marked point process. A stationary Poisson process determines fracture center locations, and a random quantile method determines fracture properties (orientation via von-Mises distribution, length via exponential distribution) [Dong 2019, pp. 1-3].
2.  **Percolation Detection:** Percolation is defined as the existence of a cluster of intersecting fractures connecting two opposite boundaries (A and B) of the study area. Detection uses a fast method based on bounding box and sweeping line (BBSL) to identify intersecting fracture clusters [Dong 2019, pp. 3-5].
3.  **Threshold Equation Derivation:** For each network type, numerous simulations are run with varying fracture numbers (n) and lengths (L or mean length 1/λ). The percolation probability P = N_p/N is calculated. Boundary curves for low (P≈0), medium (P≈0.5), and high (P≈1) percolation probability are extracted and fitted using nonlinear (exponential) functions to establish threshold equations [Dong 2019, pp. 3-5].
4.  **Scale Correction:** A correction factor (r_V) is introduced to apply the equations derived from the 100 m × 100 m model to different study area scales (w × w). For random orientations, r_V ≈ w/100 [Dong 2019, pp. 5-7].

## Key Findings
1.  For both identical-length and exponentially-distributed fracture networks, the percolation thresholds (Lt or L̄t) can be effectively described as a power-law function of fracture number (n), with high correlation coefficients (R² > 0.94) [Dong 2019, pp. 3-5].
2.  The derived threshold equations (Eqs. 3-8), combined with the scale correction formula (Eq. 9), can efficiently predict percolation thresholds for fracture networks at different scales, as validated by simulations with various study area sizes and fracture counts [Dong 2019, pp. 5-7].
3.  A connectivity evaluation standard (Table 2) is established based on the predicted threshold values (f1(n), f2(n), f3(n)) to classify fracture network connectivity as "poor," "fair," "good," or "very good" [Dong 2019, pp. 5-7].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Percolation threshold equations for identical-length networks: Lt = 113.456 × n^(-0.392) (low prob.), 257.822 × n^(-0.516) (mid prob.), 450.983 × n^(-0.577) (high prob.). | [Dong 2019, pp. 3-5] | 2D DFN, 100m x 100m area, random orientation, identical fracture length. | Correlation coefficients: 0.983, 0.996, 0.991. |
| Percolation threshold equations for exponential-length networks: L̄t = 50.365 × n^(-0.337) (low prob.), 238.022 × n^(-0.554) (mid prob.), 708.772 × n^(-0.690) (high prob.). | [Dong 2019, pp. 5-7] | 2D DFN, 100m x 100m area, random orientation, exponential fracture length. | Correlation coefficients: 0.942, 0.993, 0.992. |
| Scale correction factor for random orientation: r_V ≈ w/100, where w is the side length of the new study area. | [Dong 2019, pp. 5-7] | Derived from numerical simulations for w from 1m to 10000m. | The corrected length U = L̄ × r_V. |
| Validation of prediction equations shows high correlation (R² ≥ 0.993) between predicted and simulated percolation thresholds for different scales (w=50, 500, 5000m) and fracture numbers. | [Dong 2019, pp. 5-7] | Applied Eqs. 3-8 with correction Eq. 9. | Demonstrates the equations' effectiveness across scales. |
| Connectivity evaluation standard: "Poor" (U < f1(n)), "Fair" (f1(n) ≤ U < f2(n)), "Good" (f2(n) ≤ U < f3(n)), "Very good" (U ≥ f3(n)). | [Dong 2019, pp. 5-7] | Based on predicted threshold functions f1, f2, f3. | Provides a practical tool for assessing underground space stability. |

## Limitations
1.  The study focuses exclusively on 2D discrete fracture network models.
2.  Fracture orientations are assumed to be completely random; the effect of preferred orientations is not addressed.
3.  The scale correction factor (r_V) is derived for random orientations and may change if fractures have a dominant orientation, which could introduce prediction errors [Dong 2019, pp. 5-7].

## Assumptions / Conditions
1.  Fracture networks are modeled as 2D discrete fracture networks (DFN) where fractures are represented as line segments.
2.  Fracture center locations follow a stationary Poisson process (uniform distribution).
3.  For the identical-length model, all fractures have the same length.
4.  For the exponential-length model, fracture lengths follow an exponential distribution.
5.  Fracture orientations are completely random (no preferred direction).
6.  The base study area for deriving equations is a 100 m × 100 m square.

## Key Variables / Parameters
-   **n**: Number of fractures in the network.
-   **L**: Length of fractures (for identical-length networks).
-   **1/λ**: Mean length of fractures (for exponential-length networks).
-   **Lt / L̄t**: Percolation threshold length (critical length or mean length).
-   **P**: Percolation probability (P = N_p/N).
-   **U**: Corrected percolation threshold length for a different scale.
-   **w**: Side length of a new study area.
-   **r_V**: Scale correction factor.

## Reusable Claims
-   Using direct fracture parameters (number and length) for nonlinear fitting can establish reliable percolation threshold equations for 2D DFNs, avoiding the non-uniqueness problem associated with indirect parameters like fractal dimension [Dong 2019, pp. 1-3].
-   The percolation threshold for 2D fracture networks with random orientation follows a power-law relationship with fracture number, regardless of whether fracture lengths are identical or exponentially distributed [Dong 2019, pp. 3-5].
-   Percolation threshold equations derived for a specific scale can be applied to other scales by incorporating a linear scale correction factor, provided fracture orientations are random [Dong 2019, pp. 5-7].

## Candidate Concepts
-   [[discrete fracture network]]
-   [[percolation threshold]]
-   [[fracture network connectivity]]
-   [[underground space]]
-   [[fracture properties]]
-   [[numerical simulation]]
-   [[scale correction]]

## Candidate Methods
-   [[nonlinear fitting]]
-   [[stochastic modeling]]
-   [[marked point process]]
-   [[bounding box and sweeping line method]]
-   [[percolation analysis]]

## Connections To Other Work
The paper builds upon and critiques the common practice of using indirect parameters like fractal dimension (D) [Dong 2019, pp. 1-3] and dimensionless density [Dong 2019, pp. 1-3] to define percolation thresholds. It references prior work on percolation in fracture networks with various properties, including exponential length distributions [Dong 2019, pp. 1-3], spatial correlation [Dong 2019, pp. 1-3], preferred orientation [Dong 2019, pp. 1-3], and arbitrary shapes [Dong 2019, pp. 1-3]. The DFN modeling approach is based on methods described in [Dong 2019, pp. 1-3] and [Dong 2019, pp. 7-7].

## Open Questions
1.  How do the percolation threshold equations and scale correction factors change for 3D fracture networks?
2.  How does a preferred fracture orientation affect the scale correction factor and the overall percolation behavior?
3.  Can the approach be extended to more complex fracture geometries (e.g., curved fractures) or non-stationary spatial distributions?

## Source Coverage
All non-empty indexed fragments were processed. The compilation used 6 source blocks containing a total of 25,764 characters, achieving a coverage ratio of 1.0 by blocks and 0.956667 by characters. The source signature is `bd0f5f049d41d69443f495e8a9c8821fba2eb18a`.
