---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "1980-witherspoon-validity-of-cubic-law-for-fluid-flow-in-a-deformable-rock-fracture"
title: "Validity of Cubic Law for Fluid Flow in a Deformable Rock Fracture."
status: "draft"
source_pdf: "data/papers/1980 - Validity of Cubic Law for fluid flow in a deformable rock fracture.pdf"
collections:
citation: "Witherspoon, P. A., et al. “Validity of Cubic Law for Fluid Flow in a Deformable Rock Fracture.” *Water Resources Research*, vol. 16, no. 6, Dec. 1980, pp. 1016-1024."
indexed_texts: "8"
indexed_chars: "39334"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "38755"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.98528"
coverage_status: "full-index"
source_signature: "38f03ca0a005ea99e4a3b94cd96ff870d47cb56b"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T10:52:18"
---

# Validity of Cubic Law for Fluid Flow in a Deformable Rock Fracture.

## One-line Summary
Laboratory experiments on tension fractures in granite, basalt, and marble demonstrate that the cubic law \( Q/\Delta h = (C/f)(2b)^3 \) is valid for laminar flow in both open and closing fractures under normal stress up to 20 MPa, with aperture ranging from 4 to 250 µm, and deviations from ideal parallel plates are captured by a factor \( f \) ranging from 1.04 to 1.65. [Witherspoon 1980, pp. 1-1, 8-9]

## Research Question
Is the cubic law for fluid flow through a fracture valid when the fracture is closed under normal stress, i.e., when the fracture surfaces are in contact and the aperture is decreasing? [Witherspoon 1980, pp. 1-1]

## Study Area / Data
- Laboratory study using homogeneous intact samples of granite, basalt, and marble from quarries in California.
- Artificially induced tension fractures.
- Two flow geometries: radial (cylindrical samples) and straight (rectangular block).
- Apertures ranging from 250 µm down to a minimum of 4 µm under a normal stress of 20 MPa.
- Fluid: filtered water at ambient temperature.
- Matrix permeability of all rock types negligible relative to fracture flow. [Witherspoon 1980, pp. 2-3, 8-9]

## Methods
- **Fracture creation**: Modified Brazilian loading method to produce a horizontal tension fracture orthogonal to the cylindrical axis (radial) or through a rectangular block (straight). [Witherspoon 1980, pp. 2-3]
- **Loading apparatus**: Riehle testing machine applied axial normal stresses up to 20 MPa; for radial tests, the loading piston could lift the upper half to create open fractures with known aperture. [Witherspoon 1980, pp. 2-3]
- **Deformation measurement**: Three linear variable differential transformers (LVDT) placed 120° apart (radial) or two on one side and one opposite (straight) to detect aperture changes as small as 0.4 µm. Rock deformation was subtracted to obtain net fracture deformation \( \Delta V \) using \( \Delta V = \frac{1}{3}(\Delta V_{t1} + \Delta V_{t2} + \Delta V_{t3}) - \Delta V_r \) (straight) or average \( \Delta V_t \) values (radial). [Witherspoon 1980, pp. 3-5]
- **Aperture determination**: Apparent aperture \( 2b_a = \Delta V_m - \Delta V \) (Fig. 4). True aperture \( 2b = 2b_a + 2b_r \), where \( 2b_r \) is the residual aperture at maximum stress, determined by least‑squares fitting of flow data. [Witherspoon 1980, pp. 3-5]
- **Flow measurement**: Flow rate \( Q \) and hydraulic head difference \( \Delta h \) recorded during loading and unloading cycles. For radial flow, \( C = (2\pi/\ln(r_e/r_w)) (\rho g/12\mu) \); for straight flow, \( C = (W/L)(\rho g/12\mu) \). [Witherspoon 1980, pp. 1-1]
- **Parameter fitting**: Two least‑squares approaches:
  1. Fit exponent \( n \) and \( 2b_r \) in \( Q/\Delta h = C(2b_a + 2b_r)^n \), weighting factor \( \omega_i = \frac{1}{2}|\log(Q/\Delta h)_{i+1} - \log(Q/\Delta h)_{i-1}| \). [Witherspoon 1980, pp. 5-6]
  2. Fix \( n = 3 \) and fit \( f \) and \( 2b_r \) in \( Q/\Delta h = (C/f)(2b_a + 2b_r)^3 \). [Witherspoon 1980, pp. 6-7]
- **Reynolds number**: For radial flow, calculated using the inner radius (maximum value). Friction factor \( \Psi \) and Re were plotted following Lomize’s method. [Witherspoon 1980, pp. 7-8]

