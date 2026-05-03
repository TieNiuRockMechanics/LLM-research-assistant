---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2015-lei-a-new-approach-to-upscaling-fracture-network-models-while-preserving-geostatistical-and"
title: "A New Approach to Upscaling Fracture Network Models While Preserving Geostatistical and Geomechanical Characteristics."
status: "draft"
source_pdf: "data/papers/2015 - A new approach to upscaling fracture network models while preserving geostatistical and geomechanical characteristics.pdf"
collections:
citation: "Lei, Qinghua, et al. \"A New Approach to Upscaling Fracture Network Models While Preserving Geostatistical and Geomechanical Characteristics.\" *Journal of Geophysical Research: Solid Earth*, vol. 120, 2015, pp. 4784–, doi:10.1002/2014JB011736."
indexed_texts: "22"
indexed_chars: "107132"
nonempty_source_blocks: "22"
compiled_source_blocks: "22"
compiled_source_chars: "107570"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004088"
coverage_status: "full-index"
source_signature: "33190960a2782c195c899bc6f8e15675a39e340c"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T15:44:38"
---

# A New Approach to Upscaling Fracture Network Models While Preserving Geostatistical and Geomechanical Characteristics.

## One-line Summary
A novel 2D fracture network upscaling method using discrete-time random walks in recursive self-referencing lattices that preserves geostatistical and geomechanical characteristics from a smaller-scale outcrop pattern, applied to study permeability scaling and flow structure transitions under different stress conditions [Lei 2015, pp. 1-1].

## Research Question
How can hydromechanical properties of larger-scale natural fracture systems be estimated based on a small-sized model, while preserving both geostatistical network topology and geomechanically realistic, stress- and scale-dependent aperture and shear displacement distributions? [Lei 2015, pp. 1-2].

## Study Area / Data
- **Outcrop location:** Kilve, southern margin of the Bristol Channel Basin [Lei 2015, pp. 2-4].
- **Mapped area:** Approximately 225 m² [Lei 2015, pp. 2-4].
- **Geology:** Fractured limestone layer (~26 cm thick) sandwiched between almost impervious shales; two oblique vertical, layer-normal fracture sets (Set 1 striking ~100°, Set 2 striking ~140°) formed extensionally and filled with calcite [Lei 2015, pp. 2-4].
- **Analyzed sample:** A 6 m × 6 m extracted subarea containing ~1000 fractures used for scaling property analysis; a 2 m × 2 m subarea used for geomechanical modeling and as the source for upscaling [Lei 2015, pp. 2-4].

## Methods
1. **Scaling property analysis (sample scale):** Fractal dimension *D* via two-point correlation function; length exponent *a* via density and cumulative distributions; connectivity via percolation parameter *p* and connection length *Lc* [Lei 2015, pp. 4-6].
2. **Geomechanical modeling (FEMDEM):** Biaxial effective stresses applied (hydrostatic σ′x/σ′y=1; deviatoric σ′x/σ′y=2 with σ′y=5 MPa) to a 2 m × 2 m fractured limestone sample using material properties from [Lama and Vutukuri, 1978]; mesoscopic (network-scale opening/shearing) and microscopic (fracture-scale closure/dilation) effects synthesized to obtain stress-dependent aperture and shear displacement distributions [Lei 2015, pp. 11-14].
3. **Fracture network growth model:** Recursive self-referencing lattice with source cell (SC) and growth cells (GCs); discrete-time random walks for fracture nucleation and propagation preserving fracture barycenter spatial distribution (exclusion radius/spacing), censored/uncensored fracture types, and individual fracture properties (length, orientation, curvature, segmentation) [Lei 2015, pp. 7-10].
4. **Attribute scaling and coupling:** Fracture displacement attributes upgraded by scaling factors derived from power-law length correlations (exponents *n1*, *n2*); shear-induced dilation modeled with Barton's empirical model [Lei 2015, pp. 14-16].
5. **Flow simulation:** Single-phase flow modeled via hybrid finite element-finite volume method; equivalent permeability computed for multiscale growth realizations (2 m to 54 m) under hydrostatic and deviatoric stress conditions [Lei 2015, pp. 17-18].

