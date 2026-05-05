---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2017-chen-experimental-study-on-the-effect-of-fracture-geometric-characteristics-on-the-permeabi-c435bf9b"
title: "Experimental Study on the Effect of Fracture Geometric Characteristics on the Permeability in Deformable Rough-Walled Fractures."
status: "draft"
source_pdf: "data/papers/Experimental study on the effect of fracture geometric characteristics on the permeability in deformable rough-walled fractures.pdf"
collections:
citation: "Chen, Yuedu, et al. \"Experimental Study on the Effect of Fracture Geometric Characteristics on the Permeability in Deformable Rough-Walled Fractures.\" *International Journal of Rock Mechanics & Mining Sciences*, vol. 98, 2017, pp. 121-140. doi:10.1016/j.ijrmms.2017.07.003. Accessed 2026."
indexed_texts: "15"
indexed_chars: "72559"
nonempty_source_blocks: "15"
compiled_source_blocks: "15"
compiled_source_chars: "72882"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004452"
coverage_status: "full-index"
source_signature: "c14f96453b468b186029f50d19644c9ccda5f188"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T01:01:51"
---

# Experimental Study on the Effect of Fracture Geometric Characteristics on the Permeability in Deformable Rough-Walled Fractures.

## One-line Summary
This experimental study quantifies the relationship between three fracture geometric characteristics (aperture size of interconnected voids, contact area, and void distribution heterogeneity) and the permeability of deformable rough-walled fractures under varying confining stresses, proposing an improved predictive model.

## Research Question
The study addresses four specific issues: 1) precluding isolated void spaces from the percolation network, 2) quantitatively studying the heterogeneous distribution of interconnected void spaces and its effect on permeability, 3) investigating the variation of fracture geometric characteristics (FGC) with applied stress in deformable fractures, and 4) providing experimental validation for models relating FGC to permeability [Chen 2017, pp. 2-3].

