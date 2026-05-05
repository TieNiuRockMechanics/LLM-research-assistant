---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2013-kim-effect-of-rapid-thermal-cooling-on-mechanical-rock-properties"
title: "Effect of Rapid Thermal Cooling on Mechanical Rock Properties."
status: "draft"
source_pdf: "data/papers/Effect of Rapid Thermal Cooling on Mechanical Rock Properties.pdf"
collections:
citation: "Kim, Kwangmin, et al. \"Effect of Rapid Thermal Cooling on Mechanical Rock Properties.\" *Rock Mechanics and Rock Engineering*, 2013, doi:10.1007/s00603-013-0523-3."
indexed_texts: "11"
indexed_chars: "51860"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "52067"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.003992"
coverage_status: "full-index"
source_signature: "671f243da62eede6c79dc5ad97856347e73d4e7a"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:40:38"
---

# Effect of Rapid Thermal Cooling on Mechanical Rock Properties.

## One-line Summary
Rapid thermal cooling from 100°C can cause either microcrack growth or healing in rocks, depending on grain size and heterogeneity, as demonstrated by changes in mechanical properties and explained by 3D thermo-mechanical modeling.

## Research Question
What are the effects of rapid thermal cooling, including single and multiple cycles, on the mechanical properties (fracture toughness, tensile strength, P-wave velocity, porosity) of various rock types, and what mechanisms explain the observed behaviors?

## Study Area / Data
The study used rock specimens from northern and southern Arizona, USA, and from a mining district near Superior, Arizona. Rock types included Coconino sandstone, Sierrita granite, South Mountain granite, diabase (with and without ore veins), quartzite, KVS (Cretaceous Volcanic Sediments), and skarn. Cores for some specimens were taken from depths of 1,000–2,000 m [Kim 2013, pp. 2-3].

## Methods
- **Thermal Loading:** Specimens were slowly heated (1–2°C/min) to 100, 200, or 300°C and then rapidly cooled with a fan blowing room-temperature air (~25°C) at ~10 m/s. Multiple cyclic tests (10, 15, 20 cycles) were conducted with a maximum temperature of 100°C [Kim 2013, pp. 2-3].
- **Mechanical Testing:** Included Edge Notched Disc (END) tests for Mode I fracture toughness (K_IC), Brazilian disc tests for tensile strength, seismic tests for P-wave velocity, and porosity tests based on oven-dry and saturated mass [Kim 2013, pp. 2-3].
- **Numerical Modeling:** 3D transient thermo-mechanical analysis was conducted using the ANSYS finite element program to simulate the rapid cooling of a cylindrical specimen [Kim 2013, pp. 8-11].

## Key Findings
- Rapid cooling from 300°C significantly reduced both fracture toughness and tensile strength in Coconino sandstone [Kim 2013, pp. 4-5].
- After 5 cycles of cooling from 100°C, two distinct behaviors were observed:
    - **Crack Growth:** Granite, KVS, and diabase with ore veins showed increased porosity, decreased P-wave velocity, and decreased tensile strength [Kim 2013, pp. 5-7].
    - **Crack Healing:** Quartzite, skarn, and diabase without ore veins showed decreased porosity, increased P-wave velocity, and increased tensile strength [Kim 2013, pp. 7-8].
- ANSYS modeling indicated that rapid cooling creates a thin outer zone of high tensile stress (>6 MPa) and a large inner zone of lower compressive stress [Kim 2013, pp. 11-12].
- The behavior is linked to rock texture: more heterogeneous, coarse-grained rocks are prone to crack growth, while less heterogeneous, fine-grained rocks tend to exhibit crack healing [Kim 2013, pp. 14-14].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Fracture toughness (K_IC) of Coconino sandstone decreased from ~0.7 to ~0.6 MPa√m after heating to 300°C. | [Kim 2013, pp. 4-5] | Single cycle, 25-300°C | 10-13 END tests per temperature. |
| Tensile strength of Coconino sandstone decreased from ~6 MPa to <5 MPa after heating to 300°C. | [Kim 2013, pp. 4-5] | Single cycle, 25-300°C | 5 Brazilian tests per temperature. |
| After 20 cycles (25-100°C), K_IC of Coconino sandstone increased from 1 to 1.18 MPa√m. | [Kim 2013, pp. 4-5] | Multiple cycles, max 100°C | 12 specimens per cycle step. |
| Porosity of Sierrita granite increased by 68% after 5 cycles (25-100°C). | [Kim 2013, pp. 5-7] | 5 cycles, max 100°C | 5 samples (50.8x50.8 mm). |
| P-wave velocity of Sierrita granite decreased from 5.61 to 5.31 km/s after 5 cycles (25-100°C). | [Kim 2013, pp. 5-7] | 5 cycles, max 100°C | 14 samples (50.8x38.1 mm). |
| Porosity of diabase (no ore vein) decreased by 14% after 5 cycles (25-100°C). | [Kim 2013, pp. 7-8] | 5 cycles, max 100°C | 3 samples (63.5x50.8 mm). |
| Tensile strength of quartzite increased by 28% after 5 cycles (25-100°C). | [Kim 2013, pp. 7-8] | 5 cycles, max 100°C | 11 samples (50.8x25.4 mm). |
| ANSYS model showed tensile stresses >6 MPa in a thin outer zone (<5 mm thick) during cooling. | [Kim 2013, pp. 11-12] | Simulated 100°C to 25°C cooling | Used granite-like properties. |
| ANSYS model showed compressive stresses (~2.5 MPa) in the specimen's center during cooling. | [Kim 2013, pp. 11-12] | Simulated 100°C to 25°C cooling | Used granite-like properties. |

