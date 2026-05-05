---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-zhu-can-we-infer-the-percolation-status-of-3d-fractured-media-from-2d-outcrops"
title: "Can We Infer the Percolation Status of 3D Fractured Media from 2D Outcrops?"
status: "draft"
source_pdf: "data/papers/2022 - Can we infer the percolation status of 3D fractured media from 2D outcrops.pdf"
collections:
  - "2文章钻孔裂缝分形关系"
citation: "Zhu, Weiwei, et al. \"Can We Infer the Percolation Status of 3D Fractured Media from 2D Outcrops?\" *Engineering Geology*, vol. 302, 2022, 106648. doi:10.1016/j.enggeo.2022.106648. Accessed 1 Apr. 2026."
indexed_texts: "15"
indexed_chars: "71873"
nonempty_source_blocks: "15"
compiled_source_blocks: "15"
compiled_source_chars: "67813"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.943511"
coverage_status: "full-index"
source_signature: "6f1db8a786cc76fc67c10ff9a3c1c3ea4653c9d3"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:16:29"
---

# Can We Infer the Percolation Status of 3D Fractured Media from 2D Outcrops?

## One-line Summary
This study uses discrete fracture network modeling to show that a well-connected 2D outcrop map (with a spanning cluster) indicates the corresponding 3D fracture network is over-percolative, with an intensity at least 3.5 times the percolation threshold, and provides empirical limits for inference.

## Research Question
Can the percolation status (connectivity) of a 3D subsurface fracture network be inferred from the 2D cross-section information provided by geological outcrops? [Zhu 2022, pp. 1-2]

## Study Area / Data
The study uses synthetically generated 3D discrete fracture networks (DFNs) and their 2D cross-sections. Fracture geometries (lengths, orientations, center positions) are characterized by different stochastic distributions. The analysis also incorporates 80 published, digitized outcrop maps from various locations worldwide for validation. [Zhu 2022, pp. 3-5, 14-15]

## Methods
1.  **DFN Generation:** 3D fracture networks are generated using in-house software (HatchFrac). Fractures are represented as random convex polygons. Key geometric parameters follow stochastic distributions: fracture lengths follow a power-law distribution (exponent *a*), center positions follow a uniform or fractal spatial density distribution (fractal dimension *F_D*), and orientations follow a uniform distribution. [Zhu 2022, pp. 5-7]
2.  **Cross-Sectioning:** 2D cross-section maps are taken from the 3D networks to mimic outcrops. The map at the middle position of the domain is used as a representative. [Zhu 2022, pp. 8-10]
3.  **Cluster Analysis:** A fast Monte Carlo algorithm is used to identify and label connected fracture clusters in both 3D networks and 2D cross-sections. A "spanning cluster" connects opposite boundaries of the domain (six faces in 3D, four sides in 2D). [Zhu 2022, pp. 5-7]
4.  **Two-Phase Analysis:** The simulation tracks two critical phases: Phase 1 (when a spanning cluster forms in the 3D network) and Phase 2 (when a spanning cluster forms in the 2D cross-section map). [Zhu 2022, pp. 8-10]
5.  **Sensitivity Analysis:** The impact of geometric parameters (*a*, *F_D*, system size *L*) on connectivity parameters is quantified using input/output correlation coefficients. [Zhu 2022, pp. 10-11]

## Key Findings
1.  Clustering effects (controlled by *F_D*) significantly increase local fracture intersections but have a negligible impact on overall fracture intensities (*P_30*, *P_32*) in 3D networks. [Zhu 2022, pp. 11-12]
2.  The number of intersections per fracture (*I_2D* or *I_3D*) is not a valid percolation parameter for complex fracture networks, as it does not yield a constant threshold after finite-size correction. [Zhu 2022, pp. 11-12]
3.  Fracture intensities (*P_20*, *P_21*, *P_30*, *P_32*) generally decrease with increasing system size *L*. [Zhu 2022, pp. 11-12]
4.  **Empirical Limits for Inference:**
    *   If a spanning cluster is formed in the 2D outcrop map, the corresponding 3D network is **over-percolative**, and its fracture intensity (*P_32*) is at least **3.5 times** the intensity at the 3D percolation threshold. [Zhu 2022, pp. 13-14]
    *   If no spanning cluster is formed in the 2D outcrop map, but its fracture intensity (*P_21*) is larger than **0.43 times** the intensity required to form a spanning cluster in 2D, the corresponding 3D network can still form a spanning cluster and show good connectivity. [Zhu 2022, pp. 13-14]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Minimum number ratio (3D) between Phase 2 and Phase 1 is 3.5. | [Zhu 2022, pp. 13-14] | 2D cross-section has a spanning cluster. | Indicates 3D network is over-percolative. |
