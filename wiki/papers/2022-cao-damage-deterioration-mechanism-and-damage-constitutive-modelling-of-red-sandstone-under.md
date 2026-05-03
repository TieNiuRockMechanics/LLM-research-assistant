---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-cao-damage-deterioration-mechanism-and-damage-constitutive-modelling-of-red-sandstone-under"
title: "Damage Deterioration Mechanism and Damage Constitutive Modelling of Red Sandstone under Cyclic Thermal‑cooling Treatments."
status: "draft"
source_pdf: "data/papers/2022 - Damage deterioration mechanism and damage constitutive modelling of red sandstone under cyclic thermal-cooling treatments.pdf"
collections:
  - "part2"
citation: "Cao, Ri‑hong, et al. \"Damage Deterioration Mechanism and Damage Constitutive Modelling of Red Sandstone under Cyclic Thermal‑cooling Treatments.\" *Archives of Civil and Mechanical Engineering*, vol. 22, 2022, p. 188, doi:10.1007/s43452-022-00505-6."
indexed_texts: "12"
indexed_chars: "57563"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "57032"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.990775"
coverage_status: "full-index"
source_signature: "6d8ac5f3bdf5996f9d61639c6e38d7569a86e403"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T05:10:39"
---

# Damage Deterioration Mechanism and Damage Constitutive Modelling of Red Sandstone under Cyclic Thermal‑cooling Treatments.

## One-line Summary

This study experimentally investigates the damage deterioration, deformation, failure characteristics, and a coupled statistical damage constitutive model for red sandstone subjected to cyclic heating–cooling treatments and uniaxial compression.

## Research Question

How do cyclic heating–cooling (H–C) cycles affect the strength, deformation, microcrack evolution, failure mode, and damage accumulation of red sandstone, and how can a coupled damage constitutive model be derived to describe the mechanical behavior under combined thermal cycling and loading?

## Study Area / Data

- **Material:** Uniform red sandstone, mineral composition determined by XRD: quartz (48.84%), calcite (11.82%), feldspar (23.79%), chlorite (4.03%), mica (6.66%), anhydrite (3.42%), haematite (1.44%).  
- **Specimen geometry:** Cylindrical, 50 mm diameter × 100 mm height, prepared according to ISRM suggested methods.  
- **Test conditions:** Target temperatures of 200 °C, 500 °C, and 600 °C; H–C cycles: 5, 10, 15, 20. Two specimens per cycle number.  
- **Mechanical tests:** Uniaxial compression on a servo‑controlled WHY‑CTS600 system, loading rate 0.12 mm/min, with simultaneous AE monitoring.  
- **Post‑failure analysis:** SEM (Siri200 field emission) imaging of fracture surfaces.  

## Methods

- **Cyclic heating–cooling treatment:** Specimens heated from ambient (25 °C) to target temperature at 5 °C/min, held for 2 h, then naturally cooled to ambient for each cycle.  
- **Uniaxial compression:** Stress, vertical displacement, and AE events recorded.  
- **Macroscopic damage variable:** Defined as \( D_n = 1 - \frac{E_n}{E_0} \), where \( E_0 \) and \( E_n \) are peak tangent moduli of untreated and n‑cycle specimens, respectively.  
- **Crack closure quantification:** Extracted crack closure stress \( \sigma_{cc} \) and strain \( \varepsilon_{cc} \) from tangent modulus–strain curves.  
- **AE‑based crack classification:** Used RA (rise time/amplitude) and AF (average frequency) values, with kernel density estimation to visualize tensile vs. shear/mixed cracks.  
- **Mesoscopic characterization:** SEM scans of fracture surfaces after different cycle numbers.  
- **Damage constitutive model:** Coupled H–C damage and load damage via strain equivalence principle; micro‑element strength assumed to follow Weibull distribution; damage variable corrected by a power‑law factor \( i = \varepsilon^k \) to account for crack closure stage.  
- **Model validation:** Compared theoretical curves with experimental data, and with models by Liu et al. (2020) and Jiang et al. (2022), using RMSE and R².  

## Key Findings

