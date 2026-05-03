---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2018-yin-xingyao-review-of-in-situ-stress-prediction-technology"
title: "Review of In-Situ Stress Prediction Technology."
status: "draft"
source_pdf: "data/papers/2018 - 地应力预测技术的研究现状与进展.pdf"
collections:
  - "part4-2"
citation: "Yin Xingyao, et al. “Review of In-Situ Stress Prediction Technology.” *Geophysical Prospecting for Petroleum*, vol. 57, no. 4, 2018, pp. 488-504. DOI: 10.3969/j.issn.1000-1441.2018.04.001."
indexed_texts: "16"
indexed_chars: "77614"
nonempty_source_blocks: "16"
compiled_source_blocks: "16"
compiled_source_chars: "73183"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.94291"
coverage_status: "full-index"
source_signature: "d9b743864adfd5895f79db39dceedb0851874485"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T21:28:25"
---

# Review of In-Situ Stress Prediction Technology.

## One-line Summary
A review summarizing four categories of in‑situ stress prediction methods—direct measurement, logging calculation, numerical simulation, and seismic prediction—with emphasis on seismic methods that yield three‑dimensional stress profiles for shale gas development.

## Research Question
How can in‑situ stress be accurately predicted for low‑porosity, low‑permeability shale reservoirs to guide hydraulic fracturing, well‑wall stability, drilling optimization, and hydrocarbon migration analysis?

## Study Area / Data
The paper is a methodological review without a single field‑specific study area. An application example (Section 4) uses azimuthal stacked seismic data from an unnamed work area [Yin 2018, pp. 10-12] where six partial‑angle stacks in different azimuths were inverted for elastic and anisotropic parameters to compute the orthorhombic differential horizontal stress ratio (ODHSR). Laboratory measurements, well logs, core samples, and finite‑element models are referenced conceptually.

## Methods
The review organizes prediction techniques into four groups:

1. **Direct measurement methods** [Yin 2018, pp. 1-3]  
   *Classified into absolute stress (direct and indirect) and relative stress measurements.*  
   – Hydraulic fracturing (HF and HTPF)  
   – Acoustic emission (Kaiser effect)  
   – Geological structure information (Andersonian fault‑stress regimes)  
   – Stress relief (overcoring, flat jack, etc.)  
   – Anelastic strain recovery (ASR)  
   – Differential strain curve analysis (DSCA)  

2. **Log‑based calculation methods** [Yin 2018, pp. 3-5]  
   – Borehole breakout and induced fracture analysis from FMI/CBIL imaging logs: equations (1)–(8) using breakout width, depth, and borehole diameter to solve for σ _H, σ _h.  
   – Stress orientation from multi‑pole sonic logs via fast shear‑wave azimuth [Yin Xingyao 2018, pp. 3-4].  
   – Stress magnitudes from sonic logs: convert dynamic elastic moduli to static moduli via rock integrity coefficients, then compute σ _v by density integration (9) and horizontal stresses using models:  
     * Kinnick / Matthewell‑Kelly (eq. 10, 11) – isotropic horizontal stresses.  
     * Huang model (eq. 12, 13) – introduces tectonic coefficients ω 1, ω 2.  
     * Spring model (eq. 14, 15) – incorporates tectonic strain ε h, ε H and static elastic parameters.  
     * Dipping‑layer model (eq. 16, 17) – accounts for dip φ and azimuth β.  
     * Ge Hongkui’s stratified model (eq. 18–21) – differentiates vertical and horizontal fractures, includes temperature and tectonic coefficients.  

3. **Numerical simulation methods** [Yin 2018, pp. 5-6]  
   – Boundary displacement adjustment (Guo et al.)  
   – Boundary load adjustment (Xue et al.)  
   – Displacement back‑analysis (inverse and direct methods)  
   – Stress function / displacement function methods (polynomial fitting, finite‑element correction)  
   – Other approaches: grey system (Li et al.), ANN+genetic algorithm (Shi et al.), optimization inversion (Gioda)  

