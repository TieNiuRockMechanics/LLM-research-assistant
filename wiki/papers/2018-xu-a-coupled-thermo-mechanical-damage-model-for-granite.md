---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2018-xu-a-coupled-thermo-mechanical-damage-model-for-granite"
title: "A Coupled Thermo-Mechanical Damage Model for Granite."
status: "draft"
source_pdf: "data/papers/花岗岩热机械损伤耦合模型 A coupled thermo-mechanical damage model for granite.pdf"
collections:
citation: "Xu, X. L., and M. Karakus. \"A Coupled Thermo-Mechanical Damage Model for Granite.\" *International Journal of Rock Mechanics and Mining Sciences*, 2018. doi:10.1016/j.ijrmms.2018.01.030. Accessed 2026."
indexed_texts: "9"
indexed_chars: "41905"
nonempty_source_blocks: "9"
compiled_source_blocks: "9"
compiled_source_chars: "42077"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004105"
coverage_status: "full-index"
source_signature: "406fe1182e2eb25d68664738e800d46847878858"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T11:17:54"
---

# A Coupled Thermo-Mechanical Damage Model for Granite.

## One-line Summary
A coupled thermo-mechanical damage model for granite is developed using Weibull distribution and Lemaitre's strain-equivalent principle to simulate deformation and failure under high temperature and pressure conditions.

## Research Question
How to correctly model the coupled thermo-mechanical (TM) behavior of rocks, specifically granite, for better and safer designs of deep underground structures exposed to high temperature and pressure (HTP) conditions?

## Study Area / Data
The rock samples were granite retrieved from a depth of about 1000–1200 m in the Yanzhou hard coal mine, Shandong Province, China. The rock block was coarse-grained, relatively isotropic, and mainly comprised of feldspar, quartz, and mica. Core samples with a diameter of 50 mm and length of 100 mm were drilled and prepared according to ISRM specifications. The average longitudinal wave velocity was 4420 m/s, average density was 2.612 g/cm³, and average uniaxial compressive strength (UCS) at room temperature was 120.37 MPa [Xu 2018, pp. 1-2].

## Methods
The methodology involved two main parts: experimental testing and model derivation.
1.  **Experimental Testing:** Granite samples were heated to temperatures of 200, 400, 600, 800, 1000, and 1200 °C at a rate of 10 °C/min, held for 2 hours, and then cooled to room temperature. Five samples were used per temperature point (30 total). Subsequently, triaxial compression tests under confining pressures of 0, 10, 20, 30, and 40 MPa were conducted on the preheated samples using an MTS815.02 system with a displacement control loading rate of 0.003 mm/s [Xu 2018, pp. 1-2].
2.  **Model Derivation:** A coupled TM damage model was derived. Thermal damage (D_T) was defined based on the change in elastic modulus with temperature. Mechanical damage (D_M) was derived using a Weibull distribution for mesoscopic element strength and Lemaitre's strain-equivalent principle. The total coupled damage (D) was formulated by combining D_T and D_M. The Drucker-Prager failure criterion was used as an example to incorporate a failure criterion into the model [Xu 2018, pp. 3-5].

## Key Findings
1.  Peak stress and elastic modulus of granite show a logistic decline with increasing temperature and exponential growth with increasing confining pressure [Xu 2018, pp. 2-3].
2.  Thermal damage (D_T) increases with temperature in three stages: slow increase from 25–400 °C, rapid increase from 400–600 °C (attributed to the α-quartz to β-quartz phase transition at 573 °C), and slow increase again from 600–1000 °C [Xu 2018, pp. 7-8].
3.  As temperature and confining pressure increase, the slope of the total damage curve becomes gentler, the maximum damage evolution rate decreases exponentially, and the corresponding strain increases, indicating an enhanced ductility effect [Xu 2018, pp. 7-8].
4.  The Weibull distribution parameter `n` reflects rock brittleness and decays exponentially with increasing temperature and confining pressure. The parameter `F₀` represents peak strength and shows logistic decay with temperature and exponential growth with confining pressure [Xu 2018, pp. 8-10].
5.  The theoretical stress-strain curves from the proposed coupled TM model showed good agreement with experimental data under various temperatures [Xu 2018, pp. 8-10].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Thermal damage D_T defined as D_T = 1 - E_T/E_0, where E_0 is initial elastic modulus and E_T is modulus at temperature T. | [Xu 2018, pp. 3-5] | General definition for thermal damage based on elastic modulus degradation. | Foundational equation for thermal damage component. |
| Mechanical damage D_M derived using Weibull distribution: D_M = 1 - exp[-(F/F_0)^n]. | [Xu 2018, pp. 3-5] | Based on statistical distribution of mesoscopic element strength. | Core of the mechanical damage formulation. |
| Total coupled TM damage D = 1 - (1-D_T)(1-D_M) = 1 - (E_T/E_0) * exp[-(F/F_0)^n]. | [Xu 2018, pp. 5-7] | Coupling of thermal and mechanical damage. | Key equation of the proposed model. |
| Thermal damage D_T shows logistic growth with temperature, with a rapid increase between 400 °C and 600 °C. | [Xu 2018, pp. 7-8] | Granite samples heated from 25 °C to 1000 °C. | Attributed to α-quartz to β-quartz phase transition at 573 °C. |
| Parameter `n` (Weibull) decays exponentially with increasing temperature and confining pressure. | [Xu 2018, pp. 8-10] | Derived from triaxial test data at various T and σ₃. | Interpreted as representing the brittleness of the rock. |
| Parameter `F₀` (Weibull) shows logistic decay with temperature and exponential growth with confining pressure. | [Xu 2018, pp. 8-10] | Derived from triaxial test data at various T and σ₃. | Interpreted as representing the peak strength of the rock. |
| Model validation shows good agreement between theoretical and experimental stress-strain curves at various temperatures. | [Xu 2018, pp. 8-10] | Comparison for granite samples at different temperatures. | Demonstrates model's predictive capability. |

