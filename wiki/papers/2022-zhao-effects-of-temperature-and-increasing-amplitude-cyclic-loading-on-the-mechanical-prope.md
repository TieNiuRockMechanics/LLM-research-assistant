---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-zhao-effects-of-temperature-and-increasing-amplitude-cyclic-loading-on-the-mechanical-prope"
title: "Effects of Temperature and Increasing Amplitude Cyclic Loading on the Mechanical Properties and Energy Characteristics of Granite."
status: "draft"
source_pdf: "data/papers/2022 - Effects of temperature and increasing amplitude cyclic loading on the mechanical properties and energy characteristics of granite.pdf"
collections:
  - "靳一作以外的"
citation: "Zhao, Guokai, et al. \"Effects of Temperature and Increasing Amplitude Cyclic Loading on the Mechanical Properties and Energy Characteristics of Granite.\" *Bulletin of Engineering Geology and the Environment*, vol. 81, 2022. DOI: 10.1007/s10064-022-02655-6."
indexed_texts: "11"
indexed_chars: "52580"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "52061"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.990129"
coverage_status: "full-index"
source_signature: "c9282ad26c25f9af6cba05f4a82263044970e585"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T05:17:05"
---

# Effects of Temperature and Increasing Amplitude Cyclic Loading on the Mechanical Properties and Energy Characteristics of Granite.

## One-line Summary
This study experimentally investigates how temperature (25–600 °C) and multi-level increasing amplitude cyclic loading alter the mechanical properties, hardening behavior, and energy evolution of granite, finding that mild temperature and cyclic loading strengthen the rock, and that an approximately linear energy storage law exists between input and elastic energy densities, independent of temperature and stress history.

## Research Question
The paper examines the combined effects of temperature and increasing amplitude cyclic loading (multi-level single cyclic loading, MLSCL) on the mechanical properties (strength, deformation, elastic modulus) and energy characteristics (input, elastic, and dissipated energy densities) of granite. It also aims to clarify the rock‑hardening mechanism and to establish a mathematical relationship between elastic and input energy densities under these conditions. [Zhao 2022, pp. 1-2]

## Study Area / Data
- Rock type: Weakly altered granodiorite, light gray, semi‑self‑shaped medium‑grained granular structure, mineral particle size ~2–5 mm. [Zhao 2022, pp. 2-3]
- Mineral composition: K‑feldspar 40–45 %, plagioclase 30–35 %, quartz 20–25 %, biotite 3–5 %. [Zhao 2022, pp. 2-3]
- Source location: Outcrop in Zhumadian City, Henan province, China. [Zhao 2022, pp. 2-3]
- Specimen geometry: Cylindrical, diameter 30 mm, length 60 mm, cored from the same block, macroscopically homogeneous, no visible flaws. [Zhao 2022, pp. 2-3]
- Sample preparation: Air‑dried for 7 days (natural moisture content); non‑parallelism of ends < 0.02 mm. [Zhao 2022, pp. 3-5]
- Average P‑wave velocity: 4.418 km/s. [Zhao 2022, pp. 3-5]
- Number of samples: 21. [Zhao 2022, pp. 3-5]
- Uniaxial compressive strength (UCS) reference values (σc(T)):
  - 25 °C: 144.75 MPa
  - 100 °C: 129.54 MPa
  - 200 °C: 110.21 MPa
  - 300 °C: 114.10 MPa
  - 400 °C: 116.52 MPa
  - 500 °C: 105.19 MPa
  - 600 °C: 105.12 MPa
  [Zhao 2022, pp. 3-5]