4. **Seismic prediction methods** [Yin 2018, pp. 6-10]  
   – Reflection coefficient inversion (Tigrek): objective function (22) using PP and PS reflectivities; dynamic parameters inverted then converted to static ones for a geomechanical model.  
   – Curvature‑attribute methods: linear relation σ = E·K c (Hunt, eq. 24); thin‑plate theory derivation (He, eq. 25‑27) linking curvature and stress. Xiong et al. combined curvature‑derived horizontal strain with a spring model.  
   – Rock‑physics modeling: build an equivalent model (e.g., VTI for shale, HTI, or orthorhombic) from seismic‑log data to obtain stiffness matrix → elastic moduli → stress. Key equations:  
     * VTI stress calculations (Suarez‑Rivera, eq. 30‑32).  
     * HTI stress with DHSR (Gray, eq. 33‑35).  
     * Orthorhombic exact and approximate formulas (Ma et al., eq. 36‑42) leading to ODHSR.  
   – Azimuthal elastic impedance (AEI) inversion: linearized AEI equation (43‑44) → 6‑equation system (45‑46) using two azimuths and three angles → invert for V P, V S, density, and HTI anisotropy parameters → convert to VTI parameters → compute ODHSR. Demonstration with real data produced ODHSR slices identifying zones amenable to network fracturing (low ODHSR).  

## Key Findings
- Different stress prediction methods reflect different information scales; selection depends on applicable conditions and expected results [Yin 2018, pp. 1-1, 1‑3].  
- Log‑based methods extend point measurements to quasi‑continuous profiles, with imaging logs providing stress orientation via breakout/induced fractures and sonic logs enabling dynamic‑to‑static conversion for magnitudes [Yin 2018, pp. 3-6].  
- Numerical simulation can replicate three‑dimensional stress fields under tectonic constraints; boundary‑adjustment methods suit simple media, back‑analysis and function methods handle more complexity [Yin 2018, pp. 5-6].  
- Seismic methods enable areal continuity: the ODHSR (orthorhombic differential horizontal stress ratio) is an indicator of fracture‑network potential—low values facilitate hydraulic fracturing networks, high values tend to produce aligned fractures [Yin 2018, pp. 8-10].  
- The inversion workflow using azimuthal seismic data can map VTI anisotropy parameters and compute ODHSR, demonstrated on a real dataset [Yin 2018, pp. 10-12].  

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Hydraulic fracturing is the most widely used deep stress measurement method; HF assumes homogeneous, isotropic, linearly elastic medium with borehole aligned to a principal stress | Yin 2018, pp. 1-3 (Fairhurst 1964; Haimson 1968) | Requires intact rock, known fracture initiation pressure; HTPF extends to fractured rock | Classic HF yields plane stress; HTPF provides 3D but is time‑consuming |
| Kaiser effect (AE method) records elastic wave surges at historical maximum stress levels; can retrieve in‑situ stress orientation/magnitude from oriented cores | Yin 2018, pp. 1-3 (Kaiser; Li & Zhang 2004) | Requires laboratory loading tests on oriented samples | Sensitive to rock type, loading rate, and prior damage |
| Borehole breakout long axis indicates minimum horizontal stress direction; induced tensile fractures strike parallel to maximum horizontal stress | Yin 2018, pp. 3-4 (Huang et al. 2006; Zhao et al.) | Valid only when stress‑induced ellipticity can be distinguished from washouts; wellbore must be stable | Imaging logs (FMI/CBIL) provide breakout geometry; dipmeter logs can also identify breakout azimuth |
| Equations (4)-(5) compute σ_H and σ_h from breakout width, depth, and rock strength with a stability check (6) | Yin 2018, pp. 4-5 (Zhao, Liu et al.) | Requires calibrated rock cohesion, friction coefficient, and borehole pressure; breakout must be in stable state | Derived from shear failure criteria near wellbore |
| Dynamic elastic moduli from sonic logs must be converted to static moduli via rock integrity factors for accurate stress calculation | Yin 2018, pp. 5-6 (Lou 1989, Lin et al. 1998) | Valid only if a reliable dynamic‑static correlation exists for the formation | Conversion factor varies with lithology, porosity, and stress history |
| Spring model (eq. 14-15) incorporates tectonic strain ε_h, ε_H and static E, μ; provides layered stress estimates in tectonically active areas | Yin 2018, pp. 5-6 (Ge et al. 1998) | Assumes linear transversely isotropic elastic medium, ignores dipping layers | Widely used in PetroChina logging stress calculations |
| Dipping‑layer model (eq. 16‑17) accounts for formation dip φ and azimuth β0 with tectonic coefficients A, B | Yin 2018, pp. 5-6 | Requires knowledge of dip and stress‑coordinate orientation; assumes constant Poisson’s ratio | Extends spring model to inclined strata |
| Finite‑element boundary displacement adjustment fits modelled stress to measurements by iterating boundary displacements; best for simple geology | Yin 2018, pp. 6-7 (Guo et al. 1983; Zhu 1994) | Requires reliable in‑situ stress measurements for regression; geometric and mechanical model quality crucial | Workload large in heterogeneous settings |
| Displacement back‑analysis retrieves initial stress from measured displacements; direct method needs linear elasticity, inverse method more general | Yin 2018, pp. 7-8 (Zhao et al. 2004; Guo 2009) | Useful when direct stress data scarce; accuracy depends on displacement measurement density | Inverse method uses optimization; can incorporate plastic behaviour |
| Curvature‑stress relation σ = E·K_c (Hunt et al. 2011) approximates stress for fracture density prediction; thin‑plate theory yields σ_x, σ_y, τ_xy from curvature and elastic moduli | Yin 2018, pp. 7-8 (Hunt et al., He 2011) | Assumes small deflection thin‑plate bending; need reliable seismic curvature attributes and E, ν from inversion | Simplified representation of tectonic stress |
| PP‑PS reflectivity joint inversion (Tigrek 2003) obtains dynamic parameters; static parameter conversion yields geomechanical model and stress | Yin 2018, pp. 7-8 | Requires multi‑component seismic data, accurate wavelet, and good dynamic‑static ratio calibration | Objective function (22) sum of normalized misfits of PP and PS coefficients |
| Orthorhombic DHSR (ODHSR) exact formula (38) and elastic‑coefficient form (39); approximate form (42) uses V_P0, V_S0, ρ, γ, and normal compliance Z_N | Yin 2018, pp. 8-10 (Ma et al. 2017, 2018) | Assumes orthorhombic symmetry (combined VTI and HTI); uses linear‑slip theory approximation; anisotropy parameters from azimuthal inversion | Low ODHSR indicates easy fracture‑network formation |
| Azimuthal EI inversion (46) solves for V_P, V_S, ρ, and HTI anisotropy parameters (δ⁽V⁾, ε⁽V⁾, γ⁽V⁾) from six partial‑stack azimuthal seismic volumes | Yin 2018, pp. 10-12 (Ma et al. 2018) | Requires high‑fold azimuthal gathers, well‑calibrated EI; assumes laterally invariant regression coefficients | Demonstrated on real data yielding ODHSR slices |
| In the example, low ODHSR zones correspond to areas prone to forming fracture networks during hydraulic stimulation | Yin 2018, pp. 12-13 | Valid for the tested work area; corroborates with prior brittleness and fracture‑prediction models | Need integration with other parameters (brittleness, porosity) for development |

