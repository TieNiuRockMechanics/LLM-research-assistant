---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2008-barth-l-my-estimates-of-fracture-density-and-uncertainties-from-well-data"
title: "Estimates of Fracture Density and Uncertainties from Well Data."
status: "draft"
source_pdf: "data/papers/2009 - Estimates of fracture density and uncertainties from well data.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Barthélémy, Jean-François, et al. \"Estimates of Fracture Density and Uncertainties from Well Data.\" *International Journal of Rock Mechanics & Mining Sciences*, 10.1016/j.ijrmms.2008.08.003. Accessed 2026."
indexed_texts: "30"
indexed_chars: "145876"
nonempty_source_blocks: "30"
compiled_source_blocks: "30"
compiled_source_chars: "146652"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.00532"
coverage_status: "full-index"
source_signature: "d6c2bd36776068eaf0d0b4ffd20e9ba07d912c05"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T13:33:46"
---

# Estimates of Fracture Density and Uncertainties from Well Data.

## One-line Summary
This paper derives closed-form probability laws for 3D fracture density (P32) conditioned on the number of traces observed on a borehole image, assuming a Poisson spatial distribution of fracture centres, for both lineic (scanline) and cylindrical well models, and quantifies the resulting uncertainties and double-trace bias.

## Research Question
How can the probabilistic law of the 3D fracture density (P32) of a fractured rock be estimated from the number of fracture traces observed along a well segment, while accounting for orientation bias, finite fracture size, partial traces, and double traces, under the assumption that fracture centres follow a Poisson process? [Accessed 2026, pp. 1-2]

## Study Area / Data
The study is a theoretical and methodological development, validated with Monte Carlo simulations of discrete fracture networks. No specific field data are used; instead, synthetic fracture networks with prescribed properties (e.g., elliptical fractures with lognormal size distribution, bivariate normal orientation distribution, Poisson centre distribution) are generated to test the derived conditional density laws. [Accessed 2026, pp. 6-7, 13-15]

## Methods
- **Bayesian inference framework**: The unknown P32 is treated as a random variable, and Bayes’ theorem is applied to obtain its posterior probability density function (p.d.f.) given the observed number of traces. [Accessed 2026, pp. 1-2]
- **Lineic well model** (well as a straight line): The well segment is modelled as a scanline. The probability that a fracture cuts the well is derived from the orientation and size distributions, and a Poisson process for trace occurrence is proved. The conditional p.d.f. of P32 given $N_L$ traces is shown to be a gamma distribution $p_{P32|N_L}(p|n_L) = \Gamma_{n_L+1,\kappa_o L}(p)$, where $\kappa_o = \mathbb{E}[\cos\Theta]$. [Accessed 2026, pp. 4-6]
- **Cylindrical well model** (well as a cylinder of radius $R_c$): The analysis is extended to account for partial traces and double traces (one fracture generating two traces on the borehole wall). Fractures are assumed planar and elliptic. Correction factors $\kappa = \mathbb{E}[\sigma]/\mathbb{E}[S]$, $\kappa_1$, $\kappa_2$ are introduced, where $\sigma$ is the area of the domain that the projection of a fracture centre must occupy to intersect the cylinder. The number of fractures cutting the well, as well as the numbers of single-trace and double-trace intersections, follow Poisson laws with means $P_{32} \kappa L$, etc. The posterior p.d.f. of P32 given the total number of observed traces $N_t^L$ is a linear combination of gamma distributions: $p_{P32|N_t^L}(p|n_t^L) = \frac{1+r}{1-(-r)^{n_t^L+1}} \sum_{n_2=0}^{\lfloor n_t^L/2\rfloor} B_{r,n_t^L-n_2}(n_2) \, \Gamma_{n_t^L-n_2+1,\kappa L}(p)$, where $r = \mathbb{P}(2\text{ traces})$. [Accessed 2026, pp. 10-13]
- **Monte Carlo validation**: Discrete fracture networks are generated with known P32, and the empirical distribution of traces is compared to the theoretical conditional expectations and quantiles (e.g., 1st and 9th deciles). The agreement (79.16% and 80.96% of points within the decile curves for lineic and cylindrical models, respectively) confirms the derived laws. [Accessed 2026, pp. 6-7, 13-15]
- **Application to DFN generation**: The conditional law of the number of fractures $N_V$ in a volume $V$ given the observed trace count is derived to illustrate propagation of density uncertainty into discrete fracture models. [Accessed 2026, pp. 15-16]

