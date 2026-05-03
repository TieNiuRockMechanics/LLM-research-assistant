---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2010-bunger-stochastic-analysis-of-core-discing-for-estimation-of-in-situ-stress"
title: "Stochastic Analysis of Core Discing for Estimation of In Situ Stress."
status: "draft"
source_pdf: "data/papers/2010 - Stochastic Analysis of Core Discing for Estimation of In Situ Stress.pdf"
collections:
  - "zotero new"
citation: "Bunger, Andrew P. \"Stochastic Analysis of Core Discing for Estimation of In Situ Stress.\" *Rock Mechanics and Rock Engineering*, vol. 43, 2010, pp. 275-286. DOI: 10.1007/s00603-009-0051-3."
indexed_texts: "11"
indexed_chars: "53002"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "53255"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004773"
coverage_status: "full-index"
source_signature: "72139486c52e23479ea8965a1e5a3938c1af229b"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T14:07:22"
---

# Stochastic Analysis of Core Discing for Estimation of In Situ Stress.

## One-line Summary
A stochastic approach that uses the entire core disc length distribution, rather than a typical disc length, to estimate in situ stress; demonstrated on 900 m of diamond-drilled core from a South Australian granite, showing that convolution of Gaussian stress and strength with a mechanical discing criterion can reproduce the observed distribution shapes and provide a reasonable estimate of maximum horizontal stress. [Bunger 2010, pp. 1-2, 8-9, 11]

## Research Question
How can core discing models be reliably applied for in situ stress estimation when the disc length distribution is non‑Gaussian and a “typical” disc length is undefined? [Bunger 2010, pp. 1-2, 3-4]

## Study Area / Data
- 900 m of NQ2 diamond‑drilled core from a 1934.6 m deep vertical exploration hole near the Olympic Dam mine, South Australia. [Bunger 2010, pp. 2-3]
- Rock type: weakly‑altered, massive, Proterozoic granite of the Burgoyne Batholith, encountered from 719 m depth. [Bunger 2010, pp. 2-3]
- Strong core discing below ≈1000 m depth; fractures predominantly sub‑perpendicular to the core axis. [Bunger 2010, pp. 2-3]
- Total of 5,494 predominantly cylindrical fragments measured in eight 40–70 m long zones (1029–1926 m depth). [Bunger 2010, pp. 3-4]
- Distributions shown for three representative zones: zone 1 (1029–1079 m) right‑tail dominated; zone 5 (1563–1575 m); zone 8 (1887–1926 m) bell‑shaped. [Bunger 2010, pp. 3-4]

## Methods
- **Discing criterion**: the elastic, tensile‑strength‑based criterion of Matsuki et al. (2004) [Eqs. (1)–(3)]; core‑stub length Ls related to disc length L by empirical relationship. [Bunger 2010, pp. 4-5]
- **Stochastic model**: in situ stresses (rx, ry, rz) and tensile strength (rt) assumed to follow independent Gaussian distributions. A Monte‑Carlo algorithm convolves these distributions to compute the probability of discing at each length bin. [Bunger 2010, pp. 5-6, 6-7]
- **Probabilistic framework**: abstracted using set notation and joint probabilities [Eqs. (14)–(17)]; bin probabilities calculated via Monte‑Carlo estimation of joint probability p(b ≥ 0). [Bunger 2010, pp. 7-8, 11-12]
- **Parameter fitting**: visual best‑fit of complementary cumulative density functions (CCDF) between model and data; mean vertical stress fixed from rock density (0.0263 MPa/m), mean tensile strength fixed from Brazilian tests (8.9 MPa), stress standard deviation fixed from density variation (0.3 MPa); fitted parameters std(rt), hrxi, hryi. [Bunger 2010, pp. 8-9]

