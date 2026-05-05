---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2016-zaliapin-discriminating-characteristics-of-tectonic-and-human-induced-seismicity"
title: "Discriminating Characteristics of Tectonic and Human-Induced Seismicity."
status: "draft"
source_pdf: "data/papers/Discriminating Characteristics of Tectonic and Human-Induced Seismicity.pdf"
collections:
citation: "Zaliapin, Ilya, and Yehuda Ben-Zion. “Discriminating Characteristics of Tectonic and Human-Induced Seismicity.” *Bulletin of the Seismological Society of America*, vol. 106, no. 3, June 2016, doi:10.1785/0120150211."
indexed_texts: "13"
indexed_chars: "60564"
nonempty_source_blocks: "13"
compiled_source_blocks: "13"
compiled_source_chars: "60895"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.005465"
coverage_status: "full-index"
source_signature: "c4e330f4ac133eba00d822837e49498bdf54c336"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:39:57"
---

# Discriminating Characteristics of Tectonic and Human-Induced Seismicity.

## One-line Summary
This study identifies statistical features of earthquake clusters and background seismicity that can discriminate between tectonic and human-induced seismicity.

## Research Question
How can statistical features of seismicity clusters be used to distinguish between earthquakes caused by tectonic loads and those caused by human activities like geothermal production or mining? [Zaliapin 2016, pp. 1-2]

## Study Area / Data
The analysis uses seismic catalogs from six regions with clear dominant seismic drivers or mixed activity. [Zaliapin 2016, pp. 2-2]
- **Induced Seismicity Regions:**
    - The Geysers geothermal field, California (1984/01–2011/12, M 1.0–4.5, 75,991 events). [Zaliapin 2016, pp. 2-3]
    - TauTona gold mine, South Africa (2004/09–2010/09, M 1.5–4.2, 8519 events). [Zaliapin 2016, pp. 2-3]
- **Mixed Seismicity Regions:**
    - Coso geothermal field, California (1981/01–2013/12, M 1.0–4.41, 4412 events). [Zaliapin 2016, pp. 2-3]
    - Salton Sea geothermal field, California (1981/01–2013/12, M 1.5–5.11, 6018 events). [Zaliapin 2016, pp. 2-3]
- **Tectonic Seismicity Regions:**
    - Coso nongeothermal area, California (1981/01–2013/12, M 1.0–5.75, 56,801 events). [Zaliapin 2016, pp. 2-3]
    - San Jacinto fault zone, California (1981/01–2013/12, M 1.0–5.43, 39,768 events). [Zaliapin 2016, pp. 2-3]

## Methods
- **Nearest-Neighbor Distance:** A space-time-magnitude distance (η) between earthquakes is used to identify each event's parent (nearest earlier neighbor). [Zaliapin 2016, pp. 2-3]
- **Rescaled Components:** Time (T) and distance (R) to parent are normalized by the parent's magnitude. [Zaliapin 2016, pp. 3-5]
- **Cluster-Background Separation:** Events are classified as background (η > η₀) or clustered (η ≤ η₀) using a threshold η₀ estimated via a 1D Gaussian mixture model. [Zaliapin 2016, pp. 3-5]
- **Relative Quantile Approach:** To compare cluster styles, the relative quantiles (Q_T, Q_R) of clustered events are computed with respect to the background distribution. [Zaliapin 2016, pp. 5-6]
- **Parameters:** The analysis fixes b=1, d=1.6, and p=0.5. [Zaliapin 2016, pp. 3-5]

## Key Findings
Induced seismicity (e.g., The Geysers, TauTona) compared to tectonic seismicity (e.g., San Jacinto, Coso nongeothermal) exhibits: [Zaliapin 2016, pp. 9-10]
1.  **Higher background event rate:** Both absolute and relative to total seismicity rate. [Zaliapin 2016, pp. 1-2]
2.  **Faster temporal offspring decay:** The power-law exponent h for offspring intensity decay Λ(t) ∝ t⁻ʰ is ~2 in induced areas vs. ~1 in tectonic areas. [Zaliapin 2016, pp. 5-6]
3.  **Higher rate of repeating events:** Events occurring within a previous rupture area at long times. [Zaliapin 2016, pp. 5-6]
4.  **Larger proportion of small clusters:** The cluster size distribution has a steeper power-law tail (exponent s ≈ 2-3) in induced vs. tectonic (s ≈ 1-1.5) regions. [Zaliapin 2016, pp. 9-10]
5.  **Larger spatial separation between parent and offspring.** [Zaliapin 2016, pp. 1-2]
These differences were also observed to evolve temporally in the Coso and Salton Sea geothermal fields following the expansion of production. [Zaliapin 2016, pp. 8-9]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Induced regions (Geysers, TauTona) show a higher proportion of background events (P_B ≈ 0.83-0.88) than tectonic regions (P_B ≈ 0.18-0.66). | [Zaliapin 2016, pp. 5-5] | Analysis of six regions with clear seismic drivers. | Background proportion estimated via Gaussian mixture model. |
| The offspring intensity decay exponent h is ~2 for induced, ~1.5 for mixed, and ~1 for tectonic regions. | [Zaliapin 2016, pp. 5-6] | Analysis of close offspring (η < η₀). | Decay approximated by power law Λ(t) ∝ t⁻ʰ. |
| In induced regions, the rescaled time T to parent for nearby offspring shows a bimodal distribution (cluster vs. repeater modes), while in tectonic regions it is unimodal. | [Zaliapin 2016, pp. 5-6] | Offspring within one parent rupture length. | Rupture length estimated by L_m = 0.0152 × 10^(0.42m). |
| The cluster size distribution power-law exponent s is ~2-3 in induced regions and ~1-1.5 in tectonic regions. | [Zaliapin 2016, pp. 9-10] | Analysis of all examined regions. | Cluster defined as events connected by short (η ≤ η₀) links. |
| In Coso and Salton Sea geothermal fields, background proportion and cluster style changed after the onset of geothermal production, shifting towards characteristics of induced seismicity. | [Zaliapin 2016, pp. 8-9] | Temporal analysis before and after production expansion (1987 for Coso, 1988-1992 for Salton Sea). | Provides a natural control for regional properties. |

