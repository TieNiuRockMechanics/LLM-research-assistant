---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2013-tafti-use-of-microseismicity-for-determining-the-structure-of-the-fracture-network-of-large"
title: "Use of Microseismicity for Determining the Structure of the Fracture Network of Large-Scale Porous Media."
status: "draft"
source_pdf: "data/papers/Use of microseismicity for determining the structure of the fracture network of large-scale porous media.pdf"
collections:
citation: "Tafti, Tayeb A., et al. “Use of Microseismicity for Determining the Structure of the Fracture Network of Large-Scale Porous Media.” *Physical Review E*, vol. 87, 032152, 2013. DOI: 10.1103/PhysRevE.87.032152. Accessed 2026."
indexed_texts: "9"
indexed_chars: "43930"
nonempty_source_blocks: "9"
compiled_source_blocks: "9"
compiled_source_chars: "44136"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004689"
coverage_status: "full-index"
source_signature: "efe6141d5aa91e43986e170d14c68344398ba628"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:46:19"
---

# Use of Microseismicity for Determining the Structure of the Fracture Network of Large-Scale Porous Media.

## One-line Summary
Microseismic events induced by fluid injection can be used to determine the fractal structure of fracture networks in large-scale porous media, with results indicating a network resembling a 3D percolation cluster rather than a tectonic fault backbone.

## Research Question
Can microseismic events be used to gain insight into the properties and structure of the fracture network in large-scale porous media, such as geothermal reservoirs, and can this analysis help distinguish between tectonic and injection-induced fractures? [Accessed 2026, pp. 1-1]

## Study Area / Data
The study focuses on the northwest (NW) region of the Geysers geothermal field (GGF) in northeast California. Data consisted of catalogs of microseismic events (earthquakes with small magnitudes) provided by the Lawrence Berkeley National Laboratory and the Northern California Earthquake Data Center, covering the period from 2006 to 2010. The spatial distribution of hypocenters was analyzed within three main clusters and four subclusters defined based on seismic activity and injection well locations. [Accessed 2026, pp. 3-4]

## Methods
The spatial distribution of hypocenters was characterized by calculating the fractal dimension (Df) using the two-point correlation function C(r) ∝ r^Df, computed with the ZMAP program. The Gutenberg-Richter frequency-magnitude distribution parameter (b-value) was estimated using the maximum likelihood method, with the minimum magnitude of completeness (Mc) determined by the maximum curvature method or manual curve fitting. The analysis involved plotting the effective Df as a function of event density to ensure convergence to a stable value. [Accessed 2026, pp. 4-6]

## Key Findings
The fractal dimensions of the spatial distribution of hypocenters in the studied clusters are all in a narrow range centered around Df ≃ 2.57 ± 0.06. The b-values for most cases are about b ≃ 1.3 ± 0.1. These values are significantly higher than those typically observed for regional tectonic seismicity (Df ≈ 2, b ≈ 1). The results indicate that the seismicity is induced by the injection of cold water, activating the entire fracture network (resembling a 3D sample-spanning percolation cluster with Df ≃ 2.53), rather than being of tectonic origin which would occur on the network's backbone (Df ≈ 2). For the larger regions, the Aki relation Df ≈ 2b is approximately satisfied. [Accessed 2026, pp. 1-1, 5-6, 8-8]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Fractal dimension Df ≃ 2.57 ± 0.06 for hypocenter distributions in seismic clusters. | [Accessed 2026, pp. 1-1] | Analysis of microseismic events in the Geysers geothermal field induced by cold water injection. | Comparable to measured fractal dimension of fracture sets in the reservoir rock. |
| b-values ≃ 1.3 ± 0.1 for the Gutenberg-Richter distribution. | [Accessed 2026, pp. 1-1, 6-8] | Microseismic events from 2006-2010 in the Geysers geothermal field. | Consistent with the Aki relation Df = 2b for the larger regions studied. |
| Df values converge to a constant as event density increases. | [Accessed 2026, pp. 5-6] | Analysis of region 1 and subregions of region 2 from 2006-2010. | Ensures the estimated Df is reliable and not an artifact of limited data. |
| Estimated Df is significantly larger than 2, and b is larger than 1. | [Accessed 2026, pp. 5-6, 6-8] | Comparison with typical values for tectonic seismicity. | Supports the interpretation that seismicity is induced by fluid injection, not tectonic stress release. |
| The fracture network resembles a 3D sample-spanning percolation cluster (Df ≃ 2.53). | [Accessed 2026, pp. 8-8] | Application of percolation theory and critical path analysis to heterogeneous fractured rock. | The backbone of such a cluster has a lower fractal dimension (≈1.9), consistent with tectonic seismicity. |

