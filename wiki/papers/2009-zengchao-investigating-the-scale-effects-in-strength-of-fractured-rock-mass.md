---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2009-zengchao-investigating-the-scale-effects-in-strength-of-fractured-rock-mass"
title: "Investigating the Scale Effects in Strength of Fractured Rock Mass."
status: "draft"
source_pdf: "data/papers/2009 - Investigating the scale effects in strength of fractured rock mass.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Zengchao, Feng, Yangsheng Zhao, and Dong Zhao. \"Investigating the Scale Effects in Strength of Fractured Rock Mass.\" *Chaos, Solitons and Fractals*, vol. 41, 2009, pp. 2377-2386. doi:10.1016/j.chaos.2008.09.005."
indexed_texts: "7"
indexed_chars: "33993"
nonempty_source_blocks: "7"
compiled_source_blocks: "7"
compiled_source_chars: "34154"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004736"
coverage_status: "full-index"
source_signature: "b048201726247c3b4776a4372157f755732856d0"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T22:59:59"
---

# Investigating the Scale Effects in Strength of Fractured Rock Mass.

## One-line Summary
This study uses fractal geometry to derive a nonlinear relationship between rock mass strength and fracture quantity, establishing that the strength attenuation index is directly related to the fractal dimension of the fracture distribution.

## Research Question
How can the scale effects in the strength of a fractured rock mass be quantitatively described by relating rock mass strength to the quantity and size distribution of fractures using fractal geometry?

## Study Area / Data
The study uses fracture distribution data from coal and rock masses in approximately thirty mining areas in China [Zengchao 2009, pp. 2-3]. Specific data sources include coal mass from mines such as Xinzhou kiln, Yangquan, Wangzhuang, and Phenix mountain [Zengchao 2009, pp. 3-5], as well as rock mass fracture data from the Three Gorges Dam site [Zengchao 2009, pp. 2-3]. Physical experiments used rock samples (50 mm x 50 mm x 100 mm cuboids) from coal seams in mines including Bailong, Tuanbai, Xinzhuang, Wangtaipu, Dalong, and Xishan [Zengchao 2009, pp. 5-6]. Numerical experiments used digital plane models of various sizes (e.g., 1 m x 1 m, 0.5 m x 0.5 m) [Zengchao 2009, pp. 5-6].

## Methods
The primary method is fractal geometry, specifically the box-counting method, to quantify the relationship between fracture quantity and observational size-scale [Zengchao 2009, pp. 2-3]. The method involves selecting a square region, counting fractures at successive length scales (L0, L0/2, L0/4, etc.), and performing regression analysis on ln d vs. ln N [Zengchao 2009, pp. 2-3]. The study combines this fractal analysis with theoretical damage mechanics and numerical simulation. Numerical simulations involved creating digital rock core samples where cell strength followed a Weibull stochastic distribution, then distributing fractures according to prescribed fractal parameters and calculating uniaxial compressive strength after each addition [Zengchao 2009, pp. 3-5].

## Key Findings
1.  The relationship between fracture quantity (Nd) and size (d) follows a power law: Nd = N0 d^(-D), where D is the fractal dimension of the fracture quantity distribution [Zengchao 2009, pp. 1-2].
2.  A nonlinear relationship exists between rock mass strength (Rc) and fracture quantity (Nd): Rc = Rcm + ΔRc Exp[-B Nd], where Rcm is the residual strength and ΔRc is the strength difference between intact and residual rock [Zengchao 2009, pp. 1-2].
3.  Combining the fracture quantity-size relationship with the strength-fracture quantity relationship yields a formula for rock mass strength that includes size-scale: Rc = Rcm + ΔRc Exp(-B N1m 2^((i-1)D) l_E^(2-D)) [Zengchao 2009, pp. 1-2].
4.  The attenuation index (a) of rock mass strength with size is related to the fractal dimension: a = 2 - D [Zengchao 2009, pp. 1-2].
5.  Numerical and physical experiments confirm that larger fractures exert the primary control on rock mass strength, with strength decreasing significantly upon the introduction of larger fractures and the effect diminishing for smaller fractures [Zengchao 2009, pp. 3-5].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Fractal dimension D for fracture quantity distribution at Three Gorges site averages ~1.20. | [Zengchao 2009, pp. 2-3] | Measured at size scales from 0.066 m to 12 m. | Supports the power-law relationship Nd = N0 d^(-D). |
| Numerical experiment on a 1m x 1m digital sample shows strength decreases by ~35% after adding the third fracture step (length 0.25m). | [Zengchao 2009, pp. 3-5] | D=1.5, N1m=0.1, mean compressive strength=120 MPa. | Demonstrates the dominant control of larger fractures on strength. |
| Experimental data from coal samples fit the equation rc = rm + Δr Exp[-B N4] with high correlation (R² > 0.9). | [Zengchao 2009, pp. 5-6] | 50mm x 50mm x 100mm cuboid samples from various coal seams. | Validates the proposed nonlinear strength-fracture quantity relationship. |
| The derived size-scale strength formula rc = rm + Δr Exp(-b l_E^a) with a=2-D fits numerical data with R²=0.985. | [Zengchao 2009, pp. 8-10] | Numerical rectangular samples (height:width=2:1) from 0.1m to 500m height, D=1.5. | Confirms the relationship between attenuation index 'a' and fractal dimension D. |
| The formula by Evans and Pomeroy [4] (rc = 42.433 l^(-0.2826)) fits the same numerical data with R²=0.8432. | [Zengchao 2009, pp. 10-10] | Same numerical sample set as above. | Shows the new model has better correlation and incorporates fracture quantity. |

