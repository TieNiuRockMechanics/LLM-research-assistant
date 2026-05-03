---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2010-davy-a-likely-universal-model-of-fracture-scaling-and-its-consequence-for-crustal-hydromech"
title: "A Likely Universal Model of Fracture Scaling and Its Consequence for Crustal Hydromechanics."
status: "draft"
source_pdf: "data/papers/2010 - A likely universal model of fracture scaling and its consequence for crustal hydromechanics.pdf"
collections:
citation: "Davy, P., et al. \"A Likely Universal Model of Fracture Scaling and Its Consequence for Crustal Hydromechanics.\" *Journal of Geophysical Research*, vol. 115, B10411, 2010. doi:10.1029/2009JB007043."
indexed_texts: "16"
indexed_chars: "77669"
nonempty_source_blocks: "16"
compiled_source_blocks: "16"
compiled_source_chars: "78001"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004275"
coverage_status: "full-index"
source_signature: "6b65bd83d5873faf6d2711bdaa2215f9e168821f"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T13:51:04"
---

# A Likely Universal Model of Fracture Scaling and Its Consequence for Crustal Hydromechanics.

## One-line Summary

A simple geometrical rule—that fractures statistically do not cross larger ones—leads to a self‑similar fracture‑length distribution in dense networks with a nearly constant density term, and this “universal fracture model” (UFM) explains observed scaling of both joint and fault systems and implies that crustal fracture networks are close to the percolation threshold with critical flow organization.

## Research Question

Why do fracture networks ubiquitously exhibit power‑law length scaling, and can a basic model of fracture‑to‑fracture mechanical interactions reproduce the observed density distributions and their consequences for crustal hydromechanics? [Davy 2010, pp. 1-2]

## Study Area / Data

- **Hornelen Basin joint network (Norway)** – multiscale outcrop maps (18–720 m); 7 networks analysed [Davy 2010, pp. 4-5]
- **Swedish crystalline basement** – SKB site investigation at Simpevarp and Laxemar; outcrop maps (0.5–10 m) and regional lineament maps (100 m–10 km) [Davy 2010, pp. 5-6]
- **San Andreas fault system (California)** – compiled fault‑trace map, system size \(L = 450\) km [Davy 2010, pp. 5-6]
- **Experimental fault networks** – R15 sand‑box experiment (Davy et al. 1995) [Davy 2010, pp. 7-8]
- **Numerical fault‑network simulations** – Hardacre & Cowie (2003b) 2‑D elastoplastic model [Davy 2010, pp. 6-7]

## Methods

1. **Theoretical derivation**  
   - From the statistical rule that a fracture stops when it intersects a larger one, and that the distance to the nearest larger fracture scales as \(d \sim \bigl(L/C(l,L)\bigr)^{1/D}\) with \(D\) the fractal dimension of fracture centres, the condition \(l = \gamma d\) yields a cumulative distribution \(C_{\text{dense}}(l,L)\) and a density distribution \(n_{\text{dense}}(l,L) = D\gamma^D L^D \, l^{-(D+1)}\) [Davy 2010, pp. 2-3].

2. **Transition length**  
   - Combining the dilute‑regime distribution \(n_{\text{dilute}}(l,L) = \alpha L^D l^{-a}\) (growth rate exponent \(a\)) with the dense‑regime distribution gives a crossover length \(l_c = \bigl(\alpha/(\gamma^D)\bigr)^{1/(D+1-a)}\) [Davy 2010, pp. 3-4].

3. **Numerical simulations**  
   - 2‑D networks generated with an initial power‑law length distribution (\(a = 2.3\)) and then clipped where a fracture intersected a larger one. Evaluated for uniform, orthogonal, and acute orientation sets to estimate \(\gamma\) [Davy 2010, pp. 4-5].

4. **Data analysis**  
   - Fitting of the UFM density function (Eq. 6) to measured fracture‑trace length distributions from the Hornelen, Swedish, and San Andreas datasets [Davy 2010, pp. 4-6].  
   - Calculation of the percolation parameter \(p\) for the combined dilute‑dense model and comparison with 2‑D percolation thresholds [Davy 2010, pp. 9-10].

5. **Flow simulation**  
   - Flow computed on UFM networks at and above percolation threshold; comparison with classical percolation networks and power‑law length models [Davy 2010, pp. 10-11].