## Key Findings
1. The Kilve outcrop fracture pattern is **nonfractal** (*D* ≈ 2.0), while its length distribution follows a power law with exponent **2 < a < 3** [Lei 2015, pp. 4-5].
2. Connection length *Lc* ≈ 0.80 m, with network connectivity increasing with scale (since *a* < *D* + 1) [Lei 2015, pp. 5-6].
3. Stress state significantly influences displacement-length correlations: aperture exponent *n2* = 0.568 (hydrostatic) vs. 0.635 (deviatoric); shear displacement exponent *n1* = 0.406 (hydrostatic) vs. 1.148 (deviatoric) [Lei 2015, pp. 14-16].
4. **Permeability scaling trends diverge by stress condition:** Deviatoric case shows upward trend at small/intermediate scales (<10–20 m) then downward at larger scales (>20 m); hydrostatic case mainly shows downward trend [Lei 2015, pp. 17-18].
5. A **flow structure transition zone** exists between the connecting scale (*Lc* < 2 m) and the channeling scale (ξ at 20–50 m), where flow shifts from extremely channeled to distributed [Lei 2015, pp. 18-19].
6. **Geometric mean aperture tracks the median permeability trend** well, while arithmetic and harmonic means provide upper and lower bounds respectively [Lei 2015, pp. 19-20].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| *Dc* ≈ 2.0 (thus *D* ≈ 2.0) from two-point correlation function | [Lei 2015, pp. 4-5] | 6 m × 6 m pattern at Kilve | Fracture barycenters exhibit homogeneous 2D filling (nonfractal) |
| Length exponent *a* = 2.37 (density distribution) | [Lei 2015, pp. 4-5] | Lower cutoff 0.3 m (5% × *L*), censoring corrected | Density term α = 3.28; cumulative distribution gives a = 2.45 |
| Connection length *Lc* ≈ 0.80 m | [Lei 2015, pp. 5-6] | *pc* between 5.6–6.0, a = 2.37, D = 2.0 | Marginally influenced by *lmin* (0.05 m) |
| Hydrostatic: *n2* = 0.568; Deviatoric: *n2* = 0.635 | [Lei 2015, pp. 14-16] | σ′y = 5 MPa; limestone properties per Table 2 | Aperture-length correlation influenced by a priori square-root model |
| Hydrostatic: *n1* = 0.406; Deviatoric: *n1* = 1.148 | [Lei 2015, pp. 14-16] | Same stress conditions | Shear displacement-length correlation |
| Growth networks: D ≈ 1.96–1.98 across scales | [Lei 2015, pp. 17-18] | 2 m to 54 m, 10 realizations per stress | Recursive cell culture preserves nonfractality |
| Growth networks: a ≈ 2.43–2.66 across scales | [Lei 2015, pp. 17-18] | Same as above | Scale invariance of P21 and intersection density ω |
| Deviatoric permeability upward then downward | [Lei 2015, pp. 17-18] | km = 1×10⁻¹⁵ m², kf/km > 10⁵–10⁶ | Dominated by long-fracture transmissivity scaling |
| Flow structure transition at ξ ≈ 20–50 m | [Lei 2015, pp. 18-19] | Deviatoric stress | From channeled to distributed flow |

## Limitations
- **2D analysis** used for actual 3D fracture systems; finite layer thickness, bedding interfaces, and 3D delamination effects not captured [Lei 2015, pp. 20-21].
- **Repetition assumption** (growth cells share same length distribution as source) is a first-order approximation; heterogeneous source patterns not accounted for [Lei 2015, pp. 20-21].
- Length exponent discrepancy in upscaled networks (a ≈ 2.43→2.66) may reflect sampling bias from limited source data [Lei 2015, pp. 10-11].
- **Crack propagation neglected** due to minor effect on fracture density variation [Lei 2015, pp. 17-18].
- Hydraulic aperture equated to mechanical aperture, which may overestimate flow rates by a roughness-dependent factor of ≤2 [Lei 2015, pp. 16-17].
- **P21 scale dependency** predicted by power-law theory (Equation 26) not captured by the growth model [Lei 2015, pp. 20-21].
- Correlation between fracture position and length not incorporated [Lei 2015, pp. 20-21].
- Valid for scales ~1–100 m; larger scales (~1 km and beyond) involve additional complexities (seismically visible faults, multiple rock types, karst) not addressed [Lei 2015, pp. 1-2].

