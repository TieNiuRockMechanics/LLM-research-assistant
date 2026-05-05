---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2011-riley-quantification-of-fracture-networks-in-non-layered-massive-rock-using-synthetic-and-n"
title: "Quantification of Fracture Networks in Non-Layered, Massive Rock Using Synthetic and Natural Data Sets."
status: "draft"
source_pdf: "data/papers/Quantification of fracture networks in non-layered, massive rock using synthetic and natural data sets.pdf"
collections:
citation: "Riley, P., B. Tikoff, and A.B. Murray. “Quantification of Fracture Networks in Non-Layered, Massive Rock Using Synthetic and Natural Data Sets.” *Journal of Structural Geology*, vol. 33, no. 7, 2011, pp. 1238-1250."
indexed_texts: "16"
indexed_chars: "77611"
nonempty_source_blocks: "16"
compiled_source_blocks: "16"
compiled_source_chars: "77941"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004252"
coverage_status: "full-index"
source_signature: "1d7de2ffdfe278f71e353b725a1e03d17a399daa"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:26:10"
---

# Quantification of Fracture Networks in Non-Layered, Massive Rock Using Synthetic and Natural Data Sets.

## One-line Summary
This study investigates the correlation dimension and maximum Lyapunov exponent as quantitative measures for characterizing fracture spacing in massive, non-layered rock, testing them on synthetic data and applying them to natural fracture sets in the Sierra Nevada Batholith.

## Research Question
The research addresses the need for quantitative measures to characterize fracture spacing in mechanically non-layered rocks, where traditional methods like the Fracture Spacing Index are not applicable, to understand fracture geometry, development, and to incorporate fractures into flow models [Riley 2011, pp. 1-1].

## Study Area / Data
The study uses synthetic data sets and natural data from the Tuolumne Intrusive Suite, Sierra Nevada Batholith, California. Natural data includes sub-parallel joints in the Half Dome granodiorite near Tenaya Lake and tabular fracture clusters (TFCs) in the Cathedral Peak granodiorite near Matthes Lake [Riley 2011, pp. 8-9]. Synthetic data includes a Cantor set and randomly generated fracture sets with controlled population size, average spacing, and standard deviation [Riley 2011, pp. 4-6].

## Methods
The correlation dimension (ν) is calculated from the correlation integral, which counts pairs of data points within a distance γ, providing a rigorous estimate of the fractal dimension [Riley 2011, pp. 2-3]. The maximum Lyapunov exponent (λmax) is adapted to quantify the spatial organization of fracture spacing, where values near zero indicate regularity and positive values indicate increasing irregularity [Riley 2011, pp. 3-4]. Both methods are applied to synthetic and natural fracture spacing data collected along linear transects [Riley 2011, pp. 4-6, 8-10].

## Key Findings
The correlation dimension distinguishes between different fracture distributions (e.g., Cantor set ~0.64, synthetic sets ~0.50-0.55, natural joint sets ~0.05-0.07, TFCs ~0.19-0.21) and is robust for small populations [Riley 2011, pp. 6-6, 9-10]. The maximum Lyapunov exponent quantifies irregularity, with values near zero for regular joint sets (0.17-0.53) and higher values for clustered TFCs (1.43-1.97), effectively distinguishing between fracture sets with different genetic histories [Riley 2011, pp. 10-11]. Both methods show predictive capability with limited data [Riley 2011, pp. 11-12].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Correlation dimension for Cantor set (k=8) is 0.64, close to known fractal dimension of 0.63. | [Riley 2011, pp. 4-4] | Cantor set with p=2, s=1/3, 255 spacing measurements. | Validates the correlation dimension method. |
| Correlation dimension is insensitive to changes in average fracture spacing for synthetic normally distributed data. | [Riley 2011, pp. 6-6] | Synthetic data with varying μ (0.1 to 10.0), N=100-2000, σ proportional to μ. | Method robust across different scales. |
| λmax for synthetic bimodal distribution (Fig. 1b geometry) is 1.69, indicating high irregularity. | [Riley 2011, pp. 6-8] | Combined distributions: 500 points (μ=0.01, σ=0.01) and 40 points (μ=7.00, σ=2.00). | Demonstrates λmax distinguishes geometry from distribution. |
| Natural joint set correlation dimensions range from 0.05 to 0.07. | [Riley 2011, pp. 9-10] | Four transects in Half Dome granodiorite, population sizes 62-173. | Low values indicate a more even distribution of spacing values. |
| Natural TFC correlation dimensions range from 0.195 to 0.207. | [Riley 2011, pp. 9-10] | Three transects in Cathedral Peak granodiorite, population sizes 49-93. | Higher values than joints due to clustered spacing. |
| λmax for natural joint sets ranges from 0.21 to 0.53. | [Riley 2011, pp. 10-11] | Transects TL1-TL4. | Low values indicate high regularity in spacing. |
| λmax for natural TFCs ranges from 1.43 to 1.97. | [Riley 2011, pp. 10-11] | Transects ML1-ML3. | High values indicate high irregularity, corroborating field observations of clustering. |