## Key Findings
1. The observed transition from right‑tail‑dominated to bell‑shaped disc length distributions with increasing depth can be reproduced by a convolution of normally distributed stress and strength with the Matsuki et al. (2004) discing criterion. [Bunger 2010, pp. 6-7, 8-9]
2. Visual best‑fit comparisons (Figs. 9–11) show good agreement between model and data for all eight zones. [Bunger 2010, pp. 9-10]
3. Stress estimates (Fig. 12) from core discing provide a reasonable estimate of maximum horizontal stress rx compared with micro‑hydraulic fracturing and wellbore breakout data, but overestimate the minimum horizontal stress ry. [Bunger 2010, pp. 10-11]
4. Best‑fit parameters (Table 1) show reasonable consistency across zones. [Bunger 2010, pp. 9-10]
5. The stochastic method captures the full distribution and allows application of existing deterministic discing criteria even when a typical disc length is not well‑defined. [Bunger 2010, pp. 11-12]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Disc length distributions shift from right‑tail‑dominated (zone 1) to bell‑shaped (zone 8) with depth. | [Bunger 2010, pp. 3-4] Figs. 2–4 | 1029–1926 m depth, granite | Over 5400 fragments measured. |
| Convolution of Gaussian distributed rx,ry,rz,rt with Matsuki et al. (2004) criterion produces right‑tail‑dominated and bell‑shaped distributions when mean rz increased. | [Bunger 2010, pp. 6-7] Fig. 8 | hrzi = 28 MPa (right‑tail) vs 60 MPa (bell‑shaped), fixed stress ratios and tensile strength stats | Demonstrates hypothesis. |
| Visual best‑fit of CCDF between model and data for zones 1, 5, 8 using fitted std(rt), hrxi, hryi and fixed hrzi, std(r), hrti. | [Bunger 2010, pp. 9-10] Figs. 9–11, Table 1 | Fitted values in Table 1 | Probability densities and CCDF matched well. |
| Core discing stress estimates compared to micro‑hydraulic fracturing and wellbore breakouts: good estimate of rx, overestimate of ry. | [Bunger 2010, pp. 10-11] Fig. 12 | Depth 800–2000 m | Supports method validity for maximum horizontal stress. |
| Stresses and strength assumed independent; cluster length scales much smaller than zone length supports ignoring spatial correlation. | [Bunger 2010, pp. 3-4] | Zones ~40–70 m, clusters <1 m | Assumption justified for this dataset. |

## Limitations
- Underlying discing criterion is purely elastic and does not account for post‑peak behaviour, shear suppression of tensile discing, or plasticity. [Bunger 2010, pp. 4-5]
- The criterion does not consider thermoporoelastic stresses, mud pressure, or bit geometry differences (HQ vs NQ2). [Bunger 2010, pp. 10-11]
- Inverse parameter fitting is difficult due to strong covariance among parameters, noisy objective function, and data‑poor tails; only visual best‑fit used here. [Bunger 2010, pp. 8-9]
- Very short discs (L/R < 0.218) not handled by the criterion; Ls ≈ L assumed. [Bunger 2010, pp. 4-5]
- Gaussian distribution assumption for stresses and strength may not be appropriate; spatial correlation not explicitly modelled. [Bunger 2010, pp. 11-12]
- The method estimates only normal stress components acting perpendicular and parallel to the core axis; not a full stress tensor unless disc geometry is also used. [Bunger 2010, pp. 8-9]

## Assumptions / Conditions
- In situ stresses rx, ry, rz and tensile strength rt are each described by independent Gaussian distributions with zero spatial correlation over the zone length. [Bunger 2010, pp. 5-6, 7-8]
- Core discing occurs when the elastic tensile stress at the base of the core stub reaches rt; disc length is predicted by the Matsuki et al. (2004) criterion. [Bunger 2010, pp. 4-5]
- Core axis is aligned with a principal stress direction; stress components in the plane perpendicular to the core need not be principal. [Bunger 2010, pp. 2-3, 4-5]
- For short discs, Ls ≈ L is used, extending the criterion beyond its explicit range. [Bunger 2010, pp. 4-5]
- Variation of tensile strength dominates the randomness; stress standard deviation is negligible unless it reaches 5–10% of mean stress. [Bunger 2010, pp. 8-9]
- Fracturing is predominantly tensile (no shear‑mode suppression) based on visual examination and fracture morphology. [Bunger 2010, pp. 2-3, 10-11]

## Key Variables / Parameters
- `rx`, `ry` – maximum and minimum normal stress perpendicular to core axis [Bunger 2010, pp. 4-5]
- `rz` – normal stress parallel to core axis [Bunger 2010, pp. 4-5]
- `rt` – tensile strength of rock [Bunger 2010, pp. 4-5]
- `L` – disc length; `R` – core radius; normalised disc length `L/R` [Bunger 2010, pp. 3-4]
- `kx(Ls/R)`, `ky(Ls/R)`, `kz(Ls/R)` – numerically determined discing coefficients [Bunger 2010, pp. 4-5]
- `hrai`, `std(ra)` – mean and standard deviation of each parameter [Bunger 2010, pp. 5-6]
- `by` = hryi / hrzi; `cx` such that hrxi = (1 + c²ₓ) hryi [Bunger 2010, pp. 9-10]
- `p(Li)` – probability of disc forming at length Li [Bunger 2010, pp. 7-8]

