---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-ojeda-discrete-fracture-network-dfn-analysis-to-quantify-the-reliability-of-borehole-derive"
title: "Discrete Fracture Network (DFN) Analysis to Quantify the Reliability of Borehole-Derived Volumetric Fracture Intensity."
status: "draft"
source_pdf: "data/papers/2023 - Discrete Fracture Network (DFN) Analysis to Quantify the Reliability of Borehole-Derived Volumetric Fracture Intensity.pdf"
collections:
  - "2文章钻孔裂缝分形关系"
citation: "Ojeda, Pedro, et al. \"Discrete Fracture Network (DFN) Analysis to Quantify the Reliability of Borehole-Derived Volumetric Fracture Intensity.\" *Geosciences*, vol. 13, no. 6, 2023, article 187. doi:10.3390/geosciences13060187."
indexed_texts: "20"
indexed_chars: "98121"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T12:02:20"
---

# Discrete Fracture Network (DFN) Analysis to Quantify the Reliability of Borehole-Derived Volumetric Fracture Intensity.

## One-line Summary
This paper uses Discrete Fracture Network (DFN) models to investigate the reliability of estimating 3D volumetric fracture intensity (P32) from 1D borehole data, focusing on the effects of Terzaghi weighting angular cut-offs, sampling interval length, and boundary effects in synthetic models [Ojeda 2023, pp. 1-2].

## Research Question
How reliable are borehole-derived estimates of volumetric fracture intensity (P32), and how do common industry practices—such as limiting the minimum intersection angle for Terzaghi Weighting, choosing sampling interval lengths, and handling boundary effects in DFN models—affect this reliability? [Ojeda 2023, pp. 1-2]

## Study Area / Data
This study is based on synthetic DFN models rather than a specific field site. Fracture orientations for these models were bootstrapped using a concentration parameter of 80 from what appears to be 563 poles of oriented fracture data from an unspecified source; the stereonet included Terzaghi weighting [Ojeda 2023, pp. 5-6].

## Methods
The core methodology is numerical modelling using DFNs generated in FracMan [Ojeda 2023, pp. 3-5]. The estimation of P32 from borehole data is based on the Terzaghi-weighted correction proposed by Chilès et al., which is expressed for a scanline of length L as ˆP32 = 1/L ∑ 1/|cos(ω_i − β_i)| [Ojeda 2023, pp. 2-3]. The authors investigated:
*   **Boundary effects:** P32 was calculated on progressively smaller sampling boxes within a larger generation volume to quantify the discrepancy between target and sampled intensities [Ojeda 2023, pp. 3-5].
*   **Spatial generation methods:** Two approaches for fracture location were compared: generating fractures by their centre points vs. by random surface points [Ojeda 2023, pp. 3-5].
*   **Model convergence:** The cumulative average of P32 was tracked over up to 100 realizations to determine the number of realizations needed for stability [Ojeda 2023, pp. 7-8].
*   **Impact of angular cut-off:** The effect of limiting the minimum angle between the borehole and intersected fractures on the calculated P32 was analyzed [Ojeda 2023, pp. 1-2].

## Key Findings
*   **Limiting the minimum intersection angle for Terzaghi Weighting leads to an underestimation of the calculated P32** [Ojeda 2023, pp. 1-2]. This finding challenges a common industry practice.
*   **The size of the sampling interval has a significant impact on the variability of the calculated P32** [Ojeda 2023, pp. 1-2].
*   **Boundary effects can cause up to a 30% difference between the input and sampled target intensity** [Ojeda 2023, pp. 5-6]. As the sampling volume is reduced, the average sampled P32 value increases, showing an asymptotic behavior [Ojeda 2023, pp. 5-6].
*   **Fracture generation by centre points shows better agreement with input P32 and stabilizes faster than the surface points method** [Ojeda 2023, pp. 5-6]. The underlying Baecher spatial model, which assumes fractures are uniformly located in space, causes the boundary effect because fractures with centroids outside the generation box but within a fracture diameter of the boundary are not generated, leading to lower intensity near the edge [Ojeda 2023, pp. 6-6].
*   **Boundary effects can be minimized by using a generation box whose size is the volume of interest plus three times the mean fracture radius** [Ojeda 2023, pp. 6-7].
*   **A correction factor for intensity is independent of the fracture intensity itself**, meaning the same factor can be applied to models with different P32 values if other properties are held constant [Ojeda 2023, pp. 7-8].
*   **The number of realizations required for model convergence depends on fracture size.** For a mean fracture radius of 25 m, 30–50 realizations were needed, while for a 2 m radius, as few as 10 were sufficient [Ojeda 2023, pp. 7-8].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| Limiting the minimum angle of intersection for Terzaghi Weighting results in an underestimation of the calculated P32. | [Ojeda 2023, pp. 1-2] | DFN analysis based on Chilès' methodology. | Challenges a "self-assumed practical industry standard." |
| Boundary effects can cause a difference of up to 30% between input and target P32. | [Ojeda 2023, pp. 5-6] | Model conditions: P32 = 2 m⁻¹, mean fracture radius = 20 m. | |
| Fractures generated using their centres show a better agreement with the input P32 and the average curve stabilizes faster than using the surface points option. | [Ojeda 2023, pp. 5-6] | DFN models investigating boundary effects. | |
| Boundary effects are minimized when using a generation box size equal to the volume of interest plus three times the mean fracture radius. | [Ojeda 2023, pp. 6-7] | Based on a sensitivity analysis for varying fracture sizes. | The curve stabilizes at a distance slightly lower than three times the mean fracture radius from the boundary. |
| The correction factor for intensity is independent of the fracture intensity value, allowing the same factor for models with different intensities if other properties are constant. | [Ojeda 2023, pp. 7-8] | A range of intensities was tested for a defined box size. | See Table 2 in source. |
| For a mean fracture radius of 25 m, 30–50 realizations are required for convergence of the cumulative average P32; for a 2 m radius, ~10 are sufficient. | [Ojeda 2023, pp. 7-8] | Analysis of model convergence for a 100 m per side box. | |

