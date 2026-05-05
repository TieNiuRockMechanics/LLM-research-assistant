---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2007-lu-numerical-simulation-of-3d-percolation-mechanism-in-porous-media"
title: "Numerical Simulation of 3D Percolation Mechanism in Porous Media."
status: "draft"
source_pdf: "data/papers/孔隙介质三维逾渗机制数值模拟研究_吕兆兴.pdf"
collections:
citation: "Lu, Zhaoxing, et al. \"Numerical Simulation of 3D Percolation Mechanism in Porous Media.\" *Chinese Journal of Rock Mechanics and Engineering*, vol. 26, no. Supp. 2, Dec. 2007, pp. 4019-23."
indexed_texts: "2"
indexed_chars: "8318"
nonempty_source_blocks: "2"
compiled_source_blocks: "2"
compiled_source_chars: "7492"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.900697"
coverage_status: "full-index"
source_signature: "240171c56410eea4b435db08bcec91279fe42021"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T11:15:22"
---

# Numerical Simulation of 3D Percolation Mechanism in Porous Media.

## One-line Summary
This study uses a custom VC++6.0 numerical simulation to investigate the 3D percolation mechanism in porous media, analyzing cluster characteristics and proposing an effective surface area rate.

## Research Question
The research aims to study the 3D percolation mechanism in porous media, the characteristics of percolation clusters, and the application of renormalization theory through numerical simulation.

## Study Area / Data
The study uses a simulated 3D cubic model with dimensions of 50×50×50 voxels (125,000 total voxels) representing a 5 mm × 5 mm × 5 mm porous medium. The porosity ratio is varied from 0.20 to 0.98 [Lu 2007, pp. 1-4].

## Methods
A numerical simulation software was developed using VC++6.0. The method involves generating a 3D stochastic porous medium model, identifying percolation clusters, and applying renormalization theory. Key analyses include calculating the number of clusters, the surface area of the largest cluster, the effective surface area rate, and the fractal dimension of the percolation cluster at the threshold [Lu 2007, pp. 1-4].

## Key Findings
1.  The number of clusters increases with porosity initially, reaches a maximum when porosity is 0.20, and then decreases [Lu 2007, pp. 1-4].
2.  The surface area of the largest cluster increases with porosity, and the rate of increase becomes faster when the porosity exceeds the percolation threshold [Lu 2007, pp. 1-4].
3.  When porosity is 0.55, the surface area of the largest cluster reaches its maximum, and the effective surface area rate is 0.98 [Lu 2007, pp. 1-4].
4.  At the percolation threshold porosity of 0.3116, the percolation cluster is a random fractal with a fractal dimension D = 2.934 [Lu 2007, pp. 1-4, pp. 4-5].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| The number of clusters has a maximum value when porosity is 0.20. | [Lu 2007, pp. 1-4] | Porosity varied from 0.20 to 0.98. | Observed from the relationship curve between cluster number and porosity. |
| The surface area of the largest cluster reaches a maximum at porosity 0.55, with an effective surface area rate of 0.98. | [Lu 2007, pp. 1-4] | Porosity varied from 0.20 to 0.98. | Derived from curves of largest cluster surface area and effective surface area rate vs. porosity. |
| At porosity 0.3116, the percolation cluster is a random fractal with dimension D = 2.934. | [Lu 2007, pp. 1-4, pp. 4-5] | Porosity fixed at the percolation threshold 0.3116. | Calculated using renormalization theory and simulation data for different system sizes L. |
| The percolation threshold for the 3D model is 0.3116. | [Lu 2007, pp. 1-4] | 3D cubic lattice model. | This value is used for the fractal dimension analysis. |

## Limitations
The simulation uses a cubic model of fixed size (50×50×50 voxels). The scalability and direct applicability of the findings to real-world porous media of different structures or larger scales are not confirmed.

## Assumptions / Conditions
The porous medium is modeled as a 3D cubic lattice where each voxel is randomly assigned as pore or solid based on the target porosity. The study assumes the validity of renormalization theory for analyzing the fractal properties of the percolation cluster at the threshold.

## Key Variables / Parameters
-   **Porosity (।༣ੱ):** The volume fraction of pores, varied from 0.20 to 0.98.
-   **Percolation Threshold (P_c):** The critical porosity (0.3116) at which a spanning cluster first appears.
-   **Cluster Number:** The total number of distinct pore clusters.
-   **Largest Cluster Surface Area (।༣ੱູ):** The surface area of the largest connected pore cluster.
-   **Effective Surface Area Rate (ࠒੱ):** A proposed metric, reaching 0.98 at porosity 0.55.
-   **Fractal Dimension (D):** Calculated as 2.934 for the percolation cluster at the threshold.

## Reusable Claims
-   In a 3D stochastic porous medium model, the number of pore clusters peaks at a porosity of 0.20 before declining [Lu 2007, pp. 1-4].
-   The effective surface area rate, representing the fraction of the largest cluster's surface area relative to the total pore surface area, reaches a maximum of 0.98 when the porosity is 0.55 [Lu 2007, pp. 1-4].
-   The percolation cluster at the threshold porosity of 0.3116 in a 3D cubic lattice exhibits random fractal characteristics with a dimension of 2.934 [Lu 2007, pp. 1-4, pp. 4-5].

## Candidate Concepts
-   [[Percolation threshold]]
-   [[Fractal dimension]]
-   [[Renormalization group theory]]
-   [[Percolation cluster]]
-   [[Specific surface area]]

## Candidate Methods
-   [[Numerical simulation]]
-   [[Renormalization analysis]]
-   [[Stochastic porous media modeling]]

## Connections To Other Work
The paper cites prior work on percolation models in computational materials science [Lu 2007, pp. 4-5, Ref 4], random simulation models in porous media [Lu 2007, pp. 4-5, Ref 5], and fractal dimension simulation methods [Lu 2007, pp. 4-5, Ref 6]. It also references foundational percolation theory texts [Lu 2007, pp. 4-5, Ref 9] and studies on percolation in specific lattice structures [Lu 2007, pp. 4-5, Ref 10, 11].

## Open Questions
-   How do the findings scale with larger model sizes or different lattice structures?
-   How does the effective surface area rate correlate with macroscopic transport properties like permeability in real materials?
-   Can the fractal dimension of 2.934 be generalized to other types of 3D porous media?

## Source Coverage
All non-empty indexed fragments were processed. The compilation used 2 source blocks containing 7492 characters from a total of 8318 indexed characters, achieving a coverage ratio of 1.0 by blocks and 0.900697 by characters.
