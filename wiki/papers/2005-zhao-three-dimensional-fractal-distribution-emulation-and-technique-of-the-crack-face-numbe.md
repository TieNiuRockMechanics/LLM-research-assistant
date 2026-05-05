---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2005-zhao-three-dimensional-fractal-distribution-emulation-and-technique-of-the-crack-face-numbe"
title: "Three-Dimensional Fractal Distribution Emulation and Technique of the Crack Face Number in Rock Mass."
status: "draft"
source_pdf: "data/papers/岩体裂隙面数量的三维分形分布仿真理论与技术_赵阳升.pdf"
collections:
citation: "Zhao, Yangsheng, Zaiming Wen, and Zengchao Feng. \"Three-Dimensional Fractal Distribution Emulation and Technique of the Crack Face Number in Rock Mass.\" *Chinese Journal of Rock Mechanics and Engineering*, vol. 24, no. 6, 2005, pp. 994-998."
indexed_texts: "2"
indexed_chars: "8586"
nonempty_source_blocks: "2"
compiled_source_blocks: "2"
compiled_source_chars: "7778"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.905893"
coverage_status: "full-index"
source_signature: "54a2ee367dc5d4ae487e1a3ff48fcdeed7765ed1"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T11:03:16"
---

# Three-Dimensional Fractal Distribution Emulation and Technique of the Crack Face Number in Rock Mass.

## One-line Summary
This paper establishes a three-dimensional fractal distribution emulation model for crack face numbers in rock mass and develops a corresponding simulation system to analyze internal fracture distributions for engineering stability and stress analysis.

## Research Question
How to model and simulate the three-dimensional distribution of crack face numbers in rock mass, moving beyond previous two-dimensional studies, to support analysis of rock mass engineering stability, stress distribution, and permeability.

## Study Area / Data
The study is based on field and microscopic observations from over 20 mines, examining coal and rock layers. The fractal geometric parameters (e.g., 3D fractal dimension `Ds`, initial distribution value `Ns`) are obtained from outcrop measurements and drilling core measurements [Zhao 2005, pp. 1-3].

## Methods
1.  **Fractal Distribution Model:** A model is built based on the fractal law governing crack face numbers across different measurement scales: `N(d) = Ns * d^(-Ds)`, where `d` is the measurement scale, `N(d)` is the number of crack faces, `Ns` is the initial value, and `Ds` is the 3D fractal dimension [Zhao 2005, pp. 1-3].
2.  **Model Assumptions:** The model assumes crack faces are circular planes, their intersection with an observation plane forms a trace, and they are randomly distributed in the rock mass [Zhao 2005, pp. 1-3].
3.  **Simulation System:** A simulation system was developed using Visual C++ 6.0. It can generate a 3D crack face network and automatically extract any cross-section (parallel to xoy, yoz, xoz planes) or any sub-block for analysis [Zhao 2005, pp. 1-3, 3-5].

## Key Findings
1.  The developed emulation system provides a convenient method to study the trace distribution on any internal cross-section and the crack face distribution within any sub-block of a rock mass [Zhao 2005, pp. 1-3].
2.  The fractal characterization contains more information about crack faces than conventional statistical methods, making the results more consistent with actual distributions [Zhao 2005, pp. 1-3].
3.  The system facilitates the analysis of rock mass engineering stability and stress distribution by allowing the identification of controlling fracture planes, which can simplify models for more accurate results [Zhao 2005, pp. 3-5].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Fractal law: `N(d) = Ns * d^(-Ds)` | [Zhao 2005, pp. 1-3] | Based on field/microscopic observations from 20+ mines. | `Ds` is the 3D fractal dimension, `Ns` is the initial value. |
| Model assumes crack faces are circular planes, randomly distributed. | [Zhao 2005, pp. 1-3] | For establishing the 3D emulation model. | Simplifies complex real-world geometry. |
| Simulation system built with Visual C++ 6.0. | [Zhao 2005, pp. 1-3, 3-5] | System implementation. | Enables 3D network generation and cross-section/sub-block extraction. |
| Example simulation parameters: Group 1: Ds=2.2793, ST=90°, SP=90°, Ns=1.1, L0=1. | [Zhao 2005, pp. 3-5] | Used to demonstrate the system's utility. | Shows crack faces parallel to the yoz plane. |
| The system allows analysis of any cross-section and sub-block. | [Zhao 2005, pp. 3-5] | After 3D network simulation is complete. | Provides convenience for observing internal fracture distribution. |