## Key Findings
1. **Lineic well P32 law**: Under the Poisson centre assumption, P32 conditioned on $n_L$ observed traces follows a gamma distribution $\text{Gamma}(n_L+1, \kappa_o L)$, with expectation $ \mathbb{E}[P_{32}|N_L=n_L] = (n_L+1)/(\kappa_o L)$, mode $n_L/(\kappa_o L)$, and standard deviation $\sqrt{n_L+1}/(\kappa_o L)$. [Accessed 2026, pp. 5-6]
2. **Cylindrical well P32 law**: When fracture sizes are comparable to the well radius, the conditional p.d.f. of P32 becomes a linear combination of gamma densities, explicitly accounting for double traces. The mean and variance involve a correction term $f(n_t^L,r)$ that disappears only if $r=0$ (no double traces). [Accessed 2026, pp. 12-13]
3. **Double-trace bias**: Ignoring the possibility that a single fracture may leave two traces (i.e., treating every trace as an independent fracture) can cause significant error in the P32 estimate; this is especially important when $r$, the proportion of double-trace fractures, is not negligible. [Accessed 2026, pp. 12-13, 14-15]
4. **Validation via Monte Carlo**: Simulations with elliptical fractures and bivariate normal orientation distributions show good agreement with theoretical expectations and confidence intervals. For the cylindrical model that accounts for double traces, 80.96% of simulated points lie between the 1st and 9th deciles, whereas the model that ignores double traces captures only 60%, and the fully lineic model (assuming all traces are full) severely overestimates P32 when fractures are nearly parallel to the well. [Accessed 2026, pp. 13-15]
5. **Impact on DFN generation**: When P32 is treated as a random variable conditioned on the observed traces, the uncertainty in the number of fractures $N_V$ in a given volume does not vanish with increasing volume; the relative standard deviation tends to $1/\sqrt{n_L+1}$, highlighting the persistent importance of the observation sample size. [Accessed 2026, pp. 16-17]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| "The probability law (9) proves that the property of cutting the well path is a Poisson process. It follows that the mean number of traces per well unit length is … P10 = E[N_L]/L = P32 κ_o" | [Accessed 2026, pp. 4-5] | Fracture centres follow Poisson distribution in 3D; well is a straight line. | Derives the correction factor κ_o = E[cos Θ] linking 1D trace frequency to 3D density. |
| "Invoking Bayes’ theorem … the p.d.f. of P32 given the number N_L is … p_{P32|N_L}(p|n_L) = e^{-p κ_o L} p^{n_L} (κ_o L)^{n_L+1} / n_L! = Γ_{n_L+1, κ_o L}(p)" | [Accessed 2026, pp. 5-6] | Same Poisson assumption; prior on P32 treated as non-informative. | Establishes the gamma posterior for lineic well. |
| "E[P32|N_L=n_L] = (n_L+1)/(κ_o L) ; Mode[P32|N_L=n_L] = n_L/(κ_o L) ; √Var[P32|N_L=n_L] = √(n_L+1)/(κ_o L)" | [Accessed 2026, pp. 5-6] | Same conditions. | Expectation ≠ mode; even with zero traces the mean density is non-zero. |
| "As shown on Fig. 3, the law (13) is consistent with the Monte Carlo simulations; in particular, the proportion of points lying between the two decile curves among the 2000 drawn fracture networks is 79.16%." | [Accessed 2026, pp. 6-7] | Elliptical fractures (aspect ratio 1/2, lognormal major radius), bivariate normal orientation, lineic well. | Good agreement for lineic case. |
| "The probability law of P32 in the cylindrical case … writes as a linear combination of gamma probability density functions: p_{P32|N_t^L}(p|n_t^L) = (1+r)/(1-(-r)^{n_t^L+1}) Σ_{n2} B_{r,n_t^L-n2}(n2) Γ_{n_t^L-n2+1, κ L}(p)" | [Accessed 2026, pp. 12-13] | Cylindrical well, elliptic fractures, Poisson centres; r = P(2 traces). | Takes into account double traces and finite size. |
| "Ignoring double traces when r is far from 0 could lead to an important error in the P32 estimate." | [Accessed 2026, pp. 12-13] | Cylindrical model. | Qualitative warning. |
| "After computations … the previous data lead to a ratio r = 34.4% and to κ = 0.174 … The discrepancy between the two curves allows to quantify the error made by neglecting the double traces." | [Accessed 2026, pp. 13-14] | Example: R_c=0.1 m, L=20 m, N_t^L=20, major radius lognormal(mean 1 m, sd 0.1 m), aspect ratio 0.3, mean pole inclined 80° to well, s1=s2=0.1, Ψ=π/2. | Concrete numerical case. |
| "the proportion of points lying between the two decile curves of the M 1 model is 80.96% and only 60% between the curves of M 2." | [Accessed 2026, pp. 14-15] | Same fracture set as above. Model M1 includes double-trace correction, M2 ignores it. | M1 much better. |
| "This means that, for large values of V, an increase of the latter does not significantly reduce the uncertainty on N_V. As expected, the only way to reduce this uncertainty is then to get more observed data." | [Accessed 2026, pp. 16-17] | Application to DFN: N_V given N_L. V large. | Uncertainty bounded by observation sample size. |
| "fractures will be considered as planar … the spatial distribution of their centers is of Poisson type … the orientation and size distributions are independent … the studied well interval is assumed to be such that the spatial, size and orientation distributions can be considered as homogeneous." | [Accessed 2026, pp. 17-18, also pp. 3-4] | Core assumptions of the whole derivation. | Fundamental hypotheses. |

