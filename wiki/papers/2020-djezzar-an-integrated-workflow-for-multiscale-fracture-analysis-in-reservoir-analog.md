---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-djezzar-an-integrated-workflow-for-multiscale-fracture-analysis-in-reservoir-analog"
title: "An Integrated Workflow for Multiscale Fracture Analysis in Reservoir Analog."
status: "draft"
source_pdf: "data/papers/An integrated workflow for multiscale fracture analysis in reservoir analog.pdf"
collections:
citation: "Djezzar, Sofiane, et al. \"An Integrated Workflow for Multiscale Fracture Analysis in Reservoir Analog.\" *Arabian Journal of Geosciences*, vol. 13, 2020, art. 161, doi:10.1007/s12517-020-5085-6."
indexed_texts: "18"
indexed_chars: "86669"
nonempty_source_blocks: "18"
compiled_source_blocks: "18"
compiled_source_chars: "86813"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.001661"
coverage_status: "full-index"
source_signature: "7bdd5bd339acce6f3099dc0fd0dc34dab3d0a743"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:30:17"
---

# An Integrated Workflow for Multiscale Fracture Analysis in Reservoir Analog.

## One-line Summary
An integrated workflow using outcrop data, satellite imagery, and digital elevation models is presented to characterize and model multiscale natural fractures in a Cambro-Ordovician reservoir analog in Algeria, aiming to predict subsurface fracture networks.

## Research Question
How can an integrated workflow be developed to characterize and model natural fractures at multiple scales (from outcrop to subsurface) in a reservoir analog, and what are the resulting fracture distributions, origins, and impacts on the sedimentary cover?

## Study Area / Data
The study area is located at the southern edge of the Mouydir basin, Saharan platform, Algeria, between latitudes 24°30′N and 28°00′N and longitudes 3°00′E and 6°00′E [Djezzar 2020, pp. 2-4]. It covers approximately 67,255 km² and includes outcrops of Cambro-Ordovician formations (Ajjers, In-Tahouite, Tamadjert) and the Precambrian basement [Djezzar 2020, pp. 18-20]. Data used include geological maps at a scale of 1:100,000, satellite images with 30 m resolution, and a digital elevation model (DEM) with 65 m resolution [Djezzar 2020, pp. 4-5]. Subsurface data from the Mouydir basin (2D seismic, well cores, borehole imagery) and a 3D seismic volume from the adjacent Ahnet basin were also referenced for context [Djezzar 2020, pp. 6-8].

## Methods
The workflow integrates two main methods. The first method focuses on outcrop analog analysis using surface data. Faults were detected and digitized from curvature and illumination attribute maps generated from the DEM, combined with geological maps and satellite images [Djezzar 2020, pp. 1-2]. Two observation scales were used: mega-scale (1:100,000) for major faults and mesoscale (1:25,000) for minor faults affecting specific formations [Djezzar 2020, pp. 4-5]. Analysis included determining fault sets, length distributions, correlation coefficients, power law coefficients, and fractal dimensions using FracaFlow software [Djezzar 2020, pp. 1-2]. 3D deterministic fault models were built for each stratigraphic unit (basement, Ajjers, In-Tahouite, Tamadjert) and then merged to create a unique global model [Djezzar 2020, pp. 17-18]. The second method, which is the subject of a separate paper, involves integrating subsurface data (gravity, petrophysical, hydrogeological, seismic, core, and borehole imagery) to build a subsurface fault model [Djezzar 2020, pp. 6-8].

## Key Findings
The fracture network in the study area is classified into seven major sets: N000, N040, N060, N090, N110, N130, and N150 [Djezzar 2020, pp. 8-11]. Fracture length distributions follow a power law, with exponents generally between 1.97 and 2.89 [Djezzar 2020, pp. 8-11]. The basement and all Cambro-Ordovician units are affected by similar fracture sets, indicating basement faults structured the sedimentary cover [Djezzar 2020, pp. 14-16]. The Tamadjert formation is the most fractured unit due to its tight sandstone lithology, while the In-Tahouite formation is the least fractured due to its shaly nature [Djezzar 2020, pp. 14-16]. Fractal analysis shows the networks are fractal, with dimensions ranging from 1.0573 to 1.7114 using the center distance algorithm [Djezzar 2020, pp. 16-17]. The major structures correspond to N-S-trending dextral strike-slip faults and NNW-SSE to N-S trending reverse faults, with two major fault corridors (Amguid and Idjerane spurs) defining the basin edges [Djezzar 2020, pp. 14-16].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 394 major faults digitized at 1:100,000 scale, classified into 7 sets (N000 to N150). | [Djezzar 2020, pp. 8-11] | Global Faults Network analysis. | Power law exponents range 1.97-2.42; correlation coefficients 0.93-0.97. |
| 761 faults digitized in the basement formation, classified into 5 sets (N000, N050, N090, N120, N160). | [Djezzar 2020, pp. 11-13] | Basement formation analysis at mesoscale. | Power law exponents range 2.36-2.89; correlation coefficients 0.89-0.97. |
| 492 faults digitized in the Ajjers formation, classified into 6 sets (N000, N050, N090, N110, N130, N150). | [Djezzar 2020, pp. 11-13] | Ajjers formation analysis at mesoscale. | Power law exponents range 2.19-3.12; correlation coefficients 0.89-0.96. |
| 172 faults digitized in the In-Tahouite formation, classified into 5 sets (N000, N040, N060, N090, N130). | [Djezzar 2020, pp. 13-14] | In-Tahouite formation analysis at mesoscale. | Power law exponents range 2.19-3.0; correlation coefficients 0.89-0.99. |
| 843 faults digitized in the Tamadjert formation, classified into 5 sets (N000, N040, N070, N090, N130). | [Djezzar 2020, pp. 13-14] | Tamadjert formation analysis at mesoscale. | Power law exponents range 2.37-2.81; correlation coefficients 0.91-0.97. |
| Global fracture network fractal dimension (Dm) = 1.7114 (center distance) and 1.57 (box-counting). | [Djezzar 2020, pp. 16-17] | Analysis of all 394 major faults. | Some individual sets show no fractal dimension due to insufficient data points. |
| Tamadjert formation is the most fractured unit; In-Tahouite is the least fractured. | [Djezzar 2020, pp. 14-16] | Comparison of fracture density across Cambro-Ordovician units. | Attributed to lithology: tight sandstones (Tamadjert) vs. shaly units (In-Tahouite). |
| 85% of fractures in the area are isolated, 13% intersect, and 2% are slay (connectivity line <1). | [Djezzar 2020, pp. 14-16] | Ternary plot analysis of fracture segment connectivity. | Implications for fluid flow depend on fracture hydraulic conductivity vs. matrix. |

