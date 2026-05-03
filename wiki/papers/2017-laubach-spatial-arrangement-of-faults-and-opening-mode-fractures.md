---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2017-laubach-spatial-arrangement-of-faults-and-opening-mode-fractures"
title: "Spatial Arrangement of Faults and Opening-Mode Fractures."
status: "draft"
source_pdf: "data/papers/2018 - Spatial arrangement of faults and opening-mode fractures.pdf"
collections:
  - "2文章钻孔裂缝分形关系"
citation: "Laubach, S.E., et al. \"Spatial Arrangement of Faults and Opening-Mode Fractures.\" *Journal of Structural Geology*, 2017. doi:10.1016/j.jsg.2017.08.008. Accessed 2026."
indexed_texts: "20"
indexed_chars: "95795"
nonempty_source_blocks: "20"
compiled_source_blocks: "20"
compiled_source_chars: "96294"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.005209"
coverage_status: "full-index"
source_signature: "5de12b67e43f1d9e764677d2f1d4c5303b2782c5"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T21:18:46"
---

# Spatial Arrangement of Faults and Opening-Mode Fractures.

## One-line Summary
This paper introduces a special issue that highlights recent progress in characterizing and understanding the spatial arrangements of fault and opening‑mode fracture patterns across scales and structural settings, emphasizing new quantification methods and the interplay with diagenesis and mechanical stratigraphy.

## Research Question
How do spatial arrangements of faults and opening‑mode fractures relate to mechanical stratigraphy, scale, loading conditions, growth processes, geochemical interactions, and other factors, and how can these arrangements be rigorously quantified to reduce subsurface uncertainty?

## Study Area / Data
The paper itself does not present original field or laboratory data; it synthesizes findings from twenty contributing papers in the special issue. These studies span diverse settings:
- Tight‑gas sandstone (Frontier Formation, Wyoming, USA) and shale (Utica Shale, eastern Canada) via horizontal well logs, cores, and outcrops.
- Carbonate platforms and rift‑related carbonates in Provence (France), Apulia (Italy), Sorrento peninsula (Italy), and the Suez Rift (Egypt).
- Fold‑thrust belts: Moine Thrust Belt (NW Scotland), deep‑water thrust belt near Malaysia.
- Basement terrains: Upper Rhine Graben shoulder, southern Black Forest (Germany), Precambrian basement of South Norway.
- Deformation bands in siliciclastic‑carbonate sequences (St. Vincent Basin, South Australia).
- Supra‑detachment basin faults (Buckskin Detachment, western Arizona).
Data types include 1‑D scanlines, 2‑D images (LIDAR, UAV photogrammetry), 3‑D digital outcrop models, microresistivity image logs, and fluid‑inclusion microthermometry.

## Methods
The paper reviews a range of new and improved methods for quantifying spatial arrangement:

| Method | Description | Example application in special issue |
|--------|-------------|--------------------------------------|
| Normalized Correlation Count (CorrCount) | Analyzes spacing between all fracture pairs (not just nearest neighbours) to distinguish even, random, and clustered patterns; provides 95% confidence intervals via Monte Carlo permutation. | Marrett et al. (2017); Li et al. (2017) used it to quantify fracture clusters in Frontier Fm. sandstones. |
| Directional Semivariogram Analysis | Quantifies spatial variability of fracture density and intersection density as a function of direction; identifies structural controls (faults, folds). | Hanke et al. (2017) on Paradox Basin fractures. |
| Topological Sampling (node counting, circular windows) | Measures fracture intensity and connectivity (I‑, Y‑, X‑nodes) independent of scale and orientation. | Procter and Sanderson (2017) on limestone‑shale sequences. |
| Markov Chain Analysis | Statistically tests randomness of fracture relative‑timing relationships to reconstruct fracture development history. | Snyder and Waldron (2017) on Windsor‑Kennetcook subbasin fractures. |
| Digital Outcrop Modelling (UAV photogrammetry) | Creates virtual outcrop models (VOM) for mapping large‐scale fracture patterns (e.g., through‑going joints). | Corradetti et al. (2017) on a 250 m‑wide carbonate cliff. |
| Fluid‑Inclusion Microthermometry + Thermal History Modelling | Reconstructs opening history of fracture clusters and provides independent timing evidence. | Hooker et al. (2017) on quartz‑cemented microfractures. |
| Along‑fault friction and fluid pressure modelling (Boundary Element Method) | Simulates effects of local fluid pressure and friction on the spatial distribution of fault‑related opening‑mode fractures. | Maerten et al. (2017). |

