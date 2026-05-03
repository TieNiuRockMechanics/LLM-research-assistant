---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2016-hyman-fracture-size-and-transmissivity-correlations-implications-for-transport-simulations"
title: "Fracture size and transmissivity correlations Implications for transport simulations in sparse three-dimensional discrete fracture networks following a truncate"
status: "draft"
source_pdf: "data/papers/2016 - Fracture size and transmissivity correlations Implications for transport simulations in sparse three-dimensional discrete fracture networks following a truncate.pdf"
collections:
citation: "Hyman, J. D., et al. \"Fracture Size and Transmissivity Correlations: Implications for Transport Simulations in Sparse Three-Dimensional Discrete Fracture Networks Following a Truncated Power Law Distribution of Fracture Size.\" *Water Resources Research*, 2016. doi:10.1002/2016WR018806."
indexed_texts: "20"
indexed_chars: "98299"
nonempty_source_blocks: "20"
compiled_source_blocks: "20"
compiled_source_chars: "98734"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004425"
coverage_status: "full-index"
source_signature: "315806c087fef677d4c3638f5af46f46a3c4c9e1"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T16:40:38"
---

# Fracture size and transmissivity correlations: Implications for transport simulations in sparse three-dimensional discrete fracture networks following a truncate

## One-line Summary

Adopting a positive correlation between fracture size and transmissivity in sparse 3‑D discrete fracture networks (DFNs) leads to consistently earlier breakthrough times and higher effective permeability than uncorrelated models, even when mean transmissivity is identical; fracture network geometry primarily determines where transport occurs, while the size–transmissivity relationship controls the flow speed [Hyman 2016, pp. 1-1].

## Research Question

How do different functional relationships between fracture size (radius) and transmissivity (aperture) influence flow and transport observables – effective permeability, breakthrough curves, transport resistance, active specific surface area, and network backbone structure – in sparse, three‑dimensional discrete fracture networks? [Hyman 2016, pp. 1-1] [Hyman 2016, pp. 1-2]

## Study Area / Data

A semigeneric synthetic DFN model was constructed loosely based on the sparsely fractured crystalline rock at the Forsmark site in Sweden (potential host for spent nuclear fuel). The network consists of three sets of circular fractures whose orientations follow a Fisher distribution and whose radii are drawn from a truncated power‑law distribution (exponent γ, lower cutoff r₀ = 15 m, upper cutoff rᵤ = 560 m) within a 1 km cubic domain. Fracture set parameters (trend, plunge, concentration, number of fractures) are given in Table 1 of the paper. The connected network density is barely above the percolation threshold (p = a·p꜀ with a ≈ 1.0–1.1) and the average P₃₂ for the connected part is 0.057 m⁻¹ [Hyman 2016, pp. 3-4] [Hyman 2016, pp. 4-5].

## Methods

The computational suite **dfnWorks** ([Hyman et al., 2015a]) was used to:
- Generate DFN geometry with the **feature rejection algorithm for meshing (FRAM)** and the **LaGriT** meshing toolbox.
- Solve steady‑state single‑phase flow (no gravity, Dirichlet BC: 1 MPa top, 2 MPa bottom) with the parallel code **PFLOTRAN**.
- Track passive, non‑reactive solute particles using **WALKABOUT** (Lagrangian particle tracking) with flux‑weighted injection at the inlet plane.
- For each particle trajectory, compute breakthrough time τ and transport resistance β (equation 10).
- Estimate network **effective permeability** from Darcy velocity at the outlet.
- Identify **backbones** (dominant transport paths) using a **flow topology graph** and optimal‑path algorithm (Aldrich et al., 2016).

Four size–transmissivity relationships were compared, all scaled to the same mean transmissivity:
1. **Correlated**: log(T) = log(a·rᵇ) — deterministic, positive correlation (equation 5).
2. **Semicorrelated**: log(T) = log(a·rᵇ) + σ_T·N(0,1) — log‑normal scatter around the correlated mean (equation 6).
3. **Uncorrelated**: log(T) = μ_T + σ_T·N(0,1) — independent log‑normal, no size dependence (equation 7).
4. **Constant**: log(T) = μ_T — uniform transmissivity (equation 8).

Parameters were chosen so that all models share the same mean transmissivity and the two stochastic models have similar transmissivity distributions (Table 2). For the deterministic models a single realization was used; for the semicorrelated and uncorrelated models 30 realizations of the transmissivity field were evaluated on the same fracture network, and an additional 30 independent network realizations were generated to test geometric variability [Hyman 2016, pp. 4-5] [Hyman 2016, pp. 5-6] [Hyman 2016, pp. 6-7] [Hyman 2016, pp. 7-8] [Hyman 2016, pp. 8-9] [Hyman 2016, pp. 9-10].