## Limitations
- The method requires that fractures be planar, their centre distribution Poissonian, and that within a fracture set orientation and size are independent and stationary along the well interval. [Accessed 2026, pp. 17-18]
- For the cylindrical well model, the fracture size distribution must be known a priori; its determination from borehole images remains difficult, especially when fracture sizes are not small compared to the well radius. [Accessed 2026, pp. 17-18]
- The Poisson spatial distribution, while supported by many field studies, is suspected to be valid mainly for low‑density or early‑stage fracturing; clustered or regularly spaced networks are not covered. [Accessed 2026, pp. 17-18]
- The lineic model is adequate only when the well radius is very small relative to fracture size; otherwise, ignoring partial and double traces leads to biased density estimates. [Accessed 2026, pp. 10, 14-15]
- The derivation for the cylindrical well assumes elliptic fractures; extension to other shapes is not provided. [Accessed 2026, pp. 7, 9]
- The posterior laws rely on a non‑informative prior for P32; an informative prior could be incorporated but is not explored. [Accessed 2026, pp. 5-6, 12]

## Assumptions / Conditions
- Fractures are planar. [Accessed 2026, pp. 17-18]
- Fracture centres follow a homogeneous Poisson process in 3D (parameter P30). [Accessed 2026, pp. 3-4, 17-18]
- Orientation and size distributions are independent within a fracture set. [Accessed 2026, pp. 3-4, 17-18]
- The well interval is small enough that the spatial, size, and orientation distributions can be regarded as stationary. [Accessed 2026, pp. 17-18]
- For the cylindrical model, fractures are elliptic with random major and minor radii (A, B); the rotation angle Ψ and the shape are independent of location. [Accessed 2026, pp. 7-9]
- Trace assignment to the studied interval follows the “mid‑point” convention. [Accessed 2026, pp. 11]
- The prior distribution of P32 is taken as non‑informative, so that the posterior is proportional to the likelihood of the trace count. [Accessed 2026, pp. 5-6]