## Study Area / Data
The experimental samples are six single-fractured cylindrical sandstone specimens (Φ50 mm × 100 mm) taken from a depth of 100-150 m at the Xiegou coal mine in Shanxi Province, China [Chen 2017, pp. 6-10]. The samples are divided into three groups based on grain size: fine (FA, FB), medium (MA, MB), and coarse (CA, CB) sandstone [Chen 2017, pp. 6-10]. Mechanical properties (UCS, Young's modulus, Poisson ratio) for each sample are provided in Table 2 [Chen 2017, pp. 5-6].

## Methods
1.  **Fracture Morphology Measurement:** A point-cloud data matching method using a 3D laser scanner (precision 0.01 mm) was developed to obtain the 3D distribution of fracture surfaces without destruction [Chen 2017, pp. 3-5]. The method involves scanning the exterior and fracture surfaces of split sample halves and using coordinate transformation to align them.
2.  **Hydraulic Testing:** High-precision fluid flow tests were conducted in a triaxial cell under a range of confining stresses (σ3). Samples were saturated, and flow was measured using an electronic balance (precision 0.0001 g) and pressure transducers (resolution 0.01 MPa) [Chen 2017, pp. 6-10]. Only the linear (Darcy) flow regime was analyzed.
3.  **FGC Parameter Calculation:**
    *   **Effective Mechanical Aperture (e′m):** Arithmetic average aperture of interconnected void spaces only, with contact defined as points where aperture eI < 10 µm [Chen 2017, pp. 3-5].
    *   **Contact Ratio (ω):** Ratio of contact area (eI < 10 µm) to total fracture area [Chen 2017, pp. 5-6].
    *   **Relative Fractal Dimension (D*Δ):** Represents heterogeneity of interconnected void space distribution. Calculated using a modified Cubic Covering method with an Ultra-Thin Square Plate (UTSP) [Chen 2017, pp. 5-6]. D*Δ = log10(DΔ - DΔ_ref), where DΔ is the absolute fractal dimension and DΔ_ref is its value at σ3 = 0 [Chen 2017, pp. 6-10].
4.  **Modeling:** An improved "FGC model" relating hydraulic aperture (eh) to the three FGC parameters was developed and compared to the classical Yeo model [Chen 2017, pp. 16-18].

## Key Findings
1.  **FGC Evolution with Stress:** As confining stress (σ3) increases, the effective mechanical aperture (e′m) decreases, the contact ratio (ω) increases and stabilizes, and the relative fractal dimension (D*Δ) shows nonlinear growth [Chen 2017, pp. 11-16]. The evolution of each parameter can be fitted with exponential functions (Eqs. 12, 13, 14).
2.  **Model Performance:** The proposed FGC model (Eq. 16: eh = e′m (1 - 1.1ω^4) (1 + 2D*Δ^3/5)) predicts hydraulic aperture values in better agreement with experimental results than the Yeo model (Eq. 15) across all sandstone types and stress levels [Chen 2017, pp. 16-18]. The Yeo model can yield negative hydraulic apertures at high contact ratios.
3.  **Permeability Relationship:** Combining the FGC model with the Cubic Law (k = eh²/12) yields a direct relationship between fracture permeability (k) and the FGC parameters (Eq. 17) [Chen 2017, pp. 16-18].
4.  **Sample-Specific Trends:** Fine sandstones showed the largest reduction in e′m and increase in ω with stress. Coarse sandstones had the smallest changes and largest residual e′m [Chen 2017, pp. 11-16].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| FGC model equation: eh = e′m (1 - 1.1ω^4) (1 + 2D*Δ^3/5) | [Chen 2017, pp. 16-18] | Deformable rough-walled fractures under confining stress | Proposed as an improvement over the Yeo model. |
| Effective mechanical aperture (e′m) decreases exponentially with confining stress (σ3). | [Chen 2017, pp. 11-13] | All six sandstone samples (FA, FB, MA, MB, CA, CB) | Fitted with Eq. 12: e′m = e1 + (e_m+1 - e1) * exp(-σ3/K). |
| Contact ratio (ω) increases and stabilizes with confining stress. | [Chen 2017, pp. 13-16] | All six sandstone samples | Fitted with Eq. 13: ω = ω1 + (ω_n+1 - ω1) * exp(-σ3/K). |
| Relative fractal dimension (D*Δ) shows nonlinear growth with confining stress. | [Chen 2017, pp. 13-16] | All six sandstone samples | Fitted with Eq. 14: D*Δ = a * exp(b * σ3^c). |
| Isolated void spaces (surrounded by contact) do not contribute to flow and are precluded from FGC calculations. | [Chen 2017, pp. 2-3, 3-5] | All analyses | A key methodological distinction from some prior models. |
| The point-cloud data matching method achieves 0.01 mm spatial resolution for fracture morphology. | [Chen 2017, pp. 3-5] | Non-loading condition | Avoids surface destruction. |
| Hydraulic tests confirmed Darcy flow (Reynolds number < 3.5) in the linear regime analyzed. | [Chen 2017, pp. 10-11] | All samples and stress levels | Ensures validity of using Cubic Law-based analysis. |

## Limitations
1.  The study is limited to small-scale, single fractures in sandstone samples from one specific location [Chen 2017, pp. 18-20].
2.  The accurate estimation of FGC representation parameters at the field scale is challenging and remains an open issue [Chen 2017, pp. 16-18].
3.  The analysis focuses only on linear (Darcy) flow; nonlinear flow regimes were observed but not modeled [Chen 2017, pp. 10-11, 18-20].
4.  The contact definition relies on a threshold (10 µm) based on scanner precision, which may not perfectly represent true contact [Chen 2017, pp. 3-5].

## Assumptions / Conditions
1.  Darcy's law is valid for the linear flow regime analyzed [Chen 2017, pp. 10-11].
2.  Contact is defined as points where the measured aperture (eI) is less than 10 µm [Chen 2017, pp. 3-5].
3.  The relative normal displacement between fracture surfaces is macroscopically uniform, and shear sliding is not considered [Chen 2017, pp. 13-16].
4.  The percolation network is constituted only by interconnected void spaces; isolated voids have no effect on seepage [Chen 2017, pp. 2-3, 3-5].

## Key Variables / Parameters
*   **e′m:** Effective mechanical aperture (average aperture of interconnected void spaces) [Chen 2017, pp. 3-5].
*   **ω:** Contact ratio (contact area / total area) [Chen 2017, pp. 5-6].
*   **D*Δ:** Relative fractal dimension (heterogeneity of interconnected void distribution) [Chen 2017, pp. 5-6, 6-10].
*   **σ3:** Confining stress [Chen 2017, pp. 6-10].
*   **eh:** Hydraulic aperture [Chen 2017, pp. 1-2].
*   **k:** Fracture permeability [Chen 2017, pp. 1-2].
*   **K:** Normal stiffness of the fracture [Chen 2017, pp. 11-13].

## Reusable Claims
*   Under increasing confining stress, the effective mechanical aperture of a rough-walled fracture decreases following an exponential decay function, with the rate of decrease dependent on rock grain size and fracture normal stiffness [Chen 2017, pp. 11-13].
*   The contact ratio of a rough-walled fracture increases with confining stress and approaches a residual value, following an exponential function [Chen 2017, pp. 13-16].
*   The heterogeneity of interconnected void spaces, quantified by the relative fractal dimension, increases nonlinearly with confining stress [Chen 2017, pp. 13-16].
*   A model incorporating the effective mechanical aperture, contact ratio, and relative fractal dimension (FGC model) provides a better prediction of hydraulic aperture in deformable rough-walled fractures than models that neglect void heterogeneity or overemphasize contact area effects [Chen 2017, pp. 16-18].
*   Isolated void spaces surrounded by contact regions do not contribute to fluid flow and must be excluded when characterizing the percolation network of a fracture [Chen 2017, pp. 2-3, 3-5].

## Candidate Concepts
*   [[fracture geometric characteristics]]
*   [[rough-walled fracture]]
*   [[effective mechanical aperture]]
*   [[contact ratio]]
*   [[relative fractal dimension]]
*   [[interconnected void spaces]]
*   [[isolated void spaces]]
*   [[hydraulic aperture]]
*   [[fracture permeability]]
*   [[Cubic Law]]
*   [[deformable fracture]]
*   [[confining stress]]

## Candidate Methods
*   [[point-cloud data matching method]]
*   [[UTSP covering method]]
*   [[triaxial hydraulic testing]]
*   [[fractal dimension analysis]]

## Connections To Other Work
*   The study builds upon and critiques the **Cubic Law** for smooth parallel plates [Chen 2017, pp. 1-2].
*   It compares its proposed FGC model directly with the **Yeo model** (Eq. 15), which considers aperture mean, standard deviation, and contact ratio but not void heterogeneity [Chen 2017, pp. 16-18].
*   It references prior work on **tortuosity** (out-of-plane and in-plane) by Cook et al. and Yeo [Chen 2017, pp. 2-3].
*   It acknowledges and builds on methods for measuring fracture morphology, including resin injection, laser profilometry, and X-ray CT, while proposing an alternative [Chen 2017, pp. 3-5].
*   It situates its work within the broader context of fluid flow in fractured rock for applications like geothermal extraction, CO2 sequestration, and contaminant control [Chen 2017, pp. 1-2].

## Open Questions
1.  How can the laboratory-derived relationships between FGC parameters and permeability be upscaled to field-scale fractured rock masses? [Chen 2017, pp. 16-18, 18-20]
2.  How do the FGC and their evolution affect nonlinear flow regimes in rough-walled fractures? [Chen 2017, pp. 18-20]
3.  Can the FGC model be generalized to other rock types and fracture scales beyond the sandstone samples studied? [Chen 2017, pp. 18-20]

## Source Coverage
All 15 non-empty indexed fragments were processed. The compiled source blocks total 15, with a compiled character count of 72,882 against an indexed character count of 72,559, resulting in a coverage ratio by characters of 1.004452. The coverage status is full-index.
