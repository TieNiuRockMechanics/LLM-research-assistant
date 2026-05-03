---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2002-liu-a-note-on-unsaturated-flow-in-two-dimensional-fracture-networks"
title: "A Note on Unsaturated Flow in Two-Dimensional Fracture Networks."
status: "draft"
source_pdf: "data/papers/2002 - A note on unsaturated flow in two-dimensional fracture networks.pdf"
collections:
citation: "Liu, H. H., et al. \"A Note on Unsaturated Flow in Two-Dimensional Fracture Networks.\" *Water Resources Research*, vol. 38, no. 9, 2002, p. 1176. doi:10.1029/2001WR000977. Accessed 2026."
indexed_texts: "9"
indexed_chars: "44543"
nonempty_source_blocks: "9"
compiled_source_blocks: "9"
compiled_source_chars: "44712"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.003794"
coverage_status: "full-index"
source_signature: "8c5ef45bcf30fca167537346956255fd91e44d97"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T11:57:08"
---

# A Note on Unsaturated Flow in Two-Dimensional Fracture Networks.

## One-line Summary
Numerical study of steady-state, gravity-dominated unsaturated flow in 2D fracture networks (~2000 fractures, 10 m × 10 m) shows flow paths are vertical with subhorizontal fractures enabling communications; small fractures don’t contribute to global flow but enhance fracture–matrix interaction; average spacing between flow paths in a layered system may increase with depth; the “influence zone of a capillary barrier” concept describes drift seepage, and 3D models are needed for realistic capillary-barrier evaluation. [Liu 2002, pp. 1 1, 8 8]

## Research Question
While considerable progress had been made on unsaturated flow in single fractures, understanding of unsaturated flow processes within fracture networks remained incomplete, despite the importance of network-scale flow for field-scale applications. This study numerically investigates steady flow behavior in two-dimensional unsaturated fracture networks and examines factors affecting seepage into underground openings (drifts). [Liu 2002, pp. 1 1–1 2]

## Study Area / Data
- **Location**: Fracture-network properties are based on the highly fractured Topopah Spring welded (TSw) unit in the unsaturated zone of Yucca Mountain, Nevada. [Liu 2002, pp. 1 1, 2 2]
- **Fracture-map data**: Trace-length distributions and orientations were derived from detailed line surveys in tunnels for the TSw unit (U.S. Geological Survey, unpublished report, 2000). [Liu 2002, pp. 1 2]
- **Aperture data**: The mean and variance of log₁₀(aperture, b) for the TSw unit were approximately −4.01 and 0.04, respectively, based on air-permeability and fracture-density data. [Liu 2002, pp. 2 3]

## Methods
### Fracture-Network Construction
- Computationally constructed two-dimensional fracture networks consist of subvertical and subhorizontal fractures. [Liu 2002, pp. 1 2]
- Procedure: randomly generate points using a uniform distribution within a 10 m × 10 m vertical cross section; for each point, generate a fracture centred on it. [Liu 2002, pp. 1 2]
- Trace lengths are drawn from five groups that have different trace lengths but equal probability of occurrence; lengths and orientations are independent and based on fracture-map data. [Liu 2002, pp. 1 2]
- Fractures with trace lengths < 0.23 m are excluded, assuming they are unlikely to hydraulically connect two active fractures. [Liu 2002, pp. 1 2]
- Generation continues until a desired scanline density is achieved. [Liu 2002, pp. 1 2]
- Average fracture aperture (b) is related to trace length (L) by b = c Lᵈ; c = 1.008 × 10⁻⁴ and d = 0.317 were calibrated using the prescribed mean and variance of log(b). [Liu 2002, pp. 2 3]

### Hydraulic Properties for Individual Fractures
- Each fracture is conceptualised as a 2D porous medium with [[van Genuchten model]] constitutive relations (equations 2a–2c). [Liu 2002, pp. 2 3]
- Parameters: m = 0.633 (index of aperture size distribution), Sₛ = 1, Sᵣ = 0.01. [Liu 2002, pp. 2 3]
- Parameter α (inverse air-entry value) is related to b by α = b / (2 σ cos θ), with θ = 0°. [Liu 2002, pp. 2 3]
- Fracture permeability (k) is approximated by the parallel-plate law: k = b² / 12. [Liu 2002, pp. 2 3]
- Hydraulic-property values for the five fracture groups are in Table 1 of the source. [Liu 2002, pp. 3 4]

