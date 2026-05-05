---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2017-zhou-experimental-study-on-hydraulic-fracturing-of-granite-under-thermal-shock-de6132de"
title: "Experimental Study on Hydraulic Fracturing of Granite under Thermal Shock."
status: "draft"
source_pdf: "data/papers/热冲击下花岗岩水力压裂实验研究 Experimental study on hydraulic fracturing of granite under thermal shock.pdf"
collections:
citation: "Zhou, Changbing, et al. \"Experimental Study on Hydraulic Fracturing of Granite under Thermal Shock.\" *Geothermics*, 2017, doi:10.1016/j.geothermics.2017.09.006. Accessed 2026."
indexed_texts: "11"
indexed_chars: "52615"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "52847"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004409"
coverage_status: "full-index"
source_signature: "0000bff018bd00b07f206776369c6610db01f037"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T11:27:29"
---

# Experimental Study on Hydraulic Fracturing of Granite under Thermal Shock.

## One-line Summary
This study experimentally demonstrates that the crack initiation pressure during hydraulic fracturing of granite decreases significantly above 200°C, primarily due to thermal shock induced by the cooling effect of the fracturing fluid rather than changes in the rock's mechanical parameters.

## Research Question
How does temperature (from 20°C to 400°C) affect the hydraulic fracturing behavior, specifically the crack initiation pressure and fracture propagation pattern, of granite, and what is the underlying mechanism?

## Study Area / Data
The experimental subject was "Shandong Grey" granite from Pingyi, Shandong Province, China. Cylindrical samples had dimensions of φ200 × 400 mm with a central water injection hole (18 mm diameter, 250 mm depth). Experiments were conducted at target temperatures of 20°C, 100°C, 200°C, 300°C, and 400°C under a constant triaxial confining pressure of 25 MPa [Zhou 2017, pp. 2-3].

## Methods
1.  **Experimental Setup:** Used a "triaxial testing machine of servo control for rock mass at the high temperature of 600 °C and the high pressure of 20 MN" with a high-pressure water loading system (max 400 MPa) [Zhou 2017, pp. 1-2].
2.  **Procedure:** Samples were loaded to 25 MPa confining pressure, heated to the target temperature at 10°C/h, and held for 2 hours. High-pressure water was then injected at a steady rate (motor speed increased by 2 Hz/s). Fracturing was indicated by a sudden pressure drop (>1 MPa) [Zhou 2017, pp. 2-3].
3.  **Numerical Modeling:** A strong transient thermal stress model was established to simulate the thermal shock phenomenon. The model used a non-Fourier heat conduction equation to account for finite thermal wave propagation speed and was solved using COMSOL software [Zhou 2017, pp. 5-6, 6-8].

## Key Findings
1.  **Fracturing Mode Change:** At 20°C, fracturing was instantaneous and brittle. From 100°C upwards, fracturing became continuous, with the fracture growth rate matching the fluid injection rate [Zhou 2017, pp. 3-4].
2.  **Initiation Pressure Drop:** Crack initiation pressure decreased with increasing temperature. The drop was gradual from 20°C to 200°C but became abrupt between 200°C and 300°C (from 43.2 MPa to 24.6 MPa, a 43.1% relative drop) [Zhou 2017, pp. 3-4].
3.  **Thermal Shock Mechanism:** The primary mechanism for the pressure drop is thermal shock, not changes in mechanical parameters. The room-temperature fracturing fluid rapidly cools the high-temperature borehole, creating a large thermal gradient and tensile stress near the surface [Zhou 2017, pp. 5-6].
4.  **Dual Shock Waves:** The thermal shock generates two sequential impact waves near the borehole: an elastic wave (stress wave) followed by a thermal wave. The coupling of these waves significantly reduces the stress required for fracture initiation [Zhou 2017, pp. 8-8, 8-9].
5.  **Fracture Propagation:** With increasing temperature, fracture propagation shifted from primarily axial to more radial. Transverse fractures appeared at 300°C and 400°C, likely due to large deformations from the reduced elastic modulus [Zhou 2017, pp. 3-4, 4-5].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| First fracturing initiation pressure at 20°C was 50.6 MPa. | [Zhou 2017, pp. 3-4] | 20°C, 25 MPa confining pressure | Highest recorded initiation pressure. |
| Initiation pressure at 300°C was 24.6 MPa, a 43.1% relative drop from 200°C. | [Zhou 2017, pp. 3-4] | 300°C, 25 MPa confining pressure | Marks the threshold for a sharp drop in pressure. |
| Tensile strength decreased by only 1.1 MPa from 100°C to 400°C, while initiation pressure decreased by 32.4 MPa. | [Zhou 2017, pp. 4-5] | 100°C to 400°C | Evidence that mechanical parameter changes are not the main factor. |
| At 300°C, the velocity of the elastic wave (cs = 5300 m/s) was 6.88 times that of the thermal wave (ch = 770 m/s). | [Zhou 2017, pp. 8-8] | Granite at 300°C | Explains the sequential arrival of the two shock waves. |
| Without considering temperature, the circumferential stress at 300°C was -20.5 MPa; with thermal shock, it became 10.17 MPa, close to the tensile strength (8.5 MPa). | [Zhou 2017, pp. 9-10] | 300°C, initiation pressure 24.6 MPa | Quantitative demonstration of thermal shock's critical role. |

