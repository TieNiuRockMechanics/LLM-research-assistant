---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-zheng-study-on-mechanical-characteristics-and-damage-model-of-layered-sandstone-after-high"
title: "Study on Mechanical Characteristics and Damage Model of Layered Sandstone after High Temperature Action."
status: "draft"
source_pdf: "data/papers/2023 - Study on mechanical characteristics and damage model of layered sandstone after high temperature action.pdf"
collections:
  - "part2"
  - "zotero new"
citation: "Zheng, Fu, et al. \"Study on Mechanical Characteristics and Damage Model of Layered Sandstone after High Temperature Action.\" *Case Studies in Construction Materials*, vol. 19, 2023, e02601, doi:10.1016/j.cscm.2023.e02601."
indexed_texts: "15"
indexed_chars: "74750"
nonempty_source_blocks: "15"
compiled_source_blocks: "15"
compiled_source_chars: "69680"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.932174"
coverage_status: "full-index"
source_signature: "cc572da704d4ce0ae8954ffa54ad924e4abbb780"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T07:12:56"
---

# Study on Mechanical Characteristics and Damage Model of Layered Sandstone after High Temperature Action.

## One-line Summary
This study conducts triaxial compression tests on layered sandstone after high-temperature treatment (20–800 °C) and establishes a statistical damage constitutive model coupling high-temperature, bedding, and load damage, validated against experimental stress-strain curves [Zheng 2023, pp. 1-2].

## Research Question
How do high temperatures (up to 800 °C) and bedding orientation jointly influence the mechanical properties, damage evolution, and failure modes of layered sandstone, and can a unified statistical damage constitutive model be formulated to capture these coupled effects? [Zheng 2023, pp. 1-5]

## Study Area / Data
- **Rock type**: Yellow quartz sandstone (99.96 % quartz) from a tunnel construction site in Sichuan province, China [Zheng 2023, pp. 4-5].
- **Specimen geometry**: Standard cylinders, 50 mm diameter × 100 mm length, prepared at bedding angles β = 0°, 30°, 45°, 60°, 90° [Zheng 2023, pp. 4-5].
- **Initial properties**: Average density 2.492 g/cm³, average longitudinal wave velocity 2176 m/s, dense structure without noticeable cracks [Zheng 2023, pp. 4-5].
- **Temperature levels**: 20 °C (reference), 200 °C, 400 °C, 600 °C, 800 °C; heating at 4 h dwell, natural cooling to 20 °C [Zheng 2023, pp. 5-7].
- **Mechanical testing**: Triaxial compression at 5 MPa confining pressure, axial displacement rate 0.12 mm/min [Zheng 2023, pp. 7].
- **Microstructural evidence**: SEM images at 20 °C, 400 °C, and 800 °C document progressive crystal deterioration, pore growth, and cavity formation [Zheng 2023, pp. 12-14].

## Methods
1. **High-temperature treatment** in a muffle furnace (SX2‑8‑10) followed by natural cooling [Zheng 2023, pp. 5-7].
2. **Triaxial compression tests** using RLW‑2000 multifunctional rock triaxial apparatus at σ₃ = 5 MPa [Zheng 2023, pp. 5-7].
3. **Determination of mechanical parameters**: peak strength (σₑ), peak strain (εₑ), elastic modulus (E), Poisson’s ratio (μ), damage threshold (σₐ, εₐ) from volume strain method [Zheng 2023, pp. 9-12].
4. **Definition of coupled damage variables**:  
   - Thermal damage `D_T = 1 − E_T/E₀` [Zheng 2023, pp. 14].
   - Bedding initial damage `D_J = 1 − E_J/E₀` [Zheng 2023, pp. 14].
   - Coupled temperature‑bedding damage `D_TJ = D_J + D_T − D_J D_T = 1 − (E_T E_J)/E₀²` [Zheng 2023, pp. 14-15].
5. **Load‑induced damage** based on Weibull distribution of micro‑element strength, with temperature‑dependent scale and shape parameters: `k_TJ = k₀(1 − D_TJ)`, `λ_TJ = λ₀(1 − D_TJ)` [Zheng 2023, pp. 14-16].
6. **Micro‑element strength criterion**: Drucker‑Prager (D‑P) criterion: `F* = α I* + √J₂*` [Zheng 2023, pp. 16-17].
7. **Total damage variable**: `D_t = 1 − (E_T E_J / E₀²) exp[−(F*/(λ₀(1−D_TJ)))^{k₀(1−D_TJ)}]` [Zheng 2023, pp. 16].
8. **Constitutive equation** (segmented at damage threshold):  
   - Pre‑damage threshold: quadratic `σ = m ε² + n ε` [Zheng 2023, pp. 17].  
   - Post‑damage threshold: `σ_i = ε_i (E_T E_J/E₀) exp[−(F*/(λ₀(1−D_TJ)))^{k₀(1−D_TJ)}] + μ_{JT}(σ_p + σ_q)` [Zheng 2023, pp. 17-18].
