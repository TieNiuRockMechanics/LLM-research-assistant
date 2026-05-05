---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2018-liang-optimization-of-heat-extraction-strategies-in-fault-controlled-hydro-geothermal-reser"
title: "Optimization of Heat Extraction Strategies in Fault-controlled Hydro-geothermal Reservoirs."
status: "draft"
source_pdf: "data/papers/Optimization of heat extraction strategies in fault-controlled hydro-geothermal reservoirs.pdf"
collections:
citation: "Liang, Xu, et al. \"Optimization of Heat Extraction Strategies in Fault-controlled Hydro-geothermal Reservoirs.\" *Energy*, 2018, doi:10.1016/j.energy.2018.09.043. Accessed 2026."
indexed_texts: "12"
indexed_chars: "55575"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "55058"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.990697"
coverage_status: "full-index"
source_signature: "9c366e4f9ba2c64a740546ebf5b1c2468ae58dbb"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:36:48"
---

# Optimization of Heat Extraction Strategies in Fault-controlled Hydro-geothermal Reservoirs.

## One-line Summary
This study uses coupled thermal–hydraulic numerical modeling to optimize well placement and operational parameters for sustainable heat extraction in a fault-controlled geothermal system, achieving a net production of 1.67 MW over 50 years under optimized conditions [Liang 2018, pp. 1-4].

## Research Question
How can well placement (production depth, injection depth, well distance) and operational parameters (injection temperature, production backpressure) be optimized to maximize sustainable heat production in a fault-controlled hydro-geothermal reservoir? [Liang 2018, pp. 4-6].

## Study Area / Data
The study is based on the Zhacang geothermal field in the Guide Basin, located on the northeastern margin of the Qinghai-Tibet Plateau [Liang 2018, pp. 4-6]. The geothermal system is fault-controlled, with the Zhacang spring located at the junction of an east-west striking normal fault (F2) and a north-northwest striking reverse fault (F5) [Liang 2018, pp. 6-10]. Key data includes downhole temperature logs from well ZR1 (wellhead temperature 90°C, bottom temperature 151°C at 3 km depth), fracture patterns from outcrops, and regional heat flow measurements (79.5 to 123.1 mW/m²) [Liang 2018, pp. 6-10, pp. 10-14].

## Methods
The numerical code TOUGH2-EOS1 was used to simulate non-isothermal fluid and heat transfer in a simplified 3D model of a single conductive fault embedded in impermeable country rock [Liang 2018, pp. 10-14]. The model domain featured a fault with a length of 2.4 km, width of 30 m, and depth of 2.8 km [Liang 2018, pp. 10-14]. Boundary conditions included a specified pressure at the discharge point, a specified water flux representing recharge from the Gangyi stream (2.5 L/s at 7°C), and a constant basal heat flux of 75 mW/m² [Liang 2018, pp. 10-14]. The fault zone permeability was initially estimated using the "matchstick model" and then calibrated to 50 mD to match observed temperatures in well ZR1 [Liang 2018, pp. 10-14]. A doublet well system (one injection, one production) was modeled, and a perturbation-based one-at-a-time sensitivity analysis was used to evaluate the influence of anthropogenic and natural factors [Liang 2018, pp. 14-18].

## Key Findings
1.  The optimized strategy for the Zhacang field is: production depth of 300 m, injection depth of 1500 m, well distance of 300 m, injection temperature of 10°C, and production backpressure of 0.7 MPa. This yields a net heat production rate of 1.67 MW sustained over 50 years [Liang 2018, pp. 23-27].
2.  Terrestrial heat flux (70-130 mW/m²) has a negligible effect on heat production because heat transport in the permeable fault zone is dominated by convection rather than conduction [Liang 2018, pp. 27-31].
3.  Heat production increases with fault zone permeability, as higher permeability enhances convective heat recovery [Liang 2018, pp. 27-31].
4.  Increased country rock permeability leads to higher outflow rates but significantly lower outflow temperatures due to cool lateral recharge. When country rock permeability exceeds 0.1 mD, outflow temperature drops by more than 10% [Liang 2018, pp. 31-34].
5.  Increasing the vertical separation between injection and production wells helps avoid rapid breakthrough of injected cold water to the production well [Liang 2018, pp. 31-34].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Optimized strategy yields 1.67 MW net heat production over 50 years. | [Liang 2018, pp. 23-27] | Production depth 300 m, injection depth 1500 m, well distance 300 m, injection temperature 10°C, production backpressure 0.7 MPa, injection rate 2.5 kg/s. | This is the primary optimized result for the Zhacang field. |
| Terrestrial heat flux has negligible effect on heat production. | [Liang 2018, pp. 27-31] | Heat flux varied from 70 to 130 mW/m² under optimized well placement. | Heat transport in the fault zone is convection-dominated. |
| Outflow temperature decreases sharply in low-permeability fault zones. | [Liang 2018, pp. 27-31] | Fault permeability varied from 10 to 100 mD. | Low permeability weakens convective heat recovery. |
| Country rock permeability >0.1 mD causes outflow temperature to drop >10%. | [Liang 2018, pp. 31-34] | Country rock permeability varied from 10⁻⁴ to 1.0 mD. | Increased lateral recharge of cool water lowers fault zone temperature. |
| A production depth of 300 m is sufficient to maintain constant net heat production. | [Liang 2018, pp. 14-18] | Injection depth 1500 m, well distance 300 m, injection temperature 60°C, production backpressure 0.5 MPa. | Deeper production increases drilling cost without proportional benefit. |
| Model calibration: 50 mD fault permeability reproduces ZR1 temperature logs. | [Liang 2018, pp. 10-14] | Homogeneous, isotropic fault zone permeability. | A maximum error of 8°C at 1200 m depth is noted due to potential heterogeneity. |