## Key Findings

1. **Two‑regime organisation**  
   Fracture systems consist of a dilute regime (small fractures grow independently) and a dense regime (growth controlled by mechanical interactions). The transition length \(l_c\) is ~20 km for faulting and 1–10 m for jointing [Davy 2010, pp. 3-4, 7‑8, 11].

2. **Universal dense‑regime distribution**  
   In the dense regime the length distribution is self‑similar with exponent \(a = D+1\). The density term is fully set by \(D\) and a geometric factor \(\gamma\), which varies only between ~1 and 2, making the model nearly universal [Davy 2010, pp. 3-4, 5, 11].

3. **Empirical support**  
   - Hornelen joint network: \(n(l,L) = 4.5 \, l^{-2.8} L^{1.8}\) → \(\gamma = 1.7 \pm 0.2\) [Davy 2010, pp. 4-5].  
   - Swedish outcrop (high‑density case): \(n(l,L) = 4 \, l^{-3} L^{2}\) [Davy 2010, pp. 5-6].  
   - San Andreas fault system (large scales): \(n(l,L) = 4 \, l^{-2.7} L^{1.7}\) [Davy 2010, pp. 5-6].  
   All are consistent with \(D+1\) exponents and a density term \(D\gamma^D \approx 4\).

4. **Fault‑versus‑joint differences**  
   - Faults have smaller fractal dimension (\(D \approx 1.7\) vs. 1.8‑2.0 for joints) and a much larger \(l_c\).  
   - Large‑scale localisation in faulting inhibits small‑fault growth, whereas jointing may be driven by internal stresses that permit continued densification [Davy 2010, pp. 7-8].

5. **Critical connectivity and flow**  
   - The UFM network is just above the percolation threshold for system sizes \(L \gtrsim l_c\).  
   - Even well above threshold, a large fraction of nodes carry a substantial portion of total flow, indicating that small changes in fracture connectivity can cause large hydraulic changes [Davy 2010, pp. 10-11].

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Dense‑regime distribution \(n = D\gamma^D L^D l^{-(D+1)}\) derived from \(l = \gamma d\) | [Davy 2010, pp. 2-3] | Fracture centres fractal; distance to nearest larger neighbour scales as \(d \sim (L/C)^{1/D}\) | Only distribution satisfying the rule; equivalent to self‑similarity |
| Numerical simulations yield \(\gamma=1\) for isotropic/orthogonal sets and \(\gamma=1.5–1.7\) for 20° sets | [Davy 2010, pp. 4-5] | 2‑D, strict intersection rule, starting with \(a = 2.3\) | \(\gamma\) range seems narrow |
| Hornelen Basin joint networks fit \(n(l,L) = 4.5 \, l^{-2.8} L^{1.8}\); \(\gamma = 1.7 \pm 0.2\) | [Davy 2010, pp. 4-5] | Outcrops 18–720 m; a single UFM distribution across all scales | No upper scale limit detected; lower limit ~1 m |
| Swedish outcrop (high density of small fractures) fits \(n(l,L) = 4 \, l^{-3} L^{2}\) | [Davy 2010, pp. 5-6] | Exhaustively mapped, lengths >50 cm; through‑scale model | Density term ~4 |
| San Andreas fault system (large‑scale dense regime) fits \(n(l,L) = 4 \, l^{-2.7} L^{1.7}\); \(L=450\) km | [Davy 2010, pp. 5-6] | Fault traces; fractal dimension \(D=1.7\); \(l_c \sim 20\) km | Good fit for faults >20 km |
| Transition length \(l_c\) ~20 km for faults, 1–10 m for joints | [Davy 2010, pp. 7-8] | Observed across multiple datasets | Difference attributed to localisation vs. internal stress |
| Percolation parameter \(p\) just exceeds threshold when \(L > l_c\); flow distribution remains long‑tailed above threshold | [Davy 2010, pp. 10-11] | 2‑D UFM networks compared with classical percolation and power‑law models | Network remains critical; many nodes carry large flow |
| UFM does not apply where fracture growth is controlled by layer thickness (e.g., rubber‑pad experiments) | [Davy 2010, pp. 6-7] | Systems with external mechanical length scale | Example: Spyropoulos et al. (1999), Ackermann et al. (2001) |

## Limitations