## Limitations
Dimensional analyses may be scale-dependent and may not fully capture clustering geometry [Riley 2011, pp. 11-12]. The application of λmax differs from its traditional use in temporal dynamics, and the methods assume the observed fractures represent the total unobserved set [Riley 2011, pp. 11-12].

## Assumptions / Conditions
For the correlation dimension, the slope of the central portion of the log(γ) vs. log(C(γ)) plot accurately reflects the system's dimension, and an appropriate range of γ is used [Riley 2011, pp. 2-3]. For λmax, the data is treated as a spatial sequence of spacing measurements [Riley 2011, pp. 3-4].

## Key Variables / Parameters
- Correlation dimension (ν)
- Maximum Lyapunov exponent (λmax)
- Population size (N)
- Average fracture spacing (μ)
- Standard deviation (σ)
- Distance parameter (γ)

## Reusable Claims
- The correlation dimension provides a mathematically rigorous estimate of fractal dimension and is robust for small population sizes (N ≥ 100) [Riley 2011, pp. 6-6].
- The maximum Lyapunov exponent (λmax) quantifies the degree of irregularity or clustering in fracture spacing, where λmax ≈ 0 indicates regular spacing and increasing positive values indicate increasing irregularity [Riley 2011, pp. 3-4, 10-11].
- In non-layered rock, joint sets inferred to form from regional stress and thermal contraction show low correlation dimensions and low λmax, while tabular fracture clusters inferred to form from volatile overpressure show higher correlation dimensions and high λmax [Riley 2011, pp. 11-12].
- Both methods show predictive capability, as results are insensitive to population size, suggesting they can characterize fracture organization from limited outcrop data [Riley 2011, pp. 11-12].

## Candidate Concepts
- [[fracture reservoir]]
- [[fractal dimension]]
- [[self-similarity]]
- [[fracture spacing]]
- [[non-layered rock]]
- [[tabular fracture cluster]]
- [[joint set]]
- [[fluid flow modeling]]

## Candidate Methods
- [[correlation dimension]]
- [[maximum Lyapunov exponent]]
- [[box-counting]]
- [[fractal analysis]]
- [[transect sampling]]

## Connections To Other Work
The study builds on fractal analysis applied to fracture systems [Berkowitz et al., 2000; Bonnet et al., 2001; Turcotte, 1986] and critiques box-counting techniques [Billi et al., 2003; Roy et al., 2007]. It relates to work on fracture spacing in layered rocks [Narr and Suppe, 1991; Gross, 1993] and fluid flow in fractured media [Odling and Roden, 1997; Agosta et al., 2010]. The geological context references the Tuolumne Intrusive Suite [Bateman, 1992; Coleman et al., 2004] and fracture formation processes [Bergbauer and Martel, 1999; Riley and Tikoff, 2010].

## Open Questions
- Can these methods be applied to other rock types or more complex fracture networks?
- How do the quantitative measures correlate with specific fracture formation mechanisms beyond the two studied here?
- What is the full predictive capability for populating flow models with fractures using limited data?

## Source Coverage
All non-empty indexed fragments were processed. The coverage audit indicates 16 indexed texts with 77,611 characters, achieving full-index coverage with a coverage ratio by blocks of 1.0 and by characters of 1.004252.
