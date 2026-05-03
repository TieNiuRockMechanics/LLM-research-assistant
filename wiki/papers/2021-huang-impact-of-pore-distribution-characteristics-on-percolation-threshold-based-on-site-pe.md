---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-huang-impact-of-pore-distribution-characteristics-on-percolation-threshold-based-on-site-pe"
title: "Impact of Pore Distribution Characteristics on Percolation Threshold Based on Site Percolation Theory."
status: "draft"
source_pdf: "data/papers/2021 - Impact of pore distribution characteristics on percolation threshold based on site percolation theory.pdf"
collections:
citation: "Huang, Xudong, et al. \"Impact of Pore Distribution Characteristics on Percolation Threshold Based on Site Percolation Theory.\" *Physica A*, vol. 570, 2021, article 125800. doi:10.1016/j.physa.2021.125800."
indexed_texts: "12"
indexed_chars: "56285"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "56557"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004833"
coverage_status: "full-index"
source_signature: "e5f8d6422925213294e33f9657c170ac0af74eeb"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T04:29:14"
---

# Impact of Pore Distribution Characteristics on Percolation Threshold Based on Site Percolation Theory.

## One-line Summary
This paper introduces a pore distribution factor m into the site percolation model to study how pore distribution characteristics affect the percolation threshold in 2D and 3D porous media; larger m leads to fewer pores, easier merging, and a lower percolation threshold.

## Research Question
How do pore distribution characteristics (porosity, pore number distribution, and pore volume distribution) influence the percolation threshold of two-dimensional and three-dimensional porous media? Specifically, the study investigates the effect of a pore distribution factor m (the number of sites occupied per generated pore) on the percolation threshold using a modified site percolation model that allows pore cluster overlap and merging.

## Study Area / Data
This is a purely numerical simulation study; no natural geographic area is used. Two types of simulated porous media are generated:
- 2D square lattice with open boundary conditions.
- 3D simple cubic lattice with open boundary conditions.
The dataset consists of 5000 Monte Carlo realizations for each combination of m ∈ {1, 2, 5, 10, 15, 20, 25, 30, 35, 40} and system size L (L = 200, 400, 600, 800, 1000 for 2D; L = 120, 140, 160, 180, 200 for 3D).

## Methods
- **Modified site percolation model**: A pore distribution factor m is introduced, representing the number of sites occupied by a pore generated in each step. Pores are placed randomly, and if a new pore overlaps (partially or fully) with existing pores, they merge. This differs from random sequential adsorption (RSA) models because overlapping is allowed, and no jamming state occurs; porosity can increase up to 1. [Huang 2021, pp. 2-3]
- **Simulation procedure** (summarized from steps 1–6): Use arrays with initial value 0 (solid). Randomly assign pores of volume m in a buffer array Y (size L+2m). Pores of size not equal to m are deleted; only size-m clusters are retained. Merge Y into system X. Record porosity, pore distributions, and spanning cluster status. Repeat until porosity exceeds loop condition (99% for 2D, 70% for 3D). [Huang 2021, pp. 3-4]
- **Finite-size scaling**: Local percolation probability R_X^L(P) is fitted with an adjusted hyperbolic tangent function: R_X^L(P) = 0.5{1 + tanh[(P – P_c(L))/Δ(L)]}. The percolation threshold P_c is obtained by extrapolating P_c(L) to L → ∞ using the linear relation P_c(L) – P_c ∝ Δ(L) (Eq. 4). Error bars are given by max(|P_c^I(∞) – P_c^A(∞)|, |P_c^U(∞) – P_c^A(∞)|). [Huang 2021, pp. 3-4]
- **Critical exponent**: The correlation length exponent ν is obtained from Δ(L) ∝ L^{-1/ν}. [Huang 2021, pp. 4-6]
- **Fitting of percolation threshold vs. m**: For 2D, P_c = 59.35603 m^{-0.11332} (R² = 0.997); for 3D, P_c = 31.13764 m^{-0.33713} (R² = 0.999). [Huang 2021, pp. 6-7]