## Key Variables / Parameters
- **P32**: 3D fracture density (mean fractured surface per unit volume, m²/m³). [Accessed 2026, pp. 3-4]
- **P30**: mean number of fracture centres per unit volume (/m³). Related to P32 by P32 = P30·E[S] where E[S] is expected fracture surface. [Accessed 2026, pp. 3-4]
- **P10**: mean number of fracture traces per well unit length (/m). [Accessed 2026, pp. 3-4]
- **κ_o = E[cos Θ]**: orientation correction factor for lineic well; Θ is acute angle between fracture normal and well direction. [Accessed 2026, pp. 4-5]
- **σ**: domain area in the plane perpendicular to the well such that an elliptic fracture with given size and orientation intersects the cylinder; depends on projected radii Â, B̂ and well radius R_c. [Accessed 2026, pp. 8-10]
- **κ = E[σ]/E[S]**: cylindrical well correction factor accounting for both orientation and size. [Accessed 2026, pp. 11-12]
- **κ₁, κ₂**: contributions to κ from single-trace and double-trace intersections (κ = κ₁+κ₂). [Accessed 2026, pp. 11-12]
- **r = κ₂/κ = P(2 traces)**: probability that a fracture cutting the well leaves a double trace. [Accessed 2026, pp. 12]
- **N_L, N_t^L**: number of fractures cutting the well, and number of observed traces (N_t^L = N₁ + 2N₂). [Accessed 2026, pp. 11]
- **L**: length of the analysed well segment. [Accessed 2026, multiple]
- **R_c**: well radius (cylindrical model). [Accessed 2026, pp. 7]
- **A, B**: major and minor radii of elliptical fractures; Â, B̂ are their projections. [Accessed 2026, pp. 7-8]

## Reusable Claims
1.  In a Poissonian fracture network intersected by a straight scanline, the posterior probability density of P32 given $n_L$ traces is a gamma distribution $\text{Gamma}(n_L+1, \kappa_o L)$, with expectation $(n_L+1)/(\kappa_o L)$ and standard deviation $\sqrt{n_L+1}/(\kappa_o L)$. [Accessed 2026, pp. 5-6]
    - _Condition_: Fracture centres follow a 3D Poisson process; prior on P32 is non‑informative; fracture size and orientation are independent and stationary within the set.
    - _Limitation_: Only valid when the well can be approximated as a line (well radius ≪ fracture size).
2.  For a cylindrical well and finite‑size elliptic fractures, the conditional distribution of P32 given the total number of observed traces is a weighted sum of gamma densities, with weights depending on the probability $r$ of a double trace. The expectation and variance are corrected by a term $f(n_t^L,r)$. [Accessed 2026, pp. 12-13]
    - _Condition_: Same Poisson and independence assumptions; fracture shape is elliptic; size distribution must be known.
    - _Implication_: Ignoring double traces (setting $r=0$) leads to overestimation of P32; the bias increases with $r$.
3.  If the double‑trace probability $r$ is not negligible, using the lineic model (which assumes all traces come from distinct very large fractures) can dramatically overestimate P32, especially when fractures are sub‑parallel to the borehole. [Accessed 2026, pp. 14-15]
4.  When the true P32 is uncertain (described by the posterior), the number of fractures $N_V$ in a volume $V$ does not follow a Poisson distribution; its relative uncertainty does not shrink to zero with increasing $V$ but is bounded below by $1/\sqrt{n_L+1}$. Therefore, the only way to reduce uncertainty in $N_V$ is to collect more well traces. [Accessed 2026, pp. 16-17]
5.  A simple validation approach is Monte Carlo generation of discrete fracture networks, comparing the empirical distribution of $(N_t^L/L, P_{32})$ with theoretical decile curves of the conditional law. The fraction of points between the deciles (ideally 80%) serves as a goodness‑of‑fit check. [Accessed 2026, pp. 6-7, 14-15]

