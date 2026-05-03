---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2005-schorlemmer-variations-in-earthquake-size-distribution-across-different-stress-regimes"
title: "Variations in Earthquake-Size Distribution across Different Stress Regimes."
status: "draft"
source_pdf: "data/papers/2005 - Variations in earthquake-size distribution across different stress regimes.pdf"
collections:
  - "3文章 裂缝网络联通渗透性"
citation: "Schorlemmer, Danijel, et al. “Variations in Earthquake-Size Distribution across Different Stress Regimes.” *Nature*, vol. 437, no. 7057, 2005, pp. 539-42."
indexed_texts: "5"
indexed_chars: "22125"
nonempty_source_blocks: "5"
compiled_source_blocks: "5"
compiled_source_chars: "22261"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.006147"
coverage_status: "full-index"
source_signature: "667c972965a11beb02c0c09fb4e67b29c4c2311c"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T12:47:50"
---

# Variations in Earthquake-Size Distribution across Different Stress Regimes.

## One-line Summary
The b‑value of the earthquake frequency–magnitude distribution varies systematically with style of faulting – normal events show the highest b, thrust events the lowest – and can be interpreted as a **stress meter** that depends inversely on differential stress. [Schorlemmer 2005, pp. 1-1]

## Research Question
It had been uncertain whether observed variations of the b‑value in laboratory experiments, mines, and tectonic settings are caused by different stress regimes, or whether b ≈ 1 is a universal constant for earthquakes when large volumes are sampled. [Schorlemmer 2005, pp. 1-1]

## Study Area / Data
Five high‑quality earthquake catalogues were used, all restricted to source depths ≤ 50 km and periods of homogeneous recording above the local magnitude of completeness Mc [Schorlemmer 2005, pp. 1-1, 1‑2]:
- **Global Harvard CMT moment tensor catalogue** (1980–2004, Mc = 5.5, N = 7 636)
- **Southern California SCSN catalogue** (1981–2003, Mc = 2.5, N = 14 003) – relocated events with 3‑D velocity model, highest‑quality regional dataset
- **Northern California NCSN catalogue** (1981–2004, Mc = 3.0, N = 4 250)
- **NEID F‑Net all‑Japan catalogue** (1997–2004, Mc = 4.5, N = 1 579)
- **NEID Kanto‑Tokai catalogue** (1982–2003, Mc = 3.0, N = 2 337) – volcanic/geothermal areas excluded, coordinates listed. [Schorlemmer 2005, pp. 1-2, 1‑1]

## Methods
- **b‑value estimation**: maximum‑likelihood method (Bender 1983), uncertainties from Shi & Bolt (1982). Magnitudes binned to ΔM = 0.1. [Schorlemmer 2005, pp. 1-1]
- **Minimum sample size**: ≥ 100 events required; computations with 100–200 events are flagged with dashed error bars. [Schorlemmer 2005, pp. 1-1]
- **Focal mechanism classification**: based on rake angle λ (Aki–Richards convention). Strike‑slip: λ = 0° or ±180°; thrust: λ = 90°; normal: λ = −90°. Two analyses:
  1. **b‑l plot**: b as a function of rake λ with fixed range γ (20° for SCSN, 60° for F‑Net, 40° for others).
  2. **b‑γ plot**: b as a function of range γ (175° → 5°, step −10°) where both nodal‑plane rakes must fall within the range. [Schorlemmer 2005, pp. 1-1]
- **Significance testing**: Utsu test; log P<sub>b</sub> ≤ −1.3 (significant) and ≤ −1.9 (highly significant). [Schorlemmer 2005, pp. 1-1]
- **Quality filtering**: solution misfit ≤ 0.2, station distribution ratio ≥ 0.5 for Californian catalogues; misfit criterion for Kanto‑Tokai. [Schorlemmer 2005, pp. 1-1]