Additionally, the paper discusses traditional 1‑D methods (coefficient of variation Cv, cumulative frequency plots, non‑parametric tests) and their limitations.

## Key Findings
- **Spatial arrangement is a primary source of structural heterogeneity** that controls fluid flow, rock strength, and seismic risk; regular spacing cannot be assumed for subsurface fractures – clusters and corridors are common.
- **New quantification tools** (normalized correlation count, topology, semivariograms) now allow objective discrimination of random, clustered, and evenly spaced patterns and can be applied to 1‑D, 2‑D, and 3‑D data.
- **Diagenesis strongly modulates spatial arrangement**: fractures formed before or after cementation show different clustering patterns; early diagenetic conditions can produce unbounded, diffuse fractures, whereas later diagenesis leads to bed‑bounded, regularly spaced sets (Lavenu & Lamarche; Korneva et al.; Li et al.; Hooker et al.).
- **Fracture height hierarchies are critical**: failure to account for height patterns can make spacing data meaningless; through‑going joints arrest differently depending on mechanical unit thickness (Corradetti et al.).
- **In fold‑thrust belts**, high‑strain forelimbs contain numerous, large, interconnected fractures that are mostly quartz‑filled and sealed; low‑strain backlimbs have fewer, open, disseminated fractures – the largest fracture populations may not coincide with open, conductive fractures (Watkins et al.).
- **Topological approaches** reveal that the same fracture trace lengths and orientations can produce entirely different connectivity (e.g., a well‑connected network vs. a corridor vs. a random arrangement), and cementation of one set can destroy connectivity even where fracture traces are abundant.
- **Fault patterns** show scale‑dependent clustering (e.g., normalized correlation count reveals boundary‑condition control rather than fault‑interaction control in a supra‑detachment basin; Laubach et al.).
- **Basement studies** demonstrate that lineament detection is biased by image resolution and that fault density correlates with host rock type (higher in granite, lower in gneiss; Meixner et al.).
- A reliable fluid‑flow prediction requires three integrated elements: (1) measurement of spatial variability of geometric attributes, (2) network topology (how fractures intersect and connect), and (3) temporal and spatial variations in fracture microstructure (aperture, cement) that control transmissivity.

## Core Evidence Table

