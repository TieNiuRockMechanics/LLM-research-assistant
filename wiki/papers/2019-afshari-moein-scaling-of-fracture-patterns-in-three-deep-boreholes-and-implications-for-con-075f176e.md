---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-afshari-moein-scaling-of-fracture-patterns-in-three-deep-boreholes-and-implications-for-con-075f176e"
title: "Scaling of Fracture Patterns in Three Deep Boreholes and Implications for Constraining Fractal Discrete Fracture Network Models."
status: "draft"
source_pdf: "data/papers/Scaling of Fracture Patterns in Three Deep Boreholes and Implications for Constraining Fractal Discrete Fracture Network Models.pdf"
collections:
citation: "Afshari Moein, Mohammad Javad, et al. \"Scaling of Fracture Patterns in Three Deep Boreholes and Implications for Constraining Fractal Discrete Fracture Network Models.\" *Rock Mechanics and Rock Engineering*, 2019, https://doi.org/10.1007/s00603-019-1739-7."
indexed_texts: "19"
indexed_chars: "92918"
nonempty_source_blocks: "19"
compiled_source_blocks: "19"
compiled_source_chars: "92095"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.991143"
coverage_status: "full-index"
source_signature: "ed197d421b9ea385e04d11e3f7c19c196e4c6b6c"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:31:47"
---

# Scaling of Fracture Patterns in Three Deep Boreholes and Implications for Constraining Fractal Discrete Fracture Network Models.

## One-line Summary
A methodology for generating fractal discrete fracture networks (DFNs) is presented, and analysis of fracture spacing data from three deep boreholes demonstrates fractal scaling over more than two orders of magnitude, with implications for constraining DFN models.

## Research Question
The principal aim is to clarify the scaling properties of 1D fracture spacing data from deep boreholes and to explore the possibility of using this data to constrain 2D and 3D structural models of the rock mass [Afshari 2019, pp. 2-3].

## Study Area / Data
The study uses fracture data derived from acoustic televiewer logs in three deep boreholes: the Basel-1 well near Basel, Switzerland, and the GPK3 and GPK4 wells at the Soultz-sous-Forêts geothermal site in France [Afshari 2019, pp. 14-16]. The Basel-1 well is 5 km deep and penetrates a monzogranite basement [Afshari 2019, pp. 14-16]. The GPK3 and GPK4 wells are also 5 km deep and penetrate a porphyric monzogranite basement [Afshari 2019, pp. 14-16]. Fracture sets were identified based on orientation, with six sets in Basel-1 and seven sets in GPK3/GPK4 [Afshari 2019, pp. 14-16].

## Methods
The study employs a dual-power-law DFN model proposed by Davy et al. (1990), which is generated using a Multiplicative Cascade process [Afshari 2019, pp. 3-4]. Synthetic 1D, 2D, and 3D fracture networks were generated to evaluate stereological relationships and test fractal dimension estimation techniques [Afshari 2019, pp. 1-2]. Three techniques for estimating the fractal dimension of 1D fracture spacing were compared: the two-point correlation function, the box-counting technique, and the power-law distribution of spacing [Afshari 2019, pp. 12-13]. These methods were applied to both synthetic data and observed fracture distributions from the three boreholes [Afshari 2019, pp. 14-16].

## Key Findings
The two-point correlation method provided the most stable and reliable estimate of the fractal dimension for 1D fracture spacing data [Afshari 2019, pp. 12-13]. The distribution of fractures along the three deep boreholes was found to be fractal over more than two orders of magnitude in scale [Afshari 2019, pp. 14-16]. For all fractures combined, the fractal dimension (D1D) ranged from 0.86 to 0.88 [Afshari 2019, pp. 14-16]. For individual fracture sets of common orientation, the fractal dimension ranged between 0.65 and 0.75 [Afshari 2019, pp. 14-16]. Stereological analysis of synthetic networks showed that it is not possible to estimate the 2D and 3D fractal scaling parameters (correlation dimension and length exponent) from the 1D correlation dimension of fracture spacing, even if the length exponent is known a priori [Afshari 2019, pp. 1-2].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| The two-point correlation function yields a stable and correct estimate of the fractal dimension for synthetic 1D fracture spacing data of known fractal dimension. | [Afshari 2019, pp. 12-13] | Synthetic 1D data generated with a Multiplicative Cascade process. | Box-counting and power-law spacing methods did not deliver reliable estimates. |
| Fracture spacing in Basel-1, GPK3, and GPK4 boreholes is fractal over more than two orders of magnitude. | [Afshari 2019, pp. 14-16] | Analysis of all fractures regardless of orientation. | Fractal scaling valid in the range of 2–1000 m. |
| The 1D correlation dimension (D1D) for all fractures in each borehole is 0.86 (Basel-1), 0.88 (GPK3), and 0.87 (GPK4). | [Afshari 2019, pp. 14-16] | All fractures in each well combined. | Standard deviation of local slope within the fractal range is less than 0.06. |
| For individual fracture sets, D1D ranges from 0.65 to 0.75. | [Afshari 2019, pp. 14-16] | Analysis of the four most populous fracture sets in each borehole. | Fractal scaling valid over at least two orders of magnitude. |
| Stereological analysis shows D1D remains close to 1 for 3D DFNs with a3D=3.5, regardless of D3D. | [Afshari 2019, pp. 9-10] | Synthetic 3D DFNs with random fracture orientations. | Demonstrates impossibility of estimating 3D scaling parameters from 1D data. |
| Removal or trimming of fractures extending beyond a 2D domain boundary does not significantly impact the correlation dimension of fracture centers. | [Afshari 2019, pp. 6-7] | Synthetic 2D DFNs with length exponents a=1.5 and a=2.5. | Trimming preserves the fractal nature of the length distribution better than removal for larger fractures. |