## Limitations
- **Measurement methods**: point data, high cost, lack continuity; hydraulic fracturing assumptions (isotropy, borehole alignment) may be violated; ASR/DSCA rely on core recovery and lab conditions [Yin 2018, pp. 2-3].  
- **Logging methods**: stress orientation from breakouts can be contaminated by washouts or fracture‑induced anisotropy; dynamic‑static conversion is empirical and lithology‑dependent; models (e.g., spring model) do not handle dipping beds or complex tectonics [Yin 2018, pp. 4-6].  
- **Numerical simulation**: boundary adjustment methods are computationally heavy for heterogeneous media; regression‑based models need many in‑situ measurements for calibration [Yin 2018, pp. 6-7].  
- **Seismic methods**: require high‑quality multi‑azimuth, multi‑component data; inversion results sensitive to anisotropy parameter coupling; ODHSR approximate formula assumes linear‑slip weak anisotropy; neglects pore‑pressure and tectonic‑stress corrections [Yin 2018, pp. 10-12].  
- Overall, all methods provide partial information; integration and cross‑validation are necessary but not yet routine [Yin 2018, pp. 12-13].

## Assumptions / Conditions
- Many stress‑calculation formulas assume linear elasticity, small strains, and isotropic or transversely isotropic media unless otherwise stated.  
- Hydraulic fracturing measurement assumes a vertical borehole aligned with a principal stress and homogeneous rock mass; HTPF relaxes the homogeneity condition [Yin 2018, pp. 1-2].  
- Log‑based stress models (Kinnick, Matthewell‑Kelly, Huang, spring) assume zero or known tectonic strain coefficients and that σ_v is the overburden from density integration. The spring model adds tectonic strain but assumes uniaxial strain boundary conditions [Yin 2018, pp. 5-6].  
- In seismic curvature methods, the thin‑plate approximation requires small deflections and known elastic thickness [Yin 2018, pp. 7-8].  
- ODHSR derivation assumes orthorhombic symmetry (vertical fractures in a VTI background), linear slip theory, and that the normal compliance Z_N can be inverted from azimuthal seismic [Yin 2018, pp. 8-10].  
- Azimuthal EI inversion assumes that the coefficient matrix derived from well‑logs is constant over the reservoir zone, i.e., lateral rock‑physics stability [Yin 2018, pp. 10-12].