## Key Findings

- Even with identical mean transmissivity and nearly identical transmissivity distributions for the stochastic models, the **correlated and semicorrelated networks consistently exhibit higher effective permeability** (correlated value ≈ 2.5× the constant network) and **earlier breakthrough times** (median breakthrough 0.34× constant) than the uncorrelated/constant networks [Hyman 2016, pp. 10-11] [Hyman 2016, pp. 13-14].
- **Fracture network geometry is the primary control on transport pathways** (which fractures carry flow), while the adopted size–transmissivity relationship **controls the speed of flow and transport times**. Dominant backbones are composed of large fractures aligned with the flow direction, and these backbones are similar regardless of the correlation model [Hyman 2016, pp. 12-13] [Hyman 2016, pp. 14-15].
- **Tails of breakthrough time and transport resistance distributions exhibit similar power‑law scaling** (exponent ≈ 2), indicating that the size–transmissivity relationship does not strongly affect long‑term transport behaviour [Hyman 2016, pp. 11-12] [Hyman 2016, pp. 14-15].
- The **active specific surface area**, estimated from the linear τ–β relationship, is **15–20 % lower for correlated models** than for uncorrelated models, which could influence reactive transport predictions [Hyman 2016, pp. 12-13].
- **Flow channeling is more pronounced when a size–transmissivity correlation is included**: fewer fractures are touched by particles (43 % of fractures in correlated vs 52 % in constant) and a larger fraction of particles travels through the top backbones (49 % vs 29 %) [Hyman 2016, pp. 12-13] [Hyman 2016, pp. 13-14].
- Differences between flow and transport metrics persist across multiple independent network realizations, confirming that the observed effects are not due to a particular geometric sample [Hyman 2016, pp. 13-14].

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Perfectly correlated model effective permeability = 2.56 × constant network (values normalized by constant) | Table 3, [Hyman 2016, pp. 10-11] | Single DFN, mean transmissivity matched, cubic law, uniform aperture, no gravity | Semicorrelated values center around correlated; uncorrelated values center around constant |
| Semicorrelated mean effective perm. = 2.62 (variance 0.13); uncorrelated = 0.98 (var. 0.04) | Table 3 | 30 realizations per stochastic model on one geometry | |
| 50 % breakthrough time (τ) for correlated = 0.34; semicorrelated = 0.31; uncorrelated = 1.01; constant = 1.00 (normalized by constant) | Table 4 (τ), [Hyman 2016, pp. 12-13] | Same DFN, flux‑weighted injection | See Figure 4 |
| Power‑law exponent of τ tail: ≈2 for all models (range 1.84–2.18) | Table 4, [Hyman 2016, pp. 11-12] | Same conditions | Tail scaling insensitive to correlation model |
| Active specific surface area relative to constant: correlated Δ = 0.82 (var 0.003), semicorrelated 0.84 (var 0.02), uncorrelated 1.04 (var 0.02) | [Hyman 2016, pp. 12-13] | Median(β/τ) across particles, linear model R² > 0.9 | Correlated models 15–20 % lower |
| Percentage of fractures touched by particles: correlated 43 %, semicorrelated avg. 41 % (σ≈1 %), uncorrelated 50 % (σ≈1 %), constant 52 % | [Hyman 2016, pp. 13-14] | Single geometry; channeling more pronounced with correlation | |
| Particles traveling through top five backbones: correlated 49 % (backbone surface area 15 % of total), constant 29 % (20 % of total) | [Hyman 2016, pp. 13-14] | Same network | |

## Limitations

- The study is limited to **sparse 3‑D DFNs** with fracture radii following a **truncated power‑law distribution** and **hard upper/lower cutoffs** [Hyman 2016, pp. 15-16].
- Fracture aperture is **uniform within each fracture**; this assumption could interact with the correlation model to alter the magnitude of differences (but Makedonska et al. [2016] found in‑fracture variability had little effect on global transport properties in similar sparse networks) [Hyman 2016, pp. 15-16].
- Only the **cubic law** (T ∝ b³) was used; other aperture‑transmissivity relationships (e.g., quadratic law) could amplify or reduce the observed discrepancies [Hyman 2016, pp. 15-16].
- Particle injection is **flux‑weighted**; injection mode can influence travel time distributions [Hyman 2016, pp. 8-9].
- The network is **synthetic** and not calibrated to site‑specific flow data; parameter choices (low transmissivity variance, specific fracture set orientations) may limit direct applicability to other sites [Hyman 2016, pp. 15-16].
- Backbones were identified using a flow topology graph with specific balancing metrics; the method may not capture all channeling paths equally [Hyman 2016, pp. 9-10].

