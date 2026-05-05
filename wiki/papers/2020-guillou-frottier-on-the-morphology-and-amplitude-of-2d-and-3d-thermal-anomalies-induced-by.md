---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-guillou-frottier-on-the-morphology-and-amplitude-of-2d-and-3d-thermal-anomalies-induced-by"
title: "On the Morphology and Amplitude of 2D and 3D Thermal Anomalies Induced by Buoyancy-Driven Flow Within and Around Fault Zones."
status: "draft"
source_pdf: "data/papers/On the morphology and amplitude of 2D and 3D thermal anomalies induced by buoyancy-driven flow within and around fault zones.pdf"
collections:
citation: "Guillou-Frottier, Laurent, et al. \"On the Morphology and Amplitude of 2D and 3D Thermal Anomalies Induced by Buoyancy-Driven Flow Within and Around Fault Zones.\" *Solid Earth*, vol. 11, 2020, pp. 1571-1595. doi:10.5194/se-11-1571-2020."
indexed_texts: "23"
indexed_chars: "113211"
nonempty_source_blocks: "23"
compiled_source_blocks: "23"
compiled_source_chars: "113786"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.005079"
coverage_status: "full-index"
source_signature: "180fe5e85a018275058be612e21a505a3de15500"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T01:09:36"
---

# On the Morphology and Amplitude of 2D and 3D Thermal Anomalies Induced by Buoyancy-Driven Flow Within and Around Fault Zones.

## One-line Summary
Numerical modeling of hydrothermal convection in fault zones reveals that thermal anomaly morphology and amplitude are controlled by permeability distribution and fault geometry, with vertical faults producing the largest anomalies.

## Research Question
How do the morphology and amplitude of thermal anomalies induced by buoyancy-driven hydrothermal convection within and around fault zones vary with fault zone properties (e.g., permeability, dip angle, width) and host rock interactions?

## Study Area / Data
The study is based on conceptual numerical models using simplified fault zone geometries embedded in host rock. No specific geographic area is targeted; the models use realistic fluid and rock properties typical of granitic crust [Guillou 2020, pp. 1-2, 3-4].

## Methods
Numerical simulations were performed using the Comsol Multiphysics™ software, coupling Darcy's law, the heat equation, and mass conservation. The study employed both 2D and 3D models. 2D models used constant, depth-dependent, and time-dependent permeability with simplified fluid properties. 3D models used more realistic temperature- and pressure-dependent fluid density and viscosity, with a fixed basal heat flow of 100 mW m⁻². Boundary conditions included fixed temperatures or heat flow at depth and fixed pressure at the surface [Guillou 2020, pp. 3-4, 9-10, 19-21].

## Key Findings
- 2D models show that constant permeability leads to "finger-like" upwellings, while depth-dependent permeability favors "triangular-like" upwellings and a general cooling effect [Guillou 2020, pp. 4-5].
- Instantaneous or gradual increases in permeability transform convective patterns into "bulb-like" geometries, creating large volumes of hot fluid at shallow depths [Guillou 2020, pp. 5-7].
- A phenomenon termed "thermal inheritance" occurs where the initial thermal regime controls the final convective pattern after a permeability change [Guillou 2020, pp. 7-8].
- At high permeabilities, "pulsating plumes" or detached blobs of hot fluid can form [Guillou 2020, pp. 8-9].
- 3D models of fault zones show that thermal anomalies exhibit a "hot air balloon" morphology with constant permeability, evolving to a "funnel-shaped" geometry with depth-dependent permeability [Guillou 2020, pp. 9-11].
- The largest temperature anomalies (up to 80–90°C) are obtained for vertical fault zones. Anomalies greater than 30°C can extend laterally over more than 1 km from the fault boundary [Guillou 2020, pp. 10-11, 18-19].
- The permeability ratio between the fault zone and host rock influences the lateral extent and amplitude of the thermal anomaly [Guillou 2020, pp. 11-13].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| "Thermal inheritance" controls final convective patterns after permeability increase. | [Guillou 2020, pp. 7-8] | 2D models with instantaneous permeability increase from various initial states. | Initial upwelling locations are conserved. |
| Pulsating plumes form at high permeability (~2×10⁻¹⁴ m²). | [Guillou 2020, pp. 8-9] | 2D model with instantaneous permeability increase from depth-dependent to constant high value. | Detached blobs of fluid >300°C ascend with a period of ~240-250 years. |
| Vertical fault zones produce the largest thermal anomalies (up to 80–90°C). | [Guillou 2020, pp. 10-11] | 3D models with depth-dependent permeability and varying dip angles (0°, 15°, 30°, 45°). | Anomalies for inclined faults do not exceed 50–60°C. |
| "Funnel-shaped" thermal anomalies develop with depth-dependent permeability. | [Guillou 2020, pp. 10-11] | 3D models with exponentially decreasing permeability with depth. | Anomaly expands laterally near the surface due to higher shallow permeability. |
| Thermal anomalies >30°C extend laterally >1 km from vertical fault boundaries. | [Guillou 2020, pp. 18-19] | 3D model of a vertical, 100 m wide fault zone. | Based on preliminary 3D results. |
| Permeability ratio (kF/kH) affects anomaly width but not necessarily maximum amplitude. | [Guillou 2020, pp. 11-13] | 3D models comparing ratios of 20 and 50. | Lower ratio (20) resulted in wider anomaly (2.3 km vs 1.4 km) but similar max amplitude (78°C vs 66°C). |

