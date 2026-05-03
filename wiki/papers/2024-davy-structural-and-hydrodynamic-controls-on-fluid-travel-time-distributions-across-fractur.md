---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2024-davy-structural-and-hydrodynamic-controls-on-fluid-travel-time-distributions-across-fractur"
title: "Structural and Hydrodynamic Controls on Fluid Travel Time Distributions across Fracture Networks."
status: "draft"
source_pdf: "data/papers/2024 - Structural and hydrodynamic controls on fluid travel time distributions across fracture networks.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Davy, Philippe, et al. “Structural and Hydrodynamic Controls on Fluid Travel Time Distributions across Fracture Networks.” *PNAS*, vol. 121, no. 47, 2024, e2414901121, doi:10.1073/pnas.2414901121."
indexed_texts: "18"
indexed_chars: "88052"
nonempty_source_blocks: "18"
compiled_source_blocks: "18"
compiled_source_chars: "86817"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.985974"
coverage_status: "full-index"
source_signature: "0fbd59efea72d9a5ed4be8348a77cf9c00439e29"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T07:58:25"
---

# Structural and Hydrodynamic Controls on Fluid Travel Time Distributions across Fracture Networks.

## One-line Summary
Across a large database of discrete fracture network (DFN) models, fluid travel time distributions generically exhibit a stretched inverse gamma (SIG) regime at early times and a power‑law tail at late times, with the long‑tail exponent controlled not only by point‑velocity statistics but counter‑intuitively reduced by flow channeling; a coupled CTRW model is developed to capture this effect.

## Research Question
What are the structural and hydrodynamic controls on fluid travel time distributions in fracture networks, and why does the relationship between velocity heterogeneity, flow channeling, and anomalous transport deviate from classical continuous time random walk (CTRW) predictions?  [Davy 2024, pp. 1-1, 2-2]

## Study Area / Data
The study uses a large database of DFN simulations spanning synthetic, genetic, and field‑calibrated models.  
- Field calibration is based on the **Forsmark site in Sweden**, one of the most characterized fractured rock sites, with data provided by the Swedish Nuclear Fuel and Waste Management Company (Svensk Kärnbränslehantering AB).  [Davy 2024, pp. 3-3]
- Field tracer test data from the **Äspö Hard Rock Laboratory (Sweden)** are shown for comparison, covering time scales from 1 h to nearly one year.  [Davy 2024, pp. 2-2]
- All simulated travel time, Eulerian, and Lagrangian velocity distributions are publicly available in a GitLab repository.  [Davy 2024, pp. 11-11]

## Methods
### DFN Model Database
Fracture networks were constructed with a two‑dimensional approach to complexity:
- **Structural complexity**: Poissonian (constant size or power‑law size distribution), open genetic models calibrated to Forsmark, and In‑Plane Patches (IPPA) models that include partially sealed fractures with open patches.  [Davy 2024, pp. 2-3, 3-3]
- **Transmissivity variability**: Four classes – constant everywhere (T1), variable in network correlated with normal stress and fracture size (TSL), in‑plane variations by correlated random fields with constant mean transmissivity (T1&CRF), and in‑plane variations with variable mean transmissivity (TSL&CRF).  [Davy 2024, pp. 3-3, 4-4]

### Flow and Transport Simulation
- Flow and advective particle tracking were performed with the **DFN.lab** software, assuming complete mixing in the fracture thickness but explicitly resolving streamline partitioning at intersections.  [Davy 2024, pp. 4-4]
- **Flux‑weighted injection** was used to ensure stationarity of velocity statistics.  [Davy 2024, pp. 4-4]
- Matrix diffusion was excluded to isolate the effects of heterogeneous advection and structural heterogeneity.  [Davy 2024, pp. 4-4]

### Characterisation of Flow Structure
- **Percolation parameter** *p* was employed to assess connectivity; all models have *p* >> *p*<sub>c</sub> ≈ 2.7, so the connected backbone is not fractal.  [Davy 2024, pp. 4-4]
- **Channeling factor** *f* = *p*<sub>32</sub> / *d*<sub>q</sub> (ratio of total fracture surface to that occupied by flow) quantifies flow localisation; larger *f* indicates stronger channeling.  [Davy 2024, pp. 4-4]

