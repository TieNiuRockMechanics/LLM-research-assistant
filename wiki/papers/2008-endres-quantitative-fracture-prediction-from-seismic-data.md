---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2008-endres-quantitative-fracture-prediction-from-seismic-data"
title: "Quantitative Fracture Prediction from Seismic Data."
status: "draft"
source_pdf: "data/papers/Quantitative fracture prediction from seismic data.pdf"
collections:
citation: "Endres, H., et al. \"Quantitative Fracture Prediction from Seismic Data.\" *Petroleum Geoscience*, vol. 14, 2008, pp. 369-377, doi:10.1144/1354-079308-751."
indexed_texts: "7"
indexed_chars: "33872"
nonempty_source_blocks: "7"
compiled_source_blocks: "7"
compiled_source_chars: "34032"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004724"
coverage_status: "full-index"
source_signature: "fd1eb10f70f550bd57a7bd06e31f5f13c4c79645"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:42:49"
---

# Quantitative Fracture Prediction from Seismic Data.

## One-line Summary
This study develops and applies advanced seismic coherency processing and fractal dimension analysis to quantitatively predict sub-seismic fracture density from 3D seismic data, calibrated with borehole image logs in a North German gas field.

## Research Question
How can quantitative fracture density at sub-seismic scale be predicted from seismic data in a reservoir where fractures act as permeability barriers? [Endres 2008, pp. 1-2]

## Study Area / Data
The study area is a producing gas field located east of Bremen in the North German Basin (NW Germany). The reservoir is deep Rotliegend sandstone at depths of 4500-4800 m. The database consists of a 3D pre-stack depth-migrated seismic dataset (PSDM) with 25 m inline/crossline spacing and 4 ms sample rate, covering an area of about 10 x 210 km. Thirteen wells provide petrophysical data, core sections, and borehole images (FMI/FMS) for calibration. [Endres 2008, pp. 1-3]

## Methods
1.  **Advanced Coherency Processing:** New coherency algorithms (shaded relief, structural entropy) and IHS (Intensity, Hue, Saturation) display were applied to the seismic data to enhance the imaging of subtle tectonic lineaments beyond standard coherency displays. [Endres 2008, pp. 2-4]
2.  **Fault Attribute Analysis:** Faults and lineaments were interpreted on the Top A2 horizon. Attributes including fault density by count, fault density by length, and fault connectivity were calculated using a 1.8 km search window. [Endres 2008, pp. 4-6]
3.  **Fractal Dimension (FD) Analysis:** The fractal dimension of the cumulative fault length distribution was calculated from seismic data to characterize the fault population. FD values were computed on a 1.5 km grid across the study area. [Endres 2008, pp. 6-7]
4.  **Geostatistical Analysis:** A linear relationship between seismic-scale fault density and borehole image-scale fracture density was established. This relationship was used in collocated cokriging and Gaussian simulation to predict the areal distribution of normalized fracture density at borehole scale and to assess the probability of low fracture density areas. [Endres 2008, pp. 7-8]

## Key Findings
1.  Advanced coherency processing (IHS, shaded relief, structural entropy) significantly improved the detection of small-scale tectonic lineaments compared to conventional seismic amplitude or coherency displays. [Endres 2008, pp. 3-4]
2.  A well-defined NW-SE fault strike trend was consistently observed in both seismic coherency maps and borehole image data. [Endres 2008, pp. 4-6]
3.  A linear relationship (R² ≈ 0.76) was established between the fractal dimension (FD) of seismic fault populations and the fracture density derived from borehole images. [Endres 2008, pp. 7-8]
4.  Geostatistical methods (cokriging, Gaussian simulation) using the seismic-derived FD and fault density as secondary variables successfully predicted the spatial distribution of sub-seismic fracture density and identified areas of high and low fracture probability. [Endres 2008, pp. 7-8]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Advanced coherency techniques (IHS, shaded relief, structural entropy) reveal additional small-scale lineaments not visible in standard displays. | [Endres 2008, pp. 3-4] | Applied to Top A2 horizon seismic data. | Arrows in Fig. 4 indicate improved imaging. |
| A linear relationship exists between seismic-derived fault density and borehole image-derived fracture density. | [Endres 2008, pp. 7-8] | Based on data from 11 wells with normalized FMI data. | Regression line in Fig. 10; wells J & N excluded due to high uncertainty. |
| Fractal dimension (FD) calculated from seismic fault lengths correlates linearly with borehole fracture density (R² ≈ 0.76). | [Endres 2008, pp. 7-8] | Based on 8 wells with both FD and image log estimates. | Crossplot in Fig. 13. |
| Cokriging and Gaussian simulation predict areal distribution of fracture density and probability of low-density areas. | [Endres 2008, pp. 7-8] | Uses seismic fault density/FD as secondary variable and borehole data as primary. | Results in Figs 11 & 12. |
| Fault density and connectivity maxima coincide with large-scale, continuous W-E-trending normal faults. | [Endres 2008, pp. 6-7] | Attribute analysis on Top A2 horizon using 1.8 km search window. | Overlay of interpreted faults (Fig. 5) on attribute maps (Fig. 7). |