## Methods
- **Testing system**: Multi‑functional rock high‑temperature triaxial testing machine; total stiffness 4 × 10⁹ N/m, maximum axial load 1 000 kN, maximum heating temperature 650 °C. [Zhao 2022, pp. 3-5]
- **Heating protocol**: Heated to target temperature at 2 °C/min, held for 2 h to ensure uniform heating. [Zhao 2022, pp. 3-5]
- **Loading path**: Multi‑level single cyclic loading (MLSCL). Five unloading stress levels *i* = σᵢ / σc(T): 0.4, 0.6, 0.7, 0.8, 0.9. In each cycle, sample loaded to the upper limit stress at 0.1 kN/s and then unloaded to zero at the same rate. The sequence: 0 → 0.4σc → 0 → 0.6σc → 0 → 0.7σc → … → failure. [Zhao 2022, pp. 3-5]
- **Test temperatures**: 25 °C, 100 °C, 200 °C, 300 °C, 400 °C, 500 °C, 600 °C. [Zhao 2022, pp. 3-5]
- **Elastic modulus calculation**: For each stress level, the modulus is computed from the linear portion of the loading curve. [Zhao 2022, pp. 5-7]
- **Energy density calculation** (graphical integration):
  - Input energy density: \( u = \int_{0}^{\varepsilon_2} f_1(\varepsilon) d\varepsilon \)
  - Elastic energy density: \( u_e = \int_{\varepsilon_1}^{\varepsilon_2} f_2(\varepsilon) d\varepsilon \)
  - Dissipated energy density: \( u_d = u - u_e \)  
  where ε₁ is residual strain after unloading, ε₂ is max strain of the loading curve, and f₁(ε), f₂(ε) are the loading and unloading curve functions, respectively. [Zhao 2022, pp. 7-8]
- **Energy-based indices referenced**:
  - Peak strain energy storage index: \( W_{P\text{et}} = U_e / U_d \) [Zhao 2022, pp. 10-11]
  - Brittleness index: \( BI = (\Delta U_e + W + U_d) / (\Delta U_e + U_d) \) [Zhao 2022, pp. 10-11]

