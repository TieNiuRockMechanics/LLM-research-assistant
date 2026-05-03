---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2017-lei-the-use-of-discrete-fracture-networks-for-modelling-coupled-geomechanical-and-hydrologi"
title: "The Use of Discrete Fracture Networks for Modelling Coupled Geomechanical and Hydrological Behaviour of Fractured Rocks."
status: "draft"
source_pdf: "data/papers/2017 - The use of discrete fracture networks for modelling coupled geomechanical and hydrological behaviour of fractured rocks.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Lei, Qinghua, et al. \"The Use of Discrete Fracture Networks for Modelling Coupled Geomechanical and Hydrological Behaviour of Fractured Rocks.\" *Computers and Geotechnics*, vol. 85, 2017, pp. 151-176, doi:10.1016/j.compgeo.2016.12.024. Accessed 15 Mar. 2026."
indexed_texts: "35"
indexed_chars: "174105"
nonempty_source_blocks: "35"
compiled_source_blocks: "35"
compiled_source_chars: "174847"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004262"
coverage_status: "full-index"
source_signature: "18d267a4772cc006bc2f25c88d43d33a43a232f0"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T19:37:44"
---

# The Use of Discrete Fracture Networks for Modelling Coupled Geomechanical and Hydrological Behaviour of Fractured Rocks.

## One-line Summary
This paper reviews the state-of-the-art of discrete fracture network (DFN) models for representing the geometrical characteristics, geomechanical evolution, and the influence of stress on fluid flow and transport in fractured rocks, and provides recommendations for future coupled hydromechanical (HM) modelling.

## Research Question
The paper addresses the challenge of modelling the coupled hydromechanical (HM) behaviour of fractured rocks by examining the key subject areas progressively: the geometrical representation of complex fracture networks, the numerical methods for modelling their geomechanical behaviour, and the impact of geomechanical effects on fluid flow and transport. The overarching focus is to discuss the features or characteristics of a fracture network model needed to properly simulate coupled HM processes in fractured rocks. [Lei 2017, pp. 2-3]

## Study Area / Data
The paper is a review and does not centre on a single study area. It draws upon a wide range of published modelling studies. Data sources and application examples discussed include:
- Geologically-mapped fracture networks from limestone outcrops at the south margin of the Bristol Channel Basin, UK. [Lei 2017, pp. 2-3]
- Sandstone exposures in the Dounreay area, Scotland. [Lei 2017, pp. 3-4]
- Fault zone structures in the Valley of Fire State Park of southern Nevada, USA. [Lei 2017, pp. 3-4]
- Field data from the Sellaﬁeld site, Cumbria, UK, used for stochastic DFN modelling. [Lei 2017, pp. 4-4]
- Data from the Fanay-Augères Mine and the Stripa Mine, Sweden. [Lei 2017, pp. 22-23]
- Data from the Forsmark site in Sweden for model calibration. [Lei 2017, pp. 22-23]

## Methods
The paper reviews three main approaches for representing natural fracture networks:
- **Geologically-mapped DFNs:** Digitised outcrop analogues are used to build DFNs, preserving natural features and complex topologies. [Lei 2017, pp. 2-3]
- **Stochastically-generated DFNs:** These are based on statistical distributions of geometrical properties (orientation, size, position, aperture) derived from field measurements. This includes the conventional Poisson DFN model, fractal DFN models based on fractal dimension (D) and power-law length exponent (a), and improved models incorporating spatial clustering, attribute correlation, and topological complexity. [Lei 2017, pp. 3-6]
- **Geomechanically-grown DFNs:** These incorporate fracture growth physics, such as linear elastic fracture mechanics (LEFM), to simulate fracture network evolution as a response to palaeo-stress/strain conditions. [Lei 2017, pp. 6-6]

It also reviews numerical models for the geomechanical behaviour of fractured rock integrating DFN information:
- **Continuum/extended-continuum models:** These use equivalent/homogenised properties derived analytically or numerically, or represent fractures as softened weak elements within a fine mesh. [Lei 2017, pp. 8-9]
- **Block-type discontinuum models:** This includes the Distinct Element Method (DEM) and Discontinuous Deformation Analysis (DDA), which solve interactions between discrete blocks. [Lei 2017, pp. 9-11]
- **Particle-based discontinuum models:** This includes the Bonded-Particle Model (BPM) and Synthetic Rock Mass (SRM) approach, where rock is an assembly of cemented particles and fractures are represented by smooth-joint contact models (SJM). [Lei 2017, pp. 11-13]
- **Hybrid finite-discrete element models (FEMDEM/FDEM):** This includes ELFEN and Y-code, which combine FEM for stress/deformation evolution with DEM for transient dynamics, contact detection, and brittle fracture propagation. [Lei 2017, pp. 13-14]

