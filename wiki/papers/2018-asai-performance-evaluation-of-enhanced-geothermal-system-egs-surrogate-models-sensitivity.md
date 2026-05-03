---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2018-asai-performance-evaluation-of-enhanced-geothermal-system-egs-surrogate-models-sensitivity"
title: "Performance Evaluation of Enhanced Geothermal System (EGS): Surrogate Models, Sensitivity Study and Ranking Key Parameters."
status: "draft"
source_pdf: "data/papers/2018 - Performance evaluation of enhanced geothermal system (EGS) Surrogate models, sensitivity study and ranking key parameters.pdf"
collections:
citation: "Asai, Pranay, et al. \"Performance Evaluation of Enhanced Geothermal System (EGS): Surrogate Models, Sensitivity Study and Ranking Key Parameters.\" *Renewable Energy*, vol. 122, 2018, pp. 184-95, doi:10.1016/j.renene.2018.01.098."
indexed_texts: "12"
indexed_chars: "55773"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "55829"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.001004"
coverage_status: "full-index"
source_signature: "4161389531d98db2099d8d547aa4b860d3f8ef75"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T21:01:21"
---

# Performance Evaluation of Enhanced Geothermal System (EGS): Surrogate Models, Sensitivity Study and Ranking Key Parameters.

## One-line Summary
This study develops second-order surrogate models based on Box-Behnken design to evaluate the sensitivity and rank the impacts of five key parameters (well spacing, fracture spacing, well inclination, injection temperature, and injection rate) on heat extraction performance in a doublet Enhanced Geothermal System (EGS) over 30 years, using in-situ properties from the Utah FORGE site. [Asai 2018, pp. 1-2]

## Research Question
The research aims to determine the individual and combined effects of five key parameters on the efficiency of a doublet EGS and to establish a hierarchy of these factors based on their impact on total heat extraction over a 30-year project lifetime. It seeks to answer how completion parameters (well spacing, fracture spacing, well inclination) and operational parameters (injection temperature, injection rate) influence produced water temperature and cumulative heat recovery. [Asai 2018, pp. 2-2]

## Study Area / Data
The in-situ natural properties for the simulations are derived from the U.S. Department of Energy’s Frontier Observatory for Research in Geothermal Energy (FORGE) site near Milford, Utah. [Asai 2018, pp. 3-4]
- **Reservoir Rock:** Granodiorite with low porosity (~1% or less) and low permeability (on the order of 5–30 microdarcies). [Asai 2018, pp. 3-4]
- **Temperature Gradient:** Nominal gradient of 60 °C/km, with a reference temperature of 200 °C at a true vertical depth (TVD) of 2500 m. [Asai 2018, pp. 3-4]
- **Planned Well Configuration:** An injection well and a production well, both inclined at 60° from the vertical, with a perpendicular spacing of ~200 m. [Asai 2018, pp. 3-4]
- **Natural Fractures:** Natural fractures exist, but temperature gradients indicate a conductive rather than convective geothermal reservoir. [Asai 2018, pp. 3-4]
- **Simulated Reservoir Dimensions:** Model dimensions include a reservoir length of 900 m and width of 500 m. Fracture width is 0.01 m. [Asai 2018, pp. 4-5]

## Methods
The study employs a four-step workflow: (1) Parameter Selection – Five key variables (well spacing, fracture spacing, well inclination, injection temperature, total injection rate) are chosen, categorized as either completion or operational parameters, with natural properties fixed from the FORGE site. [Asai 2018, pp. 4-5] (2) Experimental Design – A **[[Box-Behnken design]]** (a three-level method) is used to minimize the number of required numerical simulations, generating 41 training cases. An additional 10 randomly generated test cases (within the input ranges) are created for validation. [Asai 2018, pp. 5-5] (3) Simulation – Simulations are run using the commercial thermal reservoir simulator **[[STARS (CMG)]]**. The model assumes a doublet system with water as the working fluid and vertical, rectangular, isotropic hydraulic fractures with high conductivity. [Asai 2018, pp. 3-4] (4) Surrogate Model Development – Second-order polynomial surrogate models are trained on the simulation results to predict the logarithm of produced water temperature at 59 discrete time points over 30 years. Model fitness is evaluated using the coefficient of determination (R²) and Normalized Root Mean Square Error (NRMSE). [Asai 2018, pp. 4-5]

