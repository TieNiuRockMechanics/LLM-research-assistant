---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-mahzari-characterizing-fluid-flow-paths-in-the-hellisheidi-geothermal-field-using-detailed"
title: "Characterizing Fluid Flow Paths in the Hellisheidi Geothermal Field Using Detailed Fault Mapping and Stress-Dependent Permeability."
status: "draft"
source_pdf: "data/papers/Characterizing fluid flow paths in the Hellisheidi geothermal field using detailed fault mapping and stress-dependent permeability.pdf"
collections:
citation: "Mahzari, Pedram, et al. \"Characterizing Fluid Flow Paths in the Hellisheidi Geothermal Field Using Detailed Fault Mapping and Stress-Dependent Permeability.\" *Geothermics*, vol. 94, 2021, 102127. doi:10.1016/j.geothermics.2021.102127."
indexed_texts: "14"
indexed_chars: "68877"
nonempty_source_blocks: "14"
compiled_source_blocks: "14"
compiled_source_chars: "65453"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.950288"
coverage_status: "full-index"
source_signature: "5d3136aad9abd5cbb19a5b6db9af2f06fe3aef5c"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T00:49:59"
---

# Characterizing Fluid Flow Paths in the Hellisheidi Geothermal Field Using Detailed Fault Mapping and Stress-Dependent Permeability.

## One-line Summary
This study uses detailed fault mapping and stress-dependent permeability in a coupled hydro-thermo-mechanical model to calibrate and validate fluid flow paths in the Hellisheidi geothermal field, demonstrating the critical role of geomechanics in tracer test interpretation.

## Research Question
How can fluid flow paths in the fractured basaltic reservoir of the Hellisheidi geothermal field be accurately characterized using integrated high-resolution fault mapping and stress-dependent permeability to improve the calibration of reservoir models for applications like geothermal energy extraction and CO2 mineral storage?

## Study Area / Data
The study focuses on the Husmuli re-injection zone of the Hellisheidi geothermal field in southwest Iceland, located at a divergent plate boundary [Mahzari 2021, pp. 2-2]. Data includes results from a batch tracer test performed in June 2013, where 100 kg of 1,3,6-NTS tracer was injected into well HN17 and monitored at producing wells HE31, HE48, HE44, and HE33 [Mahzari 2021, pp. 2-4]. Additional data comprises high-resolution fault and fracture mapping from aerial imagery and drone-acquired photogrammetric models [Mahzari 2021, pp. 4-5], laboratory measurements of stress-dependent permeability on basaltic samples [Mahzari 2021, pp. 5-6], and well testing data for initial reservoir parameters [Mahzari 2021, pp. 5-6]. An independent continuous tracer test from well HN16 (part of the CarbFix2 project) was used for validation [Mahzari 2021, pp. 10-11].