## Assumptions / Conditions
- Fracture pattern obeys power-law length distribution with 2 < a < 3 and nonfractal spatial organization (*D* ≈ 2) [Lei 2015, pp. 1-2].
- A priori initial apertures follow sublinear square-root scaling with length (Equation 10) from linear elastic fracture mechanics [Lei 2015, pp. 6-7].
- Fracture walls initially share identical coordinates; no initial shear displacements [Lei 2015, pp. 6-7].
- Fracture sets are distinct and crosscut with few abutting relationships (geological arresting not modeled) [Lei 2015, pp. 2-4].
- Barycenter is the initial nucleus position for idealized symmetrical crack development [Lei 2015, pp. 7-9].
- Matrix permeability *km* = 1×10⁻¹⁵ m² (lower bound for fractured hydrocarbon reservoirs) [Lei 2015, pp. 17-18].
- Plane strain conditions; biaxial far-field stresses with zero shear stress (*τ′xy* = 0) [Lei 2015, pp. 14-16].
- Fracture-dominated flow assured by *kf*/*km* > 10⁵–10⁶ [Lei 2015, pp. 17-18].

## Key Variables / Parameters
- **Fractal dimension *D*** ≈ 2.0 (correlation dimension *Dc* ≈ 2.0) [Lei 2015, pp. 4-5]
- **Power-law length exponent *a*** = 2.37 (density distribution); density term *α* = 3.28 [Lei 2015, pp. 4-5]
- **Fracture intensity *P21*** ≈ 10.7–10.8 m⁻¹ (growth networks) [Lei 2015, pp. 17-18]
- **Percolation parameter *p***: 7.48 (2 m) → 14.43 (54 m) for growth networks [Lei 2015, pp. 17-18]
- **Connection length *Lc*** ≈ 0.80 m [Lei 2015, pp. 5-6]
- **Aperture-length exponent *n2***: 0.568 (hydrostatic); 0.635 (deviatoric) [Lei 2015, pp. 14-16]
- **Shear displacement-length exponent *n1***: 0.406 (hydrostatic); 1.148 (deviatoric) [Lei 2015, pp. 14-16]
- **Channelling scale *ξ*** ≈ 20–50 m (deviatoric case) [Lei 2015, pp. 18-19]
- **Effective stresses**: σ′y = 5 MPa; σ′x/σ′y = 1 or 2 [Lei 2015, pp. 11-13]
- **Material properties (limestone)**: Young's modulus 30 GPa, Poisson's ratio 0.27, tensile strength 7 MPa, cohesion 15 MPa, energy release rate 1 kJ/m², JRC 5, JCS 100 MPa, friction coefficient 0.6 [Lei 2015, pp. 11-13]
- **Equivalent fracture apertures**: harmonic ≈0.06–0.07 mm; geometric ≈0.09–0.13 mm; arithmetic ≈0.12–0.63 mm (varying by stress and scale) [Lei 2015, pp. 17-18]

## Reusable Claims
1. **Claim:** For the studied nonfractal pattern (*D* ≈ 2) with 2 < *a* < 3, connectivity increases with scale, and the connection length *Lc* is marginally influenced by *lmin* when *a* < *D* + 1. [Lei 2015, pp. 5-6]
   **Condition:** Power-law length distribution valid; *pc* between 5.6–6.0.
2. **Claim:** Geomechanically constrained displacement-length exponents (*n1*, *n2*) deviate from classical analytical solutions due to topological complexity (crosscutting, segmentation, curvature) and non-critical stress states; stress ratio significantly affects these exponents. [Lei 2015, pp. 20-21]
   **Condition:** FEMDEM modeling with specific limestone properties and boundary stresses.
3. **Claim:** Under deviatoric stress, permeability shows an initial increase with scale (due to long-fracture dominance aided by length-correlated wide apertures) followed by a decrease at larger scales (as traversing fracture probability diminishes). Under hydrostatic stress, permeability mainly decreases with scale (lack of shear-induced dilation). [Lei 2015, pp. 17-19]
   **Condition:** 2 < *a* < 3; fracture-dominated flow (*kf*/*km* ≫ 1).
4. **Claim:** The flow structure transitions from extremely channeled (at scales between *Lc* and *ξ*) to distributed (above *ξ*), equivalent to a network alteration from "parallel" (arithmetic mean applicable) to "series" (harmonic mean applicable) behavior. Geometric mean tracks the median permeability trend across this transition. [Lei 2015, pp. 19-20]
   **Condition:** 2D fractured porous media with broad aperture-length correlations.
