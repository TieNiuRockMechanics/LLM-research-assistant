---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2018-chen-study-on-the-effective-stress-characteristic-of-rough-rock-fractures-with-water-pressu"
title: "Study on the effective stress characteristic of rough rock fractures with water pressure."
status: "draft"
source_pdf: "data/papers/含水压粗糙岩石裂隙有效应力规律研究_陈跃都.pdf"
collections:
citation: "Chen, Yuedu, et al. \"Study on the effective stress characteristic of rough rock fractures with water pressure.\" *Chinese Journal of Rock Mechanics and Engineering*, vol. 37, no. Supp. 2, Oct. 2018, pp. 3850-3860, doi:10.13722/j.cnki.jrme.2018.0622."
indexed_texts: "4"
indexed_chars: "18847"
nonempty_source_blocks: "4"
compiled_source_blocks: "4"
compiled_source_chars: "17396"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.923012"
coverage_status: "full-index"
source_signature: "f1f7663d33d08bb47906aeb16ad01c0013302497"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T11:14:06"
---

# Study on the effective stress characteristic of rough rock fractures with water pressure.

## One-line Summary
This study introduces an effective stress coefficient α, defined as the ratio of interconnected voids in a rough fracture, to describe the hydro-mechanical coupling behavior and develops a new empirical effective stress model relating α to confining stress and water pressure.

## Research Question
How to quantitatively describe the effective stress characteristics of rough rock fractures under water pressure, and how does the traditional effective stress model (e.g., Terzaghi's or Biot's) compare to a new model that accounts for fracture roughness?

## Study Area / Data
The study uses hydraulic test results from two single fractured sandstone specimens, S1 and S2, with different roughness characteristics [Chen 2018, pp. 4-8]. The experimental data and geometric analysis are based on prior work by Y. Chen et al. [Chen 2018, pp. 4-8].

## Methods
1.  **Conceptual Model:** An asperities-voids-water pressure conceptual model for a rough fracture is established, leading to a stress balance analysis [Chen 2018, pp. 1-4].
2.  **Effective Stress Coefficient Definition:** The effective stress coefficient α is defined as the ratio of interconnected void areas (where aperture > 10 μm) to the total fracture area, identified from 3D fracture surface scans [Chen 2018, pp. 4-8].
3.  **Hydraulic Testing:** Flow tests were conducted on specimens S1 and S2 under various confining stresses (σ₃) and water pressures (P) to measure flow rate (Q) and deformations [Chen 2018, pp. 4-8].
4.  **Model Fitting:** An empirical model for α as a function of confining stress and water pressure was fitted to the experimental data [Chen 2018, pp. 8-11].

## Key Findings
1.  The effective stress coefficient α, representing the interconnected void ratio, effectively describes the variation of hydro-mechanical coupling behaviors in rough fractures [Chen 2018, pp. 1-4].
2.  An empirical model α = a + b·exp(c·σ₃ + d·P) provides a good representation of how α changes with confining stress and water pressure [Chen 2018, pp. 8-11].
3.  Effective stress values calculated by the new model (Eq. 14) and the traditional model (with α=1 or α=0.5) show significant differences, especially at high confining stresses and high water pressures [Chen 2018, pp. 8-11].
4.  A critical confining stress and a critical water pressure can be identified to estimate the applicability of the traditional model. The critical water pressure increases linearly with confining pressure [Chen 2018, pp. 8-11].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| The effective stress coefficient α is defined as the ratio of interconnected void areas (aperture > 10 μm) to total area. | [Chen 2018, pp. 4-8] | Analysis of 3D fracture scans for specimens S1 and S2. | Method for quantifying α from geometry. |
| Fitting results for S1: α = 0.5503 + 0.4401·exp(-0.10348·σ₃ + 0.1596·P), R²=0.96532. | [Chen 2018, pp. 8-11] | Specimen S1, confining stress σ₃ and water pressure P. | Empirical model for α. |
| Fitting results for S2: α = 0.3955 + 0.4927·exp(-0.20143·σ₃ + 0.3844·P), R²=0.90609. | [Chen 2018, pp. 8-11] | Specimen S2, confining stress σ₃ and water pressure P. | Empirical model for α. |
| For specimen S1, the interconnected void ratio increased from 75.80% to 85.87% (a 10.07% increase) as seepage pressure increased under a confining stress of 10 MPa. | [Chen 2018, pp. 4-8] | Confining stress of 10 MPa, specimen S1. | Shows α increases with water pressure. |
| For specimen S2, the interconnected void ratio increased from 53.74% to 73.05% (a 19.31% increase) under the same conditions. | [Chen 2018, pp. 4-8] | Confining stress of 10 MPa, specimen S2. | Shows α increases with water pressure. |
| Critical confining stresses for deviation between models: ~18 MPa for S1 and ~7.5 MPa for S2. | [Chen 2018, pp. 8-11] | Comparison of new model (Eq. 14) with traditional models (α=1, α=0.5). | Threshold for traditional model applicability. |
| Critical water pressure increases linearly with confining pressure for both specimens. | [Chen 2018, pp. 8-11] | Various confining stresses for S1 and S2. | Relationship for estimating model applicability. |