## Limitations
*   The analysis is based entirely on synthetic DFN models, which may not capture the full complexity of natural fracture networks.
*   The study explicitly addresses the limitation of not knowing fracture size distribution beforehand, but the proposed methodology to mitigate boundary effects requires this knowledge [Ojeda 2023, pp. 2-2].
*   The paper focuses on the Chilès methodology for estimating P32 from borehole data, and findings regarding boundary effects are tied to the underlying Baecher spatial model [Ojeda 2023, pp. 2-2, 6-6].
*   The paper distinguishes itself from Wang's method, which assumes a univariate Fisher distribution, implying that the presented DFN approach is not similarly constrained, but the specific distributional assumptions for this study's models remain unstated [Ojeda 2023, pp. 2-2].
*   The study uses synthetic data with a constant shape (hexagon) and aspect ratio (1), which is a simplification of natural fracture shapes [Ojeda 2023, pp. 3-5].

## Assumptions / Conditions
*   **Terzaghi Weighting assumption:** The correction method assumes a zero-thickness sampling survey (e.g., a borehole) [Ojeda 2023, pp. 2-3].
*   **Spatial Model:** The analysis of boundary effects is explicitly based on the **Baecher spatial model**, which assumes fractures are located uniformly in space [Ojeda 2023, pp. 6-6].
*   **Fracture Geometry:** Fractures in the DFN models are perfect **hexagons with a constant aspect ratio of 1** [Ojeda 2023, pp. 3-5].
*   **Size Distribution:** Fracture radii follow a **lognormal distribution** with a standard deviation fixed at 40% of the mean radius [Ojeda 2023, pp. 3-5].
*   **Methodology for Mitigation:** The proposed rule for minimizing boundary effects (generation box = volume of interest + 3 * mean radius) is conditional on the fracture size distribution and orientation [Ojeda 2023, pp. 6-6].
*   **Intensity Correction Factor:** The finding that a correction factor is independent of intensity assumes all other model properties are held constant [Ojeda 2023, pp. 7-8].

## Key Variables / Parameters
*   **P32:** Volumetric fracture intensity (m⁻¹) [Ojeda 2023, pp. 1-2].
*   **P10:** Linear fracture intensity [Ojeda 2023, pp. 2-2].
*   **α:** The acute angle between the scanline and the fracture [Ojeda 2023, pp. 2-3].
*   **sinα:** The Terzaghi Weighting factor [Ojeda 2023, pp. 2-3].
*   **ˆP32:** Predicted volumetric fracture intensity using Chilès' method [Ojeda 2023, pp. 3-3].
*   **L:** Length of the scanline or survey [Ojeda 2023, pp. 3-3].
*   **β_i:** Local orientation of a scanline segment [Ojeda 2023, pp. 3-3].
*   **ω_i:** Orientation of a fracture [Ojeda 2023, pp. 3-3].
*   **Mean Fracture Radius:** A critical control on boundary effects, tested at 2, 5, 10, 15, 20, and 25 m [Ojeda 2023, pp. 3-5].
*   **Generation Box Size:** The volume in which fractures are generated, which must be larger than the volume of interest to mitigate boundary effects [Ojeda 2023, pp. 6-7].