5. **Claim:** Fracture curvature (tortuosity) nontrivially reduces transmissivity; the effect depends on the degree of tortuosity. [Lei 2015, pp. 22-23]
   **Condition:** Single-fracture sinusoidal models with constant aperture; demonstrated for specific curvature amplitudes.

## Candidate Concepts
- [[fractal dimension of fracture networks]]
- [[power-law length distribution]]
- [[fracture connectivity scaling]]
- [[percolation parameter]]
- [[connection length]]
- [[channelling scale]]
- [[flow structure transition]]
- [[displacement-length scaling]]
- [[geomechanical upscaling]]
- [[self-referencing growth lattice]]
- [[discrete-time random walk]]
- [[stress-dependent aperture]]
- [[shear-induced dilation]]
- [[equivalent permeability bounds]]
- [[fracture curvature tortuosity]]

## Candidate Methods
- [[two-point correlation function for fractal dimension]]
- [[Kaplan-Meier censoring correction for cumulative length distribution]]
- [[density distribution analysis for power-law exponent]]
- [[combined finite-discrete element method (FEMDEM)]]
- [[Barton-Bandis hyperbolic closure model]]
- [[recursive cell culture upscaling]]
- [[barycenter point packing with exclusion constraints]]
- [[discrete-time random walk with curvature control]]
- [[hybrid finite element-finite volume flow simulation]]
- [[hydromechanical coupling via displacement scaling factors]]

## Connections To Other Work
- **Permeability scale dependence:** Building on [Clauser, 1992]; distinguishing laboratory vs. borehole vs. regional scale trends [Lei 2015, pp. 1-2].
- **DFN flow modeling:** Extends prior work on flow in power-law fracture networks with constant or statistically distributed apertures [de Dreuzy et al., 2001a, 2001b, 2002; Klimczak et al., 2010] by incorporating geomechanically derived, stress-dependent apertures [Lei 2015, pp. 1-2].
- **Fractal and power-law scaling:** Methods and theory draw from [Bonnet et al., 2001; Bour et al., 2002; Darcel et al., 2003b; Davy et al., 2006] [Lei 2015, pp. 4-6].
- **Aperture-length scaling (LEFM):** Initial aperture model follows [Olson, 2003] sublinear square-root correlation, with stress-modified exponents compared to field observations [Walmann et al., 1996; Schultz et al., 2008] [Lei 2015, pp. 6-7, 14-16].
- **Fracture dilation model:** Uses [Asadollahi and Tonon, 2010] based on [Barton et al., 1985] empirical joint behavior [Lei 2015, pp. 14-16].
- **Hydromechanical coupling:** Indirect coupling approach aligns with [Rutqvist and Stephansson, 2003; Min et al., 2004; Baghbanan and Jing, 2008] [Lei 2015, pp. 11-13].

## Open Questions
- Validation of the **a priori square-root aperture-length correlation** universality under different stress scenarios; further exploration of power-law validity for aperture-length relationships needed [Lei 2015, pp. 20-21].
- How to incorporate **heterogeneous source patterns** (extraction from multiple locations) to bound permeability estimates [Lei 2015, pp. 20-21].
- Incorporation of **correlation between fracture position and length** into growth models [Lei 2015, pp. 20-21].
- Extension to **3D fracture network upscaling** with realistic geomechanical constraints, including bedding plane flow and crosscutting fracture effects [Lei 2015, pp. 20-21].
- Development of **random walk algorithms for hierarchical patterns** with sequential formation and geological arrest [Lei 2015, pp. 20-21].
- Investigation of **direct two-way hydromechanical coupling** effects (pore fluid pressure on aperture evolution) during upscaling [Lei 2015, pp. 20-21].
- Upscaling behavior for networks with different fractal dimensions (1 < D < 2) and length exponents (1 < a < 2 or a > 3) [Lei 2015, pp. 20-21].

## Source Coverage
All non-empty indexed fragments (22 blocks, totaling 107,132 characters) were processed. The compiled markdown includes contributions from all 22 source blocks (107,570 compiled characters), achieving full coverage (coverage ratio 1.0 by blocks, 1.004 by characters). Source blocks span pages 1–24 of the original paper.