Finally, it reviews hydrological studies that investigate geomechanical effects on fluid pathways, permeability, and transport in DFNs. [Lei 2017, pp. 16-19]

## Key Findings
- **DFN Model Selection:** Stochastic DFN models, despite their efficiency and 3D applicability, can lead to systematic biases from truth due to oversimplified geometries. Fractal/clustered characteristics and power-law size distributions significantly impact connectivity, permeability, flow patterns, and geomechanical behaviour and must be incorporated into DFN generation. [Lei 2017, pp. 4-6]
- **Geomechanical Model Features:** Discontinuum models (like DEM, SRM, FEMDEM) can more straightforwardly incorporate complex DFNs and model multi-fracturing processes without assuming a Representative Elementary Volume (REV). The FEMDEM method is capable of simulating the reactivation of pre-existing fractures and propagation of new cracks, which is crucial for capturing permeability evolution. [Lei 2017, pp. 8-14]
- **Stress-Dependent Fluid Pathways:** Geomechanical conditions cause heterogeneous stress fields, leading to variable fracture closure, shearing, and dilation. This reorganises fluid pathways, with flow often channelling into critically-oriented, connected fractures that undergo shear dilation under high differential stresses. [Lei 2017, pp. 16-16]
- **Stress-Dependent Permeability:** Permeability is highly sensitive to burial depth, decreasing with mean stress due to fracture closure. With increasing differential stress, permeability initially decreases but can abruptly increase beyond a critical stress ratio as shear dilation occurs. Permeability anisotropy is also enhanced by stress ratios. Fracture propagation can further significantly raise permeability. [Lei 2017, pp. 16-17]
- **Stress-Dependent Transport:** Compressive stresses can attenuate solute dispersivity by closing fractures, increasing average residence time. However, high differential stress can drastically decrease residence time by creating high-velocity dilated flow channels, causing earlier breakthrough. Inactive fractures and dead-ends are important for stagnating solutes via matrix diffusion. [Lei 2017, pp. 17-19]
- **Necessity of Realistic Features:** Hydraulically inactive fractures (dead-ends, isolated fractures) should be preserved in DFNs for HM modelling as they can serve as sites for new fracture propagation and provide surface area for diffusive mass transfer. Curved, non-planar fractures can accommodate large localised dilational jogs, critically affecting permeability. [Lei 2017, pp. 19-19]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Stochastic DFN models ignoring clustering and power-law scaling can produce systematically biased predictions compared to the truth. | [Lei 2017, pp. 4-6] | General statement on the limitations of conventional Poisson DFN models. | Supports the need for more physically-based DFN generation. |
| The fractal dimension D and power-law length exponent a control the connectivity, permeability, and strength of fractured rocks. | [Lei 2017, pp. 4-4] | Based on synthesis of fractal geometry and power-law models for fracture networks. | Key parameters for characterising fracture network statistics. |
| The DEM-DFN model can capture an abrupt increase in deformability when fracture density exceeds a mechanical percolation threshold, higher than the geometrical one. | [Lei 2017, pp. 9-9] | Study by Zhang and Sanderson using UDEC. | Implication: mechanical connectivity is not equivalent to geometrical connectivity. |
| The equivalent elastic modulus of fractured rocks increases with confining stress, while Poisson's ratio generally decreases but can exceed 0.5. | [Lei 2017, pp. 9-9] | Study by Min and Jing (2004) using a DFN-DEM technique. | Shows the stress-dependency of equivalent continuum properties. |
| Under high differential stress, only a small portion of critically-oriented, well-connected, and long fractures dilate to form major flow channels. | [Lei 2017, pp. 16-16] | Study by Min et al. (2004) using DEM with power-law length distribution. | Finding is augmented if initial apertures are broadly distributed and correlated with length. |
| Permeability exhibits a decrease-then-increase behaviour separated by a critical stress ratio that initiates shear dilation. | [Lei 2017, pp. 16-17] | Study by Min et al. (2004) for fractured rocks with constant initial aperture. | Observed similarly with increasing pore fluid pressure. |
| Propagation of new cracks from tips of pre-existing fractures under stress can create new pathways, increasing network connectivity and permeability. | [Lei 2017, pp. 14-17] | Observed by Latham et al. (2013) and others using FEMDEM and FDM. | Highlights the limitation of removing dead-end fractures in simulations. |
| Solute residence time in a fracture network increases under moderate stress ratios (<3) but decreases when high stress ratios trigger shear dilation. | [Lei 2017, pp. 17-19] | Study by Zhao et al. (2011) coupling UDEC DEM with a particle tracking code. | Includes the effects of matrix diffusion and sorption. |

