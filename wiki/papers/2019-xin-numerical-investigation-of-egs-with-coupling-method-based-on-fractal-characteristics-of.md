---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-xin-numerical-investigation-of-egs-with-coupling-method-based-on-fractal-characteristics-of"
title: "Numerical Investigation of EGS with Coupling Method Based on Fractal Characteristics of Fracture System."
status: "draft"
source_pdf: "data/papers/考虑岩体裂缝系统分形特征的EGS耦合数值模拟研究_辛莹.pdf"
collections:
citation: "Xin, Ying. \"Numerical Investigation of EGS with Coupling Method Based on Fractal Characteristics of Fracture System.\" Master's thesis, China University of Petroleum (East China), 2019."
indexed_texts: "18"
indexed_chars: "89170"
nonempty_source_blocks: "18"
compiled_source_blocks: "18"
compiled_source_chars: "86511"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.970181"
coverage_status: "full-index"
source_signature: "31204580045e0fbe5d498f1f2a523d2997446cc8"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T11:16:19"
---

# Numerical Investigation of EGS with Coupling Method Based on Fractal Characteristics of Fracture System.

## One-line Summary
This study develops and validates a thermo-hydro-mechanical (THM) coupled numerical model for Enhanced Geothermal Systems (EGS) that incorporates the fractal characteristics of fracture systems to investigate heat extraction performance at core and field scales.

## Research Question
The core research question is to reveal the mass and heat transfer mechanism between the heat-carrying fluid (water) and the high-temperature thermal reservoir in an EGS, considering the THM coupling effects and the fractal characteristics of the rock fracture system [Xin 2019, pp. 1-6].

## Study Area / Data
The research utilizes numerical models at two scales:
- **Core Scale:** A 3D model of a single rough fracture (Φ50 mm × 80 mm) for simulating fluid flow and heat transfer. Model validation was performed against laboratory physical simulation experiments using a granite sample with a straight fracture [Xin 2019, pp. 43-50].
- **Field Scale:** An idealized 3D model of a dual horizontal well EGS system (600 m × 500 m × 600 m reservoir) located at a depth of 1150 m, containing discrete fracture networks generated based on fractal characteristics [Xin 2019, pp. 62-69].

