---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2017-yang-failure-mechanical-behavior-of-pre-holed-granite-specimens-after-elevated-temperature"
title: "Failure Mechanical Behavior of Pre-Holed Granite Specimens after Elevated Temperature Treatment by Particle Flow Code."
status: "draft"
source_pdf: "data/papers/Failure-mechanical-behavior-of-pre-holed-granite-specimens-after_2018_Geothe.pdf"
collections:
citation: "Yang, Sheng-Qi, et al. \"Failure Mechanical Behavior of Pre-Holed Granite Specimens after Elevated Temperature Treatment by Particle Flow Code.\" *Geothermics*, doi:10.1016/j.geothermics.2017.10.018."
indexed_texts: "11"
indexed_chars: "52896"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "53134"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004499"
coverage_status: "full-index"
source_signature: "dce3fe140077807d0c90c53aaae40899ce3f6ddf"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:49:10"
---

# Failure Mechanical Behavior of Pre-Holed Granite Specimens after Elevated Temperature Treatment by Particle Flow Code.

## One-line Summary
This study uses a PFC 2D cluster model to numerically investigate the mechanical behavior and crack coalescence mechanisms of granite specimens containing pre-existing holes after treatment at various elevated temperatures.

## Research Question
How do elevated temperature treatments and the geometry of pre-existing holes (ligament angle) influence the mechanical properties, failure modes, and meso-scale crack evolution mechanisms of granite?

## Study Area / Data
The study uses numerical specimens modeled in PFC 2D to simulate granite from Quanzhou City, Fujian Province, China [Yang 2017, pp. 2-3]. The granite has a crystalline structure with mineral components of Calcite (42.9%), Illite (11.4%), Biotite (23%), and Quartz (22.7%) [Yang 2017, pp. 2-3]. The numerical specimens contain three pre-existing holes with a diameter of 10.5 mm and a fixed bridge length of 18 mm [Yang 2017, pp. 3-4]. The ligament angle (β) between the holes was set to 0° (H-model), 45° (D-model), and 90° (V-model) [Yang 2017, pp. 3-4].

## Methods
The research employed the cluster model in the two-dimensional Particle Flow Code (PFC 2D) [Yang 2017, pp. 1-1]. Different mineral grains were simulated by clusters with distinct linear thermal expansion coefficients [Yang 2017, pp. 1-1]. The phase transition of quartz at 573 °C was simulated by a radius expansion of 1.0046 [Yang 2017, pp. 2-3]. Micro-parameters were calibrated using a trial-and-error method to match experimental stress-strain curves, peak strength, elastic modulus, and failure modes [Yang 2017, pp. 2-3]. Specimens were heated uniformly in steps of 5 °C until equilibrium [Yang 2017, pp. 2-3]. Stress analysis in the ligament region used measurement circles to compute average stress [Yang 2017, pp. 11-12].

## Key Findings
1.  The mechanical property variation (peak strength, elastic modulus, peak strain) with temperature can be divided into three phases: Phase 1 (T ≤ 150 °C) where properties are almost constant; Phase 2 (150 °C ≤ T ≤ 600 °C) where peak strength and modulus decrease significantly while peak strain increases; Phase 3 (600 °C ≤ T ≤ 900 °C) where strength and modulus decrease gradually and peak strain increases [Yang 2017, pp. 2-3, pp. 3-4].
2.  The ligament angle (β) significantly affects crack evolution. Cracks initiate more easily in the D-model (β=45°) than in the H-model (β=0°) or V-model (β=90°) [Yang 2017, pp. 7-11].
3.  The ligament concentrates compressive stress in the H-model, shear stress in the D-model, and has almost no force concentration in the V-model [Yang 2017, pp. 12-13].
4.  The first crack coalescing between holes is a shear crack regardless of ligament angle, and the maximum shear stress values decrease with increasing temperature [Yang 2017, pp. 12-13, pp. 13-14].
5.  High-temperature treatment leads to more scattered micro-crack distributions due to tensile force concentration at temperature-induced cracks [Yang 2017, pp. 11-12].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Mechanical properties exhibit a three-phase variation with temperature. | [Yang 2017, pp. 2-3, pp. 3-4] | Intact and pre-holed granite specimens under uniaxial compression after treatment at T = 25, 150, 300, 450, 600, 750, 900 °C. | Phase 1: T ≤ 150 °C; Phase 2: 150 °C ≤ T ≤ 600 °C; Phase 3: 600 °C ≤ T ≤ 900 °C. |
| Ligament angle (β) significantly influences crack initiation and coalescence. | [Yang 2017, pp. 7-11] | Granite specimens with three holes (β = 0°, 45°, 90°) at room temperature and after 450 °C treatment. | Cracks initiate more easily in the D-model (β=45°). |
| The ligament concentrates different stress types based on its angle. | [Yang 2017, pp. 12-13] | Pre-holed specimens at room temperature. | H-model: compressive stress; D-model: shear stress; V-model: minimal force concentration. |
| The first crack coalescing between holes is a shear crack. | [Yang 2017, pp. 12-13, pp. 13-14] | Pre-holed specimens at room temperature and after high-temperature treatment. | Observed for all ligament angles (β = 0°, 45°, 90°). |
| High temperature causes more scattered micro-cracks. | [Yang 2017, pp. 11-12] | Pre-holed specimens after 450 °C treatment compared to room temperature. | Attributed to tensile force concentration at temperature-induced cracks. |

