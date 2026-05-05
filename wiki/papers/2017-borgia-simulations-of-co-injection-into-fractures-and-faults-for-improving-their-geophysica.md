---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2017-borgia-simulations-of-co-injection-into-fractures-and-faults-for-improving-their-geophysica"
title: "Simulations of CO₂ Injection into Fractures and Faults for Improving Their Geophysical Characterization at EGS Sites."
status: "draft"
source_pdf: "data/papers/Simulations of CO2 injection into fractures and faults for improving their geophysical characterization at EGS sites.pdf"
collections:
citation: "Borgia, Andrea, et al. \"Simulations of CO₂ Injection into Fractures and Faults for Improving Their Geophysical Characterization at EGS Sites.\" *Geothermics*, 2017. doi:10.1016/j.geothermics.2017.05.002."
indexed_texts: "7"
indexed_chars: "31556"
nonempty_source_blocks: "7"
compiled_source_blocks: "7"
compiled_source_chars: "31720"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.005197"
coverage_status: "full-index"
source_signature: "90312daad4ecd4126c3597c1b33de5dde6948162"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:33:49"
---

# Simulations of CO₂ Injection into Fractures and Faults for Improving Their Geophysical Characterization at EGS Sites.

## One-line Summary
Numerical simulations show that push-pull injection and production of CO₂ into fractures and faults can create geophysical property contrasts, particularly in seismic stiffness, to improve characterization at Enhanced Geothermal System sites.

## Research Question
Can CO₂ injection in push-pull well tests be used to improve the geophysical identification and characterization of fractures and faults at Enhanced Geothermal System (EGS) sites?

## Study Area / Data
The study uses numerical models of idealized vertical fractures and faults. The fracture model is a single vertical fracture at 1500 m depth with dimensions of 500 m by 500 m and an aperture of 10⁻⁴ m [Borgia 2017, pp. 4-5]. The fault model includes a slip plane, fault gouge, damage zone, and matrix at depths between 2 and 3 km [Borgia 2017, pp. 5-7]. Material properties for the fault model are provided in Table 3 [Borgia 2017, pp. 7-11].

## Methods
Numerical experiments of push-pull injection-production cycling of CO₂ were carried out using TOUGH2 V2.0 with the ECO2N equation-of-state module [Borgia 2017, pp. 1-2, 4-5]. The models simulate non-isothermal, two-phase flow, including capillary pressure and salt precipitation/dissolution [Borgia 2017, pp. 4-5]. For the fracture model, CO₂ was injected at 20°C with a constant overpressure of 2 MPa relative to hydrostatic for 10 days, followed by a 10-day production phase with a depressurization of -4 MPa relative to hydrostatic [Borgia 2017, pp. 4-5]. For the fault model, injection used 2 MPa overpressure for 10 days, and production used 4 MPa underpressure for one day [Borgia 2017, pp. 5-7]. Preliminary geophysical response modeling used a fracture/rock physics model to estimate stiffness tensor variations with CO₂ saturation [Borgia 2017, pp. 7-11].

## Key Findings
- There is a strong difference between injection and production phases, mainly due to CO₂ buoyancy. The CO₂ plume grows laterally and upward during injection, but not all CO₂ is recovered during production [Borgia 2017, pp. 1-2, 11-12].
- Under best recovery conditions, at least 10% of the pore volume remains filled with CO₂ [Borgia 2017, pp. 1-2, 5-7].
- In higher permeability fractures (10⁻¹² m² vs. 10⁻¹³ m²), a proportionally larger CO₂ plume develops, making the push-pull experiment effective for estimating fracture porosity and permeability [Borgia 2017, pp. 5-7, 11-12].
- Across the CO₂ saturation range, the normal stiffness in the horizontal direction perpendicular to the fracture plane (C₁₁) varies by about 15%. It reaches a maximum at around 6% gas saturation and decreases exponentially to a minimum at higher saturations [Borgia 2017, pp. 1-2, 7-11].
- Preliminary seismic modeling shows a measurable difference in surface seismic response between 0% and 50% CO₂ saturation, even with 10% added noise [Borgia 2017, pp. 7-11, 12-13].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| At least 10% of pore volume remains filled with CO₂ after production under best recovery conditions. | [Borgia 2017, pp. 1-2, 5-7] | Push-pull test in a vertical fracture with 2 MPa injection overpressure and 4 MPa production depressurization. | Minimum residual saturation due to buoyancy and capillary trapping. |
| C₁₁ stiffness varies by ~15% across CO₂ saturation range, with a maximum at ~6% saturation. | [Borgia 2017, pp. 1-2, 7-11] | Preliminary geophysical modeling using a fracture/rock physics model. | Indicates potential for seismic detection of CO₂ in fractures. |
| Higher fracture permeability (10⁻¹² m²) leads to a significantly larger CO₂ plume compared to lower permeability (10⁻¹³ m²). | [Borgia 2017, pp. 5-7, 11-12] | Numerical simulations with constant injection pressure. | Demonstrates sensitivity of plume size to permeability, useful for characterization. |
| Buoyancy effects are enhanced by a geothermal gradient, making CO₂ recovery more difficult in fault simulations. | [Borgia 2017, pp. 5-7] | Fault model with 2-3 km depth and 40°C/km geothermal gradient. | Hotter, less dense CO₂ rises into cooler, denser brine. |
| Measurable difference in seismic response between 0% and 50% CO₂ saturation with 10% noise. | [Borgia 2017, pp. 7-11, 12-13] | Preliminary seismic imaging simulation of a fault zone. | Suggests feasibility of time-lapse seismic monitoring. |