### Boundary Conditions and Numerical Simulator
- Infiltration flux: 5 mm yr⁻¹ applied at the top of the network. [Liu 2002, pp. 2 3]
- Bottom boundary: free drainage. Side boundaries: impermeable. [Liu 2002, pp. 2 3]
- Drift diameter: 5 m; drift boundary set at reference pressure 1 bar with no capillary suction. [Liu 2002, pp. 2 3]
- Matrix is treated as impermeable (focus on liquid flow in fractures). [Liu 2002, pp. 2 3]
- Simulations run with the integrated-finite-difference code TOUGH2; mesh ~16 000 elements for a network with ~2000 fractures. [Liu 2002, pp. 3 4]
- A non-uniform top-boundary condition was also used: only fractures between 0–1.5 m and 8.5–10 m horizontally are connected to the source, keeping total flux the same. [Liu 2002, pp. 3 4]

## Key Findings
1.  **Flow‑path structure**: Major flow paths are dominated by connected fractures with large trace lengths; flow paths are generally vertical (gravity‑dominated), while subhorizontal fractures spread paths horizontally. Fractures with small trace lengths may participate near intersections of large fractures. [Liu 2002, pp. 3 4]
2.  **Flow focusing persistence**: When flow is focused at the top boundary (two separated inlet regions), the two vertical flow paths persist through the network without significant communication or horizontal spreading. This suggests that flow focusing can be preserved even when average fracture spacing is much smaller than flow-path spacing, consistent with field observations of isolated wet features (~0.3 m wide). [Liu 2002, pp. 4 5]
3.  **Depth‑dependent flow‑path spacing (hypothesis)**: In a layered system where matrix flow is ignored, the number of vertical flow paths tends to decrease with depth as long as gravity is the dominant driving force. Observed decrease in mineral-coating abundance with depth at Yucca Mountain may be an indicator of this phenomenon, though this is a hypothesis requiring verification. [Liu 2002, pp. 5 6]
4.  **Sensitivity to α**: Increasing fracture permeabilities by one order of magnitude did not significantly change flow patterns, but increasing α by one order of magnitude (making gravity even more dominant) caused some flow paths to disappear because water cannot climb subhorizontal segments against reduced capillary gradients. [Liu 2002, pp. 5 6]
5.  **Role of small fractures**: Many small fractures do not contribute to global flow but are still connected to major flow paths (Figure 6 of the source). They can substantially affect matrix‑diffusion and other processes sensitive to the interface area between matrix and active fractures. This observation supports the “large/small fracture” continuum conceptualisation. [Liu 2002, pp. 6 7]
6.  **Capillary‑barrier failure in 2D**: In the simulated 2D networks the drift did not act as an effective capillary barrier; no significant lateral diversion was observed above the drift ceiling. Increasing permeability did not reduce seepage. [Liu 2002, pp. 6 7]
7.  **“Influence zone of a capillary barrier”**: An effective capillary barrier requires lateral flow within a very thin zone above the drift ceiling, bounded by a vertical distance of ~1/α (0.07–0.23 m for the fracture properties used). In 2D it is hard to generate sufficient lateral flow paths within such a thin zone. Three‑dimensional fracture‑network models are needed for a realistic evaluation because fractures perpendicular to the drift axis may provide substantial lateral connectivity in the third dimension. [Liu 2002, pp. 7 8]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Flow paths are vertical, with sub‑horizontal fractures inducing horizontal spreading. | [Liu 2002, pp. 3 4] | Steady‑state, infiltration 5 mm yr⁻¹, uniform‑pressure top boundary, matrix impermeable. | Figures 1–2 of the source. |
| Non‑uniform top boundary (two inlet regions) yields two persistent vertical flow paths without significant communication. | [Liu 2002, pp. 4 5] | Same total flux as uniform case; top fractures only connected at 0–1.5 m and 8.5–10 m horizontally. | Consistent with field‑observed isolated wet feature (width ~0.3 m). |
| Increasing α by one order of magnitude causes some flow paths to disappear (e.g., path from point d). | [Liu 2002, pp. 5 6] | All other boundary conditions and fracture properties as in Figure 2 of the source. | Gravity becomes more dominant; water cannot “climb” subhorizontal segments against reduced capillary gradient. |
| Small fractures connected to the backbone show large saturations but carry negligible flux. | [Liu 2002, pp. 6 7] | Steady‑state condition, initial saturation 0.1%; saturations > 7% considered a signature of connection to major flow paths. | Zone A in Figures 2 and 6 of the source; relevant for matrix‑diffusion area. |
| Drift does not act as an effective capillary barrier in 2D; no significant lateral diversion observed. | [Liu 2002, pp. 6 7] | 2D fracture network, drift diameter 5 m, capillary‑pressure boundary at drift of 1 bar. | Increasing permeability did not reduce seepage. |
| Influence‑zone thickness (1/α expressed as pressure head) ranges from 0.07 m to 0.23 m for the tested fractures. | [Liu 2002, pp. 7 8] | Table 1 of the source: α from 4.39 × 10⁻⁴ Pa⁻¹ to 1.40 × 10⁻³ Pa⁻¹. | Explains why sufficient lateral connectivity is unlikely in 2D. |