## Reusable Claims
*   **Claim:** In DFN modeling to estimate P32, using a common practice of applying a minimum angle cut-off for Terzaghi Weighting results in a systematic underestimation of the true intensity. **Conditions:** Applicable when estimating P32 from borehole data using Chilès' methodology. **Evidence:** Analysis presented in the paper indicated underestimation [Ojeda 2023, pp. 1-2]. **Limitations:** The magnitude of underestimation may depend on the fracture orientation distribution.
*   **Claim:** When generating DFN models using the Enhanced Baecher model, placing fracture generation points at their centres provides a more accurate and faster-converging estimate of target P32 compared to using random surface points. **Conditions:** Related to mitigating boundary effects in a generation volume. **Evidence:** Models with centre-based generation showed better agreement with input P32 [Ojeda 2023, pp. 5-6]. **Limitations:** Confirmed for hexagonal fractures with a lognormal size distribution.
*   **Claim:** A practical rule to minimize boundary effects on P32 in a cubic volume of interest is to generate the fracture network in a larger, concentric box whose side length equals the side length of the volume of interest plus three times the mean fracture radius. **Conditions:** Requires prior knowledge of the mean fracture radius. Assumptions include uniform spatial distribution (Baecher model) and specific fracture orientation/distribution [Ojeda 2023, pp. 6-6]. **Evidence:** The sampled P32 curve stabilized at this distance from the generation box boundary [Ojeda 2023, pp. 6-7]. **Limitations:** It is a heuristic derived from a specific set of synthetic models.
*   **Claim:** The correction factor required to calibrate a DFN model's P32 to a target value, when boundary effects are not explicitly mitigated, is independent of the intensity value itself. **Conditions:** True if fracture size distribution, orientation, and generation box geometry are held constant. **Evidence:** Variation in percentage with respect to input intensity was constant for a defined box size across different intensities [Ojeda 2023, pp. 7-8]. **Limitations:** Likely sensitive to changes in fracture size and spatial model.

## Candidate Concepts
*   [[Volumetric Fracture Intensity (P32)]]
*   [[Terzaghi Weighting]]
*   [[Orientation Bias]]
*   [[Discrete Fracture Network (DFN)]]
*   [[Boundary Effect (DFN)]]
*   [[Fracture Intensity Scaling]]
*   [[Sampling Bias (Geology)]]
*   [[Representative Elementary Volume (REV)]]

## Candidate Methods
*   [[Discrete Fracture Network (DFN) Modelling]]
*   [[Chilès Method for P32 Estimation]]
*   [[FracMan (Software)]]
*   [[Monte Carlo Simulation]]
*   [[Borehole Fracture Logging]]

## Connections To Other Work
*   The methodology directly builds upon the Terzaghi Weighting correction [Terzaghi, 1965] and its generalization for P32 estimation by **Chilès et al. [13]** [Ojeda 2023, pp. 2-3].
*   The paper contrasts its approach with limitations of other P32 estimation methods, such as those by **Zhang and Einstein [11]** (requires exposed rock faces and assumptions about fracture location/size) and **Wang [12]** (numerical approximation between P10 and P32, limited to a Univariate Fisher distribution) [Ojeda 2023, pp. 2-2].
*   The analysis of boundary effects directly references the **Baecher spatial model [20]** and recommendations by **Priest [15]** and **Samaniego and Priest [17]**, who suggested using a smaller volume of interest within a larger generation volume [Ojeda 2023, pp. 6-6].
*   From a thematic perspective, this work connects to concepts like [[Fracture Sampling Bias]], [[Scale Effects in Rock Mechanics]], and [[DFN Model Calibration and Validation]].

## Open Questions
*   How do the findings, particularly the rule for minimizing boundary effects, hold for fracture networks with orientations and spatial distributions that are markedly different (e.g., clustered, non-Baecher) from the one tested? [Ojeda 2023, pp. 6-6]
*   What is the specific impact of the angular cut-off on the underestimation of P32 for different fracture orientation dispersions (e.g., varying Fisher K)? [Ojeda 2023, pp. 1-2]
*   Can a more general analytical formulation be developed to correct for boundary effects without relying on a priori knowledge of the mean fracture radius?
*   How do these synthetic results translate to real-world datasets where the true P32 is unknown, and what validation strategies should be adopted? [Ojeda 2023, pp. 1-2]

## Source Coverage
This page is based on the provided 20 index fragments, which cover the paper's abstract, introduction, methodology for Chilès' equation, the specifics of the DFN modeling setup for boundary effect analysis, core results, and a proposed mitigation methodology. The coverage is heavily weighted towards the methods and results sections. Certain sections like a detailed discussion, final conclusions, and potential appendices are not covered in the provided fragments. Key equations (1, 2, 3) and tables (Table 1, Table 2) are partially described but not fully reproduced.
