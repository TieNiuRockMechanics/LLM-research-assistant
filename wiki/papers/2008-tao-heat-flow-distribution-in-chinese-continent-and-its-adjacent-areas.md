---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2008-tao-heat-flow-distribution-in-chinese-continent-and-its-adjacent-areas"
title: "Heat Flow Distribution in Chinese Continent and Its Adjacent Areas."
status: "draft"
source_pdf: "data/papers/2008 - Heat flow distribution in Chinese continent and its adjacent areas.pdf"
collections:
  - "山西断裂地质构造"
citation: "Tao, Wei, and Zhengkang Shen. “Heat Flow Distribution in Chinese Continent and Its Adjacent Areas.” *Progress in Natural Science*, vol. 18, 2008, pp. 843-49. doi:10.1016/j.pnsc.2008.01.018."
indexed_texts: "7"
indexed_chars: "32054"
nonempty_source_blocks: "7"
compiled_source_blocks: "7"
compiled_source_chars: "32192"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004305"
coverage_status: "full-index"
source_signature: "3d6d62178baea40e07d8af1a3854d2c50f85ba20"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T13:21:14"
---

# Heat Flow Distribution in Chinese Continent and Its Adjacent Areas.

## One-line Summary
An updated heat flow map for the Chinese continent and adjacent areas, derived from 6980 measurements using an interpolation method that combines data quality and distance weighting with characteristic heat flow values constrained by active tectonic blocks.

## Research Question
How can a more complete and reliable heat flow map be produced for the Chinese continent and its adjacent areas, given unevenly distributed and sparse measurements, by optimally utilizing all available data and a priori geological constraints?

## Study Area / Data
Chinese continent and its adjacent areas (within a yellow frame in Fig. 1). A total of 6980 heat flow measurements were compiled, of which 4282 lie inside the study region. Data sources include:
- Chinese heat flow collections (816 observations, redundant with global database removed) [Tao 2008, pp. 1-2]
- Global heat flow database (5485 observations) [Tao 2008, pp. 1-2]
- Recent Chinese publications (547 observations) [Tao 2008, pp. 2]
- Japan and India papers post‑1993 (132 observations) [Tao 2008, pp. 2]
1363 heat flow data are from China. Data quality classified into A (high), B (intermediate), C (low/unidentified), D (abnormal). In the 6980 dataset, A: 79.8%, B: 14.6%, C: 4.7%, D: 0.9%. [Tao 2008, pp. 2]

## Methods
1. **Outlier detection** – A distance‑weighted prediction (Eq. 1) was used with a characteristic decay distance \( r_0 = 14.3 \) km, estimated by fitting Eq. (2) to binned heat‑flow differences. Data with a measured‑to‑predicted difference > 200 mW/m² were removed. The cleaning screened out 76 outliers, leaving 6904 points. [Tao 2008, pp. 2-4]

2. **Geological unit framework** – The study area was divided into 41 geological units based on Zhang et al.’s active tectonic block model. For 32 units with data, characteristic heat flow was computed as a quality‑weighted mean (Eqs. 3–4). For 9 units without data, it was approximated as the mean of neighbouring units’ characteristic values. [Tao 2008, pp. 4-5]

3. **Grid interpolation** – Heat flow on a \(1^\circ \times 1^\circ\) grid was estimated by combining a locally interpolated value \(Q_r\) (distance and quality weights, Eq. 6) and the characteristic heat flow of the geological unit \(\overline{Q}\), with a weighting factor \(X\) (Eq. 5). A grid search minimising residual \(v^2\) gave \(X = 15\%\), i.e. 87% contribution from neighbourhood data smoothing and 13% from geological‑unit constraining. [Tao 2008, pp. 4-5]

4. **Resolution map** – A resolution function \(R\) (Eq. 7) based on the sum of distance‑and‑quality weights was mapped to show reliability. [Tao 2008, pp. 5]

