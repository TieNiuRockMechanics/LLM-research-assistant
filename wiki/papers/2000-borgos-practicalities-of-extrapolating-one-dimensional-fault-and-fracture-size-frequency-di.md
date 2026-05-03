---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2000-borgos-practicalities-of-extrapolating-one-dimensional-fault-and-fracture-size-frequency-di"
title: "Practicalities of Extrapolating One-Dimensional Fault and Fracture Size-Frequency Distributions to Higher-Dimensional Samples."
status: "draft"
source_pdf: "data/papers/2000 - Practicalities of extrapolating one-dimensional fault and fracture size-frequency distributions to higher-dimensional samples.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Borgos, Hilde G., et al. “Practicalities of Extrapolating One-Dimensional Fault and Fracture Size-Frequency Distributions to Higher-Dimensional Samples.” *Journal of Geophysical Research*, vol. 105, no. B12, 10 Dec. 2000, pp. 28377-28391."
indexed_texts: "18"
indexed_chars: "86112"
nonempty_source_blocks: "18"
compiled_source_blocks: "18"
compiled_source_chars: "85074"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.987946"
coverage_status: "full-index"
source_signature: "f4c832406f4212013f920b712c95e510365b3c57"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T11:50:24"
---

# Practicalities of Extrapolating One-Dimensional Fault and Fracture Size-Frequency Distributions to Higher-Dimensional Samples.

## One-line Summary
Previously published theory that extrapolates 1‑D fault/fracture size‑frequency distributions to 2‑D and 3‑D populations is of limited practical value; discrepancies arise mainly from deviations from ideal spatial uniformity and from non‑power‑law scaling, and new theory incorporating clustering is presented. [Borgos 2000, pp. 1-2]

## Research Question
How can fault and fracture population statistics observed in 1‑D samples (e.g., boreholes, traverses) be reliably extrapolated to two and three dimensions, given that the standard integer‑shift rule based on the assumptions of a spatial Poisson process and pure power‑law size‑frequency distributions often fails in natural datasets? [Borgos 2000, pp. 1-2]

## Study Area / Data
- The study is primarily theoretical and simulation‑based; it does not rely on a single geographic study area.
- Simulation examples: a 2‑D fault pattern of 25,000 faults with uniformly distributed centre points, uniformly random orientations (0°–360°), and lengths drawn from a power‑law with exponent \( C_2 = 1.6 \) and minimum length 1 m; 1000 horizontal traverses sample the pattern. [Borgos 2000, pp. 3-4]
- Field examples referred to:
  - Normal fault population in the Volcanic Tableland, eastern California, where the proportion of linked fault arrays \( \theta \) is estimated to be < 0.5 and the O/S ratio lies in 3–10. [Borgos 2000, pp. 7-8]
  - Ortega and Marrett (2000) sandstone fracture data, where a 2‑D exponent of 1.25 and a 1‑D exponent of 0.98 give \( C_2 - C_1 = 0.28 \). [Borgos 2000, pp. 6-6]
  - Fault array from the Cumberland Plateau, Tennessee, illustrating the effect of linkage criteria on 1‑D exponent estimates (Wojtal, 1996). [Borgos 2000, pp. 6-6]

## Methods
- **Simulation of ideal fractal fault patterns**: Generate 2‑D fault centre points from a uniform spatial Poisson process, assign lengths from a power‑law distribution, and sample with 1‑D traverses. Estimate power‑law exponents using a maximum likelihood estimator and examine sampling variability. [Borgos 2000, pp. 3-4]
- **Analytical extension for non‑uniform spatial distribution**: Model clustering perpendicular to the traverse by introducing a distance distribution \( f(r) \propto r^{\delta - 1} \); derive modified relationships between 1‑D and 2‑D exponents (equations (5) and (6)). [Borgos 2000, pp. 4-5]
- **Examination of non‑power‑law size‑frequency distributions**: Compare exponential 2‑D length distributions with the induced 1‑D gamma distribution, and compute the local slope of \( \log N(x) \) vs. \( \log x \) to show that the difference \( C_2(x) - C_1(x) < 1 \). [Borgos 2000, pp. 5-6]
- **Modelling of en echelon clustering and linkage**: Represent the total fault population as a mixture of isolated faults (exponent \( \beta_S \)) and fault arrays (exponent \( \beta_A \)), with a mixture proportion \( \theta \). The combined distribution is not a perfect power law, but an apparent exponent \( \beta_C \) can be fitted. The effect on 1‑D/2‑D exponent differences is studied via simulation. [Borgos 2000, pp. 6-10]
- **Random linkage probability for 1‑D data**: Derive the distribution of fault overlap \( O \) from the separation \( S \) and fault length distributions, allowing a probabilistic linkage criterion to be applied when only 1‑D transect data are available (Appendix C). [Borgos 2000, pp. 14-15]

