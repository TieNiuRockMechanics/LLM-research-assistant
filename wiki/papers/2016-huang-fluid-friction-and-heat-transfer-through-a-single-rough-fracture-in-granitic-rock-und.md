---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2016-huang-fluid-friction-and-heat-transfer-through-a-single-rough-fracture-in-granitic-rock-und"
title: "Fluid friction and heat transfer through a single rough fracture in granitic rock under confining pressure."
status: "draft"
source_pdf: "data/papers/2016 - Fluid friction and heat transfer through a single rough fracture in granitic rock under confining pressure.pdf"
collections:
citation: "Huang, Xiaoxue, et al. \"Fluid friction and heat transfer through a single rough fracture in granitic rock under confining pressure.\" 11 Apr. 2016. Accessed 1 Jan. 2026."
indexed_texts: "7"
indexed_chars: "31551"
nonempty_source_blocks: "7"
compiled_source_blocks: "7"
compiled_source_chars: "31705"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004881"
coverage_status: "full-index"
source_signature: "b6a39fcb0a2aab18a5b55350144f0e505ad2fbf9"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T16:36:52"
---

# Fluid friction and heat transfer through a single rough fracture in granitic rock under confining pressure.

## One-line Summary
Experiments with water flowing through a single rough fracture in a cylindrical granite sample under confining pressure produced dimensionless correlations for the Poiseuille number (Po) and Nusselt number (Nu), revealing that large relative roughness drastically increases flow friction and weakens convective heat transfer compared to smooth macrochannels, and a roughness–viscosity model (RVM) captured the measured behaviour [Huang 2016, pp. 1-1].

## Research Question
The work aimed to characterise single‑phase convective heat transfer and pressure drop of water through a single rough fracture in granitic rock, quantify the influence of fracture surface roughness and confining pressure, and develop empirical relations between flow rate, pressure drop, and heat transfer coefficient for enhanced geothermal systems [Huang 2016, pp. 1-2].

## Study Area / Data
- Laboratory‑scale experiment on a single tensile fracture in a granite cylinder (diameter 50 mm, length ~98.44 mm) created by the Brazilian method [Huang 2016, pp. 1-2].
- Deionised water was pumped through the fracture at flow rates 5–35 ml/min [Huang 2016, pp. 2-4].
- Confining pressures: Pc = 0, 3, 6 MPa [Huang 2016, pp. 4-5].
- Fracture surface topology (non‑contact laser scanning): average aperture δ = 135 μm, average roughness Ra = 20 μm, relative roughness Ra/2Rh = 0.148 at Pc = 0 MPa; Ra/2Rh increased slightly with confining pressure (0.1526 at 3 MPa, 0.1539 at 6 MPa) [Huang 2016, pp. 1-2, 4-5].
- Measured parameters: inlet/outlet fluid temperatures (T1, T2), rock outer surface temperature (To), volumetric flow rate Q, total pressure drop ΔPtotal [Huang 2016, pp. 2-4].
- A total of 90 experimental data points were collected, covering Re ≈ 8–80, Pr ≈ 1.69–3.39 [Huang 2016, pp. 4-5, 7-8].

## Methods
1. **Experimental setup**: high‑pressure triaxial cell; fractured rock wrapped in a thermal sleeve and immersed in hydraulic oil; Teledyne Isco syringe pump for precise water delivery; electric heater with temperature control; Pt100 sensors (accuracy 0.5 °C); strain‑based displacement monitoring [Huang 2016, pp. 1-2, 2-4].
2. **Surface characterisation**: Olympus LEXT OLS4100 Laser Scanning Microscope with a 0.8 mm cutoff wavelength to separate roughness from waviness; average Ra and aperture obtained by combining asperity heights of both fracture halves [Huang 2016, pp. 1-2].
3. **Data reduction**:
   - Po is calculated from net frictional pressure drop ΔP (correcting for minor and major losses using Streeter’s correlations) [Huang 2016, pp. 2-4].
   - The average fracture surface temperature Ti is obtained from a steady‑state heat balance assuming conduction only in semi‑cylindrical rock halves and negligible axial conduction, following Carslaw and Jaeger [Huang 2016, pp. 2-4].
   - Average Nu is based on the hydraulic diameter (2δ) and the mean temperature difference between water and fracture surface [Huang 2016, pp. 4-5].
