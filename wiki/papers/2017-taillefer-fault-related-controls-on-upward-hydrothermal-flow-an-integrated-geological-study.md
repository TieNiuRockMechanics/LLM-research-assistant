---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2017-taillefer-fault-related-controls-on-upward-hydrothermal-flow-an-integrated-geological-study"
title: "Fault-Related Controls on Upward Hydrothermal Flow: An Integrated Geological Study of the Têt Fault System, Eastern Pyrénées (France)."
status: "draft"
source_pdf: "data/papers/Fault-Related Controls on Upward Hydrothermal Flow An Integrated Geological Study of the Tet Fault System, Eastern Pyrenees (France).pdf"
collections:
citation: "Taillefer, Audrey, et al. “Fault-Related Controls on Upward Hydrothermal Flow: An Integrated Geological Study of the Têt Fault System, Eastern Pyrénées (France).” *Geofluids*, vol. 2017, 2017, pp. 1–19, doi:10.1155/2017/8190109."
indexed_texts: "18"
indexed_chars: "88814"
nonempty_source_blocks: "18"
compiled_source_blocks: "18"
compiled_source_chars: "89265"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.005078"
coverage_status: "full-index"
source_signature: "3ad321cff797929c6c48596a271207ebf03d0e35"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T00:06:18"
---

# Fault-Related Controls on Upward Hydrothermal Flow: An Integrated Geological Study of the Têt Fault System, Eastern Pyrénées (France).

## One-line Summary
An integrated geological study of the Têt fault system reveals that upward hydrothermal flow and hot spring emergence are controlled by fault-related lithological contacts, damage zone fracturing, and footwall topography.

## Research Question
How do faults control upward fluid flow in nonmagmatic hydrothermal systems in an extensional context? [Taillefer 2017, pp. 1-2]

## Study Area / Data
The study focuses on the crustal-scale, 100 km long Têt normal fault in the Eastern Pyrénées, France, which hosts an alignment of 29 hot springs (29°C to 73°C). [Taillefer 2017, pp. 1-2] Data sources include geological maps, SPOT satellite images (5 m resolution), aerial pictures (5 m resolution), a digital elevation model (USGS, 30 m resolution), field observations of springs (location, temperature, pH, conductivity), and microscopic/XRD analyses of fault rocks and sinters. [Taillefer 2017, pp. 3-5]

## Methods
1.  **Combined Mapping Method:** Integration of geologic maps, remote sensing (SPOT, aerial photos), and DEM interpretation using QGIS to map faults, lithologies, and spring locations. [Taillefer 2017, pp. 3-5]
2.  **Numerical Modeling:** A 2D model using COMSOL Multiphysics software coupling Darcy's law and the heat transfer equation to simulate hydrothermal circulation. The model was benchmarked against the Dixie Valley system. [Taillefer 2017, pp. 3-5, 12-13]

## Key Findings
1.  Hot springs consistently emerge in crystalline rocks (gneiss, granite) at contacts with metasediments, predominantly within the Têt fault footwall. [Taillefer 2017, pp. 8-10]
2.  The distribution and temperature of hot springs correlate with the height of the fault scarp relief and the surface area of high elevation in the footwall, which control hydraulic gradient and recharge volume. [Taillefer 2017, pp. 10-10]
3.  Emergence localizes at two types of structural settings: (1) in brittle fault damage zones, especially at intersections between the Têt fault and subsidiary faults, and (2) along ductile faults (e.g., the CMNC) where dissolution cavities form along foliations. [Taillefer 2017, pp. 8-10, 14-15]
4.  Numerical models show that permeable damage zones (K=10⁻¹⁴ m²) surrounding a less permeable core (K=10⁻¹⁸ m²) focus fluid upflow, causing isotherm uplift and surface temperatures of 30-50°C without an anomalous heat source. [Taillefer 2017, pp. 12-14]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 29 hot springs (29-73°C) align along the Têt fault, mostly in the footwall. | [Taillefer 2017, pp. 1-2, 5-6] | Map-scale analysis of spring locations relative to fault trace. | Only 3 springs are in the hanging wall (at Canaveilles). |
| Springs emerge in crystalline rocks at gneiss-metasediment contacts (18-21/29 springs). | [Taillefer 2017, pp. 8-10] | Field observation of lithological contacts at spring sites. | Contacts can be unfaulted or faulted (brittle or ductile). |
| Hot spring number and temperature maxima correspond to the largest fault scarp relief and widest high-elevation surfaces. | [Taillefer 2017, pp. 10-10] | Topographic profile analysis along the fault. | The Carança Range (highest relief) hosts the hottest springs (Thues-les-Bains). |
| Dissolution cavities are observed along mylonitic foliation in ductile faults (CMNC) at Vernet-les-Bains. | [Taillefer 2017, pp. 12-13] | Outcrop and thin-section analysis. | Cavities are aligned with foliation and surrounded by hydrothermal harmotome sinter. |
| Numerical model shows fluid velocities peak (1.6×10⁻⁷ m/s) in damage zones, with isotherms rising ~1900 m. | [Taillefer 2017, pp. 12-14] | 2D model with Kg=10⁻¹⁶ m², Kc=10⁻¹⁸ m², Kd=10⁻¹⁴ m². | Steady state reached after ~40,000 years, matching estimated residence times. |

