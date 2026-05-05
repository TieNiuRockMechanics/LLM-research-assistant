---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2015-ishibashi-beyond-laboratory-scale-prediction-for-channeling-flows-through-subsurface-rock-f"
title: "Beyond-Laboratory-Scale Prediction for Channeling Flows through Subsurface Rock Fractures with Heterogeneous Aperture Distributions Revealed by Laboratory Evaluation."
status: "draft"
source_pdf: "data/papers/Beyond-laboratory-scale prediction for channeling flows through subsurface rock fractures with heterogeneous aperture distributions revealed by laboratory evaluation.pdf"
collections:
citation: "Ishibashi, Takuya, et al. “Beyond-Laboratory-Scale Prediction for Channeling Flows through Subsurface Rock Fractures with Heterogeneous Aperture Distributions Revealed by Laboratory Evaluation.” *Journal of Geophysical Research: Solid Earth*, 2015, doi:10.1002/2014JB011555. Accessed 2026."
indexed_texts: "17"
indexed_chars: "83596"
nonempty_source_blocks: "17"
compiled_source_blocks: "17"
compiled_source_chars: "84049"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.005419"
coverage_status: "full-index"
source_signature: "013d2c7e47af528fb76e191c4320597b01bf6990"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:32:45"
---

# Beyond-Laboratory-Scale Prediction for Channeling Flows through Subsurface Rock Fractures with Heterogeneous Aperture Distributions Revealed by Laboratory Evaluation.

## One-line Summary
A method is developed to predict fracture aperture distributions and channeling flows beyond laboratory scale by combining the self-affine fractal nature of fracture surfaces with the scale-independent contact area revealed through laboratory experiments.

## Research Question
How do fracture aperture distributions and resulting fluid flow characteristics (e.g., permeability, channeling) change with scale, and can these scale dependencies be predicted beyond laboratory scales?

## Study Area / Data
Laboratory experiments were conducted on cylindrical samples of Inada medium-grained granite (Ibaraki Prefecture, Japan) containing single tensile fractures of sizes 0.05 m × 0.075 m, 0.1 m × 0.15 m, and 0.2 m × 0.3 m. Fractures were prepared with either no shear displacement or a 5 mm shear displacement. Experiments were performed under confining stresses of 10, 20, and 30 MPa [Ishibashi 2015, pp. 2-4].

## Methods
1.  **Laboratory Evaluation:** Fracture surface topography was measured with a laser profilometer (0.25 mm grid resolution). Permeability was measured via unidirectional fluid flow experiments under confining stress. 2-D aperture distributions were numerically determined using a permeability matching method, where surfaces are brought into contact to match the experimentally measured permeability [Ishibashi 2015, pp. 4-6].
2.  **Numerical Prediction Beyond Lab Scale:** A method was developed to predict aperture distributions for larger fractures. It uses the self-affine fractal nature of fracture surfaces (modeled via a spectral method) and the finding that contact area is scale-independent. Pairs of fractal surfaces are created and placed in contact to achieve the scale-independent contact area [Ishibashi 2015, pp. 6-7].
3.  **Fluid Flow Simulation:** Fluid flow through the determined or predicted aperture distributions was simulated by solving the Reynolds equation for steady-state laminar flow using a finite difference method [Ishibashi 2015, pp. 5-6].

## Key Findings
1.  The contact area in fracture planes was found to be virtually independent of scale for both joints (fractures without shear displacement) and faults (fractures with shear displacement). The contact areas are approximately 60% for joints and 40% for faults [Ishibashi 2015, pp. 8-9, 12-14].
2.  Aperture distributions are characterized by a scale-independent contact area, a scale-dependent geometric mean aperture, and a scale-independent geometric standard deviation (approximately 3) [Ishibashi 2015, pp. 12-14].
3.  Fluid flows are characterized by the formation of preferential flow paths (channeling flows) with a scale-independent flow area of approximately 10% of the fracture plane [Ishibashi 2015, pp. 12-14].
4.  The geometric mean aperture (μm) and permeability (m²) scale with fracture length (m, *l*) according to:
    *   Joints: *e_m, joint* = 1×10² *l*⁰·¹, *k_joint* = 1×10⁻¹² *l*⁰·²
    *   Faults: *e_m, fault* = 1×10³ *l*⁰·⁷, *k_fault* = 1×10⁻⁸ *l*¹·¹ [Ishibashi 2015, pp. 12-14].
5.  The prediction method was validated by reproducing laboratory results and matching the maximum aperture-fracture length relations reported for natural joints and faults in the literature [Ishibashi 2015, pp. 10-12].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Contact area is scale-independent (~60% for joints, ~40% for faults). | [Ishibashi 2015, pp. 8-9, 12-14] | Granite fractures under confining stress (10-30 MPa). | Key finding enabling the prediction method. |
| Aperture distributions are lognormal-like with a scale-independent geometric standard deviation (~3). | [Ishibashi 2015, pp. 7-8, 12-14] | Laboratory and predicted fractures. | Characterizes the heterogeneity of the aperture field. |
| Channeling flow occurs with a scale-independent flow area (~10%). | [Ishibashi 2015, pp. 12-14] | Laboratory and predicted fractures. | Demonstrates significant deviation from parallel plate model. |
| Permeability scaling: *k_joint* ∝ *l*⁰·², *k_fault* ∝ *l*¹·¹. | [Ishibashi 2015, pp. 12-14] | Predicted fractures under confining stress. | Derived from the novel prediction method. |
| Prediction method reproduces lab results and natural fracture scaling laws. | [Ishibashi 2015, pp. 10-12] | Comparison with lab data and literature on natural fractures. | Validates the method for extrapolation beyond lab scale. |