## Key Findings
1. The fitted exponent \( n \) in all tests ranged from 3.01 to 3.10, deviating no more than 3 % from the theoretical value of 3 (Table 1). [Witherspoon 1980, pp. 5-6]
2. When \( n \) was fixed at 3, the factor \( f \) (accounting for surface roughness and contact) varied from 1.04 to 1.65 across all samples and runs (Table 2). [Witherspoon 1980, pp. 6-7]
3. The cubic law \( Q/\Delta h = (C/f)(2b)^3 \) holds for both open (no contact) and closed (surfaces in contact) fractures, regardless of rock type (granite, basalt, marble). [Witherspoon 1980, pp. 7-8]
4. Permeability is uniquely defined by fracture aperture and is independent of loading path or stress history; repeated loading cycles did not alter the permeability–aperture relationship. [Witherspoon 1980, pp. 5-6, 8-9]
5. The factor \( f \) generally decreased with successive runs (e.g., from 1.21 to 1.04 in granite straight flow), suggesting progressive mating of fracture surfaces during cyclic loading. [Witherspoon 1980, pp. 6-7, 8]
6. The cubic law remained valid down to apertures as small as 4 µm and for normal stresses up to 20 MPa. [Witherspoon 1980, pp. 8-9]
7. The strong dependence of flow on \( (2b)^3 \) means that a slight change in aperture dominates any other change in flow‑field geometry; no discernible shift in the correlation occurs when passing from an open to a closing fracture. [Witherspoon 1980, pp. 8-9]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Fitted exponent \( n\): granite straight‑flow Run 1 = 3.04, Run 2 = 3.03, Run 3 = 3.01; granite radial Run 1 = 3.07, Run 2 = 3.04, Run 3 = 3.06; basalt radial Run 1 = 3.08, Run 2 = 3.10, Run 3 = 3.02; marble radial Run 1 = 3.06, Run 2 = 3.06, Run 3 = 3.01 | Table 1 [Witherspoon 1980, pp. 5-6] | Cyclic loading/unloading, \( \Delta h\) = 20 m (Runs 1,2) and 0.5 m (Run 3), ambient temperature | All \( n\) > 3, deviation ≤ 3 %; supports fixing \( n = 3\) and introducing \( f\) |
| Factor \( f\) and residual aperture \( 2b_r\) (fitted vs. calculated from cubic law): granite straight‑flow \( f = 1.21–1.04\), \( 2b_r\) = 8.8–11.6 µm; granite radial \( f = 1.49–1.29\), \( 2b_r\) = 4.8–12.4 µm; basalt radial \( f = 1.65–1.10\), \( 2b_r\) = 9.8–10.4 µm; marble radial \( f = 1.36–1.05\), \( 2b_r\) = 2.2–18.2 µm | Table 2 [Witherspoon 1980, pp. 6-7] | Fixed \( n = 3\), same runs as above | \( f\) > 1 as predicted; fitted \( 2b_r\) close to directly calculated values; \( f\) decreases with repeated cycles |
| Straight‑flow granite: data follow \( \Psi \cdot \text{Re} = 96f\) for \( f = 1.0\) and \( f = 1.21\) over a wide range of Re; radial‑flow granite: similar agreement with \( f = 1.0\) and \( f = 1.49\) | Figures 5, 6 [Witherspoon 1980, pp. 7-8] | Loading and unloading data; run 3 unloading includes open‑fracture points | Good agreement with cubic law whether fracture open or closed; radial flow shows larger \( f\) |
| Basalt radial flow follows cubic law with \( f = 1.65\) (dashed line); marble radial flow shows deviations at low flow rates (<10 µm aperture) but overall agreement with \( f = 1.36\) and \( f = 1.05\) | Figures 7, 8 [Witherspoon 1980, pp. 7-8] | Basalt: chip around center hole may have affected flow; marble: low‑flow deviations in runs 1, 2, change in initial mating between runs 2 and 3 | Cubic law robust despite experimental difficulties |
| Permeability is independent of loading path; hysteresis and permanent deformation present but do not alter the flow‑aperture relationship | [Witherspoon 1980, pp. 5-6] | Cyclic loading up to 20 MPa | \( Q/\Delta h\) vs. aperture relation unchanged across loading/unloading cycles |