## Key Findings
1. **Even under ideal spatial uniformity and power‑law scaling, estimator variance causes noticeable deviations.** For simulated 2‑D patterns (\( C_2 = 1.6 \)) and 1‑D samples of 60–105 faults, the estimated \( C_1 \) had a standard deviation of 0.07; the difference \( C_2 - C_1 \) ranged from 0.85 to 1.1, i.e., 15–25% deviation from the theoretical value of 1.0. With ~1000 faults, the error drops below 5%. [Borgos 2000, pp. 3-4]
2. **Non‑uniform spatial distribution perpendicular to the traverse alters the exponent shift.** If fault centre points follow a self‑similar distribution \( f(r) \propto r^{\delta - 1} \) with \( \delta < 1 \), then \( C_1 = C_2 - \delta \), so \( C_2 - C_1 = \delta < 1 \). [Borgos 2000, pp. 4-5]
3. **When the underlying size‑frequency distribution is not a power law, the integer‑shift rule fails.** For an exponential length distribution, the 1‑D sample follows a gamma distribution; the fitted power‑law exponents give a difference \( C_2 - C_1 \) of 1/2 or 2/3 (depending on the mean used), i.e., significantly less than 1.0. [Borgos 2000, pp. 5-6]
4. **En echelon clustering strongly reduces the apparent exponent difference.** When the fault population is a mixture of isolated faults (\( \beta_S \)) and linked arrays (\( \beta_A \)), the combined 2‑D apparent exponent \( \beta_C \) lies between them, and the 1‑D exponent (without linkage criterion) is close to \( \beta_S - 1/n \). The difference \( C_2 - C_1 \) becomes \( \beta_C - (\beta_S - 1/n) < 1 \). For typical values (\( \beta_S = 1.8, \beta_A = 1.3, n = 1 \)), this difference is only 0.7–0.85 when \( \theta \) is 0.25–0.5. If en echelon arrays dominate (\( \theta > 0.5 \)), the difference can be as low as 0.5. [Borgos 2000, pp. 8-10, 12]
5. **Practical implication:** Extrapolating 1‑D data to two or three dimensions without accounting for clustering and non‑power‑law behaviour leads to overestimation of small‑scale fault/fracture numbers, underestimation of large structures and maximum fault size, and incorrect spatial distributions (random instead of aligned arrays). [Borgos 2000, pp. 11, 12]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Even with uniform spatial distribution and pure power‑law fracture lengths, the estimated 1‑D exponent \( C_1 \) from ~80‑100 faults has a standard deviation of ~0.07, causing \( C_2 - C_1 \) to deviate 15–25% from the expected integer 1. | [Borgos 2000, pp. 3-4] | Simulation: 2‑D pattern, 25,000 faults, \( C_2=1.6 \), 1000 traverses; maximum likelihood estimator. | Bias and variance increase for smaller sample sizes; for ~1000 faults, error <5%. |
| Analytical derivation: when perpendicular clustering follows \( f(r) \propto r^{\delta-1} \), the 1‑D displacement exponent becomes \( C'_1 = C'_2 - \delta/n \) (length exponent: \( C_1 = C_2 - \delta \)). | [Borgos 2000, pp. 4-5] | Sub‑parallel faults, traverse perpendicular to strike; assumes profile shape factor \( \alpha \) does not matter when \( n=1 \). | When \( \delta=1 \), uniform case recovered. |
| If 2‑D fault lengths follow an exponential distribution, the 1‑D sample follows a gamma distribution; the local slope difference \( C_2(x) - C_1(x) = \frac{(\lambda x)^2}{\lambda x + 1} < 1 \). At the mean lengths, difference is ~0.5–0.67. | [Borgos 2000, pp. 5-6] | Exponential length distribution; derived from cumulative slopes. | Fitting a power law to the central part of exponential data yields a slope gap ≪1. |
| For a mixture of isolated faults (\( \beta_S = 1.8 \)) and fault arrays (\( \beta_A = 1.3 \)) with proportion \( \theta = 0.25 \), the combined apparent 2‑D exponent \( \beta_C \approx 1.66 \). Under no linkage in 1‑D, \( C_1 \approx \beta_S - 1 = 0.8 \), giving \( C_2 - C_1 \approx 0.86 \). | [Borgos 2000, pp. 8-10] | Simulation of combined distribution; \( n=1 \); 500 faults. | If \( \theta > 0.5 \), \( \beta_C \) closer to \( \beta_A \), difference can fall to ~0.5. |
| Ortega and Marrett (2000) report a real 2‑D fracture exponent of 1.25 and a 1‑D exponent of 0.98, giving a difference of 0.28, consistent with non‑power‑law or clustered behaviour. | [Borgos 2000, pp. 6] | Naturally fractured sandstone; both exponential and power‑law fits possible. | Supports the claim that integer shift rarely holds. |

