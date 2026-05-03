---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "1995-cowie-multifractal-scaling-properties-of-a-growing-fault-population"
title: "Multifractal Scaling Properties of a Growing Fault Population."
status: "draft"
source_pdf: "data/papers/1995 - Multifractal scaling properties of a growing fault population.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Cowie, Patience A., et al. “Multifractal Scaling Properties of a Growing Fault Population.” *Geophysical Journal International*, vol. 122, 1995, pp. 457-69."
indexed_texts: "13"
indexed_chars: "62481"
nonempty_source_blocks: "13"
compiled_source_blocks: "13"
compiled_source_chars: "61660"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.98686"
coverage_status: "full-index"
source_signature: "157b7f3c62290e4602627f27b313a08f1f451e2c"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T11:16:43"
---

# Multifractal Scaling Properties of a Growing Fault Population.

## One-line Summary
Using a numerical rupture model, this paper demonstrates that a growing fault population transitions from an exponential to a power-law size distribution and develops a strongly multifractal deformation pattern, with the multifractal spectrum explicitly related to the exponent `c` of the fault size distribution as strain localizes through time [Cowie 1995, pp. 1-2; 11-12; 12-13].

## Research Question
What physical mechanisms govern the emergence and evolution of scaling relationships (size distribution, spatial clustering, and displacement patterns) in fault populations, and how can the observed multifractal deformation structure be theoretically understood and linked to the power-law size distribution of faults? [Cowie 1995, pp. 1-2]

## Study Area / Data
This study uses a numerical model, not field data. However, comparisons are made to natural fault datasets for context (e.g., North Sea, Japan, West Africa, California, Arabia, Lorraine coal basin) [Cowie 1995, pp. 1-2; 5-7; 8-9; 13-13].

## Methods
- **Numerical Rupture Model:** A 2-D square lattice (180x180 elements) simulates antiplane shear deformation of an elastic plate driven by a constant plate-boundary velocity [Cowie 1995, pp. 2-2]. Each element has a randomly assigned stress threshold from a uniform distribution (quenched disorder). Rupture occurs at a critical threshold, causing an instantaneous stress drop. The stress field is recalculated to satisfy static equilibrium. Parameters `A` (material heterogeneity) and `p` (stress perturbation from rupture) constitute two types of ‘noise’ [Cowie 1995, pp. 2-3]. Simulations considered here have `A ≪ p` [Cowie 1995, pp. 3-5].
- **Fault Identification:** A fault (cluster) is defined as a discontinuity in the strain field in the y-direction and a continuous set of ruptured elements in the x-direction [Cowie 1995, pp. 5-7].
- **Size-Frequency Analysis:** The cumulative distribution of fault sizes (number of elements, `n`) follows `N(n>s) ∝ n^{-c}` [Cowie 1995, pp. 3-5]. Exponent `c` is calculated by least-squares line fit [Cowie 1995, pp. 3-5].
- **Multifractal Analysis:** A box-counting algorithm is applied to displacement maps. The moments `M_q(r) = Σ P_i^q` are calculated, where `P_i` is proportional to the sum of displacements in a box of size `r`, normalized by total displacement [Cowie 1995, pp. 7-8]. Generalized dimensions `D_q` (capacity `D_0`, information `D_1`, correlation `D_2`) and the multifractal spectrum `f(α)` are derived [Cowie 1995, pp. 7-9].
- **Theoretical Derivation:** The multifractal spectrum `f(α)` is related to the fault size distribution exponent `c` via `f(α) = 2 + c(α - 2)`, based on the assumption of uniform displacement per fault and correlation between maximum displacement and fault size [Cowie 1995, pp. 11-12].