9. **Parameter determination**: k and λ solved from peak‑point conditions (∂σ/∂ε = 0 at peak); m and n from continuity and smoothness at damage threshold [Zheng 2023, pp. 17-18].
10. **Validation**: comparison of theoretical stress‑strain curves with experimental triaxial data for various dip angles and temperatures [Zheng 2023, pp. 19].

## Key Findings
1. **Strength anisotropy**: Peak strength (σₑ), elastic modulus, and damage threshold follow a “U”‑shaped trend with bedding angle, opening upward; minimum at 45° [Zheng 2023, pp. 8-10].  
2. **Temperature effect**: Above 200 °C, peak strength decreases significantly; between 200 °C and 400 °C the impact on peak strength is especially pronounced [Zheng 2023, pp. 8-9].  
3. **Ductility transition**: After 600 °C, sandstone exhibits obvious ductile characteristics; failure mode shifts from tensile to compressive‑shear with increasing temperature [Zheng 2023, pp. 12].  
4. **Critical bedding angle**: 60° dip angle specimens are prone to shear failure along the weak bedding plane, achieve peak stress quickly after damage threshold, and show low toughness [Zheng 2023, pp. 10-12].  
5. **Normalized damage threshold**: σₐ/σₑ always exceeds 80 %, indicating substantial deformation capacity before instability [Zheng 2023, pp. 10].  
6. **Wave velocity decay**: Longitudinal wave velocity decreases with increasing temperature; anisotropy in wave velocity diminishes above 600 °C [Zheng 2023, pp. 12-13].  
7. **Microstructural degradation**: SEM reveals compact structure at 20 °C, increased intergranular/transgranular cracks at 400 °C, and loose, porous structure with large cavities at 800 °C [Zheng 2023, pp. 12-14].  
8. **Model fidelity**: The proposed statistical damage constitutive model shows good agreement with experimental triaxial curves, capturing initial compaction, damage‑threshold transition, peak, and post‑peak behavior [Zheng 2023, pp. 19-21].  
9. **Parameter physical meaning**: Parameter k reflects ductility/brittleness (larger k = more brittle); parameter λ scales peak strength; m controls pre‑peak curvature [Zheng 2023, pp. 18-20].  
10. **Temperature‑range influence**: Anisotropy initially increases with temperature up to ~400 °C then decreases from 600 °C to 800 °C [Zheng 2023, pp. 9].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Peak strength vs. dip angle forms U‑shaped curve with minimum at 45° | [Zheng 2023, pp. 8-9] | Triaxial, 5 MPa confining pressure, 20–800 °C | Consistent across all temperatures |
| Peak strength decreases rapidly between 200 °C and 400 °C | [Zheng 2023, pp. 8-9] | Yellow sandstone, all dip angles | Thermal damage accelerates in this range |
| Elastic modulus decreases monotonically with temperature | [Zheng 2023, pp. 9] | 20–800 °C, all dip angles | Anisotropy peaks ~400 °C then declines |
| Damage threshold σₐ > 0.8 σₑ for all conditions | [Zheng 2023, pp. 10] | Triaxial loading | Indicates high deformation capacity |
| 60° dip angle yields sharp rise in normalized damage threshold and low toughness | [Zheng 2023, pp. 10-12] | All temperatures | Failure along weak bedding plane |
| Longitudinal wave velocity decreases with temperature; bedding‑angle differences shrink above 600 °C | [Zheng 2023, pp. 12-13] | Bedding‑parallel vs. inclined specimens | Physical properties converge at high T |
| SEM: 20 °C compact; 400 °C inter‑/transgranular cracks; 800 °C loose, large cavities | [Zheng 2023, pp. 12-14] | 20, 400, 800 °C | Qualitative microstructural evolution |
| Weibull‑D‑P constitutive model matches experimental stress‑strain curves | [Zheng 2023, pp. 19-21] | Various T and β, σ₃=5 MPa | Segmented at damage threshold |
| Parameter k controls post‑peak brittleness; λ scales strength | [Zheng 2023, pp. 18-20] | 400 °C, varying β; β=45°, varying T | Physically interpretable |
| 30° dip angle rocks show larger k and faster post‑peak stress drop (lower ductility) | [Zheng 2023, pp. 18] | 400 °C treatment | Anisotropic ductility |