## Limitations
- The theoretical derivations for clustering perpendicular to the traverse assume sub‑parallel faults with strike perpendicular to the traverse line; more complex orientations are not treated. [Borgos 2000, pp. 4-5]
- The treatment of en echelon arrays simplifies the population to only two sub‑populations (isolated faults and arrays) with perfect power‑law distributions for each; real populations may have a continuum of linkage states. [Borgos 2000, pp. 7-8]
- The linkage criterion based solely on O/S ratio is a “convenient first approach”; a more rigorous criterion should include segment sizes and mechanical interaction. [Borgos 2000, pp. 7]
- The random linkage procedure for 1‑D data (Appendix C) requires knowledge of the length distribution exponent \( b \), the lower limit \( l_0 \), and the scaling factor \( \gamma \) in \( D_{max} = \gamma L^n \), which are often uncertain from 1‑D data alone. [Borgos 2000, pp. 14-15]
- The analysis of non‑power‑law size distributions is restricted to the special case of exponential distributions; more general deviations are not explored analytically. [Borgos 2000, pp. 5]

## Assumptions / Conditions
- **Standard integer‑shift theory** (Heifer & Bevan, 1990; Marrett & Allmendinger, 1991) assumes:
  - Fault positions are independently, uniformly distributed (spatial Poisson process) with constant intensity.
  - Fault size is independent of position.
  - The size‑frequency distribution follows a perfect power law. [Borgos 2000, pp. 1-3]
- In the non‑uniform spatial extension:
  - Faults are approximately parallel, strike is perpendicular to the traverse.
  - Displacement profile follows a shape parameter \( \alpha \), but the result \( C_1 = C_2 - \delta \) is independent of \( \alpha \) when the displacement–length scaling exponent \( n = 1 \). [Borgos 2000, pp. 4-5]
- In the en echelon model:
  - Isolated faults and segments that make up arrays have the same size‑frequency distribution (same \( \beta_S \)).
  - The maximum size of isolated faults is smaller than that of fault arrays.
  - The summed displacement profile of an array is comparable to that of an isolated fault. [Borgos 2000, pp. 6-7]
- The combined distribution approach assumes the population is a mixture of two power‑law sub‑populations and uses \( \theta \) = number of arrays / total number of faults; this ratio depends on the linkage criterion (e.g., O/S ratio) and data resolution. [Borgos 2000, pp. 7, 10]

## Key Variables / Parameters
- \( C_3, C_2, C_1 \): power‑law exponents of fault length distributions in 3‑D, 2‑D, and 1‑D samples. [Borgos 2000, pp. 2-3]
- \( C'_3, C'_2, C'_1 \): corresponding exponents for maximum displacement distributions. If \( D_{max} \propto L^n \), then \( C' = C/n \). When \( n = 1 \), displacement and length exponents coincide. [Borgos 2000, pp. 2-3]
- \( n \): scaling exponent in \( D_{max} = \gamma L^n \); commonly \( n \approx 1 \) for many fault populations. [Borgos 2000, pp. 2-3]
- \( \delta \): self‑similar clustering parameter perpendicular to traverse; \( f(r) \propto r^{\delta-1} \). \( \delta = 1 \) recovers spatial uniformity; \( \delta < 1 \) implies clustering near the traverse. [Borgos 2000, pp. 4-5]
- \( \lambda \): rate parameter of the exponential length distribution, \( \lambda = 1/\langle x \rangle \). [Borgos 2000, pp. 5-6]
- \( \beta_S \): power‑law exponent of the size distribution for isolated faults / fault segments. [Borgos 2000, pp. 8]
- \( \beta_A \): power‑law exponent for en echelon fault arrays; \( \beta_A < \beta_S \). [Borgos 2000, pp. 8]
- \( \theta \): proportion of fault arrays in the population, \( \theta = N_A / (N_A + N_I) \). [Borgos 2000, pp. 7]
- \( O/S \): overlap‑to‑separation ratio of adjacent fault tips; used as a linkage criterion. Typical observed values for natural fault arrays lie in 1–10. [Borgos 2000, pp. 6-7]
- \( b \): power‑law exponent of fault length distribution in 1‑D, \( b = C_1 \). [Borgos 2000, pp. 14]
- \( M_1, M_2 \): lower and upper bounds of the O/S interval used to define linked structures. [Borgos 2000, pp. 14]

