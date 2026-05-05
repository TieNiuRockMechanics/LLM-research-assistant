---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-zhu-fault-traces-generation-of-fault-segments-and-estimation-of-their-fractal-dimension"
title: "Fault Traces: Generation of Fault Segments and Estimation of Their Fractal Dimension."
status: "draft"
source_pdf: "data/papers/Fault Traces Generation of Fault Segments and Estimation of Their Fractral Dimension.pdf"
collections:
citation: "Zhu, Weiwei, et al. \"Fault Traces: Generation of Fault Segments and Estimation of Their Fractal Dimension.\" *Lithosphere*, vol. 2021, 2021, article 4991604, doi:10.2113/2021/4991604."
indexed_texts: "12"
indexed_chars: "59191"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "59435"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004122"
coverage_status: "full-index"
source_signature: "b52db816cf0736d4e8c95bf5c3b93a62baaca11b"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T01:04:48"
---

# Fault Traces: Generation of Fault Segments and Estimation of Their Fractal Dimension.

## One-line Summary
This paper presents a numerical method to generate detailed fault segments from an imprecise fault trace based on their fractal properties and proposes a modified algorithm to accurately calculate their fractal dimensions, finding that generated segments are comparable to natural ones.

## Research Question
How can detailed fault segments be generated from an imprecise fault trace obtained from a seismic survey or outcrop, and how can their fractal dimensions be accurately calculated to validate the generation method?

## Study Area / Data
The study uses three real fault maps for validation: (1) the northern part of the San Andreas fault system [Zhu 2021, pp. 9-10], (2) a Quaternary fault array in the central Apennines, Italy (Monte Vettore fault array) [Zhu 2021, pp. 9-10], and (3) the Top Kharaib fracture lineaments from the Lekhwair Field [Zhu 2021, pp. 9-10]. For generation, the method assumes an imprecise fault trace length of L = 10 km [Zhu 2021, pp. 3-4].

## Methods
The method generates fault segments using power-law relationships between segment parameters (mean segment length, step length, step width, and maximum fault offset) derived from outcrop studies [Zhu 2021, pp. 2-3]. It assumes fault segments are self-similar, subfault segments of a younger generation are independent, and the relationships hold at each generation step [Zhu 2021, pp. 2-3]. Segment lengths are assumed to follow a lognormal distribution [Zhu 2021, pp. 3-4]. A modified circle-based algorithm is proposed to calculate fractal dimension by covering the fault segments with the minimum number of circles, improving upon the method of Okubo and Aki (1987) [Zhu 2021, pp. 6-7]. The algorithm uses two rules: a single circle should cover as many line segments as possible, and with the same number covered, it should cover the largest possible length [Zhu 2021, pp. 6-7].

## Key Findings
Generated fault segments demonstrate hierarchical self-similar architecture, and their lengths follow approximately a lognormal distribution [Zhu 2021, pp. 1-2]. The fractal dimensions of natural fault segments (from three real maps) range from 1.29 to 1.34 [Zhu 2021, pp. 9-10]. The fractal dimensions of generated fault segments range from 1.25 to 1.31, which is similar to but slightly smaller than those of natural segments, likely because generated segments are less complex [Zhu 2021, pp. 10-12]. The method validates the generation approach from a fractal dimension perspective [Zhu 2021, pp. 12-13].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Fractal dimensions of three real fault systems (San Andreas, Apennines, Lekhwair) are 1.29, 1.29, and 1.34, respectively. | [Zhu 2021, pp. 9-10] | Calculated using the modified circle-based algorithm on real fault maps. | Upper and lower radius limits define the fractal scaling range. |
| Fractal dimensions of three generated fault segments (with mean lengths 110 m, 311 m, 1664 m) are 1.26, 1.31, and 1.25, respectively. | [Zhu 2021, pp. 10-12] | Generated with two segments per generation, no rotation, using the proposed method. | Values are slightly lower than natural faults, attributed to less geometric complexity. |
| Power-law relationships exist between mean segment length (L̄_se) and maximum fault offset (S): L̄_se = 2.16 S^0.89. | [Zhu 2021, pp. 2-3] | Derived from outcrop studies of strike-slip faults by de Joussineau and Aydin (2009). | Used as a constraint in the generation algorithm. |
| Generated fault segment lengths follow a lognormal distribution. | [Zhu 2021, pp. 3-4] | For segments generated from a 10 km trace over multiple generations. | Consistent with the Central Limit Theorem applied to the recursive division process. |
| The modified algorithm covers fault segments more accurately than the method of Okubo and Aki (1987). | [Zhu 2021, pp. 6-7] | For parallel or subparallel fault segments. | The algorithm minimizes the number of covering circles using two specific rules. |

