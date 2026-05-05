---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2008-anderson-relating-permeability-to-the-structural-setting-of-a-fault-controlled-hydrothermal"
title: "Relating Permeability to the Structural Setting of a Fault-Controlled Hydrothermal System in Southeast Oregon, USA."
status: "draft"
source_pdf: "data/papers/Relating permeability to the structural setting of a fault-controlled hydrothermal system in southeast Oregon, USA.pdf"
collections:
citation: "Anderson, Todd R., and Jerry P. Fairley. \"Relating Permeability to the Structural Setting of a Fault-Controlled Hydrothermal System in Southeast Oregon, USA.\" *Journal of Geophysical Research*, vol. 113, 2008, B05402. doi:10.1029/2007JB004962."
indexed_texts: "13"
indexed_chars: "60770"
nonempty_source_blocks: "13"
compiled_source_blocks: "13"
compiled_source_chars: "61104"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.005496"
coverage_status: "full-index"
source_signature: "32b0c7c46fca38f8a6a07935143096594074352c"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:44:04"
---

# Relating Permeability to the Structural Setting of a Fault-Controlled Hydrothermal System in Southeast Oregon, USA.

## One-line Summary
A geostatistical analysis of surface temperature data at Mickey Hot Springs is used to infer the subsurface permeability structure and propose a conceptual model linking it to the geometry of the controlling fault system.

## Research Question
Can temperature data collected in a fault-controlled hydrothermal system be used to delineate the near-surface breakdown region of the controlling fault and provide insight into fault geometry and the stress field? [Anderson 2008, pp. 1-2]

## Study Area / Data
The study area is Mickey Hot Springs in the Alvord Basin of southeast Oregon, USA. [Anderson 2008, pp. 2-4] The site is underlain by Miocene volcanic rocks, primarily the Steens Basalt, and is located within a northeast-striking graben defined by range-front faults. [Anderson 2008, pp. 2-4] The data set consists of 1550 ground and spring temperature measurements collected over a 55 m x 236 m area during a one-day period in May 2004. Ground temperatures were measured on a 1 m x 2 m grid, and spring temperatures were based on 3-5 measurements per vent. [Anderson 2008, pp. 2-4]

## Methods
The analysis used a geostatistical approach involving indicator transforms and simulation. [Anderson 2008, pp. 4-5] First, indicator kriging (IK) was used to separate the temperature data into three distinct domains (low, medium, high) based on spatial statistics, using cutoffs of 27.2°C and 58.1°C. [Anderson 2008, pp. 4-5] Experimental indicator variograms were computed and modeled with nested exponential models to capture the spatial structure of each domain. [Anderson 2008, pp. 5-5] The domain geometries were estimated via IK on a 0.25 m x 0.25 m grid. [Anderson 2008, pp. 5-7] Within each domain, the continuous temperature data were transformed to normal scores and checked for bivariate normality. [Anderson 2008, pp. 5-7] Sequential Gaussian simulation (SGS) was then used to generate 100 equally probable realizations of the temperature field within each domain. [Anderson 2008, pp. 7-8] The realizations were averaged point-wise (E-type estimates), truncated by the IK domain boundaries, and superposed to create a composite temperature field. [Anderson 2008, pp. 7-8]

## Key Findings
The analysis delineated three temperature domains with distinct spatial correlation structures. [Anderson 2008, pp. 4-5] The high-temperature domain (>58.1°C) exhibited anisotropy with major and minor ranges oriented at 30° and 120°, respectively. [Anderson 2008, pp. 5-5] The authors propose that high-temperature zones correspond to areas of more intense fracturing (or larger fractures), representing the spatial pattern of the fault's breakdown region. [Anderson 2008, pp. 11-12] The observed distribution of two slightly curved, high-temperature bands is consistent with the site being located in either a fault tip-line region or a releasing step within an obliquely slipping fault interaction area. [Anderson 2008, pp. 12-12] The medium-temperature zones may correspond to regions of compressional or shear fractures or areas warmed by diffusion from high-temperature zones. [Anderson 2008, pp. 11-12]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 1550 temperature measurements were collected on a 1m x 2m grid in a 55m x 236m area. | [Anderson 2008, pp. 2-4] | Data collected over one day in May 2004 to minimize diurnal effects. | Ground temperatures assumed in approximate equilibrium with shallow (~0.1 m) subsurface fluids. |
| Indicator kriging divided the site into low (≤27.2°C), medium (27.2-58.1°C), and high (>58.1°C) temperature domains. | [Anderson 2008, pp. 4-5] | Cutoffs determined from analysis of nine decile-based indicator variograms. | Domains are interpreted to arise from different physical generating processes. |
| The high-temperature domain variograms showed anisotropy with major range at 30° and minor range at 120°. | [Anderson 2008, pp. 5-5] | Variogram maps and indicator plots used to detect anisotropy. | Directions may be oriented parallel/normal to the trace of fractures, but requires field verification. |
| The composite simulated temperature field shows two slightly curved, high-temperature bands on opposite sides of the study area. | [Anderson 2008, pp. 7-8, 11-12] | Result of 100 in-category SGS realizations averaged and superposed. | Pattern is interpreted as corresponding to areas of opening-mode fractures in a breakdown region. |
| The pod-like geometry and high average spring temperature (86.9°C for 35 springs) argue against a simple fault trace setting. | [Anderson 2008, pp. 8-11] | Comparison to structural settings defined by Curewitz and Karson [1997]. | Setting is more likely a fault tip-line, fault interaction, or locked intersection. |

