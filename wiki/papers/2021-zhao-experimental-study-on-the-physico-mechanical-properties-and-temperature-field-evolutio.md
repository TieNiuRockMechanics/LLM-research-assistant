---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-zhao-experimental-study-on-the-physico-mechanical-properties-and-temperature-field-evolutio"
title: "Experimental Study on the Physico-Mechanical Properties and Temperature Field Evolution of Granite Subjected to Different Heating–Cooling Treatments."
status: "draft"
source_pdf: "data/papers/2021 - Experimental study on the physico-mechanical properties and temperature field evolution of granite subjected to different heating–cooling treatments.pdf"
collections:
  - "靳一作以外的"
citation: "Zhao, Zhongrui, et al. “Experimental Study on the Physico-Mechanical Properties and Temperature Field Evolution of Granite Subjected to Different Heating–Cooling Treatments.” *Bulletin of Engineering Geology and the Environment*, vol. 80, 2021, pp. 8745-8763. DOI: 10.1007/s10064-021-02466-1. Accessed 2026."
indexed_texts: "11"
indexed_chars: "53769"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "53247"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.990292"
coverage_status: "full-index"
source_signature: "a4da78d0a9fe48d4486279ceffcdbecbf10f2fdb"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T04:21:51"
---

# Experimental Study on the Physico-Mechanical Properties and Temperature Field Evolution of Granite Subjected to Different Heating–Cooling Treatments.

## One-line Summary
This study experimentally investigates the deterioration of physical and mechanical properties (permeability, P-wave velocity, UCS, tensile strength) and the evolution of internal temperature field, cooling rate, and temperature gradient in granite heated to 100–300 ℃ and quenched in water at 0–60 ℃, revealing that lower cooling-water temperature aggravates thermal cracking via higher thermal gradients.

## Research Question
How do different heating temperatures (100 ℃, 200 ℃, 300 ℃) and cooling water temperatures (0 ℃, 20 ℃, 60 ℃) affect the physico-mechanical properties and the spatiotemporal evolution of temperature, cooling rate, and temperature gradient inside granite during rapid water cooling, and what is the thermal deterioration mechanism? [Zhao 2021, pp. 1-2, 16-17]

## Study Area / Data
- Rock type: biotite granodiorite from a surface outcrop at Zhumadian city, Henan province, China; mineral composition ≈ 40% plagioclase, 20% quartz, 18% biotite, 15% alkali-feldspar, accessory zircon/apatite; grain size 0.5–2 mm. [Zhao 2021, pp. 2-3]
- Specimens: Φ50 mm × 100 mm cylinders (uniaxial compression), Φ50 mm × 25 mm discs (Brazilian splitting), and Φ50 mm × 100 mm cylinders with 7 embedded thermocouples for temperature monitoring. Natural-state properties: permeability 2.76 × 10⁻¹⁸ m², density 2.60 g/cm³, P-wave velocity 4369.60 m/s, UCS 197.13 MPa, Young’s modulus 35.14 GPa, BTS 8.51 MPa. [Zhao 2021, pp. 3, 4-5]
- Test matrix: 9 groups (3 heating temperatures × 3 cooling water temperatures); each group 3 cylinders, 3 discs, 1 instrumented cylinder. [Zhao 2021, pp. 3-4]

## Methods
- Heating–cooling treatment: specimens heated from 20 ℃ to target (100, 200, 300 ℃) at 2 ℃/min, held >2 h; then quickly immersed in 30 L water tank at 0 ℃, 20 ℃, or 60 ℃; dried 24 h before testing. [Zhao 2021, pp. 3-4]
- Permeability: pressure pulse decay method (Smart perm III) with N₂, confining/axial pressure 5 MPa, initial pore pressure 2.5 MPa. [Zhao 2021, pp. 3-4]
- P-wave velocity: NM-4B non-metal ultrasonic analyzer; Vaseline coupling, 0.2 MPa sensor contact pressure. [Zhao 2021, pp. 4-5]
- Mechanical tests: uniaxial compression and Brazilian splitting at 0.002 mm/s; strain gauges for axial and lateral strain. [Zhao 2021, p. 5]
- Temperature field: 7 thermocouples (Asmik R200D paperless recorder, 1 Hz) at positions A (center), B, C, D (radial), and E, F, G (axial). Temperature evolution, cooling rate v(t)= dT/dt, and temperature gradient analyzed. [Zhao 2021, pp. 3-4, 11-13]
- Numerical verification: COMSOL Multiphysics models of instrumented and intact specimens to assess thermocouple/hole influence on heat conduction. [Zhao 2021, pp. 13-14]