## Limitations
1.  The numerical simulation method cannot reproduce the phenomenon where peak strength first increases and then decreases with increasing temperature [Yang 2017, pp. 13-14].
2.  The model does not consider micro-crack closure, dehydration, or mineral recombination processes that occur at high temperatures [Yang 2017, pp. 13-14].
3.  The study is limited to uniaxial compression and does not incorporate coupled thermo-hydro-mechanical (THM) processes relevant to nuclear waste repository design [Yang 2017, pp. 13-14].

## Assumptions / Conditions
1.  Thermal strains are produced by modifying particle radius and parallel bond force based on linear thermal expansion coefficients [Yang 2017, pp. 2-3].
2.  The phase transition of quartz at 573 °C is simulated as a discrete radius expansion (1.0046) and shrinkage (0.9954) [Yang 2017, pp. 2-3].
3.  The granite is treated as a heterogeneous material composed of distinct mineral clusters with different thermal expansion properties [Yang 2017, pp. 1-1, pp. 2-3].

## Key Variables / Parameters
-   **Temperature (T):** 25, 150, 300, 450, 600, 750, 900 °C [Yang 2017, pp. 1-1].
-   **Ligament Angle (β):** 0° (H-model), 45° (D-model), 90° (V-model) [Yang 2017, pp. 3-4].
-   **Mineral Thermal Expansion Coefficients:** Calcite: 14.0 × 10⁻⁶ K⁻¹, Illite: 9.13 × 10⁻⁶ K⁻¹, Biotite: 3.0 × 10⁻⁶ K⁻¹, Quartz: 24.30 × 10⁻⁶ K⁻¹ [Yang 2017, pp. 2-3].
-   **Micro-parameters:** Effective Young's modulus (25 GPa), normal/shear stiffness ratio (1.5), intra-cluster bond strengths (180±30 MPa normal, 280±60 MPa shear), inter-cluster bond strengths (90±20 MPa normal, 140±30 MPa shear) [Yang 2017, pp. 2-3].

## Reusable Claims
1.  **Condition:** For granite under uniaxial compression after thermal treatment up to 900 °C. **Claim:** Mechanical properties (peak strength, elastic modulus) follow a three-phase degradation pattern with temperature, showing significant reduction between 150 °C and 600 °C [Yang 2017, pp. 2-3, pp. 3-4].
2.  **Condition:** For granite containing multiple pre-existing holes. **Claim:** The ligament angle between holes controls the stress concentration mechanism (compression, shear, or minimal) and consequently the ease of crack initiation and coalescence mode [Yang 2017, pp. 12-13].
3.  **Condition:** For pre-holed granite after high-temperature treatment. **Claim:** The first crack coalescing between holes is consistently a shear crack, and its maximum shear stress magnitude decreases with increasing treatment temperature [Yang 2017, pp. 12-13, pp. 13-14].

## Candidate Concepts
-   [[Particle Flow Code]]
-   [[cluster model]]
-   [[thermal cracking]]
-   [[crack coalescence]]
-   [[ligament angle]]
-   [[thermal damage]]
-   [[deep geological disposal]]
-   [[granite]]

## Candidate Methods
-   [[numerical simulation]]
-   [[PFC 2D]]
-   [[discrete element method]]
-   [[micro-parameter calibration]]
-   [[measurement circle stress analysis]]

## Connections To Other Work
The study builds upon and validates its numerical approach against experimental work by Huang et al. (2017b) on pre-holed granite after high-temperature treatment [Yang 2017, pp. 1-2, pp. 3-4]. It also references prior numerical studies on rock with holes by Tang et al. (2005) and Wong and Lin (2015) [Yang 2017, pp. 1-2]. The research context is set within the broader field of coupled thermo-hydro-mechanical (THM) issues for nuclear waste repositories in granite [Yang 2017, pp. 1-1, pp. 13-14].

## Open Questions
1.  How can the numerical model be improved to simulate the initial increase in peak strength observed experimentally at lower temperatures?
2.  What is the effect of incorporating coupled thermo-hydro-mechanical (THM) processes on the failure behavior of pre-holed granite?
3.  How do micro-crack closure, dehydration, and mineral recombination at high temperatures influence the meso-scale failure mechanisms?

## Source Coverage
All 11 non-empty indexed fragments were processed. The compiled source blocks total 11, with a compiled character count of 53,134 against an indexed character count of 52,896, yielding a coverage ratio of 1.004. The coverage status is full-index.