### BTC Modelling
- Breakthrough curves (BTCs) were fitted by a **stretched inverse gamma (SIG)** function for short–intermediate times and a **power‑law tail** beyond a transition time *t*<sub>c</sub> (five‑parameter model).  [Davy 2024, pp. 6-6]
- Parameters: average travel time *t̅*, transition time *t*<sub>c</sub>, stretched exponent *s*, gamma exponent *k*, and long‑tail exponent *a*.  [Davy 2024, pp. 6-6]

### Coupled CTRW Model
- A coupled CTRW is proposed in which the spatial step length ξ depends on velocity as ξ ~ *v*<sup>μ</sup> (μ > 0), leading to a time increment Δ*t* ~ *v*<sup>μ−1</sup>. The long‑tail exponent is then *a* = (δ<sub>L</sub> − μ)/(1 − μ), where δ<sub>L</sub> is the Lagrangian velocity exponent.  [Davy 2024, pp. 9-9]
- The channeling exponent μ is derived from the simulation data as μ = (*a* − δ<sub>L</sub>) / (*a* − 1).  [Davy 2024, pp. 10-10]

## Key Findings
1. **Generic BTC shape**: Across all investigated fracture networks, BTCs follow a stretched inverse gamma (SIG) function at early to intermediate times and transition to a power‑law tail at late times. The power‑law tail can contribute up to 70% of the travel time variance.  [Davy 2024, pp. 6-6, 7-7]
2. **Dominance of the Noah effect**: Particle travel times are generally dominated by a single extreme low‑velocity event (a “trap”) in one fracture, caused primarily by very low hydraulic head gradients rather than low transmissivity. The Joseph effect (broad step‑size distribution) is not significant.  [Davy 2024, pp. 7-7]
3. **Breakdown of classical CTRW relations**:
   - The long‑tail exponent *a* is consistently larger than the Eulerian exponent δ<sub>E</sub> + 1 and larger than the Lagrangian exponent δ<sub>L</sub>, contrary to standard CTRW predictions.  [Davy 2024, pp. 7-7, 8-8]
   - The relationship *a* = δ<sub>L</sub> is not observed; instead, for many networks *a* ≈ δ<sub>L</sub> + 0.15.  [Davy 2024, pp. 8-8]
4. **Counter‑intuitive role of channeling**:
   - While channeling (higher *f*) broadens the intermediate‑time SIG exponent *k* (more dispersion), it **reduces** the long‑tail exponent *a*, i.e., stronger channeling leads to less anomalous transport.  [Davy 2024, pp. 8-8]
   - For open genetic models, *a* increases linearly with channeling: *a* = 2.25 + *f* − 1/25.  [Davy 2024, pp. 8-8]
5. **Coupled CTRW explains the discrepancy**:
   - The coupled CTRW model, with step length increasing with velocity (μ > 0), captures the reduction of anomalous transport by channeling. The derived μ values range from 0.05 to 0.3 and correlate positively with the channeling factor *f*.  [Davy 2024, pp. 9-9, 10-10]
   - This mechanism can break the stability of anomalous transport when μ is large enough, driving a transition to Fickian dispersion.  [Davy 2024, pp. 9-9, 10-10]
6. **Impact of aperture fluctuations**:
   - Aperture variability alters the flux‑weighting relation between Eulerian and Lagrangian velocity distributions: it can increase (open genetic) or decrease (IPPA) the weight of low velocities.  [Davy 2024, pp. 5-5]
   - In‑plane transmissivity variations increase channeling but have limited effect on the long‑time exponent *a*.  [Davy 2024, pp. 8-8]