| Evidence | Source (in this introductory article) | Conditions | Notes |
|----------|--------------------------------------|------------|-------|
| Clustered subsurface fracture patterns in Frontier Fm. differ from regularly spaced surface patterns; clusters are fractal (35 m wide, separated by 50–100 m gaps). | Li et al. (2017) | Tight‑gas sandstone, two orthogonal open‑fracture sets; horizontal wellbore image logs vs. outcrop. | Normalized correlation count used; clusters account for gas/water production anomalies. |
| Microfracture spacing distributions show non‑random clustering that evolves from dynamic crack interaction during propagation; independent timing from fluid inclusions. | Hooker et al. (2017) | Sandstones with quartz‑filled microfractures; compiled from eight formations on three continents. | First reconstruction of fracture cluster opening history using fluid‑inclusion microthermometry. |
| Early‑diagenetic fractures in platform carbonates are unbounded in height; current mechanical stratigraphy formed later and does not control those early fractures. | Lavenu & Lamarche (2017) | Provence (France) and Apulia (Italy) carbonates; early burial, pre‑tectonic. | Fracture stratigraphy is sensitive to diagenetic history; height distribution cannot be predicted from present‑day mechanical properties. |
| Dolomitization alters petrophysical properties and modifies fracture spacing; current mechanical stratigraphy strongly affects later‑stage fractures. | Korneva et al. (2017) | Hammam Faraun Fault Block, Suez Rift, Egypt; rift‑related carbonates. | Dolomitization interplay with porosity controls rock strength; precursor limestone texture matters. |
| In fold‑thrust belts, large clustered fractures in high‑strain zones are sealed, whereas sparse disseminated fractures in low‑strain zones are open. | Watkins et al. (2017) | Achnashellach Culmination, Moine Thrust Belt, NW Scotland. | Flow conduits are offset from the most intensely fractured regions. |
| Semivariogram analysis shows that folds set the background spatial variability of fracture networks, while faults impose additional, distance‑dependent structure. | Hanke et al. (2017) | Paradox Basin, Utah; map‑scale anticline and normal fault. | Semivariogram parameters can be used as inputs for stochastic models. |
| Topological sampling (node counting) gives similar precision to scanlines but is faster and directly measures connectivity; different limestone layers show anomalous fracture intensity at different locations, unrelated to bed thickness. | Procter & Sanderson (2017) | Layered limestone‑shale, North Somerset, UK. | Georeferenced photos used for later trace‑length measurements. |
| Deformation bands in carbonates (calcarenites) show a range of cataclasis intensity with 25–33% porosity reduction, further reduced by iron‑hydroxide cement. | Lubiniecki et al. (2017) | Port Willunga Fm., St. Vincent Basin, South Australia; adjacent to Willunga Fault. | Deformation bands constrain neotectonic basin evolution. |
| In a supra‑detachment fault array, normalized correlation count shows that fault spatial and size patterns are influenced by boundary conditions (fault shape, mechanical unit thickness) rather than fault‑fault interaction. | Laubach et al. (2017) | Buckskin Detachment upper plate, Western Arizona. | High‑strain setting. |
| Lineament mapping in crystalline basement is resolution‑dependent; higher fault density in granite than in gneiss. | Meixner et al. (2017) | Southern Black Forest, Germany (~2000 km²). | Censoring and truncation biases quantified for each image type. |
| Fracture hooking (linkage) process follows three stages – underlapping, overlapping, linkage – depending on fracture length, spacing, and stress regime. | Lamarche et al. (2017b) | Permian shales, Lodève Basin, SW France. | Only fractures of similar size interact and link. |
| Vertical through‑going joints in a carbonate platform show a complex height hierarchy that reflects the mechanical behaviour of sedimentary units; major joints arrest more frequently in shallow‑water carbonates. | Corradetti et al. (2017) | Sorrento peninsula, Italy; 250 m‑wide cliff VOM. | Drone‑aided photogrammetric model with 1003 digitized fractures. |
| Markov chain analysis of fracture cross‑cutting relationships reveals overprinting history related to dextral then sinistral reactivation of the Minas Fault Zone. | Snyder & Waldron (2017) | Windsor‑Kennetcook subbasin, Maritimes Basin, Canada. | Fracture initiation linked to late Paleozoic deformation, reactivation during Atlantic opening. |
| Along‑fault variations in fluid pressure and friction produce complex patterns of fault‑related opening‑mode fractures. | Maerten et al. (2017) | Boundary element model (no specific natural case in this summary). | Highlights the role of local fluid pressure patterns along faults. |
| In the Utica Shale, three steeply‑dipping fracture sets, bed‑parallel fractures, and faults are present; variograms show clustering; some fractures have heights up to 30 m. | Ladevèze et al. (2017) | Eastern Canada; shallow wells and outcrop. | Fracture sets in outcrop match those at depth. |
| Deep‑water thrust belt shows along‑strike heave deficits on master thrusts compensated by small imbricate arrays; cross‑strike displacement relays create systematic, predictable patterns. | Totake et al. (2017) | Deep‑water setting near Malaysia; 3D seismic. | Mapping approach can infer complex faults in poorly imaged seismic volumes. |
| Fault and fracture networks in the Upper Rhine Graben shoulder are controlled by structural heritage and rock type; a hierarchy of fault blocks governs fine‑scale structures. | Bertrand et al. (2017) | Western shoulder, Upper Rhine Graben. | Reactivation of older structures interacting with rock type. |
| Wide‑scale basement fault patterns show a regular arrangement visible at the crustal block scale, encompassing faults of different ages, styles, and attitudes. | Gabrielsen et al. (2017) | Precambrian basement, South Norway; remote sensing and potential field data. | Brittle structures mapped over a large crustal block. |

