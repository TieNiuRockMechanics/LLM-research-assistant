---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2009-iassonov-segmentation-of-x-ray-computed-tomography-images-of-porous-materials-a-crucial-ste"
title: "Segmentation of X-Ray Computed Tomography Images of Porous Materials: A Crucial Step for Characterization and Quantitative Analysis of Pore Structures."
status: "draft"
source_pdf: "data/papers/2009 - Segmentation of X-ray computed tomography images of porous materials A crucial step for characterization and quantitative analysis of pore structures.pdf"
collections:
  - "论文"
citation: "Iassonov, Pavel, et al. “Segmentation of X-Ray Computed Tomography Images of Porous Materials: A Crucial Step for Characterization and Quantitative Analysis of Pore Structures.” *Water Resources Research*, vol. 45, 2009, W09415, doi:10.1029/2009WR008087. Accessed 15 Sept. 2026."
indexed_texts: "17"
indexed_chars: "81537"
nonempty_source_blocks: "17"
compiled_source_blocks: "17"
compiled_source_chars: "81952"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.00509"
coverage_status: "full-index"
source_signature: "41d1e2ba5a397978661cb9dae92cc96ce4205ca1"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T13:48:29"
---

# Segmentation of X-Ray Computed Tomography Images of Porous Materials: A Crucial Step for Characterization and Quantitative Analysis of Pore Structures.

## One-line Summary
This study evaluates 14 segmentation methods for X-ray computed tomography (CT) images of porous materials and demonstrates that methods utilizing local spatial information (especially indicator kriging and Markov random fields) yield significantly more accurate porosity estimates than global thresholding, though automation without operator bias remains a critical need.

## Research Question
How do various global and locally adaptive image segmentation methods perform for converting gray-scale X-ray CT volumes of porous media into discrete binary images, and what are the implications for quantitative characterization of pore structures?

## Study Area / Data
- Industrial X-ray CT (HYTEC FLASHCT™, 180 μm resolution) images of three material sets: precision glass beads (2.5 mm, 3.5 mm, 6.5 mm diameter), Wyoming bentonite–F35 Ottawa silica sand mixtures (dehydrating crack networks), and undisturbed macroporous Tyler loam soil columns (110 μm resolution).  
- Synchrotron microtomography (GSECARS beamline 13, 5.9 μm resolution) images of uniform glass beads provided by Dorthe Wildenschild (Oregon State University).  
[Iassonov 2009, pp. 5-6]

## Methods
**Segmentation algorithms tested** (14 methods):  
- **Global thresholding**: HS‑Zack, HS‑Tsai, CL‑Kittler, CL‑Otsu, CL‑Ridler, EN‑Kapur, EN‑Yen, SP‑Chen, SP‑Pal, and manual thresholding.  
- **Locally adaptive**: LA‑Kriging (indicator kriging by Oh & Lindquist, 1999), PCM‑Pham (probabilistic fuzzy c‑means), ED‑Yanowitz (edge detection + surface fitting), CAC‑Sheppard (converging active contours), MRF‑Berthod (supervised Markov random field segmentation).  

**Image processing**: FLASHCT™ data were corrected for large‑scale intensity variations (Iassonov & Tuller, 2009). Median filtering (3×3×3) was applied unless otherwise noted. All processing was full 3‑D; no slice‑by‑slice methods were used.  

**Quantitative evaluation**: Porosity was computed by voxel counting and compared to physically measured values for glass beads and manual segmentation for soil/bentonite samples. Noise in binary volumes was estimated via majority‑filter differences.  
[Iassonov 2009, pp. 5-8]

