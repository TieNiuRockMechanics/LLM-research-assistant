---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-xi-experimental-investigations-of-compressive-strength-and-thermal-damage-capacity-characte"
title: "Experimental Investigations of Compressive Strength and Thermal Damage Capacity Characterization of Granite under Different Cooling Modes."
status: "draft"
source_pdf: "data/papers/2020 - 不同冷却模式下花岗岩强度对比与热破坏能力表征试验研究.pdf"
collections:
  - "part2"
  - "郤"
citation: "Xi, Baoping, et al. \"Experimental Investigations of Compressive Strength and Thermal Damage Capacity Characterization of Granite under Different Cooling Modes.\" *Chinese Journal of Rock Mechanics and Engineering*, vol. 39, no. 2, Feb. 2020, pp. 286-300. doi:10.13722/j.cnki.jrme.2019.0782."
indexed_texts: "5"
indexed_chars: "23421"
nonempty_source_blocks: "5"
compiled_source_blocks: "5"
compiled_source_chars: "21615"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.92289"
coverage_status: "full-index"
source_signature: "c4382cd8d78e2523bd4da88a05bf5c403f8f4ddc"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T03:45:49"
---

# Experimental Investigations of Compressive Strength and Thermal Damage Capacity Characterization of Granite under Different Cooling Modes.

## One-line Summary
This study experimentally and numerically compares the uniaxial compressive strength and thermal damage capacity of granite subjected to natural air cooling (20 °C) and thermal shock water cooling (20 °C) after heating to 250–600 °C, introducing a thermal shock factor to quantitatively characterize thermal damage ability.

## Research Question
How do different cooling modes (natural air cooling vs. water cooling) after high‑temperature treatment affect the compressive strength and thermal damage of granite, and can a thermal shock factor effectively characterize the thermal damage capacity?

## Study Area / Data
Granite samples (density 2.65–2.67 g/cm³) were prepared as cylinders (50 mm diameter, 100 mm height) following ISRM standards. Samples were heated to target temperatures of 250, 300, 350, 400, 500, and 600 °C, held for 3 h, then cooled either in 20 °C air (natural cooling) or in 20 °C water (thermal shock). [Xi 2020, pp. 1-4]

## Methods
- **Experimental** – Uniaxial compression tests at a displacement rate of 0.001 mm/s. Surface temperature of specimens was recorded using thermocouples during cooling. Tests were performed at room temperature after cooling. [Xi 2020, pp. 1-4]
- **Numerical simulation** – A heat transfer model was built in COMSOL Multiphysics 5.3 assuming isotropic, homogeneous granite with constant thermal properties (thermal conductivity λ = 2.9 W/(m·K), specific heat c = 850 J/(kg·K), density ρ = 2650 kg/m³), elastic constants (E = 14.68 GPa, ν = 0.25), and thermal expansion coefficient α = 7×10⁻⁵ K⁻¹. Convective boundary conditions used heat transfer coefficients of 15 W/(m²·K) for air cooling and 1000 W/(m²·K) for water cooling. The thermal shock factor ω was defined as ω = ∂T/∂t · ∂x/∂t (effectively temperature gradient times cooling rate). Dynamic thermal stress was calculated as σ = αE ω. [Xi 2020, pp. 4-8, 8-12]

