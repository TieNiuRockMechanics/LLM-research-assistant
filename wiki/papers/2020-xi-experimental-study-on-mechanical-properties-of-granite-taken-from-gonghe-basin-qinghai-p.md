---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-xi-experimental-study-on-mechanical-properties-of-granite-taken-from-gonghe-basin-qinghai-p"
title: "Experimental Study on Mechanical Properties of Granite Taken from Gonghe Basin, Qinghai Province after High Temperature Thermal Damage."
status: "draft"
source_pdf: "data/papers/2020 - 青海共和盆地花岗岩高温热损伤力学特性试验研究.pdf"
collections:
  - "part2"
  - "郤"
citation: "Xi, Baoping, et al. \"Experimental Study on Mechanical Properties of Granite Taken from Gonghe Basin, Qinghai Province after High Temperature Thermal Damage.\" *Chinese Journal of Rock Mechanics and Engineering*, vol. 39, no. 1, 2020, pp. 69-83, doi:10.13722/j.cnki.jrme.2019.0182."
indexed_texts: "8"
indexed_chars: "37857"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "35912"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.948622"
coverage_status: "full-index"
source_signature: "70b93b86d6bf76986d157b36293ffe5309267994"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:11:36"
---

# Experimental Study on Mechanical Properties of Granite Taken from Gonghe Basin, Qinghai Province after High Temperature Thermal Damage.

## One-line Summary
This study investigates the mechanical properties (compressive, tensile, and shear strength) of granite from the Gonghe Basin after high-temperature thermal damage (250°C to 600°C) to provide parameters for dry hot rock geothermal engineering.

## Research Question
How do high temperatures (up to 600°C) and subsequent natural cooling affect the mechanical properties (strength, elastic modulus, brittleness) and fracture characteristics of granite from the Gonghe Basin, and what are the implications for dry hot rock geothermal engineering design and construction?

## Study Area / Data
The granite samples were taken from Longcaigou in the Gonghe Basin, Qinghai Province, China. This granite is consistent with the rock mass encountered in the GR1 exploration borehole for the Gonghe dry hot rock project. The rock is a grey-white, medium-coarse grained granite with a density of 2.65–2.67 g/cm³, primarily composed of plagioclase (40%–50%), quartz (20%–50%), and biotite (5%–10%) [Xi 2020, pp. 2-5].

## Methods
The experimental methodology involved:
1.  **Sample Preparation:** Standard specimens were prepared according to ISRM standards: cylindrical specimens (φ50 mm × 100 mm) for uniaxial compression, disc specimens (φ50 mm × 25 mm) for Brazilian splitting, and cubic specimens (50 mm × 50 mm × 50 mm) for variable angle shear tests [Xi 2020, pp. 2-5].
2.  **Thermal Treatment:** Specimens were heated in a muffle furnace to target temperatures (250°C, 300°C, 350°C, 400°C, 500°C, 600°C) at a rate of 3–5°C/h, held for 3 hours, and then cooled naturally in air [Xi 2020, pp. 2-5].
3.  **Mechanical Testing:** After cooling, tests were conducted on a 600 kN servo-hydraulic universal testing machine:
    *   Uniaxial compression (displacement rate: 0.001 mm/s)
    *   Brazilian splitting (displacement rate: 0.001 mm/s)
    *   Variable angle shear test (displacement rate: 0.002 mm/s) at angles of 45°, 55°, and 65° [Xi 2020, pp. 2-5].
4.  **Microscopic Analysis:** Micro-CT scanning was performed on small cores (φ6 mm × 10 mm) drilled from specimens to observe thermal fracture patterns [Xi 2020, pp. 10-13].
5.  **Numerical Simulation:** COMSOL Multiphysics 5.3a was used to model temperature gradients and thermal stress distribution during cooling [Xi 2020, pp. 10-13].

## Key Findings
1.  **Strength Degradation:** Uniaxial compressive strength, elastic modulus, tensile strength, and cohesion all decreased significantly with increasing temperature. For example, compressive strength dropped from 173.40 MPa at 250°C to 71.49 MPa at 600°C [Xi 2020, pp. 2-5].
2.  **Empirical Formulas:** The study derived empirical formulas relating mechanical properties to temperature:
    *   Compressive strength: σ_c = 314.23 exp(-0.0025T) [Xi 2020, pp. 2-5].
    *   Elastic modulus: E = 21.243 exp(-0.0019T) [Xi 2020, pp. 2-5].
    *   Tensile strength: σ_t = 35.05 exp(-0.0044T) [Xi 2020, pp. 8-10].
    *   Cohesion: c = 168.47 exp(-0.003T) [Xi 2020, pp. 5-8].
    *   Internal friction angle: φ = 17.249 ln(T) - 73.326 [Xi 2020, pp. 5-8].