## Limitations
The paper does not explicitly list limitations. However, the model's assumptions (e.g., circular crack faces, random distribution) are simplifications of natural rock mass complexity. The accuracy of the simulation depends on the quality of the input fractal parameters obtained from measurements.

## Assumptions / Conditions
1.  Crack faces in the rock mass are spatial planes with a circular disk shape [Zhao 2005, pp. 1-3].
2.  The intersection line between a crack face and an observation plane is the crack trace [Zhao 2005, pp. 1-3].
3.  Crack faces are randomly distributed within the rock mass [Zhao 2005, pp. 1-3].

## Key Variables / Parameters
*   **g:** Number of crack face groups (based on orientation) [Zhao 2005, pp. 1-3, 3-5].
*   **L₀:** Initial measurement scale (mm) [Zhao 2005, pp. 1-3, 3-5].
*   **Ds:** Three-dimensional fractal dimension (rational number between 2 and 3) [Zhao 2005, pp. 1-3, 3-5].
*   **Ns:** Initial crack face distribution value (rational number > 0) [Zhao 2005, pp. 1-3, 3-5].
*   **ST, SP:** Dip angle and azimuth of the crack face normal vector [Zhao 2005, pp. 1-3, 3-5].
*   **nr(l, m, n):** Normal vector of a crack face [Zhao 2005, pp. 1-3].

## Reusable Claims
*   The distribution of crack face numbers in rock mass across different scales follows a fractal law: `N(d) = Ns * d^(-Ds)` [Zhao 2005, pp. 1-3].
*   A 3D fractal emulation model, based on the assumptions of circular, randomly distributed crack planes, can be used to simulate the crack face network in rock mass [Zhao 2005, pp. 1-3].
*   A computer simulation system can automatically extract any cross-section or sub-block from a generated 3D crack network, greatly facilitating the analysis of internal fracture distributions for engineering purposes [Zhao 2005, pp. 1-3, 3-5].
*   Fractal characterization provides more comprehensive information about crack face distributions compared to conventional statistical methods [Zhao 2005, pp. 1-3].

## Candidate Concepts
*   [[fractal distribution]]
*   [[crack face network]]
*   [[rock mass stability]]
*   [[permeability analysis]]
*   [[fractal dimension]]
*   [[three-dimensional simulation]]

## Candidate Methods
*   [[fractal modeling]]
*   [[Monte Carlo simulation]] (referenced as prior work)
*   [[Visual C++ simulation system]]
*   [[cross-section extraction]]

## Connections To Other Work
The paper builds upon and extends previous research:
*   It cites prior use of the Monte Carlo method for simulating damage joint distribution [Zhao 2005, pp. 1-3].
*   It references a scaling method for simulating actual joint distribution [Zhao 2005, pp. 1-3].
*   It notes a previous approach using three orthogonal plane fracture distributions to describe 3D distribution, which was still fundamentally a 2D study [Zhao 2005, pp. 1-3].
*   The work is part of a series by the authors' research group over more than ten years [Zhao 2005, pp. 1-3].

## Open Questions
*   How can the model's accuracy be validated against more extensive real-world 3D fracture data?
*   How sensitive is the simulation to the accuracy of the measured fractal parameters (`Ds`, `Ns`)?
*   Can the model be adapted for rock masses with non-circular or more complexly shaped fracture planes?
*   How can this simulation be integrated with coupled hydro-mechanical analysis tools?

## Source Coverage
All non-empty indexed fragments were processed. The compilation is based on 2 indexed text blocks containing 8586 characters. The compiled page uses 7778 characters from these sources, achieving a coverage ratio of 1.0 by blocks and 0.905893 by characters. The source signature is `54a2ee367dc5d4ae487e1a3ff48fcdeed7765ed1`.
