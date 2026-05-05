---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-chen-the-influence-of-fracture-geometry-variation-on-non-darcy-flow-in-fractures-under-conf"
title: "The Influence of Fracture Geometry Variation on Non-Darcy Flow in Fractures under Confining Stresses."
status: "draft"
source_pdf: "data/papers/The influence of fracture geometry variation on non-Darcy flow in fractures under confining stresses.pdf"
collections:
citation: "Chen, Yuedu, et al. \"The Influence of Fracture Geometry Variation on Non-Darcy Flow in Fractures under Confining Stresses.\" *International Journal of Rock Mechanics and Mining Sciences*, vol. 113, 2019, pp. 59-71, doi:10.1016/j.ijrmms.2018.11.017."
indexed_texts: "11"
indexed_chars: "54542"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "54774"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004254"
coverage_status: "full-index"
source_signature: "3f842052fc0d22cb5a9afda263425ef6db831222"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:40:37"
---

# The Influence of Fracture Geometry Variation on Non-Darcy Flow in Fractures under Confining Stresses.

## One-line Summary
This study experimentally demonstrates that variations in fracture geometry, specifically surface roughness and the heterogeneous distribution of interconnected void areas, significantly influence non-Darcy flow behavior under confining stress, and proposes quantitative models linking these geometric characteristics to Forchheimer's equation coefficients and the critical Reynolds number.

