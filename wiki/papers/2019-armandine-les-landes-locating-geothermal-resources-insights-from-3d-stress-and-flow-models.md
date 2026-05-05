---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-armandine-les-landes-locating-geothermal-resources-insights-from-3d-stress-and-flow-models"
title: "Locating Geothermal Resources: Insights from 3D Stress and Flow Models at the Upper Rhine Graben Scale."
status: "draft"
source_pdf: "data/papers/Locating Geothermal Resources Insights from 3D Stress and Flow Models at the Upper Rhine Graben Scale.pdf"
collections:
citation: "Armandine Les Landes, Antoine, et al. \"Locating Geothermal Resources: Insights from 3D Stress and Flow Models at the Upper Rhine Graben Scale.\" *Geofluids*, vol. 2019, 2019, pp. 1-24, doi:10.1155/2019/8494539. Accessed 12 May 2026."
indexed_texts: "25"
indexed_chars: "122080"
nonempty_source_blocks: "25"
compiled_source_blocks: "25"
compiled_source_chars: "122717"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.005218"
coverage_status: "full-index"
source_signature: "a66f07887498b53a2266526db9e0a041c0306743"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:31:26"
---

# Locating Geothermal Resources: Insights from 3D Stress and Flow Models at the Upper Rhine Graben Scale.

## One-line Summary
This study uses first-of-their-kind 3D numerical flow and stress models at the Upper Rhine Graben scale to identify geothermally favorable areas by cross-analyzing preferential fluid discharge zones and mechanically favorable stress states, with results correlating well with known thermal anomalies.

## Research Question
How can 3D numerical models of regional groundwater flow and crustal stress, explicitly incorporating a discrete fault network, be used to locate hidden geothermal resource anomalies in a fault-controlled geological setting like the Upper Rhine Graben?

## Study Area / Data
The study area is the Upper Rhine Graben (URG), an NNE-trending crustal-scale rift approximately 300 km long and 30-40 km wide, located between Frankfurt (Germany) and Basel (Switzerland) [Armandine 2019, pp. 3-4]. The case study focuses on a 130 × 150 km² area centered on the main thermal anomalies [Armandine 2019, pp. 4-5]. Data sources include the transnational geological model and seismic fault map from the GeORG project, borehole data, geological maps, digital terrain models, and a temperature map at 2 km depth [Armandine 2019, pp. 3-4, 4-5, 8-10].

## Methods
The methodology involves building a 3D Discrete Fracture Network (DFN) model representing the regional fault network, which is then used as the geometry for separate 3D flow and stress models [Armandine 2019, pp. 1-2, 3-4].
1.  **DFN Model Construction:** A DFN with 351 fault zones was generated using 3DEC™ software, integrating major structural features (e.g., Variscan faults, URG border faults) and secondary faults from the GeORG database and DTM analysis. Geometric simplifications were applied to meet software requirements [Armandine 2019, pp. 4-5, 5-6].
2.  **3D Flow Model:** Built using the 3FLO software (discrete-continuum method). The DFN is represented by 1D pipe elements, and sedimentary units are 3D tetrahedral elements. Hydraulic properties were assigned (e.g., fault transmissivity of 10⁻⁷ m²/s). Steady-state flow was simulated with topography-controlled boundary conditions. Particle tracking was used to simulate flow paths, and indicators (travel distance, time, depth reached) were used to identify preferential discharge areas of deep regional groundwater loops [Armandine 2019, pp. 5-6, 6-8, 8-8].
3.  **3D Stress Model:** Built using the 3DEC™ software (distinct element method). The rock matrix was modeled as elastic, and fault zones followed an elastoplastic Coulomb slip law with dilation. Boundary conditions were set based on the present-day tectonic context. The initial state was approximated with gravitational loading. The mean stress (σₘ) was used as the mechanical indicator, with low values (less compressed areas) considered favorable for fluid upwelling [Armandine 2019, pp. 10-11, 11-12].
4.  **Cross-Analysis:** Favorable areas from the flow and stress models were overlapped to delineate areas where both hydraulic and mechanical conditions favor geothermal resource setup [Armandine 2019, pp. 12-13].