## Key Findings
- The percolation threshold decreases with increasing m (m ≤ 40) in both 2D and 3D systems. [Huang 2021, pp. 1, 12]
- 2D percolation thresholds: m=1 → 59.27%, m=40 → 38.38%. 3D percolation thresholds: m=1 → 31.16%, m=40 → 8.65%. [Huang 2021, pp. 1, 6‑7, 10]
- For a fixed porosity, a larger m results in a drastic reduction of pore number and an increase in pore volume heterogeneity; pores merge more easily into large spanning clusters, causing a lower percolation threshold. [Huang 2021, pp. 6-7, 10‑11]
- The pore number first increases then decreases with porosity; both the maximum pore number and the porosity at which it occurs decrease with m. [Huang 2021, pp. 7, 11]
- Pore connectivity is determined by both porosity and pore distribution characteristics; relying solely on porosity can lead to misjudgment of connectivity. [Huang 2021, pp. 1, 12]
- The critical exponent ν obtained for 2D (∼4/3) and 3D (∼7/8) matches that of ordinary random percolation, indicating the model belongs to the same universality class regardless of m. [Huang 2021, pp. 5, 7]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 2D percolation threshold for m=1 is 59.27(1)% | Table 1 [Huang 2021, pp. 6] | 2D square lattice, open boundaries, m=1 | Consistent with known classical site percolation value. |
| 2D percolation threshold for m=40 is 38.38(5)% | Table 1 [Huang 2021, pp. 6] | 2D square lattice, m=40 | Decrease by ~20.9 percentage points from m=1. |
| 3D percolation threshold for m=1 is 31.16(1)% | Table 2 [Huang 2021, pp. 10] | 3D simple cubic lattice, open boundaries, m=1 | Consistent with known classical site percolation value. |
| 3D percolation threshold for m=40 is 8.65(5)% | Table 2 [Huang 2021, pp. 10] | 3D simple cubic lattice, m=40 | Decrease by ~22.5 percentage points. |
| 2D ν for m=1: 1.38(13) | Table 1 [Huang 2021, pp. 6] | Finite-size scaling | Close to exact ν=4/3. |
| 3D ν for m=1: 0.92(19) | Table 2 [Huang 2021, pp. 10] | Finite-size scaling | Close to exact ν≈0.875. |
| At porosity 45%, when m=1, number of pores ~88,060; when m=40, number of pores 212 (2D) | Fig. 6 [Huang 2021, pp. 7] | 2D, L=1000, porosity=45% | Drastic reduction in pore count. |
| Maximum pore number in 2D: m=1 → 130,473 at porosity 26.79%; m=40 → 1,847 at porosity 14.93% | Fig. 7 [Huang 2021, pp. 7] | 2D, L=1000 | Peak pore number and peak porosity decrease with m. |
| Maximum pore number in 3D: m=1 → 694,156 at porosity 17.79%; m=40 → 4,615 at porosity 5.14% | Fig. 12 [Huang 2021, pp. 11] | 3D, L=200 | Same trend as 2D. |
| P_c – m fit: 2D: P_c = 59.35603 m^{-0.11332}, R² = 0.997 | Eq. 5 [Huang 2021, pp. 7] | m = 1,2,…,40 | Power-law decrease. |
| P_c – m fit: 3D: P_c = 31.13764 m^{-0.33713}, R² = 0.999 | Eq. 6 [Huang 2021, pp. 10] | m = 1,2,…,40 | Faster decay than 2D. |
| Overlapping allowed in this model; no jamming state | [Huang 2021, pp. 2-3] | Filling method | Main difference from RSA-based models (e.g., Cornette et al. 2003). |
| Percolation thresholds obtained here are lower than those from non-overlapping k-mer models for m>1 | [Huang 2021, pp. 6] | e.g., comparison with Ref. [47] | Due to merging of overlapped pores. |

## Limitations
- The study is limited to m ≤ 40 because of computational constraints and algorithm limitations. Behavior for m > 40 remains unexplored. [Huang 2021, pp. 6, 10]
- The simulated porous media are idealized and differ significantly from real natural porous media. The findings can explain certain percolation phenomena in natural rocks but should be applied with caution. [Huang 2021, pp. 11-12]
- Porosity loop conditions were capped at 99% (2D) and 70% (3D); the percolation threshold for m > 40 is not investigated. [Huang 2021, pp. 3, 12]
- Only square (2D) and simple cubic (3D) lattices were used; the influence of lattice type is not examined.

## Assumptions / Conditions
- Open boundary conditions are used in all directions for percolation detection. [Huang 2021, pp. 3-4]
- Pores are generated sequentially with random location and arbitrary shape; the shape randomness means larger m leads to more diverse and complex pore shapes, but all shapes at the same m are equally probable. [Huang 2021, pp. 3]
- Overlap (partial or full) between new and existing pores results in merging into a larger pore cluster; no excluded volume. [Huang 2021, pp. 2-3]
- The system is initially fully solid (porosity = 0). Porosity is increased until the loop condition is met. [Huang 2021, pp. 3]
- The finite-size scaling analysis assumes that P_c(L) – P_c ∝ L^{-1/ν} and that the scaling relationship P_c(L) – P_c ∝ Δ(L) holds. [Huang 2021, pp. 4]
- The percolation threshold is defined as the porosity at which the percolation probability reaches 0.5 in the hyperbolic tangent fit. [Huang 2021, pp. 4]
- Percolation thresholds reported are the extrapolated values for infinite system size (L → ∞). [Huang 2021, pp. 4]