## Assumptions / Conditions

- Matrix is impermeable; all flow and transport occurs within fractures [Hyman 2016, pp. 3-4].
- Aperture is constant on each fracture and controls flow via the cubic law (T = (ρ g)/(12 μ) · b³) [Hyman 2016, pp. 4-5].
- Steady‑state flow, no gravity, Dirichlet boundary conditions (top 1 MPa, bottom 2 MPa), no‑flow lateral boundaries [Hyman 2016, pp. 7-8].
- Fracture shape: circular disks with radii drawn from truncated power‑law (Eq. 2); fracture centers uniformly distributed in the domain [Hyman 2016, pp. 3-4].
- Mean transmissivity is identical across all transmissivity models, and the distributions of aperture/transmissivity for the semicorrelated and uncorrelated models are similar (low variance, σ_T = 0.7–0.8) [Hyman 2016, pp. 6-7].
- Transport is purely advective (no local dispersion, no matrix diffusion or sorption in the primary comparison) [Hyman 2016, pp. 7-8].
- Particles are inserted with flux‑weighted mass to obtain stable travel time statistics [Hyman 2016, pp. 8-9].

## Key Variables / Parameters

**Fracture network generation Table 1, [Hyman 2016, pp. 4-5]**

| Set | Orientation (Fisher) | Power‑law exponent γ | r₀ (m) | rᵤ (m) | Number of fractures |
|-----|----------------------|----------------------|--------|--------|---------------------|
| NS  | h₀=90°, φ₀=0°, κ=21.7 | 2.5 | 15 | 560 | 2093 |
| NE  | h₀=135°, φ₀=0°, κ=21.5 | 2.7 | 15 | 560 | 2000 |
| HZ  | h₀=360°, φ₀=90°, κ=8.2 | 2.38 | 15 | 560 | 7711 |
Domain size: 1 km³; P₃₂ (connected) ≈ 0.057 m⁻¹.

**Transmissivity models Table 2, [Hyman 2016, pp. 6-7]**

| Model | Relationship | Parameters | Mean log₁₀(T) |
|-------|--------------|------------|--------------|
| Correlated | log(T) = log(a·rᵇ) | a=1.3×10⁻²⁹, b=0.5 | −18.79 |
| Semicorrelated | log(T) = log(a·rᵇ) + σ_T N(0,1) | a=1.3×10⁻²⁹, b=0.5, σ_T=0.7 | −18.79 (plus scatter) |
| Uncorrelated | log(T) = μ_T + σ_T N(0,1) | μ_T=−18.79, σ_T=0.8 | −18.79 |
| Constant | log(T) = μ_T | μ_T=−18.79 | −18.79 |

**Transport variables:**
- Breakthrough time τ (Eq. 10) [Hyman 2016, pp. 7-8]
- Transport resistance β (Eq. 10) [Hyman 2016, pp. 7-8]
- Active specific surface area s_f = β/τ (Eq. 11) [Hyman 2016, pp. 8-9]
- Effective permeability derived from Darcy velocity [Hyman 2016, pp. 10-11]

## Reusable Claims

1. **Claim:** In sparse 3‑D discrete fracture networks with truncated power‑law size distribution, a **perfectly correlated** size–transmissivity relationship (cubic law) yields **effective permeability ~2.5 times** that of a constant‑transmissivity network, even when the mean transmissivity is identical.  
   *Conditions:* Cubic law, uniform fracture aperture, low transmissivity variance, network geometry similar to Forsmark background fractures; derived from a single deterministic realization [Hyman 2016, pp. 10-11].

2. **Claim:** Under the same conditions, the **50 % breakthrough time** for the correlated model is **~0.34 times** that of the constant model; the semicorrelated model gives slightly earlier breakthroughs (0.31), while uncorrelated and constant models are nearly equal [Hyman 2016, pp. 12-13].

3. **Claim:** The **active specific surface area** (linear approximation s_f ≈ β/τ) is **15–20 % lower** for correlated/semicorrelated models than for uncorrelated/constant models, suggesting that size–transmissivity correlations can affect predictions of matrix diffusion and fracture‑wall reactions [Hyman 2016, pp. 12-13].