## Limitations
- The 3D models are preliminary and simplified: they do not account for topography, complex fault intersections, or time-dependent permeability [Guillou 2020, pp. 18-19].
- The host rock is assumed homogeneous in most models [Guillou 2020, pp. 18-19].
- Fluid properties are for pure water; salinity effects are not considered [Guillou 2020, pp. 18-19].
- The imposed basal heat flow (100 mW m⁻²) limited maximum temperatures in 3D models to ~214°C, preventing study of supercritical conditions [Guillou 2020, pp. 9-10].
- The study is conceptual and not calibrated to a specific field site [Guillou 2020, pp. 18-19].

## Assumptions / Conditions
- Fluid flow is buoyancy-driven (free convection) within permeable fault zones.
- The system is in a liquid water phase (no vapor) [Guillou 2020, pp. 3-4].
- Initial thermal regime is often purely conductive [Guillou 2020, pp. 9-10].
- Host rock is impermeable in many 3D experiments, except where permeability ratio is tested [Guillou 2020, pp. 11-13].
- Fault zones are simplified as uniform permeable blocks [Guillou 2020, pp. 3-4].

## Key Variables / Parameters
- Fault zone permeability (constant, depth-dependent, time-dependent)
- Fault zone dip angle
- Fault zone width/thickness
- Permeability ratio between fault zone and host rock (kF/kH)
- Basal heat flow
- Fluid properties (density, viscosity as functions of T and P)

## Reusable Claims
- Vertical fault zones produce the largest thermal anomalies (up to 80–90°C) compared to inclined faults [Guillou 2020, pp. 10-11].
- The "thermal inheritance" mechanism means that the initial thermal regime strongly influences the final convective pattern after a change in permeability [Guillou 2020, pp. 7-8].
- Anomalies greater than 30°C can extend laterally over more than 1 km from the boundary of a vertical, 100 m wide fault zone [Guillou 2020, pp. 18-19].
- A sudden increase in permeability can transform "finger-like" or "triangular-like" upwellings into "bulb-like" geometries, creating a large volume of hot fluid at shallow depth [Guillou 2020, pp. 5-7].
- The permeability ratio between a fault zone and its host rock controls the lateral extent of thermal diffusion into the host rock [Guillou 2020, pp. 11-13].

## Candidate Concepts
- [[thermal inheritance]]
- [[pulsating plumes]]
- [[hydrothermal convection]]
- [[fault zone permeability]]
- [[buoyancy-driven flow]]
- [[geothermal reservoir]]

## Candidate Methods
- [[numerical modeling]]
- [[finite-element method]]
- [[Comsol Multiphysics]]
- [[coupled thermo-hydraulic modeling]]

## Connections To Other Work
- The 2D models reproduce and extend the work of Rabinowicz et al. (1998) on hydrothermal convection [Guillou 2020, pp. 3-4].
- 3D benchmark tests were performed against the study of Magri et al. (2017) [Guillou 2020, pp. 9-10, 19-21].
- Findings on fault dip angle effects are consistent with 2D models of Duwiquet et al. (2019) [Guillou 2020, pp. 10-11].
- The concept of pulsating plumes relates to work by Coumou et al. (2006) and Fontaine and Wilcock (2007) [Guillou 2020, pp. 8-9].
- The study discusses implications for geothermal exploration and links to structural controls identified in field studies (e.g., Faulds et al., 2010; Roche et al., 2019) [Guillou 2020, pp. 2-3].

## Open Questions
- How do topography and fault intersections affect the morphology and amplitude of 3D thermal anomalies?
- What are the effects of time-dependent (dynamic) permeability in 3D fault zone models?
- How does fluid salinity (non-pure water) influence the results?
- Can a regime diagram be constructed for 3D convective patterns based on fault width, dip angle, and permeability distribution?
- What is the critical fault permeability above which positive thermal anomalies disappear?

## Source Coverage
All 23 non-empty indexed fragments were processed. The compiled source blocks total 23, with a coverage ratio by blocks of 1.0 and by characters of 1.005079, indicating full-index coverage.