## Reusable Claims
1. **Claim:** When extrapolating 1‑D fault size‑frequency data to higher dimensions, assuming an integer shift (\( C_2 = C_1 + 1 \)) is valid *only if* the spatial distribution is uniform Poissonian and the size distribution is a perfect power law. [Borgos 2000, pp. 1-3]
   *Condition/Limitation:* Even then, for datasets of <100 faults, estimator variance can cause 15–25% deviation from the expected integer shift.

2. **Claim:** If fault positions cluster in a self‑similar fashion perpendicular to a traverse (with exponent \( \delta < 1 \)), then \( C_2 - C_1 = \delta \), not 1. [Borgos 2000, pp. 4-5]
   *Condition/Limitation:* Requires subparallel faults perpendicular to the traverse; displacement‑length scaling exponent \( n = 1 \) for the result to be independent of the displacement profile shape.

3. **Claim:** If the underlying fault length distribution is exponential rather than power‑law, the difference between fitted power‑law exponents in 2‑D and 1‑D will be *less than 1*; for typical data it is about 0.5–0.67. [Borgos 2000, pp. 5-6]
   *Condition/Limitation:* Fitting a straight line to the central part of the log‑cumulative plot; more general non‑power‑law cases will also give \( <1 \).

4. **Claim:** In populations with en echelon arrays, if 1‑D data are analysed without a linkage criterion, the effective 2‑D exponent difference is reduced: \( C_2 - C_1 \) may be as low as 0.7–0.85 (or 0.5 when arrays dominate). [Borgos 2000, pp. 8-10, 12]
   *Condition/Limitation:* Requires knowing or estimating the proportion \( \theta \) of arrays and applying a physically based linkage criterion (e.g., O/S ratio); both depend on data resolution.

5. **Claim:** Neglecting spatial clustering in extrapolation leads to overestimation of small‑scale fracture numbers, underestimation of large structures, and a spatially random arrangement that does not reflect natural en echelon organisation. [Borgos 2000, pp. 11]
   *Condition/Limitation:* Applies to all dimensions; the problem is equally severe when going from 2‑D maps to 3‑D volumes.

6. **Claim:** A statistical linkage probability can be assigned to 1‑D fault pairs using the conditional probability \( \text{Prob}\{sM_1 \le O \le sM_2 | S = s\} \) derived from the fault length distribution, allowing random linkage classification when 2‑D information is missing. [Borgos 2000, pp. 14-15]
   *Condition/Limitation:* Requires estimates of the length distribution exponent \( b \), minimum length \( l_0 \), and scaling factor \( \gamma \); the procedure yields only one statistical realisation, not a unique linkage map.

## Candidate Concepts
- [[fracture reservoir]] – although not explicitly named, the motivation (permeability, seismic anisotropy) is stated. [Borgos 2000, pp. 1-2]
- [[power law size-frequency distribution]] – central to fault population descriptions.
- [[spatial Poisson process]] – the baseline uniform model for fault positions.
- [[en echelon arrays]] – a key form of fault clustering studied in this work.
- [[fractal dimension of fault patterns]] – referenced from Davy et al. (1992); used to discuss faults centre point distributions.
- [[mark point process]] – used to represent fault patterns with positions and sizes.
- [[displacement-length scaling]] – the relation \( D_{max} \propto L^n \), often linear (\( n=1 \)).
- [[O/S ratio (overlap-separation)]] – criterion for segment linkage.
- [[maximum likelihood estimator]] – used to estimate power‑law exponents; known to be biased.
- [[exponential distribution (fault lengths)]] – alternative to power law; observed in mid‑ocean ridge fault populations.
- [[gamma distribution]] – length distribution of faults intersected by a traverse when 2‑D lengths are exponential.
- [[fault linkage]] – process of segments connecting to form larger structures.

