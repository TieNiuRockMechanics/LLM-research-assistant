---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2010-davy-a-likely-universal-model-of-fracture-scaling-and-its-consequence-for-crustal-hydromech-e3c4724e"
title: "A Likely Universal Model of Fracture Scaling and Its Consequence for Crustal Hydromechanics."
status: "draft"
source_pdf: "data/papers/A likely universal model of fracture scaling and its consequence for crustal hydromechanics.pdf"
collections:
citation: "Davy, P., et al. \"A Likely Universal Model of Fracture Scaling and Its Consequence for Crustal Hydromechanics.\" *Journal of Geophysical Research*, vol. 115, B10411, 2010, doi:10.1029/2009JB007043."
indexed_texts: "15"
indexed_chars: "72931"
nonempty_source_blocks: "15"
compiled_source_blocks: "15"
compiled_source_chars: "73254"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004429"
coverage_status: "full-index"
source_signature: "2a55440541e2b05cd11fc3722a33ddadd3be98b2"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:27:08"
---

# A Likely Universal Model of Fracture Scaling and Its Consequence for Crustal Hydromechanics.

## One-line Summary
A theoretical model proposes that most fracture systems are organized into a "dilute" regime of independently growing small fractures and a "dense" regime where growth is inhibited by larger fractures, leading to a universal self-similar density distribution that controls network connectivity and flow.

## Research Question
Why does power law scaling ubiquitously describe the density of fracture networks, and what fundamental properties of fracture growth and interaction give rise to this scaling? [Davy 2010, pp. 1-2]

## Study Area / Data
The model is tested against quantitative data from three exhaustive fracture network studies:
1.  Joint networks in the Hornelen Basin, Norway, mapped at outcrop scales from 18 to 720 m. [Davy 2010, pp. 4-5]
2.  Fracture maps (outcrops at 0.5–10 m and regional lineaments at 100 m–10 km) and deep boreholes from the Swedish Nuclear Fuel and Waste management company (SKB) investigation sites (Simpevarp and Laxemar). [Davy 2010, pp. 4-5]
3.  The San Andreas fault system map compiled by Jennings (1988). [Davy 2010, pp. 5-6]

## Methods
-   Derivation of a theoretical density distribution for the "dense" regime based on the statistical rule that a fracture stops growing when it intersects a larger one. [Davy 2010, pp. 2-3]
-   Basic 2-D numerical simulations to validate the mathematical model and estimate the dimensionless parameter *g*. Fractures were generated with a dilute distribution (exponent *a* = 2.3) and then modified by removing the shortest tip of any fracture intersecting a larger one. [Davy 2010, pp. 3-4]
-   Application of the Universal Fracture Model (UFM) equation to fit the density distributions of the three geological datasets. [Davy 2010, pp. 4-6]
-   Calculation of the percolation parameter for the combined dilute-dense model to analyze connectivity. [Davy 2010, pp. 8-10]

## Key Findings
-   Fracture systems are spatially organized into two regimes: a "dilute" regime for small fractures growing independently and a "dense" regime controlled by mechanical interactions. [Davy 2010, pp. 1-2]
-   The dense regime follows a self-similar power law distribution *n(l, L) = Dγ^D L^D l^{-(D+1)}*, where *D* is the fractal dimension of fracture centers and *γ* is a dimensionless parameter. This model is termed the likely Universal Fracture Model (UFM). [Davy 2010, pp. 2-3, 63-65]
-   The range of values for *D* and *γ* appears extremely limited, making the model quite universal. For 2-D networks, *D* is typically between 1.7 and 2, and *γ* is between 1 and 2. [Davy 2010, pp. 3-4, 65]
-   The transition length *l_c* between the dilute and dense regimes is about a few tenths of a kilometer for fault systems and a few meters for joints. [Davy 2010, pp. 1, 66]
-   UFM networks are in a critical state near the percolation threshold, with a large number of nodes carrying a large amount of flow, making hydraulic properties highly sensitive to small changes. [Davy 2010, pp. 1, 58-61]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Hornelen Basin joint density: *n(l, L) = 4.5 l^{-2.8} L^{1.8}*, with *γ* = 1.7 ± 0.2. | [Davy 2010, pp. 4-5] | Joint network, 2-D outcrop maps. | Fits the UFM form with *a = D + 1*. |
| Swedish outcrop (SKB) density: *n(l, L) = 4(±1) l^{-3} L^{2}*. | [Davy 2010, pp. 4-5] | Joint network, exhaustive sampling of fractures >50 cm. | Consistent with UFM. |
| San Andreas fault density: *n(l, L) = 4 l^{-2.7} L^{1.7}*. | [Davy 2010, pp. 5-6] | Fault network, 2-D trace map. | Fits faults >20 km up to 100 km. *D* = 1.7. |
| Numerical simulations: *γ* ≈ 1 for uniform/orthogonal orientations; *γ* ≈ 1.5–1.7 for two sets at 20°. | [Davy 2010, pp. 3-4] | 2-D toy model with strict intersection rule. | Validates UFM distribution and estimates *γ* range. |
| Percolation threshold reached when system size *L* is between 1.3 and 2 times the transition length *l_c*. | [Davy 2010, pp. 9-10] | Combined dilute-dense model with typical parameters (*γD*≈2, *d+1-a*≈0.8–1). | Shows UFM networks are near critical connectivity. |
| Flow distribution at percolation threshold has a long tail, indicating many critical nodes. | [Davy 2010, pp. 10-11] | UFM simulations compared to small-crack and power-law models. | Highlights critical state of UFM networks. |