## Limitations
- The special issue does not cover all important aspects of fault and fracture spatial arrangement (e.g., active geomechanical and stochastic modeling are not directly represented).
- Many outcrop studies are affected by censoring and truncation artifacts (limited scanline length, undersampling of large structures); surface exposures may have different deformation histories than subsurface rocks (e.g., joints formed during late uplift may be absent at depth).
- 1‑D scanline measures of spacing and intensity are strongly scale‑dependent unless the size range of measured fractures is explicitly stated.
- Methods built on an assumption of regular or random spacing are unreliable for subsurface fractures, which are commonly clustered.
- Fracture height patterns are rarely rigorously documented; undiagnosed height hierarchies can render outcrop spacing data misleading.
- The link between spatial arrangement and fracture‑filling cement (timing, amount) is only beginning to be explored, and few studies combine spatial analysis with petrology.

## Assumptions / Conditions
- Spatial arrangement is defined as the property of an array that defines the positions of constituent structures; it can be viewed either as objects‑in‑space (position, orientation, abundance) or as objects‑in‑relation‑to‑one‑another (topology).
- Regular spacing is often assumed in widely used subsurface fracture assessment methods, but this assumption is frequently violated.
- Fracture patterns are inferred to reflect growth processes, mechanical stratigraphy, loading conditions, and diagenetic history.
- For fractures that grew in the subsurface, the most meaningful measure for fluid flow or rock strength is the spatial arrangement of fractures at or above a threshold size (often the largest, open fractures).
- Topological measures are scale‑ and orientation‑invariant, permitting unbiased comparison across scales.
- The three key elements for predicting fluid flow are spatial variability of geometry, network topology, and spatio‑temporal variations in fracture transmissivity (aperture, cement).

## Key Variables / Parameters
- **Spacing**: nearest‑neighbour distance, average spacing, median, standard deviation, coefficient of variation (Cv).
- **Intensity**: number of fractures per unit length (1‑D), trace length per unit area (2‑D), surface area per unit volume (3‑D).
- **Normalized correlation count**: measures deviation from random spacing for all fracture pairs; used to identify statistically significant clustering or even spacing.
- **Topological nodes**: I‑nodes (isolated tips), Y‑nodes (abutting or splaying), X‑nodes (crossing); proportions define connectivity.
- **Cluster / corridor dimensions**: width, spacing, internal size distribution.
- **Fracture height**: bed‑bounded vs. non‑stratabound, height hierarchies.
- **Mechanical layer thickness**: controls spacing in bed‑bounded sets.
- **Cement fill**: open, partially cemented, fully sealed; affects transmissivity.
- **Aperture size distribution**: often follows power‑law scaling.
- **Fluid pressure along faults**: influences opening‑mode fracture distribution.
- **Semivariogram range and sill**: quantify spatial continuity of fracture density.

## Reusable Claims
- “Among these techniques, coefficient of variation and interval counting are least affected by the minimum size, or threshold, of fractures sampled.” （fragment）[Laubach 2017, pp. 2-3]
- “For subsurface situations, where narrow fractures may be preferentially sealed with natural cements, the most meaningful measure for fluid flow or fracture strength is the spatial arrangement of fractures at or above a threshold size.” [Laubach 2017, pp. 2-3]
- “Regular spacing is not a safe assumption for subsurface fractures.” [Laubach 2017, pp. 2-3]
- “Spatial organization implies objects are spatially organized and thus arranged non‑randomly. Spatial organization is a special case of spatial arrangement, possibly arising as an emergent property of a self‑organized system or imposed by some other aspect of the geology, such as host rock type and dimensions, diagenetic overprint, or position in folds.” [Laubach 2017, pp. 3-4]
- “Differences in height patterns, particularly if undiagnosed, can render outcrop fracture spacing data meaningless and interfere with comparison of field data with models.” [Laubach 2017, pp. 4-5]
- “Where damage zones are concentrations of faults, deformation bands and fully cemented veins they may provide important sealing capacity, but where open or partially cemented fractures occur they provide fluid pathways along faults.” [Laubach 2017, pp. 5-6]
- “For such fractures, the terms ‘joint’ and ‘vein’ are inconvenient descriptors. Instead, it is preferable to specify the displacement mode, which can be observed, and explicitly describe the mineral fill.” [Laubach 2017, pp. 5-6]
- “Clustering is prominent in some fault patterns. Even in regional joint systems there are commonly well‑developed, but poorly understood, fracture corridors.” [Laubach 2017, pp. 5-6]
- “Only by combining information from all three of these aspects [spatial location, size, patterns, and evolving geochemistry] is it possible to predict reliably the fluid flow, rock strength, and other key properties affected by fractures.” [Laubach 2017, pp. 12]
- “Fracture clusters (or corridors) have been identified as widespread features in both groundwater and hydrocarbon reservoir rocks that need to be accounted for in reservoir modeling.” [Laubach 2017, pp. 11]
- “The path from fracture characterization to predicting fluid flow and other effects clearly involves three key considerations: 1) The measurement of geometrical attributes linked to the spatial location…; 2) An understanding of how the individual fractures relate to one another… in terms of topology…; 3) How the form and microstructure (aperture, cement, etc.) varies spatially and temporally…” [Laubach 2017, pp. 12]