## Limitations
- The observed cluster style differences may not be universal; some tectonic regions (e.g., Parkfield) can exhibit features like high repeater rates that resemble induced seismicity. [Zaliapin 2016, pp. 10-12]
- Catalog uncertainties, particularly location errors, can create artificial cluster patterns reminiscent of induced seismicity. [Zaliapin 2016, pp. 10-12]
- The analysis is based on a limited number of selected regions. [Zaliapin 2016, pp. 9-10]

## Assumptions / Conditions
- The analysis uses fixed parameters: b-value (b=1), fractal dimension of hypocenters (d=1.6), and a parameter p=0.5. [Zaliapin 2016, pp. 3-5]
- The cluster-background separation threshold η₀ is estimated from the data using a 1D Gaussian mixture model. [Zaliapin 2016, pp. 3-5]
- The study assumes that the physical properties and catalog compilation factors within a region (like Coso or Salton Sea) remained similar before and after the onset of geothermal production, allowing changes to be attributed to the seismic driver. [Zaliapin 2016, pp. 8-9]

## Key Variables / Parameters
- **η_ij:** Nearest-neighbor distance between earthquake j and its parent i, combining space, time, and magnitude. [Zaliapin 2016, pp. 2-3]
- **T_ij, R_ij:** Rescaled time and distance components of η_ij, normalized by parent magnitude. [Zaliapin 2016, pp. 3-5]
- **η₀:** Threshold separating background (η > η₀) and clustered (η ≤ η₀) events. [Zaliapin 2016, pp. 3-5]
- **P_B:** Proportion of background events. [Zaliapin 2016, pp. 5-5]
- **h:** Power-law exponent for temporal decay of offspring intensity. [Zaliapin 2016, pp. 5-6]
- **s:** Power-law exponent for the tail of the cluster size distribution. [Zaliapin 2016, pp. 9-10]

## Reusable Claims
- **Claim:** Induced seismicity is characterized by a higher proportion of background events relative to clustered events compared to tectonic seismicity. [Zaliapin 2016, pp. 5-5, 9-10]
    - **Condition:** Based on analysis of regions with clear dominant seismic drivers (The Geysers, TauTona vs. San Jacinto, Coso nongeothermal).
    - **Limitation:** May not hold in all tectonic settings; catalog quality affects estimation.
- **Claim:** The temporal decay of aftershock-like offspring is faster (higher power-law exponent h) in regions of induced seismicity than in tectonic regions. [Zaliapin 2016, pp. 5-6, 9-10]
    - **Condition:** Derived from offspring with nearest-neighbor distance below the cluster threshold.
    - **Limitation:** Assumes a power-law decay model.
- **Claim:** The onset of significant geothermal production in the Coso and Salton Sea fields led to a measurable shift in seismicity cluster style towards characteristics associated with induced seismicity. [Zaliapin 2016, pp. 8-9]
    - **Condition:** Analysis of high-quality catalogs spanning the production onset.
    - **Limitation:** Assumes other regional factors remained constant.

## Candidate Concepts
- [[Nearest-neighbor distance]]
- [[Cluster style]]
- [[Background seismicity]]
- [[Clustered seismicity]]
- [[Relative quantile]]
- [[Repeating earthquakes]]
- [[Induced seismicity]]
- [[Tectonic seismicity]]

## Candidate Methods
- [[Seismic cluster analysis]]
- [[Nearest-neighbor distance calculation]]
- [[Gaussian mixture model for threshold estimation]]
- [[Relative quantile analysis]]
- [[Power-law fitting of temporal decay and cluster size]]

## Connections To Other Work
- The study builds on seismic cluster techniques developed for southern California. [Zaliapin 2016, pp. 1-2]
- It uses the nearest-neighbor distance definition from Baiesi and Paczuski (2004). [Zaliapin 2016, pp. 2-3]
- The interpretation relates to concepts of stress field heterogeneity and fault zone properties discussed in prior work. [Zaliapin 2016, pp. 5-6]
- It addresses the problem of discriminating induced earthquakes, a topic highlighted in recent studies on fracking and wastewater disposal. [Zaliapin 2016, pp. 1-2]

## Open Questions
- Can the identified discriminating characteristics be generalized to other regions with different tectonic settings or types of human activity?
- How do catalog uncertainties (e.g., location errors, magnitude completeness) quantitatively affect the estimated cluster style parameters?
- What additional statistical signals could be developed to increase the robustness of discrimination? [Zaliapin 2016, pp. 10-12]

## Source Coverage
All 13 non-empty indexed fragments were processed. The compiled source contains 60,895 characters from a total of 60,564 indexed characters, resulting in a coverage ratio by characters of 1.005. The coverage ratio by blocks is 1.0, indicating full-index coverage. [Zaliapin 2016, pp. 1-14]