## Limitations
The range of length scales over which the correlation function C(r) was varied (about two orders of magnitude) is less than the ideal four orders of magnitude, which could affect the robustness of the fractal dimension estimate. The accuracy of locating individual seismic events is limited by crustal heterogeneity. The b-values are more scattered than Df values, possibly because each earthquake may not fully activate a fracture in the network. [Accessed 2026, pp. 4-5, 6-8]

## Assumptions / Conditions
The analysis assumes that the spatial distribution of microseismic hypocenters reflects the structure of the underlying fracture network. It assumes that the fracture network in large-scale porous media is self-similar and scale-invariant (fractal). The interpretation relies on percolation theory, assuming the fracture network's connectivity resembles that of a percolation cluster at or near its threshold. The Aki relation (Df = 2b) is considered under the assumption that slip scales with the area of the active fault plane. [Accessed 2026, pp. 1-3, 8-8]

## Key Variables / Parameters
- **Fractal Dimension (Df)**: Characterizes the scale-invariant structure of the fracture network or spatial distribution of hypocenters.
- **Gutenberg-Richter b-value**: Slope of the log-linear frequency-magnitude distribution of seismicity.
- **Correlation Function C(r)**: Used to compute Df from the spatial distribution of hypocenters.
- **Minimum Magnitude of Completeness (Mc)**: The magnitude above which the earthquake catalog is considered complete, used in b-value estimation.

## Reusable Claims
- In the Geysers geothermal field, the fractal dimension of the spatial distribution of microseismic hypocenters induced by cold water injection is approximately 2.57, which is significantly higher than the value of ~2 typical for tectonic seismicity. [Accessed 2026, pp. 1-1, 5-6]
- The b-value of the Gutenberg-Richter distribution for injection-induced microseismicity in the Geysers is approximately 1.3, higher than the typical tectonic value of ~1, indicating a relative abundance of small earthquakes. [Accessed 2026, pp. 1-1, 6-8]
- For sufficiently large study regions, the fractal dimension Df and b-value approximately satisfy the Aki relation Df ≈ 2b. [Accessed 2026, pp. 6-8]
- The fracture network activated by fluid injection in a heterogeneous porous medium resembles a 3D sample-spanning percolation cluster, whereas tectonic seismicity occurs on the cluster's backbone. [Accessed 2026, pp. 8-8]

## Candidate Concepts
- [[Fractal dimension]]
- [[Gutenberg-Richter law]]
- [[Microseismicity]]
- [[Percolation theory]]
- [[Fracture network]]
- [[Geothermal reservoir]]
- [[Induced seismicity]]
- [[Critical path analysis]]

## Candidate Methods
- [[Correlation integral analysis]]
- [[Gutenberg-Richter b-value estimation]]
- [[Maximum likelihood method]]
- [[ZMAP software]]

## Connections To Other Work
The study builds on prior work characterizing fracture networks as fractal structures (e.g., Barton and Larsen, Sammis et al.). It connects to the Aki relation between Df and b. The interpretation uses percolation theory (Ambegaokar et al., Stauffer and Aharony, Sahimi) to explain the network structure. The findings relate to studies of tectonic seismicity (e.g., Robertson et al., Pastén et al.) and have implications for understanding seismicity induced by hydraulic fracturing ("fracking"). [Accessed 2026, pp. 1-3, 8-9]

## Open Questions
Is the relationship between high Df, high b-values, and induced seismicity generalizable to other large-scale porous media and injection settings? Does the Aki relation hold universally for induced seismicity in fractured rock? How do the specific properties of the injected fluid and rock heterogeneity affect the resulting fracture network structure? [Accessed 2026, pp. 6-8, 8-9]

## Source Coverage
All 9 non-empty indexed fragments were processed. The compiled source contains 44,136 characters from a total indexed character count of 43,930, resulting in a coverage ratio by characters of 1.004689. The coverage ratio by blocks is 1.0, indicating full-index coverage. [Coverage audit data provided]