## Limitations
1.  The prediction method assumes the contact area remains constant under confining stress, which may not hold under very high pressures or temperatures where surface smoothing or gouge formation occurs [Ishibashi 2015, pp. 14-15].
2.  The Reynolds equation used for flow simulation may overestimate permeability by a factor of 1.3-1.6, though this is assumed to be consistent across scales [Ishibashi 2015, pp. 5-6].
3.  The study focuses on flow perpendicular to shear displacement; the scale-dependent anisotropy of permeability is not fully resolved [Ishibashi 2015, pp. 14-15].
4.  The method's applicability is constrained to confining stresses up to approximately 100 MPa [Ishibashi 2015, pp. 12-14].

## Assumptions / Conditions
1.  Fracture surfaces exhibit self-affine fractal behavior from laboratory to field scales [Ishibashi 2015, pp. 6-7].
2.  The contact area between fracture surfaces is independent of scale under given stress conditions [Ishibashi 2015, pp. 8-9].
3.  The Reynolds equation adequately describes laminar flow in rough-walled fractures for the purpose of evaluating scaling trends [Ishibashi 2015, pp. 5-6].
4.  Deformation of contacting asperities is not explicitly modeled; overlapping asperities are treated as regions of zero aperture [Ishibashi 2015, pp. 5-6].

## Key Variables / Parameters
*   **Contact Area:** Percentage of fracture plane where aperture is zero. Scale-independent.
*   **Geometric Mean Aperture (*e_m*):** Representative aperture of the nonzero aperture distribution. Scale-dependent.
*   **Geometric Standard Deviation:** Measure of aperture heterogeneity. Scale-independent (~3).
*   **Flow Area:** Percentage of fracture plane contributing to significant flow. Scale-independent (~10%).
*   **Fracture Permeability (*k*):** Hydraulic conductivity of the fracture. Scale-dependent.
*   **Fracture Length (*l*):** Characteristic scale of the fracture.
*   **Fractal Dimension (*D*):** Describes the roughness scaling of the fracture surface (2.3 for the studied granite) [Ishibashi 2015, pp. 6-7].
*   **Mismatch Length Scale (*λ_c*):** Wavelength above which fracture surfaces become mated (0.7 mm for the studied granite) [Ishibashi 2015, pp. 6-7].

## Reusable Claims
1.  Under confining stress, the contact area in granite fractures is approximately 60% for joints and 40% for faults, and this value is independent of fracture scale [Ishibashi 2015, pp. 8-9, 12-14].
2.  The geometric mean aperture of joints and faults increases with fracture length (*l*) following power laws: *e_m, joint* = 1×10² *l*⁰·¹ μm and *e_m, fault* = 1×10³ *l*⁰·⁷ μm [Ishibashi 2015, pp. 12-14].
3.  The permeability of joints and faults increases with fracture length (*l*) following power laws: *k_joint* = 1×10⁻¹² *l*⁰·² m² and *k_fault* = 1×10⁻⁸ *l*¹·¹ m² [Ishibashi 2015, pp. 12-14].
4.  Channeling flow is a fundamental characteristic of fluid flow through rock fractures at all scales, with only about 10% of the fracture plane area conducting the majority of the flow [Ishibashi 2015, pp. 12-14].
5.  A fracture aperture distribution for any scale can be predicted by placing two numerically generated self-affine fractal surfaces in contact to achieve a target scale-independent contact area [Ishibashi 2015, pp. 6-7].

## Candidate Concepts
*   [[Channeling flow]]
*   [[Self-affine fractal]]
*   [[Fracture aperture distribution]]
*   [[Scale dependency]]
*   [[Contact area]]
*   [[Discrete fracture network (DFN)]]
*   [[Hydraulic aperture]]
*   [[Reynolds equation]]

## Candidate Methods
*   [[Permeability matching method]]
*   [[Spectral method for fractal surface generation]]
*   [[Numerical flow simulation via Reynolds equation]]
*   [[Laser profilometry for surface topography]]

## Connections To Other Work
*   Builds upon the development of the GeoFlow simulator for 3-D channeling flow in fracture networks [Ishibashi 2015, pp. 1-2].
*   Extends prior work on fracture surface roughness being self-affine fractals [Brown 1987a; Power et al. 1987].
*   Validates findings against field-observed maximum aperture-length scaling laws for joints and faults [Schlische et al. 1996; Schultz et al. 2008].
*   Compares predicted flow areas with those from field investigations at the Stripa mine [Abelin et al. 1985].
*   Discusses inconsistencies with earlier studies on scale-dependent permeability [Witherspoon et al. 1979; Raven and Gale 1985].

## Open Questions
1.  How does the anisotropy of fracture permeability (parallel vs. perpendicular to shear) change with scale under confining stress? [Ishibashi 2015, pp. 14-15]
2.  How do the scale dependencies change under conditions of very high confining stress (>100 MPa) or high temperature where surface alteration occurs? [Ishibashi 2015, pp. 14-15]
3.  Can the method be extended to fractures with more complex shear histories or different rock types?

## Source Coverage
All 17 non-empty indexed fragments were processed. The compiled source blocks total 17, with a compiled character count of 84,049. The coverage ratio by blocks is 1.0 and by characters is 1.005419, indicating full-index coverage.
