---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-zhu-impacts-of-t-type-intersections-on-the-connectivity-and-flow-in-complex-two-dimensional"
title: "Impacts of T-type Intersections on the Connectivity and Flow in Complex Two-Dimensional Fracture Networks."
status: "draft"
source_pdf: "data/papers/2023 - Impacts of T-type intersections on the connectivity and flow in Complex two-dimensional fracture networks.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Zhu, Weiwei, et al. \"Impacts of T-type Intersections on the Connectivity and Flow in Complex Two-Dimensional Fracture Networks.\" *Engineering Geology*, vol. 320, 2023, p. 107122. doi:10.1016/j.enggeo.2023.107122. Accessed 2026."
indexed_texts: "11"
indexed_chars: "53939"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T12:48:58"
---

# Impacts of T-type Intersections on the Connectivity and Flow in Complex Two-Dimensional Fracture Networks.

## One-line Summary

This study systematically compares the connectivity, single-phase permeability, and two-phase gas/water production between stochastic discrete fracture networks (original) and their kinematically grown counterparts enriched with T-type intersections, finding that kinematic networks enhance connectivity and flow in ~68–77% of cases, but flow results are not solely determined by connectivity and are strongly influenced by the number of inlets and outlets [Zhu 2023, pp. 1‑1, 5‑6, 6‑8].

## Research Question

What are the impacts of T‑type intersections on the connectivity and flow behavior (permeability, gas/water production) in complex two‑dimensional fracture networks when fracture growth is considered? [Zhu 2023, pp. 1‑1].

## Study Area / Data

The study is based on synthetically generated two‑dimensional discrete fracture networks, not a specific field site. Key statistical parameters are informed by general outcrop observations; for instance, the power‑law length exponent varies in the range \([2.0, 3.0]\), and the concentration parameter κ is typically < 3.0 for multi‑set networks [Zhu 2023, pp. 2‑3].  
A Taguchi design is used to create nine orthogonal cases spanning three parameters (fracture length exponent, spatial clustering, orientation concentration) at three levels, with ten independent realizations per case, yielding 90 analyzed realizations [Zhu 2023, pp. 2‑3].  
The networks are constructed up to an “over‑percolative” state, defined as a fracture intensity twice the percolation threshold intensity, a condition reported in natural outcrops [Zhu 2023, pp. 2‑3].

## Methods

- **Discrete Fracture Network (DFN) Construction**: Stochastic DFNs (“original fracture networks”) are generated using prescribed statistical distributions for fracture length, spatial positions, and orientations. A rule‑based kinematic growth algorithm is then applied to produce “kinematic fracture networks” that share the same fracture intensity (\(P_{20}\) and \(P_{21}\)) and orientations but contain a substantial proportion of T‑type intersections [Zhu 2023, pp. 1‑1, 3‑4].

- **Kinematic Growth Algorithm**: Growth follows a simplified nucleation‑growth‑arrest scheme based on Davy et al. (2013, 2010) and Bonneau et al. (2013). Fracture tips grow at a constant velocity (\(n=0\) in the sub‑critical growth law \(v = A (K_I / K_{IC})^n\)), with a length‑dependent random component to match the prescribed intensity [Zhu 2023, pp. 3‑4]. Each tip arrests upon encountering a large fracture [Zhu 2023, pp. 3‑4]. The growth velocity for the \(i\)‑th fracture is \(v_i = l_c + \text{rand}(0, \beta \times l_i / l_\text{max})\) [Zhu 2023, pp. 3‑4].

- **Flow Simulations**: Single‑phase flow (permeability) and two‑phase gas‑water flow (ten‑day cumulative gas production) are simulated. Single‑phase boundary conditions: constant pressure at inlet (200 kPa, left) and outlet (0 kPa, right), impermeable top/bottom boundaries, Reynolds number constrained to \(O(10^{-3})\) [Zhu 2023, pp. 4‑5]. Two‑phase setup: ultra‑low‑permeability matrix (1.0 μd), high‑permeability fractures (10 darcies), initial formation pressure 30,000 kPa, horizontal well at middle with bottom‑hole pressure 10,000 kPa [Zhu 2023, pp. 4‑5]. Fractures are represented as 3D objects with constant height; matrix porosity 0.05, fracture porosity 1.0 [Zhu 2023, pp. 5‑6].

- **Connectivity Metric**: Topological connectivity is measured by \(C_B\), the mean number of linkages per branch [Zhu 2023, pp. 2‑3].

## Key Findings