## Limitations
1.  The model uses linear elasticity (Hooke's law) for pre-peak behavior and does not incorporate plasticity theory, which is suggested for future improvement [Xu 2018, pp. 8-10].
2.  The model does not account for the residual strength of the rock after peak stress, which is important for practical engineering applications like excavation design and stability evaluation [Xu 2018, pp. 8-10].
3.  The experimental validation was conducted on a specific type of granite from one location; generalizability to other rock types requires further study.

## Assumptions / Conditions
1.  The rock material is discretized into representative elementary volumes (REVs) whose mechanical properties follow a Weibull statistical distribution [Xu 2018, pp. 3-5].
2.  Lemaitre's strain-equivalent principle is applied: the strain caused by nominal stress on damaged material is equivalent to the strain caused by effective stress on non-damaged material [Xu 2018, pp. 3-5].
3.  The pre-peak behavior of granite is assumed to be linear elastic [Xu 2018, pp. 8-10].
4.  The model is derived for quasi-brittle materials like granite under coupled thermo-mechanical loading.

## Key Variables / Parameters
*   **D_T:** Thermal damage variable.
*   **D_M:** Mechanical damage variable.
*   **D:** Total coupled thermo-mechanical damage variable.
*   **E_0:** Initial elastic modulus at room temperature.
*   **E_T:** Elastic modulus at elevated temperature T.
*   **F:** Random variable of Weibull distribution (related to stress state).
*   **F_0, n:** Weibull statistical distribution parameters.
*   **σ_f, ε_f:** Peak stress and corresponding peak strain from uniaxial/triaxial tests.
*   **α₀, k:** Material constants for the Drucker-Prager failure criterion.

## Reusable Claims
1.  **Condition:** For granite under heating from 25 °C to 1000 °C. **Claim:** Thermal damage increases slowly from 25–400 °C, rapidly from 400–600 °C, and slowly again from 600–1000 °C, with the rapid phase linked to the α-quartz to β-quartz phase transition at 573 °C. [Xu 2018, pp. 7-8]
2.  **Condition:** For granite under triaxial compression after thermal treatment. **Claim:** Increasing confining pressure improves the stress state, delays damage development, and enhances rock ductility, leading to a decrease in the maximum damage evolution rate. [Xu 2018, pp. 7-8]
3.  **Condition:** Within the proposed Weibull-based coupled TM damage model. **Claim:** The parameter `n` can be used to represent the brittleness of the rock, while `F₀` can be used to represent its peak strength. [Xu 2018, pp. 8-10]

## Candidate Concepts
*   [[Thermal damage]]
*   [[Mechanical damage]]
*   [[Coupled thermo-mechanical (TM) coupling]]
*   [[Weibull distribution]]
*   [[Lemaitre's strain-equivalent principle]]
*   [[Damage evolution]]
*   [[Brittle-ductile transition]]
*   [[Quartz phase transformation]]

## Candidate Methods
*   [[Triaxial compression tests]]
*   [[High-temperature treatment]]
*   [[Damage mechanics modeling]]
*   [[Statistical damage constitutive model]]
*   [[Drucker-Prager failure criterion]]

## Connections To Other Work
The study builds upon and references prior work on TM properties of various rocks (e.g., claystone, sandstone, marble, limestone) and specific studies on granite [Xu 2018, pp. 1-2]. It compares its proposed model framework to other existing damage models for rock listed in Table 1 of the paper [Xu 2018, pp. 2-3]. The model incorporates the Drucker-Prager criterion as an example but notes compatibility with other failure criteria like Mohr-Coulomb and Hoek-Brown [Xu 2018, pp. 5-7].

## Open Questions
1.  How can the model be extended to incorporate plasticity theory and residual strength for more comprehensive engineering application?
2.  How does the model perform for other rock types beyond the specific granite studied?
3.  What is the precise stabilization point for the critical total damage value (D_cr) at high confining pressures, given the limited number of samples tested?

## Source Coverage
All non-empty indexed fragments were processed. The compilation used 9 source blocks containing a total of 42,077 characters, achieving a coverage ratio of 1.004105 by characters relative to the indexed text. The source signature is `406fe1182e2eb25d68664738e800d46847878858`.
