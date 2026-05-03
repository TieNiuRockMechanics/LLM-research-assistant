---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2024-xi-evaluation-of-pore-characteristics-evolution-and-damage-mechanism-of-granite-under-therm"
title: "Evaluation of Pore Characteristics Evolution and Damage Mechanism of Granite under Thermal-Cooling Cycle Based on Nuclear Magnetic Resonance Technology."
status: "draft"
source_pdf: "data/papers/2024 - Evaluation of pore characteristics evolution and damage mechanism of granite under thermal-cooling cycle based on nuclear magnetic resonance technology.pdf"
collections:
  - "zotero new"
citation: "Xi, Yan, et al. \"Evaluation of Pore Characteristics Evolution and Damage Mechanism of Granite under Thermal-Cooling Cycle Based on Nuclear Magnetic Resonance Technology.\" *Geoenergy Science and Engineering*, vol. 241, 2024, 213101. doi:10.1016/j.geoen.2024.213101. Accessed 2026."
indexed_texts: "21"
indexed_chars: "104336"
nonempty_source_blocks: "21"
compiled_source_blocks: "21"
compiled_source_chars: "98108"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.940308"
coverage_status: "full-index"
source_signature: "2f59e9aee2256ee77fedd7d2efd2e6d6f2c88bc3"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T07:23:11"
---

# Evaluation of Pore Characteristics Evolution and Damage Mechanism of Granite under Thermal-Cooling Cycle Based on Nuclear Magnetic Resonance Technology.

## One-line Summary
This study experimentally quantifies pore size, distribution, and mechanical degradation of granite under natural, water, and liquid nitrogen cooling across 1 to 12 thermal cycles (heating to 500 °C) using low-field NMR, and establishes a quantitative relationship between T₂ spectrum damage, porosity damage, and compressive strength damage to reveal the rock deterioration mechanism for hot dry rock (HDR) engineering. [Xi 2024, pp. 1-2, 3-3, 19-20]

## Research Question
How do pore characteristics (number, size, distribution) and mechanical properties of HDR granite evolve under different cooling methods (natural, water, LN₂) and varying numbers of thermal-cooling cycles, and can a quantitative relationship be established between NMR-based pore damage and mechanical degradation to predict rock damage non-destructively? [Xi 2024, pp. 2-3, 14-15, 19-20]

## Study Area / Data
- **Rock type:** Fine granite from Yueyang City, Hunan Province, China; mineral composition (XRD): quartz 28.2%, potassium feldspar 27.4%, mica 22.2%, plagioclase feldspar 17.3%, clay minerals 4.9%. [Xi 2024, pp. 3-3]
- **Sample geometry:** Disk samples (diameter 50 mm, height 25 mm) for T₂ spectrum and pore size distribution; cylindrical samples (diameter 50 mm, height 100 mm) for NMR imaging and uniaxial compression. [Xi 2024, pp. 3-3]
- **Thermal treatment:** Heating to 500 °C at 5 °C/min, held 150 min, then cooled by natural air, immersion in water, or immersion in LN₂ for 120 min; cycling numbers: 1, 2, 4, 8, 12. [Xi 2024, pp. 3-3]
- **Control group:** Room-temperature samples without any thermal cycle, subjected to same NMR and uniaxial tests. [Xi 2024, pp. 3-3]

