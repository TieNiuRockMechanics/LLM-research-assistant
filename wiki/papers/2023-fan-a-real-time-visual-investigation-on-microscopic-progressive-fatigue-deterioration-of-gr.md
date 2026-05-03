---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-fan-a-real-time-visual-investigation-on-microscopic-progressive-fatigue-deterioration-of-gr"
title: "A Real-Time Visual Investigation on Microscopic Progressive Fatigue Deterioration of Granite Under Cyclic Loading."
status: "draft"
source_pdf: "data/papers/2023 - A Real-Time Visual Investigation on Microscopic Progressive Fatigue Deterioration of Granite Under Cyclic Loading.pdf"
collections:
  - "part2"
citation: "Fan, L. F., et al. \"A Real-Time Visual Investigation on Microscopic Progressive Fatigue Deterioration of Granite Under Cyclic Loading.\" *Rock Mechanics and Rock Engineering*, vol. 56, 2023, pp. 5133-5147. doi:10.1007/s00603-023-03326-y."
indexed_texts: "11"
indexed_chars: "53311"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "52867"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.991672"
coverage_status: "full-index"
source_signature: "aa1eaee5974cd9f763f13445ef3f8729cadf58b6"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:07:06"
---

# A Real-Time Visual Investigation on Microscopic Progressive Fatigue Deterioration of Granite Under Cyclic Loading.

## One-line Summary
This paper investigates the microscopic progressive fatigue deterioration of granite under cyclic loading using real-time CT scanning, revealing that damage primarily occurs when the maximum cyclic stress exceeds 46.04% of UCS in multi-level loading, and that under crack initiation stress, porosity increases concentrate in the first twenty cycles.

## Research Question
How does the microscopic progressive fatigue deterioration (cracking and pore evolution) of granite evolve under multi-level and single‑level cyclic loading, and what are the effects of cyclic number when the maximum stress equals the crack initiation stress? [Fan 2023, pp. 1-2, 14]

## Study Area / Data
- **Rock material**: Fresh, intact granite from Hunan Province, China; no visible cracks. [Fan 2023, pp. 2-4]
- **Mineralogy** (XRD): quartz 28.2%, K‑feldspar 27.4%, plagioclase 17.3%, mica 22.2%, kaolinite 4.9%. [Fan 2023, pp. 3-4]
- **Sample geometry**: Cylinders, diameter 6.0 mm, height 12.0 mm (height/diameter ratio 2.0). Ends polished; dried at 105 °C for 48 h. [Fan 2023, pp. 3-4]
- **UCS**: Approximately 108.6 MPa (dry, uniaxial compression). [Fan 2023, pp. 3-4]
- **Experimental environment**: Ambient temperature constant at 20 °C. [Fan 2023, pp. 3-4]

## Methods
- **Real‑time CT scanning system**: Nano Voxel‑2200 high‑resolution CT equipped with Deben Micro‑test CT 5000 loading device. [Fan 2023, pp. 3-4]
  - X‑ray source: cone‑beam, voltage 150 kV, current 150 μA, exposure 0.38 s. [Fan 2023, pp. 4-5]
  - Resolution: 15.71 μm (pixel size 15.71 μm × 15.71 μm planar, 15.71 μm × 15.71 μm × 15.71 μm volumetric). [Fan 2023, pp. 4-5]
  - Scanned region: a central cylinder Φ 6.000 mm × 7.855 mm was analysed after eliminating end‑effect‑distorted slices. [Fan 2023, pp. 4-7]
- **Cyclic loading protocols (displacement control, 0.02 mm/min)**  
  - **Multi‑level cyclic loading**: σ_min = 20.0 MPa; σ_max starts at 30.0 MPa, increases by 10.0 MPa every 100 cycles until failure. CT scanning before loading, after every 100 cycles, and after failure. [Fan 2023, pp. 4-5]
  - **Single‑level cyclic loading**: σ_max = crack initiation stress (46.04% UCS) determined from multi‑level test; σ_min = 20.0 MPa; total 300 cycles. CT scans at cycles 0, 20, 40, 60, 80, 100, 200, 250, 300. [Fan 2023, pp. 4-5, 7-9]
- **Quantitative parameters**
  - **Areal porosity** (*P*_s): percentage of damaged area in a 2D vertical section (three sections at 0°, 120°, 240°). [Fan 2023, pp. 5-7]
  - **Volumetric porosity** (*P*_v): percentage of damaged volume in the 3D analysed region. [Fan 2023, pp. 7-9]
- **Image processing**: threshold‑based separation of micro‑defects (cracks, pores) and matrix from CT slices; voxel counting and 3D reconstruction. [Fan 2023, pp. 4-7, 11-13]