## Key Findings
1. Lower cooling-water temperature aggravated deterioration: after rapid cooling, permeability increased and P-wave velocity, UCS, Young’s modulus, and tensile strength decreased with decreasing cooling-water temperature and increasing heating temperature. [Zhao 2021, pp. 5-6, 6-8]
2. Internal heat transfer was unsteady; temperature evolution divided into three stages: rapid cooling (0–200 s, ~70% of initial ΔT), slow cooling (200–400 s, ~20%), and near-constant (400–600 s, ~10%). [Zhao 2021, pp. 10-11]
3. Cooling rate and temperature gradient both increased sharply then decreased slowly; maximum values always occurred near the outer surface (closest to solid–liquid interface). [Zhao 2021, pp. 11-13]
4. Maximum thermal stress calculated from the largest ΔT exceeded the tensile strength of the granite, explaining thermal cracking; e.g., for 200–0 ℃ sample, calculated thermal stress 22.19 MPa vs. tensile strength 4.57 MPa. [Zhao 2021, pp. 16-17]
5. Microscopic observations confirmed inter-granular and trans-granular microcracks in the 200–0 ℃ sample. [Zhao 2021, pp. 17]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Permeability increased with heating and with lower cooling-water T; at 300 ℃, permeability: 300–60 ℃ ~7.3–9.6 × 10⁻¹⁸ m², 300–0 ℃ 12.1–16.5 × 10⁻¹⁸ m². | [Zhao 2021, Table 2, pp. 4-6] | Granite heated 100–300 ℃, quenched in 0, 20, 60 ℃ water; permeability by pressure pulse decay (N₂, 5 MPa confining). | Increase ratio relative to natural permeability (2.76 × 10⁻¹⁸ m²) provided. |
| P-wave velocity decreased with heating and with lower cooling-water T; at 200 ℃, P-wave velocity: 200–60 ℃ 3871 m/s, 200–0 ℃ 3247 m/s. | [Zhao 2021, Table 2, pp. 5-6] | Same heating–cooling matrix. | Natural P-wave velocity: 4369.60 m/s. |
| UCS reduced from 197.13 MPa (natural) to 137.30 MPa (300–0 ℃) and 163.32 MPa (300–60 ℃). | [Zhao 2021, Table 2, pp. 6-8] | Uniaxial compression at 0.002 mm/s. | Brittle failure in all cases. |
| Tensile strength reduced from 8.51 MPa (natural) to 3.56 MPa (300–0 ℃) and 6.32 MPa (300–60 ℃). | [Zhao 2021, Table 2, pp. 8-11] | Brazilian splitting test. | |
| Temperature evolution stages: for 300–0 ℃, rapid stage (0–200 s) drops ~70% of initial ΔT; the sample reaches water temperature after ~600 s. | [Zhao 2021, pp. 10-11] | Thermocouples at 1 Hz in 7 positions. | Unsteady heat conduction. |
| Maximum cooling rate increased with heating T and lower cooling T: 3.18 ℃/s (100–0 ℃) → 9.46 ℃/s (300–0 ℃); at 100 ℃, 0.88 ℃/s (100–60 ℃) → 3.18 ℃/s (100–0 ℃). | [Zhao 2021, pp. 11-12] | From dT/dt at monitoring point D (outermost radial). | |
| Maximum temperature gradient in radial C-D area: 30.6 ℃/mm for 300–0 ℃, decreasing inward (B-C: 16.1 ℃/mm, A-B: 5 ℃/mm). | [Zhao 2021, pp. 12-13] | Radial temperature differences. | |
| Maximum thermal stress (σ_thermal = EαΔT/(1-ν)): 300–0 ℃ → 41.35 MPa vs. BTS 3.56 MPa; 200–0 ℃ → 22.19 MPa vs. BTS 4.57 MPa. | [Zhao 2021, Table 4, pp. 16-17] | α=6×10⁻⁶ ℃⁻¹, ν=0.25. | Actual stress may be larger because external surface temperature not monitored. |

