---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2016-he-effects-of-surface-roughness-on-the-heat-transfer-characteristics-of-water-flow-through"
title: "Effects of Surface Roughness on the Heat Transfer Characteristics of Water Flow through a Single Granite Fracture."
status: "draft"
source_pdf: "data/papers/2016 - Effects of surface roughness on the heat transfer characteristics of water flow through a single granite fracture.pdf"
collections:
  - "part2"
  - "雷恩学派分形研究"
citation: "He, Yuanyuan, et al. \"Effects of Surface Roughness on the Heat Transfer Characteristics of Water Flow through a Single Granite Fracture.\" *Computers and Geotechnics*, vol. 80, 2016, pp. 312-321. doi:10.1016/j.compgeo.2016.09.002. Accessed 2026."
indexed_texts: "8"
indexed_chars: "36267"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "36403"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.00375"
coverage_status: "full-index"
source_signature: "c4b9aa05600381b2024e35d38a6227bb8ed39d10"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T16:30:49"
---

# Effects of Surface Roughness on the Heat Transfer Characteristics of Water Flow through a Single Granite Fracture.

## One-line Summary
Combining experiment and numerical simulation, this study examines how fracture surface roughness (quantified by fractal dimension and profile waviness) governs the local heat transfer coefficient distribution during water flow through a single granite fracture, finding that roughness dominates over aperture and flow rate.

## Research Question
How does the surface roughness of a single rock fracture – characterized by the fractal dimension \(D\) (updated h‑L method) and the profile waviness \(Ra\) – affect the heat transfer behaviour of flowing water, especially the spatial distribution of the local heat transfer coefficient?

## Study Area / Data  
- Rock sample: cylindrical granite core (diameter ≈ 50 mm, length ≈ 98 mm) split by the Brazilian method. [He 2016, pp. 2-4]  
- Fracture surface: 3‑D laser scan (Olympus LEXT OLS4100) of the upper half; five evenly spaced 2‑D profiles (Y = 30, 40, 50, 60, 70) used for analysis. [He 2016, pp. 2-4]  
- Experimental conditions: confining pressures 0, 3, 6 MPa → apertures 125.5, 95, 80.5 µm; flow rates 5, 15, 30 ml/min; inlet water temperatures 328–356 K; outlet temperatures 350–362 K (Table 2). [He 2016, pp. 4-6]  
- Rock properties: thermal conductivity 2.78 W/(m·K), density 2968 kg/m³. [He 2016, pp. 2-4]  

## Methods  
### Roughness characterisation  
- Fractal dimension \(D\) computed using the updated h‑L method (Li & Zhang, 2015) on four‑digit precision profile curves. [He 2016, pp. 2-2, 2‑4]  
- Profile waviness \(Ra\) defined as the vertical distance of a surface point from a reference plane (Z = 0). [He 2016, pp. 6-8]  

### Experiment  
- Triaxial apparatus TAW‑2000 with high‑pressure cell, controlled temperature and flow; laminar flow verified. [He 2016, pp. 2-4, 4‑6]  
- Outlet temperatures recorded after steady state (Table 2). [He 2016, pp. 4-6]  