## Key Findings
- **Transition in Dominant Mechanism:** Fault populations initially exhibit uncorrelated nucleation with an exponential size distribution. With increasing strain, growth and coalescence of faults dominate, leading to a power-law size distribution and a fractal pattern [Cowie 1995, pp. 1-2; 3-5].
- **Evolution of Size Exponent `c`:** When the power-law distribution first appears, `c ≈ 1.6–1.9`. The value of `c` decreases systematically through time, reaching an asymptotic value of `1.0–1.4`, reflecting the transition from nucleation-dominated to growth/coalescence-dominated regimes [Cowie 1995, pp. 3-5].
- **Decreasing Fractal Dimensions:** The capacity dimension `D_0` remains constant at 2.0 (space-filling). However, the information dimension `D_1` and correlation dimension `D_2` both decrease through time, indicating the development of a strongly multifractal pattern (`D_0 > D_1 > D_2`) as strain localizes onto major faults [Cowie 1995, pp. 7-8].
- **Strain Localization (Convergence):** The relative strain contribution of the smallest faults decreases over time (from >90% initially to ~40% at large times), while the largest faults accommodate an increasing proportion of the total strain [Cowie 1995, pp. 5-7].
- **Physical Origin of Multifractality:** The multifractal structure arises from the superposition of a power-law distribution of fault displacements onto a fractal fault pattern. Crucially, it requires the correlation between large displacements and large (clustered) faults [Cowie 1995, pp. 9-11].
- **Theoretical `f(α)` Spectrum:** The multifractal spectrum is explicitly related to the size-distribution exponent `c` by `f(α) = 2 + c(α - 2)`, showing that a decrease in `c` (more large faults) produces a broader, more pronounced multifractal spectrum [Cowie 1995, pp. 11-12; 12-13].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| Initial fault size distribution is exponential, evolving to power-law `N(n>s) ∝ n^{-c}` | [Cowie 1995, pp. 3-5] | Model plate driven by constant velocity; `A ≪ p`; analysis of cluster size (elements per fault) | Transition occurs when coalescence starts to dominate over nucleation. |
| Value of `c` decreases from `1.6–1.9` to asymptotic `1.0–1.4` with increasing strain. | [Cowie 1995, pp. 3-5] | Four different model realizations; time evolution tracked. | Decrease correlates with period of rapid increase in size of largest fault (`n_max`) and slight decrease in total fault number. |
| Generalized dimensions evolve to `D_0=2.0 > D_1 > D_2`; multifractality strengthens with time. | [Cowie 1995, pp. 7-8] | Multifractal analysis of displacement maps; `D_0` always 2.0 in this model. | Multifractal onset coincides with appearance of power-law size scaling. |
| Strain contribution of faults ≤50% size of largest fault drops from >90% to ~40% as strain accumulates. | [Cowie 1995, pp. 5-7] | Strain contribution normalized by the largest fault size at each time step. | Interpreted as increasing "convergence" of strain onto large faults. |
| Multifractal spectrum `f(α)` broadens with time; for large strains `α_{q→+∞} ~ 1.0–1.5`, for small strains `α_{q→-∞} ~ 3.0`. | [Cowie 1995, pp. 9-11] | Calculated `f(α)` at four time steps for one simulation. | Indicates large strains are concentrated in linear zones (`P(r) ∝ r^1`), while low strains are anti-clustered (`P(r) ∝ r^3`). |
| Theoretically derived relationship: `f(α) = 2 + c(α - 2)` (`c` from cumulative size distribution). | [Cowie 1995, pp. 11-12] | Assumes `d(x)=d_max` (uniform displacement on each fault) and that `d_max` correlates with fault length. | Derived from power-law displacement histogram `Prob(d) ∝ d^{-ϕ}` with `ϕ = c + 1`. |

## Limitations
- This is a scalar 2-D lattice model (antiplane shear), so it does not consider stress/strain direction, mass conservation, or physical lengthening/shortening of elements [Cowie 1995, pp. 2-3].
- A thin plate approximation applies, making it most relevant for large-scale (e.g., crustal-scale) structures where faults break the entire plate thickness [Cowie 1995, pp. 2-3].
- The model defines fault size as "cluster size" (aggregate length of linked segments), which is not directly equivalent to the fault-length parameter typically measured in field studies [Cowie 1995, pp. 5-5].
- The theoretical derivation of `f(α)` assumes each fault has a uniform displacement equal to its maximum, which removes displacement variability along a single fault [Cowie 1995, pp. 11-12; 11-12].
- The model considers only the conditions where quenched disorder `A` is much less than rupture-induced noise `p`; different behavior is expected when `p ≥ A` [Cowie 1995, pp. 3-5; 2-3].

## Assumptions / Conditions
- The plate material is elastically heterogeneous with a uniformly random distribution of rupture thresholds (quenched disorder `A`) [Cowie 1995, pp. 2-2].
- Long-range and short-range elastic interactions are present, which are crucial for generating spatial correlation [Cowie 1995, pp. 12-13].
- Rupture occurs at a critical stress threshold and produces a stress drop, creating a positive feedback for strain localization [Cowie 1995, pp. 12-13].
- The plate boundary is driven by a constant velocity [Cowie 1995, pp. 1-2].
- A key condition for the observed evolution is that the effects of material heterogeneity (`A`) dominate over stress perturbation noise (`p`) in controlling fault nucleation [Cowie 1995, pp. 3-5].
- Pre-existing structure, specific boundary conditions, fault kinematics, and strain softening are not required to produce the observed scaling behaviors [Cowie 1995, pp. 12-13].