## Key Findings
- **Systematic b‑value ordering**: In every catalogue, normal faulting events have the highest b, strike‑slip events intermediate, and thrust events the lowest (b<sub>NR</sub> > b<sub>SS</sub> > b<sub>TH</sub>). [Schorlemmer 2005, pp. 1-2]
- **SCSN details** (γ = 5°): b<sub>TH</sub> ≈ 0.72 ± 0.05, b<sub>SS</sub> = 1.00 ± 0.05, b<sub>NR</sub> = 1.11 ± 0.08; differences are highly significant (log P<sub>b</sub> ≤ −3.61 for thrust vs. normal). [Schorlemmer 2005, pp. 1-2, 2‑4 Table 2]
- **Harvard CMT** (γ = 5°): b<sub>TH</sub> = 0.81 ± 0.03, b<sub>SS</sub> = 1.13 ± 0.05, b<sub>NR</sub> = 1.17 ± 0.08; same ordering. Using only the first nodal plane improves separation. [Schorlemmer 2005, pp. 1-2, 2‑4 Table 2]
- **Other catalogues** (NCSN, Kanto‑Tokai, F‑Net) show the same pattern; clear separation can be lost for narrow γ when sample size is small. [Schorlemmer 2005, pp. 1-2, 2‑4]
- **Universal inverse stress‑b relationship**: Because mean stress levels obey σ̅<sub>TH</sub> > σ̅<sub>SS</sub> > σ̅<sub>NR</sub> for a given vertical stress, the observed b ordering implies that b is inversely proportional to differential stress Δσ. Thus, b acts as a “stressmeter” in the Earth’s crust. [Schorlemmer 2005, pp. 1-2, 2‑4]
- **Consistency with prior work**: Kagan (1987–1999 Harvard CMT) found b<sub>NR</sub>=0.731 > b<sub>SS</sub>=0.643 > b<sub>TH</sub>=0.642, matching the same relation. [Schorlemmer 2005, pp. 2-4]
- **Physical mechanisms**: Scholz (1968) explains that in high‑differential‑stress environments, more subvolumes are near failure, so ruptures grow larger → lower b. Amitrano (2003) emphasises confining pressure: at high pressure, internal friction angle decreases, allowing interactions in all directions, thus larger failures. [Schorlemmer 2005, pp. 2-4, 4‑4]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| SCSN: b<sub>TH</sub>=0.72(05), b<sub>SS</sub>=1.00(05), b<sub>NR</sub>=1.11(08) (γ=5°); log P<sub>b</sub>(TH‑NR)=−3.61 | [Schorlemmer 2005, pp. 2-4] | M≥2.5, depth all, solution misfit≤0.2, station ratio≥0.5 | Highest‑quality regional catalogue with 3‑D velocity model |
| Harvard CMT: b<sub>TH</sub>=0.81(3), b<sub>SS</sub>=1.13(5), b<sub>NR</sub>=1.17(8) (γ=5°); log P<sub>b</sub>(TH‑NR)=−3.67 | [Schorlemmer 2005, pp. 2-4] | M≥5.5, depth 0‑50 km | Global data; ordering persists, clearer when using only first nodal plane |
| NCSN: b<sub>TH</sub>=0.73(4), b<sub>SS</sub>=0.91(2), b<sub>NR</sub>=1.00(4) (γ=45°) | [Schorlemmer 2005, pp. 2-4] | Northern California, M≥3.0 | b<sub>TH</sub> significantly lower than b<sub>SS</sub> (log P<sub>b</sub>=−3.50) |
| Kanto‑Tokai: b<sub>TH</sub>=0.66(2), b<sub>SS</sub>=0.90(4), b<sub>NR</sub>=1.06(7) (γ=45°) | [Schorlemmer 2005, pp. 2-4] | Japan, M≥3.0, volcanic areas excluded | Very high significance for TH‑SS (log P<sub>b</sub>=−7.50) |
| F‑Net: b<sub>TH</sub>=0.78(3), b<sub>SS</sub>=1.09(5), b<sub>NR</sub>=1.05(5) (γ=45°) | [Schorlemmer 2005, pp. 2-4] | All Japan, M≥4.5 | TH‑SS difference highly significant (log P<sub>b</sub>=−5.28) |
| Los Angeles Basin: b<sub>SS</sub>=1.1, b<sub>TH</sub>=0.7 (Hauksson 1990) | [Schorlemmer 2005, pp. 2-4] | Only 144 and 78 events | Supports general trend |
| Creeping vs. locked fault sections: low b on locked (high Δσ) sections, high b on creeping (low Δσ) sections | [Schorlemmer 2005, pp. 2-4, 4‑4] | Examples from Parkfield, other faults | Consistent with the stress‑meter interpretation |