## Key Findings
- **Parameter Hierarchy:** The sensitivity analysis reveals a clear, time-dependent ranking. Over a 30-year period, well spacing is the most dominant factor, followed by injection temperature, total injection rate, fracture spacing, and well inclination angle (least impact). [Asai 2018, pp. 9-10]
- **Well Spacing:** Well spacing is directly proportional to total heat output. A system with 300 m well spacing extracts almost three times more heat over 30 years than one with 100 m spacing. This is because larger spacing encompasses a greater reservoir volume and heat content. [Asai 2018, pp. 5-7]
- **Injection Temperature:** Lower injection temperature (e.g., 80 °C) results in higher total heat extraction over 30 years by increasing the temperature gradient and initial heat transfer rate, though it causes a more rapid temperature decline. [Asai 2018, pp. 5-7][Asai 2018, pp. 7-9]
- **Injection Rate:** Higher injection flow rate is directly proportional to heat extraction rate. A higher flow rate depletes the reservoir faster, extracting more heat even though the fluid residence time is reduced and produced water temperature may be lower. [Asai 2018, pp. 7-9]
- **Fracture Spacing:** Smaller fracture spacing (i.e., more fractures) increases the surface area for heat transfer, leading to higher heat recovery. However, interference can occur if spacing drops below a certain threshold. [Asai 2018, pp. 5-7]
- **Well Inclination:** Horizontal wells (90° to vertical) perform better than inclined wells (e.g., 45°). This is because all fractures in a horizontal system lie in a higher average temperature zone, whereas inclined well systems place some fractures in cooler zones. [Asai 2018, pp. 5-7]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| Well spacing is the most crucial parameter for total heat output over 30 years. | [Asai 2018, pp. 9-10] | Doublet well system; FORGE site properties; other parameters at medium values. | Well spacing directly affects the primary heat recovery factor (encompassed reservoir volume). |
| For 300m well spacing, total heat extracted is almost three times that for 100m spacing over 30 years. | [Asai 2018, pp. 5-7] | Doublet well system; fracture spacing, well inclination, injection temperature, and rate held at medium values. | Temperature produced with 300m spacing remains above 150°C. |
| A lower injection temperature (80°C) extracts more cumulative heat over 30 years than a higher temperature (120°C). | [Asai 2018, pp. 7-9] | Doublet well system; other parameters at medium values. | Lower injection temperature increases the temperature difference, which is the driving factor for heat exchange and rate of extraction. |
| Injection flow rate is directly proportional to the rate of heat extraction. | [Asai 2018, pp. 7-9] | Doublet well system; assuming constant heat content. | High rates deplete the reservoir faster due to greater volume of fluid available to carry heat, despite lower produced water temperature. |
| Smaller fracture spacing (more fractures) provides more area for heat transfer and increases heat recovery. | [Asai 2018, pp. 5-7] | Fixed well length; other parameters constant. | Interference between fractures can occur if spacing is too small. |
| Horizontal wells (90°) extract more heat than inclined wells (45°) over 30 years. | [Asai 2018, pp. 5-7] | First fracture location fixed at toe of well; other parameters constant. | Horizontal wells place all fractures in a zone with a higher average reservoir temperature. |
| The hierarchy of factors changes over time; flow rate and injection temperature dominate in the first year, but well spacing becomes dominant later. | [Asai 2018, pp. 9-10] | Doublet system with parameters from FORGE site. | Early-time dominance is due to lack of interference; later-time dominance shifts to volume-related parameters. |

## Limitations
- The study only evaluates a single doublet well configuration. [Asai 2018, pp. 1-2]
- Hydraulic fractures are modeled as simple, planar, uniform, and isotropic with constant conductivity. [Asai 2018, pp. 3-4]
- The analysis uses a specific set of in-situ properties from the Utah FORGE site; results may not be directly transferable to other reservoirs with different natural parameters. [Asai 2018, pp. 3-4]
- The well inclination angle transformation used a reciprocal to achieve linearity (+1, 0, -1), as the actual angles (45°, 60°, 90°) are not linearly spaced. [Asai 2018, pp. 5-5]
- Temperature decline curves of different natures (e.g., sharp early decline vs. slow increase then decline) can cause a peak in surrogate model error (NRMSE) for some time steps. [Asai 2018, pp. 4-5]

## Assumptions / Conditions
- The EGS operates as a closed-loop system with a make-up water line. [Asai 2018, pp. 2-3]
- Water is maintained as a pressurized liquid to avoid flashing and condensation. [Asai 2018, pp. 2-3]
- All simulated hydraulic fractures are uniform, isotropic, and have the same fracture conductivity. [Asai 2018, pp. 3-4]
- For sensitivity analysis, while studying the effect of one factor, all other factors are kept at their medium values. [Asai 2018, pp. 5-7]
- The temperature of produced water is calculated by interpolation between the discrete time points of the 59 surrogate models. [Asai 2018, pp. 4-5]