## Limitations
1.  Simplified 1D hydrological models (e.g., Velard, 1979) treat the fault as a single fracture and do not account for system complexity. [Taillefer 2017, pp. 3-5]
2.  Geothermometer estimates (suggesting >100°C at depth) may be unreliable for siliceous rocks. [Taillefer 2017, pp. 3-5]
3.  The numerical model is 2D and uses simplified geometry; absolute temperature values depend on assigned permeabilities. [Taillefer 2017, pp. 13-14]

## Assumptions / Conditions
1.  Hydrothermal fluids circulate exclusively in crystalline rocks (gneiss and granite). [Taillefer 2017, pp. 3-5, 15-16]
2.  The geothermal gradient is assumed to be 30°C/km. [Taillefer 2017, pp. 12-13]
3.  Metasediments act as impermeable barriers to fluid flow. [Taillefer 2017, pp. 15-16]
4.  The hydrothermal system is nonmagmatic; warming is due to the normal crustal geothermal gradient. [Taillefer 2017, pp. 1-2, 13-14]

## Key Variables / Parameters
-   **Fault Zone Permeability:** Core zone (Kc ~10⁻¹⁸ m²), Damage zone (Kd ~10⁻¹⁴ m²). [Taillefer 2017, pp. 12-13]
-   **Host Rock Permeability:** Gneiss (Kg ~10⁻¹⁶ m²). [Taillefer 2017, pp. 12-13]
-   **Topographic Gradient:** Hydraulic gradient driven by fault scarp relief (up to 1650 m in model). [Taillefer 2017, pp. 12-13]
-   **Fluid Temperature:** Surface emergence temperatures (29-73°C); estimated reservoir temperatures >100°C. [Taillefer 2017, pp. 3-5, 5-6]
-   **Fault Architecture:** Segmentation, damage zone thickness, core zone composition (cataclasite). [Taillefer 2017, pp. 10-12]

## Reusable Claims
1.  In nonmagmatic hydrothermal systems, the intensity of hydrothermal activity (spring number and temperature) is controlled by the height of the fault scarp relief and the surface area of high-elevation recharge zones. [Taillefer 2017, pp. 10-10, 14-15]
2.  Hot spring emergence in basement rocks preferentially occurs at contacts between permeable crystalline rocks and impermeable metasediments, which act as flow barriers. [Taillefer 2017, pp. 8-10, 15-16]
3.  Intersections between a main normal fault and subsidiary faults create highly connected fracture networks in damage zones that serve as efficient conduits for focused hydrothermal upflow. [Taillefer 2017, pp. 14-15]
4.  Ductile shear zones (mylonites) can provide significant permeability for hydrothermal fluids through foliation-parallel dissolution cavities, enabling fluid pathways distinct from brittle fault damage zones. [Taillefer 2017, pp. 12-13, 15-16]

## Candidate Concepts
- [[fault zone architecture]]
- [[hydrothermal system]]
- [[fracture reservoir]]
- [[lithological juxtaposition]]
- [[hydraulic gradient]]
- [[buoyancy-driven flow]]
- [[damage zone permeability]]
- [[cataclastic core zone]]

## Candidate Methods
- [[integrated geological mapping]]
- [[numerical modeling of coupled fluid and heat flow]]
- [[remote sensing interpretation]]
- [[microstructural analysis]]
- [[topographic profile analysis]]

## Connections To Other Work
-   The study's numerical approach builds on and benchmarks against models of the Dixie Valley geothermal system (McKenna and Blackwell, 2004). [Taillefer 2017, pp. 3-5, 12-13]
-   It addresses a gap in studying nonmagmatic hydrothermal systems in extensional contexts with high relief, which are rarely studied compared to magmatic or rift systems. [Taillefer 2017, pp. 1-2]
-   Findings on fault damage zone permeability align with conceptual models from other fault hydrogeology studies (e.g., Caine et al., 1996; Bense et al., 2013). [Taillefer 2017, pp. 14-15]

## Open Questions
1.  What is the primary factor controlling fluid pathways: brittle fault architecture or lithological contacts? The study suggests both are important but prioritizes lithology. [Taillefer 2017, pp. 15-16]
2.  Is there a single hydrothermal reservoir feeding all springs, or are there separate reservoirs compartmentalized by fault segmentation (e.g., beneath the Canigou vs. Carança ranges)? [Taillefer 2017, pp. 14-15]
3.  How does the time-dependent interplay between hydrothermal sealing (by mineralization) and stress-driven fracture opening affect long-term permeability and flow? [Taillefer 2017, pp. 15-16]

## Source Coverage
All non-empty indexed fragments were processed. The compilation includes 18 source blocks containing 88,814 characters, achieving a coverage ratio of 1.0 by blocks and 1.005 by characters. The source signature is `3ad321cff797929c6c48596a271207ebf03d0e35`.
