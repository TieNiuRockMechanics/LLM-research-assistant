---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2016-zhao-thermal-influence-on-mechanical-properties-of-granite-a-microcracking-perspective"
title: "Thermal Influence on Mechanical Properties of Granite: A Microcracking Perspective."
status: "draft"
source_pdf: "data/papers/Thermal Influence on Mechanical Properties of Granite-A Microcracking Perspective.pdf"
collections:
citation: "Zhao, Zhihong. \"Thermal Influence on Mechanical Properties of Granite: A Microcracking Perspective.\" *Rock Mechanics and Rock Engineering*, vol. 49, 2016, pp. 747–62. DOI: 10.1007/s00603-015-0767-1."
indexed_texts: "12"
indexed_chars: "57459"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "57540"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.00141"
coverage_status: "full-index"
source_signature: "b5b7d39385b83a85be42c0bce6ab52f36bef8764"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:59:35"
---

# Thermal Influence on Mechanical Properties of Granite: A Microcracking Perspective.

## One-line Summary
This study uses the particle mechanics method to simulate thermally induced microcracking in granite, elucidating how temperature-dependent mechanical properties are governed by the development of tensile microcracks and thermal stresses.

## Research Question
How do heating and heating-cooling cycles influence the macroscopic mechanical properties of granite, and what are the underlying microcracking mechanisms responsible for these changes?

## Study Area / Data
The study focuses on Lac du Bonnet granite, a uniform granite consisting of 31% quartz, 27% potassium feldspar, 38% plagioclase, and 4% mica [Zhao 2016, pp. 4-6]. Numerical specimens were created using a 2D particle flow code (PFC2D) with 15,000 particles for small-scale tests and 10,000 particles for thermal gradient tests [Zhao 2016, pp. 4-6, 8-11].

## Methods
The particle mechanics method (PFC2D) was used to model the granite as a heterogeneous assembly of cemented, deformable disks [Zhao 2016, pp. 2-3]. Transient heat conduction was simulated via a network of heat reservoirs and thermal pipes [Zhao 2016, pp. 3-4]. Thermal strain was incorporated by modifying disk radii and bond forces based on temperature changes and mineral-specific thermal expansion coefficients [Zhao 2016, pp. 3-4]. Two thermal scenarios were simulated: continuous heating from 20°C to peak temperatures (100–400°C) and heating-cooling cycles back to 20°C [Zhao 2016, pp. 4-6]. Mechanical tests (uniaxial compression and direct tension) were performed on the numerically heated specimens [Zhao 2016, pp. 6-7]. A separate model with a central borehole was used to study thermal gradient cracking under different boundary conditions (free, partially fixed, fully fixed) [Zhao 2016, pp. 8-11].

## Key Findings
- Heating generally reduces the compressive and tensile strengths of granite due to two primary mechanisms: increasing thermal stresses and the generation of tensile microcracks [Zhao 2016, pp. 1-2, 13-14].
- After a heating-cooling cycle, mechanical properties are reduced solely because of the increased density of thermally induced tensile microcracks, as significant thermal stresses are released during cooling [Zhao 2016, pp. 7-8, 13-14].
- Thermally induced microcracks predominantly occur at the interfaces between different mineral grains (intergranular) and are mainly tensile in nature [Zhao 2016, pp. 6-7, 8-11].
- A thermal gradient induces macrocracks that propagate from relatively cool to relatively warm regions [Zhao 2016, pp. 1-2, 11-13].
- Boundary conditions affect the development of microcracks and the initiation of macrocracks; confinement can prevent macrocrack formation [Zhao 2016, pp. 11-13, 13-14].
- The failure mode of granite under uniaxial compression shifts from brittle ('X'-shaped) at lower temperatures (≤200°C) to more ductile (fracture network) at higher temperatures (≥300°C) [Zhao 2016, pp. 6-7].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Elastic modulus and compressive strength decrease with increasing temperature during continuous heating. | [Zhao 2016, pp. 6-7] | Lac du Bonnet granite, 20–400°C, uniaxial compression. | E.g., compressive strength dropped from 153 MPa at 20°C to 94 MPa at 400°C (plane strain). |
| Tensile strength decreases significantly with increasing temperature during continuous heating. | [Zhao 2016, pp. 6-7] | Lac du Bonnet granite, 20–400°C, direct tension. | Dropped from 40 MPa at 20°C to 12 MPa at 400°C. |
| After a heating-cooling cycle, the reduction in strength is smaller than during continuous heating. | [Zhao 2016, pp. 7-8] | Lac du Bonnet granite, peak temperatures 100–400°C. | E.g., compressive strength after 400°C cycle was 139 MPa vs. 94 MPa during continuous heating. |
| Microcracks initiate at ~200°C and increase with temperature; >60% are intergranular. | [Zhao 2016, pp. 6-7] | Lac du Bonnet granite, continuous heating. | Parallel bonds mainly failed in tension. |
| Macrocracks from a thermal gradient propagate from cool to warm regions. | [Zhao 2016, pp. 11-13] | Square specimen with central borehole, heating/cooling. | Critical temperature for macrocrack initiation depended on boundary conditions. |
| Fully fixed boundaries can prevent macrocrack development under thermal gradients. | [Zhao 2016, pp. 11-13] | Square specimen with central borehole, heating to 400°C. | Shear microcracks were generated but no macrocracks formed. |