## Limitations
The stereological problem of constraining 2D and 3D scaling parameters from 1D observations is underdetermined and leads to non-unique solutions [Afshari 2019, pp. 18-19]. The Levy–Lee flight process (as in Fracman software) was found to produce networks where the output fractal dimension did not match the input, likely due to finite domain effects [Afshari 2019, pp. 3-4]. The resolution of acoustic televiewer logs may not permit identification of very thin discontinuities [Afshari 2019, pp. 14-16]. The analysis of fracture sets was limited to the four most populous sets due to insufficient data in others [Afshari 2019, pp. 14-16].

## Assumptions / Conditions
The fracture network is assumed to follow a fractal organization described by the dual-power-law model [Afshari 2019, pp. 3-4]. The borehole fracture data is assumed to provide a reasonably complete sampling of the fracture families present in the rock mass [Afshari 2019, pp. 14-16]. Synthetic DFN generation assumes random fracture orientations unless otherwise specified [Afshari 2019, pp. 9-10]. The stereological relationships derived by Darcel et al. (2003b) are used as a theoretical framework [Afshari 2019, pp. 9-10].

## Key Variables / Parameters
- **D**: Correlation dimension of fracture centers [Afshari 2019, pp. 1-2].
- **a**: Fracture length exponent [Afshari 2019, pp. 1-2].
- **D1D**: Correlation dimension of fracture intersection points along a 1D scanline (borehole) [Afshari 2019, pp. 9-10].
- **D2D**: Correlation dimension of fracture centers in a 2D plane [Afshari 2019, pp. 9-10].
- **D3D**: Correlation dimension of fracture centers in 3D space [Afshari 2019, pp. 9-10].
- **a1D, a2D, a3D**: Length exponents in 1D, 2D, and 3D, respectively [Afshari 2019, pp. 9-10].

## Reusable Claims
- The two-point correlation function provides the most stable and reliable estimate of the fractal dimension for 1D fracture spacing data derived from boreholes, as validated against synthetic data of known fractal dimension [Afshari 2019, pp. 12-13].
- Fracture spacing distributions in deep crystalline rock boreholes exhibit fractal scaling over more than two orders of magnitude, with a correlation dimension (D1D) between 0.86 and 0.88 when all fractures are considered [Afshari 2019, pp. 14-16].
- It is not possible to uniquely determine the 3D fractal scaling parameters (D3D and a3D) of a fracture network solely from the 1D correlation dimension (D1D) measured along a borehole, even if the length exponent is known [Afshari 2019, pp. 1-2, 18-19].
- The fractal dimension of fracture sets with common orientation is slightly lower (0.65–0.75) than that of the combined dataset, indicating some clustering [Afshari 2019, pp. 14-16, 18-19].

## Candidate Concepts
- [[fractal discrete fracture network]]
- [[correlation dimension]]
- [[length exponent]]
- [[dual power-law model]]
- [[stereological relationships]]
- [[fracture spacing]]
- [[Enhanced Geothermal Systems]]

## Candidate Methods
- [[Multiplicative Cascade process]]
- [[two-point correlation function]]
- [[box-counting technique]]
- [[power-law distribution of spacing]]
- [[discrete inverse transform method]]

## Connections To Other Work
The study builds upon the dual-power-law DFN model proposed by Davy et al. (1990) [Afshari 2019, pp. 3-4]. It references stereological analyses by Darcel et al. (2003b) [Afshari 2019, pp. 9-10]. The work is motivated by the need to constrain DFN models for geothermal reservoir development, linking to studies on hydraulic stimulation and induced seismicity (e.g., Afshari Moein et al. 2018a, 2018b) [Afshari 2019, pp. 2-3]. It also connects to broader literature on power-law scaling in fracture networks (e.g., Bonnet et al. 2001) [Afshari 2019, pp. 2-3].

## Open Questions
How can the scaling properties of fracture networks be linked to stress fluctuations observed from borehole failure or to the seismogenic b-value parameter? [Afshari 2019, pp. 2-3]. What additional information (e.g., from induced seismicity or stress tomography) is required to constrain 3D DFN models from 1D borehole data? [Afshari 2019, pp. 18-19]. How do mechanical interactions between fractures influence the scaling laws, and can novel DFN algorithms that respect these interactions improve stereological relationships? [Afshari 2019, pp. 19-20].

## Source Coverage
All 19 non-empty indexed fragments were processed. The compiled source blocks total 19, with a compiled character count of 92,095 out of a total indexed character count of 92,918, resulting in a coverage ratio by characters of 0.991. The coverage status is full-index.