## Limitations
1.  The model assumes isotropic and homogeneous thermal and hydraulic properties for the fault zone and country rock [Liang 2018, pp. 10-14].
2.  Injection and production wells are modeled as simple source/sink terms without considering heat and fluid transport within the wellbores [Liang 2018, pp. 14-18].
3.  The study focuses on a single fault zone and does not account for potential interactions with other geological structures [Liang 2018, pp. 10-14].
4.  Economic analysis is limited to drilling cost considerations; a full techno-economic optimization is not performed [Liang 2018, pp. 14-18].

## Assumptions / Conditions
1.  The fault geometry is based on field investigations and well ZR1 logs: length 2.4 km, width 30 m, depth 2.8 km [Liang 2018, pp. 10-14].
2.  Boundary conditions: constant pressure (0.1 MPa) at the discharge point, constant recharge flux (2.5 L/s at 7°C), and constant basal heat flux (75 mW/m²) [Liang 2018, pp. 10-14].
3.  Physical and thermal parameters are specified according to Lang et al. (2016) and are summarized in Table 1 of the paper [Liang 2018, pp. 10-14].
4.  The sustainability criterion is that outflow temperature should not decrease by more than 10% of its initial value during the 50-year operation period [Liang 2018, pp. 14-18].
5.  Bottom hole injection pressure increase is limited to less than 6.9 MPa to avoid inducing fractures [Liang 2018, pp. 14-18].

## Key Variables / Parameters
*   **Anthropogenic (Operational):** Production depth (d_p), Injection depth (d_i), Well separation distance (h), Injection temperature (T_inj), Production backpressure (P_pro), Injection rate (Q_inj) [Liang 2018, pp. 14-18].
*   **Natural (Reservoir):** Fault zone permeability (k_f), Country rock permeability (k_m), Terrestrial heat flux (q), Porosity (φ) [Liang 2018, pp. 10-14, pp. 27-31].
*   **Performance Metrics:** Outflow temperature (T_out), Outflow rate (Q_out), Net heat production rate (W) [Liang 2018, pp. 14-18].

## Reusable Claims
*   **Claim:** In a fault-controlled hydro-geothermal reservoir where heat transport is convection-dominated, the terrestrial heat flux has a negligible influence on the long-term heat production performance. **Condition:** This applies when the fault zone has sufficient permeability (e.g., ~50 mD) to allow significant fluid circulation. **Limitation:** The claim is based on a specific numerical model of the Zhacang field; applicability to systems with different geometries or boundary conditions requires verification [Liang 2018, pp. 27-31].
*   **Claim:** Optimizing the vertical separation between injection and production wells (e.g., injection deeper than production) is critical for preventing rapid thermal breakthrough and sustaining heat production. **Condition:** This is effective in a vertical or sub-vertical fault zone with a conductive pathway between the wells. **Limitation:** The optimal separation distance depends on specific reservoir permeability and operational flow rates [Liang 2018, pp. 14-18, pp. 31-34].
*   **Claim:** Increasing the permeability of the fault zone enhances both the outflow rate and temperature, improving heat production. **Condition:** This assumes the fault zone is the primary flow path and that increased permeability does not lead to excessive cooling from recharge. **Limitation:** Very high permeability might reduce water residence time too much, though this was not observed in the tested range (10-100 mD) [Liang 2018, pp. 27-31].

## Candidate Concepts
*   [[fault-controlled geothermal reservoir]]
*   [[doublet well system]]
*   [[thermal-hydraulic coupled modeling]]
*   [[heat extraction optimization]]
*   [[convective heat transport]]
*   [[geothermal sustainability]]
*   [[sensitivity analysis]]

## Candidate Methods
*   [[TOUGH2-EOS1]]
*   [[integrated finite difference method]]
*   [[Newton-Raphson iteration]]
*   [[matchstick model]]
*   [[one-at-a-time sensitivity analysis]]
*   [[numerical reservoir simulation]]

## Connections To Other Work
The study builds on previous numerical modeling work of fluid and heat flow in fault zones, such as López and Smith (1995) [Liang 2018, pp. 4-6]. It applies optimization approaches similar to those used by Aliyu and Chen (2017) for fractured reservoirs [Liang 2018, pp. 4-6]. The geological setting and parameters are informed by prior investigations of the Guide Basin and Zhacang field [Liang 2018, pp. 4-6, pp. 34-36].

## Open Questions
1.  How would heterogeneous and anisotropic permeability distributions within the fault zone affect the optimized strategies? [Liang 2018, pp. 10-14].
2.  What is the full techno-economic optimum when considering both drilling costs and long-term energy revenue? [Liang 2018, pp. 14-18].
3.  How can the findings be generalized to other fault-controlled geothermal systems with different geometries (e.g., multiple interacting faults)? [Liang 2018, pp. 31-34].

## Source Coverage
All non-empty indexed fragments were processed. The compilation is based on 12 indexed source blocks containing 55,575 characters. The compiled page uses 12 source blocks with 55,058 characters, achieving a coverage ratio of 1.0 by block count and 0.990697 by character count. The source signature is `9c366e4f9ba2c64a740546ebf5b1c2468ae58dbb`.
