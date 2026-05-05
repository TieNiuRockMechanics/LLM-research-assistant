---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-zhu-fractal-and-multifractal-characterization-of-stochastic-fracture-networks-and-real-outc-621bebe3"
title: "Fractal and Multifractal Characterization of Stochastic Fracture Networks and Real Outcrops."
status: "draft"
source_pdf: "data/papers/Fractal and multifractal characterization of stochastic fracture networks and real outcrops.pdf"
collections:
citation: "Zhu, Weiwei, et al. \"Fractal and Multifractal Characterization of Stochastic Fracture Networks and Real Outcrops.\" *Journal of Structural Geology*, vol. 155, 5 Jan. 2022, p. 104508. Accessed 2026."
indexed_texts: "12"
indexed_chars: "58689"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "55344"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.943005"
coverage_status: "full-index"
source_signature: "45ba739e0892bb23303aaa2b3bec547a37ef7138"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T01:09:52"
---

# Fractal and Multifractal Characterization of Stochastic Fracture Networks and Real Outcrops.

## One-line Summary
This study systematically investigates how fracture geometries (length, orientation, position) and system size affect the fractal dimension and multifractal spectrum of stochastic fracture networks and 80 digitized real outcrops, finding that system size has the most significant impact and that multifractal measures better capture complexity from clustering.

## Research Question
How do different fracture geometrical properties (lengths, orientations, center positions) and system sizes impact the fractal and multifractal characterization of complex fracture networks? [Zhu 2022, pp. 1-2]

## Study Area / Data
The study uses two data sources: (1) Stochastic Discrete Fracture Networks (SDFNs) generated with the in-house software HATCHFRAC, and (2) 80 digitized real outcrop maps from various publications, with scales ranging from millimeters to thousands of kilometers. [Zhu 2022, pp. 2-3, 8-9]

## Methods
- **Stochastic Network Construction:** 2D fracture networks are built with line segments. Fracture lengths follow a power-law distribution (exponent *a*), orientations follow a von Mises-Fisher distribution (concentration parameter *κ*), and center positions follow either a uniform or a fractal spatial density distribution (fractal dimension *F_D*). The termination criterion is the formation of a spanning cluster. [Zhu 2022, pp. 2-3]
- **Fractal Analysis:** The box-counting method is used to calculate the single fractal dimension (*D*) and the multifractal spectrum. The multifractal spectrum is characterized by the difference in the Lipschitz-Hölder exponent, *Δα*. [Zhu 2022, pp. 3-4]
- **Sensitivity Analysis:** A Taguchi design with an L9 orthogonal array is used to design parameter combinations. The input/output correlation method calculates linear correlation coefficients between input parameters (*a*, *F_D*, *κ*, *L*) and outputs (*D*, *Δα*). [Zhu 2022, pp. 5-6]
- **Outcrop Digitization:** A pixel-based fracture detection algorithm is applied to binary outcrop images to interpret fractures as line segments or polylines. [Zhu 2022, pp. 2-3, 8-9]

## Key Findings
1.  In stochastic networks, fracture lengths (*a*), orientations (*κ*), and system size (*L*) have positive correlations with both the single fractal dimension (*D*) and *Δα*. System size (*L*) has the most significant impact. [Zhu 2022, pp. 5-6, 6-7]
2.  The single fractal dimension (*D*) is uncorrelated with the fractal dimension of fracture center positions (*F_D*), meaning it cannot capture complexity from clustering effects. [Zhu 2022, pp. 5-5, 6-7]
3.  *Δα* has a strong negative correlation with *F_D*, indicating that clustering effects increase network complexity and that *Δα* can capture this heterogeneity. [Zhu 2022, pp. 5-5, 6-7]
4.  *D* shows clear finite-size effects, while *Δα* does not. [Zhu 2022, pp. 5-7]
5.  For the 80 real outcrops, *D* and *Δα* show wide variations even at similar scales, with negligible correlations with scale, supporting self-similarity. Mean values of *D* and *Δα* are smaller than in stochastic networks. [Zhu 2022, pp. 8-9, 9-12]
6.  The inconsistent correlation between *D* and *Δα* in stochastic networks (weak positive) versus real outcrops (weak negative) suggests stochastic models may oversimplify geometries (e.g., lacking tortuosity and T-type intersections). [Zhu 2022, pp. 9-12]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Single fractal dimension *D* and *Δα* are used to represent fractal and multifractal patterns. | [Zhu 2022, pp. 1-2] | Stochastic fracture networks and real outcrops. | Key metrics for characterization. |
| Fracture lengths follow a power-law distribution with exponent *a* ∈ [2.0, 3.0]. | [Zhu 2022, pp. 2-3] | Stochastic network construction. | Based on field observations. |
| Fracture orientations follow a von Mises-Fisher distribution with concentration parameter *κ*. | [Zhu 2022, pp. 2-3] | Stochastic network construction. | *κ*=0 is uniform; higher *κ* is more concentrated. |
| Fracture center positions follow a uniform or fractal spatial density distribution (dimension *F_D*). | [Zhu 2022, pp. 2-3] | Stochastic network construction. | Fractal distribution introduces clustering. |
| Box-counting method used to calculate *D* and *Δα*. | [Zhu 2022, pp. 3-4] | Applied to both stochastic networks and digitized outcrops. | Minimum box size not limited by image resolution for line-segment representations. |
| System size (*L*) has the most significant positive correlation with *D* and *Δα*. | [Zhu 2022, pp. 6-7] | Sensitivity analysis of stochastic networks. | *L* ∈ {10, 30, 50}. |
| *D* is uncorrelated with *F_D*; *Δα* has a strong negative correlation with *F_D*. | [Zhu 2022, pp. 5-5, 6-7] | Sensitivity analysis of stochastic networks. | *Δα* captures clustering complexity; *D* does not. |
| 80 real outcrops show wide variations in *D* (1.41-1.96) and *Δα* (0.94-2.18). | [Zhu 2022, pp. 8-9] | Digitized outcrop maps from various scales and settings. | Indicates no universal indicator for complexity. |
| *D* and *Δα* have negligible correlations with scale in real outcrops. | [Zhu 2022, pp. 9-12] | Analysis of 80 outcrops. | Supports self-similarity of natural fracture networks. |