## Key Findings
- Heat flows in the eastern part of the Chinese continent are relatively higher than in the western part, except for the Tibetan Plateau area. [Tao 2008, pp. 1]
- Ordos and North China blocks: ~60 mW/m². South China (excluding continental marginal seas): 50–55 mW/m². [Tao 2008, pp. 1]
- Junggar Basin: lowest, 35–45 mW/m². Tarim Basin: 45–55 mW/m². [Tao 2008, pp. 1]
- Continental marginal seas east of China: high heat flow >80 mW/m² with high resolution, comparable to oceanic plate. [Tao 2008, pp. 5]
- Southern and central Tibetan Plateau: >75 mW/m², but derived from limited data along a highway; resolution low in much of the plateau. [Tao 2008, pp. 5-6]
- Qaidam Basin (northern Tibetan Plateau): 35–40 mW/m², high resolution. [Tao 2008, pp. 6]
- Northeast China and Mongolia: heat flows variable; 60–70 mW/m² in Russia and northern Mongolia; 45–60 mW/m² in Northeast China (mainly Songliao Basin). [Tao 2008, pp. 6]
- Overall pattern: high values in the east and southwest, low values in the central and northwestern parts, consistent with previous studies but with improved methodology and data volume. [Tao 2008, pp. 6-7]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Total dataset: 6980 measurements, of which 4282 in study region; outlier cleaning removed 76, leaving 6904. | [Tao 2008, pp. 2-4] | Global database, Chinese compilations, recent papers; quality classification A–D used. | Chinese data: 1363 points. |
| Characteristic decay distance \( r_0 = 14.3 \) km for heat‑flow difference correlation. | [Tao 2008, pp. 3-4] | Estimated from binned data pairs 0–300 km; bin width 1 km. | Used in outlier detection and interpolation. |
| Interpolation combines distance‑ and quality‑weighted local estimate (87%) with characteristic heat flow of geological unit (13%). | [Tao 2008, pp. 4-5] | Optimal \( X = 15\% \) from grid search minimising v². | Grid nodes on \(1^\circ \times 1^\circ\) spacing. |
| Eastern China (Ordos/North China) heat flow ~60 mW/m²; South China 50–55 mW/m² (excl. marginal seas). | [Tao 2008, pp. 1] | From final interpolated map; resolution moderate to high. | Consistent with previous studies. |
| Junggar Basin: 35–45 mW/m²; Tarim Basin: 45–55 mW/m². | [Tao 2008, pp. 1] | Derived from interpolated map. | Junggar is the lowest in the study area. |
| Tibetan Plateau (southern/central) >75 mW/m², but low resolution in large areas. | [Tao 2008, pp. 5-6] | Data concentrated along highway; caution needed. | May include frictional heating from the Indo‑Asia collision. |
| Marginal seas east of China >80 mW/m² with high resolution. | [Tao 2008, pp. 5] | Abundant data from Japanese islands and Japan Sea. | Comparable to typical oceanic heat flow. |
| Resolution map shows reliable estimates in Ordos, North China, South China (north), Yinshan, Chuandian (south), western Yunnan, eastern Tianshan, central Qaidam, Qilian blocks. Less reliable in Lhasa, Qiangtang, Bayan Har, Alxa, northern NE China blocks, Yellow Sea, parts of India plate. | [Tao 2008, pp. 5] | Based on density and quality of data within a certain radius. | Resolution function \( R \) defined in Eq. 7. |
| Overall pattern (high east/southwest, low central/northwest) matches Hu et al. (2000) and Wang et al. (1999). | [Tao 2008, pp. 6-7] | Comparison with previous Chinese heat flow maps. | This study uses larger dataset and refined interpolation. |

## Limitations
- Data are sparse and unevenly distributed, especially in western China (Lhasa, Qiangtang, Bayan Har, Alxa blocks) leading to low resolution there. [Tao 2008, pp. 2, 5]
- Yellow Sea data were unavailable and excluded. [Tao 2008, pp. 6-7]
- Nine geological units had no in‑situ measurements; their characteristic heat flows were approximated from neighbours. [Tao 2008, pp. 4]
- Outlier detection may discard valid local geothermal anomalies that do not represent regional heat flow. [Tao 2008, pp. 3]
- The thermal contribution of frictional heating along the Indo‑Asia subduction interface remains poorly understood, limiting interpretation of high Tibetan heat flows. [Tao 2008, pp. 6]

## Assumptions / Conditions
- Measured heat flow differences at close distance reflect either measurement failure or local anomalies that should be treated as outliers (spatial coherency assumption). [Tao 2008, pp. 3]
- Heat flow within a tectonic block is similar due to shared latest tectono‑thermal reactivation history; the active tectonic block model of Zhang et al. (2003) adequately captures that control. [Tao 2008, pp. 2, 6‑7]
- The distance‑weighting function and characteristic decay distance \( r_0 = 14.3 \) km are representative for the entire study area. [Tao 2008, pp. 3-4]
- The weighting factor \( X = 15\% \) (from minimising residuals) optimally balances local data interpolation and geological‑unit constraining. [Tao 2008, pp. 5]
- Data quality categories (A–D) as assigned in the Chinese heat flow compilations accurately reflect reliability. [Tao 2008, pp. 2, 4]