## Limitations
- Temperature of the external sample surface was not monitored; thus actual maximum thermal stress may be higher than calculated. [Zhao 2021, pp. 16-17]
- The embedded thermocouples, cement filling, and drilled holes influence local heat conduction, especially for axial monitoring points E, F, G (verified by numerical simulation). [Zhao 2021, pp. 13-14]
- Only one rock type (biotite granodiorite) and a limited temperature range (100–300 ℃) were tested; applicability to other lithologies or higher temperatures remains unverified. [Zhao 2021, pp. 2, 17-18]
- The experiments used small cylindrical specimens; scale effects on thermal cracking and fluid flow were not addressed. [Zhao 2021, not explicitly stated; inferred from method constraints]
- Permeability measurements used gas (N₂) under low confining stress (5 MPa); in situ stress and water-rock interactions could alter transport properties. [Zhao 2021, pp. 3-4; note to be marked as not confirmed for in situ extrapolation]

## Assumptions / Conditions
- Thermal stress is estimated using linear thermoelasticity with constant thermal expansion coefficient (α=6×10⁻⁶ ℃⁻¹) and constant Poisson’s ratio (ν=0.25). [Zhao 2021, pp. 16-17]
- The temperature gradient-dominated thermal cracking mechanism is assumed to be the primary cause of property degradation during rapid cooling. [Zhao 2021, pp. 15-16]
- P-wave velocity reduction and permeability increase are treated as proxies for damage (microcrack density). [Zhao 2021, pp. 5-6]
- The heating rate of 2 ℃/min and holding time >2 h are assumed to avoid thermal shock during heating, so pre-existing thermal microcracks are minimal before quenching. [Zhao 2021, pp. 3-4]
- The cooling water volume (30 L) is assumed sufficient to maintain nearly constant bath temperature. [Zhao 2021, pp. 3-4]

## Key Variables / Parameters
- Independent variables: heating temperature (100, 200, 300 ℃), cooling water temperature (0, 20, 60 ℃). [Zhao 2021, pp. 3-4]
- Measured physical properties: permeability (×10⁻¹⁸ m²), P-wave velocity (m/s). [Zhao 2021, pp. 4-5]
- Measured mechanical properties: uniaxial compressive strength (MPa), Young’s modulus (GPa), Brazilian tensile strength (MPa), stress-strain curves. [Zhao 2021, pp. 5, 6-8]
- Temperature field parameters: temperature-time series at 7 points, cooling rate (℃/s), temperature gradient (℃/mm), and maximum temperature difference ΔT (℃). [Zhao 2021, pp. 11-13]
- Derived parameter: thermal stress (σ_thermal = EαΔT/(1-ν)). [Zhao 2021, pp. 16-17]
- Rock properties: grain size 0.5–2 mm, mineral composition, natural density 2.60 g/cm³. [Zhao 2021, pp. 2-3]