## Limitations
- Stochastic fracture networks use simplified 2D line segments, potentially over-simplifying real geometries by omitting features like fracture tortuosity and T-type intersections. [Zhu 2022, pp. 9-12]
- The study is limited to 2D representations, while real subsurface fracture networks are 3D. [Zhu 2022, pp. 9-12]
- The analysis assumes geometrical parameters are independent for the sensitivity analysis. [Zhu 2022, pp. 6-7]

## Assumptions / Conditions
- Fractures are represented as line segments in 2D. [Zhu 2022, pp. 2-3]
- The termination criterion for stochastic network generation is the formation of a spanning cluster, not a prescribed fracture intensity. [Zhu 2022, pp. 2-3]
- Fracture lengths follow a power-law distribution, orientations follow a von Mises-Fisher distribution, and center positions follow either a uniform or a fractal spatial density distribution. [Zhu 2022, pp. 2-3]
- The box-counting method's linear regression for *D* must include the fixed point (0,0). [Zhu 2022, pp. 4-5]

## Key Variables / Parameters
- **Input Parameters:** Power-law exponent (*a*), fractal dimension of center positions (*F_D*), concentration parameter for orientations (*κ*), system size (*L*). [Zhu 2022, pp. 4-5]
- **Output Metrics:** Single fractal dimension (*D*), difference of Lipschitz-Hölder exponent (*Δα*). [Zhu 2022, pp. 1-2, 4-5]

## Reusable Claims
- System size (*L*) has the most significant positive correlation with both the single fractal dimension (*D*) and the multifractal spectrum width (*Δα*) among the tested parameters in stochastic 2D fracture networks. [Zhu 2022, pp. 6-7]
- The multifractal parameter *Δα* is superior to the single fractal dimension *D* for characterizing the heterogeneity of fracture networks because it is sensitive to clustering effects, whereas *D* is not. [Zhu 2022, pp. 5-5, 6-7, 9-12]
- Natural fracture networks exhibit self-similarity, as indicated by negligible correlations between fractal/multifractal metrics (*D*, *Δα*) and observation scale across 80 outcrops. [Zhu 2022, pp. 9-12]
- Stochastic discrete fracture network models that use only line segments may oversimplify natural fracture networks, as evidenced by inconsistent correlations between *D* and *Δα* compared to real outcrops. [Zhu 2022, pp. 9-12]

## Candidate Concepts
- [[fractal dimension]]
- [[multifractal spectrum]]
- [[discrete fracture network]]
- [[box-counting method]]
- [[clustering effects]]
- [[self-similarity]]
- [[spanning cluster]]
- [[von Mises-Fisher distribution]]
- [[power-law distribution]]

## Candidate Methods
- [[box-counting method]]
- [[Taguchi design]]
- [[sensitivity analysis]]
- [[fracture detection algorithm]]
- [[Legendre transform]]

## Connections To Other Work
- Builds on the concept of fractals introduced by Mandelbrot (1977, 1982). [Zhu 2022, pp. 1-2]
- Extends multifractal formalism developed by Frisch and Parisi (1980) and Halsey et al. (1986). [Zhu 2022, pp. 2-2]
- Uses and critiques the conventional box-counting method for fracture analysis (Barton, 1995; Roy et al., 2007). [Zhu 2022, pp. 2-3, 3-4]
- Compares findings with prior work on fractal analysis of faults (e.g., Aviles et al., 1987; Cello, 1997) and multifractal properties of fracture networks (Berkowitz and Hadad, 1997; Cowie et al., 1995a). [Zhu 2022, pp. 1-2, 2-2]
- References the importance of fracture connectivity and topology (Sanderson and Nixon, 2015; Davy et al., 2013). [Zhu 2022, pp. 9-12]

## Open Questions
- How would incorporating more realistic 3D fracture geometries (e.g., tortuosity, T-type intersections) affect the fractal and multifractal characterizations? [Zhu 2022, pp. 9-12]
- Can the findings be extended to 3D subsurface fracture networks, given current data acquisition limitations? [Zhu 2022, pp. 9-12]

## Source Coverage
All non-empty indexed fragments were processed. The coverage audit shows 12 indexed texts with 58,689 characters. The compiled source blocks total 12 with 55,344 characters, resulting in a coverage ratio by blocks of 1.0 and by characters of 0.943005. The source signature is `45ba739e0892bb23303aaa2b3bec547a37ef7138`.