## Candidate Concepts
- [[fracture spatial arrangement]]
- [[fracture spacing]]
- [[fracture clustering]]
- [[fracture corridor]]
- [[fracture swarm]]
- [[mechanical stratigraphy]]
- [[diagenesis and fractures]]
- [[topology of fracture networks]]
- [[normalized correlation count]]
- [[fracture damage zone]]
- [[fracture height hierarchy]]
- [[stratabound fractures]]
- [[opening‑mode fracture]]
- [[coefficient of variation (Cv)]]
- [[spatial organization]]

## Candidate Methods
- [[Normalized correlation count (CorrCount)]]
- [[Directional semivariogram analysis]]
- [[Topological sampling (node counting)]]
- [[Markov chain analysis for fracture timing]]
- [[Digital outcrop modelling (UAV photogrammetry)]]
- [[Fluid‑inclusion microthermometry]]
- [[Boundary element method for fault‑related fractures]]
- [[Scanline sampling]]
- [[Cumulative frequency distribution testing]]
- [[Fracture porosity history from petrology]]

## Connections To Other Work
The introductory article places the special issue within a broad literature context. Key connections include:
- Previous spatial‑arrangement concepts: Bonnet et al. (2001) scaling; Olson (2004) subcritical crack‑growth models; Sanderson & Nixon (2015) topology; Narr & Lerche (1984) subsurface fracture density.
- Mechanical stratigraphy: Ladeira & Price (1981) spacing‑bed thickness relationship; Narr & Suppe (1991) joint spacing.
- Diagenesis and fracture opening: Laubach (2003) sealed fractures; Olson et al. (2009) diagenesis‑mechanics coupling; Hooker & Katz (2015) synkinematic cementation.
- Fault damage zones: Chester & Logan (1986); Kim et al. (2004); Choi et al. (2016).
- Fracture corridors in reservoirs: Questiaux et al. (2010); Ogata et al. (2014).
- Correlation analysis: Marrett et al. (2017) CorrCount method.
- Semivariogram applications: Hanke et al. (2017).
- Fluid flow implications: Philip et al. (2005) coupled fracture‑matrix flow; Manzocchi (2002) connectivity of correlated fractures.

## Open Questions
- How do fracture height patterns evolve with progressive diagenesis and burial, and how can these height hierarchies be rigorously incorporated into 1‑D subsurface datasets?
- What are the quantitative thresholds that distinguish fracture clusters formed by dynamic crack interaction from those imposed by inherited sedimentary or structural heterogeneities?
- Can the fractal dimensions of fracture clusters be predicted from geomechanical‑chemical models that couple subcritical crack growth, stress shadowing, and cement precipitation?
- How do geochemical processes (cement timing and composition) control the transmissivity of fracture networks independently of their geometric connectivity, and how can this be parameterized in flow simulators?
- To what extent are surface‑derived fracture patterns (e.g., joints formed during exhumation) reliable analogues for deeply buried, potentially cemented fracture systems?
- What is the relative importance of self‑organization versus external forcing (e.g., fault‑related stress perturbations, fluid pressure cycles) in producing large‑scale fracture corridors in tight reservoirs?

## Source Coverage
All 20 non‑empty indexed text blocks from this paper were processed and incorporated into the Wiki page.  
- Indexed fragments: 20  
- Indexed characters: 95,795  
- Compiled characters: 96,294  
- Coverage ratio by fragments: 1.0 (100%)  
- Coverage ratio by characters: 1.0052 (~100.5%, slight increase due to Markdown formatting)  
No content was omitted; every indexed fragment contributed to the assembled content.