## Limitations
-   The basic UFM rule (a fracture stops when intersecting a larger one) is a crude simplification of complex mechanical interactions. [Davy 2010, pp. 2-3]
-   The model may not apply to fracture systems whose growth is primarily controlled by an external force or constraint (e.g., layer thickness in some experiments). [Davy 2010, pp. 6-7, 66]
-   Testing scaling distributions requires exhaustive sampling of fracture networks, which is rarely achieved in geological studies. [Davy 2010, pp. 4]
-   The UFM fit for fault systems covers a very small range of lengths, making it difficult to distinguish from other functions like an exponential. [Davy 2010, pp. 7]

## Assumptions / Conditions
-   Fracturing is quasi-static, and growth is controlled by stress perturbations from neighboring fractures. [Davy 2010, pp. 1-2]
-   In the dense regime, the inhibiting role of large fractures on smaller ones is the dominant control on the density distribution. [Davy 2010, pp. 2-3]
-   Fracture centers are fractally distributed with dimension *D*. [Davy 2010, pp. 2-3]
-   The model is developed for 3-D networks, but 2-D trace data can be used for validation via stereological relationships. [Davy 2010, pp. 4]

## Key Variables / Parameters
-   **D**: Fractal (correlation) dimension of the fracture-center network. [Davy 2010, pp. 2-3]
-   **γ**: Dimensionless geometric parameter encompassing fracture correlations and orientations. [Davy 2010, pp. 2-3]
-   **a**: Density term (power law exponent) in the dilute regime distribution. [Davy 2010, pp. 2]
-   **l_c**: Transition length scale between the dilute and dense regimes. [Davy 2010, pp. 3]
-   **n(l, L)**: Number density of fractures of length *l* in a system of size *L*. [Davy 2010, pp. 2]
-   **p**: Percolation parameter controlling network connectivity. [Davy 2010, pp. 8]

## Reusable Claims
-   **Claim**: For dense fracture networks where growth is inhibited by larger fractures, the length density distribution follows *n(l, L) = Dγ^D L^D l^{-(D+1)}*.
    **Condition**: Applies when fracture growth is primarily limited by mechanical interaction with larger fractures (dense regime).
    **Limitation**: Does not apply if growth is controlled by external constraints like mechanical layer thickness. [Davy 2010, pp. 2-3, 6-7]
-   **Claim**: The fractal dimension *D* for 2-D fracture traces typically ranges from 1.7 to 2, and the parameter *γ* ranges from 1 to 2.
    **Condition**: Based on analysis of exhaustive outcrop maps and numerical simulations.
    **Limitation**: Values outside these ranges may occur but are considered unlikely for typical geological networks. [Davy 2010, pp. 3-4]
-   **Claim**: Fracture networks organized according to the UFM are in a critical state near the percolation threshold, resulting in a high sensitivity of flow properties to small changes in network geometry.
    **Condition**: For systems where the dense (UFM) regime is developed.
    **Limitation**: The exact hydraulic consequences depend on detailed intersection properties not fully captured by the geometric model. [Davy 2010, pp. 10-11]

## Candidate Concepts
-   [[Fracture scaling]]
-   [[Self-similar distribution]]
-   [[Dilute regime]]
-   [[Dense regime]]
-   [[Fractal dimension]]
-   [[Percolation threshold]]
-   [[Crustal hydromechanics]]
-   [[Universal Fracture Model (UFM)]]

## Candidate Methods
-   [[Numerical simulation]] of fracture growth and interaction.
-   [[Stereological analysis]] to relate 3-D fracture networks to 2-D traces.
-   [[Percolation theory]] applied to fracture network connectivity.
-   [[Power law fitting]] of fracture length distributions.

## Connections To Other Work
-   Builds on the ubiquity of power law scaling in fracture systems noted by many, including Bonnet et al. (2001). [Davy 2010, pp. 1-2]
-   The inhibiting role of large fractures is supported by work such as Segall and Pollard (1983) and Nur (1982). [Davy 2010, pp. 2-3]
-   The discussion of fault growth and localization connects to experimental and numerical work by Spyropoulos et al. (1999), Ackermann et al. (2001), and Hardacre and Cowie (2003b). [Davy 2010, pp. 5-7]
-   The analysis of connectivity and percolation extends concepts from Bour and Davy (1997, 1998) and Darcel et al. (2003b). [Davy 2010, pp. 8-10]

## Open Questions
-   What is the fundamental origin of the difference in transition length *l_c* between faulting (large) and jointing (small)? [Davy 2010, pp. 1, 66]
-   How do internal stresses (e.g., from thermal expansion, fluid pressure) specifically influence the fracture process and scaling in joint systems? [Davy 2010, pp. 8-9]
-   What are the detailed consequences of the UFM's critical connectivity for large-scale permeability and dispersivity? [Davy 2010, pp. 10-11]

## Source Coverage
All 15 non-empty indexed fragments were processed. The compiled source contains 73,254 characters from a total indexed character count of 72,931, resulting in a coverage ratio of 1.004. The coverage status is full-index.