## Limitations
- Only one confining pressure (5 MPa) was used; the model’s performance under different σ₃ is not validated in this study [Zheng 2023, pp. 7].
- The model is calibrated for yellow quartz sandstone; applicability to other lithologies (e.g., shale, granite) is not confirmed [Zheng 2023, pp. 4-5].
- The Weibull parameters are assumed to follow simple linear degradation with (1−D_TJ); more complex thermal‑damage evolution laws are not explored [Zheng 2023, pp. 14-16].
- Damage threshold determined from volume strain method; alternative damage initiation criteria not compared [Zheng 2023, pp. 10].
- The model adopts a piecewise quadratic‑exponential form; the quadratic segment is empirical and fitted to each test, limiting predictive generality [Zheng 2023, pp. 17-18].

## Assumptions / Conditions
- The rock is treated as a continuous medium with micro‑elements whose strength follows a Weibull distribution [Zheng 2023, pp. 14-16].
- Thermal damage and bedding damage are isotropic in their influence on the elastic modulus; coupling is expressed through a simple product form [Zheng 2023, pp. 14-15].
- The D‑P criterion is valid for the micro‑element strength under triaxial compression [Zheng 2023, pp. 16-17].
- The damage threshold marks the transition from stable crack growth to unstable propagation, and the stress‑strain curve is smooth at this point [Zheng 2023, pp. 10, 17-18].
- Poisson’s ratio μ_JT is treated as a known input from experiments and held constant during the post‑damage stage [Zheng 2023, pp. 17].
- The model does not include time‑dependent or creep effects; loading is quasi‑static [Zheng 2023, pp. 7].

## Key Variables / Parameters
- **T**: Temperature (20, 200, 400, 600, 800 °C) [Zheng 2023, pp. 7].
- **β**: Bedding dip angle (0°, 30°, 45°, 60°, 90°) [Zheng 2023, pp. 4-5].
- **σ₃**: Confining pressure (constant 5 MPa) [Zheng 2023, pp. 7].
- **σₑ, εₑ**: Peak stress and corresponding strain [Zheng 2023, pp. 8].
- **σₐ, εₐ**: Damage threshold stress and strain (from volume strain inflection) [Zheng 2023, pp. 10].
- **E₀, E_T, E_J**: Elastic moduli at 20 °C (intact), after temperature T, and for bedding angle J [Zheng 2023, pp. 14].
- **μ, μ_JT**: Poisson’s ratios [Zheng 2023, pp. 17].
- **D_T, D_J, D_TJ, D_t**: Thermal, bedding, coupled, and total damage variables [Zheng 2023, pp. 14-16].
- **k, λ**: Weibull shape and scale parameters (k_TJ, λ_TJ for heated layered rock) [Zheng 2023, pp. 15-17].
- **α, φ**: D‑P criterion parameters related to internal friction angle [Zheng 2023, pp. 16-17].
- **m, n**: Quadratic fitting coefficients for pre‑damage threshold segment [Zheng 2023, pp. 17-18].

## Reusable Claims
1. **Claim**: For layered sandstone under triaxial compression, peak strength, elastic modulus, and damage threshold follow a U‑shaped trend with bedding angle, minimum at 45°, under temperatures from 20 °C to 800 °C [Zheng 2023, pp. 8-10].  
   *Condition*: 5 MPa confining pressure, yellow quartz sandstone, cylindrical specimens.  
   *Limitation*: Confirmed only for the tested lithology and geometry.

2. **Claim**: The temperature interval 200–400 °C causes the most rapid decrease in peak strength of layered sandstone [Zheng 2023, pp. 8-9].  
   *Condition*: Heated for 4 h, naturally cooled, tested at 5 MPa confining pressure.

3. **Claim**: The damage threshold of layered sandstone always exceeds 80 % of peak stress, indicating significant post‑damage initiation load‑bearing capacity [Zheng 2023, pp. 10].  
   *Condition*: Observed under triaxial compression at 5 MPa.

