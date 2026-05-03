---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2012-sun-3d-thermal-structure-of-the-continental-lithosphere-beneath-china-and-adjacent-regions"
title: "3D Thermal Structure of the Continental Lithosphere beneath China and Adjacent Regions."
status: "draft"
source_pdf: "data/papers/2013 - 3D thermal structure of the continental lithosphere beneath China and adjacent regions.pdf"
collections:
  - "山西断裂地质构造"
  - "神经网络结合分形网络研究"
citation: "Sun, Yujun, et al. \"3D Thermal Structure of the Continental Lithosphere beneath China and Adjacent Regions.\" *Journal of Asian Earth Sciences*, 2012, doi:10.1016/j.jseaes.2012.11.020."
indexed_texts: "8"
indexed_chars: "38609"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "38763"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.003989"
coverage_status: "full-index"
source_signature: "e6fb939d660f55d3dc8b81668ef6f48a04d07a17"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T14:56:42"
---

# 3D Thermal Structure of the Continental Lithosphere beneath China and Adjacent Regions.

## One-line Summary
A 3D steady-state finite-element model constrained by surface heat flow and upper mantle temperatures derived from seismic velocities reveals that Precambrian cratons are 100–300 °C colder than surrounding regions, Moho temperatures reach 800–1000 °C beneath Tibet and 500–700 °C beneath cratons, and thermal transition zones correlate with orogenic belts and the north‑south seismic zone.[Sun 2012, pp. 1-1, pp. 5-6, pp. 6-8]

## Research Question
What is the three‑dimensional thermal structure of the continental lithosphere beneath China and adjacent regions, and how does it relate to surface geology, craton stability, and tectonic processes?[Sun 2012, pp. 1-1]

## Study Area / Data
- **Domain**: Chinese continent and adjacent regions (76 °E–136 °E, 20 °N–52 °N).[Sun 2012, pp. 1-2]
- **Model layers**: upper crust, middle crust, lower crust, lithospheric mantle (bottom fixed at 100 km depth). Thicknesses from the Crust2.0 model.[Sun 2012, pp. 1-2]
- **Top boundary**: annual average ground surface temperature, interpolated by Kriging from 195 meteorological stations (terrestrial areas); ocean bottom fixed at 4 °C.[Sun 2012, pp. 1-2, pp. 2-3]
- **Bottom boundary**: temperature at 100 km depth inverted from seismic velocities using the seismic‑thermal method of Goes et al. (2000) and Goes & Lee (2002), as provided by An & Shi (2006, 2007).[Sun 2012, pp. 1-1, pp. 1-2, pp. 2-3]
- **Thermal conductivity**: measured surface values from the global heat‑flow database and other literature, interpolated to 1° × 1°; corrected for temperature and pressure using Eq. (5).[Sun 2012, pp. 2-3]
- **Heat production**: derived from P‑wave velocity using the empirical relationship ln Q = 14.59 ‑ 2.33 V’ₚ (Wang & Wang, 1992), corrected for in‑situ temperature and pressure (Eqs. 7‑9). Upper‑crust heat production adjusted iteratively by fitting calculated surface heat flow to measured values.[Sun 2012, pp. 2-3, pp. 3-5]
- **Surface heat flow constraining**: 390 1° × 1° cells with measured surface heat flow, used to adjust upper‑crust heat production until fitting error <20% in 89% of cells.[Sun 2012, pp. 3-5]

## Methods
- **Numerical approach**: 3D finite‑element solution of the steady‑state heat conduction equation in spherical coordinates (Eq. 1), with 1,205,820 prism elements (horizontal resolution 0.25°, vertical 18 layers).[Sun 2012, pp. 1-2, pp. 2-3]
- **Boundary conditions**: sides adiabatic; top from interpolated ground temperature; bottom from seismically inverted mantle temperature (100 km).[Sun 2012, pp. 2-3]
- **Thermal parameters**: thermal conductivity temperature‑ and pressure‑dependent after interpolation (Eq. 5); radiogenic heat production tied to P‑wave velocity via the Wang & Wang relation, corrected to 293.15 K and 100 MPa using pressure from Crust2.0 density and thickness (Eqs. 8‑9).[Sun 2012, pp. 2-3, pp. 3-5]
- **Iterative fitting**: computed surface heat flow compared with 1°×1° cell averages; upper‑crust heat production adjusted iteratively until 89% of cells have <20% error.[Sun 2012, pp. 3-5]
- **Validation**: comparison with global thermal models (Artemieva & Mooney, 2001; Artemieva, 2006) shows consistency in Tibet and Baikal Rift Zone at 50 km depth, supporting usability in tectonically active regions.[Sun 2012, pp. 6-8]

