---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-zhao-on-the-effective-stress-coefficient-of-single-rough-rock-fractures"
title: "On the Effective Stress Coefficient of Single Rough Rock Fractures."
status: "draft"
source_pdf: "data/papers/On the effective stress coefficient of single rough rock fractures.pdf"
collections:
citation: "Zhao, Zhihong, et al. \"On the Effective Stress Coefficient of Single Rough Rock Fractures.\" *International Journal of Rock Mechanics & Mining Sciences*, vol. 137, 2021, p. 104556. DOI:10.1016/j.ijrmms.2020.104556."
indexed_texts: "8"
indexed_chars: "38712"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "36380"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.93976"
coverage_status: "full-index"
source_signature: "63e82f4e06982f1dd54c5ed38ca5a2fac8e034ec"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:35:58"
---

# On the Effective Stress Coefficient of Single Rough Rock Fractures.

## One-line Summary
A new stress-dependent effective stress coefficient model for single rough water-bearing rock fractures is proposed using initial normal stiffness and maximum normal closure, incorporated into a hydromechanical coupling model that outperforms Terzaghi's law under moderate stress conditions.

## Research Question
How can the effective stress coefficient for single water-bearing rough rock fractures be accurately defined and calculated using easily measured mechanical parameters, and how does it influence hydromechanical coupling behavior?

## Study Area / Data
The study is theoretical and uses published laboratory and in-situ experimental data for validation. Specific data sources include:
- Laboratory data from Chen et al. (2018) [Zhao 2021, pp. 3-3].
- Laboratory data from Xu and Xie (2009), Xie et al. (2011), Vogler et al. (2018), and Shu et al. (2020) [Zhao 2021, pp. 5-6].
- In-situ hydraulic test data from a large artificial fracture in Falkenberg granite [Zhao 2021, pp. 5-6].

## Methods
1.  **Theoretical Derivation:** A new effective stress coefficient (α) model is derived based on the physical meaning of the coefficient as the ratio of the nominal fracture surface occupied by water to the total area. The derivation uses the Barton-Bandis constitutive model for fracture deformation [Zhao 2021, pp. 3-3].
2.  **Model Formulation:** The proposed model for a fully saturated fracture is:
    α = 1 / (1 + (σ_n - p) / (k_n0 * u_nmax)) for σ_n ≥ p, and α = 1 for σ_n < p.
    This is incorporated into a hydromechanical coupling model [Zhao 2021, pp. 3-3].
3.  **Validation:** The model is verified by fitting experimental data of effective stress coefficients, normal displacement vs. water pressure, and normal displacement vs. normal stress from multiple cited studies [Zhao 2021, pp. 3-5, 5-6].
4.  **Comparison:** Model predictions are compared against those using Terzaghi's effective stress law (σ' = σ - p) [Zhao 2021, pp. 3-5, 5-6].

## Key Findings
1.  The effective stress coefficient for a single rough rock fracture is less than 1 and decreases with an increasing difference between normal stress and water pressure [Zhao 2021, pp. 1-2, 7-8].
2.  The newly proposed model, which incorporates the stress-dependent effective stress coefficient, provides a better fit to experimental normal displacement data than Terzaghi's law, especially under moderate normal stress conditions [Zhao 2021, pp. 3-5, 5-6].
3.  When normal stress is close to or considerably higher than fracture water pressure, both the new model and Terzaghi's model yield similar normal displacement predictions [Zhao 2021, pp. 1-2, 5-6].
4.  The model was successfully validated against both laboratory and in-situ hydraulic test data [Zhao 2021, pp. 5-6].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| The effective stress coefficient (α) is defined as the ratio of the nominal fracture surface occupied by water to the total fracture surface area. | [Zhao 2021, pp. 1-2] | Single rough rock fracture, fully saturated. | Provides the physical basis for the new model. |
| A new model for α is proposed: α = 1 / (1 + (σ_n - p) / (k_n0 * u_nmax)) for σ_n ≥ p. | [Zhao 2021, pp. 3-3] | Fully saturated rough rock fracture under normal stress. | Key equation of the study, derived from Barton-Bandis model. |
| The model was validated using experimental data from Chen et al. (2018), showing good agreement for effective stress coefficient and normal displacement. | [Zhao 2021, pp. 3-3, 3-5] | Laboratory tests on a single rock fracture. | Fitting parameters: k_n0 = 42 GPa/m, u_nmax = 113.8 μm. |
| The new model provides a better fit (higher R²) to normal displacement vs. water pressure data than Terzaghi's law. | [Zhao 2021, pp. 3-5] | σ_n = 7.5, 10, 12, 15 MPa. | R² values for the new model range from 0.550 to 0.805. |
| The model was also validated against in-situ hydraulic test data from the Falkenberg granite fracture. | [Zhao 2021, pp. 5-6] | σ_n = 4.4 MPa, p = 2.49–4.36 MPa. | Fitting parameters: k_n0 = 2.41 GPa/m, u_nmax = 1.58 mm. |
| The difference in predicted normal displacement between the new model and Terzaghi's law is significant under moderate normal stress. | [Zhao 2021, pp. 5-6] | When σ_n is not close to or much higher than p. | Terzaghi's law may overstate the role of water pressure. |