## Limitations
1.  The empirical model (Eq. 13) is derived from tests on only two sandstone specimens (S1 and S2), so its generalizability to other rock types or fracture geometries is not confirmed [Chen 2018, pp. 8-11].
2.  The study focuses on the effective stress characteristic; the full coupled hydro-mechanical process is not modeled in detail [Chen 2018, pp. 1-4].
3.  The definition of interconnected voids uses a fixed aperture threshold (10 μm), which may not be universally applicable [Chen 2018, pp. 4-8].

## Assumptions / Conditions
1.  The rough fracture is conceptualized as a system of asperities, voids, and water pressure [Chen 2018, pp. 1-4].
2.  The effective stress coefficient α is assumed to be equal to the ratio of interconnected voids in the fracture [Chen 2018, pp. 1-4].
3.  The water pressure in the interconnected voids is assumed to be the applied seepage pressure [Chen 2018, pp. 1-4].
4.  The analysis assumes steady-state flow conditions during hydraulic tests [Chen 2018, pp. 4-8].

## Key Variables / Parameters
*   **α**: Effective stress coefficient, defined as the ratio of interconnected void area to total fracture area.
*   **σ₃**: Confining stress (MPa).
*   **P**: Water pressure or seepage pressure (MPa).
*   **σ'ₙ**: Effective normal stress (MPa).
*   **Q**: Flow rate (mL/min).
*   **ΔP**: Hydraulic head pressure difference.
*   **a, b, c, d**: Empirical fitting parameters in the model for α.

## Reusable Claims
1.  **Condition:** For rough rock fractures under coupled stress and water pressure. **Claim:** The effective stress coefficient α, representing the interconnected void ratio, can be empirically modeled as α = a + b·exp(c·σ₃ + d·P), where σ₃ is confining stress and P is water pressure [Chen 2018, pp. 8-11].
2.  **Condition:** When comparing effective stress models for rough fractures. **Claim:** The traditional effective stress model (using α=1) significantly overestimates effective stress compared to the new model at high confining stresses and high water pressures, with a critical confining stress threshold existing for each fracture [Chen 2018, pp. 8-11].
3.  **Condition:** For estimating the applicability of the traditional Terzaghi effective stress principle to rough fractures. **Claim:** The critical water pressure, above which the traditional model deviates significantly, increases linearly with the applied confining pressure [Chen 2018, pp. 8-11].

## Candidate Concepts
*   [[effective stress coefficient]]
*   [[rough rock fracture]]
*   [[hydro-mechanical coupling]]
*   [[interconnected voids]]
*   [[fracture aperture]]
*   [[critical confining stress]]
*   [[critical water pressure]]

## Candidate Methods
*   [[hydraulic testing]]
*   [[3D fracture surface scanning]]
*   [[conceptual model of asperities-voids-water]]
*   [[stress balance analysis]]
*   [[empirical model fitting]]

## Connections To Other Work
*   The study builds upon and discusses the traditional effective stress principles of Terzaghi [Chen 2018, pp. 1-4] and Biot [Chen 2018, pp. 1-4].
*   It references prior experimental work on coupled hydro-mechanical behavior in fractures by researchers like Xie et al. [Chen 2018, pp. 11-11], Liu et al. [Chen 2018, pp. 11-11], and Yi [Chen 2018, pp. 11-11].
*   The geometric analysis of fracture voids is based on methods from Y. Chen et al. [Chen 2018, pp. 4-8].
*   The discussion of flow regimes references work by Louis [Chen 2018, pp. 4-8] and Zhang & Nemcik [Chen 2018, pp. 11-11].

## Open Questions
1.  How well does the empirical model for α (Eq. 13) perform for fractures in other rock types (e.g., granite, limestone) or with different roughness scales?
2.  What is the physical mechanism linking the macroscopic effective stress coefficient α to the microscopic contact mechanics and fluid distribution within the fracture?
3.  Can the identified critical confining stress and water pressure thresholds be predicted a priori from measurable fracture geometric properties?

## Source Coverage
All non-empty indexed fragments were processed. The compilation used 4 source blocks containing a total of 17,396 characters from the original 18,847 indexed characters, achieving a coverage ratio of 0.923 by character count. The coverage status is full-index.