| Maximum number ratio (2D) between Phase 1 and Phase 2 is 0.43. | [Zhu 2022, pp. 13-14] | 2D cross-section has no spanning cluster. | If actual intensity > 0.43 * percolation intensity, 3D network may percolate. |
| Clustering effects (*F_D*) have a strong negative correlation with *I_3D* but weak correlation with *P_30* and *P_32*. | [Zhu 2022, pp. 11-12] | Phase 1 (3D percolation). | Shows clustering enhances local intersections but not global intensity. |
| *I_2D* and *I_3D* do not remain constant after finite-size correction. | [Zhu 2022, pp. 11-12] | Across various system sizes *L* and exponents *a*. | Evidence that intersection count is not a valid percolation parameter. |
| 63 out of 80 analyzed natural outcrop maps have a spanning cluster. | [Zhu 2022, pp. 3-5, 14-15] | Collection of published outcrop maps. | Suggests most natural outcrops are well-connected, implying over-percolative 3D networks. |

## Limitations
1.  The study assumes outcrop samples are unbiased and representative of subsurface structures, which may not hold due to weathering, stress release, and sampling bias. [Zhu 2022, pp. 8-10]
2.  DFN models use simplified geometries (convex polygons) and exclude fracture terminations (T-type intersections). [Zhu 2022, pp. 5-7]
3.  The analysis focuses on geometrical connectivity, not hydraulic conductivity, which is affected by aperture, roughness, stress, and diagenesis. [Zhu 2022, pp. 3-5]
4.  The maximum system size (*L*=40) is limited due to computational cost of the cluster-check operation. [Zhu 2022, pp. 11-12]

## Assumptions / Conditions
1.  Outcrop maps on the surface can be related to subsurface structures and are similar to a cross-section map of the subsurface fracture network. [Zhu 2022, pp. 8-10]
2.  Discrete Fracture Networks (DFNs) are representative of natural fracture networks. [Zhu 2022, pp. 8-10]
3.  Fracture terminations (T-type intersections) are not included. [Zhu 2022, pp. 5-7]
4.  Different geometric parameters (lengths, orientations, positions) are independent. [Zhu 2022, pp. 10-11]

## Key Variables / Parameters
*   **Geometric Distributions:** Power-law exponent for length (*a*), fractal dimension for center positions (*F_D*), system size (*L*). [Zhu 2022, pp. 10-11]
*   **Fracture Intensity:** *P_20* (number/area), *P_21* (length/area), *P_30* (number/volume), *P_32* (area/volume). [Zhu 2022, pp. 3-5]
*   **Connectivity Metrics:** *I_2D* (intersections/fracture in 2D), *I_3D* (intersections/fracture in 3D). [Zhu 2022, pp. 3-5]
*   **Phase Linkage Ratios:** Number ratio (3D), Area ratio (3D), Number ratio (2D), Length ratio (2D). [Zhu 2022, pp. 3-5]

## Reusable Claims
*   **Claim:** If a 2D outcrop map exhibits a spanning cluster, the corresponding 3D subsurface fracture network is over-percolative, with a fracture intensity (*P_32*) at least 3.5 times greater than the intensity at the 3D percolation threshold.
    *   **Condition:** Based on DFN modeling with power-law length distributions and uniform/fractal spatial distributions.
    *   **Limitation:** Assumes the outcrop is an unbiased analog of the subsurface; does not account for hydraulic conductivity.
*   **Claim:** If a 2D outcrop map has no spanning cluster but its fracture intensity (*P_21*) exceeds 0.43 times the intensity required to form a 2D spanning cluster, the corresponding 3D network may still form a spanning cluster.
    *   **Condition:** Derived from statistical analysis of synthetic DFN cross-sections.
    *   **Limitation:** Provides a probabilistic indicator, not a certainty; dependent on the representativeness of the outcrop.

## Candidate Concepts
*   [[discrete fracture network]]
*   [[percolation theory]]
*   [[fracture intensity]]
*   [[spanning cluster]]
*   [[fracture connectivity]]
*   [[outcrop analog]]

## Candidate Methods
*   [[discrete fracture network modeling]]
*   [[sensitivity analysis]]
*   [[cluster labeling algorithm]]
*   [[cross-section sampling]]

## Connections To Other Work
*   Builds on prior work correlating 1D, 2D, and 3D fracture intensities (*P_ij*), noting that 2D-3D correlations are stronger than 1D-3D. [Zhu 2022, pp. 1-2]
*   Extends findings that common parameters like total excluded area and intersections per fracture are not valid percolation parameters for complex networks. [Zhu 2022, pp. 3-5]
*   Contrasts with experimental work by Renshaw et al. (2020) which suggested limited fracture growth after percolation onset, by arguing that natural geological history allows for multiple fracture sets leading to over-percolation. [Zhu 2022, pp. 14-15]
*   Uses and references a collection of 80 digitized outcrop maps from previous research. [Zhu 2022, pp. 3-5, 14-15]

## Open Questions
*   What is a proper, universal percolation parameter for complex fracture networks with power-law lengths and clustered positions? [Zhu 2022, pp. 3-5]
*   How can the link between 2D outcrop connectivity and 3D subsurface connectivity be validated with real, inaccessible 3D subsurface data? [Zhu 2022, pp. 3-5]
*   How do factors like fracture sealing, stress state, and diagenesis, which affect hydraulic conductivity, interact with the geometric connectivity conclusions? [Zhu 2022, pp. 14-15]

## Source Coverage
All 15 non-empty indexed fragments were processed. The compiled source blocks total 15, with a coverage ratio by blocks of 1.0 and a coverage ratio by characters of 0.943511.