## Limitations
1.  The study assumes isotropic compressive stress conditions and neglects shear stress [Zhao 2021, pp. 6-7].
2.  Fracture water pressure is assumed to be uniformly distributed, which is not reasonable for large rock fractures [Zhao 2021, pp. 6-7].
3.  The model is only applied to saturated rough rock fractures; the effective stress law for unsaturated fractures requires further verification [Zhao 2021, pp. 6-7].
4.  The model does not account for crack initiation, propagation, or shear slip of pre-existing fractures during hydraulic stimulation [Zhao 2021, pp. 6-7].

## Assumptions / Conditions
1.  The rock fracture is composed of two surfaces with heterogeneous asperities and void space [Zhao 2021, pp. 2-3].
2.  Isotropic compressive stress conditions are considered, neglecting shear stress [Zhao 2021, pp. 2-3].
3.  The Barton-Bandis model adequately describes the nonlinear normal stress-displacement behavior of the fracture [Zhao 2021, pp. 3-3].
4.  For the saturated case, the fracture is fully saturated with water (S_r = 1) [Zhao 2021, pp. 3-3].

## Key Variables / Parameters
- **σ_n**: Total external normal stress.
- **p**: Fracture water pressure.
- **σ'_n**: Effective normal stress.
- **α**: Effective stress coefficient for saturated fractures.
- **χ**: Effective stress parameter for partially saturated fractures.
- **k_n0**: Initial normal stiffness of the fracture.
- **u_nmax**: Maximum normal closure of the fracture.
- **S_c**: Contact ratio (contact area / total area).
- **S_r**: Water saturation in the fracture.

## Reusable Claims
1.  **Claim:** The effective stress coefficient for a single rough rock fracture is stress-dependent and can be calculated using the initial normal stiffness and maximum normal closure.
    **Condition:** For a fully saturated rough rock fracture under normal compression.
    **Limitation:** Assumes isotropic stress and uniform water pressure; does not account for shear or complex stress states.
2.  **Claim:** Using Terzaghi's effective stress law (σ' = σ - p) for rough rock fractures under moderate normal stress can overestimate the role of water pressure, leading to underestimation of normal deformation and overestimation of permeability changes.
    **Condition:** When the normal stress is not close to or much higher than the fracture water pressure.
    **Limitation:** Based on theoretical model validation against specific experimental datasets.
3.  **Claim:** Incorporating a stress-dependent effective stress coefficient into hydromechanical models improves the prediction of fracture normal displacement compared to using Terzaghi's law.
    **Condition:** For single rough rock fractures under varying normal stress and water pressure.
    **Limitation:** Model accuracy depends on correct determination of k_n0 and u_nmax for the specific fracture.

## Candidate Concepts
- [[effective stress coefficient]]
- [[hydromechanical coupling]]
- [[rough rock fracture]]
- [[contact ratio]]
- [[Barton-Bandis model]]
- [[normal stiffness]]
- [[maximum normal closure]]
- [[Terzaghi's effective stress law]]

## Candidate Methods
- [[Barton-Bandis constitutive model]]
- [[effective stress law derivation]]
- [[hydromechanical model validation]]
- [[fracture normal displacement calculation]]

## Connections To Other Work
- The study builds upon and modifies the effective stress coefficient expression proposed by Duveau et al. (1997) [Zhao 2021, pp. 1-2].
- It incorporates the Barton-Bandis model (Barton et al., 1985) for fracture deformation [Zhao 2021, pp. 3-3].
- It compares its approach to Terzaghi's effective stress law (Terzaghi, 1923, 1936) [Zhao 2021, pp. 1-2].
- It references and validates against experimental data from multiple studies (e.g., Chen et al., 2018; Xu and Xie, 2009; Vogler et al., 2018) [Zhao 2021, pp. 3-5, 5-6].
- It discusses implications for subsurface engineering problems like CO2 sequestration and geothermal energy extraction [Zhao 2021, pp. 6-7].

## Open Questions
1.  How does the effective stress coefficient behave under combined normal and shear stress conditions?
2.  How can the model be extended to account for non-uniform water pressure distribution in large fractures?
3.  How does the effective stress coefficient evolve in unsaturated rough rock fractures?
4.  How do processes like crack initiation, propagation, and shear slip during hydraulic stimulation affect the effective stress coefficient in fractured rock masses?

## Source Coverage
All non-empty indexed fragments were processed. The compilation is based on 8 indexed fragments containing 38,712 characters. The compiled page uses information from all 8 source blocks, resulting in a coverage ratio of 1.0 by blocks and 0.94 by characters.