7. **Topological control**: Eulerian velocity statistics are primarily governed by network topology and are surprisingly insensitive to aperture fluctuations at network or fracture scale.  [Davy 2024, pp. 10-10]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| BTCs across all models exhibit a SIG shape at early times and a power‑law tail at late times, with the tail contributing up to 70% of the variance. | [Davy 2024, pp. 6-6, 7-7] | DFN models with *p* >> *p*<sub>c</sub>; flux‑weighted injection; advection only. | Field BTCs from Äspö show similar behavior (power‑law tail different from −3/2 matrix diffusion). |
| Long‑tail exponent *a* is systematically larger than δ<sub>E</sub> + 1 and δ<sub>L</sub>, contradicting standard CTRW predictions. | [Davy 2024, pp. 7-7, 8-8] | All DFN structures except the most homogeneous (constant‑size, *p* = 8). | For open genetic and Poissonian models with constant transmissivity, *a* ≈ δ<sub>L</sub> + 0.15. |
| Channeling factor *f* is positively correlated with the intermediate‑time exponent *k* (more dispersion) but negatively correlated (or unrelated) with the late‑time exponent *a* (less anomalous). | [Davy 2024, pp. 8-8] | Open genetic, IPPA, and Poissonian networks. | For open genetic models, *a* = 2.25 + *f* − 1/25. |
| The coupled CTRW model with ξ ~ *v*<sup>μ</sup> recovers the reduction of anomalous transport; derived μ values (0.05–0.3) increase with channeling. | [Davy 2024, pp. 9-9, 10-10] | All DFN simulations; μ calculated from *a* and δ<sub>L</sub>. | When μ ≥ (3−δ<sub>L</sub>)/2, transport can become Fickian (*a* > 3). |
| Particle travel times are dominated by a single “trap” event in one fracture, caused by extremely low hydraulic head gradient, not by low transmissivity. | [Davy 2024, pp. 7-7] | Open genetic DFN with TSL transmissivity; analysis of trap time vs. total travel time. | Joseph effect (tortuosity) plays a minor role. |
| In open genetic models, aperture fluctuations reduce the heterogeneity of Lagrangian velocities (δ<sub>L</sub> increases); in IPPA models, they increase heterogeneity (δ<sub>L</sub> decreases). | [Davy 2024, pp. 5-5] | Constant vs. variable aperture networks. | Modifications relative to the flux‑weighting relation n<sub>L</sub>(*v*) ~ *v* n<sub>E</sub>(*v*). |
| Eulerian velocity statistics exhibit small variability across different transmissivity models for a given network topology. | [Davy 2024, pp. 10-10] | Open genetic, IPPA, power‑law, constant‑size DFNs. | Suggests dominant control of network topology on velocity field. |

## Limitations
- **Advection only**: Matrix diffusion is excluded; the study focuses on advective travel times. Including diffusion, especially at low Péclet numbers, may modify the long‑time power‑law behavior.  [Davy 2024, pp. 4-4, 11-11]
- **Injection mode**: Results are derived from flux‑weighted injection. Resident injection could oversample low‑velocity zones and potentially enhance anomalous transport in highly channelized flows.  [Davy 2024, pp. 4-4, 10-10]
- **Complete mixing assumption**: Fracture‑thickness mixing is assumed; while justified for the considered time scales (diffusion time across aperture is seconds to minutes vs. days to years), it may not hold for very early times or very thin fractures.  [Davy 2024, pp. 4-4]
- **Network connectivity**: All models are well above the percolation threshold. Behaviour at or near the percolation threshold, where the backbone becomes fractal, is not covered.  [Davy 2024, pp. 7-7]
- **Generality**: The conclusions are drawn from a specific set of DFN structures and transmissivity models. Specific DFN configurations not considered here could exhibit different dynamics.  [Davy 2024, pp. 11-11]
- **Dead‑end fractures**: Very low velocities in dead‑end clusters are not sampled by advective particles in the simulations, placing a practical limit on the observable range of the power‑law tail (approximately six orders of magnitude in probability).  [Davy 2024, pp. 5-5]

## Assumptions / Conditions
- **Open fraction**: For field‑calibrated models (Forsmark), open fraction is 15–25%; open genetic models represent this by fully open or sealed fractures depending on size, while IPPA models use correlated random fields to distribute open patches.  [Davy 2024, pp. 3-3]
- **Transmissivity models**:
  - T1: constant transmissivity everywhere.
  - TSL: transmissivity exponentially decreasing with normal stress and linearly increasing with fracture size.
  - T1&CRF, TSL&CRF: in‑plane lognormal transmissivity variations (σ<sub>log T</sub> = 1 or 2) superimposed on T1 or TSL.
- **Fracture size distributions**: Poissonian models use constant size or power‑law distributions with exponents −4, −3.5, −3; open genetic models produce a double power‑law distribution with a universal large‑scale exponent.  [Davy 2024, pp. 3-3, 4-4]
- **Cubic law**: Fracture transmissivity and transport aperture are related by the classical cubic law.  [Davy 2024, pp. 3-3]
- **Stationarity of Lagrangian velocities**: Ensured by flux‑weighted injection and large domain; the Moses effect (nonstationarity) is considered minimal.  [Davy 2024, pp. 4-4, 7-7]
- **Percolation parameter *p* >> *p*<sub>c</sub>**: Except for one model (*p* = 3), all simulations have *p* well above the threshold, implying non‑fractal connected backbones.  [Davy 2024, pp. 4-4]