## Limitations
The generated fault segments are non-unique solutions to an underdetermined inverse problem [Zhu 2021, pp. 2-3]. The method assumes fault segments are perfectly parallel or subparallel for accurate fractal dimension calculation, though it can be extended to subparallel segments with lower accuracy [Zhu 2021, pp. 6-7]. Generated segments may be less complex in geometry than real fault segments, leading to slightly lower fractal dimensions [Zhu 2021, pp. 10-12]. The algorithm's accuracy depends on the resolution of the input fault map [Zhu 2021, pp. 9-10].

## Assumptions / Conditions
1. Fault segments are self-similar across scales [Zhu 2021, pp. 2-3].
2. Subfault segments of a younger generation are independent of each other [Zhu 2021, pp. 2-3].
3. The power-law relationships found by de Joussineau and Aydin (2009) are valid at each generation step [Zhu 2021, pp. 2-3].
4. Step length is proportional to step width with a factor of 2.7 [Zhu 2021, pp. 2-3].
5. The number of segments in each generation is three or four with equal probability [Zhu 2021, pp. 2-3].
6. Overlapping structures between segments are dominant (probability 0.9) [Zhu 2021, pp. 2-3].
7. Subfault lengths follow a lognormal distribution [Zhu 2021, pp. 3-4].

## Key Variables / Parameters
- **L**: Length of the imprecise fault trace from a seismic map [Zhu 2021, pp. 2-3].
- **n_se**: Number of segments in each generation [Zhu 2021, pp. 2-3].
- **L̄_se**: Mean segment length [Zhu 2021, pp. 2-3].
- **S**: Maximum fault offset [Zhu 2021, pp. 2-3].
- **x**: Step length [Zhu 2021, pp. 2-3].
- **y**: Step width [Zhu 2021, pp. 2-3].
- **D**: Fractal dimension [Zhu 2021, pp. 6-7].
- **r**: Radius of covering circles [Zhu 2021, pp. 6-7].
- **N(r)**: Number of covering circles of radius r [Zhu 2021, pp. 6-7].

## Reusable Claims
- Generated fault segments from an imprecise trace exhibit hierarchical self-similar architecture and segment lengths that follow an approximate lognormal distribution, consistent with natural fault observations [Zhu 2021, pp. 1-2, 3-4].
- The fractal dimensions of both natural and generated fault segments range between 1.2 and 1.4, validating the generation method from a fractal perspective [Zhu 2021, pp. 1-2, 10-12].
- A modified circle-based algorithm that covers fault segments with the minimum number of circles provides a more accurate calculation of fractal dimension for parallel or subparallel fault sets compared to previous methods [Zhu 2021, pp. 6-7].
- The generation method incorporates minimum information (trace length) and can be constrained further if additional data, such as slip distribution, are available [Zhu 2021, pp. 2-3].

## Candidate Concepts
- [[fractal dimension]]
- [[fault segmentation]]
- [[damage zone]]
- [[self-similarity]]
- [[lognormal distribution]]
- [[echelon geometry]]
- [[fault linkage]]
- [[fractal geometry]]

## Candidate Methods
- [[circle-based fractal dimension calculation]]
- [[fault segment generation algorithm]]
- [[scaled logistic function fitting]]
- [[minimum circle covering algorithm]]

## Connections To Other Work
The study builds on the fractal concepts of Mandelbrot (1977) [Zhu 2021, pp. 2-3, 6-7]. It uses empirical relationships between fault segment parameters from de Joussineau and Aydin (2009) [Zhu 2021, pp. 2-3]. The fractal dimension calculation method improves upon the circle-based approach of Okubo and Aki (1987) [Zhu 2021, pp. 6-7]. It references observations of fault segmentation and self-similarity from outcrops and experiments (e.g., Otsuki and Dilov, 2005) [Zhu 2021, pp. 2-3]. The work connects to studies on fault damage zones and their impact on fluid flow (e.g., Aydin, 2000; Caine et al., 1996) [Zhu 2021, pp. 1-2].

## Open Questions
How can more complexities (e.g., more segments per generation, orientation rotations) be incorporated into the generated fault segments to make them closer to reality and increase their fractal dimension? [Zhu 2021, pp. 10-12].
How can the generated fault segments and their associated damage zones be used to model subsurface fluid flow in faulted reservoirs? [Zhu 2021, pp. 10-12].
Can the method be validated with higher-resolution seismic data or outcrop studies that reveal finer-scale segmentation?

## Source Coverage
All 12 non-empty indexed fragments were processed. The compiled source blocks total 12, with a coverage ratio by blocks of 1.0 and by characters of 1.004122, indicating full-index coverage.