4. **Empirical correlations**: Po and Nu are fitted as functions of Re (and Pr for Nu) for each confining pressure, yielding Eqs. (7a)–(7c) and (9a)–(9c) [Huang 2016, pp. 4-5].
5. **Roughness–viscosity model (RVM)**: adopted from Mala & Li; effective viscosity μeff = μf + μr, where μr depends on a roughness Reynolds number Rek and an empirical coefficient A (Eq. 13); momentum and energy equations are solved numerically across the fracture aperture (x‑direction changes neglected, finite difference for energy) [Huang 2016, pp. 5-7].

## Key Findings
- Flow friction in the fracture is **much larger** than the ideal parallel‑plate value (Po = 96); Po decreases with Re, but the decrease is gentler at higher Re [Huang 2016, pp. 4-5, 7-8].
- Nusselt number is **two orders of magnitude smaller** than the macrochannel value (7.54); Nu increases rapidly with decreasing non‑dimensional heating length Lh+ (i.e., higher Re and Pr enhance heat transfer) [Huang 2016, pp. 4-5, 7-8].
- Applying confining pressure (0 → 6 MPa) reduces aperture and raises relative roughness, leading to **increases in both Po and Nu** for the same Re [Huang 2016, pp. 4-5].
- The Prandtl number exponent in the Nu correlation is **>1**, in contrast to typical macrochannel correlations, because μeff > μf [Huang 2016, pp. 5, 7-8].
- The **RVM predictions agree well with experimental Po and Nu** (Figs. 6 and 8); the model shows that roughness thickens the boundary layer, increasing wall shear stress (hence higher pressure drop) and reducing near‑wall velocity and temperature gradients (hence lower Nu) [Huang 2016, pp. 5-7, 7-8].
- The empirical coefficient A for the fracture surface is given by Eq. (13): A = (Rh/Ra)^2.7334 exp(0.2235 Re – 0.0395 Re Rh/Ra) [Huang 2016, pp. 5-7].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Po = 96^2.3053 Re^{-0.2902} for Ra/2Rh = 0.148 (Pc = 0) | [Huang 2016, pp. 4-5] | 8 ≤ Re ≤ 80, water, granite, Pc = 0 MPa | Po far above 96, decreases with Re. |
| Po = 96^2.3728 Re^{-0.1723} for Ra/2Rh = 0.1526 (Pc = 3 MPa) | [Huang 2016, pp. 4-5] | 8 ≤ Re ≤ 80, water, granite | Higher Pc raises Po. |
| Po = 96^2.4268 Re^{-0.1575} for Ra/2Rh = 0.1539 (Pc = 6 MPa) | [Huang 2016, pp. 4-5] | 8 ≤ Re ≤ 80, water, granite | Slope gentler than lower Pc. |
| Nu = 7.54 – 3.6107 Re^{1.2399} Pr^{0.8583} for Ra/2Rh = 0.148 | [Huang 2016, pp. 4-5] | 8 ≤ Re ≤ 80, 1.69 ≤ Pr ≤ 3.39 | Nu ~ two orders lower than 7.54. |
| Nu = 7.54 – 3.7815 Re^{1.3113} Pr^{1.0251} for Ra/2Rh = 0.1526 | [Huang 2016, pp. 4-5] | same Re, Pr range | Pr exponent > 1. |
| Nu = 7.54 – 4.2424 Re^{1.3632} Pr^{1.5388} for Ra/2Rh = 0.1539 | [Huang 2016, pp. 4-5] | same Re, Pr range | Nu increases with Pc. |
| Surface roughness Ra = 20 μm, initial aperture δ0 = 135 μm | [Huang 2016, pp. 1-2] | granite, Brazilian split, laser scan, cutoff 0.8 mm | Relative roughness 0.148 at Pc = 0. |
| Aperture determination uncertainty wδ/δ ≈ 6.08 % when Pc applied, leading to wPo/Po = 18.4 %, wNu/Nu = 2.46 % | [Huang 2016, pp. 7-8] | full experimental runs | Uncertainty analysis per Holman. |
| RVM predicts velocity profile with thickened boundary layer and reduced near‑wall gradients; matches flow and heat transfer data | [Huang 2016, pp. 5-7, 7-8] | Re = 8–80, model coefficient A from Eq. (13) | Valid for laminar flow. |