## Key Findings
1. **Global thresholding** – Only CL‑Otsu and CL‑Ridler produced consistent porosities across most samples. All other global methods, especially entropy‑based ones, failed for low‑contrast or unimodal‑like histograms. [Iassonov 2009, pp. 9]  
2. **Locally adaptive methods** consistently outperformed global ones in accuracy and noise tolerance. [Iassonov 2009, pp. 9]  
3. **Best overall**: MRF‑Berthod (supervised Bayesian) achieved 1.3 % average error in porosity and robust multiphase segmentation, but required manual class initialization and had the highest computational cost. [Iassonov 2009, pp. 9]  
4. **Second best**: LA‑Kriging (2.4 % average error) was computationally efficient but highly dependent on the two initial global thresholds. [Iassonov 2009, pp. 9]  
5. **PCM‑Pham** performed similarly to LA‑Kriging with less initialization sensitivity, but the basic c‑means kernel misclassified non‑equidistant clusters (e.g., dense aggregates in soil). [Iassonov 2009, pp. 9-10]  
6. **ED‑Yanowitz** uniquely handled beam‑hardening artifacts, but required extensive smoothing and was limited to two‑phase systems. [Iassonov 2009, pp. 10]  
7. **CAC‑Sheppard** (converging active contours) gave variable results (4.4 % error) and was extremely sensitive to initial thresholds and speed‑function parameters, demanding trial‑and‑error. [Iassonov 2009, pp. 10]  
8. Utilization of **local spatial information** (covariance, indicator kriging, MRF) is crucial for high‑quality segmentation; manual supervision remains a major limitation for fully automated workflows. [Iassonov 2009, pp. 9-10]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Porosity values for 14 methods on glass beads, soil, and bentonite‑sand (Table 2). Only CL‑Otsu and CL‑Ridler gave results close to measured porosity among global methods. | [Iassonov 2009, pp. 7-8, Table 2] | Data corrected for intensity distortion; median filter 3×3×3; full 3‑D processing. | Measured porosities: 0.366 (2.5 mm beads), 0.378 (3.5 mm), 0.374 (6.5 mm), 0.508 (synchrotron beads). |
| Noise tolerance of adaptive methods on unfiltered CT (Table 3). LA‑Kriging, PCM‑Pham, CAC‑Sheppard, MRF‑Berthod all produced noise fractions ≤1.13 % vs. 2.57 % for manual. | [Iassonov 2009, pp. 8-9, Table 3] | Unfiltered FLASHCT™ macroporous soil (180 μm) and synchrotron glass beads (5.9 μm). | MRF‑Berthod showed lowest noise (0.46 % and 0.08 %). |
| ED‑Yanowitz successfully segmented images with pronounced beam‑hardening, where global CL‑Otsu failed (Figure 7). | [Iassonov 2009, pp. 10] | 3.5 mm glass bead CT with severe beam hardening. | ED‑Yanowitz relies solely on edge information, thus inherently sensitive to noise. |
| MRF‑Berthod could segment three phases (pores, solid, dense aggregates) in macroporous soil, while PCM‑Pham misclassified the dense aggregate phase (Figure 6). | [Iassonov 2009, pp. 9-10] | Supervision via manually selected representative regions for each class. | PCM‑Pham limited by equidistant cluster assumption. |

## Limitations
- **Lack of ground truth** – optimal binarization is unknown; evaluation relied on bulk porosity and visual inspection.  
- **Manual bias** – supervised methods (MRF‑Berthod, LA‑Kriging initialization) require skilled operators; manual thresholding is inconsistent.  
- **Method‑specific weaknesses**: MRF‑Berthod is computationally expensive and supervised; PCM‑Pham fails for non‑equidistant cluster centers; ED‑Yanowitz demands smoothing and is only for two phases; CAC‑Sheppard needs extensive parameter tuning.  
- **Image artifacts** – only intensity‑correction and median filtering were applied; effects of advanced filtering were not systematically studied.  
- **Sample scope** – tested on glass beads, sand‑bentonite, and one loam soil; transferability to other porous materials (e.g., rocks) not demonstrated.  
[Iassonov 2009, pp. 2, 8‑10]

## Assumptions / Conditions
- All FLASHCT™ images were corrected for smooth intensity variations before segmentation (Iassonov & Tuller, 2009).  
- Median filtering (3×3×3) was used for filtered‑data comparisons; unfiltered data were compared separately for noise evaluation.  
- Full 3‑D processing was applied; 2‑D slice‑by‑slice methods are considered inferior because they neglect neighbourhood information.  
- Porosity of glass beads was assumed to be accurately known from gravimetric and container‑volume measurements; for soil and bentonite, manual segmentation was used as a proxy benchmark.  
[Iassonov 2009, pp. 5, 7‑8]

## Key Variables / Parameters
- **Porosity** (image‑derived vs. measured) – primary evaluation metric.  
- **Segmentation method** – 9 global + 5 locally adaptive algorithms.  
- **CT resolution** – 180 μm (industrial) and 5.9 μm (synchrotron).  
- **Material** – glass beads, sand‑bentonite mixture, macroporous soil.  
- **Noise fraction** – percentage of voxels altered by majority filtering.  
- **Beam hardening** – evaluated qualitatively via ED‑Yanowitz.  
[Iassonov 2009, pp. 7-9]