## Key Findings
- The cross-analysis of the 3D flow and stress models delineated three main favorable areas for geothermal resources: one west of Speyer, one south of Soultz-sous-Forêts, and one south of Strasbourg [Armandine 2019, pp. 12-13].
- This north-south distribution of three areas is in good agreement with the distribution of the main local thermal anomalies known in the URG at a 2 km depth [Armandine 2019, pp. 12-13].
- The area south of Soultz-sous-Forêts was the best correlated by the model, combining favorable structural (horst with intersecting faults), hydraulic (preferential discharge area), and mechanical (less compressed region) conditions [Armandine 2019, pp. 13-15].
- The results demonstrate the key role of the regional fault network, stress, and fluid flow in the setup of geothermal resources and underline the potential of this cross-numerical approach for exploration [Armandine 2019, pp. 1-2, 17-18].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Cross-analysis of flow and stress models delineates three favorable areas (west of Speyer, south of Soultz-sous-Forêts, south of Strasbourg) that correlate with known thermal anomalies. | [Armandine 2019, pp. 12-13] | URG scale, using the constructed DFN, flow, and stress models. | Validates the approach; the southern Soultz area is the best match. |
| The major thermal anomaly near Soultz-sous-Forêts is best located by the model because it combines a structural horst, a hydraulic discharge area, and a mechanical low-stress zone. | [Armandine 2019, pp. 13-15] | Detailed analysis of the cross-analysis results for the Soultz area. | Highlights the integrated control of structure, flow, and stress. |
| Geochemical data suggest thermal anomalies result from regional circulation through deep faults, consistent with model flow paths showing particles traveling from the URG center to its borders. | [Armandine 2019, pp. 13-15] | Comparison of model flow paths with geochemical signatures from Sanjuan et al. [14]. | Supports the model's representation of deep regional circulation. |
| The DFN model is composed of 351 fault zones, built from seismic data, geological maps, and structural expertise, forming the basis for both physical models. | [Armandine 2019, pp. 4-5] | Construction for the 130x150 km² URG case study area. | A critical and challenging step for the entire approach. |
| Hydraulic criteria for the flow model include particle travel distance, time, and depth reached (>2.5 km), used to identify regional groundwater loops. | [Armandine 2019, pp. 8-8] | Particle tracking simulation and post-processing. | Indicators are proxies for the thermal signature of anomalies. |
| The mechanical indicator is mean stress (σₘ), with low values (less compressed areas) assumed to favor fluid discharge and upwelling. | [Armandine 2019, pp. 11-12] | Interpretation of the 3DEC stress model results. | A qualitative criterion based on the link between stress and flow. |

## Limitations
- The models rely on simplifying assumptions, such as uniform hydraulic properties for fault sets and simplified, extrapolated mechanical parameters [Armandine 2019, pp. 6-8, 10-11].
- The cross-analysis of favorable areas is qualitative, based on overlapping contours from separate models [Armandine 2019, pp. 16-17].
- The DFN geometry, while consistent with geological knowledge, involves simplifications (e.g., planar faults, priority rules) and could be improved with more detailed structural data [Armandine 2019, pp. 4-5, 16-17].
- The flow model assumes a topography-controlled water table and steady-state conditions [Armandine 2019, pp. 6-8].
- The choice of a single mechanical indicator (mean stress) is difficult and may not capture all relevant processes; other indicators like fault opening tendency were also tested [Armandine 2019, pp. 11-12, 17-17].

## Assumptions / Conditions
- Geothermal anomalies are primarily caused by long-term regional groundwater flow, which is the most efficient ubiquitous transport mechanism [Armandine 2019, pp. 8-8].
- The regional fault network significantly controls both stress redistribution and fluid circulation pathways [Armandine 2019, pp. 1-2, 15-16].
- The water table is topography-controlled, justified by the URG's humid region with subdued topography and low hydraulic conductivity [Armandine 2019, pp. 6-8].
- The rock matrix of the basement is considered impermeable, with flow occurring within faults [Armandine 2019, pp. 6-8].
- The present-day stress state is driven by the African-Eurasian plate convergence, resulting in a sinistral strike-slip regime [Armandine 2019, pp. 3-4].
- Large deformations are localized into fault zones (joints), not the rock matrix [Armandine 2019, pp. 10-11].