### Numerical model  
- 2‑D COMSOL Multiphysics model: upper surface profile extruded by aperture as the fracture. Navier‑Stokes equations for water (constant density), heat conduction in rock. No contact asperities. [He 2016, pp. 4-6, 4‑6]  
- Local heat transfer coefficient \(h'\) from Eq. (4):

\(h' = \frac{c_{p,w}\,\rho_w\,u\,d\,(t_2 - t_1)}{2\,(x_2 - x_1)\,\bigl(T_i - \frac{t_1 + t_2}{2}\bigr)}\)  

where \(t_1, t_2\) = water temperatures at adjacent points, \(T_i\) = inner surface temperature, \(u\) = flow velocity, \(d\) = aperture. [He 2016, pp. 2-2]  

- Simulation verified against experiment: outlet temperature error ≤ 0.62 % (Fig. 8). [He 2016, pp. 6-6]  

### Analysis  
- For each profile and flow condition, water temperature, inner surface temperature, flow rate exported; \(h'\) computed along the flow path and compared with \(Ra\). [He 2016, pp. 6-8]  

## Key Findings  

1. **Dominance of surface roughness** – The local heat transfer coefficient distribution depends primarily on fracture surface roughness, followed by aperture and flow rate. [He 2016, pp. 8-8]  

2. **Inverse relationship with waviness** – \(h'\) attains a minimum where \(Ra\) is maximum (humps) and a maximum where \(Ra\) is minimum (depressions); it remains constant on smooth stretches. [He 2016, pp. 8-8]  

3. **Temperature distributions insensitive to roughness** – When flow rate and aperture are held constant, water and inner‑surface temperature profiles remain approximately logarithmic, and surface roughness has little effect on their shape. [He 2016, pp. 8-8]  

4. **Small temperature difference justifies lumped‑temperature assumption** – The difference between water and inner‑surface temperature is negligible (Fig. 13), supporting the common simplification of identical bulk‑fluid and fracture‑surface temperatures in rough heat‑transfer estimates. [He 2016, pp. 8-8]  

5. **Secondary role of flow rate and aperture** – For a fixed surface roughness, \(h'\) increases with flow rate and decreases with larger aperture, but neither factor substantially alters the spatial distribution pattern. [He 2016, pp. 8-8]  

6. **Contrast with average coefficients** – Traditional formulas (Chapman, Zhao, Zhang) yield a single average \(h\) for a given condition, whereas Eq. (4) reveals a strongly position‑dependent local \(h'\) that follows the fracture topography (Fig. 15). [He 2016, pp. 6-8, 8‑8]  

## Core Evidence Table  

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Local \(h'\) distribution mainly controlled by surface roughness, then aperture and flow rate. | [He 2016, pp. 8-8] (conclusion 6) | All flow‑rate/aperture combinations; five profiles with \(D\) 1.0159–1.0258 | Consistent across the tested parameter range. |
| \(h'\) minimum at humps (max \(Ra\)), maximum at depressions (min \(Ra\)). | [He 2016, pp. 8-8] (conclusion 2) | All profiles (e.g., Fig. 15) | Flow rate lower at humps, higher at depressions. |
| Water temperature and inner‑surface temperature distributions are approximately logarithmic and barely affected by changes in surface roughness. | [He 2016, pp. 8-8] (conclusion 3) | Constant flow rate = 30 ml/min, aperture 125.5 µm (Fig. 9–10) | Also observed at other conditions. |
| Difference between water and inner‑surface temperature is small enough to ignore. | [He 2016, pp. 8-8] (conclusion 4) | Example: 5 ml/min, aperture 80.5 µm (Fig. 13) | Supports identical‑temperature assumption. |
| Maximum simulation error in outlet temperature is 0.62 %. | [He 2016, pp. 6-6] | Y = 50 profile; three apertures, three flow rates (Fig. 8) | Validates numerical model. |
| Average heat transfer coefficient formulas give three different constants for one condition, whereas local \(h'\) is a varying distribution. | [He 2016, pp. 6-8, 8‑8] | 30 ml/min, 125.5 µm (Figs. 14, 15) | Highlights limitation of lumped‑parameter equations. |

## Limitations  
- Model assumes no contact asperities; only the main fracture surfaces are considered. [He 2016, pp. 4-6]  
- Analysis restricted to a 2‑D rectangular geometry; three‑dimensional channeling effects are ignored. [He 2016, pp. 4-6]  
- Only one granite specimen and five profile slices are studied.  
- Conclusions are stated to be scale dependent (no universality claimed). [He 2016, pp. 8-8]  
- Inlet and outlet temperatures were forced to be identical across different roughness profiles in the simulations, which may mask some roughness‑induced inlet/outlet variations. [He 2016, pp. 6-6]  

## Assumptions / Conditions  
- Laminar, single‑phase water flow (confirmed by Re number). [He 2016, pp. 2-4]  
- Constant water density (1000 kg/m³) and specific heat (4200 J/(kg·K)). [He 2016, pp. 2-2]  
- No contact between fracture halves (aperture uniform across the width). [He 2016, pp. 4-6]  
- Rock outer surface temperature fixed at 90 °C. [He 2016, pp. 4-6]  
- Identical inlet/outlet temperatures for all five profiles in simulations. [He 2016, pp. 6-6]  
- Identical temperature between bulk fluid and fracture surface is acceptable for rough heat transfer estimation. [He 2016, pp. 8-8]  

## Key Variables / Parameters  
- Fractal dimension \(D\) (updated h‑L method)  
- Profile waviness \(Ra\) (mm)  
- Local heat transfer coefficient \(h'\) (W/(m²·K))  
- Average heat transfer coefficient \(h\) (W/(m²·K))  
- Flow rate (ml/min) → velocity \(u\) (m/s)  
- Aperture \(d\) (µm)  
- Confining pressure (MPa)  
- Inlet water temperature \(t_1\) (K), outlet temperature \(t_2\) (K)  
- Water temperature along fracture, inner surface temperature \(T_i\)  
- Rock thermal conductivity \(k\) (2.78 W/(m·K)), rock density \(\rho_r\) (2968 kg/m³)  

## Reusable Claims  
1. *“The local heat transfer coefficient distribution mainly depends on the fracture surface roughness, followed by aperture and flow rate.”*  
   – Condition: single water‑flushed granite fracture under laminar flow, no contact asperities; conclusion may be scale‑dependent. [He 2016, pp. 8-8]  

2. *“The local heat transfer coefficient reaches a minimum where the profile waviness \(Ra\) reaches a maximum (hump) and reaches a maximum where \(Ra\) reaches a minimum (depression); it remains constant when the surface is relatively smooth.”*  
   – Condition: as above; observed for all five roughness profiles. [He 2016, pp. 8-8]  

3. *“Surface roughness has little effect on the water temperature and the inner surface temperature distribution along the flow direction when flow rate and aperture are constant; both remain approximately logarithmic.”*  
   – Condition: constant flow rate and aperture, water‑rock heat exchange at 90 °C external temperature. [He 2016, pp. 8-8]  

4. *“It is reasonable to assume an identical temperature between the bulk fluid and fracture surfaces during rough estimation of heat transfer effect for simplicity.”*  
   – Condition: verified by small temperature difference (Fig. 13) under the tested range. [He 2016, pp. 8-8]  

5. *“The updated h‑L method (Li & Zhang, 2015) provides a convenient, non‑subjective way to calculate fractal dimension \(D\) of rock joint profiles from 2‑D data.”*  
   – Condition: requires removal of trend and identification of intersection points; tested on five granite profiles. [He 2016, pp. 2-2, 2‑4]  

6. *“When surface roughness is held constant, the local heat transfer coefficient increases with increasing flow rate and decreases with increasing aperture, but the shape of the distribution remains essentially unchanged.”*  
   – Condition: demonstrated for Y = 30 profile (Fig. 16). [He 2016, pp. 8-8]  

## Candidate Concepts  
- [[fracture surface roughness]]  
- [[local heat transfer coefficient]]  
- [[fractal dimension D]]  
- [[profile waviness Ra]]  
- [[updated h-L method]]  
- [[hot dry rock]]  
- [[enhanced geothermal system]]  
- [[convective heat transfer in fractures]]  
- [[fracture aperture]]  
- [[tortuosity]]  
- [[joint roughness coefficient (JRC)]]  
- [[fractal geometry in rock mechanics]]  
- [[temperature difference assumption]]  

## Candidate Methods  
- [[h-L method (fractal dimension)]]  
- [[COMSOL Multiphysics fluid-solid coupling]]  
- [[experimental-numerical combined approach for heat transfer]]  
- [[laser scanning microscopy (Olympus LEXT OLS4100)]]  
- [[Brazilian split for fracture creation]]  
- [[local heat transfer coefficient calculation from numerical temperature data]]  
- [[profilometry-based roughness quantification]]  

## Connections To Other Work  
- **Bai et al. (2016)** – provided the experimental and numerical framework for obtaining local heat transfer coefficients; this paper extends that work to examine roughness effects. [He 2016, pp. 2-2, 4‑6]  
- **Li & Zhang (2015)** – proposed the updated h‑L method for fractal dimension here adopted. [He 2016, pp. 2-2]  
- **Zhao (1999), Zhao & Tso (1993)** – earlier noted non‑linear temperature profiles and questioned constant heat transfer coefficients. [He 2016, pp. 1-2]  
- **Tsang (1984), Brown (1987)** – showed that ignoring surface roughness can cause 1–2 orders of magnitude error in flow estimation. [He 2016, pp. 1-2]  
- **Chapman (1989), Zhao (1993), Zhang et al. (2015)** – provided average heat transfer coefficient formulas that are compared with the local distribution results. [He 2016, pp. 6-8]  
- **Xie & Pariseau (1994)** – established fractal dimension as a measure of JRC. [He 2016, pp. 2-2]  
- **Ranjith (2010)** – showed that roughness determines the Reynolds number that describes flow state. [He 2016, pp. 1-2]  

## Open Questions  
- Do the observed relationships hold for three‑dimensional fracture networks and under higher confining pressures?  
- How would the presence of contact asperities (omitted here) alter the local heat transfer coefficient distribution?  
- Can the scale‑dependent conclusions be generalized across different rock types and fracture scales?  
- What is the precise link between the updated h‑L fractal dimension and the flow‑determined “hydraulic roughness”?  
- Are there robust scaling laws between profile waviness statistics and the spatial pattern of \(h'\)?  

## Source Coverage  
All 8 non‑empty indexed source blocks were processed.  
- Compiled source blocks: 8  
- Coverage ratio (by number of blocks): 1.0  
- Coverage ratio (by character count): 1.00375 (compiled characters exceed indexed characters slightly due to formatting, fully within the source).  
- Source signature: `c4b9aa05600381b2024e35d38a6227bb8ed39d10`  
- Compile strategy: single-pass markdown from full-index coverage.