## Limitations
- **Geologically-mapped DFNs:** Limited feasibility for deep rocks and difficulty in building 3D structures; constrained by measurement scale and resolution. [Lei 2017, pp. 6-8]
- **Stochastic DFNs:** Oversimplification of fracture geometries and topologies leads to large uncertainties; negligence of physical processes. [Lei 2017, pp. 6-8]
- **Geomechanical DFNs:** High uncertainty in input properties (palaeostress, rock properties) and tectonic conditions; large computational time; often neglect coupled THM (thermal-hydrological-mechanical-chemical) processes. [Lei 2017, pp. 6-8]
- **Continuum Geomechanical Models:** Cannot adequately consider stress variations, fracture interactions and block rotations; validity is based on the existence of an REV, which may not exist for natural systems. [Lei 2017, pp. 14-16]
- **Discontinuum Geomechanical Models:** Input parameters like bonding strength or joint stiffness often need indirect numerical calibration rather than from direct physical measurements; computational time can be considerably large. [Lei 2017, pp. 14-16]
- **HM Modelling:** Most reviewed studies focus on the geomechanical effects on hydrology ("one-way coupling"), while the reverse effect of fluid flow on rock mass deformation is also a very important issue. [Lei 2017, pp. 19-19]

## Assumptions / Conditions
- A "DFN" here broadly refers to any explicit fracture network model, including those from mapping, stochastic realisation, or geomechanical simulation. [Lei 2017, pp. 2-3]
- For upscaling and continuum models, an REV is assumed, though its existence is not guaranteed for natural systems. [Lei 2017, pp. 14-16]
- The power-law length model is bounded by upper (related to crustal thickness) and lower (related to grain size or measurement resolution) limits. For numerical simulations, the model size L typically meets l_min ≪ L ≪ l_max. [Lei 2017, pp. 4-4]
- In block-type DEM and DDA, dead-ends and isolated fractures are usually removed for simplicity, which is an assumption that may be acceptable for extremely hard rocks but not for most rock types where crack propagation is important. [Lei 2017, pp. 14-16]
- The review is focused on HM behaviour and is not exhaustive; only limited references are cited for brevity. [Lei 2017, pp. 2-3]

## Key Variables / Parameters
- **Geometrical (DFN):** Fracture orientation, size (length), position, shape, aperture, density (P30/P20/P10) and intensity (P32/P21/P10) [Lei 2017, pp. 3-4]
- **Stochastic Descriptors:** Fractal dimension (D), power-law length exponent (a), density term (α) [Lei 2017, pp. 4-4]
- **Geomechanical:** In-situ stress (magnitude, direction, ratio), joint stiffness (normal and shear), joint friction, tensile strength, cohesion, elastic modulus, Poisson's ratio [Lei 2017, pp. 9-15]
- **Fracture Mechanics:** Stress intensity factor (KI), subcritical index (n) or velocity exponent (j), energy release rate (G), material toughness (KIC), stress corrosion limit (KO) [Lei 2017, pp. 6-6]
- **Hydrological:** Equivalent and effective permeability, fracture transmissivity (governed by cubic law), fluid velocity, dispersivity, solute residence time [Lei 2017, pp. 16-19]