## Methods
- **NMR measurements:** Low-field NMR used to measure T₂ spectra and porosity after vacuum-saturation (2 h vacuum, then 20 MPa water pressure for 24 h). Pore size distribution inverted from T₂ using surface relaxation model: 1/T₂ = ρ₂ (S/V), and T₂ = C r, with C as conversion coefficient. [Xi 2024, pp. 3-5]
- **Pore classification:** Micropores (r ≤ 0.1 μm), mesopores (0.1 < r ≤ 1 μm), macropores (r > 1 μm) following Hodot and Li et al. standards. [Xi 2024, pp. 10-10]
- **Surface morphology:** LCD digital microscope (1080FHD, 300× magnification) to observe crack development. [Xi 2024, pp. 5-6]
- **NMR imaging (NMRI):** Proton density-weighted images of horizontal cross-sections; pixel value distribution analysis to quantify damage area ratio. [Xi 2024, pp. 17-19]
- **Mechanical testing:** Uniaxial compression to obtain compressive strength; damage factor D_n defined via statistical rock strength distribution. [Xi 2024, pp. 14-15]
- **Damage variable calculation:**
  - T₂ spectral area damage: D_Area = (aA_{n,mic}+bA_{n,mes}+cA_{n,mac})/(aA_{0,mic}+bA_{0,mes}+cA_{0,mac}) − 1, with weights a,b,c derived from coefficient of variation of spectral peak areas. [Xi 2024, pp. 13-14]
  - Porosity-based damage: D_P = (P_n−P_0)/(1−P_0). [Xi 2024, pp. 14-14]
  - Damage area ratio from NMRI pixel counting: Δ(n,β) = Σ x_i, and ratio relative to initial state. [Xi 2024, pp. 19-20]
- **Fitting:** Porosity evolution fitted by P_n = a + b·e^{c·n} (R²≥0.96). [Xi 2024, pp. 10-10]

## Key Findings
1. **Porosity evolution:** Porosity increased with thermal cycles in three stages: rapid growth (0–2 cycles, average increase 133.33%), slow growth (2–6 cycles, 11.58%), stabilization (6–12 cycles). At same cycle number, porosity under water cooling > LN₂ cooling > natural cooling. [Xi 2024, pp. 10-10, 20-22]
2. **T₂ spectrum shifts:** With increasing cycles, T₂ peak value increased and T₂max (maximum relaxation time) moved rightward, indicating pore enlargement. After 12 cycles, peak increases: 50.43% (natural), 106.44% (water), 53.96% (LN₂); T₂max increases: 86.79%, 248.91%, 225.51% respectively. The bimodal T₂ distribution gradually changed to trimodal, reflecting micropore-to-macropore conversion and improved connectivity. [Xi 2024, pp. 6-7]
3. **Pore content changes:** Macropores grew the fastest and dominated porosity increase. The proportion of macropores rose (e.g., natural: 54.18%→65.48% after 4 cycles), while micropores and mesopores decreased relatively. LN₂ cooling primarily promoted macropore development, whereas natural cooling enhanced micropores. [Xi 2024, pp. 10-13]
4. **Damage quantification:**
   - T₂ spectral area damage D_Area increased exponentially with cycles, with large pores having the most significant weight (c ≈ 0.56–0.62). After 12 cycles, D_Area: 2.20 (natural), 4.56 (water), 2.91 (LN₂). [Xi 2024, pp. 13-14, 20-22]
   - Porosity damage D_P followed a similar rapid-then-slow trend. [Xi 2024, pp. 14-14]
   - Compressive strength decreased linearly with porosity (R² = 0.87–0.91). Water cooling caused the greatest strength loss (from 164.66 MPa to 40.92 MPa after 12 cycles). [Xi 2024, pp. 15-17]
   - A positive proportional linear relationship between pore damage factor (D_P) and mechanical degradation coefficient (D_n) was established: D_n = k·P_n + const, with coefficients varying by cooling method. [Xi 2024, pp. 15-17]