## Reusable Claims
1. **Local spatial information is essential** – “Utilization of local image information such as spatial correlation as well as the application of locally adaptive techniques yielded significantly better results,” valid for both industrial and synchrotron CT of unconsolidated granular media, provided basic intensity corrections are applied. [Iassonov 2009, pp. 1, 10]  
2. **CL‑Otsu and CL‑Ridler are the most reliable global thresholds** – Among unsupervised global methods, only these two clustering‑based algorithms consistently approach measured porosity across diverse samples, but they still fail under severe beam hardening or unimodal histograms. [Iassonov 2009, pp. 9]  
3. **LA‑Kriging balances accuracy and efficiency** – The two‑stage indicator kriging method (Oh & Lindquist, 1999) achieves a 2.4 % average porosity error when initialized with CL‑Ridler thresholds, but its quality is sensitive to the choice of the initial bounding thresholds T₀ and T₁. [Iassonov 2009, pp. 9]  
4. **MRF‑Berthod gives the highest accuracy but needs supervision** – The supervised Markov random field method yields the lowest error (1.3 %) and handles multiphase systems, yet requires manual selection of representative class statistics and carries a heavy computational burden. [Iassonov 2009, pp. 9]  
5. **ED‑Yanowitz handles beam hardening at the cost of generality** – Because it relies exclusively on edge information, it segments images with strong intensity inhomogeneities but is inherently noise‑sensitive and limited to two‑phase objects. [Iassonov 2009, pp. 10]  
6. **Full 3‑D processing avoids directional bias** – Slice‑by‑slice 2‑D segmentation neglects critical neighbourhood information and can lead to misclassification; 3‑D processing is strongly recommended. [Iassonov 2009, pp. 8]  
7. **Noise tolerance of adaptive methods** – Locally adaptive techniques (LA‑Kriging, PCM‑Pham, MRF‑Berthod, etc.) produce binary volumes with <1.2 % noise even without prior filtering, making them suitable for low‑quality CT data. [Iassonov 2009, pp. 9, Table 3]

## Candidate Concepts
- [[X-ray computed tomography]]
- [[image segmentation]]
- [[porous media]]
- [[global thresholding]]
- [[locally adaptive segmentation]]
- [[beam hardening]]
- [[indicator kriging]]
- [[Markov random field]]
- [[fuzzy c-means]]
- [[converging active contours]]
- [[two-phase segmentation]]
- [[multiphase segmentation]]
- [[porosity]]
- [[voxel classification]]
- [[partial volume effect]]

## Candidate Methods
- [[CL-Otsu]]
- [[CL-Ridler]]
- [[LA-Kriging]]
- [[MRF-Berthod]]
- [[PCM-Pham]]
- [[ED-Yanowitz]]
- [[CAC-Sheppard]]
- [[HS-Zack]]
- [[HS-Tsai]]
- [[CL-Kittler]]
- [[EN-Kapur]]
- [[EN-Yen]]
- [[SP-Chen]]
- [[SP-Pal]]
- [[manual thresholding]]
- [[median filtering]]
- [[intensity correction for CT]]

## Connections To Other Work
- **Oh & Lindquist (1999)** – indicator kriging method (LA‑Kriging).  
- **Berthod et al. (1996)** – supervised MRF segmentation.  
- **Sheppard et al. (2004)** – converging active contours (CAC‑Sheppard).  
- **Pham (2001)** – probabilistic fuzzy c‑means (PCM‑Pham).  
- **Yanowitz & Bruckstein (1989)** – edge‑detection‑based adaptive thresholding (ED‑Yanowitz).  
- **Otsu (1979)**, **Ridler & Calvard (1978)** – commonly used global clustering methods.  
- **Kaestner et al. (2008)** – review of image filtering for porous‑media CT.  
- **Ketcham & Carlson (2001)** – fundamentals and artifacts of X‑ray CT.  
- **Wildenschild et al. (2002)** – review of CT in hydrology.  
[Iassonov 2009, pp. 1-2, 4, 10‑12]

## Open Questions
- How can unsupervised, data‑driven MRF methods be adapted to reduce operator bias while maintaining accuracy?  
- What are the optimal filtering strategies prior to segmentation for different CT sources and materials?  
- Can hybrid methods that combine fast global initialization with local refinement achieve fully automated, high‑quality segmentation across diverse porous media?  
- In multiphase systems (e.g., water, air, NAPL), how do segmentation errors propagate into fluid‑distribution and flow simulations?  
- How do segmentation choices affect pore‑network parameters beyond porosity (specific surface area, tortuosity, connectivity)?  
[Iassonov 2009, pp. 1, 9‑10]

## Source Coverage
All 17 non‑empty indexed source blocks were processed. The compiled page captures 17 source fragments (81,952 characters), representing **100 %** of the non‑empty source blocks and a coverage ratio of **1.005** by characters (due to slight formatting overhead). No content was omitted.
