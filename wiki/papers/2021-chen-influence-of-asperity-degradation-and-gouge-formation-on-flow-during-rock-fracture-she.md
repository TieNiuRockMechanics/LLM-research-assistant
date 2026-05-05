---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-chen-influence-of-asperity-degradation-and-gouge-formation-on-flow-during-rock-fracture-she"
title: "Influence of Asperity Degradation and Gouge Formation on Flow During Rock Fracture Shearing."
status: "draft"
source_pdf: "data/papers/Influence of asperity degradation and gouge formation on flow during rock fracture shearing.pdf"
collections:
citation: "Chen, Yuedu, et al. \"Influence of Asperity Degradation and Gouge Formation on Flow During Rock Fracture Shearing.\" *International Journal of Rock Mechanics & Mining Sciences*, vol. 143, 2021, 104795. Accessed 2026."
indexed_texts: "13"
indexed_chars: "63163"
nonempty_source_blocks: "13"
compiled_source_blocks: "13"
compiled_source_chars: "59022"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.934439"
coverage_status: "full-index"
source_signature: "189a858120798dc8211c85fd926833d369983a4f"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:26:23"
---

# Influence of Asperity Degradation and Gouge Formation on Flow During Rock Fracture Shearing.

## One-line Summary
This study experimentally and numerically investigates how shear-induced asperity degradation and gouge formation control the evolution of fracture geometry and permeability, demonstrating a transition from shear-dilation-enhanced flow to gouge-blocked channelized flow.

## Research Question
How do the shear-induced processes of asperity degradation and gouge formation affect the evolution of fracture geometries and the resulting fluid flow behavior in rock fractures?

## Study Area / Data
The experimental data comes from a cylindrical sandstone sample (50 mm diameter × 96 mm height) obtained from the Xiegou coal mine in Shanxi Province, China [Chen 2021, pp. 3-3]. A single rough fracture was produced in the sample using the Brazilian splitting test [Chen 2021, pp. 3-3]. The sandstone is composed of 54% Quartz, 16% Microcline, 12% Albite, 10% Calcite, with a grain size of 0.12–0.25 mm [Chen 2021, pp. 3-3].

## Methods
The study combined experimental shear-flow tests with numerical modeling and simulation.
*   **Experimental:** A direct shear-flow test was conducted on the fractured sample under a constant confinement pressure of 4 MPa and a shear displacement rate of 0.12 mm/min [Chen 2021, pp. 3-3]. A constant flow rate of 10 ml/min was injected at each shear step to measure permeability [Chen 2021, pp. 3-3]. 3D scanning (OKIO-H-200 scanner) was used to characterize the morphologies of the fracture surfaces before and after shearing [Chen 2021, pp. 3-3].
*   **Numerical:** A simplified modeling algorithm was proposed to quantitatively characterize asperity degradation and gouge accumulation during shear [Chen 2021, pp. 6-8]. The algorithm discretizes the fracture surfaces into a lattice, calculates gouge volume from inter-penetration, and redistributes it into void spaces [Chen 2021, pp. 6-8]. A series of 3D fracture geometry models at different shear stages were established to conduct Navier-Stokes (N-S) flow simulations using COMSOL™ software [Chen 2021, pp. 8-10].

## Key Findings
1.  Fracture permeability evolution during shearing is closely related to geometry changes. Permeability increases significantly with shear dilation at early stages but decreases gradually at the residual stage due to gouge formation blocking flow paths [Chen 2021, pp. 14-14].
2.  The modeled distributions of asperity degradation and gouge, as well as the normalized permeability change, correlated well with experimental measurements [Chen 2021, pp. 1-1].
3.  Fracture permeability is affected not only by aperture but also by the distribution, location, and size of contacts evolving during shear [Chen 2021, pp. 1-1].
4.  Channeling flow becomes more dominant as shear displacement increases, controlled by contact zones that span the fracture width and block flow paths [Chen 2021, pp. 1-1]. Fluid flow transforms from dispersion at early stages to apparent channeling along the narrow side of the fracture at later stages [Chen 2021, pp. 1-1].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Permeability increased to a maximum of ~1.87E-10 m² at a shear displacement of 7 mm, then decreased. | [Chen 2021, pp. 3-3] | Cylindrical sandstone sample, 4 MPa confinement, 10 ml/min flow rate. | Measured via shear-flow test using the cubic law. |
| Contact zones reorganize during shearing, gathering where higher-order asperities abut opposing walls. | [Chen 2021, pp. 12-13] | Numerical modeling of fracture geometries at various shear displacements. | Contact ratio decreased to ~10% at 7 mm shear, then increased to ~29% at 15 mm. |
| Streamlines become more channeled with observable tortuosity under increasing shear displacements. | [Chen 2021, pp. 13-14] | N-S flow simulations in 3D fracture models. | Channeling is largely controlled by contact locations spanning the fracture width. |
| The simplified modeling algorithm's predicted asperity degradation and gouge distribution matched test observations. | [Chen 2021, pp. 11-12] | Comparison of 3D scan data (with developer dye) and model output. | Positive values (degradation) and negative values (gouge) correlated well. |
| The model assumes shear-induced dilation is uniform and gouge is distributed evenly around degradation zones. | [Chen 2021, pp. 6-8] | Simplified modeling algorithm. | These assumptions may not apply to rocks with heterogeneous mineral compositions. |