- Peak strength decreased with increasing temperature and number of H–C cycles; at 600 °C, an accelerated decline occurred after 5 cycles.  
- Damage variable \( D_n \) increased with cycle number at all temperatures; at 600 °C, damage accumulation accelerated significantly with cycles.  
- Both crack closure stress \( \sigma_{cc} \) and crack closure strain \( \varepsilon_{cc} \) increased with H–C cycles and temperature, indicating greater difficulty in closing internal cracks.  
- SEM revealed increased intergranular microcrack length, transgranular microcracking, and widened microcrack spacing with cycles; at 20 cycles, microcracks interpenetrated.  
- Macroscopic failure mode transitioned from shear failure (≤10 cycles) to splitting (tensile) failure at 20 cycles, consistent with AE analysis showing tensile cracks becoming dominant.  
- The proposed damage constitutive model with correction coefficient \( k \) captured crack closure deformation well; predicted peak stress, peak strain, and tangent modulus agreed with experiments.  
- Model outperformed Liu et al. and Jiang et al. models in terms of RMSE and R², especially for higher cycle numbers and at the initial loading stage.  
- Weibull parameters \( \alpha \) and \( m \) decreased with cycles, indicating a shift from brittle to ductile behavior and reduced microelement strength concentration.  

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Peak strength at 600 °C declined from ~69.4 MPa (0 cycles) to ~32.7 MPa (20 cycles) | [Cao 2022, pp. 4-5] | Uniaxial compression, 600 °C target temperature | Accelerated decline after 5 cycles |
| Damage variable \( D_n \) at 600 °C increased from ~0.17 (5 cycles) to ~0.56 (20 cycles) | [Cao 2022, pp. 4-5] | Defined by tangent modulus change | Damage accumulation increases with cycle number |
| Crack closure strain \( \varepsilon_{cc} \) increased with cycles; e.g., at 600 °C, from ~0.5% (5 cycles) to ~1.2% (20 cycles) estimated from graphs | [Cao 2022, pp. 6-7] | Extracted from tangent modulus–strain curves | Indicative of increased microcrack density |
| SEM: after 20 cycles at 600 °C, intergranular and transgranular microcracks expand and interpenetrate | [Cao 2022, pp. 6-7] | Post‑failure fracture surfaces, 600 °C | Explains failure mode change |
| AE kernel density clouds show tensile cracks dominate at 20 cycles at 600 °C | [Cao 2022, pp. 10-12] | Crack propagation stage, RA‑AF classification | Consistent with macroscopic splitting failure |
| Constitutive model R² = 0.9167 for 600 °C, 20 cycles (proposed) vs. 0.5276 (Jiang) and −1.3492 (Liu) | [Cao 2022, pp. 14-16] | Uniaxial compression data | Demonstrates model superiority |
| Weibull parameters: for 600 °C, \( \alpha \) decreases from 0.8639 (5 cycles) to 0.4928 (20 cycles) | [Cao 2022, pp. 14-15] | Table 1 parameters | Reflects ductile transition |

## Limitations

- Only one rock type (red sandstone) was tested; generalizability to other lithologies is not confirmed.  
- Thermal cycles used natural cooling; different cooling rates (e.g., water quenching) may yield different damage patterns.  
- The model assumes initial damage zero and that micro‑element strength follows a Weibull distribution; other distributions or initial damage states are not considered.  
- The correction factor \( k \) is empirically determined for each temperature–cycle combination; a predictive relationship for \( k \) is not established.  
- The study focused on uniaxial compression; triaxial and tensile behaviors under cyclic H–C are not addressed.  
- Long‑term cyclic effects (beyond 20 cycles) and coupled thermal–hydraulic–mechanical processes were not investigated.

## Assumptions / Conditions

- Damage accumulation under H–C cycles is quantified solely by the change in peak tangent modulus (macroscopic damage variable).  
- Strain equivalence principle (Lemaitre) holds for coupling H–C damage and load damage.  
- Micro‑element strength within the rock follows a two‑parameter Weibull statistical distribution.  
- Initial damage state of untreated specimens is assumed to be zero.  
- The crack closure stage can be modeled by a power‑law correction factor \( i = \varepsilon^k \).  
- AE crack classification uses a line with slope 0.5 kHz/ms/v to separate tensile from shear/mixed cracks.  
- All tests were performed under ambient conditions after cooling; no real‑time high‑temperature loading.

## Key Variables / Parameters

- **Temperature** \( T \) (°C): 200, 500, 600.  
- **Number of H–C cycles** \( n \): 5, 10, 15, 20.  
- **Damage variable** \( D_n = 1 - E_n/E_0 \).  
- **Peak tangent modulus** \( E_n \) (GPa).  
- **Peak strength** \( \sigma_p \) (MPa).  
- **Peak strain** \( \varepsilon_p \) (%).  
- **Crack closure stress** \( \sigma_{cc} \) and **crack closure strain** \( \varepsilon_{cc} \).  
- **Weibull distribution parameters** \( \alpha \) (scale), \( m \) (shape).  
- **Model correction coefficient** \( k \).  
- **AE metrics** RA (ms/v) and AF (kHz).

## Reusable Claims

- **Claim:** For red sandstone, peak uniaxial compressive strength decreases monotonically with increasing number of heating–cooling cycles, and the rate of decline accelerates when the treatment temperature reaches 600 °C after 5 cycles.  
  *Conditions:* Target temperatures 200–600 °C, cycles 5–20, natural cooling, uniaxial loading.  