5. **NMRI and damage mechanism:** Proton density images showed pixel clusters darkening, merging, and forming connected regions as cycles increased, indicating pore aggregation and microcrack network formation. Pixel value probability density curves shifted rightwards (toward higher proton density) and peak values decreased. The damage area ratio (from NMRI) increased, with LN₂ cooling causing more load-bearing area reduction than natural cooling despite similar porosity. [Xi 2024, pp. 17-20]
6. **Cooling method comparison:** Water cooling caused the most severe damage due to efficient convective heat transfer and thermal shock; LN₂ cooling was intermediate because a vapor cushion (Leidenfrost effect) reduces heat transfer; natural cooling was the mildest. [Xi 2024, pp. 10-10, 17-18]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Porosity increase rates: 0–2 cycles avg. +133.33%, 2–6 cycles +11.58%, stable 6–12 cycles | [Xi 2024, pp. 10-10] | Heating 500 °C, natural/water/LN₂ cooling | Three stages consistent across cooling methods |
| T₂ peak amplitude after 12 cycles: natural +50.43%, water +106.44%, LN₂ +53.96% | [Xi 2024, pp. 6-7] | 500 °C, 12 cycles | Water cooling nearly doubles T₂ peak vs. natural |
| T₂max increase after 12 cycles: natural +86.79%, water +248.91%, LN₂ +225.51% | [Xi 2024, pp. 7-8] | 500 °C, 12 cycles | Indicates maximum pore size growth |
| Compressive strength after 12 cycles: 80.72 MPa (natural), 40.92 MPa (water), 71.43 MPa (LN₂), from initial 164.66 MPa | [Xi 2024, pp. 15-15] | Uniaxial compression, 500 °C heating | Water cooling reduces strength by ~75% |
| Linear correlation σ_n = k P_n + l: natural k = −57.188, R²=0.87; water k = −57.111, R²=0.91; LN₂ k = −61.495, R²=0.88 | [Xi 2024, pp. 15-17] | Uniaxial vs. porosity | Strong negative linear relationship |
| Pore damage D_Area after 12 cycles: natural 2.20, water 4.56, LN₂ 2.91 | [Xi 2024, pp. 13-14, 20-22] | Weighted by variation coefficient | Macropore weight c ≈ 0.56–0.62 |
| Damage area ratio from NMRI after 12 cycles: natural 2.56, water 3.58, LN₂ 2.88 | [Xi 2024, pp. 19-20] | Proton density pixel counting | LN₂ ratio higher than natural due to macropore connectivity |
| Porosity fitting equation: P_n = a + b·e^{c·n}, R²≥0.96; coefficients given | [Xi 2024, pp. 10-10] | Separate a,b,c for each cooling method | Predictive model for porosity |
| Macropore proportion increase after 4 cycles: natural 54.18%→65.48%, water 58.78%→67.55%, LN₂ 56.27%→67.20% | [Xi 2024, pp. 13-13] | Micropore and mesopore decrease concurrently | Macropore development dominates total damage |
| Microscopic observation: after 4 cycles, water and LN₂ cooling produced visible microcracks; after 12 cycles, water cooling caused cracks connected with fragments peeling, LN₂ interconnected cracks, natural single-direction cracks | [Xi 2024, pp. 5-6] | LCD digital microscope 300× | Cooling method influences crack morphology |

## Limitations
- The study only considered a single heating temperature (500 °C) and three cooling media; extension to other HDR temperatures (150–650 °C) and other cooling fluids (e.g., CO₂) is not verified. [Xi 2024, pp. 1-2, 3-3, not confirmed for other temperatures]
- All samples were taken from the same granite block to avoid heterogeneity, but natural rock variability and scale effects from laboratory to reservoir scale are not addressed. [Xi 2024, pp. 3-3]
- The porosity fitting and damage equations were derived from a limited number of cycle points (1,2,4,8,12) and may not capture behavior for arbitrary intermediate cycle counts without further validation. [Xi 2024, pp. 10-10, 13-14]
- The NMR conversion coefficient C (T₂-to-pore radius) was assumed constant; actual surface relaxivity ρ₂ could change with thermal damage, potentially introducing error. [Xi 2024, pp. 5-5]
- The relationship between pore damage and mechanical damage is based on a uniaxial compression test; triaxial or in-situ stress conditions in HDR reservoirs are not considered. [Xi 2024, pp. 14-15, not explicitly stated as limitation but inferred from the uniaxial method]