## Limitations
- Investigation limited to normal stress; shear deformation was not studied. [Witherspoon 1980, pp. 8-9]
- Experiments conducted at room temperature; thermal expansion effects on aperture were not examined. [Witherspoon 1980, pp. 8-9]
- Potential size effect on measured hydraulic properties (noted in Witherspoon et al. 1979) was not addressed. [Witherspoon 1980, pp. 8-9]
- Only three rock types and one artificially induced tension fracture per sample were used; natural fractures with weathering or gouge may behave differently. [Witherspoon 1980, pp. 2-3]
- Marble data exhibited deviations at apertures below 10 µm and a shift in residual aperture between runs, indicating sensitivity to subtle changes in surface mating. [Witherspoon 1980, pp. 7-8]
- The factor \( f\) is empirical and may depend on stress level and fracture history; its physical interpretation as a roughness factor needs further validation. [Witherspoon 1980, pp. 6-7]
- Flow was laminar (Reynolds numbers below the critical value of ~2300–2400); turbulent flow or inertial effects were not considered. [Witherspoon 1980, pp. 1-2]
- Residual aperture \( 2b_r\) was assumed constant for each run; real contact area and its evolution were not directly measured. [Witherspoon 1980, pp. 3-5, 8-9]

## Assumptions / Conditions
- Laminar, steady, isothermal flow of a viscous incompressible fluid. [Witherspoon 1980, pp. 1-1]
- The fracture is idealized as parallel planar plates for the derivation of the cubic law. [Witherspoon 1980, pp. 1-1]
- Darcy’s law holds (\( Q \propto \Delta h\)) under the experimental conditions. [Witherspoon 1980, pp. 5-6]
- For a closed fracture, the aperture is the sum of an apparent aperture (from deformation measurements) and a residual aperture that accounts for flow at high stress. [Witherspoon 1980, pp. 3-5]
- The cubic law (with \( n = 3\)) is valid for all apertures, allowing direct estimation of residual aperture for comparison. [Witherspoon 1980, pp. 5-6]
- Deviations from ideal parallel plates are grouped into a multiplicative factor \( f \) such that \( Q/\Delta h = (C/f)(2b)^3\); this factor subsumes roughness and contact effects. [Witherspoon 1980, pp. 1-2, 6-7]
- The dynamic process of fracture closure under normal stress is controlled by the strength of contacting asperities; these contacts maintain flow space while supporting load, and the resulting overall geometry can still be characterised by a single effective aperture \( 2b\). [Witherspoon 1980, pp. 8-9]

## Key Variables / Parameters
- \( Q \) – flow rate (L³/T)
- \( \Delta h \) – difference in hydraulic head (L)
- \( 2b \) – true fracture aperture (L), \( 2b = 2b_a + 2b_r \)
- \( 2b_a \) – apparent aperture from deformation measurements (L)
- \( 2b_r \) – residual aperture at maximum normal stress (L)
- \( C \) – geometric and fluid property constant; for radial flow \( C = (2\pi/\ln(r_e/r_w))(\rho g/12\mu) \), for straight flow \( C = (W/L)(\rho g/12\mu) \)
- \( f \) – fracture surface characteristic factor (dimensionless), \( f \ge 1 \), accounting for roughness and contact
- \( n \) – exponent in fracture flow law (dimensionless), ideally 3
- \( \sigma_e \) – axial normal stress (M/LT²)
- \( \Delta V \) – net fracture deformation (L)
- \( \Delta V_m \) – maximum fracture deformation (L)
- \( \Delta V_r \) – rock deformation (L)
- \( \Delta V_t \) – total deformation measured by LVDT (L)
- \( \text{Re} \) – Reynolds number
- \( \Psi \) – friction factor
- Rock type (granite, basalt, marble) – investigated but found not to influence the validity of the cubic law.

## Reusable Claims
1. **Validity of cubic law for closed fractures** – For laminar flow in a deformable rock fracture under normal stress up to 20 MPa, the relationship \( Q/\Delta h = (C/f)(2b)^3 \) holds for apertures from 4 µm to 250 µm, regardless of whether the fracture is open (no contact) or closed (surfaces in contact). [Witherspoon 1980, pp. 7-9]  
   *Conditions*: laminar flow, no shear movement, ambient temperature, homogeneous crystalline rock.

2. **Aperture‑dominance over stress history** – Fracture permeability is uniquely defined by the aperture \( 2b \) and is independent of the loading path, number of loading cycles, or stress history. Hysteresis and permanent deformation do not alter the \( Q/\Delta h \) – \( 2b \) relationship. [Witherspoon 1980, pp. 5-6, 8-9]

3. **Rock‑type independence** – The cubic law’s validity does not depend on rock type (tested for granite, basalt, marble). [Witherspoon 1980, pp. 8-9]