## Limitations
- Shortage of specimens from the mining client limited the number and types of tests for some rock types [Kim 2013, pp. 3-4].
- END tests for fracture toughness were not conducted on mining samples due to the complexity of thermal stresses around the notch [Kim 2013, pp. 3-4].
- The ANSYS model did not include cracks; stress analysis was used to infer crack behavior [Kim 2013, pp. 8-11].
- Microscopy was not performed, which would have been helpful for interpreting crack healing [Kim 2013, pp. 14-14].

## Assumptions / Conditions
- The heating rate (1–2°C/min) was slow enough to avoid significant transient thermal gradients during heating [Kim 2013, pp. 2-3].
- The convective heat transfer coefficient for the fan cooling was estimated at 100 W/m²K [Kim 2013, pp. 2-3].
- The 3D ANSYS model assumed isotropic, homogeneous material properties typical of hard rock (e.g., granite) [Kim 2013, pp. 8-11].
- Subcritical crack growth theory was used to interpret crack propagation in the tensile stress zone [Kim 2013, pp. 11-12].

## Key Variables / Parameters
- **Thermal Loading Temperature:** 100°C, 200°C, 300°C.
- **Number of Cycles:** 1, 5, 10, 15, 20.
- **Rock Type:** Granite, sandstone, diabase, quartzite, KVS, skarn.
- **Rock Texture:** Grain size, heterogeneity, presence of ore veins.
- **Measured Properties:** Mode I fracture toughness (K_IC), tensile strength, P-wave velocity, porosity.

## Reusable Claims
- Rapid cooling from 100°C can cause measurable changes in rock mechanical properties even without high peak temperatures [Kim 2013, pp. 4-5].
- The presence of ore veins in diabase promotes crack growth during thermal cycling, whereas their absence promotes crack healing [Kim 2013, pp. 7-8].
- In coarse-grained, heterogeneous rocks, tensile cracking in a thin outer zone during rapid cooling can dominate over compressive closure in the interior, leading to net crack growth [Kim 2013, pp. 14-14].
- In fine-grained, homogeneous rocks, the tensile cracking zone may not form, allowing compressive closure in the interior to dominate, leading to net crack healing [Kim 2013, pp. 14-14].
- The loss of water saturation during thermal testing cannot explain observed increases in P-wave velocity, as saturation increases velocity [Kim 2013, pp. 7-8].

## Candidate Concepts
- [[Thermal stress]]
- [[Microcrack propagation]]
- [[Crack healing]]
- [[Subcritical crack growth]]
- [[Convective heat transfer]]
- [[Thermo-mechanical coupling]]
- [[Rock fatigue]]

## Candidate Methods
- [[Edge Notched Disc (END) test]]
- [[Brazilian disc test]]
- [[Seismic P-wave velocity measurement]]
- [[Porosity measurement by saturation]]
- [[3D transient thermo-mechanical finite element modeling]]

## Connections To Other Work
- The study references prior work on thermal cracking in rocks due to slow heating [Zomeni 1997; Meredith and Atkinson 1985].
- It connects to engineering applications like deep mining ventilation and nuclear waste storage [Kemeny et al. 2006].
- The analysis uses subcritical crack growth properties from Ko and Kemeny (2011) for Coconino sandstone.
- It notes that thermal fatigue in rocks has been studied by others [Spagnoli et al. 2011; Li et al. 1992; Migliazza et al. 2011; Ferrero et al. 2009].

## Open Questions
- How does the initial water saturation state of the rock influence the crack growth/healing response to thermal cycling?
- Would analyzing the results in terms of fatigue theory provide additional insights beyond subcritical crack growth?
- How would microscopy (e.g., thin section analysis) clarify the mechanisms of crack healing observed in some rocks?

## Source Coverage
All 11 non-empty indexed fragments were processed. The compiled source blocks total 11, with a coverage ratio of 1.0 by blocks and 1.004 by characters (52,067 compiled chars from 51,860 indexed chars). The source signature is `671f243da62eede6c79dc5ad97856347e73d4e7a`.