- The UFM is derived from a extremely simplified rule; real systems obey it only probabilistically. [Davy 2010, pp. 2-3]
- Testing the dense‑regime scaling on faults is difficult because the scaling range is very narrow (a few large fractures). [Davy 2010, pp. 7-8]
- Exhaustive fracture sampling is rare; many geological maps do not meet the completeness required for scaling analysis. [Davy 2010, pp. 4-5]
- The numerical simulations are “toy” models with strict intersection rules; they do not capture dynamic growth or realistic stress interactions. [Davy 2010, pp. 4-5]
- The model does not apply to fracture systems where an external mechanical length (e.g., layer thickness) controls scaling. [Davy 2010, pp. 6-7]
- The transition to dense regime assumes \(a < D+1\); the opposite case would lead to a dense‑to‑dilute transition and is not treated in detail. [Davy 2010, pp. 3-4]
- Transport properties were only calculated on 2‑D UFM‑like networks; full 3‑D flow analysis is lacking. [Davy 2010, pp. 10-11]

## Assumptions / Conditions

- **Quasi‑static fracturing**: most fracture growth is controlled by the stress field perturbations of existing fractures, with a perturbation length of the order of the fracture length. [Davy 2010, pp. 1-2]
- **Hierarchical inhibition**: large fractures suppress the growth of smaller ones in their vicinity, but not vice‑versa. [Davy 2010, pp. 2-3]
- **Statistical rule**: a fracture stops when it intersects a larger one, so that its length statistically equals the distance to the nearest larger fracture. [Davy 2010, pp. 2-3]
- **Fractal fracture centres**: the positions of fracture centres have a correlation (mass) dimension \(D\), which can be smaller than the embedding space dimension. [Davy 2010, pp. 2-3]
- **Dilute growth follows a power‑law growth rate** \(dl/dt \propto l^a\), with \(a < D+1\). [Davy 2010, pp. 2-3]
- **Fractures are modelled as line segments in 2‑D** for trace analysis; 3‑D to 2‑D stereological relationships are given in Appendix A. [Davy 2010, pp. 4-5, 11‑12]
- **The dimensionless parameter \(\gamma\)** captures the effects of orientation distributions and deviations from the strict intersection rule. [Davy 2010, pp. 3-4]

## Key Variables / Parameters

- \(l\) – fracture length  
- \(L\) – system size  
- \(n(l,L)\) – number of fractures with length in \([l, l+dl]\) in a system of size \(L\)  
- \(D\) – fractal (correlation) dimension of fracture centres  
- \(\gamma\) – dimensionless geometric factor (order 1–2)  
- \(a\) – exponent in the growth‑rate power law and in the dilute‑regime length distribution  
- \(l_c\) – crossover length between dilute and dense regimes  
- \(\alpha\) – density term of the dilute‑regime distribution  
- \(p\) – percolation parameter  
- \(l_{\text{inc}}\) – portion of fracture length inside the system volume [Davy 2010, pp. 2-3, 3‑4, 9‑10]

## Reusable Claims

- **Claim**: In dense fracture networks where large fractures inhibit smaller ones, the statistically inevitable length distribution is self‑similar with exponent \(a = D+1\) and a density term \(D\gamma^D\). The parameter \(\gamma\) appears to vary only between 1 and 2, making the distribution nearly universal.  
  **Conditions**: applicable when fracture growth is predominantly limited by interactions among fractures, not by an external mechanical length scale; fracture centres must have a well‑defined fractal dimension \(D\); the rule “a fracture stops when crossing a larger one” holds statistically. [Davy 2010, pp. 2-3, 3‑4, 11]

- **Claim**: Fracture networks transition from a dilute growth regime (small fractures) to a dense interaction‑controlled regime (large fractures) at a length \(l_c\) that depends on the dilute‑regime density and the UFM parameters. For natural faults \(l_c\) is of order 10–20 km; for joints it is 1–10 m.  
  **Conditions**: this holds if the growth‑rate exponent \(a < D+1\) and the system has reached a sufficient density for interactions to dominate. [Davy 2010, pp. 3-4, 7‑8]

- **Claim**: The UFM yields a fracture density distribution that fits both joint and fault datasets with a single density term \(D\gamma^D \approx 4\), suggesting a common geometrical control despite different forcing mechanisms.  
  **Conditions**: validated on the Hornelen joint network, SKB Swedish outcrops, and the San Andreas fault system; requires complete length sampling. [Davy 2010, pp. 4-6]