## Limitations
The available data are insufficient to uniquely determine the structural setting of the springs. [Anderson 2008, pp. 12-12] The analysis is primarily descriptive and does not offer a physical explanation for the underlying drivers of the observed temperature distributions. [Anderson 2008, pp. 11-12] The relationship between temperature and permeability is only approximate and holds over a limited range. [Anderson 2008, pp. 11-12]

## Assumptions / Conditions
Temperature is treated as a proxy for permeability due to increased advective heat transport in areas of increased fracturing. [Anderson 2008, pp. 2-2] Ground temperature measurements are assumed to be in approximate equilibrium with shallow (~0.1 m) subsurface fluids. [Anderson 2008, pp. 2-4] The continuous temperature data within each domain are assumed to be multivariate normal, checked via bivariate normality. [Anderson 2008, pp. 5-7]

## Key Variables / Parameters
- **Temperature Domains**: Low (≤27.2°C), Medium (27.2-58.1°C), High (>58.1°C). [Anderson 2008, pp. 4-5]
- **Indicator Variogram Model Parameters**: Provided in Table 1 for each domain and direction. [Anderson 2008, pp. 5-5]
- **Simulation Variogram Model Parameters**: Provided in Table 2 for each domain (isotropic models). [Anderson 2008, pp. 7-8]

## Reusable Claims
- In fault-controlled hydrothermal systems, zones of high surface temperature can be used to infer the spatial extent of the near-surface breakdown region (zone of intense fracturing) associated with the controlling fault(s). [Anderson 2008, pp. 11-12, 12-12]
- Geostatistical indicator analysis can partition a temperature field into domains with distinct spatial correlation structures, which may correspond to different underlying physical mechanisms (e.g., different fracture modes or heat transport processes). [Anderson 2008, pp. 11-12]
- The geometry of high-permeability zones inferred from thermal data can provide constraints on the structural setting (e.g., fault tip-line vs. releasing step) when combined with fault mapping. [Anderson 2008, pp. 12-12, 12-13]

## Candidate Concepts
- [[Fault-controlled hydrothermal system]]
- [[Breakdown region]]
- [[Permeability structure]]
- [[Fault zone architecture]]
- [[Indicator kriging]]
- [[Sequential Gaussian simulation]]
- [[Geostatistical simulation]]
- [[Structural settings of hot springs]]

## Candidate Methods
- [[Indicator kriging]]
- [[Sequential Gaussian simulation]]
- [[Variogram analysis]]
- [[Geostatistical modeling]]
- [[Cross-validation]]

## Connections To Other Work
The study builds on and applies methods developed in previous geostatistical analyses of the Borax Lake fault system. [Anderson 2008, pp. 2-2, 8-11] It uses the structural classification of hydrothermal springs from Curewitz and Karson [1997]. [Anderson 2008, pp. 8-11] The interpretation of fracturing patterns references mechanical models of fault interaction and oblique slip, such as those by Crider [2001] and Connolly and Cosgrove [1999]. [Anderson 2008, pp. 11-12]

## Open Questions
Could the thermal data be used in a detailed model of the site stress-field to determine the actual structural setting uniquely? [Anderson 2008, pp. 8-11] Do the directions of anisotropy in the high-temperature domain (30° and 120°) correspond to the orientation of fractures, as proposed? This requires verification by additional fieldwork. [Anderson 2008, pp. 11-12]

## Source Coverage
All non-empty indexed fragments were processed. The compilation used 13 source blocks containing 61,104 characters, achieving a coverage ratio of 1.0 by blocks and 1.005 by characters relative to the indexed source. The coverage status is full-index.