## Methods
1.  **Fractal Characterization:** Used spectral synthesis method to construct realistic rough fracture surfaces with different fractal dimensions (D = 2.2, 2.4, 2.6, 2.8) [Xin 2019, pp. 13-14]. For field-scale fracture networks, a fractal relationship between fracture length and number was applied [Xin 2019, pp. 15-19].
2.  **Mathematical Modeling:** Established a THM coupling mathematical model for EGS mass and heat transfer. The model includes governing equations for temperature field (heat conduction and convection), seepage field (Darcy's law), and stress field (elastic deformation), along with their finite element formulations [Xin 2019, pp. 23-32].
3.  **Numerical Simulation:** Implemented and solved the THM coupled model using the commercial finite element software COMSOL Multiphysics. The model was validated by comparing core-scale results with experimental data and field-scale results with analytical solutions [Xin 2019, pp. 33-36, 50-52].
4.  **Analysis:** Applied fractal analysis to process seepage and temperature field results at the core scale. Conducted single-factor and orthogonal test analyses on factors affecting average outlet temperature. Constructed a thermal recovery evaluation system for the field-scale model, assessing parameters like outlet temperature, heat production, power generation, energy efficiency, and heat recovery rate [Xin 2019, pp. 42-48, 58-70].

## Key Findings
1.  Higher fractal dimension (D) leads to more irregular fracture surface distribution [Xin 2019, pp. 13-14, 71].
2.  The established THM coupled mathematical model and solution method were verified as reliable through comparison with experimental and analytical results [Xin 2019, pp. 33-36, 50-52, 71].
3.  Numerical simulations at both core and field scales revealed strong THM coupling effects during fluid flow and heat transfer, consistent with general conclusions [Xin 2019, pp. 49, 70-71].
4.  Fluid flow on rough fracture surfaces exhibits high heterogeneity and localization; a larger fractal dimension increases the heterogeneity of the seepage field distribution. A fitting formula between fractal dimension and equivalent hydraulic conductivity coefficient was derived [Xin 2019, pp. 43-45, 71].
5.  Among factors affecting core-scale average outlet temperature, the most significant is average fracture aperture, followed by rock thermal expansion coefficient and injection temperature [Xin 2019, pp. 46-48, 71].
6.  For field-scale EGS with dual horizontal wells: interconnected fracture networks with higher bifurcation numbers yield higher heat production and power generation; unconnected networks show advantages in energy efficiency; more fractures and higher bifurcation numbers increase local and overall heat recovery rates near the production well [Xin 2019, pp. 61-70].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Fractal dimension D higher -> fracture surface more irregular. | [Xin 2019, pp. 13-14] | Spectral synthesis method used to generate surfaces with D=2.2, 2.4, 2.6, 2.8. | Visual observation from generated surfaces. |
| THM model validated against lab experiment (granite sample, 92°C, 40°C water). | [Xin 2019, pp. 33-36] | Core-scale single straight fracture model. | Numerical and experimental temperature curves showed good agreement over time. |
| THM model validated against analytical solution for fracture flow and heat transfer. | [Xin 2019, pp. 50-52] | Field-scale single fracture model with specific parameters (e.g., T_r0=80°C, T_w0=30°C). | Numerical and analytical temperature distributions were very close. |
| Larger fractal dimension D -> greater heterogeneity in seepage field distribution. | [Xin 2019, pp. 43-45] | Core-scale rough fracture models with D=2.2, 2.4, 2.6, 2.8. | Fractal analysis of velocity distribution on a cross-section. |
| Fitting formula: Equivalent hydraulic conductivity vs. fractal dimension (cubic polynomial). | [Xin 2019, pp. 44-45] | Core-scale models with D from 2.2 to 2.8. | Derived from calculated equivalent conductivity coefficients. |
| Factor influence on outlet temperature: Avg. aperture > Thermal expansion coeff. > Injection temp. | [Xin 2019, pp. 46-48] | Orthogonal test with 3 factors (injection temp, avg. aperture, thermal expansion coeff.) at 3 levels. | Based on range analysis of simulation results. |
| Interconnected fracture networks with higher bifurcation -> higher heat production & power generation. | [Xin 2019, pp. 61-66] | Field-scale dual horizontal well model with different fracturing schemes (e.g., Schemes 5,6 vs. others). | Evaluated over an 80-year simulation period. |
| Unconnected fracture networks -> advantage in energy efficiency. | [Xin 2019, pp. 66-67] | Field-scale model comparing connected (Schemes 4,5,6) and unconnected (Scheme 1) networks. | Energy efficiency based on heat production and power generation decreased over time. |
| More fractures & higher bifurcation -> higher local & overall heat recovery rates. | [Xin 2019, pp. 68-70] | Field-scale model comparing different fracturing schemes (e.g., Scheme 6 vs. Scheme 1). | Evaluated at t=80 a for local rate and over time for overall rate. |

## Limitations
1.  The study uses water as the working fluid and does not consider the chemical reactions between fluid and rock over long time scales [Xin 2019, pp. 72].
2.  The field-scale model does not account for heat replenishment from surrounding rock or the thermal reservoir recovery process after extraction [Xin 2019, pp. 72].
3.  The model assumes single-phase fluid saturation and that water does not vaporize under high-temperature reservoir conditions [Xin 2019, pp. 23].
4.  The initial in-situ stress field is not considered in the stress field analysis for both core and field scales [Xin 2019, pp. 37, 53].

## Assumptions / Conditions
The THM coupled model is based on the following key assumptions [Xin 2019, pp. 23]:
1.  In porous rock matrix, water temperature equals rock temperature; heat convection in pores is negligible.
2.  In fractures, heat exchange occurs via convection and conduction; heat transfer between fluid and rock follows Newton's law.
3.  The entire model is saturated with a single-phase fluid; flow in rock and fractures follows Darcy's law.
4.  Rock matrix is a continuous, compressible porous medium with permeability much lower than fractures.
5.  Fracture aperture varies with time and space, leading to different hydraulic conductivities.
6.  Rock matrix deformation follows the small strain assumption and is thermoelastic with thermal expansion.

## Key Variables / Parameters
- **Fractal Dimension (D):** Characterizes the irregularity of fracture surfaces (core scale) and fracture length distribution (field scale) [Xin 2019, pp. 13, 15].
- **Average Fracture Aperture:** A key factor influencing flow and heat transfer efficiency [Xin 2019, pp. 46].
- **Thermal Expansion Coefficient (α_T):** Governs rock deformation due to temperature changes, affecting fracture permeability [Xin 2019, pp. 46].
- **Injection Temperature:** Temperature of the cold working fluid injected into the reservoir [Xin 2019, pp. 45].
- **Fracture Density Parameter (C):** Describes the density of the fracture network in the field-scale model [Xin 2019, pp. 17].
- **Bifurcation Number:** Refers to the branching level of induced fractures in the horizontal well fracturing scheme [Xin 2019, pp. 60].
- **Equivalent Hydraulic Conductivity Coefficient:** A measure of the overall flow capacity of a rough fracture [Xin 2019, pp. 44].
- **Local Heat Recovery Rate (γ_L):** Ratio of heat absorbed by fluid to maximum extractable heat from rock at a point [Xin 2019, pp. 40-41].
- **Overall Heat Recovery Rate (γ):** Ratio of total extracted heat to total available heat in the reservoir at time t [Xin 2019, pp. 41].

## Reusable Claims
1.  **Claim:** The spectral synthesis method can generate realistic rough fracture surfaces whose irregularity is quantitatively controlled by the fractal dimension D.
    **Condition/Limitation:** Applicable to modeling single rock fractures at the core scale.
2.  **Claim:** In a THM-coupled EGS system, the average fracture aperture is the most influential factor on the outlet temperature of the working fluid, surpassing the effects of thermal expansion coefficient and injection temperature.
    **Condition/Limitation:** Based on orthogonal test analysis for a specific core-scale rough fracture model.
3.  **Claim:** For a dual horizontal well EGS, an interconnected fracture network with a higher bifurcation number enhances short-to-medium term heat production and power generation but may reduce the project's operational lifespan due to faster thermal breakthrough.
    **Condition/Limitation:** Derived from numerical simulations of idealized field-scale models over an 80-year period.
4.  **Claim:** Fracture networks that are not directly connected between injection and production wells demonstrate superior energy efficiency (ratio of produced energy to consumed pumping energy) over long-term operation.
    **Condition/Limitation:** Observed in comparative simulations of different fracturing schemes; may be related to reduced fluid losses.
5.  **Claim:** The heterogeneity of fluid flow velocity on a rough fracture surface increases with the fractal dimension D of the surface.
    **Condition/Limitation:** Concluded from fractal analysis of velocity distributions in core-scale numerical simulations.

## Candidate Concepts
- [[Enhanced Geothermal System (EGS)]]
- [[Thermo-Hydro-Mechanical (THM) Coupling]]
- [[Fractal Dimension]]
- [[Fracture Network]]
- [[Rough Fracture]]
- [[Heat Extraction Performance]]
- [[Spectral Synthesis Method]]
- [[Discrete Fracture Model]]
- [[Dual Horizontal Well]]

## Candidate Methods
- [[Spectral Synthesis Method]] for generating rough fracture surfaces.
- [[Finite Element Method]] for solving the THM coupled governing equations.
- [[Fractal Analysis]] for characterizing seepage and temperature field distributions.
- [[Orthogonal Test Design]] for multi-factor sensitivity analysis.
- [[Numerical Simulation]] using [[COMSOL Multiphysics]].

## Connections To Other Work
The study builds upon and references several key areas of prior research:
- **Global EGS Projects:** Reviews progress from projects like Fenton Hill (USA), Rosemanowes (UK), and Soultz (France) [Xin 2019, pp. 3-5].
- **Fractal Theory in Porous Media:** Cites foundational work by Mandelbrot and applications by Katz, Sahimi, and others on fractal characteristics of pores and fractures [Xin 2019, pp. 5-7].
- **Fractured Medium Models:** Discusses the evolution from dual-porosity models (Barenblatt) to discrete fracture models and discrete-continuum coupled models [Xin 2019, pp. 7-9].
- **EGS Coupling Models:** References prior THM coupling models developed by Noorishad, Zhao Yangsheng, Sun Zhixue, and others, as well as simulation software like TOUGH2 and COMSOL [Xin 2019, pp. 9-11].
- **Analytical Solutions:** Uses the analytical solution for heat extraction from a single fracture by Cheng et al. for model validation [Xin 2019, pp. 50-51].

## Open Questions
1.  How do long-term chemical reactions (THMC coupling) between the working fluid and rock matrix affect the fracture permeability and overall heat extraction efficiency?
2.  What is the optimal fracturing scheme (fracture number, spacing, bifurcation level) for a specific geological setting to balance high heat production, long project life, and high energy efficiency?
3.  How can the model be improved to account for heat replenishment from the surrounding rock mass and predict the thermal recovery time of the reservoir after cessation of extraction?
4.  How do different working fluids (e.g., supercritical CO2) perform compared to water under the same THM coupling conditions and fractal fracture characteristics?

## Source Coverage
All 18 non-empty indexed fragments were processed. The compiled source blocks total 18, with a compiled character count of 86,511 out of a total indexed character count of 89,170, resulting in a coverage ratio by characters of 0.970181. The coverage status is "full-index".