## Key Variables / Parameters
- **m**: pore distribution factor, number of sites occupied by a pore generated in one step. [Huang 2021, pp. 2-3]
- **L**: linear system size (number of sites along one edge). [Huang 2021, pp. 3]
- **P_c**: global percolation threshold (porosity at which a spanning cluster first appears in infinite system). [Huang 2021, pp. 4]
- **ν**: critical correlation length exponent. [Huang 2021, pp. 4]
- **Δ(L)**: percolation transition width. [Huang 2021, pp. 4]
- **R_X^L(P)**: percolation probability along direction(s) X for system size L at porosity P. [Huang 2021, pp. 4]
- **Porosity**: ratio of occupied sites to total sites. [Huang 2021, pp. 3]

## Reusable Claims
- In a modified 2D square site percolation model with overlapping pores, the percolation threshold decreases from 59.27% (m=1) to 38.38% (m=40) as the pore distribution factor m increases. [Huang 2021, pp. 6]
- In a modified 3D simple cubic site percolation model with overlapping pores, the percolation threshold decreases from 31.16% (m=1) to 8.65% (m=40). [Huang 2021, pp. 10]
- The percolation threshold P_c follows a power-law relationship with m: for 2D, P_c ∝ m^{-0.11332}; for 3D, P_c ∝ m^{-0.33713} (within m ≤ 40). [Huang 2021, pp. 7, 10]
- Larger m leads to a smaller number of pores for a given porosity, and pores are more likely to merge into large clusters, which causes a lower percolation threshold. [Huang 2021, pp. 6-7, 10‑11]
- Pore connectivity is controlled by both porosity and pore distribution characteristics; using only porosity can misjudge connectivity. [Huang 2021, pp. 1, 12]
- The critical exponent ν remains consistent with ordinary random percolation (4/3 for 2D, ~0.875 for 3D) irrespective of m, indicating the model belongs to the same universality class. [Huang 2021, pp. 5, 7]
- The filling method that allows overlapping and merging avoids the jamming state, enabling porosity to reach 1. This distinguishes it from RSA-based multiple-occupation models. [Huang 2021, pp. 2-3]

## Candidate Concepts
- [[site percolation model]]
- [[pore distribution factor m]]
- [[finite-size scaling]]
- [[percolation threshold]]
- [[critical correlation length exponent ν]]
- [[percolation probability]]
- [[universality class]]
- [[pore connectivity]]
- [[pore number distribution]]
- [[pore volume distribution]]
- [[jamming state]]
- [[random sequential adsorption (RSA)]]
- [[open boundary conditions]]

## Candidate Methods
- [[Monte Carlo simulation of site percolation]]
- [[finite-size scaling with hyperbolic tangent fit]]
- [[linear extrapolation of percolation threshold]]
- [[modified filling method with overlapping pore clusters]]
- [[pore cluster identification and size analysis]]

## Connections To Other Work
- The classical site percolation thresholds for 2D square and 3D simple cubic lattices (59.27% and 31.16%) are reproduced for m=1, consistent with existing research. [Huang 2021, pp. 1, 6, 10]
- Compared with RSA-based k-mer models (e.g., Cornette et al. [47]) where overlapping is forbidden, the model in this paper yields lower percolation thresholds for m>1 because overlapping facilitates merging. [Huang 2021, pp. 2-3, 6]
- The critical exponent ν obtained matches that of ordinary random percolation, aligning with values reported by Stauffer & Aharony [41] and Yonezawa et al. [32]. [Huang 2021, pp. 5, 7]
- The simulated percolation thresholds can be compared with natural porous media (e.g., oil shale, sandstone) to explain why some natural systems have thresholds much lower than classical site percolation values. [Huang 2021, pp. 2, 11‑12]
- The pore distribution factor approach extends the classic site percolation model and can be related to continuum percolation studies of overlapping particles. [Huang 2021, pp. 2]

## Open Questions
- What is the behavior of the percolation threshold for m > 40? The current study is limited by computational capacity; further investigation is needed. [Huang 2021, pp. 6, 10]
- How well do the simulated pore distribution characteristics correspond to specific natural porous media, and can the model accurately predict percolation properties of, for example, oil shale after retorting or sandstone reservoirs? A future paper is planned to address this. [Huang 2021, pp. 11-12]
- Does the power-law relationship between P_c and m hold for larger m or different lattice types?
- Can the filling method be extended to include pore size distributions other than uniform m, and how would that affect the percolation threshold?

## Source Coverage
All 12 non-empty indexed fragments (from pages 1–14 of the original paper) were processed and compiled. The total indexed character count was 56,285; the compiled source blocks contain 56,557 characters, yielding a coverage ratio by characters of 1.004833. Coverage ratio by blocks is 1.0. No indexed fragment was omitted.