## Reusable Claims
- For this granite, permeability after heating followed by water quenching increases with heating temperature and with decreasing cooling water temperature; at 300 ℃, cooling in 0 ℃ water yielded permeability 12.1–16.5 × 10⁻¹⁸ m² versus 7.3–9.6 × 10⁻¹⁸ m² for 60 ℃ water. [Zhao 2021, Table 2, pp. 5-6]
- P-wave velocity decreased from ~4369 m/s (natural) to ~2707–2775 m/s for 300–0 ℃ treatment, indicating substantial damage. [Zhao 2021, Table 2, pp. 5-6]
- UCS of granite dropped to 137.30 MPa (300–0 ℃) from 197.13 MPa (natural); tensile strength dropped to 3.56 MPa (300–0 ℃) from 8.51 MPa (natural). [Zhao 2021, Table 2, pp. 6-8, 8-11]
- Under water quenching, the internal temperature of granite cylinders decreases in three stages: rapid (0–200 s, ~70% of initial ΔT), slow (200–400 s, ~20%), and near-constant (400–600 s, remaining 10%). [Zhao 2021, pp. 10-11]
- The maximum cooling rate and maximum temperature gradient always occur in the outermost region (near the solid–liquid interface). For 300–0 ℃, max cooling rate 9.46 ℃/s, max temperature gradient 30.6 ℃/mm in C-D area. [Zhao 2021, pp. 11-13]
- Calculated thermal stress from the largest temperature difference during quenching exceeds the tensile strength for all tested heating–cooling combinations, confirming that thermal-gradient-induced tensile stress drives cracking. [Zhao 2021, Table 4, pp. 16-17]

## Candidate Concepts
- [[thermal shock cracking]]
- [[unsteady heat conduction in rock]]
- [[cooling rate and temperature gradient evolution]]
- [[permeability enhancement by thermal cracking]]
- [[P-wave velocity as damage indicator]]
- [[thermal stress criterion for granite failure]]
- [[enhanced geothermal system (EGS) stimulation]]

## Candidate Methods
- [[heating–cooling treatment with instrumented specimens]]
- [[pressure pulse decay permeability measurement]]
- [[ultrasonic P-wave velocity testing]]
- [[embedded thermocouple array for internal temperature field]]
- [[finite element model validation of temperature measurements]]
- [[analysis of cooling rate and temperature gradient from time-series data]]
- [[calculation of thermal stress using largest ΔT during quenching]]

## Connections To Other Work
- Previous studies focused on cooling media (liquid nitrogen, air, water) but not on the effect of varying water temperature on temperature field evolution inside the sample. This study fills that gap by systematically varying both heating and cooling water temperatures. [Zhao 2021, pp. 1-2]
- Results agree with findings by Wu et al. (2019a, 2019b, 2019c), Jin et al. (2019), and Sha et al. (2020) that lower cooling-medium temperatures aggravate mechanical degradation and permeability increase in granite. [Zhao 2021, pp. 1-2, 5-6, 8-11]
- The observation that thermal gradient-induced tensile stress exceeds rock tensile strength aligns with numerical simulations by Kim et al. (2014) and Ren et al. (2021). [Zhao 2021, pp. 2, 16]
- The three-stage temperature evolution complements numerical studies by Wu et al. (2021) on flow velocity effects. [Zhao 2021, pp. 2, 11]
- The damage spatial gradient (largest near surface) is consistent with CT-based findings of Fan et al. (2020). [Zhao 2021, pp. 2]

## Open Questions
- How do cooling-induced thermal cracks evolve under subsequent mechanical loading or long-term fluid circulation? (Not covered in this study.)
- What is the effect of confining stress on thermal cracking and permeability under in-situ conditions? (Tests were conducted at low or zero confining stress except for permeability measurement at 5 MPa.)
- Can the thermal stress exceed tensile strength at greater depths when in-situ stress and pore pressure are considered? (Only calculated for unconfined lab conditions.)
- How do mineralogical variations (e.g., different granite types) influence the temperature gradient thresholds for cracking?
- What is the role of thermal expansion mismatch between minerals during rapid cooling compared to gradient-induced stress? (The study primarily attributes deterioration to gradient-induced stress but acknowledges both mechanisms.)
- Could the experimental design be improved by using smaller thermocouples and insulating the exposed parts of the protection tube to reduce thermal disturbance? (Suggested by authors as a future improvement.)

## Source Coverage
All non-empty indexed fragments (11 fragments, covering ~53,769 characters) were processed. The compiled markdown incorporates information from all fragments, with a coverage ratio of 1.0 by blocks and 0.99 by characters. No additional sources were used.