## Limitations
The study relies on outcrop analog data to predict subsurface fracture networks, which involves inherent uncertainty [Djezzar 2020, pp. 1-2]. The Mouydir basin lacks 3D seismic data, and only old 2D seismic surveys and few wells exist [Djezzar 2020, pp. 2-4]. Some fracture sets showed no fractal dimension due to an insufficient number of fractures for analysis [Djezzar 2020, pp. 16-17]. The second method (subsurface integration) is not fully presented in this paper [Djezzar 2020, pp. 6-8].

## Assumptions / Conditions
The workflow assumes that fracture patterns observed at outcrops (reservoir analog) are representative of those in the subsurface reservoirs [Djezzar 2020, pp. 1-2]. It assumes that fracture length distributions follow a power law [Djezzar 2020, pp. 5-6]. The analysis assumes that curvature and illumination attributes applied to DEMs are robust tools for identifying fractures at outcrops [Djezzar 2020, pp. 18-20].

## Key Variables / Parameters
- Fracture orientation (fault sets)
- Fracture length distribution
- Fractal dimension
- Power law exponent (a)
- Correlation coefficient
- Fracture density
- Mechanical stratigraphy (lithology and unit thickness)

## Reusable Claims
- Curvature and illumination attributes derived from digital elevation models are effective for detecting and digitizing both major and minor fault networks at outcrops [Djezzar 2020, pp. 1-2].
- Fracture length populations in the studied Cambro-Ordovician analog follow a power law distribution, with exponents generally between 1.97 and 2.89 [Djezzar 2020, pp. 8-11].
- The fractal dimension of fracture networks, calculated using center distance and box-counting algorithms, ranges from 1.0573 to 1.7114, indicating a fractal nature [Djezzar 2020, pp. 16-17].
- The impact of basement faults on the overlying sedimentary cover is significant, as similar fracture sets affect both units, suggesting structural inheritance [Djezzar 2020, pp. 14-16].
- Fracture intensity is lithology-dependent; tight sandstone formations (e.g., Tamadjert) are more fractured than shaly formations (e.g., In-Tahouite) [Djezzar 2020, pp. 14-16].

## Candidate Concepts
- [[reservoir analog]]
- [[multiscale fracture analysis]]
- [[power law distribution]]
- [[fractal dimension]]
- [[mechanical stratigraphy]]
- [[structural inheritance]]
- [[fracture connectivity]]

## Candidate Methods
- [[curvature attribute analysis]]
- [[illumination attribute analysis]]
- [[fractal analysis]]
- [[3D deterministic fault modeling]]
- [[power law fitting]]

## Connections To Other Work
The study builds on previous work using curvature attributes for fracture detection [Lisle 1994; Roberts 2001; Gao 2013, cited in Djezzar 2020, pp. 1-2]. It references established concepts of power law length distributions in fracture sets [Davy et al. 1990, 1992; Bonnet et al. 2001, cited in Djezzar 2020, pp. 5-6]. The tectonic history and structural framework of the Saharan platform are based on regional studies [e.g., Haddoum et al. 2001; Zazoun 2001; Boudjema 1987, cited in Djezzar 2020, pp. 14-16, 18-20]. The workflow integrates concepts from fracture network characterization [Bour et al. 2002, cited in Djezzar 2020, pp. 5-6] and fractal geometry [Mandelbrot 1975; Bonnet et al. 2001, cited in Djezzar 2020, pp. 16-17].

## Open Questions
- How accurately can the outcrop-derived fracture models predict subsurface fracture networks and fluid flow in the Mouydir basin?
- What is the precise relationship between fracture connectivity (as indicated by the ternary plot) and effective permeability in these tight reservoirs?
- How do the post-Hercynian tectonic events specifically influence the fracture sets not attributed to the Hercynian orogeny?

## Source Coverage
All 18 non-empty indexed fragments were processed. The compiled source blocks total 18, with a compiled character count of 86,813, achieving a coverage ratio of 1.001661 by characters. The source signature is "7bdd5bd339acce6f3099dc0fd0dc34dab3d0a743", confirming full-index coverage.