## Limitations
- Experiments cover only **laminar flow** (Re ≤ 80) and a limited range of Pr (1.69–3.39) and relative roughness (0.148–0.1539) [Huang 2016, pp. 7-8].
- The fracture is a **single artificial tensile fracture** in a specific granite; surface conditions and aperture distributions may differ in natural or shear fractures.
- Po and Nu correlations were developed for the specific fracture geometry and may not generalise without further validation.
- The RVM relies on an **empirical coefficient A** fitted to the same experimental data; its transferability to other fractures, fluids, or flow regimes is not demonstrated [Huang 2016, pp. 5-7].
- The experimental set‑up avoids phase change; water remained liquid throughout; results cannot be directly applied to boiling or two‑phase conditions [Huang 2016, pp. 7-8].
- Uncertainty in Po (18.4 %) is significant, largely due to aperture uncertainty under confining pressure [Huang 2016, pp. 7-8].

## Assumptions / Conditions
- Heat transfer within the rock is pure **conduction in semi‑cylindrical slices**, with no axial conduction; the rock outer surface temperature To is constant and equals the surrounding oil temperature [Huang 2016, pp. 2-4].
- Flow is **fully developed laminar** and pressure‑driven; the fracture height‑to‑width ratio H/W is minute, so velocity variation in the x‑direction is neglected [Huang 2016, pp. 2-4, 5-7].
- The **net frictional pressure drop** is obtained by subtracting minor and major losses estimated from Streeter’s handbook correlations [Huang 2016, pp. 2-4].
- Surface roughness was separated from waviness using a **standard cutoff wavelength of 0.8 mm** [Huang 2016, pp. 1-2].
- The mean fluid temperature between inlet and outlet is used as the reference temperature for fluid properties [Huang 2016, pp. 2-4].
- In the RVM, **velocity in the x‑direction** (spanwise) is ignored; this assumption is justified by the very small fracture H/W [Huang 2016, pp. 5-7].

## Key Variables / Parameters
- **Poiseuille number** (Po = f·Re) – dimensionless flow resistance [Huang 2016, pp. 2-4].
- **Average Nusselt number** (Nu = h·Dh/λw) – dimensionless heat transfer [Huang 2016, pp. 2-4].
- **Reynolds number** (Re = 2ρQ/(μf b)) based on hydraulic diameter 2δ [Huang 2016, pp. 2-4].
- **Prandtl number** (Pr) [Huang 2016, pp. 4-5].
- **Relative roughness** (Ra/2Rh) – key surface‑condition parameter; varied from 0.148 to 0.1539 [Huang 2016, pp. 1-2, 4-5].
- **Confining pressure** (Pc = 0, 3, 6 MPa) – controls aperture reduction [Huang 2016, pp. 4-5].
- **Fracture aperture** (δ) – determined from initial measurement and displacement under Pc [Huang 2016, pp. 1-2, 7-8].
- **Non‑dimensional heating length** (Lh+ = L/(2Re·Pr)) – used to characterise thermal entrance region [Huang 2016, pp. 4-5].
- **Effective viscosity** (μeff = μf + μr) – RVM parameter [Huang 2016, pp. 5-7].
- **Roughness Reynolds number** (Rek) and empirical coefficient A – RVM closure [Huang 2016, pp. 5-7].

## Reusable Claims
1. **Po‑Re correlation for water flow through a rough granite fracture**  
   - *Claim*: At Ra/2Rh = 0.148 (Pc = 0), Po = 96^2.3053 Re^{-0.2902} for 8 ≤ Re ≤ 80.  
   - *Condition*: Single tensile fracture, laminar flow, water, granite, specific surface topology.  
   - *Source*: [Huang 2016, pp. 4-5].
2. **Nu‑Re‑Pr correlation for water flow through a rough granite fracture**  
   - *Claim*: At Ra/2Rh = 0.148, Nu = 7.54 – 3.6107 Re^{1.2399} Pr^{0.8583} for 8 ≤ Re ≤ 80 and 1.69 ≤ Pr ≤ 3.39.  
   - *Condition*: Same fracture, Lh+ > 0.14 (thermal entrance region lengthened by roughness).  
   - *Source*: [Huang 2016, pp. 4-5].
3. **Effect of confining pressure on friction and heat transfer**  
   - *Claim*: Increasing confining pressure (decreasing aperture) raises Po and Nu at a given Re.  
   - *Condition*: For Pc 0 → 6 MPa, Ra/2Rh increased 0.148 → 0.1539, Po exponent and Nu coefficients increased accordingly.  
   - *Source*: [Huang 2016, pp. 4-5].