## Key Findings
- **Multi‑level cycling**
  - When σ_max < 46.04% UCS (stages 1 & 2, 30–40 MPa), original cracks compress and close; areal porosity drops (e.g., from 1.44% to 0.97%) and volumetric porosity drops slightly (from 0.39% to 0.34%). [Fan 2023, pp. 7-9]
  - When σ_max reaches 46.04% UCS (stage 3, 50 MPa), large cracks parallel to loading generate; average areal porosity jumps from 0.97% → 5.92% (+311.11%), volumetric porosity from 0.34% → 6.87% (+1661.54%). [Fan 2023, pp. 7-9]
  - At stage 4 (60 MPa), sample fails after 28 cycles; multiple macroscopic failed planes form; areal porosity reaches 41.45%, volumetric porosity 47.70%. [Fan 2023, pp. 7-9]
- **Single‑level cycling at crack initiation stress (46.04% UCS)**
  - Areal porosity of the three vertical sections increases monotonically with cycle number. The most rapid increase occurs in the first 20 cycles (e.g., section 3 from 0.44% → 3.08%). [Fan 2023, pp. 9-11]
  - Volumetric porosity increases monotonically: 0.43% → 1.67% (cycles 0–20, +288.37%), then slows (1.67% → 2.01% by cycle 100, +20.36%), then accelerates again (2.63% → 3.79% by cycle 300). [Fan 2023, pp. 11-14]
  - 3D reconstructions show a penetrating crack forms early (first 20 cycles), then small cracks expand and connect with it, eventually leading to a larger penetrating crack. [Fan 2023, pp. 11-13]
- **Methodological highlight**: Real‑time CT technology can intuitively and continuously capture the progressive fatigue deterioration of granite under cyclic loading. [Fan 2023, pp. 1-2, 14]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Average areal porosity decreased from 1.44% to 0.97% during multi‑level stages 1–2 (σ_max ≤40 MPa) and then surged to 41.45% at failure. | [Fan 2023, pp. 7-9] | σ_min = 20 MPa, 100 cycles per level; dry granite, 20 °C, displacement control 0.02 mm/min. | Crack closure dominates at low stress; sudden failure at σ_max = 60 MPa. |
| Volumetric porosity went from 0.39% (initial) to 0.34% (stage 2) to 47.70% (failure). | [Fan 2023, pp. 7-9] | Same multi‑level loading conditions. | A 1661.54% increase relative to initial when σ_max reaches 50 MPa (stage 3). |
| Under single‑level loading at crack initiation stress (46.04% UCS), volumetric porosity increased 288.37% in the first 20 cycles (0.43%→1.67%). | [Fan 2023, pp. 11-14] | σ_min = 20 MPa, 300 cycles; same granite and environment. | Most fatigue damage concentrates in early cycles. |
| 3D reconstruction showed a penetrating large crack formed by cycle 20; later cycles mainly caused expansion and coalescence of small cracks. | [Fan 2023, pp. 11-13] | Single‑level loading, analysed cylinder Φ 6 mm × 7.855 mm. | Visual tracking of crack initiation, growth, and connection. |

## Limitations
- The CT scanning resolution (15.71 μm) limits the detection of finer microcracks and pores; smaller damage features may be missed. [Fan 2023, pp. 4-5]
- Sample size is very small (diameter 6.0 mm, height 12.0 mm), which may not fully capture the heterogeneous behaviour of field‑scale rock masses. [Fan 2023, pp. 3-4]
- Only one rock type (granite from Hunan) was tested under dry conditions at 20 °C; the influence of moisture, temperature variations, or different lithologies was not investigated within this study. [Fan 2023, pp. 2-4]
- The selection of the analyzed region excluded end‑affected slices, which may omit some boundary effects on cracking. [Fan 2023, pp. 4-7]

## Assumptions / Conditions
- The sample was dried at 105 °C for 48 h before testing. [Fan 2023, pp. 3-4]
- Ambient temperature was held constant at 20 °C throughout the experiments. [Fan 2023, pp. 3-4]
- Loading was displacement‑controlled at a constant rate of 0.02 mm/min for both loading and unloading. [Fan 2023, pp. 4-5]
- The minimum cyclic stress was fixed at 20.0 MPa in all cyclic loading protocols. [Fan 2023, pp. 4-5]
- CT imaging was always performed while the sample was subjected to the minimum cyclic stress, avoiding unloading rebound effects. [Fan 2023, pp. 3-4]
- Voxel counts for damage and matrix were converted to volumes by multiplying by the voxel volume (15.71 μm³); porosity was defined as the percentage of damaged volume (or area) over total volume (or area). [Fan 2023, pp. 5-9]

## Key Variables / Parameters
- **Maximum cyclic stress** (σ_max): multi‑level stages 30, 40, 50, 60 MPa; single‑level fixed at crack initiation stress (~50 MPa, i.e. 46.04% UCS). [Fan 2023, pp. 4-5, 9]
- **Cyclic number** (*N*): multi‑level 100 cycles per stage; single‑level up to 300 cycles. [Fan 2023, pp. 4-5]
- **Areal porosity** (*P*_s): measured on three vertical sections (0°, 120°, 240°). [Fan 2023, pp. 5-7]
- **Volumetric porosity** (*P*_v): measured on the 3D analysed cylinder (Φ 6 mm × 7.855 mm). [Fan 2023, pp. 7-9]
- **Crack initiation stress**: determined as 46.04% UCS from the multi‑level test (the stress level at which porosity begins to increase rapidly). [Fan 2023, pp. 9]

