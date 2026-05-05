---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2017-ma-the-in-situ-stress-seismic-prediction-method-based-on-the-theory-of-orthorhombic-anisotr"
title: "The In-Situ Stress Seismic Prediction Method Based on the Theory of Orthorhombic Anisotropic Media."
status: "draft"
source_pdf: "data/papers/2017 - 基于正交各向异性介质理论的地应力地震预测方法.pdf"
collections:
  - "part4-2"
citation: "Ma, Ni, et al. \"The In-Situ Stress Seismic Prediction Method Based on the Theory of Orthorhombic Anisotropic Media.\" *Chinese Journal of Geophysics*, vol. 60, no. 12, 2017, pp. 4766-4775, doi:10.6038/cjg20171218."
indexed_texts: "8"
indexed_chars: "39505"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "37611"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.952057"
coverage_status: "full-index"
source_signature: "875244d0d17830a604b489090e32a27c2ea76ffc"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:06:29"
---

# The In-Situ Stress Seismic Prediction Method Based on the Theory of Orthorhombic Anisotropic Media.

## One-line Summary
This paper derives a new formula for the Orthorhombic Differential Horizontal Stress Ratio (ODHSR) based on orthorhombic anisotropic media theory, which simultaneously considers the effects of vertical transverse isotropy (VTI) and horizontal transverse isotropy (HTI) to improve in-situ stress prediction for shale gas reservoirs.

## Research Question
How can in-situ stress prediction for shale gas reservoirs be improved by accounting for both the vertical layering (VTI) and aligned vertical fractures (HTI) present in actual shale formations, which are not fully captured by existing methods based solely on HTI media?

## Study Area / Data
The study uses well log data from Well A in a shale gas reservoir in eastern China. The data includes P-wave velocity (V_P0), S-wave velocity (V_S0), density (ρ), and anisotropic parameters: HTI parameters ε^(V), δ^(V), γ^(V) estimated from a fracture rock physics model, and the VTI parameter γ [Ma 2017, pp. 6-9].

## Methods
1.  **Constitutive Equation Derivation:** The stress-strain constitutive equation for orthorhombic anisotropic (OA) media is derived using the general form of Hooke's law [Ma 2017, pp. 2-3].
2.  **Stress Formula Derivation:** Assuming zero horizontal strain (ε_x = ε_y = 0), the maximum (σ_y) and minimum (σ_x) horizontal stresses are expressed in terms of the vertical stress (σ_z) and the OA medium's compliance coefficients [Ma 2017, pp. 3-5].
3.  **ODHSR Definition:** The Orthorhombic Differential Horizontal Stress Ratio (ODHSR) is defined as (σ_y - σ_x)/σ_y and derived as a function of the OA medium's elastic constants [Ma 2017, pp. 3-5].
4.  **Approximation via Linear Slip Theory:** An approximate, more practical formula for ODHSR is derived by modeling the OA medium as a VTI background with a perturbation of aligned fractures, using the linear slip theory of Schoenberg and Sayers [Ma 2017, pp. 5-6].
5.  **Validation:** The exact ODHSR formula is validated by degenerating it to the HTI case and comparing the resulting DHSR with Gray's (2011) DHSR formula. The approximate ODHSR is also compared to Gray's DHSR using well data [Ma 2017, pp. 5-6, 6-9].

## Key Findings
1.  The derived ODHSR formula explicitly incorporates parameters from both VTI and HTI media, making it more representative of actual shale formations than the existing DHSR based only on HTI [Ma 2017, pp. 3-5].
2.  When degenerated to the HTI case, the exact ODHSR formula yields a DHSR expression identical to that derived directly from the HTI constitutive equations, proving its correctness and eliminating approximation errors present in Gray's method [Ma 2017, pp. 5-6].
3.  The approximate ODHSR formula, derived using linear slip theory, shows trends consistent with Gray's DHSR, with differences attributed to the influence of VTI anisotropy (parameter γ) [Ma 2017, pp. 6-9].
4.  Low ODHSR values indicate regions where the minimum and maximum horizontal stresses are close, suggesting a higher likelihood of forming a complex fracture network during hydraulic fracturing, which is favorable for shale gas development [Ma 2017, pp. 3-5].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Derivation of OA medium constitutive equation and stress-strain relations using Hooke's law. | [Ma 2017, pp. 2-3] | General elastic deformation range. | Foundation for stress formulas. |
| Formula for ODHSR in terms of OA compliance coefficients (s_ij). | [Ma 2017, pp. 3-5] | Assumes zero horizontal strain (ε_x = ε_y = 0). | Exact but complex formula. |
| Approximate ODHSR formula: ODHSR ≈ (2V_S0²ρ(2γ+1)Z_N) / (1 + 2V_S0²ρ(2γ+1)Z_N). | [Ma 2017, pp. 5-6] | Derived using linear slip theory (S = S_v + S_f). | More practical for application. |
| Degeneration of exact ODHSR to HTI DHSR matches Gray's (2011) DHSR formula. | [Ma 2017, pp. 5-6] | VTI anisotropy parameters set to zero (ε=δ=γ=0). | Validates the exact ODHSR derivation. |
| Comparison of approximate ODHSR and Gray's DHSR using Well A data shows consistent trends. | [Ma 2017, pp. 6-9] | Uses measured elastic and anisotropic parameters from Well A. | Differences are attributed to VTI influence (γ). |

