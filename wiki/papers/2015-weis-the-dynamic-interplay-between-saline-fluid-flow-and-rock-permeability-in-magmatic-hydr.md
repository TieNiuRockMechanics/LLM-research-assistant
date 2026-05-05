---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2015-weis-the-dynamic-interplay-between-saline-fluid-flow-and-rock-permeability-in-magmatic-hydr"
title: "The Dynamic Interplay between Saline Fluid Flow and Rock Permeability in Magmatic-Hydrothermal Systems."
status: "draft"
source_pdf: "data/papers/The dynamic interplay between saline fluid flow and rock permeability in magmatic-hydrothermal systems.pdf"
collections:
citation: "Weis, P. “The Dynamic Interplay between Saline Fluid Flow and Rock Permeability in Magmatic-Hydrothermal Systems.” *Geofluids*, vol. 15, 2015, pp. 350–371. doi:10.1111/gfl.12100. Accessed 2026."
indexed_texts: "21"
indexed_chars: "102000"
nonempty_source_blocks: "21"
compiled_source_blocks: "21"
compiled_source_chars: "102456"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004471"
coverage_status: "full-index"
source_signature: "63431f8ad6cb823f1fc2edea6eafa8504b84cb17"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:57:15"
---

# The Dynamic Interplay between Saline Fluid Flow and Rock Permeability in Magmatic-Hydrothermal Systems.

## One-line Summary
Numerical simulations show that the interplay between saline fluid flow and dynamic rock permeability self-organizes magmatic-hydrothermal systems into a hydrological divide, controlling ore formation and geothermal processes.

## Research Question
How does the dynamic interplay between saline fluid flow and rock permeability control the evolution of magmatic-hydrothermal systems, and what are the implications for the formation of porphyry copper and epithermal gold deposits, as well as for active geothermal and volcanic systems?

## Study Area / Data
The study uses numerical simulations rather than direct field data. The model setup is inspired by geological observations from porphyry copper deposits (e.g., Yerington Batholith) and active systems like the Taupo Volcanic Zone (TVZ). The modeling domain represents a 2D section of the upper continental crust with a magma chamber emplaced at 5 km depth [Weis 2015, pp. 6-8].

## Methods
The study employs numerical simulations using the Complex Systems Modeling Platform (CSMP++) with a control volume finite element method [Weis 2015, pp. 6-8]. The model simulates multiphase flow of compressible, variably miscible H2O–NaCl fluids, incorporating a thermodynamic model for phase relations and fluid properties [Weis 2015, pp. 3-4]. A dynamic permeability model is implemented, which includes depth-dependent permeability profiles, temperature-dependent permeability closure at the brittle-ductile transition, fluid pressure-dependent permeability, and hydraulic fracturing [Weis 2015, pp. 4-5].

## Key Findings
1.  The system self-organizes into a hydrological divide separating an inner domain of ascending magmatic fluids under near-lithostatic pressures from an outer domain of convecting meteoric fluids under near-hydrostatic pressures [Weis 2015, pp. 1-2].
2.  Porphyry copper ore shells form at the stable temperature-pressure front of this hydrological divide [Weis 2015, pp. 17-18].
3.  Magmatic fluids ascend in overpressure-permeability waves due to episodic hydraulic fracturing in the nominally ductile zone [Weis 2015, pp. 2-3].
4.  The permeability range influences the shape of the ore body; higher permeabilities lead to narrower, vertically extended ore shells [Weis 2015, pp. 17-18].
5.  Salinity (NaCl) enhances hydraulic fracturing and moves the hydrological divide to shallower depths compared to pure water [Weis 2015, pp. 13-14].
6.  Volcano topography reverses meteoric convection, leading to discharge at distances up to 7 km from the volcanic center [Weis 2015, pp. 14-17].
7.  The hydrological divide provides a mechanism to transport magmatic salt through the crust [Weis 2015, pp. 17-18].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Permeability ranges between 10⁻²² and 10⁻¹³ m² are used, incorporating depth-dependent profiles for tectonically active crust. | [Weis 2015, pp. 1-2] | Dynamic permeability model. | Background permeability follows log k = -14 - 3.2 log z (k in m², z in km). |
| The brittle-ductile transition is assumed to start at 360°C, where permeability decreases log-linearly to 10⁻²² m² at 500°C. | [Weis 2015, pp. 4-5] | Temperature-dependent permeability. | Based on the approach of Hayba & Ingebritsen (1997). |
| Hydraulic fracturing temporarily increases permeability by up to two orders of magnitude when fluid pressure exceeds the stress-state-dependent failure criterion. | [Weis 2015, pp. 5-6] | Fluid pressure > failure pressure. | Permeability increase is incremental and proportional to overpressure squared (k²-dependence). |
| Porphyry copper ore shells form at a stable temperature-pressure front at the hydrological divide. | [Weis 2015, pp. 17-18] | Simulation results. | Matches observed copper ore grades and vein sequences in porphyry deposits. |
| With a volcano topography, meteoric convection reverses, causing discharge at epithermal conditions up to 7 km from the center. | [Weis 2015, pp. 14-17] | Simulation with volcano. | Topography-driven flow alters the hydrological divide's shape. |
| The ore-forming event is predicted to last between 50,000 and 100,000 years. | [Weis 2015, pp. 17-18] | Simulation timescale. | Consistent with high-precision geochronology and earlier modeling studies. |