## Limitations
- The study is limited to two‑dimensional vertical‑cross‑section fracture networks; three‑dimensional connectivity effects are not captured. [Liu 2002, pp. 7 8]
- Only steady‑state flow is considered; transient or intermittent flow behaviours (e.g., rivulet snapping and re‑forming) are not addressed. [Liu 2002, pp. 1 1]
- The rock matrix is treated as impermeable, so fracture–matrix fluid exchange is neglected. [Liu 2002, pp. 2 3]
- The fracture‑network construction is relatively simple (subvertical/subhorizontal sets), and fractures with trace lengths < 0.23 m are excluded. [Liu 2002, pp. 1 2]
- The hypothesised depth‑dependent flow‑path spacing in layered systems is not directly validated in the paper. [Liu 2002, pp. 5 6]
- Although fracture permeabilities were varied, a “larger increase” that could yield significant flow‑pattern changes was not investigated. [Liu 2002, pp. 5 6]

## Assumptions / Conditions
- Gravity‑dominated flow; capillary forces are present but gravity is the primary driving force. [Liu 2002, pp. 3 4]
- Infiltration rate is constant at 5 mm yr⁻¹ (estimated net infiltration for Yucca Mountain). [Liu 2002, pp. 2 3]
- Fracture constitutive relations follow the [[van Genuchten model]] with m = 0.633, Sₛ = 1, Sᵣ = 0.01. [Liu 2002, pp. 2 3]
- Fracture permeability follows the parallel‑plate law (k = b²/12) using the average aperture. [Liu 2002, pp. 2 3]
- Fracture aperture and trace length are related by a power law (b = c Lᵈ), calibrated to air‑permeability and density data. [Liu 2002, pp. 2 3]
- Matrix is impermeable, i.e., liquid flow occurs only in fractures. [Liu 2002, pp. 2 3]
- Contact angle for water is assumed to be 0°. [Liu 2002, pp. 2 3]
- Fracture intersections are assigned the properties of one of the intersected fractures (randomly). [Liu 2002, pp. 2 3]

## Key Variables / Parameters
- **Trace length (L)** [m]: five groups, 0.23–2.65 m. [Liu 2002, pp. 3 4]
- **Average aperture (b)** [m]: 6.3 × 10⁻⁵ to 2.0 × 10⁻⁴ m. [Liu 2002, pp. 3 4]
- **Permeability (k)** [m²]: 3.33 × 10⁻¹⁰ to 3.37 × 10⁻⁹ m². [Liu 2002, pp. 3 4]
- **van Genuchten α** [Pa⁻¹]: 4.39 × 10⁻⁴ to 1.40 × 10⁻³ Pa⁻¹. [Liu 2002, pp. 3 4]
- **van Genuchten m**: 0.633 (n = 1/(1 – m) ≈ 2.72). [Liu 2002, pp. 2 3, 3 4]
- **Flow focusing**: spacing of vertical flow paths on the order of metres to tens of metres. [Liu 2002, pp. 3 4]
- **Influence‑zone thickness**: the vertical distance 1/α (expressed as pressure head), here 0.07–0.23 m. [Liu 2002, pp. 7 8]

## Reusable Claims
1.  “In gravity‑dominated unsaturated fracture networks, major flow paths are controlled by connected fractures with large trace lengths; subhorizontal fractures provide communication and induce horizontal spreading of otherwise vertical paths.” [Liu 2002, pp. 3 4, 8 8]  
    *Condition*: 2D network with properties typical of welded tuff (TSw), constant infiltration ~5 mm yr⁻¹, matrix impermeable. *Limitation*: may not generalise to strongly capillary‑driven regimes or 3D networks with different connectivity.

2.  “Flow focusing set at the top boundary can persist through a fracture network without significant lateral spreading, even when the average fracture spacing is much smaller than the spacing between the imposed flow paths.” [Liu 2002, pp. 4 5]  
    *Condition*: same as above; non‑uniform top‑boundary saturation.

3.  “Fractures with small trace lengths that are connected to the globally‑conducting backbone do not contribute appreciable fluxes but substantially enlarge the fracture–matrix interface area, affecting matrix‑diffusion and other interface‑sensitive processes.” [Liu 2002, pp. 6 7]  
    *Condition*: identified in the 2D network simulations; initial saturation 0.1%, steady state.