## Limitations
The study primarily uses 2D plane models for numerical simulations [Zengchao 2009, pp. 5-6]. The physical experiments were conducted on small-scale laboratory samples (50 mm x 50 mm x 100 mm) [Zengchao 2009, pp. 5-6]. The extrapolation from small-scale measurable areas to large engineering areas assumes perfect scale invariance [Zengchao 2009, pp. 2-3]. The model assumes fractures are distributed according to a strict power-law across all scales.

## Assumptions / Conditions
1.  The distribution of fracture quantities exhibits scale invariance, a fundamental property of fractal objects [Zengchao 2009, pp. 2-3].
2.  The measurable fracture quantity in a small area (L0 x L0) is independent of its location within the larger engineering area (LE x LE) [Zengchao 2009, pp. 2-3].
3.  In numerical models, the cell strength of the sample follows a Weibull stochastic distribution [Zengchao 2009, pp. 3-5].
4.  Only fractures larger than a certain size (controlled by the first 'i' steps) significantly control rock mass strength [Zengchao 2009, pp. 5-6].

## Key Variables / Parameters
*   **D**: Fractal dimension of the fracture quantity distribution.
*   **Nd**: Number of fractures with length ≥ d.
*   **N0**: Initial value of the fracture quantity distribution.
*   **N1m**: Initial fracture quantity distribution value for a 1 m x 1 m standard size scale.
*   **Rc**: Rock mass strength.
*   **Rcm**: Residual strength of fractured rock mass.
*   **ΔRc (Δr)**: Strength difference between intact rock strength (Rc0) and residual strength (Rcm).
*   **B**: Attenuation index for strength with respect to fracture quantity.
*   **a**: Attenuation index for strength with respect to size-scale, where a = 2 - D.
*   **b**: Strength attenuation index for a cubic sample with side length 1 m.
*   **lE**: Engineering size-scale (side length).
*   **m**: Homogeneity index (in Weibull distribution).

## Reusable Claims
*   **Condition:** For a fractured rock mass where fracture quantity follows a fractal distribution. **Limitation:** Based on 2D analysis and scale invariance assumption. **Claim:** The attenuation index (a) of rock mass strength with increasing size is equal to 2 minus the fractal dimension (D) of the fracture quantity distribution [Zengchao 2009, pp. 1-2, 8-10].
*   **Condition:** When relating rock mass strength to fracture quantity. **Limitation:** Derived from theoretical damage mechanics and experimental validation on coal/rock samples. **Claim:** Rock mass strength decays exponentially with increasing fracture quantity according to the formula Rc = Rcm + ΔRc Exp[-B Nd] [Zengchao 2009, pp. 1-2, 5-6].
*   **Condition:** In a rock mass with a fractal fracture distribution. **Limitation:** Assumes the largest fractures within the considered size range dominate strength. **Claim:** The control of fractures on rock mass strength is primarily exerted by the larger fractures, and the effect of smaller fractures can be neglected beyond a certain size threshold [Zengchao 2009, pp. 3-5].

## Candidate Concepts
*   [[Fractal geometry]]
*   [[Scale effect]]
*   [[Fracture quantity distribution]]
*   [[Rock mass strength]]
*   [[Damage mechanics]]
*   [[Box-counting method]]
*   [[Residual strength]]
*   [[Attenuation index]]

## Candidate Methods
*   [[Box-counting method]]
*   [[Fractal analysis]]
*   [[Numerical simulation]]
*   [[Weibull distribution]]
*   [[Regression analysis]]

## Connections To Other Work
The study builds on and compares its results to several prior empirical formulas for rock mass strength scale effects:
*   Evans and Pomeroy [4]: rc = k a^(-b) [Zengchao 2009, pp. 1-2].
*   Hock and Brown [6]: rc = σ50 (50/D)^0.18 [Zengchao 2009, pp. 1-2].
*   Baochen [3]: rc = rm + a exp(-bD) [Zengchao 2009, pp. 1-2].
*   Guangzhong and Ruiguang [5]: r = rm + (r0 - rm) N^(-a) [Zengchao 2009, pp. 1-2].
The work also references fractal models by Carpinteri and Chiaia [1] and Carpinteri and Paggi [2] on size-scale effects [Zengchao 2009, pp. 1-2].

## Open Questions
*   How does the model perform when extended to three-dimensional fracture networks?
*   How sensitive are the results to deviations from the assumed perfect power-law (fractal) distribution of fractures?
*   Can the parameters (B, Rcm, ΔRc) be reliably predicted from basic geological or mechanical properties without extensive fracture mapping?

## Source Coverage
All non-empty indexed fragments were processed. The compilation used 7 source blocks containing a total of 34,154 characters. The coverage ratio by blocks is 1.0, and the coverage ratio by characters is 1.004736, indicating full-index coverage.