## Candidate Concepts
- [[fracture density P32]]
- [[Poisson fracture network]]
- [[scanline sampling]]
- [[cylindrical well fracture intersection]]
- [[orientation bias correction]]
- [[size–orientation independence]]
- [[double trace bias]]
- [[Bayesian estimation of P32]]
- [[conditional gamma distribution]]
- [[elliptic integral in fracture intersection]]
- [[confidence interval for fracture density]]
- [[discrete fracture network (DFN) uncertainty]]

## Candidate Methods
- [[Lineic well P32 estimation via gamma posterior]]
- [[Cylindrical well P32 estimation with double-trace correction]]
- [[Monte Carlo validation of conditional density laws]]
- [[Computation of σ surfaces for elliptical fractures on a cylinder]]
- [[Quantile computation for combined gamma posteriors]]
- [[Propagation of density uncertainty to DFN generation]]

## Connections To Other Work
- **Correction factor from 1D to 3D**: Builds on Terzaghi (1965) [53] and later work by Dershowitz (1985) [14], Dershowitz & Herda (1992) [15], Mauldon (1994) [35], Mauldon & Mauldon (1997) [36], Wang (2005) [56], and others. [Accessed 2026, pp. 3-4]
- **Poisson spatial distribution**: Relies on field‑study validations by Priest & Hudson (1976) [47], Rives et al. (1992) [48], Sisavath et al. (2004) [50], noting that the Poisson model is best suited to low‑density networks. [Accessed 2026, pp. 3, 17]
- **Stereology of fracture traces on cylindrical surfaces**: Uses results from Gupta & Adler (2006) [23] for the surface σ and full‑trace conditions; also references Özkaya (2003) [44] for size estimation via correlation with observable properties. [Accessed 2026, pp. 9-10, 17]
- **Fracture size estimation from traces**: Mentions Berkowitz & Adler (1998) [7] for plane outcrops and notes the difficulty of extending such methods to cylinders when fracture size is not small compared to borehole radius. [Accessed 2026, pp. 15, 17]
- **DFN conditioning**: References Andersson et al. (1984) [1] for conditional probability of fracture numbers, and many works on permeability/connectivity of fracture networks (Bourbiaux, de Dreuzy, etc.). [Accessed 2026, pp. 1-2, 16-17, 23-24]

## Open Questions
- The fracture size distribution must be supplied externally; no direct method is provided to extract it from borehole images without additional assumptions (e.g., correlation with aperture or spacing). A robust, assumption‑free size‑estimation technique for cylindrical wells is still needed. [Accessed 2026, pp. 17-18]
- The Poisson spatial distribution of centres is recognised to be limited to low‑density or early‑stage fracturing. Extending the framework to include spatial correlations (e.g., fractal models) or other spacing distributions (e.g., lognormal) remains an open area. [Accessed 2026, pp. 17-18]
- Only single fracture sets are treated; the case of multiple sets with potential inter‑set correlations is not addressed. [Accessed 2026, pp. 3]
- The current work does not consider an informative prior on P32; incorporating prior geological knowledge could refine the estimates. [Accessed 2026, pp. 5-6]
- The application to DFN generation shows that uncertainty in P32 propagates into NV, but the consequences for flow and transport predictions (e.g., percolation threshold, effective permeability) are not quantified. [Accessed 2026, pp. 15-16]

## Source Coverage
All 30 non‑empty indexed text blocks (100% of indexed pieces) were processed to compile this page. The coverage ratio by blocks is 1.0 and by characters is 1.00532, corresponding to a full‑index pass. No indexed fragment was omitted.