4.  “For an underground opening in fractured rock, the ‘influence zone of a capillary barrier’ is the thin layer above the ceiling (thickness ~1/α in pressure head) within which lateral flow must occur for the capillary barrier to be effective. In 2D networks this zone is often too thin to develop sufficient lateral connectivity, causing barrier failure.” [Liu 2002, pp. 7 8]  
    *Condition*: drift at constant pressure, no capillary suction at the wall; fracture properties as in Table 1. *Limitation*: 3D connectivity perpendicular to the drift axis is not captured.

5.  “In a layered system where matrix flow is negligible, average spacing between gravity‑driven vertical flow paths tends to increase with depth, implying a depth‑dependent reduction in the number of active pathways.” [Liu 2002, pp. 5 6]  
    *Status*: stated as a hypothesis; requires field or modelling verification. *Context*: consistent with observed decrease in mineral‑coating abundance with depth in welded Yucca Mountain units.

## Candidate Concepts
- [[unsaturated fracture network]]
- [[flow focusing in fracture networks]]
- [[influence zone of capillary barrier]]
- [[large and small fracture continuum]]
- [[fracture network constitutive relations]]
- [[persistence of flow focusing in layered media]]
- [[capillary barrier failure in fractures]]

## Candidate Methods
- [[2D fracture network generation with scanline density]]
- [[b = c L^d aperture–trace length scaling]]
- [[van Genuchten model for single fractures]]
- [[TOUGH2 simulation of unsaturated fracture networks]]
- [[capillary barrier influence zone analysis]]

## Connections To Other Work
- **Single‑fracture process studies**: finger‑flow (Glass et al. 1996), film‑flow (Tokunaga & Wan 1997, 2001; Or & Tuller 2000), chaotic behaviour (Faybishenko 1999), intermittent rivulet flow (Su et al. 1999). This paper notes that upscaling these small‑scale mechanisms remains a challenge. [Liu 2002, pp. 1 1]
- **Prior unsaturated fracture‑network models**:
  - Kwicklis & Healy (1993): steady flow in a 2D cross‑section with fewer than ten fractures → highly variable pressure and flux. [Liu 2002, pp. 1 2]
  - Karasaki et al. (1993): 2D horizontal network → strong phase interference. [Liu 2002, pp. 1 2]
  - Therrien & Sudicky (1996): 3D discrete‑fracture analysis → erratic head patterns, irregular plumes. [Liu 2002, pp. 1 2]
  - Finsterle (2000): continuum approach for seepage → calibrated continuum models can produce reasonable results under certain objectives. [Liu 2002, pp. 1 2]
  - Liu & Bodvarsson (2001): fracture‑network‑based constitutive relations; proposed a modified tortuosity factor for the [[Brooks and Corey model]]. [Liu 2002, pp. 1 2, 3 4]
- **Field observations**: Wang et al. (1999) observed an isolated, nearly wet feature ~0.3 m wide in a Yucca Mountain tunnel, consistent with the simulated persistent flow‑focusing pattern. [Liu 2002, pp. 4 5]
- **Mineral‑coating evidence**: CRWMS M&O (2000c) reported decreasing abundance of mineral coatings with depth in the welded part of Yucca Mountain; Liu et al. propose this may reflect a decreasing number of active flow paths with depth. [Liu 2002, pp. 5 6]
- **Large/small fracture continuum**: The observations provide direct evidence supporting the conceptualisation of Wu et al. (2001, unpublished), where “large” fractures carry global flow and “small” fractures enhance interface area. [Liu 2002, pp. 6 7]

## Open Questions
- How can small‑scale mechanisms (fingering, film flow, intermittent rivulet behaviour) be upscaled into field‑scale fracture‑network models? [Liu 2002, pp. 1 1]
- Is the hypothesised depth‑dependent increase in flow‑path spacing in layered systems valid? What controls the rate of decrease in the number of active flow paths with depth? [Liu 2002, pp. 5 6, 8 8]
- How does fracture‑network connectivity in the third dimension (e.g., fractures perpendicular to the drift axis) affect the “influence zone of a capillary barrier” and the likelihood of seepage? [Liu 2002, pp. 7 8]
- How does the behaviour change under transient infiltration rates, intermittent flow, or when the matrix is permeable? [Liu 2002, pp. 1 1, 2 3]
- What is the critical fracture‑permeability increase that would significantly alter flow patterns? (One‑order‑of‑magnitude increase was insufficient; larger increases were not tested.) [Liu 2002, pp. 5 6]

## Source Coverage
All non‑empty indexed fragments from Liu 2002 were processed.  
Coverage metrics: indexed texts: 9; compiled source blocks: 9 of 9 (1.0 by blocks); compiled source characters: 44 712 vs. indexed characters 44 543 (1.004 by chars).  
Compilation strategy: single‑pass‑markdown.  
Source signature: 8c5ef45bcf30fca167537346956255fd91e44d97.  
Coverage status: full‑index.
