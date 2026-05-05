---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2024-dong-relationship-between-box-counting-fractal-dimension-and-properties-of-fracture-network"
title: "Relationship between Box-Counting Fractal Dimension and Properties of Fracture Networks."
status: "draft"
source_pdf: "data/papers/2024 - Relationship between box-counting fractal dimension and properties of fracture networks.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Dong, Shaoqun, et al. \"Relationship between Box-Counting Fractal Dimension and Properties of Fracture Networks.\" *Unconventional Resources*, vol. 4, 2024, art. 100068. Accessed 2026."
indexed_texts: "12"
indexed_chars: "57552"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "54116"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.940297"
coverage_status: "full-index"
source_signature: "fbb5c211e3a83147398e3ba4198710d1fef49502"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:19:43"
---

# Relationship between Box-Counting Fractal Dimension and Properties of Fracture Networks.

## One-line Summary
This study uses Monte Carlo simulations and multivariate analysis to derive rational function equations that predict the box-counting fractal dimension (D) of two-dimensional fracture networks from their properties, including fracture number, length, and orientation.

## Research Question
How can the box-counting fractal dimension (D) of a fracture network be predicted from a combination of its multiple properties, such as fracture number, length, and orientation distribution?

## Study Area / Data
The study utilizes synthetic two-dimensional fracture networks generated via discrete fracture network (DFN) modeling within a square study area of 100 m × 100 m [Dong 2024, pp. 3-5]. For validation, a real fracture network from a geological outcrop is used [Dong 2024, pp. 13-14].

## Methods
The methodology involves generating a large number of synthetic fracture networks using Monte Carlo simulations of discrete fracture network (DFN) models [Dong 2024, pp. 1-2]. The box-counting method is applied to calculate the fractal dimension (D) for each network [Dong 2024, pp. 3-5]. Multivariate analysis is then employed to fit rational functions that relate D to the network's properties [Dong 2024, pp. 5-7]. Three types of DFNs are analyzed: (1) invariant fracture length and random orientation, (2) exponential fracture length and random orientation, and (3) exponential fracture length and von-Mises orientation [Dong 2024, pp. 5-7].

## Key Findings
1.  For DFNs with invariant fracture length and random orientation, the relationship between D, fracture number (n), and constant length (L) is well-described by a rational function (Eq. 6), with a correlation coefficient >0.999 and a root-mean-square error (RMSE) of 0.0152 [Dong 2024, pp. 7-9].
2.  For DFNs with exponential fracture length and random orientation, the relationship between D, n, and average length (1/λ) is captured by a rational function (Eq. 9), with a correlation coefficient >0.999 and an RMSE of 0.0141 [Dong 2024, pp. 9-10].
3.  For DFNs with exponential fracture length and von-Mises orientation, the comprehensive relationship between D, n, 1/λ, and the concentration parameter (κ) is represented by a rational function (Eq. 12), with a correlation coefficient nearly one and an RMSE of 7×10⁻⁶ [Dong 2024, pp. 10-13].
4.  Validation using a real outcrop fracture network (n=35, 1/λ=4, κ=145.18) showed the predicted D (0.99507) had a low error (e.g., 0.6% for k=10) compared to directly calculated values [Dong 2024, pp. 13-14].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Rational function (Eq. 6) predicts D from (n, L) with correlation >0.999. | [Dong 2024, pp. 7-9] | DFNs with invariant fracture length and random orientation. | Parameters: d₁=1.665, d₂=35.42, d₃=0.3603, d₄=678.1, d₅=22.43, d₆=0.1759, d₇=669.7. |
| Rational function (Eq. 9) predicts D from (n, 1/λ) with correlation >0.999. | [Dong 2024, pp. 9-10] | DFNs with exponential fracture length and random orientation. | Parameters: e₁=1.365, e₂=21.18, e₃=0.4364, e₄=122.7, e₅=17.52, e₆=0.218, e₇=209.4. |
| Rational function (Eq. 12) predicts D from (n, 1/λ, κ) with correlation nearly one. | [Dong 2024, pp. 10-13] | DFNs with exponential fracture length and von-Mises orientation. | Parameters: p₁=1.619, p₂=34.158, p₃=1.209, p₄=0.344, p₅=0.004, p₆=-0.007, p₇=507.549, p₈=23.151, p₉=1.215, p₁₀=0.169, p₁₁=0.002, p₁₂=-0.008, p₁₃=537.385. |
| D increases with fracture number (n) and average length (L or 1/λ). | [Dong 2024, pp. 5-7, 13-14] | All three DFN types analyzed. | Observed from univariate and multivariate analyses. |
| D decreases with an increase in the concentration parameter (κ). | [Dong 2024, pp. 10-11] | DFNs with von-Mises orientation. | Relationship becomes evident with multiple realizations. |
| Validation on real outcrop network (n=35, 1/λ=4, κ=145.18) yields predicted D=0.99507 with low error. | [Dong 2024, pp. 13-14] | Fracture traces from Wilson [5]. | Error was 0.6% for grid parameter k=10. |

