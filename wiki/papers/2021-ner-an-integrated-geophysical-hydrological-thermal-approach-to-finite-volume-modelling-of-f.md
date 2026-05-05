---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-ner-an-integrated-geophysical-hydrological-thermal-approach-to-finite-volume-modelling-of-f"
title: "An Integrated Geophysical, Hydrological, Thermal Approach to Finite Volume Modelling of Fault-Controlled Geothermal Fluid Circulation in Gediz Graben."
status: "draft"
source_pdf: "data/papers/An integrated geophysical, hydrological, thermal approach to finite volume modelling of fault-controlled geothermal fluid circulation in Gediz Graben.pdf"
collections:
citation: "Üner, S., and D. Dusunur Dogan. \"An Integrated Geophysical, Hydrological, Thermal Approach to Finite Volume Modelling of Fault-Controlled Geothermal Fluid Circulation in Gediz Graben.\" *Geothermics*, vol. 90, 2021, 102004, doi:10.1016/j.geothermics.2020.102004."
indexed_texts: "8"
indexed_chars: "36424"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "34791"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.955167"
coverage_status: "full-index"
source_signature: "7b4247ed217296f7fcecac1b5ca8e07fad3741ad"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:28:38"
---

# An Integrated Geophysical, Hydrological, Thermal Approach to Finite Volume Modelling of Fault-Controlled Geothermal Fluid Circulation in Gediz Graben.

## One-line Summary
A first-of-its-kind integrated hydro-thermo-geophysical model using the finite volume method demonstrates the dominant role of the low-angle Master Graben Boundary Fault (MGBF) in controlling deep fluid circulation and heat distribution in the Gediz Graben geothermal system.

## Research Question
How do fault structures, particularly the low-angle Master Graben Boundary Fault (MGBF), control the patterns of geothermal fluid circulation and temperature distribution in the Gediz Graben, Western Anatolia?

## Study Area / Data
The study area is the Gediz Graben in Western Anatolia, Turkey, an East-West trending graben bordered by major normal faults. The model is based on two depth-migrated seismic reflection profiles (S-12 and S-8) that reveal the graben's sedimentary fill and fault geometry [Dusunur 2021, pp. 2-3]. Data inputs include thermal and physical rock properties from previous studies, well data (e.g., Alasehir-1 well with a thermal gradient of 41.6 °C/km), and outcrop-derived porosity and permeability values [Dusunur 2021, pp. 3-4]. The main thermomineral vent fields are located along the southern border of the graben [Dusunur 2021, pp. 2-3].

## Methods
The study employs a coupled transient fluid flow and heat transport numerical simulation using the finite volume method implemented in the ANSYS FLUENT software [Dusunur 2021, pp. 3-4]. The model geometry was created from seismic sections, discretized into 2D triangular meshes. The fluid flow is considered laminar and viscous, with density varying with temperature according to the Boussinesq approximation [Dusunur 2021, pp. 3-4]. The MGBF was partitioned into three segments (an impervious core and two permeable damaged flanks) to investigate its structural role [Dusunur 2021, pp. 3-4]. User Defined Functions (UDFs) were used to incorporate depth-dependent porosity and temperature-dependent viscosity and thermal conductivity [Dusunur 2021, pp. 3-4].

## Key Findings
1.  The low-angle MGBF has three dominant roles: transporting meteoric water to depth, distributing heated geothermal water into the basin via inner faults, and transmitting heated water to the surface [Dusunur 2021, pp. 1-2].
2.  Simulations show that the presence of faults perturbs the fluid flow pattern, creating convection cells even for systems with Rayleigh numbers below the critical value [Dusunur 2021, pp. 4-5].
3.  Fluid circulation in the shallow reservoir is mainly controlled by high-angle normal faults within the basin [Dusunur 2021, pp. 5-7].
4.  Calculated fluid velocities range from 5×10⁻¹⁶ m/s in the basement to a maximum of 2×10⁻¹¹ m/s within sedimentary units and faults, with high velocities accumulated at the base of the MGBF [Dusunur 2021, pp. 4-4].
5.  The model verifies the conceptual model where meteoric water penetrates downward through active faults, is heated at depth, and circulates back to the surface [Dusunur 2021, pp. 5-7].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| MGBF acts as a channel feeding the deep reservoir and bringing heated fluid upwards. | [Dusunur 2021, pp. 5-7] | Numerical simulation of S-12 seismic section. | Demonstrates the integrated role of the fault. |
| Fluid velocities range from 5×10⁻¹⁶ m/s to 2×10⁻¹¹ m/s. | [Dusunur 2021, pp. 4-4] | Model along S-12 seismic line. | Shows velocity variation between basement and faults/sediments. |
| Porosity values vary from 9% to 28% with depth, calculated every 200 m. | [Dusunur 2021, pp. 3-4] | Implemented via User Defined Function (UDF). | Accounts for porosity collapse with depth. |
| Permeability of MGBF damage zone is 1.0E-15 m²; core is 1.0E-18 m². | [Dusunur 2021, pp. 5-7] | Assigned cell condition in the model. | Highlights the contrast between fault core and damage zone. |
| High-angle normal faults within the basin control shallow reservoir circulation. | [Dusunur 2021, pp. 5-7] | Simulation results from both S-12 and S-8 models. | Identifies secondary structural control. |
| The model is the first complete hydro-thermo-geophysical model for the Gediz Graben. | [Dusunur 2021, pp. 1-2] | Study context. | States the novelty of the integrated approach. |