## Key Variables / Parameters
- **Stress components**: σ_v (vertical/overburden), σ_H (maximum horizontal principal stress), σ_h (minimum horizontal principal stress), pore pressure p_p.  
- **Elastic properties**: static and dynamic Poisson’s ratio μ/μ_d, Young’s modulus E/E_d, shear modulus G, bulk modulus K, Lamé coefficients λ, Biot coefficient α.  
- **Tectonic parameters**: tectonic stress coefficients ω 1, ω 2 (Huang model); tectonic strains ε_h, ε_H (spring model); coefficients A, B (dipping model); K_h, K_H (stratified model).  
- **Anisotropy parameters**: VTI Thomsen parameters ε, δ, γ; HTI parameters δ⁽V⁾, ε⁽V⁾, γ⁽V⁾; orthorhombic elastic constants c_ij or compliances s_ij; normal compliance Z_N.  
- **Geometric/log data**: borehole radius r_w, breakout width b and depth D_max, azimuth angles, formation dip φ, dip azimuth β0; seismic curvature K_c; density ρ, P‑wave velocity V_P0, S‑wave velocity V_S0.  
- **Ratio indicators**: DHSR = (σ_H‑σ_h)/σ_H; ODHSR for orthorhombic media.

## Reusable Claims
- Claim: Borehole breakout direction indicates the minimum horizontal principal stress direction, and drilling‑induced fractures indicate the maximum horizontal principal stress direction [Yin 2018, pp. 3-4]. Condition: Requires borehole imaging logs and assurance that breakouts are stress‑induced, not washouts or fracture‑related.  
- Claim: The vertical principal stress can be accurately calculated by integrating density logs: σ_v = ∫ ρ(h)·g·dh, where ρ(h) is depth‑varying density [Yin 2018, pp. 5, eq. 9]. Condition: Requires reliable density log over the depth interval; no tectonic uplift correction included.  
- Claim: The spring model (eq. 14‑15) predicts layer‑specific horizontal stresses in tectonically active regions if tectonic strains ε_h, ε_H are calibrated [Yin 2018, pp. 5-6]. Condition: Assumes isotropic uniaxial strain boundary conditions and static elastic parameters; not directly applicable to dipping strata.  
- Claim: Dynamic elastic moduli from sonic logs must be reduced to static equivalents using rock integrity factors before stress calculation [Yin 2018, pp. 5]. Condition: Requires laboratory‑measured dynamic‑static correlations for the target formation.  
- Claim: The differential horizontal stress ratio (DHSR) is a reservoir quality indicator: values approaching 0 correspond to isotropic horizontal stress, favouring complex fracture networks; high values promote planar fractures [Yin 2018, pp. 8-10]. Condition: DHSR definition depends on the assumed symmetry; for orthorhombic media, ODHSR (eq. 38‑42) is more appropriate.  
- Claim: ODHSR can be approximated by ξ ODHSR ≈ 2·V² S0·ρ·(2γ+1)·Z_N / [1 + 2·V² S0·ρ·(2γ+1)·Z_N], using inverted anisotropy and elastic parameters [Yin 2018, pp. 10, eq. 42]. Condition: Requires linear‑slip theory, small normal compliance, and azimuthal seismic inversion for γ and Z_N.

