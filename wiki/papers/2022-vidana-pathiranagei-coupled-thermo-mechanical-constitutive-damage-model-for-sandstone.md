---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-vidana-pathiranagei-coupled-thermo-mechanical-constitutive-damage-model-for-sandstone"
title: "Coupled Thermo-Mechanical Constitutive Damage Model for Sandstone."
status: "draft"
source_pdf: "data/papers/砂岩热机械耦合损伤模型 Coupled thermo-mechanical constitutive damage model for sandstone.pdf"
collections:
citation: "Vidana Pathiranagei, Savani, and Ivan Gratchev. \"Coupled Thermo-Mechanical Constitutive Damage Model for Sandstone.\" *Journal of Rock Mechanics and Geotechnical Engineering*, 2022."
indexed_texts: "10"
indexed_chars: "49635"
nonempty_source_blocks: "10"
compiled_source_blocks: "10"
compiled_source_chars: "49865"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004634"
coverage_status: "full-index"
source_signature: "4d5e48b35484b478f5b8bd2c6f1d11f4877e3fea"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T11:31:19"
---

# Coupled Thermo-Mechanical Constitutive Damage Model for Sandstone.

## One-line Summary
A statistical coupled thermo-mechanical damage constitutive model for sandstone, based on Weibull distribution and Lemaitre’s strain equivalent principle, was established and validated against triaxial test data under high temperature and pressure conditions.

## Research Question
How can the coupled thermo-mechanical (TM) damage behavior of sandstone under high temperature and three-dimensional stress conditions be modeled to predict its strength and failure characteristics for underground engineering applications?

## Study Area / Data
The study used sandstone from Gold Coast, Australia, a dominant rock type in Southeast Queensland. X-ray diffraction analysis showed the sandstone was composed of 45% quartz, 39% feldspar, 10% kaolinite, and 6% illite [Vidana 2022, pp. 3-5]. Twenty-four cubic (50 mm) samples were prepared. Triaxial tests were conducted at temperatures of 25°C, 400°C, 600°C, and 800°C and confining pressures of 3 MPa, 6 MPa, and 9 MPa [Vidana 2022, pp. 3-5].

## Methods
The coupled TM damage model was developed using the Weibull damage method to analyze mechanical characteristics and a thermal damage factor based on elastic modulus [Vidana 2022, pp. 1-2]. The total damage was defined using generalized damage variables. The Mohr-Coulomb failure criterion was incorporated into the damage model [Vidana 2022, pp. 2-3]. Model parameters (m and F0) were determined using the "extremum method" from the peak point of stress-strain curves [Vidana 2022, pp. 2-3]. Triaxial tests were performed using a true triaxial testing system with a loading rate of 0.2 MPa/s [Vidana 2022, pp. 3-5].

## Key Findings
1.  The proposed coupled TM damage model showed good agreement with experimental triaxial test results for sandstone at temperatures up to 600°C [Vidana 2022, pp. 9-11].
2.  The total coupled TM damage (D) decreased with increasing temperature but increased with increasing confining pressure [Vidana 2022, pp. 1-1, 8-9].
3.  Peak stress and elastic modulus generally increased with increasing confining pressure. The effect of temperature on peak stress was positive, while its effect on elastic modulus was more complex [Vidana 2022, pp. 5-6].
4.  The internal friction angle of sandstone increased with temperature, while cohesion remained relatively unchanged [Vidana 2022, pp. 6-8].
5.  The model parameters m and F0 can be calculated using conventional laboratory test results [Vidana 2022, pp. 1-1].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| The model is in good agreement with experimental results up to 600°C. | [Vidana 2022, pp. 9-11] | Temperatures ≤ 600°C, Confining pressure 3 MPa | Validation against triaxial test curves. |
| Total TM damage (D) decreases with increasing temperature. | [Vidana 2022, pp. 1-1, 8-9] | Temperatures from 25°C to 800°C | Linked to peak stress behavior and mineral thermal expansion. |
| Total TM damage (D) increases with increasing confining pressure. | [Vidana 2022, pp. 8-9] | Confining pressures of 3, 6, and 9 MPa at 400°C | Shows confining pressure weakens stress state and speeds damage development. |
| Peak stress increases with both temperature and confining pressure. | [Vidana 2022, pp. 5-6] | All tested temperatures and pressures | Attributed to crack healing, mineral expansion, and increased friction. |
| Internal friction angle increases with temperature; cohesion is relatively stable. | [Vidana 2022, pp. 6-8] | Temperatures from 25°C to 800°C | Based on Mohr-Coulomb criterion regression analysis. |
| Model parameters m and F0 can be derived from lab test data. | [Vidana 2022, pp. 1-1, 8-9] | General | Using the extremum method on stress-strain peak points. |