## Key Findings
1.  **Rock hardening, not weakening**: Under mild temperatures (100–500 °C) and MLSCL, the granite samples are strengthened rather than weakened. The elastic modulus increases with stress level in an approximately logarithmic relationship, while the relative residual strain generally decreases. [Zhao 2022, pp. 10-10]
2.  **Three hardening mechanisms**: The hardening is attributed to (i) closure of temperature‑induced and original cracks under compression, (ii) increased friction between crack surfaces that does not fully recover on unloading, making the internal structure more compact, and (iii) crack‑closure‑dominated pre‑peak deformation, which expands the yield locus in the strain‑hardening regime. Time‑dependent cracking within the experimental time frame (max ~8.9 h at 600 °C) is considered negligible. [Zhao 2022, pp. 10-10]
3.  **Energy evolution transition**: With increasing temperature, the energy evolution transforms from nonlinear to nearly linear. At 25 °C and 100 °C, input energy density *u* and elastic energy density *uₑ* increase nonlinearly with stress level (approximately exponential). From 200 °C to 600 °C, *u* and *uₑ* increase almost linearly when the unloading stress level is < 0.9. [Zhao 2022, pp. 7-8]
4.  **Linear energy storage law**: A strong linear correlation exists between *uₑ* and *u* across all tested temperatures, following \( u_e = a \cdot u + b \), with R² = 0.996–0.999. The slope *a* is nearly constant (coefficient of variation = 0.02), indicating that the relationship is independent of temperature and stress history (for the tested post‑compaction stages). [Zhao 2022, pp. 8-10]
5.  **Deformation “memory” effect**: The outer envelope of each unloading–reloading curve is similar to a conventional uniaxial compression curve, and the loading curve continues the upward trend of the previous cycle; thus, the deformation has a “memory” effect and is little influenced by the loading history (temperature and stress). [Zhao 2022, pp. 5-7]
6.  **Critical temperature 500–600 °C**: At 600 °C the stress–strain curves are more sparse, maximum strains are larger, and plastic deformation is enhanced; there is no sharp increase of *u* at the last compression failure. This coincides with the α‑to‑β quartz transition at ~573 °C. [Zhao 2022, pp. 7-8]
7.  **Energy distribution**: At all temperatures, the proportion of dissipated energy to input energy (*u_d/u*) is highest in the first cycle (19–35 %), then decreases and tends to stabilize. In the pre‑peak cyclic loading process, energy accumulation (uₑ) is dominant. [Zhao 2022, pp. 8-10]
8.  **Accurate peak elastic energy calculation**: The linear energy storage law provides a new, more accurate method for calculating the elastic energy at peak stress, avoiding errors from the conventional assumption of equal loading–unloading moduli. This is critical for energy‑based brittleness indices used in reservoir stability and compressibility evaluation. [Zhao 2022, pp. 10-11]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Elastic modulus decreases with increasing temperature; increases with stress level in an approximately logarithmic relationship (hardening). | [Zhao 2022, pp. 5-7] | Granite, MLSCL, 25–600 °C, stress levels *i* = 0.4–0.9. | Maximum modulus at 25 °C; minimum at 600 °C. |
| Maximum strain increases approximately linearly with stress level when *i* < 0.9. | [Zhao 2022, pp. 5-7] | Granite, MLSCL, 25–600 °C. | Rapid increase only near failure. |
| Relative residual strain generally decreases with stress level; development is reduced by temperature and cyclic loading. | [Zhao 2022, pp. 7-8] | Granite, MLSCL; 25–200 °C and 300–500 °C behave slightly differently; 600 °C shows a sharp increase near failure. | Largest cumulative residual strain occurs at 600 °C. |
| *u* and *uₑ* increase nonlinearly (approximately exponential) with stress level at 25 °C and 100 °C; increase almost linearly at 200–600 °C when *i* < 0.9. | [Zhao 2022, pp. 7-8] | Granite, MLSCL. | Indicates a transformation from nonlinear to linear energy evolution with rising temperature. |
| *u_d/u* ratio is highest in the first cycle (19.36–34.82 %), then decreases and stabilizes; energy accumulation (*uₑ/u*) is dominant in pre‑peak cycling. | [Zhao 2022, pp. 8-10] | Granite, MLSCL, all seven temperatures. | Temperature has little effect on the distribution mode (proportion). |
| Linear relationship \( u_e = a \cdot u + b \): slope *a* = 0.908–0.940 (mean ~0.91, CV ≈ 0.02), R² = 0.996–0.999. | [Zhao 2022, pp. 8-10] [Zhao 2022, pp. 10-11] | Granite, MLSCL, 25–600 °C, stress levels excluding compaction stage. | Slope *a* is a material constant; the law is independent of temperature and loading history (within tested range). |
| Peak strain energy storage index WP et = 10.44–12.67 across 25–600 °C. | [Zhao 2022, pp. 11-12] | Granite, calculated via Eq. (6) using the linear energy storage law. | Indicates that brittleness remains strong at high temperatures for this granite. |

## Limitations
- No stress level was set within the initial compaction stage; therefore, the linear energy storage law was verified only for the quasi‑elastic, elastic, and yield stages. [Zhao 2022, pp. 8-10]
- The stress‑controlled loading mode prevented acquisition of the post‑peak stress–strain curve, so the full brittleness index (Eq. 7) could not be quantitatively calculated. [Zhao 2022, pp. 11-12]
- The time‑dependent cracking within the experimental timeframe (max ~8.9 h) was assumed negligible, but this assumption was not experimentally isolated. [Zhao 2022, pp. 10-10]
- The specific critical temperature for the transition from nonlinear to linear energy evolution, identified here as between 100 and 200 °C, requires further study for precise determination. [Zhao 2022, pp. 7-8]
- The generalized equation for the linear energy storage law across different rock types under MLSCL at high temperatures still needs to be defined. [Zhao 2022, pp. 8-10]