- **Claim:** The macroscopic damage variable defined by the reduction in peak tangent modulus increases with cycle number, and damage accumulation is sensitive to both cycle count and temperature level.  
  *Conditions:* Same as above.  
- **Claim:** Cyclic H–C treatment promotes microcrack development, leading to increased crack closure stress and strain, and a transition from shear‑dominated to splitting (tensile) macroscopic failure.  
  *Conditions:* Verified by SEM and AE crack classification; applies to red sandstone at 600 °C.  
- **Claim:** A damage constitutive model combining H–C damage (tangent modulus reduction) and load‑induced damage (Weibull‑based) with a strain‑dependent correction factor can reproduce the full stress–strain curve including the crack closure phase.  
  *Conditions:* Requires calibration of parameters \( \alpha \), \( m \), and \( k \) from experimental data.  
- **Claim:** The Weibull parameters \( \alpha \) and \( m \) decrease with increasing H–C cycles, indicating a shift from brittle to more ductile post‑peak behavior.  
  *Conditions:* Applies to red sandstone under the tested thermal regimes.

## Candidate Concepts

- [[cyclic heating‑cooling damage]]  
- [[macroscopic damage variable]]  
- [[crack closure stress]]  
- [[crack closure strain]]  
- [[transgranular microcrack]]  
- [[intergranular microcrack]]  
- [[splitting failure]]  
- [[strain equivalence principle]]  
- [[Weibull statistical damage model]]  
- [[tangent modulus reduction]]  
- [[acoustic emission crack classification]]  
- [[RA‑AF crack type identification]]  
- [[kernel density estimation for AE data]]  
- [[microcrack spacing]]  
- [[thermal expansion mismatch damage]]

## Candidate Methods

- [[cyclic thermal‑cooling treatment]]  
- [[peak tangent modulus damage quantification]]  
- [[uniaxial compression with AE monitoring]]  
- [[SEM fracture surface analysis]]  
- [[tangent modulus–strain curve crack closure extraction]]  
- [[damage constitutive model with crack closure correction factor]]  
- [[strain equivalence coupling of thermal and load damage]]  
- [[Weibull distribution for microelement strength]]  
- [[AE‑based tensile‑shear crack classification (RA‑AF)]]  
- [[KDE visualization of AE parameter clouds]]  
- [[model comparison using RMSE and R²]]

## Connections To Other Work

- **Hassen (2011):** Provided a coupled thermohydro‑mechanical model for concrete transient creep during a heating–cooling cycle; cited as theoretical foundation.  
- **Jiang et al. (2022):** Proposed a Weibull‑based statistical damage model for red sandstone after heating and water‑cooling cycles; compared here and shown to be less accurate for higher thermal damage.  
- **Zhou et al. (2017):** Developed a statistical damage model for rocks under cyclic stress and high temperature using Weibull distribution; extended in this work with a crack closure correction.  
- **Li et al. (2020):** Used NMR to show porosity/permeability increase in sandstone after thermal treatment; consistent with microcrack development observed here.  
- **Chen et al. (2017) and Wu et al. (2021):** SEM studies on granite showed mineral bond weakening and microcrack growth with temperature; similar mesoscale deterioration seen in red sandstone.  
- **Kong et al. (2018):** Correlated AE time‑domain features with thermal deformation stages; this study used AE for real‑time crack classification during loading.  
- **Ji et al. (2018):** Introduced a method to model nonlinear crack closure; the correction factor \( k \) in this model is conceptually similar.  
- **Yin et al. (2020), Meng et al. (2020), Zhang et al. (2019):** Investigated fracture toughness, shear behavior, and tensile strength of thermally treated rocks; this paper complements those by focusing on cyclic effects and uniaxial compression.

## Open Questions

- How does the damage accumulation and constitutive model behave under different cooling rates (e.g., water quenching vs. natural cooling)?  
- Can the correction coefficient \( k \) be expressed as a function of cycle number and temperature to enable prediction without separate calibration?  
- Is the observed brittle‑to‑ductile transition with cycles generalizable to other sandstones or igneous rocks?  
- What is the evolution of permeability and pore structure under cyclic H–C and how does it couple with mechanical damage?  
- How do cyclic H–C effects influence the long‑term stability of geothermal reservoirs under in‑situ stress and fluid flow conditions?  
- Are there threshold cycle numbers beyond which the constitutive model fails due to extreme damage (e.g., disintegration)?

## Source Coverage

All 12 non‑empty indexed fragments were processed, containing a total of 57,563 indexed characters. The compiled text from these sources accounts for 57,032 characters, yielding a coverage ratio of 0.990775 by characters and 1.0 by blocks. No source block was omitted; the mapping of all fragments is complete.