4. **Claim:** **Flow channeling** (fraction of fractures participating in transport, particle concentration on backbones) is enhanced when size–transmissivity correlation is introduced; however, the **geometric identity of the dominant transport backbone is primarily determined by network topology and fracture orientations**, not by the correlation model [Hyman 2016, pp. 12-13] [Hyman 2016, pp. 14-15].

5. **Claim:** The **tail of the breakthrough time distribution** (long‑term transport) is not significantly influenced by the choice of size–transmissivity relationship; all models exhibit similar power‑law decay with exponent near 2 [Hyman 2016, pp. 11-12] [Hyman 2016, pp. 14-15].

6. **Claim:** Differences in breakthrough times and effective permeability persist across **different geometric realizations** of the fracture network, indicating that the observed effects are general for sparse DFNs with the given statistical properties [Hyman 2016, pp. 13-14].

## Candidate Concepts

- [[fracture size–transmissivity correlation]]
- [[discrete fracture network (DFN)]]
- [[effective permeability]]
- [[breakthrough curve]]
- [[transport resistance (β)]]
- [[active specific surface area]]
- [[flow channeling in fractures]]
- [[fracture network backbone]]
- [[Lagrangian particle tracking]]
- [[truncated power law distribution]]
- [[Fisher distribution]]
- [[cubic law]]
- [[sparse fracture network]]
- [[percolation threshold in DFN]]

## Candidate Methods

- [[dfnWorks]]
- [[FRAM (feature rejection algorithm for meshing)]]
- [[LaGriT meshing toolbox]]
- [[PFLOTRAN]]
- [[WALKABOUT particle tracking]]
- [[flow topology graph (FTG)]]
- [[backbone identification algorithm]]
- [[flux‑weighted injection]]
- [[optimal path extraction in FTG]]

## Connections To Other Work

- [de Dreuzy et al. (2004)] showed that correlating size and aperture increases effective permeability in **2‑D** DFNs, but did not examine transport; the present study extends this to **3‑D** and transport observables [Hyman 2016, pp. 1-2] [Hyman 2016, pp. 10-11].
- [Baghbanan and Jing (2007)] reported that overall permeability of a 2‑D DFN was controlled by large fractures assigned higher apertures, consistent with the backbone channeling observed here [Hyman 2016, pp. 1-2].
- [Frampton and Cvetkovic (2010)] calibrated a perfectly correlated model at Laxemar using flow‑log data; the present study uses synthetic networks but echoes the importance of the correlation for flow patterns [Hyman 2016, pp. 5-6].
- [Cvetkovic and Frampton (2012)] demonstrated that the choice between cubic and quadratic law influences τ and β; combining those results with the present findings suggests that joint sensitivity of size‑transmissivity and aperture‑transmissivity relationships could create large differences in breakthrough times [Hyman 2016, pp. 15-16].
- [Makedonska et al. (2016)] found that in‑fracture aperture variability had little effect on global transport in sparse 3‑D DFNs; however, the interaction of such variability with a size‑transmissivity correlation was not investigated [Hyman 2016, pp. 15-16].
- [Joyce et al. (2014)] and [Follin et al. (2014)] calibrated three size‑transmissivity models at Forsmark and observed that uncorrelated models require higher mean transmissivity to match flow data, aligning with the reported compensation effect [Hyman 2016, pp. 1-2] [Hyman 2016, pp. 16-17].

## Open Questions

- How do **joint uncertainties** of the size–transmissivity relationship and the **aperture–transmissivity relationship** (cubic vs quadratic vs other laws) combine – linear or nonlinear? This could produce order‑of‑magnitude differences in breakthrough times [Hyman 2016, pp. 15-16].
- What is the influence of **internal fracture aperture variability** when combined with a size–transmissivity correlation, especially for different physical aperture‑structuring processes (e.g., erosion‑induced channelization)? [Hyman 2016, pp. 15-16]
- Can field‑scale **flow and aperture (or transmissivity) distributions** be used to discriminate among the four correlation models, and can a combined calibration identify the most plausible model for a given site? [Hyman 2016, pp. 16-17]
- What is the **field relevance** of the identified backbones and, conversely, the stagnant regions? Can these pathways be identified *a priori* for a given hydraulic setup? [Hyman 2016, pp. 16-17]
- Under which conditions does the difference in **active specific surface area** (15–20 % lower for correlated models) translate into significant changes in reactive transport predictions? [Hyman 2016, pp. 16-17]

## Source Coverage

All 20 non‑empty indexed text blocks （of the published article）[Hyman 2016, pp. 1-18] were processed. Source blocks: 20, compiled characters: 98 734 (coverage ratio by blocks: 1.0, coverage ratio by chars: 1.004). The complete article text is represented in the fragments used above.