## Key Variables / Parameters
- **`A` (Quenched Disorder):** Controls the width of the uniform distribution of element stress thresholds; represents material heterogeneity [Cowie 1995, pp. 2-2].
- **`p` (Rupture-induced noise):** Controls the magnitude of stress drop during an element rupture, simulating overshoot or undershoot [Cowie 1995, pp. 2-2].
- **`c` (Size-distribution exponent):** Defines the slope of the cumulative power-law distribution of fault sizes (`N(n>s) ∝ n^{-c}`) [Cowie 1995, pp. 3-5].
- **`D_q` (Generalized fractal dimensions):** `D_0` (capacity), `D_1` (information), and `D_2` (correlation) quantify the spatial heterogeneity of the deformation field [Cowie 1995, pp. 7-8].
- **`f(α)` (Multifractal spectrum):** Describes the distribution of strain singularity strengths `α`; related to `c` [Cowie 1995, pp. 8-9; 11-12].
- **`n_max` (Size of largest fault):** Tracks the growth of the largest cluster and indicates the onset of dominant coalescence [Cowie 1995, pp. 3-5].

## Reusable Claims
- Claim: In a deforming system with long-range elastic interactions, fault populations evolve from an exponential size distribution during nucleation-dominated phases to a power-law size distribution (`N(n>s) ∝ n^{-c}`) when growth and coalescence become dominant [Cowie 1995, pp. 3-5].
- Claim: The exponent `c` of the fault size distribution systematically decreases with increasing strain, reflecting the transition from nucleation to coalescence and progressive strain localization [Cowie 1995, pp. 3-5].
- Claim: The deformation pattern of a fault population is strongly multifractal, with the broadening of the `f(α)` spectrum over time being a signature of strain concentration onto major faults [Cowie 1995, pp. 9-11; 12-13].
- Claim: The multifractal spectrum `f(α)` is explicitly linked to the fault size distribution exponent `c` via `f(α) = 2 + c(α - 2)`, under the condition that maximum fault displacement correlates with fault length and intra-fault displacement variability is ignored [Cowie 1995, pp. 11-12].
- Claim: The relative contribution of small faults to total extensional strain decreases as total strain increases, implying that a single, universal proportion is not expected; this reconciles conflicting field-based estimates [Cowie 1995, pp. 5-7].
- Claim: The development of strictly scale-invariant fault patterns in nature may require the material heterogeneity (e.g., inherited tectonic fabric) to be fractal over the same scale range as the resulting structures [Cowie 1995, pp. 12-13].

## Candidate Concepts
- [[fault population]]
- [[multifractal scaling]]
- [[power-law size distribution]]
- [[fractal dimension]]
- [[capacity dimension D0]]
- [[information dimension D1]]
- [[correlation dimension D2]]
- [[multifractal spectrum]]
- [[fault nucleation]]
- [[fault coalescence]]
- [[strain localization]]
- [[long-range elastic interaction]]
- [[quenched disorder]]
- [[self-organized criticality]]

## Candidate Methods
- [[numerical rupture model]]
- [[2D lattice model]]
- [[box-counting algorithm]]
- [[multifractal analysis]]
- [[generalized dimensions]]
- [[least-squares fit]]
- [[fault size-frequency analysis]]

## Connections To Other Work
- Builds on the theoretical framework and numerical model of Cowie, Vanneste & Sornette (1993) and Sornette, Davy & Sornette (1990) [Cowie 1995, pp. 1-2; 2-2].
- Consistent with analogue models of fault growth by A. Sornette, Davy & Sornette (1990, 1993) [Cowie 1995, pp. 2-2; 3-5].
- Supports findings of localization in shear bands by Poliakov & Herrmann (1994), who also observed a strongly multifractal structure [Cowie 1995, pp. 2-2; 8-9].
- Relates the asymptotic value `c` to the analysis of Sornette & Davy (1991), who argued `c=1.0` is an "attracting" value for a self-organized critical state dominated by fault growth [Cowie 1995, pp. 3-5].
- Explains conflicting field-based estimates of small-fault strain contribution from Scholz & Cowie (1990), Walsh et al. (1991), and Marrett & Allmendinger (1992) by showing that this contribution decreases with total strain [Cowie 1995, pp. 5-7].
- Compares `D_q` results to multifractal analyses of natural fractures (Vignes-Adler et al. 1991) and faults (Ouillon, Sornette & Castaing, in press) [Cowie 1995, pp. 8-9].

## Open Questions
- How does the presence of tectonic rotations, which can frustrate fault growth and require new fault nucleation, alter the asymptotic value of `c` and the evolution of the multifractal spectrum? [Cowie 1995, pp. 3-5]
- How does the model's prediction that small-fault strain contribution decreases with total strain apply quantitatively to natural systems, such as evolving sedimentary basins, where independent strain estimates are available? [Cowie 1995, pp. 3-5]
- What is the effect of a fractal (rather than uniform) distribution of initial material properties on the scale-invariance and multifractality of the resulting fault pattern? [Cowie 1995, pp. 12-13]
- Can the theoretical linkage `f(α) = 2 + c(α - 2)` be generalized to account for non-uniform displacement profiles along faults? [Cowie 1995, pp. 11-12]

## Source Coverage
All 13 non-empty indexed source blocks from the publication (Cowie et al., 1995) were processed. These blocks contain a total of 61,660 characters out of 62,481 indexed characters, yielding a character coverage ratio of 0.98686.