4. **Correction factor for roughness/contact** – Deviations from ideal parallel‑plate behavior in a closing fracture can be incorporated by replacing \( C \) with \( C/f \), where \( f \) varies between 1.04 and 1.65 under the tested conditions. [Witherspoon 1980, pp. 6-7, 8-9]

5. **Aperture sensitivity** – Because flow depends on \( (2b)^3 \), a small change in aperture dominates any other change in flow‑field geometry; this explains why no detectable shift occurs when moving from open to closing fracture conditions. [Witherspoon 1980, pp. 8-9]

6. **Fitted exponent near theoretical** – When the exponent \( n \) is treated as a free parameter, least‑squares fits give \( n \) values of 3.01–3.10, confirming that \( n = 3 \) is appropriate. [Witherspoon 1980, pp. 5-6]

7. **Residual aperture determination** – The residual aperture at maximum normal stress can be reliably estimated by directly applying the cubic law to the low‑flow data; fitted values match this direct calculation closely. [Witherspoon 1980, pp. 5-6]

8. **Progressive mating** – The factor \( f \) tends to decrease with repeated loading cycles, indicating progressive mating of fracture surfaces. [Witherspoon 1980, pp. 6-7]

## Candidate Concepts
- [[Cubic Law]]
- [[Deformable Rock Fracture]]
- [[Fracture Aperture]]
- [[Residual Aperture]]
- [[Apparent Aperture]]
- [[Fracture Surface Roughness Factor]]
- [[Parallel Plate Model]]
- [[Laminar Flow in Fractures]]
- [[Normal Stress and Fracture Closure]]
- [[Asperity Contact]]
- [[Permeability–Aperture Relationship]]
- [[Friction Factor in Fracture Flow]]
- [[Reynolds Number for Fracture Flow]]
- [[Cyclic Loading and Fracture Hydraulics]]

## Candidate Methods
- [[Brazilian Loading Method for Tension Fracture Creation]]
- [[Least Squares Fit for Fracture Flow Parameters]]
- [[Radial Flow Test in Rock Fracture]]
- [[Straight Flow Test in Rock Fracture]]
- [[LVDT Measurement of Fracture Deformation]]
- [[Residual Aperture Estimation by Flow Fitting]]
- [[Cyclic Loading–Unloading Test for Fracture Permeability]]
- [[Reynolds Number Calculation for Fracture Flow]]

## Connections To Other Work
- Earlier workers (Boussinesq, Lomize, Romm, Louis, Snow) derived the cubic law for open, parallel‑plate fractures. [Witherspoon 1980, pp. 1-1]
- Lomize (1951) introduced the roughness factor \( \Psi \cdot \text{Re} = 96f \) with \( f = 1 + \epsilon/(2b) \) for \( \epsilon/2b > 0.065 \); the present study uses a similar factor \( f \) to account for deviations. [Witherspoon 1980, pp. 1-2]
- Romm (1966) validated the cubic law down to 0.2 µm aperture for fine and superfine open fractures. [Witherspoon 1980, pp. 1-2]
- Sharp (1970) and Sharp & Maini (1972) argued for an exponent of 2, but Gale (1975) showed the cubic law holds when using the actual aperture. The present work confirms Gale’s view. [Witherspoon 1980, pp. 1-2]
- Witherspoon et al. (1979) observed a potential size‑effect in hydraulic property determination, a topic relevant to how fracture contact area evolves at different scales. [Witherspoon 1980, pp. 8-9]

## Open Questions
- How does the cubic law behave when both normal and shear stresses act on the fracture? [Witherspoon 1980, pp. 8-9]
- What is the physical nature of contact area evolution and how does it influence flow at higher stresses? [Witherspoon 1980, pp. 8-9]
- How do thermal expansion and elevated temperatures affect aperture and thus flow in a deforming fracture? [Witherspoon 1980, pp. 8-9]
- What is the role of fracture size (scale effect) on the hydraulic properties of a deforming fracture? [Witherspoon 1980, pp. 8-9]
- Can the factor \( f \) be predicted from measurable surface roughness parameters, and how does it change during shear? [Witherspoon 1980, pp. 6-7]
- Are the results transferable to natural, weathered fractures or those with gouge material? [Witherspoon 1980, pp. 2-3]

## Source Coverage
All indexed fragments (8 source blocks) were processed. The index covers the full paper pages 1–9, including the abstract, introduction, laboratory procedures, discussion of results, conclusions, and notation. Coverage ratio by blocks: 1.0; by characters: 0.98528. All non‑empty source blocks were compiled into this page. Source signature: 38f03ca0a005ea99e4a3b94cd96ff870d47cb56b.