4. **Claim**: A bedding dip angle of 60° promotes shear failure along weak bedding planes and results in low toughness (rapid post‑peak strength loss) [Zheng 2023, pp. 10-12].  
   *Condition*: Validated for yellow sandstone up to 800 °C.

5. **Claim**: The proposed Weibull‑D‑P statistical damage constitutive model can reproduce the full stress‑strain curve of high‑temperature‑treated layered sandstone when segmented at the damage threshold [Zheng 2023, pp. 19-21].  
   *Condition*: Requires experimental determination of E, μ, peak values, and damage threshold for calibration.

6. **Claim**: The Weibull parameter k controls post‑peak brittleness/ductility, and λ scales the peak strength; both show systematic variation with temperature and bedding angle [Zheng 2023, pp. 18-20].  
   *Condition*: Under the assumption that micro‑element strength follows D‑P criterion and Weibull distribution.

## Candidate Concepts
- [[layered rock]]  
- [[thermal damage]]  
- [[bedding damage]]  
- [[coupled damage variable]]  
- [[Weibull distribution]]  
- [[Drucker-Prager criterion]]  
- [[statistical damage constitutive model]]  
- [[anisotropic rock mechanics]]  
- [[damage threshold]]  
- [[normalized damage threshold]]  
- [[longitudinal wave velocity damage indicator]]  
- [[ductile-brittle transition in rock]]  
- [[shear failure along bedding plane]]  
- [[segmented constitutive model]]  
- [[rock microelement strength]]

## Candidate Methods
- [[high-temperature triaxial compression test on layered rock]]  
- [[volume strain method for damage threshold]]  
- [[Weibull-based statistical damage mechanics]]  
- [[D-P yield criterion for microelements]]  
- [[piecewise constitutive fitting (quadratic + exponential)]]  
- [[elastic modulus-based thermal damage definition]]  
- [[coupled temperature-bedding-load damage variable construction]]  
- [[SEM microstructural characterization of heated rock]]  
- [[longitudinal wave velocity measurement for damage assessment]]  
- [[peak-point derivative method for Weibull parameter determination]]

## Connections To Other Work
- **Thermal damage on rock properties**: Aligns with findings that increasing temperature reduces wave velocity, increases porosity, and decreases strength (Chaki et al., 2008; Yang et al., 2017; Zhang et al., 2018) [Zheng 2023, pp. 2].
- **Bedding anisotropy**: Consistent with previous studies showing strength and deformation anisotropy in layered rocks (Zhou et al., 2016; Heng et al., 2015; Nasseri et al., 2003) [Zheng 2023, pp. 2].
- **Statistical damage models**: Extends the Weibull-based rock damage framework (Krajcinovi, 1982; Deng et al., 2011; Wang et al., 2007) by incorporating coupled thermal and bedding damage [Zheng 2023, pp. 2-5].
- **Coupled damage models**: Builds on Zhang et al. (2022) damage model for layered rock masses and Jiang et al. (2021) high‑temperature rock model, adding simultaneous temperature–bedding–load coupling [Zheng 2023, pp. 3-5].
- **D‑P criterion for micro‑elements**: Adopts the approach of previous researchers who used D‑P or Mohr‑Coulomb criteria to define micro‑element strength in damage models [Zheng 2023, pp. 16-17].
- **Tunnel fire and deep engineering context**: References the effects of tunnel fires on rock behavior (Wasantha et al., 2021) and the need for high‑temperature rock models in deep underground engineering [Zheng 2023, pp. 1-2].

## Open Questions
- How does the model perform under different confining pressures (not only 5 MPa) and loading paths? [not confirmed in fragments]
- Can the constitutive model be extended to include time‑dependent effects (creep, relaxation) at high temperature? [not confirmed in fragments]
- What is the quantitative link between SEM‑observed micro‑crack density and the Weibull parameters? [not confirmed in fragments]
- Is the assumed simple linear degradation of Weibull parameters with (1−D_TJ) valid over a wider temperature range or for cyclic thermal loading? [not confirmed in fragments]
- How does the model adapt to fluid‑saturated conditions, which are common in deep reservoirs? [not confirmed in fragments]
- Can the damage threshold‑based segmentation be generalized to a continuous constitutive formulation without a distinct inflection point? [not confirmed in fragments]

## Source Coverage
All indexed fragments (15 source blocks; total 74,750 characters indexed; 69,680 compiled characters) were processed in a single pass. Coverage ratio by blocks = 1.0; by characters ≈ 0.932. The compiled page retains factual claims only from the provided index [Zheng 2023, pp. 1-23].