## Limitations
1.  The model shows significant discrepancy with experimental curves at temperatures of 600°C and 800°C, likely due to the phase transition of quartz mineral around 573°C [Vidana 2022, pp. 9-11].
2.  The theoretical model reflects an initial compaction stage not always evident in test curves, leading to lower theoretical stress before yield [Vidana 2022, pp. 9-11].
3.  During plastic deformation, the model shows elastic-plastic behavior, whereas test curves show strain-hardening behavior [Vidana 2022, pp. 9-11].
4.  The model's applicability is limited to sandstone with a specific mineral composition (low clay, no calcite) as studied [Vidana 2022, pp. 5-6].

## Assumptions / Conditions
1.  The rock's microscopic element strength follows a Weibull distribution function [Vidana 2022, pp. 1-2].
2.  The thermal damage factor is defined based on linear damage mechanics using the elastic modulus [Vidana 2022, pp. 1-2].
3.  The relationship between effective stress and apparent stress follows Lemaitre’s strain equivalent principle [Vidana 2022, pp. 1-2].
4.  The linear Mohr-Coulomb criterion is acceptable for describing the geomechanical behavior of the thermally treated sandstone [Vidana 2022, pp. 6-8].
5.  The model assumes linear elastic behavior before reaching a yield point [Vidana 2022, pp. 9-11].

## Key Variables / Parameters
*   **D_T**: Thermal damage factor.
*   **D_M**: Mechanical damage variable (Lemaitre’s damage variable).
*   **D**: Total coupled thermo-mechanical damage.
*   **E_T**: Elastic modulus at temperature T.
*   **E_0**: Elastic modulus at room temperature.
*   **m**: Shape parameter of the Weibull distribution.
*   **F_0**: Mean value of the elemental strength parameter.
*   **σ_ij**: Nominal (apparent) stress tensor.
*   **σ*_ij**: Effective stress tensor.
*   **ε_ij**: Strain tensor.
*   **c**: Cohesion of the rock.
*   **φ**: Internal friction angle.
*   **I'_1**: First effective stress invariant.
*   **J'_2**: Second effective deviator stress invariant.

## Reusable Claims
1.  **Condition:** For sandstone with mineral composition similar to the tested sample (45% quartz, 39% feldspar, 10% kaolinite, 6% illite). **Limitation:** Up to temperatures of 600°C. **Claim:** The coupled thermo-mechanical damage constitutive model based on Weibull distribution and the Mohr-Coulomb criterion can accurately predict the stress-strain behavior and damage evolution.
2.  **Condition:** Under triaxial stress conditions with confining pressure. **Claim:** Increasing confining pressure increases the total coupled thermo-mechanical damage (D) in sandstone, indicating it diminishes rock resistance and accelerates damage development.
3.  **Condition:** For the tested sandstone after thermal treatment. **Claim:** The internal friction angle increases with temperature due to differential thermal expansion of mineral particles, while cohesion remains relatively unaffected, suggesting peak stress is primarily governed by frictional properties.
4.  **Condition:** For sandstone subjected to heating and air-cooling. **Claim:** The strength enhancement at temperatures above 600°C is attributed to higher porosity, weaker heterogeneity of mineral thermal expansion, plastic expansion of minerals, and the fact that strength weakening during air-cooling does not fully compensate for heating-stage enhancement.

## Candidate Concepts
*   [[Thermo-mechanical coupling]]
*   [[Damage mechanics]]
*   [[Weibull distribution]]
*   [[Mohr-Coulomb criterion]]
*   [[Constitutive model]]
*   [[Triaxial testing]]
*   [[Thermal damage]]
*   [[Mechanical damage]]
*   [[Effective stress]]
*   [[Strain equivalent principle]]
*   [[Rock failure]]
*   [[Mineral thermal expansion]]

## Candidate Methods
*   [[Triaxial testing]]
*   [[Weibull damage method]]
*   [[Mohr-Coulomb failure criterion]]
*   [[Extremum method]] (for parameter determination)
*   [[X-ray diffraction analysis]]
*   [[Linear regression analysis]]

## Connections To Other Work
The study builds upon and addresses gaps in prior research on thermal damage models for rocks like granite, claystone, marble, and shale [Vidana 2022, pp. 1-1]. It specifically notes limited prior investigation into the coupled TM damage model for sandstone, referencing work by Hassanzadegan et al. (2014) and Zhu et al. (2021) [Vidana 2022, pp. 1-2]. The model incorporates principles from Lemaitre (1992) and uses a framework similar to that applied to granite by Xu and Karakus (2018) [Vidana 2022, pp. 2-3].

## Open Questions
1.  How can the model be improved to account for behavior above 600°C, potentially by incorporating plasticity theory and residual strength?
2.  How would the model perform for sandstones with different mineral compositions, particularly those with higher clay or calcite content?
3.  What is the long-term performance of this model under sustained loads and cyclic thermal conditions?
4.  How does the cooling method (e.g., air cooling vs. water quenching) affect the model's parameters and validity?

## Source Coverage
All 10 non-empty indexed fragments were processed. The compiled source blocks total 49,865 characters, achieving a coverage ratio of 1.004634 by characters relative to the indexed text. The coverage status is "full-index".