## Limitations
1.  Porosity and permeability values from outcrop samples may not exactly represent true values at depth due to confining pressure and surface weathering effects [Dusunur 2021, pp. 3-4].
2.  The model assumes local thermal equilibrium between fluid and solid in the porous media [Dusunur 2021, pp. 3-4].
3.  The study is based on 2D cross-sectional models, which may not capture all 3D flow complexities.

## Assumptions / Conditions
1.  Fluid flow is laminar and viscous; inertial effects are neglected due to slow accelerations [Dusunur 2021, pp. 3-4].
2.  Darcy's law is valid for flow in the porous media [Dusunur 2021, pp. 3-4].
3.  The vertical sides of the model are impermeable and adiabatic; the upper surface has a constant temperature of 17 °C [Dusunur 2021, pp. 3-4].
4.  Permeability and heat capacity are constant and uniform within the same rock unit but vary between units [Dusunur 2021, pp. 3-4].
5.  The main heat source is the high regional geothermal gradient, not magmatic intrusion [Dusunur 2021, pp. 3-4].

## Key Variables / Parameters
-   **Permeability:** Ranges from 1.0E-18 m² (basement, MGBF core) to 1.0E-15 m² (MGBF damage zone) [Dusunur 2021, pp. 5-7].
-   **Porosity:** Varies from 2% to 35% in outcrops; modeled with depth-dependent collapse from 28% to 9% [Dusunur 2021, pp. 3-4].
-   **Thermal Conductivity:** Varies by unit (e.g., Basement: 3.10 W/m·K, SSU1: 1.93 W/m·K) and is temperature-dependent via UDF [Dusunur 2021, pp. 5-7].
-   **Fluid Viscosity:** Temperature-dependent, implemented via UDF [Dusunur 2021, pp. 3-4].
-   **Geothermal Gradient:** 41.6 °C/km from Alasehir-1 well data [Dusunur 2021, pp. 3-4].
-   **Precipitation:** Average of 727.8 mm/yr (1929-2017) used as recharge [Dusunur 2021, pp. 3-4].

## Reusable Claims
1.  In extensional graben systems, low-angle master boundary faults can act as integrated conduits, simultaneously channeling recharge to depth and providing pathways for heated fluid ascent to the surface [Dusunur 2021, pp. 1-2, 5-7].
2.  The presence of faults can induce permeability anisotropy and perturb regional fluid flow, generating fault-bounded convection cells even when the bulk Rayleigh number is subcritical [Dusunur 2021, pp. 4-5].
3.  Shallow geothermal reservoir circulation in faulted basins is primarily controlled by the geometry and permeability of high-angle intra-basin faults [Dusunur 2021, pp. 5-7].
4.  Numerical modeling using finite volume methods can effectively integrate seismic structural data with petrophysical and thermal parameters to simulate coupled hydro-thermal processes in geothermal systems [Dusunur 2021, pp. 3-4].

## Candidate Concepts
-   [[Fault-controlled geothermal circulation]]
-   [[Finite volume method]]
-   [[Hydro-thermo-geophysical model]]
-   [[Master Graben Boundary Fault (MGBF)]]
-   [[Boussinesq approximation]]
-   [[Geothermal reservoir]]
-   [[Convective heat transfer]]

## Candidate Methods
-   [[Finite volume modelling]]
-   [[Computational Fluid Dynamics (CFD)]]
-   [[Numerical simulation of coupled processes]]
-   [[Seismic interpretation for model geometry]]
-   [[User Defined Functions (UDF) for parameterization]]

## Connections To Other Work
The study builds upon and verifies a conceptual model proposed by earlier hydrogeological and geochemical studies (e.g., Tarcan et al., 2005; Hacıoğlu et al., 2020) [Dusunur 2021, pp. 2-3]. It extends previous numerical modeling work on fault influences (e.g., López and Smith, 1995; Simms and Garven, 2004) by applying an integrated approach to a specific, well-documented natural laboratory [Dusunur 2021, pp. 1-2]. The model uses petrophysical data from Çiftçi et al. (2010) and Balkan et al. (2017) [Dusunur 2021, pp. 3-4].

## Open Questions
1.  How would a fully 3D model alter the predicted flow patterns and convection cell geometries?
2.  What is the sensitivity of the model results to the assumed permeability contrast between the fault core and damage zone?
3.  Can this modeling framework be successfully applied to other geothermal provinces in Western Anatolia with different fault geometries?

## Source Coverage
All non-empty indexed fragments were processed. The compilation is based on 8 source blocks containing 36,424 characters. The compiled page incorporates 34,791 characters from these sources, achieving a coverage ratio of 0.955 by character count. The coverage status is full-index.