## Candidate Methods
- [[simulation of 2-D fault patterns with uniform spatial distribution]]
- [[1-D traverse sampling of simulated fault patterns]]
- [[maximum likelihood estimation of power-law exponents]]
- [[analytical derivation of 1-D length distribution from a general 2-D distribution (Appendix A)]]
- [[derivation of slope on bilogarithmic plots of fault number vs size (Appendix B)]]
- [[random linkage probability for 1-D fault data (Appendix C)]]
- [[O/S ratio linkage criterion for 2-D fault maps]]
- [[combined (mixture) distribution of fault sizes for en echelon populations]]

## Connections To Other Work
- **Marrett & Allmendinger (1991), Heifer & Bevan (1990), Piggott (1997), Berkowitz & Adler (1998):** Established the integer‑shift rule (\( C_3 - C_2 = 1, C_2 - C_1 = 1 \)) under spatial uniformity, which is the starting point criticized here. [Borgos 2000, pp. 1-3]
- **Malinverno (1997):** First attempt to modify the theory for non‑uniform spatial distributions (turbidite beds); the present paper extends his approach to faults and adds parallel‑strike clustering. [Borgos 2000, pp. 2, 4-5]
- **Davy et al. (1992), Bour & Davy (1999):** Proposed a relationship between fractal dimension of fault centre points and length distribution exponent; Borgos et al. argue that centre‑point analysis alone fails to capture en echelon clustering because array tips are close but centres are far apart. [Borgos 2000, pp. 2]
- **Cowie & Scholz (1992a,b), Dawers et al. (1993), Schlische et al. (1996):** Provided evidence that \( D_{max} \propto L \) (\( n = 1 \)) for many fault populations, simplifying the displacement–length relations used here. [Borgos 2000, pp. 2-3]
- **Ortega & Marrett (2000):** Real‑world example where the 1‑D/2‑D exponent difference was only 0.28, supporting the paper’s conclusions about non‑integer differences. [Borgos 2000, pp. 6]
- **Berkowitz & Adler (1998):** Generated 3‑D joint networks from 2‑D maps using the integer‑shift rule; found good exponent agreement but the simulated patterns lacked observed clustering and en echelon alignment, which this study shows will strongly affect aggregate rock properties. [Borgos 2000, pp. 11]
- **Hatton et al. (1993):** Empirical relationship \( C_3 = a_1 C_2 + a_2 \) with \( a_1 = 1.3, a_2 = -0.2 \); the present theory suggests \( a_1 = 1.0 \) and \( 0 \le a_2 \le 1.0 \), and the difference between wet and dry experiments may explain the discrepancy. [Borgos 2000, pp. 11-12]
- **Marrett (1996):** Aggregate properties of fracture populations depend critically on the assumed 3‑D power‑law exponents and spatial distribution; the current findings imply those conclusions may need re‑evaluation. [Borgos 2000, pp. 11]

## Open Questions
- How can the random linkage probability approach for 1‑D data be validated against cases where true 2‑D linkage is known? [Borgos 2000, pp. 14-15]
- What is the general relationship between 1‑D and higher‑dimensional exponents when size distributions are neither power‑law nor exponential but mixtures of both? [Borgos 2000, pp. 5-6]
- How do en echelon clustering and fault linkage affect the extrapolation from 2‑D maps to 3‑D volumes, particularly given the complex 3‑D morphology of fault surfaces? [Borgos 2000, pp. 11]
- Can the linkage criteria be improved by incorporating mechanical interaction (stress shadows, displacement profile distortion) beyond the simple O/S ratio? [Borgos 2000, pp. 7]
- How robust are the conclusions when applied to joints, veins, and shear fractures that may have different displacement‑length relations? [Borgos 2000, pp. 6, 11]
- What are the implications for aggregate rock properties (porosity, permeability, seismic anisotropy) when realistic spatial clustering is included in 3‑D fracture network models? [Borgos 2000, pp. 11]
- Is it possible to derive an analytical expression for the combined exponent \( \beta_C \) as a function of \( \theta \), \( \beta_S \), and \( \beta_A \), or must it always be estimated by simulation? [Borgos 2000, pp. 10]

## Source Coverage
All 18 non‑empty indexed text fragments were processed.  
- Indexed characters: 86,112  
- Compiled source characters: 85,074  
- Coverage ratio by character: 98.79%  
- No fragment was omitted; full indexing was achieved.  
- Source signature: f4c832406f4212013f920b712c95e510365b3c57