## Reusable Claims
- **Claim:** Synthetic rock mass (SRM) models, which integrate explicit DFN representations, have an advantage over the Hoek-Brown approach for deriving orientation-specific strength and considering the influence of fracture length distribution and connectivity. [Lei 2017, pp. 11-13]
- **Condition/Limitation:** The SRM approach uses smooth-joint models to overcome particle interlocking; accuracy depends on realistic representation of grain shapes and textures (mesh dependency). [Lei 2017, pp. 11-13]
- **Claim:** Fracture permeability exhibits a decrease, then an abrupt increase, as the differential stress ratio increases, with a critical ratio defining the onset of large-scale shear dilation and permeability enhancement. [Lei 2017, pp. 16-17]
- **Condition/Limitation:** This non-monotonic behaviour is observed under high differential stresses where shearing of critically-oriented, well-connected fractures can occur; the specific critical ratio depends on fracture properties. [Lei 2017, pp. 16-17]
- **Claim:** Bent, non-planar natural fractures can accommodate localized dilation (jogs) under high differential stress, leading to a significant increase in permeability and a more highly anisotropic permeability tensor, an effect not captured by planar DFN assumptions. [Lei 2017, pp. 16-17]
- **Condition/Limitation:** This claim is supported by FEMDEM and coupled FDM models of realistic fracture geometries under high differential stress conditions. [Lei 2017, pp. 15-17]

## Candidate Concepts
- [[discrete fracture network]]
- [[fractured rock]]
- [[hydromechanical coupling]]
- [[fracture permeability]]
- [[fractal fracture network]]
- [[representative elementary volume]]
- [[distinct element method]]
- [[bonded-particle model]]
- [[synthetic rock mass]]
- [[smooth-joint contact model]]
- [[finite-discrete element method]]
- [[power-law scaling]]
- [[fracture propagation]]
- [[solute transport]]
- [[stress-dependent permeability]]

## Candidate Methods
- [[DFN generation from geological mapping]]
- [[stochastic DFN modelling (Poisson model)]]
- [[fractal DFN generation]]
- [[geomechanical fracture growth simulation (LEFM)]]
- [[extended-continuum modelling with weak fracture elements]]
- [[block-type distinct element method (DEM) with DFN]]
- [[discontinuous deformation analysis (DDA) for fractured rock]]
- [[particle-based synthetic rock mass (SRM) modelling]]
- [[hy brid finite-discrete element method (FEMDEM/FDEM)]]
- [[coupled DEM-particle tracking for transport modelling]]
- [[DFN calibration with borehole and tunnel data]]
- [[DFN model upscaling with self-referencing random walks]]

## Connections To Other Work
- **DFN Reviews:** The paper builds upon and directs readers to more extensive reviews by Dershowitz and Einstein (1988), Liu et al. (2016), and textbooks by Adler and Thovert (1999) and Adler et al. (2012). [Lei 2017, pp. 2-3]
- **Rock Mechanics Reviews:** Connections are made to reviews of numerical methods by Jing and Hudson (2002), Jing (2003), Lisjak and Grasselli (2014), and others. [Lei 2017, pp. 2-3]
- **HM Reviews:** It explicitly relates to reviews on HM coupling by Rutqvist and Stephansson (2003) and stress effects on fluid flow by Zhang and Sanderson (2002). [Lei 2017, pp. 2-3]
- **Fracture Formation:** The geomechanical DFN models connect to field observations (e.g., Pollard & Aydin, 1988; Engelder & Geiser, 1980) and fundamental fracture mechanics work (e.g., Atkinson, 1984). [Lei 2017, pp. 6-6]
- **Hydraulic Fracturing:** It briefly notes the connection to recent developments in modelling fluid-driven fracture propagation in pre-existing DFNs (e.g., Kresse et al., 2013; Fu et al., 2013). [Lei 2017, pp. 19-19]

## Open Questions
- How to create more realistic DFNs that capture key characteristics like clustering, scaling, connectivity, termination, curvature, and aperture-size correlation. [Lei 2017, pp. 19-20]
- How to develop appropriate upscaling approaches that preserve geostatistical and geomechanical characteristics for evaluating large-scale behaviour. [Lei 2017, pp. 19-20]
- How to develop more advanced "two-way" coupling schemes and extend models to complex 3D systems and multiphase flow. [Lei 2017, pp. 19-20]
- How to develop robust calibration and validation procedures for DFN models using field measurements from underground research laboratories, hydraulic tests, and tracer tests. [Lei 2017, pp. 19-20]
- The question of how to create realistic fracture networks remains an unresolved issue, particularly concerning the extrapolation from 1D/2D data to 3D. [Lei 2017, pp. 1-2]

## Source Coverage
All non-empty indexed fragments were processed. Coverage: 35 of 35 source blocks, representing 1.0043 of the indexed character volume (174,105 source chars, 174,847 compiled chars). The source signature is 18d267a4772cc006bc2f25c88d43d33a43a232f0. Compile strategy: single-pass-markdown.