## Limitations
1.  The derived equations (Eqs. 6, 9, 12) are approximate representations; other mathematical expressions could also describe the relationships [Dong 2024, pp. 13-14].
2.  The findings are specifically applicable to estimating fractal dimensions in DFNs characterized by high fracture density. For low-density DFNs with short fractures or small numbers, the correlation between D and properties may be weak [Dong 2024, pp. 13-14].
3.  The analysis simplifies the orientation parameter μ in the von-Mises function and focuses only on two-dimensional fracture networks [Dong 2024, pp. 13-14].
4.  The equations provide a numerical prediction but lack a physical interpretation of their parameters [Dong 2024, pp. 13-14].

## Assumptions / Conditions
1.  The relationship between multiple fracture network properties and D can be effectively fitted by a rational function [Dong 2024, pp. 5-7].
2.  The study area is a square of 100 m × 100 m [Dong 2024, pp. 3-5].
3.  Fracture length follows either a fixed value or an exponential distribution (Eq. 1) [Dong 2024, pp. 3-5].
4.  Fracture orientation follows either a random distribution or a von-Mises distribution (Eq. 2) [Dong 2024, pp. 3-5].
5.  The analysis assumes high fracture density for the derived relationships to hold [Dong 2024, pp. 13-14].

## Key Variables / Parameters
*   **D**: Box-counting fractal dimension.
*   **n**: Fracture number.
*   **L**: Constant fracture length (for invariant length models).
*   **1/λ**: Average fracture length (for exponential length models, where λ is the parameter of the exponential distribution).
*   **μ**: Mean orientation parameter in the von-Mises distribution (analogous to mean).
*   **κ**: Concentration parameter in the von-Mises distribution (analogous to inverse variance); higher κ means more similar orientations.
*   **P₂₀**: Fracture density, proportional to n (P₂₀ = n / 10⁴ for the 100m×100m area).

## Reusable Claims
1.  **Condition**: For two-dimensional discrete fracture networks with high density. **Claim**: The box-counting fractal dimension (D) can be predicted with high accuracy (correlation >0.999) from fracture number (n) and average fracture length (L or 1/λ) using a rational function. **Limitation**: The relationship weakens for low-density networks with short fractures or few fractures.
2.  **Condition**: For fracture networks with a preferential orientation described by a von-Mises distribution. **Claim**: The fractal dimension (D) decreases as the orientation concentration parameter (κ) increases. **Limitation**: This relationship is derived from numerical simulations and requires multiple realizations to be statistically evident.
3.  **Condition**: Given fracture property data (n, 1/λ, κ) from sources like core or outcrop measurements. **Claim**: The derived rational function (Eq. 12) provides an efficient method to estimate the fractal dimension, saving computational resources compared to full numerical simulation. **Limitation**: The predicted D represents an expected value for the von-Mises orientation model.

## Candidate Concepts
*   [[Fractal dimension]]
*   [[Box-counting method]]
*   [[Fracture network]]
*   [[Discrete fracture network (DFN)]]
*   [[Monte Carlo simulation]]
*   [[Multivariate analysis]]
*   [[Fracture density]]
*   [[Fracture orientation]]
*   [[von-Mises distribution]]
*   [[Percolation threshold]]
*   [[Fracture network permeability]]

## Candidate Methods
*   [[Box-counting fractal dimension calculation]]
*   [[Discrete fracture network (DFN) modeling]]
*   [[Monte Carlo simulation]]
*   [[Multivariate regression analysis]]
*   [[Rational function fitting]]

## Connections To Other Work
The paper builds on the established use of fractal dimension to analyze fracture network connectivity [Dong 2024, pp. 1-2] and permeability [Dong 2024, pp. 1-2]. It extends previous univariate analyses between D and single properties like density [Dong 2024, pp. 1-2] by introducing a multivariate approach. The DFN modeling approach follows methodologies described in prior work [Dong 2024, pp. 3-5].

## Open Questions
1.  Can analytical formulas, rather than empirical numerical equations, be derived to explain the relationships between D and fracture properties?
2.  What is the physical interpretation of the parameters in the derived rational functions?
3.  How do these relationships extend to three-dimensional fracture networks?
4.  How can the method be adapted for low-density fracture networks where the current relationships are less accurate?

## Source Coverage
All 12 non-empty indexed fragments were processed. The compiled source blocks total 12, with a compiled character count of 54,116 out of a total indexed character count of 57,552, resulting in a coverage ratio by characters of 0.94. The coverage status is full-index.