## Research Question
How do the geometric characteristics of deformable rough fractures under confining stresses influence the behaviors of non-Darcy flow, and can quantitative relationships be established between these geometric properties and the parameters governing non-Darcy flow (Forchheimer's coefficients and critical Reynolds number)? [Chen 2019, pp. 1-1]

## Study Area / Data
The experimental data were obtained from hydraulic tests on four cylindrical fractured sandstone specimens (Φ50mm×100mm) with two different grain sizes (fine: FA, FB; coarse: CA, CB). The sandstone blocks were sourced from sedimentary strata at depths between 100m and 150m in the Xiegou coal mine in Shanxi Province, China. [Chen 2019, pp. 5-5] The data include relationships between hydraulic gradient and flow rate under various confining stresses, and 3D scanned morphology of the rough fracture surfaces. [Chen 2019, pp. 5-5]

## Methods
A servo-controlled tri-axial system was used to conduct hydraulic tests through the fractured samples under various normal compressive stresses. [Chen 2019, pp. 5-5] Fracture surface geometry was characterized using the peak asperity height (ξ) calculated from scanned profiles. [Chen 2019, pp. 7-8] The interior geometric characteristics, representing the heterogeneity of interconnected void areas, were quantified using the box-counting method to calculate the fractal dimension (D). [Chen 2019, pp. 8-10] The experimental pressure gradient (ΔP) versus flow rate (Q) data were fitted to the Forchheimer's equation (ΔP = AQ + BQ²) to obtain coefficients A and B. [Chen 2019, pp. 5-7] Empirical models were then developed to relate the non-Darcy coefficient (β) and critical Reynolds number (Re_c) to the geometric parameters ξ, D, and hydraulic aperture (e_h). [Chen 2019, pp. 8-10]

## Key Findings
1.  The Forchheimer's equation provides a good description of non-Darcy flow in rough fractures, with correlation coefficients R² of 0.998 observed in the experimental data. [Chen 2019, pp. 5-7]
2.  The coefficients A and B in Forchheimer's equation are sensitive to fracture geometric characteristics and increase with rising confining stress, primarily due to the reduction of hydraulic aperture and the increased heterogeneity of interconnected void areas. [Chen 2019, pp. 1-1, 5-7]
3.  The fractal dimension D of the heterogeneous distribution of interconnected void areas increases with confining stress and shows a power-law relationship with the hydraulic aperture ratio (e_h/e_0). [Chen 2019, pp. 8-10]
4.  A quantitative model was proposed for the non-Darcy coefficient β that incorporates both surface (peak asperity height ξ) and interior (fractal dimension D) geometric characteristics. This model was used to represent the nonlinear coefficient B and the critical Reynolds number Re_c. [Chen 2019, pp. 8-10]
5.  The critical Reynolds number Re_c decreases as the hydraulic aperture e_h increases, with maximum values below 4 in the experiments. [Chen 2019, pp. 10-12]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Forchheimer's equation fits ΔP vs. Q data with R² = 0.998. | [Chen 2019, pp. 5-7] | Specimen FA at 5 MPa confining stress. | Demonstrates the equation's adequacy for describing non-Darcy flow. |
| Coefficients A and B increase with confining stress for all specimens. | [Chen 2019, pp. 5-7] | All four sandstone specimens (FA, FB, CA, CB) under varying confining stresses. | Attributed to reduced hydraulic aperture and more heterogeneous void distribution. |
| Fractal dimension D increases with confining stress, following D = a + b·exp(σ_n). | [Chen 2019, pp. 8-10] | All specimens from 0 to 21 MPa confining stress. | R² for fits > 90%. Indicates increased heterogeneity of flow paths under stress. |
| D shows a power-law relationship with hydraulic aperture ratio: D = p·(e_h/e_0)^q. | [Chen 2019, pp. 8-10] | All specimens. | Parameters p (2.032-2.253) and q (0.025-0.043) vary in a narrow range; R² > 92%. |
| Proposed model for β: β = f(D) = c·log(e_0/e_h) + m·(e_h/e_0)^n + d. | [Chen 2019, pp. 8-10] | Derived from experimental data. | Model incorporates both surface (via e_h) and interior (via D) geometry. |
| Critical Reynolds number Re_c decreases as hydraulic aperture e_h increases. | [Chen 2019, pp. 10-12] | Experimental data from all specimens and data from Chen et al. (2015). | Maximum Re_c < 4. Validated model predictions against experimental data. |

## Limitations
1.  Non-Darcy flow behavior was not clearly observed in experiments at very high confining stresses due to the considerable decrease in fracture aperture and fluid conductivity. [Chen 2019, pp. 5-7]
2.  The empirical models (Eqs. 16 and 17) were validated with lab data, but it is not certain that the model parameters are applicable to all rock types. The range of parameter values for different rocks needs further study. [Chen 2019, pp. 10-12]
3.  The accurate estimation of model parameters at the field scale is more challenging than in lab tests, and upscaling from laboratory-scale to field-scale fractured geological media remains to be explored. [Chen 2019, pp. 10-12]

## Assumptions / Conditions
1.  The injected purified water was assumed to be incompressible. Tests were conducted under isothermal conditions at 25°C. [Chen 2019, pp. 5-5]
2.  Contact areas within the fracture were defined as regions with an aperture below 10 µm; remaining regions (aperture > 10 µm) were considered void spaces. [Chen 2019, pp. 5-5]
3.  Isolated void spaces surrounded by contact regions, which do not contribute to flow seepage, were identified and precluded from the analysis of interconnected void areas. [Chen 2019, pp. 5-5]
4.  The hydraulic aperture e_h was defined as a unique value representing intrinsic permeability, calculated from the linear (Darcy) region of the ΔP vs. Q curve, and is independent of flow rate. [Chen 2019, pp. 7-8]

## Key Variables / Parameters
-   **Hydraulic gradient (ΔP)**: Pressure gradient along the flow direction.
-   **Flow rate (Q)**: Volumetric flow rate.
-   **Confining stress (σ_n)**: Normal compressive stress applied to the fracture.
-   **Hydraulic aperture (e_h)**: Aperture of a smooth parallel-plate fracture with equivalent flow capacity.
-   **Peak asperity height (ξ)**: Surface geometric characteristic (Z_max - Z_min).
-   **Fractal dimension (D)**: Interior geometric characteristic quantifying heterogeneity of interconnected void areas.
-   **Forchheimer coefficients (A, B)**: Linear and nonlinear coefficients in ΔP = AQ + BQ².
-   **Non-Darcy coefficient (β)**: Parameter in B = βρA_h/(2w), related to fracture geometry.
-   **Critical Reynolds number (Re_c)**: Reynolds number marking the onset of non-Darcy flow.

## Reusable Claims
-   Forchheimer's equation adequately describes non-Darcy flow in rough fractures with R² > 0.998 under tested laboratory conditions. [Chen 2019, pp. 5-7]
-   The fractal dimension D of interconnected void areas increases with confining stress, following an exponential relationship D = a + b·exp(σ_n). [Chen 2019, pp. 8-10]
-   The non-Darcy coefficient β can be modeled as a function of both the hydraulic aperture ratio (e_h/e_0) and the fractal dimension D, incorporating surface and interior geometry effects. [Chen 2019, pp. 8-10]
-   The critical Reynolds number Re_c for the onset of non-Darcy flow in rough fractures decreases as the hydraulic aperture increases, with observed values below 4. [Chen 2019, pp. 10-12]

## Candidate Concepts
-   [[non-Darcy flow]]
-   [[Forchheimer's equation]]
-   [[fractal dimension]]
-   [[hydraulic aperture]]
-   [[confining stress]]
-   [[rough fracture]]
-   [[interconnected void areas]]
-   [[critical Reynolds number]]
-   [[peak asperity height]]

## Candidate Methods
-   [[box-counting method]]
-   [[Brazilian tensile method]]
-   [[3D scanning]]
-   [[point-cloud data matching]]
-   [[hydraulic testing]]
-   [[triaxial testing]]

## Connections To Other Work
-   The study builds on the use of Forchheimer's law for non-Darcy flow description, referencing its wide application in the field. [Chen 2019, pp. 1-1]
-   It addresses the insufficiency of surface roughness alone (e.g., peak asperity height) to characterize flow, highlighting the importance of interior void space distribution, as suggested by other studies. [Chen 2019, pp. 1-3]
-   The experimental methodology and data analysis for laminar flow in fractures were adopted from the authors' previous work (Chen et al., 2017). [Chen 2019, pp. 5-5]
-   The proposed models were validated not only with the authors' data but also with experimental data from Chen et al. (2015) conducted at higher confining stresses. [Chen 2019, pp. 10-12]

## Open Questions
-   What is the range of values for the model parameters (m, n, c, d, p, q) across different rock types? [Chen 2019, pp. 10-12]
-   How can the proposed laboratory-scale models be accurately upscaled to field-scale fractured geological media? [Chen 2019, pp. 10-12]

## Source Coverage
All non-empty indexed fragments were processed. The compilation is based on 11 indexed source blocks containing 54,542 characters, achieving a coverage ratio of 1.0 by blocks and 1.004 by characters. The source signature is `3f842052fc0d22cb5a9afda263425ef6db831222`, and the coverage status is `full-index`.