- Kinematic fracture networks (with T‑type intersections) connect more fractures into a larger cluster while generally having fewer total intersections than the original networks [Zhu 2023, pp. 5‑6].
- In 61 of 90 cases, kinematic networks show higher single‑phase permeability than original networks; permeability enhancement can reach up to 3.5 times [Zhu 2023, pp. 5‑6]. Overall, 68% of cases exhibit permeability enhancement, and 77% show higher cumulative gas production [Zhu 2023, pp. 6‑8].
- Kinematic networks composed of small fractures (larger power‑law exponent \(a\)) and with strong spatial clustering (smaller fractal dimension \(F_D\)) tend to have higher permeability enhancement. In contrast, concentrated fracture orientations (parameter \(\kappa\)) show a non‑monotonic or weakly negative impact on flow enhancement [Zhu 2023, pp. 5‑6, 6‑8].
- Flow results (permeability, cumulative production) have strong positive correlations with the connectivity index \(C_B\), but they are **nonequivalent**: the number of inlets and outlets at the domain boundaries correlates even more strongly with flow results (correlation coefficients up to 0.97) than the connectivity index does [Zhu 2023, pp. 6‑8].
- The sensitivity of production ratio to geometrical parameters differs from that of permeability ratio, indicating that two‑phase flow does not simply mirror single‑phase permeability trends [Zhu 2023, pp. 6‑8].

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 87 of 90 kinematic fracture networks have different length distributions from original ones (Two‑sample K‑S test), necessary to match prescribed intensity. | [Zhu 2023, pp. 4‑5] | Same \(P_{20}, P_{21}\), same orientations; growth velocity given by Eq. (4). | Kinematic networks are statistically distinct in length but share intensity and orientation. |
| Kinematic networks connect more fractures with fewer intersections and yield better connectivity. | [Zhu 2023, pp. 5‑6] | Over‑percolative synthetic DFNs; \(C_B\) as connectivity metric. | Connectivity enhancement is nearly universal (100% of cases). |
| 61/90 cases show increased permeability in kinematic networks; maximum increase 3.5×; 68% of cases show permeability enhancement. | [Zhu 2023, pp. 5‑6, 6‑8] | Single‑phase flow, constant pressure boundaries. | Enhancement percentage varies by sub‑figure (a, b, c) in Fig. 10. |
| 77% of cases show higher cumulative gas production in kinematic networks (10 days). | [Zhu 2023, pp. 6‑8] | Two‑phase gas‑water simulation, ultra‑low‑permeability matrix; well‑based production. | |
| Flow results strongly positively correlate with connectivity index, but even more strongly with the number of inlets/outlets (e.g., \(r=0.97\) for permeability‑inlets/outlets in kinematic networks). | [Zhu 2023, pp. 8‑8] | Correlation analysis across original and kinematic networks. | The number of inlets/outlets is not an independent geometrical parameter. |

## Limitations

- The study is restricted to **two‑dimensional** fracture networks; 3D extensions are noted as possible but not carried out here [Zhu 2023, pp. 2‑3].
- Fracture **aperture variations** are not included; the connectivity analysis is purely topological [Zhu 2023, pp. 2‑3].
- The growth parameters (constant velocity \(v_c\), weight \(\beta\)) are chosen by trial and error [Zhu 2023, pp. 3‑4]; the sensitivity to these algorithmic choices is not systematically explored in the provided fragments.
- Two‑phase simulation is limited to **10 days** due to computational cost [Zhu 2023, pp. 4‑5]; longer‑term production behavior is not assessed in the indexed material.
- The matrix is assumed ultra‑low‑permeability and fractures have fixed, high permeability (10 darcies); fracture‑matrix transfer processes may be simplified [Zhu 2023, pp. 4‑5].

## Assumptions / Conditions

- Fracture networks are statistically characterized by a **power‑law length distribution** (exponent \(a\)), spatial clustering (fractal dimension \(F_D\)), and von Mises‑Fisher orientation concentration (\(\kappa\)) [Zhu 2023, pp. 2‑3].
- All networks are generated to an **over‑percolative state** where intensity equals twice the percolation threshold intensity [Zhu 2023, pp. 2‑3].
- The kinematic growth algorithm uses **constant fracture growth velocity** (\(n=0\)) and an arrest rule when a tip meets a large fracture [Zhu 2023, pp. 3‑4].
- **Matrix is impermeable** in single‑phase flow simulations; for two‑phase flow, the matrix has a permeability of 1.0 μd and fractures 10 darcies [Zhu 2023, pp. 4‑5].
- Flow is driven by **constant pressure boundary conditions** in single‑phase and a constant bottom‑hole pressure in two‑phase simulations [Zhu 2023, pp. 4‑5].
- Kinematic and original networks share identical fracture intensity (\(P_{20}, P_{21}\)) and orientation distributions; only the spatial arrangement and connectivity are altered by the growth process [Zhu 2023, pp. 4‑5].