## Methods
A fully coupled hydro-thermo-mechanical numerical model (CMG-GEM) was employed using a dual porosity representation [Mahzari 2021, pp. 6-7]. The methodology integrated: 1) High-resolution surface fault mapping to identify primary flow paths (NE-ENE, WNW, and NS trending systems) [Mahzari 2021, pp. 4-5]; 2) Laboratory-derived stress-dependent permeability relationships for basaltic fractures [Mahzari 2021, pp. 5-6]; 3) A 7-layer geological model based on feedzone depths [Mahzari 2021, pp. 6-7]; 4) History matching of the HN17 batch tracer test using an optimization algorithm (CMG's Designed Exploration and Controlled Evolution) to tune 27 parameters (longitudinal/transverse permeability and porosity multipliers for layers and flow paths) [Mahzari 2021, pp. 6-7]. The model was validated by predicting tracer recovery from an independent continuous injection test at well HN16 without further tuning [Mahzari 2021, pp. 10-11].

## Key Findings
- Vertically extended faults are the primary fluid flow paths, but connecting fractures play an important role in transport [Mahzari 2021, pp. 1-2].
- The calibrated model identified upward flow streamlines, indicating vertical communication between geological layers, and highlighted a "sweet spot" for sustainable flow near faults intercepting layers at ~1100 m depth [Mahzari 2021, pp. 1-2, 7-8].
- Inclusion of stress-dependent permeability in history matching significantly improved the calibration of tracer arrival times and concentrations compared to models without geomechanics [Mahzari 2021, pp. 9-10]. Ignoring geomechanics delayed tracer arrivals and reduced recovered concentrations [Mahzari 2021, pp. 9-10].
- The calibrated model successfully predicted tracer recovery from an independent test at well HN16 with a root-mean-square error below 3.55%, validating its predictive capability [Mahzari 2021, pp. 10-11].
- The reservoir compartmentalizes into two main fluid path zones (layers 1-3 and 5-7) with distinct permeability characteristics [Mahzari 2021, pp. 9-10].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Tracer first arrived at HE31 after 14 days and at HE48 after 18 days. | [Mahzari 2021, pp. 2-4] | Batch injection of 100 kg 1,3,6-NTS into HN17 in June 2013. | Indicates fast flow along conductive fracture conduits. |
| Laboratory data shows logarithm of fracture permeability has a linear relationship with effective stress. | [Mahzari 2021, pp. 5-6] | Experiments on basaltic glass samples with three parallel fractures. | Permeability can change by up to 3 orders of magnitude with stress. |
| History matching with geomechanics achieved a root-mean-square error of 0.94% for tracer profiles. | [Mahzari 2021, pp. 7-8] | Model calibrated to HN17 batch tracer test data. | Demonstrates high accuracy of the coupled model. |
| Decoupling geomechanics delayed tracer arrival times and reduced concentrations at HE31 and HE48. | [Mahzari 2021, pp. 9-10] | Re-running the calibrated model without stress-dependent permeability. | Highlights the critical impact of geomechanics on flow path characterization. |
| Predictive model for HN16 continuous tracer test had RMSE < 3.55%. | [Mahzari 2021, pp. 10-11] | No tuning performed; used parameters from HN17 calibration. | Validates the model's predictive capability for independent data. |
| Fracture mapping shows predominance of NE-ENE, WNW, and NS fracture systems. | [Mahzari 2021, pp. 4-5] | Analysis of aerial imagery and drone-acquired outcrop models using FraqPaQ. | Supports the interpreted NE-trending primary fluid flow direction. |

## Limitations
- The model did not capture the double-peak tracer profiles observed in wells HE31 and HE48, which may indicate distinct flow paths or measurement uncertainties [Mahzari 2021, pp. 11-12].
- Cold water injection effects on injectivity and permeability were not considered due to computational costs [Mahzari 2021, pp. 5-6].
- History matching is subject to non-uniqueness and uncertainty [Mahzari 2021, pp. 11-12].
- The stress-dependent permeability relationship was assumed to be isotropic [Mahzari 2021, pp. 5-6].

## Assumptions / Conditions
- The reservoir is represented as a dual-porosity system (fracture network and matrix) [Mahzari 2021, pp. 4-5].
- The relationship between fracture permeability and effective stress is isotropic and based on laboratory data from basaltic samples [Mahzari 2021, pp. 5-6].
- The modelled fluid is single-phase liquid water [Mahzari 2021, pp. 6-7].
- Geochemical interactions are assumed insignificant during the 200-day tracer test period [Mahzari 2021, pp. 6-7].
- Initial effective stress within the reservoir was uniformly set to zero to represent a stress-dependent permeability ratio of 1 [Mahzari 2021, pp. 6-7].
- Geomechanical properties (elastic modulus, Poisson's ratio) for matrix and fracture are identical, based on data from the Krafla region [Mahzari 2021, pp. 6-7].

## Key Variables / Parameters
- Fracture porosity and permeability (horizontal and vertical) [Mahzari 2021, pp. 5-6].
- Stress-dependent permeability multiplier [Mahzari 2021, pp. 5-6].
- Layer thicknesses based on feedzone depths [Mahzari 2021, pp. 6-7].
- Multipliers for longitudinal (horizontal) and transverse (vertical) permeability used in history matching [Mahzari 2021, pp. 6-7].
- Initial fluid pressure (12 MPa at top layer) and base water density (750 kg/m³) [Mahzari 2021, pp. 6-7].
- Fracture spacing (50 m) [Mahzari 2021, pp. 5-6].

## Reusable Claims
- Including stress-dependent permeability in history matching of tracer tests is essential for accurate characterization of fluid flow paths in fractured geothermal reservoirs, as it significantly affects predicted tracer arrival times and concentrations [Mahzari 2021, pp. 9-10].
- Vertically extended faults act as primary fluid conduits in the Hellisheidi field, but smaller fractures connecting these faults are crucial for inter-well communication and vertical flow between geological layers [Mahzari 2021, pp. 1-2, 7-8].
- A calibrated hydro-thermo-mechanical model, validated against an independent tracer test, can provide reliable predictions for reservoir performance and CO2 storage assessments [Mahzari 2021, pp. 10-11].
- The Husmuli reservoir exhibits compartmentalization into two main fluid flow zones (upper and lower), with distinct permeability and porosity characteristics [Mahzari 2021, pp. 9-10].
- Surface fracture density mapping can help identify zones of enhanced subsurface fluid flow, supporting the interpretation of NE-trending flow paths [Mahzari 2021, pp. 4-5].

## Candidate Concepts
- [[Fractured reservoir]]
- [[Stress-dependent permeability]]
- [[Dual porosity model]]
- [[Tracer test]]
- [[Geomechanical coupling]]
- [[Fluid flow path characterization]]
- [[Geothermal reservoir simulation]]
- [[CO2 mineral storage]]

## Candidate Methods
- [[Hydro-thermo-mechanical modelling]]
- [[History matching]]
- [[Fracture pattern analysis]]
- [[Tracer test interpretation]]
- [[Numerical reservoir simulation]]
- [[Optimization algorithm]]

## Connections To Other Work
- The study builds on previous tracer test analyses at Hellisheidi [Norbeck et al., 2018; Doe et al., 2014; Alfredsson et al., 2013] but incorporates geomechanics for improved accuracy [Mahzari 2021, pp. 7-8].
- It is directly relevant to the CarbFix2 CO2 storage project at Hellisheidi, providing insights into flow paths critical for mineral carbonation [Mahzari 2021, pp. 10-11].
- The methodology integrates concepts from structural geology (fault mapping), rock mechanics (stress-dependent permeability), and reservoir engineering (dual porosity modelling) [Mahzari 2021, pp. 1-2].
- The work references and contrasts with conventional hydrodynamic modelling approaches that neglect geomechanics [Mahzari 2021, pp. 2-2].

## Open Questions
- How do long-term geochemical processes (e.g., mineral precipitation/dissolution) interact with stress-dependent permeability to alter flow paths over decades?
- Can the identified flow path compartmentalization and "sweet spots" be generalized to other geothermal fields in similar tectonic settings?
- What is the quantitative impact of cold water injection on permeability evolution, which was excluded from this model?
- How can the non-uniqueness in history matching be further reduced, perhaps by integrating additional data types (e.g., microseismicity, temperature logs)?

## Source Coverage
All 14 non-empty indexed fragments were processed, compiling 65,453 characters out of a total 68,877 indexed characters. This represents a coverage ratio of 0.95 by characters, achieving full-index coverage.
