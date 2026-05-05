---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-zhou-permeability-evolution-of-grout-infilled-fractures-subjected-to-triaxial-compression-w"
title: "Permeability Evolution of Grout Infilled Fractures Subjected to Triaxial Compression with Low Confining Pressure."
status: "draft"
source_pdf: "data/papers/Permeability evolution of grout infilled fractures subjected to triaxial compression with low confining pressure.pdf"
collections:
citation: "Zhou, Dong, et al. \"Permeability Evolution of Grout Infilled Fractures Subjected to Triaxial Compression with Low Confining Pressure.\" *Tunnelling and Underground Space Technology*, vol. 104, 2020, p. 103539."
indexed_texts: "10"
indexed_chars: "49620"
nonempty_source_blocks: "10"
compiled_source_blocks: "10"
compiled_source_chars: "49649"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.000584"
coverage_status: "full-index"
source_signature: "a980098d2ec689ff32c5744c0c4fdbbb73c4a71d"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:39:17"
---

# Permeability Evolution of Grout Infilled Fractures Subjected to Triaxial Compression with Low Confining Pressure.

## One-line Summary
The permeability of grout-infilled granite fractures slightly decreases under low deviatoric stress but increases drastically (5-10 times) upon reaching peak stress due to compression-induced cracking in the grout and at the grout-granite interface.

## Research Question
How does the permeability of rock fractures infilled with grout evolve during the complete stress-strain process under triaxial compression with low confining pressure?

## Study Area / Data
The experimental study used cylindrical core plugs (50 mm diameter, 100 mm height) drilled from blocks of Jinan granite from Shandong, China. The granite has a low matrix permeability of 1.4 × 10⁻²⁰ m² [Zhou 2020, pp. 2-2]. The fractures were infilled with Ordinary Portland Cement (OPC) grout with a water-to-cement ratio of 0.6 [Zhou 2020, pp. 2-3]. Samples included one planar unfilled fracture, three planar infilled fractures (grout thicknesses of 2, 5, and 8 mm), and two rough infilled fractures (grout thicknesses of 2 and 8 mm) [Zhou 2020, pp. 2-3].

## Methods
1.  **Sample Preparation:** Planar fractures were created by cutting and polishing, while rough fractures were produced by axial splitting. Grout was injected into fractures using iron sheets to control thickness, then cured for 28 days [Zhou 2020, pp. 2-3].
2.  **Triaxial Compression & Permeability Testing:** Tests were conducted using an MTS 815 rock mechanics system. A constant confining pressure (Pc) of 5 MPa was applied. Permeability was measured continuously during axial loading using the transient method with deionized water as the pore fluid [Zhou 2020, pp. 2-3].
3.  **Microstructural Analysis:** A Phoenix v/tome/xm300 X-ray microfocus CT system (resolution ~100 μm) was used to scan samples before and after testing to observe damage [Zhou 2020, pp. 3-5].
4.  **Numerical Modeling:** Two-dimensional particle-based discrete element method (DEM) models using PFC2D were constructed to simulate the cracking processes in grout and granite under compression [Zhou 2020, pp. 6-8].

## Key Findings
1.  **Two-Phase Permeability Evolution:** For grout-infilled fractures, permeability slightly decreased or fluctuated when deviatoric stress was below the crack damage stress, followed by a rapid increase phase when stress exceeded the crack damage stress [Zhou 2020, pp. 5-6].
2.  **Magnitude of Change:** At peak deviatoric stress, the permeability of infilled fractures increased by about 5–10 times compared to the permeability at a deviatoric stress of 5 MPa [Zhou 2020, pp. 1-2].
3.  **Contrast with Unfilled Fractures:** The permeability of the unfilled fracture did not change significantly with increasing deviatoric stress until failure [Zhou 2020, pp. 5-6].
4.  **Mechanism of Increase:** CT scans and DEM simulations showed that compression-induced cracks developing within the grout and at the grout-granite interface are the primary sources for the drastic permeability enhancement under high deviatoric stress [Zhou 2020, pp. 1-2, pp. 6-8].
5.  **Effect of Grout Thickness & Roughness:** Sample permeability at low stress increased with grout thickness. Rough infilled fractures had lower permeability than planar infilled fractures with the same grout thickness [Zhou 2020, pp. 3-5].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Permeability of infilled fractures increased by about 5–10 times at peak deviatoric stress compared to at 5 MPa deviatoric stress. | [Zhou 2020, pp. 1-2] | Triaxial compression with 5 MPa confining pressure. | Main experimental finding. |
| Two phases of permeability evolution: fluctuation/reduction below crack damage stress, then rapid increase above it. | [Zhou 2020, pp. 5-6] | All grout-infilled samples. | Contrasts with behavior of unfilled fracture. |
| CT images show compression-induced cracks in grouts and at grout-granite interfaces after testing. | [Zhou 2020, pp. 5-6] | Samples P5, P8, R2. | Visual evidence of damage mechanism. |
| DEM modeling shows microcrack coalescence between grout and granite at high deviatoric stress (~120 MPa). | [Zhou 2020, pp. 6-8] | Numerical samples NP2, NP5, NP8. | Supports the mechanism for permeability increase. |
| Unfilled fracture permeability fluctuated between 0.7 and 1.2 times its initial value until peak stress. | [Zhou 2020, pp. 5-6] | Unfilled planar fracture sample. | Demonstrates different behavior from infilled fractures. |
| Sample permeability of infilled fractures increased with grout thickness at a deviatoric stress of 5 MPa. | [Zhou 2020, pp. 3-5] | Planar and rough infilled fractures. | Initial permeability depends on grout volume. |
| Rough infilled fractures had lower sample permeability than planar infilled fractures with the same grout thickness. | [Zhou 2020, pp. 3-5] | Comparison of R2 vs P2, R8 vs P8. | Effect of fracture surface morphology. |