## Reusable Claims
- For the tested dry granite, when maximum cyclic stress is below approximately 46% UCS, cyclic loading mainly causes closure of original cracks, and the overall porosity remains nearly constant (slight decrease). [Fan 2023, pp. 7-9]
- Once the maximum cyclic stress reaches or exceeds the crack initiation stress (identified as ~46% UCS in this case), a sharp increase in both areal and volumetric porosity occurs, accompanied by the generation of large cracks parallel to the loading direction. [Fan 2023, pp. 7-9]
- Under constant‑amplitude cyclic loading at the crack initiation stress, a few cycles (≤20) can cause significant crack initiation and a large porosity jump (e.g., volumetric porosity increase of ~288%). [Fan 2023, pp. 11-14]
- Under the same conditions, after the initial rapid damage phase, further cycling (20–100 cycles) causes much smaller porosity increments, indicating a relatively stable internal structure before a later acceleration phase. [Fan 2023, pp. 11-14]
- Real‑time CT scanning with a resolution of 15.71 μm can visually and continuously track the progressive fatigue deterioration of granite, including crack closure, generation, expansion, and coalescence. [Fan 2023, pp. 1-2, 14]

## Candidate Concepts
- [[real-time CT technology]] – Continuous X‑ray computed tomography during mechanical loading to observe damage evolution visually. [Fan 2023, pp. 1-3]
- [[areal porosity]] – Percentage of damaged area in a 2D CT slice used to quantify planar damage. [Fan 2023, pp. 5-7]
- [[volumetric porosity]] – Percentage of damaged volume in a 3D region used to quantify spatial damage. [Fan 2023, pp. 7-9]
- [[crack initiation stress]] – The threshold cyclic stress above which microcracking begins to dominate over crack closure, identified as 46.04% UCS for this granite. [Fan 2023, pp. 9]
- [[multi-level cyclic loading]] – A stepped increase in maximum cyclic stress while keeping the minimum stress constant. [Fan 2023, pp. 4-5]
- [[single-level cyclic loading]] – Cyclic loading with a constant amplitude equal to the crack initiation stress. [Fan 2023, pp. 4-5]
- [[fatigue deterioration mechanism]] – The progressive internal damage process of rock under repeated loading. [Fan 2023, pp. 1-2]

## Candidate Methods
- [[real-time CT scanning under cyclic loading]] – Simultaneous CT imaging and cyclic mechanical loading to capture microstructure changes continuously. [Fan 2023, pp. 3-5]
- [[digital image processing for porosity analysis]] – Thresholding and voxel counting on CT slices to separate microdefects from matrix and compute area/volume fractions. [Fan 2023, pp. 4-7]
- [[3D reconstruction of rock damage]] – Colouring individual cracks and pores in different colours to visualise damage evolution in 3D. [Fan 2023, pp. 11-13]
- [[crack initiation stress determination from porosity data]] – Using the sharp increase of volumetric or areal porosity to pinpoint the stress at which microcracking becomes dominant. [Fan 2023, pp. 9]
- [[X-ray diffraction (XRD) for mineral identification]] – Quantitative mineralogy before mechanical testing. [Fan 2023, pp. 3-4]

## Connections To Other Work
- This study extends prior macroscopic cyclic loading investigations (e.g., Bagde & Petros 2005; Cerfontaine & Collin 2018; Liu & Dai 2021) by providing real‑time micro‑scale visualisation of the deterioration process. [Fan 2023, pp. 1-2]
- It builds on existing CT‑based rock mechanics studies that have mainly focused on post‑failure crack patterns (Yang et al. 2020) or uniaxial compression (Duan et al. 2019; Gao et al. 2021), and demonstrates that real‑time CT can capture progressive fatigue evolution, filling a recognised gap. [Fan 2023, pp. 2-3]
- The observed importance of the first few cycles on damage accumulation is consistent with the concept that fatigue life is strongly influenced by early crack initiation, a point relevant to injection‑induced seismicity and fatigue hydraulic fracturing (Zang et al. 2013; Ji et al. 2021). [Fan 2023, pp. 1-2, 14]

## Open Questions
- The paper does not explicitly propose future research directions or open questions within the provided fragments. Based on the experimental scope, one could ask how the findings extend to other rock types, saturated conditions, different loading frequencies or waveforms, but no such statements appear in the indexed material. [Fan 2023, pp. 1-14]

## Source Coverage
All non‑empty indexed fragments (11 source blocks, 52,867 characters) were processed. Compiled coverage: 100% of source blocks, 99.17% of source characters. The complete content of the paper (excluding only trivial formatting elements) is included in this page.