## Key Findings
1. **Craton vs. surroundings**: Temperature beneath Precambrian cratons (Tarim, Yangtze, Indian plate) is 100–300 °C lower than in other areas at depths 20‑80 km. The Sino‑Korean craton is colder only above ~40 km; below 60 km its eastern part shows elevated temperatures, implying destruction of the cratonic root.[Sun 2012, pp. 1-1, pp. 5-6]
2. **Moho temperatures**: 800–1000 °C beneath the Tibetan plateau, 500–700 °C beneath Precambrian cratons (Indian plate, Sichuan basin, South China, North China, Tarim).[Sun 2012, pp. 1-1, pp. 5-6, pp. 6-8]
3. **Tibetan flow support**: High temperatures in the middle‑lower crust and upper mantle of the central Tibetan plateau (especially Qiangtang) are consistent with the proposed eastward flow of lower crustal or upper mantle material.[Sun 2012, pp. 1-1, pp. 5-6]
4. **Volcanism correlation**: Regions with intensive volcanism (Baikal – Vitim volcanoes; northeastern China – Changbai, Wudalianchi; southwestern China – Tengchong) coincide with dominant high‑temperature anomalies in the crust and upper mantle, likely related to subduction‑slab dehydration (northeast and southwest) and a mantle plume (Baikal).[Sun 2012, pp. 1-1, pp. 5-6]
5. **Orogenic thermal transitions**: Sharp temperature changes occur across orogenic belts (Himalayan, Longmenshan, Yanshan), visible in lateral profiles.[Sun 2012, pp. 1-1, pp. 6-8]
6. **Seismicity link**: The crustal thermal transition between eastern and western China aligns with the north‑south seismic zone, the most seismically active belt in China, suggesting a thermal role in deformation.[Sun 2012, pp. 1-1, pp. 6-8]
7. **Model reliability**: 89% of 390 constrained 1°×1° surface‑heat‑flow cells have <20% fitting error between calculated and observed values, thereby providing a constraint on the depth distribution of crustal radiogenic heat production.[Sun 2012, pp. 3-5]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Calculated surface heat flow matches measured in 348 of 390 1°×1° cells within 20% error | [Sun 2012, pp. 3-5] | 3D steady‑state model; top boundary from 195 meteorological stations; bottom boundary from seismic‑inverted temperature at 100 km; thermal conductivity interpolated and corrected; heat production from Vₚ with upper‑crust adjustment | 89% of cells satisfied criterion; provides constraint on crustal radiogenic heat production distribution. |
| Temperature beneath Precambrian cratons 100‑300 °C colder than other areas at same depth | [Sun 2012, pp. 5-6] | Depths 20, 40, 60, 80 km maps (Fig. 6a‑d); model as above | Exception: eastern Sino‑Korean craton >60 km shows high temperature, indicating destruction. |
| Moho temperature: 800‑1000 °C (Tibet), 500‑700 °C (cratons: Indian plate, Sichuan, South China, North China, Tarim) | [Sun 2012, pp. 5-6, pp. 6-8] | Profiles A‑A', B‑B', etc. (Fig. 7); Crust2.0 Moho | Consistent with low seismic velocities and low electrical resistivity in Tibet (INDEPTH). |
| Eastern Sino‑Korean craton hot below 60 km, indicating lithospheric destruction | [Sun 2012, pp. 5-6] | Temperature map at 60 km (Fig. 6c) and regional context | Agrees with tomography (Feng et al., 2010; Tian & Zhao, 2011) and previous thermal modelling (Artemieva & Mooney, 2001; Lin et al., 2005). |
| High thermal state beneath Qiangtang supports eastward flow of lower crustal/upper mantle material | [Sun 2012, pp. 5-6] | Middle‑lower crust temperatures 800‑1200 °C | Supports flow models (Clark & Royden, 2000; Huang et al., 2000). |
| Volcanoes (Baikal, NE China, SW China) spatially coincide with hot anomalies in crust/upper mantle | [Sun 2012, pp. 5-6] | Temperature maps at 60, 80 km (Fig. 6c,d) | Explained by subducting slab dehydration (Zhao & Liu, 2010) and Baikal mantle plume (Johnson et al., 2005). |
| Sharp thermal transitions across Himalayan, Longmenshan, Yanshan orogenic belts | [Sun 2012, pp. 6-8] | Lateral profiles (Fig. 7a,e,f) | Temperature changes align with crustal structure discontinuities. |
| Crustal thermal transition between eastern and western China coincides with north‑south seismic belt | [Sun 2012, pp. 6-8] | Temperature maps at 20‑40 km depth | Possibly controls seismicity distribution (Wang et al., 2010). |