## Limitations
1.  The dynamic permeability model uses simplifications, such as a constant, homogeneous near-critical stress state for the brittle crust and assumes rdiff = 0 in the ductile zone [Weis 2015, pp. 4-5].
2.  The model does not explicitly account for spatial and temporal variations in stress field, strain rate, or pre-existing fractures and fault zones [Weis 2015, pp. 18-19].
3.  Geochemical feedbacks (e.g., quartz precipitation/dissolution altering porosity and permeability) are not explicitly modeled, except for halite precipitation [Weis 2015, pp. 18-19].
4.  The parameterization of hydraulic fracturing is an ad hoc approach mimicking the effect rather than resolving the actual rock mechanics process [Weis 2015, pp. 5-6].
5.  The model assumes a constant host rock porosity of 0.05 [Weis 2015, pp. 6-8].

## Assumptions / Conditions
1.  Permeability follows a depth-dependent profile characteristic for tectonically active crust (log k = -14 - 3.2 log z) [Weis 2015, pp. 4-5].
2.  The brittle crust is in a near-critically stressed state under normal-faulting conditions, with a differential stress of 5 MPa above hydrostatic [Weis 2015, pp. 4-5].
3.  The brittle-ductile transition starts at 360°C, with permeability decreasing to 10⁻²² m² at 500°C [Weis 2015, pp. 4-5].
4.  Fluid and rock are in local thermal equilibrium [Weis 2015, pp. 3-4].
5.  Magmatic fluids are expelled with a salinity of 10 wt% NaCl and a temperature of 700°C [Weis 2015, pp. 8-9].
6.  The magma chamber has an initial temperature of 900°C and a solidus temperature of 700°C [Weis 2015, pp. 6-8].

## Key Variables / Parameters
-   **Permeability (k):** Dynamic parameter ranging from 10⁻²² to 10⁻¹³ m², controlled by depth, temperature, and fluid pressure.
-   **Fluid Pressure (p):** Ranges from near-hydrostatic to near-lithostatic, driving hydraulic fracturing.
-   **Temperature (T):** Controls the brittle-ductile transition (360–500°C) and fluid phase separation.
-   **Salinity (X_NaCl):** Mass fraction of NaCl, affecting fluid density, viscosity, and phase behavior.
-   **Failure Criterion (p_fail):** Stress-state-dependent pressure for brittle shear or extension failure, calculated from Eqs. 9, 11, or 12 [Weis 2015, pp. 4-5].
-   **Porosity (φ):** Constant at 0.05 in the model [Weis 2015, pp. 6-8].

## Reusable Claims
1.  **Condition:** In magmatic-hydrothermal systems with focused magmatic fluid expulsion. **Claim:** The system self-organizes into a hydrological divide, separating an inner, high-temperature, near-lithostatically pressured domain from an outer, cooler, near-hydrostatically pressured domain. **Limitation:** Based on numerical simulations with specific permeability and stress assumptions.
2.  **Condition:** For porphyry copper formation. **Claim:** Ore shells form at the stable temperature-pressure front of the hydrological divide, where conditions favor copper precipitation (350–450°C). **Limitation:** The model uses a proxy for copper precipitation based on temperature change.
3.  **Condition:** In systems with saline (H2O–NaCl) magmatic fluids. **Claim:** Salinity enhances hydraulic fracturing intensity and moves the hydrological divide to shallower crustal levels compared to pure water systems. **Limitation:** The effect is demonstrated through comparative simulations.
4.  **Condition:** In tectonic settings with hydrous magmatism. **Claim:** The hydrological divide can separate the base of high-enthalpy geothermal systems from the magma chamber by several kilometers vertically. **Limitation:** Contrasts with settings of anhydrous magmatism where the base may be closer.

## Candidate Concepts
-   [[hydrological divide]]
-   [[brittle-ductile transition]]
-   [[hydraulic fracturing]]
-   [[overpressure-permeability waves]]
-   [[porphyry copper deposit]]
-   [[epithermal gold deposit]]
-   [[dynamic permeability]]
-   [[phase separation]]
-   [[magmatic-hydrothermal system]]

## Candidate Methods
-   [[numerical simulation]]
-   [[dynamic permeability modeling]]
-   [[multiphase flow modeling]]
-   [[control volume finite element method]]
-   [[thermodynamic modeling (H2O-NaCl)]]

## Connections To Other Work
This study builds directly on previous numerical simulations by Weis et al. (2012) that first identified the hydrological divide mechanism for porphyry copper formation [Weis 2015, pp. 2-3]. It connects to broader concepts of dynamic crustal permeability (e.g., Manning & Ingebritsen 1999; Cox 2005, 2010) and wave-like fluid flow in the crust (e.g., Sibson et al. 1988; Connolly & Podladchikov 2004). The findings relate to active geothermal systems like the Taupo Volcanic Zone (Bertrand et al. 2012) and the search for supercritical geothermal resources (e.g., Fridleifsson & Elders 2005). The work also discusses implications for excess degassing at volcanoes (Shinohara 2008) and episodic ground deformation (Bodnar et al. 2007).

## Open Questions
1.  How do pre-existing fractures, fault zones, and spatially/temporally varying stress fields affect the hydrological divide and ore formation?
2.  What are the quantitative effects of geochemical feedbacks (e.g., quartz precipitation, fluid-rock reaction) on permeability evolution and system dynamics?
3.  How does the model apply to different tectonic settings (e.g., strike-slip regimes) or crustal compositions with varying permeability profiles?
4.  Can the mechanism for supercritical geothermal resources in hydrous magmatic settings be confirmed with direct drilling evidence?

## Source Coverage
All 21 non-empty indexed fragments were processed. The compiled source blocks total 21, with a compiled character count of 102,456 against an indexed character count of 102,000, resulting in a coverage ratio by characters of 1.004471. The coverage status is "full-index".