## Key Variables / Parameters
- **BTC fitting parameters**: average travel time *t̅*, transition time *t*<sub>c</sub>, stretched exponent *s*, gamma exponent *k*, long‑tail exponent *a*.  [Davy 2024, pp. 6-6]
- **Velocity exponents**:
  - δ<sub>E</sub>: power‑law exponent of Eulerian velocity distribution (for *v*<sup>−1</sup>).
  - δ<sub>L</sub>: power‑law exponent of Lagrangian velocity distribution (sampled along streamlines).
- **Channeling factor** *f* = *p*<sub>32</sub> / *d*<sub>q</sub>.  [Davy 2024, pp. 4-4]
- **Channeling exponent** μ in coupled CTRW (ξ ~ *v*<sup>μ</sup>), derived from *a* and δ<sub>L</sub>.  [Davy 2024, pp. 9-9, 10-10]
- **Percolation parameter** *p*, controlling network connectivity.  [Davy 2024, pp. 4-4]

## Reusable Claims
1. **Across diverse DFN structures (Poisson, open genetic, IPPA), BTCs can be described by a stretched inverse gamma function transitioning to a power‑law tail, with the tail contributing up to 70% of the travel time variance.**
   - *Condition*: Flux‑weighted injection, advection only, networks well above percolation threshold.
   - *Limitation*: Not verified for resident injection or below percolation.  [Davy 2024, pp. 6-6, 7-7]

2. **The long‑tail exponent *a* is significantly larger than predicted by classical CTRW using either Eulerian (*a* = δ<sub>E</sub> + 1) or Lagrangian (*a* = δ<sub>L</sub>) velocity statistics.**
   - *Condition*: Applies to all networks investigated except the most homogeneous (constant‑size, high density).
   - *Limitation*: The relationship depends on the DFN structure and transmissivity model.  [Davy 2024, pp. 7-7, 8-8]

3. **Flow channeling reduces anomalous transport: for a given Lagrangian velocity exponent, networks with stronger channeling (higher *f*) exhibit a larger long‑tail exponent *a* (less anomalous).**
   - *Condition*: Valid for open genetic and Poissonian DFNs; relationship is weaker for IPPA models.
   - *Limitation*: Scatter exists between different realisations.  [Davy 2024, pp. 8-8]

4. **A coupled CTRW model with velocity‑dependent step size (ξ ~ *v*<sup>μ</sup>) captures the reduction of anomalous transport by channeling; μ can be estimated from *a* and δ<sub>L</sub> and correlates positively with the channeling factor *f*.**
   - *Condition*: Advective transport in fracture networks; μ > 0.
   - *Limitation*: The functional form ξ ~ *v*<sup>μ</sup> is a hypothesis; physical interpretation of μ needs further validation.  [Davy 2024, pp. 9-9, 10-10]

5. **Particle travel times are controlled by the Noah effect: a single extreme low‑velocity event in one fracture dominates the total travel time. Low velocities arise primarily from low hydraulic head gradients, not low transmissivities.**
   - *Condition*: Networks with *p* >> *p*<sub>c</sub>; flux‑weighted injection.
   - *Limitation*: May not hold if the network includes significant dead‑end clusters that are never visited by advective particles.  [Davy 2024, pp. 7-7]

6. **Aperture fluctuations modify the relationship between Eulerian and Lagrangian velocity distributions: network‑scale variability (TSL) tends to reduce Lagrangian velocity heterogeneity, while strong in‑plane heterogeneity (IPPA) increases it.**
   - *Condition*: Based on open genetic and IPPA models.
   - *Limitation*: The effect depends on the specific spatial correlation structure of apertures.  [Davy 2024, pp. 5-5]

7. **Eulerian velocity statistics are primarily controlled by network topology and are surprisingly insensitive to aperture fluctuations at fracture or network scale.**
   - *Condition*: True for the range of DFN structures and transmissivity models studied.
   - *Limitation*: May not generalise to networks with extreme transmissivity contrasts.  [Davy 2024, pp. 10-10]