4. **RVM predictive capability for rough‑fracture flow**  
   - *Claim*: The roughness–viscosity model with effective viscosity μeff = μf[1 + A Rek (l/Ra) (1 – exp(–Rek Re l/Ra))²] and coefficient A from Eq. (13) yields numerical results that agree well with experimental Po and Nu.  
   - *Condition*: Laminar, pressure‑driven flow; model calibrated to the same fracture.  
   - *Source*: [Huang 2016, pp. 5-7, 7-8].
5. **Mechanism of roughness‑induced changes**  
   - *Claim*: Surface roughness thickens the boundary layer, increasing total shearing stress (higher ΔP) while reducing near‑wall velocity and temperature gradients (lower Nu).  
   - *Condition*: As modelled by RVM and observed experimentally.  
   - *Source*: [Huang 2016, pp. 7-8].
6. **Pr exponent anomaly in Nu correlation**  
   - *Claim*: The exponent on Pr in the Nu correlation exceeds 1 because the fluid viscosity μf underestimates the effective viscosity μeff in the Prandtl number definition.  
   - *Condition*: When using fluid‑based Pr for rough‑fracture data fitting.  
   - *Source*: [Huang 2016, pp. 5, 7-8].

## Candidate Concepts
- [[enhanced geothermal systems]]
- [[single rough fracture]]
- [[fracture reservoir]]
- [[cubic law]]
- [[hydraulic aperture]]
- [[Poiseuille number]]
- [[Nusselt number]]
- [[Reynolds number]]
- [[Prandtl number]]
- [[relative roughness]]
- [[roughness–viscosity model]]
- [[effective viscosity]]
- [[non-dimensional heating length]]
- [[thermal entrance region]]
- [[boundary layer thickening]]
- [[fracture aperture]]
- [[confining pressure]]
- [[hot dry rock]]

## Candidate Methods
- [[Brazilian method]] (rock splitting)
- [[non-contact laser scanning]] (surface topology)
- [[pressure-driven flow experiment in triaxial cell]]
- [[data reduction for Poiseuille number]]
- [[data reduction for Nusselt number]]
- [[roughness–viscosity model numerical simulation]]
- [[finite difference solution of energy equation in fracture]]
- [[uncertainty analysis per Holman]]

## Connections To Other Work
- **Cubic law validity**: The widely used cubic law (Witherspoon et al. 1980) assumes ideal parallel plates; this study confirms that surface roughness and aperture variation cause significant deviations, underscoring the need for roughness‑dependent corrections [Huang 2016, pp. 1-1, 8-8].
- **Zhao & Tso (1992, 1993)**: Previously reported heat convection experiments in rock fractures and correlated heat transfer coefficient with velocity; the present work extends those findings by explicitly linking heat transfer to relative roughness and confining pressure [Huang 2016, pp. 1-1, 1-2, 8-8].
- **Microchannel roughness studies**: The RVM approach originates from Mala & Li (1999) and Qu et al. (2000) for microtubes and trapezoidal microchannels; Shen et al. (2006) showed that roughness lengthens the thermal entrance region in microchannels, consistent with the present fracture findings [Huang 2016, pp. 5-5, 8-8].
- **EGS reservoir models**: Many large‑scale codes assume a constant heat transfer coefficient (Jiang et al. 2013; Shaik et al. 2011); this work provides velocity‑ and geometry‑dependent correlations that could improve such simulations [Huang 2016, pp. 1-2, 8-8].

## Open Questions
- How do the Po and Nu correlations **scale to larger temperature and roughness ranges** and to non‑granitic rocks? [Huang 2016, pp. 7-8]  
- Can the roughness–viscosity model be calibrated without a priori experimental data for new fractures (e.g., using only surface scans)?  
- Will two‑phase or boiling conditions, avoided here, alter the flow and heat transfer scaling? [Huang 2016, pp. 7-8]  
- How do **natural fracture networks** with multiple intersecting fractures behave compared to a single isolated fracture?  
- Can the observed Pr exponent anomaly be generalised into a modified Prandtl number using a consistent effective viscosity definition?

## Source Coverage
All 7 non‑empty indexed source blocks (covering pages 1–8 of the article) were processed for this wiki entry.  
- Indexed texts: 7  
- Compiled source blocks: 7  
- Coverage by blocks: **100.0%**  
- Coverage by characters: ~100.5% (slight excess due to overlapping block boundaries)  
No external or invented data were used beyond the provided fragments.