## Reusable Claims
1. When core disc length distributions are non‑Gaussian, a stochastic approach that models the entire distribution can enable stress estimation by convolving assumed distributions of in situ parameters with a deterministic discing criterion. [Bunger 2010, pp. 1-2, 11-12] **Condition** – requires a valid discing criterion and sufficient data for zone‑wide statistics; spatial correlation length must be small relative to zone size.
2. A shift from right‑tail‑dominated to bell‑shaped disc length distributions can be explained by increasing mean stress acting parallel to the core axis, while keeping stress ratios and strength variability constant. [Bunger 2010, pp. 6-7] **Condition** – using an elastic tensile‑failure criterion and Gaussian stress/strength distributions.
3. The probabilistic framework (Eqs. 12–17) is general and can incorporate any discing criterion (elastic or elasto‑plastic) provided it can be expressed as a set of non‑negativity constraints on a vector b = K(L)x. [Bunger 2010, pp. 7-8] **Condition** – linear criterion facilitates computation; nonlinear criterion can still be used via Monte‑Carlo.
4. For the South Australian granite data, the discing analysis yielded a reasonable estimate of maximum horizontal stress but systematically overestimated minimum horizontal stress compared with micro‑hydraulic fracturing. [Bunger 2010, pp. 10-11] **Condition** – may reflect missing mechanisms (thermoporoelasticity, mud pressure, bit geometry) or inaccurate discing criterion.
5. The approach of fixing mean vertical stress from density and mean tensile strength from laboratory tests, then fitting only stress ratios and strength dispersion, can provide first‑order stress estimates. [Bunger 2010, pp. 8-9] **Condition** – requires independent constraints on vertical stress and tensile strength.

## Candidate Concepts
- [[core discing]]
- [[stochastic approach]]
- [[in situ stress estimation]]
- [[disc length distribution]]
- [[non-Gaussian distribution]]
- [[right-tail dominated distribution]]
- [[bell-shaped distribution]]
- [[elastic discing criterion]]
- [[complimentary cumulative density function (CCDF)]]
- [[tensile strength variability]]
- [[spatial correlation length]]
- [[probabilistic framework]]
- [[joint probability]]
- [[inverse modeling]]

## Candidate Methods
- [[Matsuki et al. (2004) discing criterion]]
- [[Monte-Carlo convolution]]
- [[probabilistic discing model (Bunger 2010)]]
- [[visual best-fit matching of CCDF]]
- [[joint probability computation via Monte-Carlo]]
- [[fixed-parameter fitting approach]]

## Connections To Other Work
- Builds on the discing criterion of [[Matsuki et al. 2004]] and numerical stress analysis by [[Kaga et al. 2003]]. [Bunger 2010, pp. 4-5]
- References early core discing stress analysis by [[Cook 1962]], [[Jaeger & Cook 1963]], [[Obert & Stephenson 1965]]. [Bunger 2010, pp. 1-2]
- Compares with elasto‑plastic analysis of [[Corthésy & Leite 2008]], who emphasised that shear failure can suppress tensile discing. [Bunger 2010, pp. 4-5]
- Stress results compared with micro‑hydraulic fracturing ([[Cornet 1986]] method) and wellbore breakout analysis by [[Klee et al. 2008]]. [Bunger 2010, pp. 10-11]
- Related to work by [[Ishida & Saito 1995]] and [[Zhu et al. 1985]] on disc length distributions and stress criteria. [Bunger 2010, pp. 1-2]

## Open Questions
- How to extend the discing criterion to very short discs (L/R < 0.25)? [Bunger 2010, pp. 4-5]
- What is the effect of thermoporoelastic stresses, mud pressure, and bit geometry on predicted disc length distributions? [Bunger 2010, pp. 10-11]
- Can elasto‑plastic models that account for shear suppression lead to better agreement for minimum horizontal stress? [Bunger 2010, pp. 10-11]
- How should spatial correlation of stress and strength be incorporated, and does it affect the overall distribution? [Bunger 2010, pp. 11-12]
- What robust inverse method can overcome parameter covariance and data‑poor tails? [Bunger 2010, pp. 8-9]
- Are Gaussian distributions appropriate for in situ stress and strength, or do alternative distributions (e.g., log‑normal) provide better fits? [Bunger 2010, pp. 11-12]

## Source Coverage
All 11 non‑empty indexed source blocks were processed.  
Coverage by blocks: 1.0 (100%)  
Coverage by characters: 1.004773 (≈100.48%)  
No content outside the indexed fragments was introduced.