## Key Findings
- The compressive strength under water cooling is 85 %–90 % of that under air cooling for all temperature levels tested (250–600 °C). [Xi 2020, pp. 1-4, 14-15]
- Temperature gradients, thermal shock factor, and dynamic thermal stress all evolve similarly; maxima occur near the specimen surface for both cooling modes. Under water cooling, the maximum temperature gradient reached 22 766–57 184 °C/m, whereas under air cooling it was 952–3 022 °C/m. [Xi 2020, pp. 8-12]
- For granite heated to 600 °C and cooled in water, the maximum thermal shock factor was about 94.8 times larger than that in air. [Xi 2020, pp. 8-12]
- The thermal shock factor effectively characterizes thermal damage capacity: UCS decreases linearly with ω_max for air cooling (UCS = ‑0.4571 ω_max + 211.34, R² = 0.9794) and logarithmically for water cooling (UCS = ‑104.23 ln(ω_max) + 1131, R² = 0.9534). [Xi 2020, pp. 12-14]
- The time of most serious internal fracture can be identified from the evolution of the thermal shock factor (within first 10 s for water cooling, around 150 s for air cooling). [Xi 2020, pp. 8-12, 14-15]
- Quantitative classification of thermal damage capacity is feasible using the thermal shock factor. [Xi 2020, pp. 14-15]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| UCS of water‑cooled granite is 85 %–90 % of air‑cooled | Abstract, Section 2.4.2, Conclusion (1) | Samples heated to 250–600 °C, held 3 h, cooled in 20 °C water vs 20 °C air | Ratio consistent across all temperatures |
| Water cooling produces much larger temperature gradient (e.g., 57 184 °C/m vs 3 022 °C/m at 600 °C) | Fig. 8, Fig. 9, Section 3.4 | At surface A‑B distance 5 mm | Max gradient for water is 18.93 times that of air at 600 °C |
| Maximum thermal shock factor ω_max ratio water/air ≈ 94.8 at 600 °C | Section 3.5, Table 2 | ω_max air = 302.2 °C/(m·s), water = 28 602 °C/(m·s) | Calculated from Table 2 |
| Linear correlation UCS–ω_max for air cooling: σ = ‑0.4571 ω_max + 211.34 (R² = 0.9794) | Eq. (7), Fig. 14 | ω_max range 95.2–302.2 °C/(m·s) | Applies to natural cooling only |
| Logarithmic correlation UCS–ω_max for water cooling: σ = ‑104.23 ln(ω_max) + 1131 (R² = 0.9534) | Eq. (8), Fig. 15 | ω_max range 11 383–28 602 °C/(m·s) | Applies to thermal shock cooling only |
| Peak thermal stress in water cooling occurs within ~10 s, then decays; in air cooling peaks ~150 s | Fig. 13 | Point A at surface | Dynamic thermal stress magnitudes: water up to ~48 MPa, air up to ~20 MPa |
| Numerical model assumptions: isotropic, homogeneous, constant λ, c, ρ, E, α | Section 3.2 | Model uses convective boundary with h = 15 (air), 1000 (water) | Parameter values from literature |

## Limitations
- The numerical model assumed constant thermal and mechanical properties, neglecting temperature dependence and possible phase transformations (e.g., quartz α–β transition at ~573 °C) that may affect damage. [Xi 2020, pp. 4-8 assumptions, discussion in Section 6 hints at simplifications]
- Only macroscopic uniaxial compressive strength was measured; no direct microstructural characterization (e.g., CT, SEM) was performed to validate thermal shock factor with actual crack density. [Xi 2020, pp. 14-15 reference to previous CT studies, not done here]
- A single granite type and specimen size was used; results may not generalize to other rock types or larger scales.
- The thermal shock factor definition depends on the assumed heat transfer coefficients, which are empirical and may vary with flow conditions.

## Assumptions / Conditions
- Specimens are isotropic, homogeneous, and elastic with constant thermal properties during cooling. [Section 3.2]
- Cooling media temperatures fixed at 20 °C; water bath maintained at constant temperature with circulation.
- Heat transfer coefficients: 15 W/(m²·K) for air natural cooling, 1000 W/(m²·K) for water thermal shock. [Section 3.2]
- Initial temperature distribution uniform before cooling; no internal heat generation.
- Displacement‑controlled loading at 0.001 mm/s for UCS tests.

## Key Variables / Parameters
- **Independent variables**: initial heating temperature (250–600 °C), cooling mode (air vs. water)
- **Dependent variables**: uniaxial compressive strength (UCS, MPa), surface temperature evolution, temperature gradient, thermal shock factor ω, dynamic thermal stress
- **Model parameters**: λ = 2.9 W/(m·K), c = 850 J/(kg·K), ρ = 2650 kg/m³, E = 14.68 GPa, ν = 0.25, α = 7×10⁻⁵ K⁻¹, h_air = 15 W/(m²·K), h_water = 1000 W/(m²·K)
- **Derived quantities**: maximum thermal shock factor ω_max (from numerical simulation at surface point AB), UCS degradation ratio