## Limitations
1.  Seismic data quality was poor in some areas (e.g., near wells E, J, N), preventing FD calculation and introducing uncertainty in fracture density estimates. [Endres 2008, pp. 6-7]
2.  The method requires calibration with borehole image data, which is not available for all wells (e.g., wells B and K). [Endres 2008, pp. 2-3]
3.  The reliability of geostatistical predictions is higher along the NW-SE well trend and lower perpendicular to it. [Endres 2008, pp. 7-8]
4.  The study focuses on cemented, tight fractures acting as barriers; applicability to uncemented, conductive fracture systems is suggested but not demonstrated. [Endres 2008, pp. 7-8]

## Assumptions / Conditions
1.  The fault population exhibits fractal (scale-invariant) behavior, allowing the use of fractal dimension as a characteristic parameter. [Endres 2008, pp. 6-7]
2.  The linear relationship between seismic-scale fault density and borehole-scale fracture density is valid and can be used for prediction. [Endres 2008, pp. 7-8]
3.  Borehole image data (FMI/FMS) provides a representative sample of the fracture population at the well location. [Endres 2008, pp. 3-4]
4.  The 1.5 km grid spacing for FD calculation provides stable results for the dataset. [Endres 2008, pp. 6-7]

## Key Variables / Parameters
*   **Fractal Dimension (FD):** Exponent of the power-law relationship for cumulative fault length distribution; used as a seismic-derived predictor for fracture density. [Endres 2008, pp. 6-7]
*   **Fault Density (by count/length):** Number or total length of interpreted faults within a search area. [Endres 2008, pp. 6-7]
*   **Fault Connectivity:** Number of fault intersections within a search area. [Endres 2008, pp. 6-7]
*   **Normalized Fracture Density:** Borehole image-derived fracture count normalized to a 300 m reference length. [Endres 2008, pp. 2-3]
*   **Coherency Attributes:** Maximum coherency, local dip, azimuth, shaded relief reflectivity, structural entropy. [Endres 2008, pp. 2-4]

## Reusable Claims
1.  **Condition:** In areas with fractal fault populations and available borehole calibration data. **Claim:** The fractal dimension (FD) of seismic fault length distributions can be linearly correlated with borehole-derived fracture density to predict sub-seismic fracture occurrence. [Endres 2008, pp. 6-8]
2.  **Condition:** When standard seismic or coherency displays are insufficient. **Claim:** Advanced coherency processing techniques (e.g., IHS, shaded relief, structural entropy) can enhance the detection of subtle, sub-seismic tectonic lineaments. [Endres 2008, pp. 3-4]
3.  **Condition:** Given a linear relationship between seismic and borehole fracture metrics. **Claim:** Geostatistical methods like cokriging and Gaussian simulation can interpolate fracture density between wells and quantify prediction uncertainty. [Endres 2008, pp. 7-8]

## Candidate Concepts
*   [[Sub-seismic faults]]
*   [[Fractal dimension]]
*   [[Coherency analysis]]
*   [[Fracture density]]
*   [[Reservoir compartmentalization]]
*   [[Borehole image logs]]
*   [[Geostatistics]]

## Candidate Methods
*   [[Advanced seismic coherency processing]]
*   [[Fault attribute analysis]]
*   [[Fractal analysis of fault populations]]
*   [[Collocated cokriging]]
*   [[Gaussian simulation]]
*   [[IHS color display]]

## Connections To Other Work
The results coincide with independently achieved results from numerical fracture modelling published by Lohr et al. (2007), which deduced that maximum strain magnitude increases with fault displacement. [Endres 2008, pp. 7-8]

## Open Questions
1.  Can the calibration and prediction technique be reliably applied to uncemented fault and fracture systems that enhance reservoir quality? [Endres 2008, pp. 7-8]
2.  How can the method be benchmarked and quantified for fracture studies in undrilled areas and uncored intervals? [Endres 2008, pp. 7-8]
3.  What are the specific relationships between the predicted fracture distribution and reservoir quality (e.g., porosity, permeability)? [Endres 2008, pp. 7-8]

## Source Coverage
All non-empty indexed fragments were processed. The compilation used 7 source blocks containing 33,872 characters. The compiled page contains 34,032 characters, resulting in a coverage ratio by characters of 1.004724. The coverage status is full-index.