## Candidate Concepts
- [[in‑situ stress]]  
- [[shale gas reservoir]]  
- [[hydraulic fracturing]]  
- [[borehole breakout]]  
- [[induced tensile fractures]]  
- [[Kaiser effect]]  
- [[differential strain curve analysis]]  
- [[anelastic strain recovery]]  
- [[dynamic‑static elastic parameter conversion]]  
- [[spring model (geomechanics)]]  
- [[finite‑element stress simulation]]  
- [[boundary displacement adjustment]]  
- [[displacement back‑analysis]]  
- [[seismic curvature attribute]]  
- [[horizontal stress difference ratio (DHSR)]]  
- [[orthorhombic differential horizontal stress ratio (ODHSR)]]  
- [[azimuthal elastic impedance (AEI) inversion]]  
- [[HTI anisotropy parameters]]  
- [[VTI anisotropy parameters]]  
- [[orthorhombic medium]]  
- [[geomechanical model]]  
- [[fracture network indicator]]

## Candidate Methods
- [[hydraulic fracturing stress measurement]]  
- [[acoustic emission stress measurement]]  
- [[differential strain curve analysis (DSCA)]]  
- [[overcoring stress relief]]  
- [[borehole imaging log stress orientation]]  
- [[multi‑pole sonic log anisotropy analysis]]  
- [[density‑integration vertical stress]]  
- [[Kinnick / Matthewell‑Kelly horizontal stress formula]]  
- [[Huang model for horizontal stress]]  
- [[spring model for layered horizontal stress]]  
- [[dipping‑layer stress model]]  
- [[Ge Hongkui stratified stress formula]]  
- [[finite‑element boundary adjustment]]  
- [[displacement back‑analysis for initial stress]]  
- [[curvature‑based tectonic stress estimation]]  
- [[PP‑PS joint reflectivity inversion for dynamic parameters]]  
- [[anisotropic rock‑physics model for stress]]  
- [[azimuthal elastic impedance inversion for anisotropy]]  
- [[ODHSR seismic prediction method]]  
- [[VTI‑to‑HTI parameter conversion]]

## Connections To Other Work
This review builds upon and cites numerous foundational works:  
- Fairhurst (1964) and Haimson (1968) for hydraulic fracturing theory, extended by Haimson & Cornet (2003) for HTPF.  
- Anderson (1942) for fault‑stress regimes used in geological stress inference.  
- Suarez‑Rivera et al. (2009) for VTI stress equations adopted in rock‑physics‑based seismic prediction.  
- Gray (2011) for HTI stress estimation using seismic data, introducing DHSR.  
- Tsyvankin (1997) for orthorhombic anisotropic parameterization used in ODHSR derivation.  
- Sayers (2010) for geophysics under stress linking rock physics and geomechanics.  
- The azimuthal EI approach is rooted in Chen et al. (2014) and Li (2013) for fracture parameter inversion.  
- The work by Ma et al. (2017, 2018) directly extends stress prediction by combining azimuthal seismic data with orthorhombic media theory.  
- Zhang et al. (2015) proposed a shale rock‑physics equivalent model for VTI stress estimation.  
- He (2011) and Xiong et al. (2017) contributed curvature‑based tectonic stress calculation.  
- References 104–110 link this review to elastic impedance inversion, fluid identification, and rock‑physics modeling advances that underpin the seismic stress prediction framework.

## Open Questions
- How to accurately incorporate tectonic stress and pore‑pressure variations into seismic stress prediction formulas.  
- How to derive more precise stress‑prediction equations that account for complex geological factors while remaining computationally feasible.  
- How to effectively apply these theoretical methods in large‑scale real‑data cases and validate with production and micro‑seismic data.  
- The relationship between ODHSR and actual hydraulic fracture network complexity needs further field validation.  
- Integration of stress‑prediction results with other reservoir characterization parameters (brittleness, porosity, permeability) to optimize well placement and completion design [Yin 2018, pp. 12-13].

## Source Coverage
All 16 non‑empty indexed fragments (pages 1‑1 through 17‑17) were processed.  
- Number of indexed text blocks: 16  
- Number of non‑empty source blocks: 16  
- Compilation block count: 16  
- Total indexed characters: 77,614; total compiled characters: 73,183  
- Coverage ratio by blocks: 1.0  
- Coverage ratio by characters: 0.94291  
- Source signature: d9b743864adfd5895f79db39dceedb0851874485  
- Compilation strategy: single‑pass‑markdown  
- Coverage status: full‑index (all provided fragments incorporated).