## Assumptions / Conditions
- The UCS values used to set stress levels were taken from a prior study on the same rock at high temperature (Zhao et al. 2019a). [Zhao 2022, pp. 3-5]
- Each increment of MLSCL is treated as a separate test for elastic modulus calculation. [Zhao 2022, pp. 5-7]
- The conventional assumption that the elastic modulus during loading and unloading is equal was stated to cause errors in peak elastic energy calculation; this study’s linear law avoids that assumption. [Zhao 2022, pp. 10-11]
- The four types of micro‑cracks (stress‑induced, temperature‑induced, cyclic fatigue, time‑dependent) are acknowledged, but their individual contributions are considered impossible to completely distinguish under the experimental conditions. [Zhao 2022, pp. 10-10]
- It is assumed that thermal cracking in granite between 100 and 500 °C is mainly due to anisotropy and mismatch of thermal expansion of minerals and loss of water, and does not cause structural damage. [Zhao 2022, pp. 10-10]

## Key Variables / Parameters
- Temperature (*T*): 25, 100, 200, 300, 400, 500, 600 °C
- Unloading stress level (*i* = σᵢ / σc(T)): 0.4, 0.6, 0.7, 0.8, 0.9
- Uniaxial compressive strength at temperature (σc(T)): see table in section “Study Area / Data”
- Elastic modulus (*E*)
- Maximum strain (*ε_max*)
- Cumulative residual strain and relative residual strain
- Input energy density (*u*), elastic energy density (*uₑ*), dissipated energy density (*u_d*)
- Ratio *u_d/u* (energy dissipation proportion)
- Linear energy storage law slope (*a*) and intercept (*b*)
- Peak strain energy storage index (WP et = Uₑ / U_d)

## Reusable Claims
1.  **CLAIM**: Under mild temperatures (100–500 °C) and multi‑level increasing amplitude cyclic loading, granite exhibits rock hardening: the elastic modulus increases with stress level in an approximately logarithmic relationship, and relative residual strain generally decreases. **CONDITION**: Granite subjected to MLSCL at stress levels 0.4–0.9, heated at 2 °C/min with a 2 h hold. **LIMITATION**: True only for the tested granite; the presence of a compaction stage at lower stress levels was not included in the modulus trend. [Zhao 2022, pp. 5-7] [Zhao 2022, pp. 7-8] [Zhao 2022, pp. 10-10]
2.  **CLAIM**: The relationship between elastic energy density (*uₑ*) and input energy density (*u*) during MLSCL is strongly linear (R² > 0.99) and the slope (*a*) is a material constant (CV ≈ 0.02) independent of temperature (25–600 °C) and stress history. **CONDITION**: Granite, post‑compaction stages (quasi‑elastic, elastic, yield). **LIMITATION**: Verification for the compaction stage and for a generalized rock set is lacking. [Zhao 2022, pp. 8-10] [Zhao 2022, pp. 8-10]
3.  **CLAIM**: The energy evolution pattern of granite changes from nonlinear (exponential‑like increase of *u* and *uₑ* with stress level at ≤ 100 °C) to linear behavior (at ~200–600 °C). **CONDITION**: MLSCL, stress levels < 0.9. **LIMITATION**: The exact critical temperature between 100 and 200 °C requires further study. [Zhao 2022, pp. 7-8]
4.  **CLAIM**: In granite subjected to MLSCL, the dissipated energy proportion *u_d/u* is largest in the first loading cycle and then decreases and stabilizes; pre‑peak energy accumulation (*uₑ*) is dominant and the distribution mode is little affected by temperature. **CONDITION**: Granite, 25–600 °C, MLSCL. **LIMITATION**: Confirmed only for the tested granite and stress path. [Zhao 2022, pp. 8-10]
5.  **CLAIM**: The linear energy storage law allows a more accurate calculation of elastic energy at peak stress, avoiding the error from assuming equal loading and unloading moduli. **CONDITION**: Applicable in energy‑based brittleness and rockburst evaluations where *Uₑ* must be determined from pre‑peak cycles. **LIMITATION**: Requires knowledge of the linear law parameters for the specific rock. [Zhao 2022, pp. 10-11]