## Key Variables / Parameters
- **[[Well spacing]]** (100–300 m): A completion parameter.
- **[[Fracture spacing]]** (50–100 m): A completion parameter.
- **[[Well inclination angle]]** (45°–90° from vertical): A completion parameter, transformed as reciprocal of angle for the experimental design.
- **[[Injection temperature]]** (80–120 °C): An operational parameter.
- **[[Total injection rate]]** (5000–10000 m³/day): An operational parameter.
- **[[Produced water temperature]]**: The primary response variable modeled by surrogates.
- **[[Total heat extraction]] (H)**: Calculated via integration: H = ∫₀ᵗ Q ρ cₚ (Tₚ − Tᵢₙⱼ) dt.

## Reusable Claims
1.  Over the lifetime of a doublet EGS, **[[well spacing]]** becomes the most critical parameter controlling total heat extraction, because it determines the volume of reservoir rock accessed. [Asai 2018, pp. 5-7]
2.  **Operational parameters** (injection temperature and rate) primarily control the *rate* of heat extraction and can be used to manage thermal depletion rate after the heat recovery factor is fixed by completion parameters. [Asai 2018, pp. 2-3][Asai 2018, pp. 7-9]
3.  A **[[Box-Behnken design]]** is an effective method to minimize the number of simulations required to train a second-order polynomial surrogate model for EGS performance evaluation. [Asai 2018, pp. 5-5]
4.  A lower injection fluid temperature increases long-term total heat extraction in an EGS by increasing the temperature difference driving heat transfer, despite causing a more rapid thermal decline of the reservoir. [Asai 2018, pp. 7-9]
5.  The importance ranking of EGS parameters is time-dependent: injection flow rate dominates in the near-term before well/frac interactions occur, while well spacing dominates in the long-term. [Asai 2018, pp. 9-10]

## Candidate Concepts
- [[surrogate model]]
- [[Box-Behnken design]]
- [[enhanced geothermal system]]
- [[doublet well system]]
- [[fracture reservoir]]
- [[heat recovery factor]]
- [[parameter sensitivity hierarchy]]
- [[thermal depletion]]
- [[reservoir interference]]
- [[FORGE site]]

## Candidate Methods
- [[Box-Behnken experimental design]]
- [[second-order polynomial surrogate model]]
- [[STARS (CMG) thermal reservoir simulation]]
- [[Normalized Root Mean Square Error (NRMSE)]]
- [[Coefficient of determination (R-squared)]]
- [[tornado plot for sensitivity analysis]]
- [[cumulative heat extraction integration]]

## Connections To Other Work
- **Fracture Studies:** Sun et al. (2017) studied the effect of different fracture geometries on heat extraction, while Guo et al. (2016) investigated aperture heterogeneity in a single fracture. [Asai 2018, pp. 2-2]
- **Well Configurations:** Sanyal and Butler (2005) studied a five-spot layout, and Frash et al. (2015) evaluated doublet and triplet systems. Jiang et al. (2014) concluded a triplet layout elongates lifespan by 10 years over a doublet, which contrasts with the doublet focus of this study. [Asai 2018, pp. 1-2][Asai 2018, pp. 2-2]
- **Sensitivity and Optimization:** Xia et al. (2017) performed sensitivity on fracture spacing, well deviation, and flow rates. Ekneligoda and Min (2014) studied optimization of parameters for a horizontally fractured reservoir. [Asai 2018, pp. 2-2]
- **Parameter Studies:** Chen and Jiang (2015, 2016) studied multi-well layouts and showed flow pattern is dominant for heat extraction, and Zeng et al. (2013) found energy efficiency is a function of permeability and flow rate. [Asai 2018, pp. 2-2]

## Open Questions
- How does the hierarchy of parameters change for other well configurations, such as triplet or five-spot systems, which was not evaluated here? not confirmed, inferred from study scope in [Asai 2018, pp. 1-2]
- What is the precise threshold for fracture spacing below which thermal interference between fractures begins to negatively impact overall performance? not confirmed, based on qualitative statement in [Asai 2018, pp. 5-7]
- How do these parameter rankings change if the natural reservoir properties (e.g., much higher matrix permeability or convective regime) differ significantly from the Utah FORGE site’s conductive, low-permeability granodiorite? (not confirmed)

## Source Coverage
All 12 non-empty indexed fragments from the source paper (Asai et al., 2018) were processed to compile this page. The coverage ratio by blocks is 1.0, and by characters is 1.001, confirming full utilization of the provided indexed evidence.