## Key Variables / Parameters
- \( Q \): heat flow value (mW/m²) [Tao 2008, pp. 4]
- \( r_0 = 14.3 \) km: characteristic decay distance for distance weighting [Tao 2008, pp. 3-4]
- \( X = 15\% \): weighting factor for geological‑unit characteristic heat flow in final interpolation [Tao 2008, pp. 5]
- \( \omega_{i,1} \): distance weighting function, \( \omega_{i,2} \): data quality weighting (A=4, B=2, C=1, D=0) [Tao 2008, pp. 3, 4]
- \( \overline{Q} \): characteristic heat flow of a geological unit [Tao 2008, pp. 4]
- \( R \): resolution, log‑scale sum of composite weights [Tao 2008, pp. 5]
- Number of geological units: 41, of which 32 have in‑situ data [Tao 2008, pp. 4]

## Reusable Claims
- The characteristic decay distance for heat‑flow spatial correlation in the Chinese continent and adjacent areas is 14.3 km, derived from 6980 measurements. [Tao 2008, pp. 3-4]; condition: using data pairs binned at 1 km intervals up to 300 km distance; may vary with regional data coverage.
- Heat flow in the Junggar Basin is 35–45 mW/m², the lowest in the study area. [Tao 2008, pp. 1]; condition: based on the 2008 compilation and interpolation; resolution moderate.
- Heat flow in the Ordos and North China blocks is around 60 mW/m². [Tao 2008, pp. 1]; condition: derived from interpolated map with relatively high resolution.
- Eastern China heat flow is systematically higher than western China except for the Tibetan Plateau, which also shows high values (>75 mW/m²). [Tao 2008, pp. 1]; condition: western China resolution is generally low; regional averages may mask local variability.
- An interpolation that combines distance‑weighted local data (87%) with a geological‑unit characteristic heat flow (13%) yields minimal residuals for this dataset. [Tao 2008, pp. 5]; condition: weight \(X\ determined by grid search; applicable when active tectonic block model is used.)
- The global heat‑flow correlation with latest tectono‑thermal reactivation age can be effectively implemented in China using Zhang et al.’s active tectonic block subdivision. [Tao 2008, pp. 2, 7]; condition: the model represents Cenozoic to present deformation; may not capture all local thermal disturbances.

## Candidate Concepts
- [[heat flow distribution]]
- [[active tectonic blocks]]
- [[geological unit constrained interpolation]]
- [[characteristic heat flow of tectonic units]]
- [[spatial coherence of heat flow]]
- [[outlier detection in geothermal datasets]]
- [[resolution map for heat flow models]]
- [[tectono-thermal reactivation age]]

## Candidate Methods
- [[distance-weighted interpolation with data quality weights]]
- [[characteristic decay distance estimation from heat flow differences]]
- [[grid search for weighting parameter in combined interpolation]]
- [[quality-weighted mean for geological unit heat flow]]
- [[spatial outlier screening using prediction residuals]]

## Connections To Other Work
- Builds on the global heat flow analysis of Pollack et al. (1993) and their finding that conductive heat flow correlates inversely with latest tectono‑thermal reactivation age. [Tao 2008, pp. 2]
- Uses the active tectonic block model of Zhang et al. (2003) for China as the basis for geological units, instead of traditional orogenic‑age‑based subdivisions. [Tao 2008, pp. 2, 7]
- Directly extends and updates previous Chinese heat flow maps by Wang (1996), Hu et al. (2000), Wang et al. (1999), and He et al. (2001, 2002). The overall pattern remains consistent, but the present work provides a much larger compilation (6980 vs. < 3000 data points) and a more rigorous, objective interpolation method. [Tao 2008, pp. 6-7]
- The final product (heat flow values on a \(1^\circ \times 1^\circ\) grid, contour map, and resolution map) is intended as input for lithospheric thermal and rheological modelling (e.g. Artemieva & Mooney 2001, Fukahata & Matsu’ura 2001). [Tao 2008, pp. 1, 7]

## Open Questions
- What are the true regional heat flow values in the data‑sparse western blocks (Lhasa, Qiangtang, Bayan Har, Alxa)? Additional field measurements are needed. [Tao 2008, pp. 5]
- How much frictional heating along the Indo‑Asia subduction interface contributes to the elevated heat flow in Tibet, and how does it vary spatially? [Tao 2008, pp. 6]
- Can the resolution of the heat flow map be improved by incorporating indirect geophysical indicators (e.g. Curie depth, seismic attenuation) into the interpolation? (Not addressed in this paper, but implied as a future direction.)
- What is the effect of using different tectonic subdivision schemes on the interpolated heat flow pattern? The active tectonic block model was chosen; comparison with other models could be tested. [Tao 2008, pp. 7]

## Source Coverage
All 7 non‑empty indexed fragments were processed.  
- Indexed texts: 7  
- Nonempty source blocks: 7  
- Compiled source blocks: 7  
- Compiled source characters: 32,192 (coverage ratio by chars: 1.004305, by blocks: 1.0)  

No content beyond the indexed fragments was used. This page is evidence for RAG and not a polished literature review. Facts not explicitly supported by the fragments are indicated as not confirmed.