- **Claim**: UFM‑type networks are near the percolation threshold and retain a critical flow structure even well above threshold, with many nodes carrying a large fraction of total flow. Small changes in fracture intersection can therefore drastically alter permeability.  
  **Conditions**: analysis performed on 2‑D networks; the effect is tied to the fractal and self‑similar organisation of the dense regime. [Davy 2010, pp. 10-11]

## Candidate Concepts

- [[dilute fracture regime]]
- [[dense fracture regime]]
- [[universal fracture model (UFM)]]
- [[self‑similar fracture network]]
- [[fractal dimension of fracture centres]]
- [[fracture percolation]]
- [[critical fracture connectivity]]
- [[fracture‑to‑fracture mechanical interaction]]
- [[lacunarity of fractal fracture networks]]
- [[fault‑versus‑joint scaling]]

## Candidate Methods

- [[solving for self‑similar length distribution from intersection rule]]
- [[estimating γ from numerical fracture‑network simulations]]
- [[fitting UFM to observed fracture trace length distributions]]
- [[calculating percolation parameter for combined dilute‑dense model]]
- [[stereological conversion from 3D fractures to 2D traces (disks-to-lines)]]
- [[flow frequency distribution analysis on discrete fracture networks]]

## Connections To Other Work

- **Scaling of fracture systems**: builds on the review by Bonnet et al. (2001) and previous analyses of Hornelen (Odling 1997; Bour et al. 2002) [Davy 2010, pp. 1-2, 4‑5]
- **Fractal fracture networks and connectivity**: relates to Bour & Davy (1997, 1998, 1999); Darcel et al. (2003b); Berkowitz et al. (2000) on percolation in power‑law and fractal networks [Davy 2010, pp. 8-10]
- **Mechanical interaction rules**: inspired by Segall & Pollard (1983), Nur (1982), Renshaw & Pollard (1994) [Davy 2010, pp. 2-3]
- **Experimental faulting**: compared with the sand‑box experiments of Davy et al. (1995) and the numerical models of Hardacre & Cowie (2003b) [Davy 2010, pp. 6-7]
- **Fault growth models**: references to Sornette & Davy (1991), Cowie et al. (1995), Lyakhovsky (2001) for dilute‑regime scaling [Davy 2010, pp. 2-3]
- **Joint spacing and layer thickness**: contrasts with the scenarios of Wu & Pollard (1995) and rubber‑pad models (Spyropoulos et al. 1999; Ackermann et al. 2001) where an external length scale dominates [Davy 2010, pp. 6-7]
- **Self‑organised criticality**: the dense‑regime self‑similarity is discussed in the context of critical dynamics (Bak et al. 1988; Sornette et al. 1990) [Davy 2010, pp. 1-2]

## Open Questions

- **Origin of the difference in \(l_c\) between faulting and jointing**: Why does large‑scale localisation suppress small‑fault growth while jointing continues to densify? Role of internal stresses needs further investigation. [Davy 2010, pp. 8-9]
- **Detailed connectivity and transport properties of UFM networks**: aspects such as assortativity, topology, averaging properties, and the influence of intersection‑length distribution remain to be studied. [Davy 2010, pp. 10-11]
- **Applicability to other fracture systems**: does the UFM hold for fracture networks in different tectonic settings, fluid‑driven fracture, or dynamic fracturing? [Davy 2010, pp. 8-9]
- **Refinement of the γ parameter**: what is the exact dependence of γ on orientation distribution and correlation, and can it be predicted from mechanical models? [Davy 2010, pp. 3-4]
- **Universality of the density term**: is the value \(D\gamma^D \approx 4\) indeed universal, or does it vary systematically with lithology, stress state, or boundary conditions? [Davy 2010, pp. 5-6]
- **Mechanistic validation**: the model relies on a statistical rule; direct mechanical modelling (e.g., incorporating stress interactions explicitly) is needed to test the underlying assumptions. [Davy 2010, pp. 4-5]

## Source Coverage

All 16 non‑empty indexed fragments from the paper were processed, covering the full article from page 1 to 13. Indexed characters: 77 669; compiled source characters: 78 001; coverage ratio by blocks: 1.0; coverage ratio by chars: ≈1.004. No content outside the supplied fragments was used.