## Key Variables / Parameters
- **Fault Transmissivity:** 10⁻⁷ m²/s (uniform for all fault sets as a first approximation) [Armandine 2019, pp. 6-8].
- **Sedimentary Permeability:** Deep unit (Keuper, Muschelkalk, Buntsandstein): 4×10⁻¹⁴ m²; Shallow unit (Jurassic, Oligocene, etc.): 1×10⁻¹⁸ m² [Armandine 2019, pp. 6-8].
- **Mechanical Parameters (Rock Matrix):** Density (ρ), Bulk modulus (K), Shear modulus (G) for sediment and basement [Armandine 2019, pp. 10-11].
- **Mechanical Parameters (Fault Zones):** Normal stiffness (kₙ), Shear stiffness (kₛ), Cohesion (c₀), Internal friction angle (ϕ), Dilation angle (ψ), Critical shear displacement (uᶜₛ) [Armandine 2019, pp. 10-11].
- **Flow Model Indicators:** Particle travel distance, travel time, depth reached (>2.5 km) [Armandine 2019, pp. 8-8].
- **Stress Model Indicator:** Mean stress (σₘ = Tr(σ)/3) [Armandine 2019, pp. 11-12].

## Reusable Claims
- Cross-analyzing results from separate 3D flow and stress models, each built on a common discrete fault network, can effectively delineate areas favorable for geothermal resources in rift settings, as demonstrated by correlation with known thermal anomalies in the URG [Armandine 2019, pp. 12-13, 17-18].
- In fault-controlled geothermal systems, the intersection of hydraulically favorable (preferential discharge of deep regional flow) and mechanically favorable (low mean stress) zones is a strong indicator for the location of thermal anomalies [Armandine 2019, pp. 12-13, 13-15].
- The discrete numerical approach is necessary to capture the key role of the regional fault network in controlling both stress heterogeneity and localized fluid flow pathways at the geothermal system scale [Armandine 2019, pp. 1-2, 3-4].
- The geographical distribution of geothermal resources in the URG is strongly correlated with preferential discharge areas of deep regional fluid circulation occurring within the regional fault network and related to less compressed areas that favor upwellings [Armandine 2019, pp. 17-18].

## Candidate Concepts
- [[discrete fracture network]]
- [[particle tracking]]
- [[mean stress]]
- [[preferential discharge area]]
- [[regional groundwater flow]]
- [[thermal anomaly]]
- [[fault-controlled geothermal system]]
- [[Upper Rhine Graben]]
- [[geothermal exploration favorability]]

## Candidate Methods
- [[3D flow modeling]]
- [[3D stress modeling]]
- [[discrete-continuum method]]
- [[distinct element method]]
- [[cross-analysis of models]]
- [[geothermal criteria definition]]
- [[indicator-based interpretation]]

## Connections To Other Work
- The study builds upon the structural database from the GeORG project [Armandine 2019, pp. 2-2, 3-4].
- It references and compares with previous hydrothermal models of the URG (e.g., Le Carlier et al. [13], Clauser and Villinger [10]) but notes their limitations in scale and dimensionality [Armandine 2019, pp. 2-3].
- The interpretation of flow paths is consistent with geochemical studies by Sanjuan et al. [14] on brine circulation [Armandine 2019, pp. 13-15].
- The mechanical model setup and boundary conditions follow the approach of Buchmann and Connolly [62] [Armandine 2019, pp. 10-11].
- The work acknowledges the broader context of studies linking stresses to flow properties and thermal anomalies (e.g., references [6, 22-24]) [Armandine 2019, pp. 2-2].

## Open Questions
- Is it essential to explicitly include thermal physical processes (e.g., conductive/convective heat transfer) in the models to better locate thermal anomalies, or is the cross-analysis of stress and flow sufficient for exploration targeting? [Armandine 2019, pp. 15-16].
- How can the models be improved through one-way or full coupling, and is this feasible at the regional scale with the current computational tools? [Armandine 2019, pp. 15-16].
- How should mechanical results be best interpreted—through a straightforward indicator like mean stress, or to parameterize the flow model (e.g., via permeability changes)? [Armandine 2019, pp. 17-17].
- How can the DFN geometry be further refined by integrating deeper seismic data and more detailed tectonic evolution models? [Armandine 2019, pp. 16-17].

## Source Coverage
All 25 non-empty indexed fragments were processed, comprising 122,080 characters. The compiled source blocks total 25, with 122,717 characters, resulting in a coverage ratio of 1.0 by block count and 1.005 by character count. The source signature is `a66f07887498b53a2266526db9e0a041c0306743`.