## Limitations
1.  The derivation assumes zero horizontal strain, meaning the formula is applicable only to shale reservoirs with simple tectonic settings where this assumption holds [Ma 2017, pp. 3-5, 6-9].
2.  The exact ODHSR formula is complex and not convenient for direct practical application [Ma 2017, pp. 5-6].
3.  The method does not account for the influence of tectonic stress, which is noted as an area for future research [Ma 2017, pp. 6-9].

## Assumptions / Conditions
1.  The rock is bounded and cannot move, leading to the assumption of zero horizontal strain (ε_x = ε_y = 0) [Ma 2017, pp. 3-5].
2.  The shale formation is modeled as an orthorhombic anisotropic medium, composed of horizontally layered minerals (VTI background) and aligned vertical fractures (HTI perturbation) [Ma 2017, pp. 2-3, 5-6].
3.  The approximate formula relies on the linear slip theory, which treats fractures as displacement discontinuities [Ma 2017, pp. 5-6].

## Key Variables / Parameters
*   **σ_x, σ_y, σ_z:** Minimum, maximum, and vertical principal stresses.
*   **ODHSR:** Orthorhombic Differential Horizontal Stress Ratio, (σ_y - σ_x)/σ_y.
*   **DHSR:** Differential Horizontal Stress Ratio (for HTI media).
*   **V_P0, V_S0:** Vertical P-wave and S-wave velocities.
*   **ρ:** Density.
*   **ε, δ, γ:** Thomsen's anisotropic parameters for VTI media.
*   **ε^(V), δ^(V), γ^(V):** Anisotropic parameters for HTI media.
*   **Z_N, Z_T:** Normal and tangential fracture compliance (weakness).
*   **s_ij:** Compliance coefficients of the OA medium.
*   **c_ij:** Elastic stiffness constants of the OA medium.

## Reusable Claims
1.  **Claim:** The ODHSR is a more physically representative parameter than the HTI-based DHSR for evaluating the fracturability of shale gas reservoirs because it accounts for both the intrinsic vertical anisotropy (VTI) and stress-induced horizontal anisotropy (HTI). **Condition:** Applicable to shale formations with orthorhombic symmetry. **Limitation:** Assumes zero horizontal strain, limiting use to tectonically simple areas.
2.  **Claim:** Degenerating the orthorhombic stress model to the HTI case yields a DHSR formula that is exact and free from the approximation errors introduced by using linear slip theory directly on Hooke's law, as in Gray's method. **Condition:** Valid for HTI media. **Limitation:** Does not apply to more complex anisotropy.
3.  **Claim:** The approximate ODHSR formula, derived via linear slip theory, provides a practical means to estimate stress ratios from seismic inversion parameters (V_S0, ρ, γ, Z_N). **Condition:** Assumes the OA medium can be approximated as a VTI background plus fracture perturbation. **Limitation:** Accuracy depends on the validity of the linear slip approximation.

## Candidate Concepts
*   [[Orthorhombic anisotropy]]
*   [[Vertical Transverse Isotropy (VTI)]]
*   [[Horizontal Transverse Isotropy (HTI)]]
*   [[In-situ stress]]
*   [[Differential Horizontal Stress Ratio (DHSR)]]
*   [[Shale gas reservoir]]
*   [[Hydraulic fracturing]]
*   [[Linear slip theory]]
*   [[Rock physics]]

## Candidate Methods
*   [[Orthorhombic Differential Horizontal Stress Ratio (ODHSR) calculation]]
*   [[Stress prediction from seismic data]]
*   [[Degeneration of anisotropic models]]
*   [[Approximation via linear slip theory]]

## Connections To Other Work
*   Builds upon and critiques the DHSR concept and method introduced by Gray (2011) for HTI media [Ma 2017, pp. 2-3, 5-6].
*   Uses the parameterization for orthorhombic media proposed by Tsvankin (1997) [Ma 2017, pp. 3-5].
*   Applies the linear slip theory for fractured media from Schoenberg and Sayers (1995) [Ma 2017, pp. 5-6].
*   References prior work on in-situ stress measurement and estimation (e.g., Iverson, 1995; Zoback, 2007) and seismic reservoir characterization methods (e.g., Yin et al., 2014a, 2014b, 2015) [Ma 2017, pp. 2-3, 5-6].

## Open Questions
1.  How can the influence of tectonic stress be incorporated into the ODHSR framework to improve prediction accuracy in complex structural settings?
2.  Can the complex exact ODHSR formula be further simplified or approximated using the orthorhombic anisotropic parameters for more direct application?
3.  How robust is the ODHSR prediction when derived from seismic inversion results, which carry their own uncertainties?

## Source Coverage
All non-empty indexed fragments were processed. The compilation is based on 8 indexed text blocks containing a total of 39,505 characters. The compiled page incorporates content from all 8 source blocks, covering 37,611 characters, resulting in a coverage ratio by characters of 0.952. The coverage status is full-index.