## Assumptions / Conditions
- Thermal-cooling cycle experiments were performed at atmospheric pressure, heated to 500 °C, then cooled to room temperature; the rock was completely dry before heating. [Xi 2024, pp. 3-3]
- Surface relaxation dominates the NMR signal, and diffuse and free relaxation can be ignored by using short echo times. [Xi 2024, pp. 5-5]
- Pore size classification adheres to Hodot (1966) and Li et al. (2014): micropore ≤0.1 μm, mesopore 0.1–1 μm, macropore >1 μm. [Xi 2024, pp. 10-10]
- Damage variable based on effective bearing area (Rabotnov model) is applicable to thermal stress-induced damage; the damaged area loses all bearing capacity. [Xi 2024, pp. 13-14, 19-20]
- The weight coefficients a, b, c for pore size contributions to damage are derived from the coefficient of variation of spectral peak areas, assuming that greater relative variability indicates greater contribution to damage. [Xi 2024, pp. 13-14]
- During LN₂ cooling, a vapor cushion (Leidenfrost effect) reduces convective heat transfer, explaining why LN₂ damage is less than water cooling. [Xi 2024, pp. 10-10]
- The relationship σ_n = σ_0(1−D_n) from Ou et al. (2023) and the statistical damage distribution from Hu et al. (2022) are assumed valid for thermally treated granite. [Xi 2024, pp. 14-15]

## Key Variables / Parameters
- **Independent variables:** Number of thermal cycles n (1,2,4,8,12), cooling method β (natural, water, LN₂). [Xi 2024, pp. 3-3]
- **Pore structure:** porosity P_n (%), T₂ spectral area, T₂ peak amplitude, T₂max (ms), micropore/mesopore/macropore contents and proportions, pore size distribution (μm). [Xi 2024, pp. 6-7, 10-10]
- **Mechanical:** uniaxial compressive strength σ_n (MPa), damage factor D_n. [Xi 2024, pp. 15-15]
- **NMRI:** pixel value probability density distribution, damage area ratio Δ. [Xi 2024, pp. 17-19]
- **Damage coefficients:** T₂ spectral area damage D_Area, porosity damage D_P, and their weights a, b, c (natural: a=0.33102, b=0.08928, c=0.57970; water: a=0.33255, b=0.10678, c=0.56067; LN₂: a=0.33381, b=0.04760, c=0.61859). [Xi 2024, pp. 13-14]
- **Fitting parameters for porosity:** a, b, c as in Table 1; for compressive strength vs. porosity: k, l as in Table 3. [Xi 2024, pp. 10-10, 15-17]
- **Conversion coefficient C** relating T₂ to pore radius (not explicitly given, but implied by the proportional relationship). [Xi 2024, pp. 5-5]

## Reusable Claims
- Under thermal-cooling cycles up to 500 °C, the porosity of granite increases in a rapid-then-slow-then-stable pattern, with the most acute changes occurring within the first 2 cycles. [Xi 2024, pp. 10-10, 20-22]
- Water cooling causes more pore development and mechanical degradation than LN₂ cooling, which in turn causes more than natural cooling, because of differences in heat transfer efficiency and thermal shock. [Xi 2024, pp. 10-10, 17-18]
- The macropore (r > 1 μm) proportion is the dominant contributor to overall porosity change and mechanical damage, and the T₂ spectral area damage coefficient can be calculated with weighted contributions from micropores, mesopores, and macropores. [Xi 2024, pp. 13-14]
- There exists a negative linear correlation between uniaxial compressive strength and porosity for thermally cycled granite, with correlation coefficients R² ≥ 0.87 for the three cooling methods. [Xi 2024, pp. 15-17]
- The pore damage factor derived from porosity (D_P) or T₂ spectral area (D_Area) is positively proportional to the mechanical degradation coefficient (D_n), allowing non-destructive NMR measurements to predict rock strength loss in geothermal wells. [Xi 2024, pp. 15-17, 19-20]
- NMR imaging pixel value distributions shift to higher values (higher proton density) with increasing thermal cycles, corresponding to macropore formation and coalescence, and the damage area ratio can be used to quantify the reduction in effective load-bearing cross-section. [Xi 2024, pp. 17-20]
- The evolution of T₂ spectra from bimodal to trimodal indicates the emergence of a new pore size class (macropores) and enhanced pore connectivity. [Xi 2024, pp. 7-8, 20-22]