## Limitations
- For narrow rake‑angle ranges γ, sample sizes drop below 200 (or 100), increasing errors; some catalogues lack data for γ = 5° in certain classes (e.g., NCSN, Kanto‑Tokai, F‑Net). [Schorlemmer 2005, pp. 1-2, 2‑4]
- Only crustal events (depth ≤ 50 km) included; deep events may obey different laws. [Schorlemmer 2005, pp. 1-1]
- The absolute level of b varies between regions and networks; only the relative ordering is considered universally valid. [Schorlemmer 2005, pp. 1-2]
- Local secondary effects from material heterogeneity and pore‑pressure changes can mask the primary stress dependence. [Schorlemmer 2005, pp. 1-2]

## Assumptions / Conditions
- The rake‑angle ranges for class definition (±γ) are chosen ad‑hominem per catalogue to balance smoothing and sample size: γ = 20° (SCSN), γ = 40° (NCSN, Harvard, Kanto‑Tokai), γ = 60° (F‑Net). [Schorlemmer 2005, pp. 1-1]
- Magnitude of completeness Mc is determined for each catalogue and period; these Mc values are assumed correct. [Schorlemmer 2005, pp. 1-1]
- Focal mechanisms have sufficient quality (misfit, station distribution) to reliably classify events. [Schorlemmer 2005, pp. 1-1]
- The relationship between faulting style and stress level – i.e. thrust faults are under higher mean stress than strike‑slip, which are under higher stress than normal faults for a given vertical stress – is taken as known. [Schorlemmer 2005, pp. 1-2]

## Key Variables / Parameters
- **b‑value**: slope of the earthquake frequency‑magnitude power‑law distribution. [Schorlemmer 2005, pp. 1-1]
- **Differential stress Δσ**: the controlling physical parameter inferred to vary inversely with b. [Schorlemmer 2005, pp. 1-2]
- **Rake angle λ**: used with prescribed ranges γ to classify events into normal, strike‑slip, or thrust. [Schorlemmer 2005, pp. 1-1]
- **Magnitude of completeness Mc**: lower cut‑off for catalogue processing. [Schorlemmer 2005, pp. 1-1]
- **Sample size N**: minimum 100 required; 200 used as threshold for robust error estimates. [Schorlemmer 2005, pp. 1-1]
- **Utsu test probability log P<sub>b</sub>**: measures significance of b‑value differences (≤ −1.3 significant, ≤ −1.9 highly significant). [Schorlemmer 2005, pp. 1-1]

## Reusable Claims
1. **Claim**: *In all analysed high‑quality earthquake catalogues, normal‑faulting events exhibit the highest b‑values, thrust events the lowest, and strike‑slip events intermediate b‑values.*  
   **Condition**: Applies to crustal depths (≤ 50 km) and requires robust focal mechanisms; the absolute b‑value level may differ but the relative ordering is consistent. [Schorlemmer 2005, pp. 1-2]  
2. **Claim**: *The b‑value can be interpreted as a stress meter that is inversely proportional to differential stress Δσ, because b<sub>TH</sub> < b<sub>SS</sub> < b<sub>NR</sub> matches the known stress ordering σ̅<sub>TH</sub> > σ̅<sub>SS</sub> > σ̅<sub>NR</sub>.*  
   **Limitation**: Local factors (material heterogeneity, pore pressure) can superimpose secondary effects. [Schorlemmer 2005, pp. 1-2]  
3. **Claim**: *The systematic b‑value variation is universal across scales (sub‑mm laboratory to 100s km faults) and tectonic environments.*  
   **Support**: Observed in laboratory experiments, mines, and regional‑to‑global catalogues. [Schorlemmer 2005, pp. 1-1, 2‑4]  
4. **Claim**: *Hazard analyses may benefit from separate recurrence estimates for each faulting style and from mapping spatial b‑value heterogeneities as proxies for differential stress.*  
   **Condition**: Requires sufficient data to compute style‑specific b‑values. [Schorlemmer 2005, pp. 4-4]  