## Limitations
- The model is **steady‑state**; transient thermal effects in active regions (e.g., Tibet, Baikal) are not captured, although comparison with Artemieva (2006) suggests reasonable estimates at 50 km depth for such regions.[Sun 2012, pp. 6-8]
- **Surface heat flow uncertainty** (up to 20%) would alone cause temperature uncertainties of 120‑200 °C at 50 km and 200‑360 °C at 100 km; the seismic‑inverted bottom temperature (uncertainty ~150 °C) reduces this, but a combined uncertainty remains.[Sun 2012, pp. 6-8]
- **Heat production** is inferred from P‑wave velocity using an empirical relationship whose applicability to all crustal rock types is debated (Fountain, 1987; Kern & Siegesmund, 1989), and depth distribution is adjusted only by surface heat flow fitting.[Sun 2012, pp. 2-3]
- **Thermal conductivity** extrapolated with depth using generic correction factors; local variations in mineralogy may affect accuracy.[Sun 2012, pp. 2-3]
- **Moho depth** taken from Crust2.0; any inaccuracies propagate into temperature estimates.[Sun 2012, pp. 1-2]

## Assumptions / Conditions
- Heat transfer governed by **3D steady‑state conduction equation** in spherical coordinates; no advection or transient terms.[Sun 2012, pp. 1-2]
- **Top boundary** temperature on land equals annual average ground temperature from Kriging‑interpolated station data; ocean bottom set to constant 4 °C.[Sun 2012, pp. 2-3]
- **Bottom boundary** (100 km) temperature directly taken from An & Shi (2006, 2007) seismic‑thermal inversion.[Sun 2012, pp. 2-3]
- **Side boundaries adiabatic** (no lateral heat exchange across model edges).[Sun 2012, pp. 2-3]
- **Radiogenic heat production** obeys ln Q = 14.59 ‑ 2.33 V’ₚ, where V’ₚ is velocity corrected to 293.15 K and 100 MPa.[Sun 2012, pp. 3-5]
- **Thermal conductivity** corrected for temperature and pressure using Eq. 5 with layer‑specific b coefficients。[Sun 2012, pp. 2-3]
- **Upper crust heat production** tuned by iterative fitting to surface heat flow cells; fitting criterion ≤20% error for 89% of cells.[Sun 2012, pp. 3-5]

## Key Variables / Parameters
- **Temperature** T (dependent variable)[Sun 2012, pp. 1-2]
- **Top surface temperature** (annual mean, terrain‑corrected)[Sun 2012, pp. 2-3]
- **Bottom temperature** at 100 km from seismic‑thermal inversion[Sun 2012, pp. 2-3]
- **Thermal conductivity** k (T,P) from Eq. 5[Sun 2012, pp. 2-3]
- **Heat production** Q from Vₚ (Eq. 7)[Sun 2012, pp. 3-5]
- **Crustal layer thicknesses** from Crust2.0 model[Sun 2012, pp. 1-2]
- **Surface heat flow** q_R (computed vs. observed)[Sun 2012, pp. 3-5]

## Reusable Claims
1. In a 3D steady‑state model of China constrained by surface heat flow and seismically derived upper‑mantle temperatures, **Precambrian craton lithosphere is 100–300 °C colder** than surrounding domains at depths up to 80 km, except the eastern Sino‑Korean craton, which is hot below 60 km, indicating destruction.[Sun 2012, pp. 1-1, pp. 5-6]
2. **Moho temperature** beneath the Tibetan plateau is **800–1000 °C**, whereas beneath major cratons (Indian plate, Sichuan basin, South China, North China, Tarim) it is **500–700 °C**; this dichotomy can serve as a regional thermal reference for lithospheric modelling.[Sun 2012, pp. 1-1, pp. 6-8]
3. **Elevated crustal temperatures beneath Qiangtang** support the concept of **eastward crustal/upper mantle flow**, corroborating independent geophysical evidence (low seismic velocities, low resistivity).[Sun 2012, pp. 5-6]
4. **Surface volcanism** (Baikal, NE China, SW China) lies above prominent high‑temperature anomalies in the upper mantle, consistent with slab dehydration and plume‑related thermal sources.[Sun 2012, pp. 5-6]
5. **Sharp thermal contrasts across orogenic belts** (Himalaya, Longmenshan, Yanshan) are a robust feature of the lithospheric thermal field, and the **east‑west crustal thermal transition aligns with the north‑south seismic zone**, suggesting a thermal contribution to seismicity.[Sun 2012, pp. 1-1, pp. 6-8]
6. **A 3D finite‑element approach that iteratively fits surface heat flow with <20% error** provides improved constraints on crustal radiogenic heat production distribution compared to 1D/2D approximations.[Sun 2012, pp. 3-5, pp. 6-8]