3.  **Shear Strength Criterion:** A thermo-mechanical shear failure strength criterion was established: τ = σ tan(17.249 ln(T) - 73.326) + 168.47 exp(-0.003T) [Xi 2020, pp. 5-8].
4.  **Brittle-Ductile Transition:** Granite exhibited a transition from brittle to ductile behavior. Between 250°C and 400°C, failure was brittle with explosive fragmentation. Between 500°C and 600°C, ductile characteristics became prominent, with increased strain before failure [Xi 2020, pp. 2-5, 8-10].
5.  **Cooling Rate and Fracturing:** The cooling rate is highest in the first 400 seconds of air cooling, especially the first 150 seconds, leading to the largest temperature gradients and most severe thermal cracking. A higher cooling rate results in a higher density of thermal fractures [Xi 2020, pp. 10-13].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Compressive strength decreases from 173.40 MPa (250°C) to 71.49 MPa (600°C). | [Xi 2020, pp. 2-5] | Uniaxial compression test after thermal damage. | Strength reduction is 58.77% over this temperature range. |
| Elastic modulus decreases from 14.197 GPa (250°C) to 6.717 GPa (600°C). | [Xi 2020, pp. 2-5] | Uniaxial compression test after thermal damage. | Reduction is 52.69%. |
| Tensile strength decreases from 10.89 MPa (250°C) to 2.49 MPa (600°C). | [Xi 2020, pp. 8-10] | Brazilian splitting test after thermal damage. | Reduction is 77.13%. |
| Cohesion decreases from 71.425 MPa (250°C) to 28.200 MPa (600°C). | [Xi 2020, pp. 5-8] | Variable angle shear test after thermal damage. | Reduction is 60.52%. |
| Internal friction angle increases from 20.56° (250°C) to 35.50° (600°C). | [Xi 2020, pp. 5-8] | Variable angle shear test after thermal damage. | Increase is 72.67%. |
| At 500°C–600°C, ductile failure characteristics become prominent. | [Xi 2020, pp. 2-5, 8-10] | Uniaxial compression and Brazilian splitting tests. | Failure strain increases, and explosive brittle failure is less common. |
| The first 150 seconds of air cooling have the highest cooling rate and most severe thermal cracking. | [Xi 2020, pp. 10-13] | Temperature monitoring and micro-CT scanning. | Higher cooling rate leads to higher thermal stress and fracture density. |

## Limitations
1.  The study focuses on granite from a specific location (Longcaigou, Gonghe Basin), and results may not be directly generalizable to all granite types.
2.  The research primarily addresses the effects of high temperature followed by natural air cooling. The effects of other cooling methods (e.g., water quenching) are not the focus of this study.
3.  The temperature range studied is up to 600°C, which is relevant for the Gonghe Basin project but may not cover all possible geothermal scenarios.

## Assumptions / Conditions
1.  The granite samples are representative of the rock mass in the Gonghe Basin dry hot rock reservoir.
2.  The heating and cooling procedures (controlled rate heating, 3-hour hold, natural air cooling) simulate the thermal damage conditions relevant to engineering processes like drilling and reservoir stimulation.
3.  The mechanical tests conducted (uniaxial compression, Brazilian splitting, variable angle shear) are sufficient to characterize the rock's strength and failure behavior for engineering design.

## Key Variables / Parameters
*   **Independent Variable:** Temperature (250°C, 300°C, 350°C, 400°C, 500°C, 600°C).
*   **Dependent Variables:** Uniaxial compressive strength (σ_c), elastic modulus (E), tensile strength (σ_t), cohesion (c), internal friction angle (φ), peak strain, failure mode, cooling rate, thermal fracture density.
*   **Controlled Parameters:** Heating rate (3–5°C/h), holding time (3 hours), specimen dimensions, loading rates during mechanical tests.

## Reusable Claims
*   For Gonghe Basin granite, uniaxial compressive strength (σ_c in MPa) can be estimated as a function of temperature (T in °C) using the formula: σ_c = 314.23 exp(-0.0025T) for T between 250°C and 600°C [Xi 2020, pp. 2-5].
*   The elastic modulus (E in GPa) of Gonghe Basin granite after thermal damage follows: E = 21.243 exp(-0.0019T) for T between 250°C and 600°C [Xi 2020, pp. 2-5].
*   A brittle-ductile transition in Gonghe Basin granite is observed between 500°C and 600°C, where ductile failure characteristics become dominant [Xi 2020, pp. 2-5, 8-10].
*   During natural air cooling of heated granite, the most critical period for thermal fracturing is the first 150 seconds, when the cooling rate and resulting thermal stress are highest [Xi 2020, pp. 10-13].

## Candidate Concepts
*   [[Thermal damage]]
*   [[Dry hot rock]]
*   [[Brittle-ductile transition]]
*   [[Thermal stress]]
*   [[Cooling rate]]
*   [[Shear strength criterion]]
*   [[Empirical formula]]

## Candidate Methods
*   [[Uniaxial compression test]]
*   [[Brazilian splitting test]]
*   [[Variable angle shear test]]
*   [[Micro-CT scanning]]
*   [[Numerical simulation (COMSOL)]]

## Connections To Other Work
The study builds upon and references extensive prior research on the mechanical behavior of granite at high temperatures, including work by Liu Quansheng [Xi 2020, pp. 1-2], Du Shouji [Xi 2020, pp. 1-2, 5-8], Zhu Hehua [Xi 2020, pp. 1-2], Xu Xiaoli [Xi 2020, pp. 1-2], Zuo Jianping [Xi 2020, pp. 1-2], Wan Zhijun [Xi 2020, pp. 1-2], and others on different granite types and experimental conditions. It specifically addresses a gap noted in previous studies regarding the shear strength of thermally damaged granite [Xi 2020, pp. 1-2].

## Open Questions
1.  How do different cooling methods (e.g., water quenching vs. air cooling) affect the mechanical properties and fracture network of Gonghe Basin granite?
2.  What are the long-term effects of cyclic thermal loading (heating and cooling) on the granite's mechanical integrity?
3.  How do the derived empirical formulas and strength criteria perform under true triaxial stress conditions representative of deep reservoirs?

## Source Coverage
All 8 non-empty indexed fragments were processed. The compiled content covers 35,912 characters out of 37,857 indexed characters, achieving a coverage ratio of 0.948622 by character count. The coverage status is full-index.