## Limitations
- The model assumes dry rock specimens; pore pressure effects are not considered [Zhao 2016, pp. 14-15].
- Temperatures above 500°C, which may cause mineral decomposition or phase transitions, were not modeled [Zhao 2016, pp. 4-6].
- The study assumes uniform elastic/strength properties for inter-grain and intra-grain bonds, though a sensitivity analysis was performed [Zhao 2016, pp. 13-14].
- The model does not account for temperature-dependent changes in microparameters (e.g., bond strength) [Zhao 2016, pp. 14-15].
- The analysis is 2D, which may not fully capture 3D fracture processes [Zhao 2016, pp. 2-3].

## Assumptions / Conditions
- The mechanical effect occurs instantaneously compared to thermal conduction [Zhao 2016, pp. 3-4].
- The granite is homogeneous in texture and composition at the specimen scale [Zhao 2016, pp. 4-6].
- Thermal expansion coefficients are constant for each mineral type [Zhao 2016, pp. 4-6].
- The study focuses on intact rock; pre-existing fractures are not considered [Zhao 2016, pp. 14-15].
- The maximum peak temperature is limited to 400°C to avoid complex chemical reactions [Zhao 2016, pp. 4-6].

## Key Variables / Parameters
- Temperature (peak temperature, thermal gradient)
- Microcrack density (number and type: tensile/shear, intergranular/intragranular)
- Mechanical properties (elastic modulus, Poisson's ratio, compressive strength, tensile strength)
- Boundary conditions (free, partially fixed, fully fixed)
- Mineral composition and their thermal expansion coefficients
- Thermal conductivity and specific heat

## Reusable Claims
- Heating granite reduces its compressive and tensile strengths primarily due to the development of significant thermal stresses, with tensile microcracking acting as a secondary contributor [Zhao 2016, pp. 7-8, 13-14].
- The strength reduction in granite after a heating-cooling cycle is less severe than during continuous heating because thermal stresses are released upon cooling, leaving microcrack density as the main cause of degradation [Zhao 2016, pp. 7-8, 13-14].
- Thermally induced microcracks in granite predominantly form at mineral grain boundaries (intergranular) and are tensile in nature [Zhao 2016, pp. 6-7, 8-11].
- Under a thermal gradient, macrocracks in granite nucleate and propagate from cooler regions toward warmer regions [Zhao 2016, pp. 11-13].
- Confinement (fixed boundary conditions) can suppress the formation of macrocracks induced by thermal gradients in granite [Zhao 2016, pp. 11-13, 13-14].

## Candidate Concepts
- [[Thermal cracking]]
- [[Microcrack]]
- [[Thermal stress]]
- [[Heating-cooling cycle]]
- [[Thermal gradient]]
- [[Intergranular microcrack]]
- [[Intragranular microcrack]]
- [[Brittle-ductile transition]]
- [[Boundary condition]]

## Candidate Methods
- [[Particle mechanics method]]
- [[PFC2D]]
- [[Bonded-particle model]]
- [[Numerical simulation of thermal-mechanical coupling]]
- [[Uniaxial compression test]]
- [[Direct tension test]]

## Connections To Other Work
- The study compares its numerical results with experimental data from various rocks summarized in Table 1 [Zhao 2016, pp. 2-3].
- It builds upon the particle mechanics modeling framework for Lac du Bonnet granite established by Potyondy and Cundall (2004) and others [Zhao 2016, pp. 2-3, 4-6].
- The thermal gradient cracking simulation replicates and extends the experimental setup of Jansen et al. (1993) [Zhao 2016, pp. 8-11].
- Findings on the role of thermal stress versus microcracking are discussed in relation to Wang et al. (2013) [Zhao 2016, pp. 7-8].
- The influence of boundary conditions is compared to in-situ observations by Andersson et al. (2009) [Zhao 2016, pp. 13-14].

## Open Questions
- How do coupled thermal-hydro-mechanical (THM) processes, including pore pressure and fluid chemistry, affect the thermal cracking and mechanical behavior of granite?
- How do temperature-dependent changes in microparameters (e.g., bond strength, elastic modulus) influence the simulation results, especially for rocks showing non-monotonic property changes?
- What is the effect of the rate of heating or cooling on thermal stress development and microcracking?
- How do pre-existing fractures interact with thermally induced microcracks to affect the overall mechanical and transport properties of rock masses?

## Source Coverage
All 12 non-empty indexed fragments were processed. The compiled source blocks total 12, with a compiled character count of 57,540, achieving a coverage ratio of 1.0 by blocks and 1.00141 by characters. The coverage status is full-index.