## Limitations
1.  The thermal shock model simplifies the rock as an infinite, homogeneous medium and assumes the borehole wall temperature drops instantaneously to water temperature [Zhou 2017, pp. 5-6].
2.  The study focuses on a single type of granite ("Shandong Grey"). Results may vary for other rock types.
3.  The experimental setup limited the investigation to temperatures up to 400°C, whereas actual EGS reservoirs can be hotter [Zhou 2017, pp. 1-2].

## Assumptions / Conditions
1.  Before injection, the rock sample is a stable isothermal body [Zhou 2017, pp. 5-6].
2.  The engineering rock mass is considered infinite relative to the fracturing point [Zhou 2017, pp. 5-6].
3.  The temperature of the fracturing fluid (water) is constant at room temperature during injection [Zhou 2017, pp. 5-6].
4.  The borehole wall temperature drops to the water temperature at the moment of contact [Zhou 2017, pp. 5-6].

## Key Variables / Parameters
*   **Independent Variable:** Sample temperature (20°C, 100°C, 200°C, 300°C, 400°C).
*   **Dependent Variables:** Crack initiation pressure (MPa), fracture propagation pattern, water pressure loading curve characteristics.
*   **Controlled Variables:** Confining pressure (25 MPa), sample size and geometry, fracturing fluid (water), injection rate control mode.
*   **Key Parameters:** Elastic modulus (E), tensile strength (St), thermal diffusion coefficient (a), thermal relaxation time (τ₀), linear expansion coefficient (α).

## Reusable Claims
1.  **Condition:** For Shandong Grey granite under 25 MPa confining pressure. **Claim:** The crack initiation pressure during hydraulic fracturing decreases significantly when the rock temperature exceeds 200°C, with the most dramatic drop occurring between 200°C and 300°C [Zhou 2017, pp. 3-4].
2.  **Condition:** During hydraulic fracturing of high-temperature rock (>200°C). **Claim:** The primary mechanism reducing fracturing pressure is thermal shock induced by the cooling effect of the injected fracturing fluid, which generates coupled elastic and thermal stress waves near the borehole, rather than the degradation of the rock's intrinsic mechanical properties [Zhou 2017, pp. 5-6, 9-10].
3.  **Condition:** In granite subjected to temperatures from 200°C to 400°C. **Claim:** The presence of thermally-induced micro-cracks changes the fracture propagation mode from brittle, instantaneous failure to a continuous process where the main fracture tip connects with pre-existing micro-cracks [Zhou 2017, pp. 4-5, 5-6].

## Candidate Concepts
*   [[Thermal shock]]
*   [[Hydraulic fracturing]]
*   [[Thermo-mechanical coupling]]
*   [[Enhanced Geothermal Systems (EGS)]]
*   [[Crack initiation pressure]]
*   [[Thermal fracturing]]
*   [[Non-Fourier heat conduction]]

## Candidate Methods
*   [[Triaxial hydraulic fracturing experiment]]
*   [[Numerical modeling of thermal stress]]
*   [[Strong transient thermal stress model]]
*   [[High-temperature servo-controlled testing]]

## Connections To Other Work
*   The study addresses a gap in physical experiments for hydraulic fracturing at high temperatures (>200°C), noting most prior research focused on low-temperature rocks like coal and shale [Zhou 2017, pp. 1-2].
*   It builds on prior knowledge that temperature affects rock mechanical properties (e.g., [Yin et al., 2015; Xu and Liu, 2000]) but argues this is not the dominant factor for fracturing pressure [Zhou 2017, pp. 1-2, 4-5].
*   The experimental equipment was independently developed by China University of Mining and Technology [Zhao et al., 2008a].
*   The work references cases of hydraulic fracturing failure in Australia to highlight the engineering importance of understanding high-temperature effects [Rahman et al., 2007].

## Open Questions
1.  How do the findings scale to larger rock masses and different rock types in actual EGS reservoirs?
2.  What is the long-term effect of repeated thermal shocks on fracture network permeability and stability?
3.  Can the thermal shock effect be optimized or controlled to engineer more complex and desirable fracture networks?

## Source Coverage
All 11 non-empty indexed fragments were processed. The compiled source blocks total 52,847 characters, achieving a coverage ratio of 1.004409 by character count relative to the indexed text (52,615 characters). The coverage status is full-index.