## Key Variables / Parameters

- **Independent geometrical parameters** (Taguchi factors): Power‑law length exponent \(a\), spatial clustering \(F_D\) (fractal dimension), orientation concentration parameter \(\kappa\) [Zhu 2023, pp. 2‑3].
- **Connectivity metrics**: Mean number of linkages per branch \(C_B\) [Zhu 2023, pp. 2‑3]; number of T‑type intersections \(N_T\) vs. total intersections; ratios \(N_{lc}/N_t\), \(L_{lc}/L_t\) for largest cluster [Zhu 2023, pp. 6‑8].
- **Flow responses**: Single‑phase permeability; 10‑day cumulative gas production; permeability ratio and production ratio (kinematic/original) [Zhu 2023, pp. 5‑6, 6‑8].
- **Boundary‑condition counts**: Number of inlets and outlets at domain boundaries [Zhu 2023, pp. 8‑8].
- **Growth‑related parameters**: Sub‑critical index \(n\) (set to 0), constant velocity \(l_c\) (5 units/step), weight \(\beta\) (2.0), Eq. (4) [Zhu 2023, pp. 3‑4].
- **Flow parameters**: Inlet pressure 200 kPa, outlet 0 kPa, pressure gradient 2.0 kPa/m, Reynolds number \(O(10^{-3})\); matrix permeability 1.0 μd, fracture permeability 10 d, porosity values, initial pressure 30,000 kPa, bottom‑hole pressure 10,000 kPa [Zhu 2023, pp. 4‑5, 5‑6].

## Reusable Claims

- **Claim 1**: In over‑percolative two‑dimensional DFNs governed by power‑law length, clustering, and orientation statistics, applying a kinematic fracture growth algorithm that preserves intensity and orientation while forming T‑type intersections results in kinematic networks that almost always have **higher topological connectivity (by \(C_B\))**, even though the **total number of intersections usually decreases** [Zhu 2023, pp. 5‑6].  
  *Conditions*: Applicable under the chosen nucleation‑growth‑arrest rules with constant velocity; network in an over‑percolative state; 2D networks. *Limitations*: Unclear if 3D or different arrest criteria yield the same result.

- **Claim 2**: For the same boundary conditions, the **kinematic fracture networks exhibit higher single‑phase permeability in 68% of cases** and **higher cumulative two‑phase gas production in 77% of cases** compared to stochastic networks without T‑type growth, with flow enhancement being more pronounced for networks composed of **small fractures (larger exponent \(a\)) and strong clustering (smaller \(F_D\))** [Zhu 2023, pp. 5‑6, 6‑8].  
  *Conditions*: 2D; constant pressure drop; two‑phase production simulated for 10 days; matrix permeability 1.0 μd, fracture permeability 10 d. *Limitations*: Not universal; 32% and 23% of cases do not show enhancement.

- **Claim 3**: Connectivity and flow performance are **not equivalent** in fracture networks: the number of inlets/outlets can have a higher correlation with permeability and production than the connectivity index \(C_B\), especially in networks with permeability contrast [Zhu 2023, pp. 8‑8].  
  *Conditions*: Over‑percolative networks; constant pressure boundary conditions. *Limitations*: Number of inlets/outlets is not an independent parameter, so causal relationships are difficult to isolate from the provided data.

- **Claim 4**: The kinematic growth procedure (Eq. (4)) that couples growth velocity to original fracture length ensures that **larger original fractures grow faster**, helping kinematic networks retain a similar shape while matching the prescribed intensity; this **necessitates a different length distribution** in kinematic networks (confirmed in 87/90 cases by K‑S test) [Zhu 2023, pp. 3‑4, 4‑5].

## Candidate Concepts

- [[fracture connectivity]]  
- [[T-type intersection]]  
- [[stochastic discrete fracture network]]  
- [[kinematic fracture growth]]  
- [[over-percolative state]]  
- [[percolation threshold]]  
- [[power-law fracture length distribution]]  
- [[fracture spatial clustering]]  
- [[fracture orientation concentration]]  
- [[single-phase permeability in fractured media]]  
- [[two-phase flow in fractured reservoirs]]  
- [[topological connectivity measure CB]]  
- [[inlet-outlet effect]]  
- [[Taguchi orthogonal array design]]