## Candidate Concepts
- [[rock hardening]]
- [[deformation memory effect]]
- [[multi-level single cyclic loading (MLSCL)]]
- [[linear energy storage law]]
- [[energy evolution transition (nonlinear to linear)]]
- [[energy distribution mode]]
- [[peak strain energy storage index]]
- [[brittleness index]]
- [[complex stress path]]
- [[crack closure and frictional strengthening]]
- [[critical temperature (granite, 500–600 °C)]]
- [[α–β quartz transition (573 °C)]]

## Candidate Methods
- [[MLSCL test (granite, high temperature)]]
- [[graphical integration method for energy density]]
- [[elastic modulus calculation from linear loading portion]]
- [[linear energy storage law fitting (u_e vs. u)]]
- [[energetics-based peak elastic energy calculation (avoiding equal-modulus assumption)]]
- [[residual strain analysis (accumulative and relative)]]

## Connections To Other Work
- **Gong et al. (2019b)**: This study’s linear energy storage law extends Gong et al.’s concept by demonstrating its independence from temperature and stress level for granite under MLSCL. [Zhao 2022, pp. 8-10] [Zhao 2022, pp. 11-12]
- **Zhao et al. (2019a)**: UCS values and the observation of rock hardening under constant‑amplitude cyclic loading at 100–500 °C are directly used and corroborated here. [Zhao 2022, pp. 2-3] [Zhao 2022, pp. 3-5]
- **Wong et al. (2020)**: The finding that mild temperature can strengthen rather than weaken rock is consistent with Wong et al.’s review on rock strengthening/weakening upon heating. [Zhao 2022, pp. 10-10]
- **Zhang et al. (2016)**: The α–β quartz phase transition at ~573 °C (cited) explains the critical change in behavior observed at 600 °C. [Zhao 2022, pp. 7-8]
- **Fatigue hydraulic fracturing (Zang et al. 2013, 2017; Zhuang et al. 2019)**: The hardening phenomenon under stepped‑amplitude cyclic loading is relevant to the concept of fatigue hydraulic fracturing in EGS, where higher fracturing pressures may be required if rock is strengthened by the loading path. [Zhao 2022, pp. 10-11]
- **Xia et al. (2015)**: The classification of rocks into damaged and hardened samples under cyclic temperature and stress is noted as context for the observed hardening. [Zhao 2022, pp. 2-3]

## Open Questions
- What is the exact critical temperature for the nonlinear‑to‑linear energy evolution transition (currently between 100 and 200 °C)? [Zhao 2022, pp. 7-8]
- Does the linear energy storage law hold for the missing compaction stage of MLSCL? [Zhao 2022, pp. 8-10]
- Can a generalized equation for the linear energy storage law be established for different rock types at high temperatures? [Zhao 2022, pp. 8-10] [Zhao 2022, pp. 11-12]
- How does the observed strengthening behavior affect the required injection pressure in fatigue hydraulic fracturing, and how should the balance between fracturing efficiency and induced seismicity risk be managed? [Zhao 2022, pp. 10-11]
- What is the separate contribution of stress‑induced, temperature‑induced, and cyclic fatigue micro‑cracks to the net hardening effect? [Zhao 2022, pp. 10-10]
- Is the material‑constant nature of the linear energy storage slope *a* truly universal across all granites, or is it sensitive to mineralogy and grain size? [Not confirmed in source; derived from the finding that slope is constant for this granite.]

## Source Coverage
All non‑empty indexed fragments from `data/papers/2022 - Effects of temperature and increasing amplitude cyclic loading on the mechanical properties and energy characteristics of granite.pdf` were processed in this compilation.  
**Coverage metrics**: 11 out of 11 source blocks compiled; compiled source characters 52 061 out of 52 580 (≈99.0 %).  
[Zhao 2022, pp. 1-13]