## Limitations
- The models use idealized, single vertical fractures or simplified fault geometries that may not capture the full complexity of natural fracture networks [Borgia 2017, pp. 2-4].
- The fracture model assumes no damage zone or matrix adjacent to the fracture [Borgia 2017, pp. 4-5].
- The geophysical response modeling is preliminary and subject to refinement [Borgia 2017, pp. 7-11].
- The simulations do not consider the presence of different fracture sets or their interconnections in the fracture model [Borgia 2017, pp. 4-5].

## Assumptions / Conditions
- Initial conditions are hydrostatic pressure, 200°C temperature, and brine with 0.10 NaCl mass fraction [Borgia 2017, pp. 4-5].
- CO₂ is injected as a cool (20°C), dense phase with 0.99 mass fraction in the gas phase [Borgia 2017, pp. 4-5].
- Supercritical CO₂ tends to remain in the fracture/fault due to brine/CO₂ surface tension, inhibiting entry into the fine-grained matrix [Borgia 2017, pp. 4-5].
- The fault model assumes a closed top boundary and open side/bottom boundaries to fluid flow [Borgia 2017, pp. 5-7].

## Key Variables / Parameters
- Fracture aperture (A): 10⁻⁵ to 10⁻⁴ m [Borgia 2017, pp. 2-4].
- Fracture permeability: 10⁻¹² to 10⁻¹³ m² [Borgia 2017, pp. 4-5, 7-11].
- CO₂ saturation in pores [Borgia 2017, pp. 5-7, 7-11].
- Stiffness tensor elements (C₁₁, C₂₂, C₃₃, C₁₂) [Borgia 2017, pp. 7-11].
- Injection overpressure: 2 MPa [Borgia 2017, pp. 4-5, 5-7].
- Production underpressure: 4 MPa [Borgia 2017, pp. 4-5, 5-7].

## Reusable Claims
- CO₂ injection in push-pull tests can create a geophysical property contrast in fractures and faults, with the normal stiffness (C₁₁) varying by about 15% across the CO₂ saturation range, making it a sensitive indicator for seismic imaging [Borgia 2017, pp. 1-2, 7-11].
- Due to CO₂ buoyancy and capillary trapping, at least 10% of the pore volume in a fracture will retain CO₂ after a production phase, providing a persistent target for time-lapse geophysical monitoring [Borgia 2017, pp. 1-2, 5-7].
- The size of the CO₂ plume developed during injection is highly sensitive to fracture permeability, allowing push-pull experiments to be used for permeability estimation [Borgia 2017, pp. 5-7, 11-12].

## Candidate Concepts
- [[Push-pull well testing]]
- [[Enhanced Geothermal System (EGS)]]
- [[CO₂ as a geophysical contrast agent]]
- [[Fracture and fault characterization]]
- [[Seismic stiffness tensor]]
- [[Buoyancy-driven flow in fractures]]
- [[Capillary trapping of CO₂]]

## Candidate Methods
- [[TOUGH2/ECO2N numerical simulation]]
- [[Time-lapse seismic monitoring]]
- [[Rock physics modeling for stiffness tensor]]
- [[Push-pull injection-production cycling]]

## Connections To Other Work
- The study builds on prior work proposing the use of CO₂ for brightening faults and fractures for seismic imaging [Borgia 2017, pp. 1-2].
- It references earlier numerical simulations of CO₂-EGS in fractured reservoirs with salt precipitation [Borgia 2017, pp. 12-13].
- The fault zone conceptual model is adapted from Gudmundsson et al. (2002) [Borgia 2017, pp. 2-4].
- The preliminary seismic imaging results are based on work by Oldenburg et al. (2016) [Borgia 2017, pp. 12-13].

## Open Questions
- How do the results from these idealized models translate to complex, naturally fractured reservoirs?
- What is the optimal design for integrated CO₂ injection with active seismic, well-logging, and pressure transient monitoring for field implementation?
- How do varying geothermal gradients and in-situ stress fields affect the buoyancy challenge and CO₂ recovery efficiency in different fault orientations?

## Source Coverage
All non-empty indexed fragments were processed. The compilation used 7 source blocks containing 31,556 characters, resulting in a compiled page of 31,720 characters. The coverage ratio by blocks is 1.0 and by characters is 1.005197, indicating full-index coverage.