## Candidate Concepts
- [[thermal-cooling cycle]]
- [[hot dry rock (HDR)]]
- [[nuclear magnetic resonance (NMR)]]
- [[T₂ spectrum]]
- [[pore size distribution]]
- [[macroporosity damage]]
- [[effective bearing area]]
- [[thermal shock]]
- [[Leidenfrost effect]]
- [[proton density-weighted imaging]]
- [[damage variable]]
- [[uniaxial compressive strength degradation]]
- [[granite pore connectivity]]

## Candidate Methods
- [[low-field NMR for rock porosity]]
- [[T₂ spectrum to pore size inversion]]
- [[proton weighting in NMR imaging]]
- [[pixel value statistics for damage quantification]]
- [[coefficient of variation weighting for pore size damage]]
- [[porosity-based damage variable (D_P)]]
- [[effective bearing area damage model]]
- [[numerical fitting of porosity evolution (P_n = a + b·e^{c·n})]]
- [[linear regression of strength vs. porosity]]
- [[optical microscopy for surface crack observation]]

## Connections To Other Work
- Previous research reported that water and LN₂ cooling promote microcrack growth more than natural cooling, consistent with Rui et al. (2024), Li et al. (2019), Rong et al. (2021), Zhu et al. (2021). [Xi 2024, pp. 2-2]
- Zhu et al. (2020a) found density and P-wave velocity decrease with thermal cycles, especially after first cycle, and UCS and elastic modulus decrease – similar trends observed here. [Xi 2024, pp. 2-2]
- Gao et al. (2021) noted dynamic properties decrease exponentially with thermal cycles and the first cycle induces most damage, aligning with the rapid stage of porosity increase. [Xi 2024, pp. 2-2]
- Jing et al. (2021) used NMR to show that thermal cycles increase mesopore and macropore numbers due to pore water escape, thermal expansion, and mineral decomposition; this study extends to quantitative damage linkage. [Xi 2024, pp. 2-3]
- Cao et al. (2023) observed porosity increase and relaxation peak change from 2 to 3 with water cooling cycles, corroborating the bimodal-to-trimodal transition found here. [Xi 2024, pp. 2-3]
- Wu et al. (2023) showed water cooling causes larger tensile stress, promoting pore development – this study quantifies that effect across three cooling methods. [Xi 2024, pp. 2-3]
- The effective bearing area damage concept builds on Kachanov (1958) and Rabotnov (1963). [Xi 2024, pp. 13-13]
- The statistical strength damage model from Hu et al. (2022) and its relation D_n = 1 − exp[−(σ_n/λ)^k] is adopted for linking porosity to strength degradation. [Xi 2024, pp. 14-15]
- The Leidenfrost effect (Leidenfrost, 1966) explains the reduced heat transfer of LN₂, consistent with Tang et al. (2018). [Xi 2024, pp. 17-18]

## Open Questions
- How do the established damage relationships extrapolate to higher temperatures (e.g., 650 °C) and to different rock types? Not confirmed. [Xi 2024, pp. 1-2, 22-23]
- The effect of confining pressure and in-situ stress on pore damage evolution and the porosity-strength correlation remains unexamined under the present experimental conditions. [Xi 2024, pp. 14-15, no confining pressure data]
- The contribution of mineral-specific thermal expansion anisotropy to crack initiation under different cooling rates has not been isolated; the paper only provides net pore damage. [Xi 2024, pp. 2-3, 18-19]
- Can the T₂ spectrum damage coefficient be directly linked to permeability changes? The study infers connectivity but does not measure permeability. [Xi 2024, pp. 2-3, 10-10]
- The long-term cycling effect (beyond 12 cycles) on pore stabilization and any possible pore closure due to mineral precipitation is unknown. [Xi 2024, pp. 20-22]
- How transferable are the weight coefficients a,b,c to other granites with different initial pore structures and mineralogies? [Xi 2024, pp. 13-14; coefficients may be sample-specific]

## Source Coverage
All 21 indexed source blocks (100% of nonempty blocks) have been processed and used in this compiled page. The indexed text total 104,336 characters; compiled source characters 98,108 (94.0% coverage by chars). The source signature is `2f59e9aee2256ee77fedd7d2efd2e6d6f2c88bc3`. All factual claims are derived from the supplied fragments with cited source labels. No external inventions were made.