## Limitations
1.  The study focused on fractures oriented parallel to the axial stress; the effect of fracture inclination angle was not investigated [Zhou 2020, pp. 8-9].
2.  The brittle failure of samples prevented measurement of post-peak permeability [Zhou 2020, pp. 9-10].
3.  Sample preparation for thin, rough fractures was challenging, sometimes leading to pre-existing flaws or pores in the grout [Zhou 2020, pp. 9-10].
4.  The effect of fracture surface roughness on permeability could not be well described by existing flow models [Zhou 2020, pp. 9-10].
5.  The study considered only low confining pressure (5 MPa), representative of shallow tunnels [Zhou 2020, pp. 2-3].

## Assumptions / Conditions
1.  Deionized water was used as the pore fluid, and silicone oil was used as the confining pressure fluid [Zhou 2020, pp. 2-3].
2.  The transient method for permeability measurement assumes Darcy's law applies [Zhou 2020, pp. 2-3].
3.  The 2D DEM models assume plane strain conditions and use circular disks to represent rock and grout particles [Zhou 2020, pp. 6-8].
4.  The confining pressure of 5 MPa was chosen to represent stress conditions in a subsea tunnel at depths of 150–200 m [Zhou 2020, pp. 2-3].

## Key Variables / Parameters
*   **Independent Variables:** Deviatoric stress, grout thickness (2, 5, 8 mm), fracture surface type (planar, rough, unfilled).
*   **Dependent Variables:** Sample permeability, axial strain, microcrack distribution.
*   **Controlled Parameters:** Confining pressure (5 MPa), sample dimensions, grout composition (water-to-cement ratio 0.6), loading rate.

## Reusable Claims
*   Under triaxial compression with low confining pressure (5 MPa), the permeability of grout-infilled granite fractures can increase by an order of magnitude (5-10 times) when the deviatoric stress reaches the peak strength, compared to its value at low stress (5 MPa) [Zhou 2020, pp. 1-2].
*   The primary mechanism for stress-induced permeability enhancement in grout-infilled fractures is the initiation and coalescence of cracks within the grout body and along the grout-rock interface [Zhou 2020, pp. 1-2, pp. 6-8].
*   The permeability evolution of grout-infilled fractures under compression exhibits two distinct phases: a slight reduction or fluctuation phase below the crack damage stress, followed by a rapid increase phase above it [Zhou 2020, pp. 5-6].
*   For a given fracture aperture, roughness reduces the initial permeability of a grout-infilled fracture compared to a planar one [Zhou 2020, pp. 3-5].

## Candidate Concepts
*   [[grout-infilled fracture]]
*   [[triaxial compression]]
*   [[permeability evolution]]
*   [[crack damage stress]]
*   [[excavation damage zone]]
*   [[pre-grouting]]
*   [[tunnel water inflow]]

## Candidate Methods
*   [[transient method]] for permeability measurement
*   [[particle-based discrete element method (DEM)]]
*   [[X-ray microfocus CT scanning]]
*   [[triaxial compression testing]]

## Connections To Other Work
*   The study builds on prior work on the mechanical behavior of rock samples with grout-infilled flaws [Zhou 2020, pp. 1-2].
*   It addresses a gap identified in the literature regarding the permeability evolution of grout-infilled fractures during the complete stress-strain process [Zhou 2020, pp. 2-2].
*   The findings have implications for predicting water inflow into pre-grouted tunnels, referencing analytical solutions from Li et al. (2018) [Zhou 2020, pp. 8-9].
*   The DEM modeling approach follows methodologies established by Potyondy and Cundall (2004) and Zhao and Zhou (2016) [Zhou 2020, pp. 6-8].

## Open Questions
*   How does the inclination angle of the grout-infilled fracture relative to the principal stresses affect its permeability evolution?
*   What is the post-peak permeability behavior of grout-infilled fractures, and how can it be measured?
*   How does the three-dimensional nature of fractures and grout failure influence permeability, and can 3D DEM models capture this?
*   How does the shear failure (slip) of grout-infilled fractures, which may occur in the excavation damage zone, affect permeability?
*   How can the effect of fracture surface roughness on the permeability of grout-infilled fractures be better quantified in flow models?

## Source Coverage
All 10 non-empty indexed fragments were processed. The compiled source blocks total 49,649 characters, achieving a coverage ratio of 1.000584 by character count relative to the indexed text (49,620 characters). The coverage status is full-index.