5. **Claim**: *In a high‑stress (locked) fault section, b is low; in a low‑stress (creeping) section, b is high.*  
   **Evidence**: Reported for locked vs. creeping fault sections, and confirmed by the 2004 M6 Parkfield earthquake rupturing a previously mapped low‑b segment. [Schorlemmer 2005, pp. 2-4, 4‑4]

## Candidate Concepts
- [[b-value]]  
- [[faulting style]]  
- [[differential stress]]  
- [[seismic hazard]]  
- [[stressmeter]]  
- [[frequency-magnitude distribution]]  
- [[power-law]]  
- [[focal mechanism]]  
- [[rake angle]]  
- [[magnitude of completeness]]  
- [[maximum likelihood estimation]]  
- [[Utsu test]]  
- [[creeping fault]]  
- [[locked fault]]  
- [[fracture reservoir]]

## Candidate Methods
- [[Maximum-likelihood b-value estimation]] (Bender 1983)  
- [[Utsu test for b-value differences]]  
- [[Focal mechanism classification by rake angle]]  
- [[b-l plot analysis]]  
- [[b-g plot analysis]]  
- [[3-D velocity model relocation]]  
- [[Completeness magnitude Mc estimation]]

## Connections To Other Work
- **Kagan (1999, 2002)**: earlier analysis of Harvard CMT catalogue found a similar b ordering; the present study reproduces that result with refined data. [Schorlemmer 2005, pp. 2-4]  
- **Frohlich & Davis (1993)**: suggested b≈1 appears constant when large volumes are sampled; this study shows that systematic differences emerge when events are separated by faulting style. [Schorlemmer 2005, pp. 1-1]  
- **Scholz (1968)**: physical model linking low b to high differential stress because ruptures grow larger in high‑stress environments. [Schorlemmer 2005, pp. 2-4]  
- **Amitrano (2003)**: geometrical model emphasising confining pressure: at low confinement, failure is restricted in direction; at high confinement, interactions occur in all directions, leading to larger events. [Schorlemmer 2005, pp. 4-4]  
- **Hauksson (1990)**: Los Angeles basin data show b<sub>SS</sub>=1.1, b<sub>TH</sub>=0.7 from small samples, consistent with the global trend. [Schorlemmer 2005, pp. 2-4]  
- **Amelung & King (1997), Wiemer & Wyss (1997)**: creeping vs. locked fault sections show contrasting b‑values, reinforcing the stress‑dependent interpretation. [Schorlemmer 2005, pp. 2-4, 4‑4]  
- **Schorlemmer & Wiemer (2005)**: the 2004 Parkfield earthquake ruptured a low‑b patch, supporting the fault‑locking model. [Schorlemmer 2005, pp. 4-4]

## Open Questions
- Can a systematic decrease of b during the seismic loading cycle be detected? The expected amplitude of differential‑stress increase is much smaller than in laboratory or mining environments, and high‑quality datasets to test this may not yet exist. [Schorlemmer 2005, pp. 4-4]  
- To what extent do secondary effects (material heterogeneity, pore pressure) modify the stress‑b relationship in specific regions? [Schorlemmer 2005, pp. 1-2]  
- Why does depth not exhibit a systematic control on b, given that confining pressure increases with depth? Contradictory depth‑b trends are reported in California and Japan. [Schorlemmer 2005, pp. 1-2]  
- Is the relationship fully universal for very deep earthquakes (>50 km), which were excluded from this study? [Schorlemmer 2005, pp. 1-1]

## Source Coverage
All five non‑empty indexed fragments from the paper were processed and used to construct this page. Coverage metrics:  
- Indexed texts: 5  
- Indexed characters: 22,125  
- Non‑empty source blocks compiled: 5  
- Compiled source characters: 22,261  
- Coverage ratio by blocks: 1.0  
- Coverage ratio by characters: 1.006 (minor excess due to formatting)  
- Source signature: `667c972965a11beb02c0c09fb4e67b29c4c2311c`  
- Compilation strategy: single‑pass‑markdown, full index.