## Candidate Concepts
- [[fracture network]]
- [[discrete fracture network (DFN)]]
- [[continuous time random walk (CTRW)]]
- [[anomalous transport]]
- [[stretched inverse gamma distribution]]
- [[breakthrough curve (BTC)]]
- [[Noah effect]]
- [[Joseph effect]]
- [[Moses effect]]
- [[flow channeling]]
- [[percolation theory]]
- [[critical path analysis]]
- [[Eulerian velocity distribution]]
- [[Lagrangian velocity distribution]]
- [[coupled CTRW model]]
- [[channeling factor]]
- [[open genetic DFN model]]
- [[IPPA model]]
- [[Forsmark site]]
- [[Äspö Hard Rock Laboratory]]
- [[matrix diffusion]]
- [[power‑law tail]]
- [[velocity correlation length]]

## Candidate Methods
- [[DFN.lab software]]
- [[advective particle tracking]]
- [[flux‑weighted injection]]
- [[BTC fitting with SIG and power‑law]]
- [[maximum likelihood estimation for BTC parameters]]
- [[computation of Eulerian and Lagrangian velocity distributions]]
- [[percolation parameter calculation]]
- [[channeling factor d_q]]
- [[coupled CTRW random walk simulations]]
- [[analysis of trap time and tortuosity along particle trajectories]]

## Connections To Other Work
- **Classical CTRW theory** (refs. 3, 19, 41, 42) predicts *a* = δ<sub>L</sub> for anomalous transport; this study shows that prediction is not valid across diverse fracture networks.  [Davy 2024, pp. 1-2, 2-2, 8-8]
- **Field tracer tests** at Äspö (ref. 34) exhibit BTC shapes similar to the simulations and power‑law tails different from the −3/2 matrix diffusion scaling.  [Davy 2024, pp. 2-2]
- **Previous DFN transport studies** (refs. 38, 39) noted that point‑velocity statistics overestimate tailing; the coupled CTRW provides a mechanistic explanation.  [Davy 2024, pp. 1-2, 2-2, 9-9]
- **Percolation and critical path analysis** (ref. 45) have been applied to porous media but their applicability to fracture network transport remains an open question.  [Davy 2024, pp. 2-2, 10-10]
- **Velocity correlation and spatial Markov models** (refs. 26, 39) introduce velocity‑dependent correlation; the coupled CTRW shares qualitative similarities.  [Davy 2024, pp. 9-9]
- **Brain microvascular networks** (ref. 14) exhibit network‑driven anomalous transport; the q‑model from granular physics (ref. 86) may help explain head gradient formation in networks.  [Davy 2024, pp. 10-11]
- **Genetic DFN model** (refs. 32, 62) is validated against field data from Forsmark and reproduces key flow characteristics.  [Davy 2024, pp. 3-3]
- **Dead‑end fracture effects** (ref. 75) are recognised but not fully resolved in this study because extremely low velocities in dead ends are not sampled.  [Davy 2024, pp. 5-5]

## Open Questions
- **How does network topology control the hydraulic head distribution at fracture intersections, and thus the formation of low‑gradient traps?**  
  String‑based graph models (refs. 83, 84) and the q‑model (refs. 86, 87) are suggested as potential approaches.  [Davy 2024, pp. 10-10]
- **Can the coupled CTRW framework be generalised to include matrix diffusion and a broader range of Péclet numbers?**  
  The current study is advection‑only; advection–diffusion simulations are needed.  [Davy 2024, pp. 11-11]
- **How do different injection modes (e.g., resident vs. flux‑weighted) interact with channeling to modify anomalous transport exponents?**  
  Preliminary discussion suggests resident injection could enhance anomalous transport in channeled flows.  [Davy 2024, pp. 10-10]
- **To what extent do the findings hold for networks at or near the percolation threshold, where the flowing backbone is fractal?**  
  The present models are all far above percolation, excluding the fractal regime.  [Davy 2024, pp. 4-4, 7-7]
- **Can the coupled CTRW model be unified with correlated CTRW / spatial Markov models that define velocity‑dependent transition probabilities?**  
  Qualitative similarities suggest potential for a unified framework.  [Davy 2024, pp. 9-9]
- **What is the physical origin of the channeling exponent μ in real fracture networks, and can it be predicted from geometric and hydraulic properties?**  
  At present μ is only inferred from transport statistics.  [Davy 2024, pp. 9-9, 10-10]

## Source Coverage
All 18 non‑empty indexed text blocks from the paper were processed. The compiled source comprises approximately 86,817 characters (98.6% of indexed characters), achieving full coverage (block coverage ratio = 1.0). No fragments were omitted.