## Candidate Concepts
- [[continental lithosphere thermal structure]]
- [[Precambrian craton thermal regime]]
- [[seismic-thermal method]]
- [[upper mantle temperature inversion]]
- [[Crust2.0 model]]
- [[radiogenic heat production – Vp relationship]]
- [[Sino-Korean craton destruction]]
- [[Tibetan plateau lower crustal flow]]
- [[thermal transition zone and seismicity]]
- [[3D steady-state heat conduction in spherical coordinates]]

## Candidate Methods
- [[3D finite element heat conduction model (spherical coordinates)]]
- [[Kriging interpolation of ground temperature and thermal conductivity]]
- [[P-wave velocity to heat production conversion]]
- [[iterative adjustment of upper crust heat production by heat flow fitting]]
- [[temperature-corrected thermal conductivity (Chapman & Furlong parameterization)]]
- [[surface heat flow 1°×1° cell averaging and error evaluation]]

## Connections To Other Work
- Relies on upper mantle temperatures from **An & Shi (2006, 2007)** as bottom boundary.[Sun 2012, pp. 1-1, pp. 2-3]
- Uses the **seismic‑thermal methodology** developed by **Goes et al. (2000)** and **Goes & Lee (2002)**.[Sun 2012, pp. 1-1]
- Global thermal models by **Artemieva & Mooney (2001)** and **Artemieva (2006)** are cited for comparison and validation.[Sun 2012, pp. 6-8]
- Heat production‑velocity relation from **Wang & Wang (1992)**, with critique by Fountain (1987) and Kern & Siegesmund (1989).[Sun 2012, pp. 3-5]
- Tectonic framework based on **Ren et al. (1999)**.[Sun 2012, pp. 1-1]
- Thermal‑rheological models referenced for Tarim (**Liu et al., 2004**), North China (**Zang et al., 2005**), and Eastern China (**Wang & Cheng, 2012**).[Sun 2012, pp. 1-1, pp. 8-8]
- Tomographic evidence from **Feng et al. (2010)** and **Tian & Zhao (2011)** supports the destruction of the Sino‑Korean craton.[Sun 2012, pp. 5-6]
- INDEPTH results (Wei et al., 2001; Haines et al., 2003; Unsworth et al., 2005) provide independent validation for the Tibetan thermal anomaly.[Sun 2012, pp. 5-6]

## Open Questions
- What is the exact **depth distribution of radiogenic heat production** in the Chinese crust, and how does it deviate from a Vₚ‑derived model?[Sun 2012, pp. 3-5]
- How large is the **transient thermal effect** in tectonically active regions (Tibet, Baikal) when a steady‑state solution is used?[Sun 2012, pp. 6-8]
- What is the **uncertainty in the empirical Vₚ‑heat production relation** for diverse crustal lithologies, and can it be replaced by more direct geochemical constraints?[Sun 2012, pp. 3-5]
- How does the **east‑west thermal transition** physically influence seismicity along the north‑south seismic zone?[Sun 2012, pp. 6-8]
- Can the 3D model be extended below 100 km incorporating **mantle advection** to improve thermal estimates for lithosphere‑asthenosphere boundary depth?[not specified in supplied fragments – not confirmed]

## Source Coverage
All **8 non‑empty indexed fragments** from Sun 2012 were processed and compiled. The source signature is `e6fb939d660f55d3dc8b81668ef6f48a04d07a17`. Coverage ratios: **by blocks = 1.0**, **by characters = 1.003989** (total processed characters 38,763 vs. 38,609 original). No fragment was omitted. All factual claims, figures, equations, and references derive exclusively from the supplied indexed material.