## Reusable Claims
1. For granite heated to 250–600 °C and then cooled in 20 °C water, uniaxial compressive strength is only 85 %–90 % of that following natural air cooling at the same initial temperature. [Abstract; Conclusion (1)]
2. The thermal shock factor ω, defined as ω = ∂T/∂t · ∂x/∂t (or equivalently ω = ∂T/∂x · dx/dt), can be used to quantitatively characterize the thermal damage capacity of granite under different cooling modes. [Abstract; Section 5.1]
3. For natural air cooling, UCS and maximum thermal shock factor follow a linear relationship: UCS (MPa) = ‑0.4571 ω_max (°C/(m·s)) + 211.34 (R² = 0.9794) within ω_max 95.2–302.2 °C/(m·s). [Eq. (7); Section 5.2]
4. For water thermal shock cooling, UCS and ω_max follow a logarithmic relationship: UCS (MPa) = ‑104.23 ln(ω_max (°C/(m·s))) + 1131 (R² = 0.9534) within ω_max 11 383–28 602 °C/(m·s). [Eq. (8); Section 5.3]
5. The maximum temperature gradient near the surface is significantly higher under water cooling (e.g., 57 184 °C/m at 600 °C) compared to air cooling (3 022 °C/m), and the maximum gradient ratio is ~18.93. [Section 3.4 and Figs. 8-9]
6. The most intensive internal fracturing occurs within the first 10 s of water cooling, while under air cooling it occurs around 150 s, as indicated by the peak thermal shock factor and thermal stress. [Section 3.5, Figs. 10-13]
7. The heat transfer coefficient strongly influences the thermal shock severity: the water cooling coefficient (1000 W/(m²·K)) produces a thermal shock factor ~94.8 times that of air cooling (15 W/(m²·K)) for 600 °C granite. [Table 2; Section 3.5]

## Candidate Concepts
- [[thermal shock factor]]  
- [[thermal damage capacity]]  
- [[dynamic thermal stress]]  
- [[cooling mode]]  
- [[temperature gradient]]  
- [[heat transfer coefficient]]  
- [[granite thermal cracking]]  
- [[uniaxial compressive strength degradation]]  
- [[convective cooling boundary]]

## Candidate Methods
- [[uniaxial compression test after thermal treatment]]  
- [[surface temperature history measurement]]  
- [[finite element heat transfer simulation (COMSOL)]]  
- [[thermal shock factor derivation]]  
- [[convective heat transfer coefficient assignment]]  
- [[temperature gradient calculation along radius]]

## Connections To Other Work
- The thermal shock factor concept extends earlier work on thermal stress (Lidman & Bobrowsky, 1949; Norton, 1926; Winkelman & Schott, 1894) and rock thermal physics (Lin Muzeng, 1991). [References]
- Similar comparative cooling studies (Kumari et al., 2017, 2018; Shao et al., 2014) report strength reduction under rapid cooling; this study quantifies damage via ω and provides correlation equations. [Section 6; Discussion]
- The approach aligns with numerical modeling of thermal cracking in rock (Tang Shibin et al., 2018) but introduces the thermal shock factor as a practical damage index. [Section 6]
- Previous work on high‑temperature granite properties (Xi Baoping & Zhao Yangsheng, 2010; Xu Xichang & Liu Quansheng, 2000) provides baseline for mechanical changes, enhanced here by cooling mode differentiation. [Introduction references]

## Open Questions
- How does the thermal shock factor correlate with actual microcrack density and distribution, beyond inferred damage? (e.g., CT validation lacking)
- How would temperature‑dependent thermal and mechanical properties affect the model’s predictive accuracy, especially near phase transitions (e.g., quartz inversion)?
- Can the thermal shock factor approach be generalized to other rock types, other cooling fluids, or larger field‑scale geometries?
- What is the role of water‑induced chemical weakening (e.g., subcritical crack growth) superimposed on thermal shock in water cooling?
- Could the thermal shock factor be integrated into a damage variable for constitutive modeling?

## Source Coverage
All 5 non‑empty indexed fragments from Xi et al. (2020) pages 1–4, 4–8, 8–12, 12–14, and 14–15 were processed. Total characters in fragments: 23,421; assembled characters: 21,615; character coverage ratio: 92.3 %; block coverage ratio: 100 %. No sections were omitted. The compiled page uses evidence exclusively from these fragments.