## Limitations
*   The modeling algorithm assumes that shear-induced dilation is distributed uniformly over the whole fracture surface and that gouge is distributed evenly around degradation zones [Chen 2021, pp. 6-8]. This may not be valid for rocks with heterogeneous mineral compositions or material property differences [Chen 2021, pp. 13-14].
*   The model neglects the movement of gouge particles carried by fluid flow [Chen 2021, pp. 6-8].
*   The study does not account for potential long-term weakening of surface asperities due to fluid infiltration, chemical effects, or high-temperature damage [Chen 2021, pp. 13-14].
*   The geometric reconstruction in COMSOL™ required assigning a small aperture (~10 μm) to contact elements to avoid computational errors [Chen 2021, pp. 8-10].

## Assumptions / Conditions
*   Shear-induced dilation normal to the fracture is uniform over the entire surface [Chen 2021, pp. 6-8].
*   Negative aperture (inter-penetration) is recognized as asperity degradation [Chen 2021, pp. 6-8].
*   Gouge generated from degradation is distributed around degradation zones, and its movement by fluid flow is neglected [Chen 2021, pp. 6-8].
*   The damage of interlocked asperities on upper and lower surfaces contributes equally to gouge generation [Chen 2021, pp. 6-8].
*   Flow simulations assume steady, incompressible, isothermal, single-phase Newtonian fluid flow [Chen 2021, pp. 8-10].
*   Experiments were conducted under isothermal conditions (~25°C) with the outlet open to atmosphere [Chen 2021, pp. 3-3].

## Key Variables / Parameters
*   Shear Displacement
*   Normal Dilation (ΔW)
*   Fracture Permeability
*   Contact Ratio
*   Mean Aperture
*   Flow Velocity
*   Water Pressure
*   Shear Stress (τ/σₙ)
*   Gouge Volume (Nᵢ,ⱼ)

## Reusable Claims
*   **Claim:** Shear dilation increases fracture permeability at early shearing stages, but this effect is offset by gouge formation at residual stages, leading to reduced permeability. **Condition:** Observed in a cylindrical sandstone sample under 4 MPa confinement. **Limitation:** The transition point and magnitude depend on rock type and gouge properties.
*   **Claim:** The distribution, location, and size of evolving contacts during shear significantly affect fracture permeability, not just the mean aperture. **Condition:** Based on N-S flow simulations in 3D fracture geometries. **Limitation:** The model assumes uniform initial dilation and even gouge distribution.
*   **Claim:** Fluid flow in sheared fractures transforms from a dispersed pattern to an apparent channeling flow along the narrow side of the fracture as shear displacement increases. **Condition:** Demonstrated through N-S flow simulations. **Limitation:** Channeling is controlled by contact zones that span the fracture width, which may vary with rock type.

## Candidate Concepts
*   [[asperity degradation]]
*   [[gouge formation]]
*   [[fracture permeability]]
*   [[shear-flow coupling]]
*   [[channeling flow]]
*   [[fracture geometry evolution]]
*   [[contact ratio]]
*   [[shear dilation]]

## Candidate Methods
*   [[Brazilian splitting test]]
*   [[direct shear-flow test]]
*   [[3D scanning]]
*   [[Navier-Stokes flow simulation]]
*   [[simplified modeling algorithm]]
*   [[point cloud matching technique]]
*   [[binarization processing]]

## Connections To Other Work
*   The study builds on prior experimental work assessing flow in fractures during shear under different boundary conditions (e.g., constant normal load/stiffness) and flow directions [Chen 2021, pp. 1-3].
*   It addresses a gap identified in previous research that often focused only on shear-dilation-induced permeability increase while neglecting asperity degradation effects [Chen 2021, pp. 1-3].
*   The theoretical development references work by Nguyen and Selvadurai, who assumed gouge production is related to plastic work of shear stresses and used the cubic law [Chen 2021, pp. 1-3].
*   The observation of asperity degradation and gouge formation is consistent with published test results and microscopic DEM studies [Chen 2021, pp. 6-8].

## Open Questions
*   How do heterogeneous mineral compositions and material property differences between rock regions affect the distribution and impact of gouge formation?
*   What are the long-term effects of fluid infiltration, chemical reactions, or high-temperature damage on surface asperity properties and subsequent gouge generation?
*   How does the washing away of small gouge particles by fluid flow influence aperture changes and permeability evolution during shear?

## Source Coverage
All 13 non-empty indexed fragments were processed. The coverage ratio by blocks is 1.0, and the coverage ratio by characters is 0.934439. The source signature is `189a858120798dc8211c85fd926833d369983a4f`.