## Candidate Methods

- [[kinematic fracture growth algorithm (nucleation-growth-arrest)]] – based on Davy et al. 2010, 2013; used to generate T‑type‑rich networks [Zhu 2023, pp. 1‑2, 3‑4].  
- [[stochastic DFN model with power-law length, fractal clustering, and von Mises-Fisher orientation]] [Zhu 2023, pp. 2‑3].  
- [[single-phase flow in discrete fractures with constant pressure boundaries]] [Zhu 2023, pp. 4‑5].  
- [[two-phase gas-water simulation in fractured porous media with ultra-low matrix permeability]] – UNCONG simulator, 3D representation of 2D fractures [Zhu 2023, pp. 4‑5].  
- [[topological connectivity analysis – CB index]] [Zhu 2023, pp. 2‑3].  
- [[Two-sample Kolmogorov-Smirnov test for length distributions]] [Zhu 2023, pp. 4‑5].  
- [[input-output correlation analysis for sensitivity]] [Zhu 2023, pp. 6‑8, 8‑8].  
- [[ternary diagram of fracture intersection types]] – used to contextualize natural fracture data [Zhu 2023, pp. 8‑8].

## Connections To Other Work

- The kinematic growth method directly builds on the **nucleation‑growth‑arrest scheme** of **Davy et al. (2013, 2010)**, which itself simplifies mechanical calculations to generate T‑type intersections [Zhu 2023, pp. 1‑2, 3‑4].
- The work follows **Bonneau et al. (2013)** in examining fracture coalescence and connectivity, and **Maillot et al. (2016)**, who investigated T‑type intersections’ impact on connectivity and flow but limited their study to comparisons between kinematic and Poissonian models with uniform fracture centers and orientations [Zhu 2023, pp. 1‑2].
- The percolation threshold caveat (“conventional percolation threshold … only applicable to the Poisson model dominated by small fractures”) connects to **Bour and Davy (1997a)** and **Zhu et al. (2018)** [Zhu 2023, pp. 1‑2].
- The finding that **\(p_f\) is an invalid connectivity parameter for complex networks** references **Bour and Davy (1998)** and **Zhu et al. (2018)** [Zhu 2023, pp. 5‑6].
- Statistical parameter ranges (exponent \(a=[2.0,3.0]\), κ < 3.0) are informed by **Bonnet et al. (2001)** and **Zhu et al. (2018, 2022b)** [Zhu 2023, pp. 2‑3].
- The observation that natural fractures are clustered rather than uniform references **Akara et al. (2021)** and **Zhu et al. (2018)** [Zhu 2023, pp. 1‑2].
- The over‑percolative state being common in outcrops is drawn from **Watkins et al. (2015)** and **Zhu et al. (2022d)** [Zhu 2023, pp. 2‑3].
- **Candidate broader connections** that are not directly confirmed by specific cross‑study comparisons in the fragments: can link from a thematic perspective to topics such as [[fracture network flow upscaling]], [[3D DFN connectivity]], [[subcritical crack growth index n]], and [[mechanical stratigraphy controls on T-type intersections]].

## Open Questions

- Whether the enhanced connectivity and flow results observed in 2D hold for **three‑dimensional fracture networks** remains unconfirmed from these fragments [Zhu 2023, pp. 2‑3].
- The sensitivity of conclusions to the **choices of growth parameters** (\(l_c, \beta, n=0\)) and **arrest rules** is not reported in the indexed sections; other kinematic rules could yield different proportions of enhancement.
- The relationship between **T‑type network structure** and **two‑phase flow relative permeability/phase interference** is not detailed beyond the production‑ratio result.
- The **mechanistic causes** of why inlet/outlet counts correlate so strongly with flow, and whether this is an artifact of boundary conditions, is an open issue identified by the authors [Zhu 2023, pp. 8‑8].

## Source Coverage

This page is based on **11 indexing fragments** drawn from the Abstract, Introduction, Methods (fracture generation, kinematic growth, flow simulation), Results, and Discussion sections of Zhu et al. (2023).  
**Covered well**: general problem statement, model setup, parameter ranges, algorithmic steps, connectivity‑flow results, and sensitivity/summary conclusions.  
**Potentially underrepresented or missing**: detailed validation against natural fracture maps (mentioned but not extensively described in these fragments), full parameter sensitivity tables beyond the discussed trends, detailed two‑phase flow mechanisms, and any appendix data. The influence of fracture aperture heterogeneity, mechanical layering, and alternative growth rules is not assessed in the provided fragments.
