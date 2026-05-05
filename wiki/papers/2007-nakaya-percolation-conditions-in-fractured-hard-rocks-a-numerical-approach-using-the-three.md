---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2007-nakaya-percolation-conditions-in-fractured-hard-rocks-a-numerical-approach-using-the-three"
title: "Percolation Conditions in Fractured Hard Rocks: A Numerical Approach Using the Three-Dimensional Binary Fractal Fracture Network (3D-BFFN) Model."
status: "draft"
source_pdf: "data/papers/Percolation conditions in fractured hard rocks A numerical approach using the three-dimensional binary fractal fracture network (3D-BFFN) model.pdf"
collections:
citation: "Nakaya, Shinji, and Kiminori Nakamura. \"Percolation Conditions in Fractured Hard Rocks: A Numerical Approach Using the Three-Dimensional Binary Fractal Fracture Network (3D-BFFN) Model.\" *Journal of Geophysical Research*, vol. 112, B12203, 2007, doi:10.1029/2006JB004670."
indexed_texts: "13"
indexed_chars: "61161"
nonempty_source_blocks: "13"
compiled_source_blocks: "13"
compiled_source_chars: "61466"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004987"
coverage_status: "full-index"
source_signature: "6f5a19da6a5b37132aeb7ae69be484a18de12add"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:37:34"
---

# Percolation Conditions in Fractured Hard Rocks: A Numerical Approach Using the Three-Dimensional Binary Fractal Fracture Network (3D-BFFN) Model.

## One-line Summary
This study numerically investigates fracture connectivity and percolation conditions in fractured hard rocks using a three-dimensional binary fractal fracture network (3D-BFFN) model, finding that percolation probability is controlled by three fractal geometric parameters and is independent of fracture orientation anisotropy.

## Research Question
The study aims to numerically clarify the percolation conditions in three-dimensional fracture networks, extending previous two-dimensional analyses, and to develop an analytical solution for percolation probability as a function of fractal parameters. It further seeks to apply this model to seismogenic fractures to assess its viability for predicting fluid percolation in natural systems [Nakaya 2007, pp. 1-2].

## Study Area / Data
The model is applied to seismogenic fractures determined from an earthquake catalogue for an offshore volcanic region between Miyake-jima Island (MI) and Kozu-shima Island (KI) off the Izu Peninsula, Japan. The data cover a 7-week earthquake swarm period from 26 June to 18 August 2000, compiled by the Japan Meteorological Agency (JMA), including events with magnitude M > 2 and depths between 10 and 20 km [Nakaya 2007, pp. 9-12].

## Methods
The study uses a Monte Carlo simulation with a three-dimensionally random binary fractal fracture network (3D-RBFFN) model. The model is characterized by three fractal parameters: the fractal dimension (D2) of the spatial distribution of fractures, the exponent (a) of the power-law cumulative fracture length distribution, and the maximum fracture length normalized by the domain length (lmax/L). Fracture networks are generated using a "fractal fragmentation" method for spatial distribution and assigned lengths and orientations (random or Fisher distribution). Percolation probability (P) is calculated as the frequency of percolation occurrences over J=30 iterations for each parameter set [Nakaya 2007, pp. 2-4].

## Key Findings
1.  Percolation probability (P) changes continuously with the three fractal parameters D2, a, and lmax/L, but is independent of any anisotropy in fracture orientations (Q) [Nakaya 2007, pp. 4-7].
2.  When a < 1.8 and lmax/L < 1.0, percolation seldom occurs (P < 0.1), independently of D2 and Q [Nakaya 2007, pp. 4-7].
3.  An analytical solution for percolation probability (P) as a function of D2, a, and lmax/L is derived for the 3D-RBFFN model [Nakaya 2007, pp. 4-7].
4.  Application to seismogenic fractures between MI and KI suggests that domains with P > 0.55 correspond to percolated domains (Pf = 1). The percolation probability P is mainly affected by errors involved in determining the parameter a during actual surveys [Nakaya 2007, pp. 12-14].
5.  The percolated zone within the seismogenic fracture networks reveals they formed from seismic-swarm-related fractures over a 7-week period related to dyke intrusion [Nakaya 2007, pp. 12-14].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Percolation probability P is independent of anisotropy in orientations Q. | [Nakaya 2007, pp. 4-7] | 3D-RBFFN model with random or Fisher distributions. | Based on numerical results for P=0.25, 0.5, and 0.75. |
| Percolation seldom occurs when a < 1.8 and lmax/L < 1.0. | [Nakaya 2007, pp. 4-7] | 3D-RBFFN model. | P is less than 0.1 under these conditions. |
| Analytical solution for P: P = [a - {0.0590(D2-3)^4 e^{-1.5L0} + 4.88 e^{-1.0L0}}] / [0.271(D2-3)^4 e^{-1.5L0} + 2.08 e^{-1.0L0}] | [Nakaya 2007, pp. 4-7] | 3D-RBFFN model, where L0 = lmax/L. | Derived from numerical fitting. |
| Domains with P > 0.55 are percolated domains. | [Nakaya 2007, pp. 12-14] | Application to seismogenic fractures between MI and KI. | Based on comparison with network connectivity search (Pf). |
| P is mainly affected by errors in determining a (from b-value). | [Nakaya 2007, pp. 12-14] | Application to earthquake data. | Standard error in b-value is the primary source of uncertainty in P. |

## Limitations
1.  The model does not cover heterogeneous (multifractal) fractal structure in the spatial distribution of fractures due to its primitive approach [Nakaya 2007, pp. 2-4].
2.  The application to seismogenic fractures is limited by the completeness of the earthquake catalogue, particularly the high minimum magnitude of completeness (Mc ~4.0) in the offshore region, which affects the accuracy of determining the parameter a [Nakaya 2007, pp. 12-14].
3.  The determination of lmax from the maximum observed magnitude (Mmax) can introduce errors, as Mmax may differ from the value estimated from the Gutenberg-Richter fit [Nakaya 2007, pp. 12-14].

## Assumptions / Conditions
1.  Fractures are binary (open or closed) and do not interact when they cut each other [Nakaya 2007, pp. 2-4].
2.  Fracture spatial distribution follows a fractal described by dimension D2, and length distribution follows a power-law with exponent a [Nakaya 2007, pp. 2-4].
3.  Fracture orientations are either randomly distributed or follow a Fisher (spherical normal) distribution [Nakaya 2007, pp. 2-4].
4.  The target domain is a cube of size L x L x L [Nakaya 2007, pp. 2-4].
5.  Percolation is defined as the existence of a connected fracture path from one opposite side of the cubic domain to the other [Nakaya 2007, pp. 2-4].

## Key Variables / Parameters
*   **D2**: Fractal dimension of the spatial distribution of fractures.
*   **a**: Exponent of the power-law cumulative fracture length distribution.
*   **lmax/L**: Maximum fracture length normalized by the domain length.
*   **P**: Percolation probability.
*   **Q**: Fracture orientations (random or Fisher distribution).
*   **lmin**: Minimum cutoff fracture length.
*   **nt**: Total number of fractures in the model.
*   **b**: b-value of the Gutenberg-Richter relationship for earthquakes.
*   **Mc**: Minimum magnitude of complete recording.
*   **Pf**: Network connectivity of seismogenic fractures (1 if percolated, 0 if not).

## Reusable Claims
*   In 3D binary fractal fracture networks, percolation probability is independent of fracture orientation anisotropy for random or Fisher distributions [Nakaya 2007, pp. 4-7].
*   Percolation is unlikely (P < 0.1) in 3D fracture networks when the length distribution exponent a < 1.8 and the normalized maximum fracture length lmax/L < 1.0 [Nakaya 2007, pp. 4-7].
*   A percolation probability P > 0.55 serves as a useful index to indicate that a three-dimensional fracture network domain is percolated, based on validation with seismogenic fracture data [Nakaya 2007, pp. 12-14].
*   The accuracy of percolation probability predictions from the 3D-BFFN model is primarily limited by errors in determining the length distribution exponent a from field or seismic data [Nakaya 2007, pp. 12-14].

## Candidate Concepts
*   [[fracture network]]
*   [[percolation threshold]]
*   [[fractal dimension]]
*   [[power-law distribution]]
*   [[seismogenic fracture]]
*   [[connectivity]]
*   [[hard rock]]

## Candidate Methods
*   [[Monte Carlo simulation]]
*   [[fractal fragmentation]]
*   [[correlation integral]]
*   [[Gutenberg-Richter relationship]]
*   [[maximum likelihood estimation]]

## Connections To Other Work
This study extends the two-dimensional binary fractal fracture network (2D-BFFN) model of Nakaya et al. [2003] to three dimensions. It builds upon theoretical and numerical work on fracture connectivity and percolation by Robinson [1983, 1984], Balberg et al. [1991], Bour and Davy [1997, 1998], de Dreuzy et al. [2000, 2001], and Darcel et al. [2003]. The application to seismogenic fractures relates to studies of fractal properties in seismicity by Kagan and Knopoff [1980], Hirata and Imoto [1991], and Nakaya and Hashimoto [2002].

## Open Questions
1.  How can the accuracy of determining the parameter a (from earthquake b-values) be improved in offshore or data-sparse regions to enhance percolation probability predictions?
2.  How applicable is the 3D-BFFN model and the derived percolation probability relationship to other volcanic regions or different tectonic settings?
3.  What is the effect of incorporating heterogeneous (multifractal) spatial distributions of fractures on the percolation conditions?

## Source Coverage
All 13 non-empty indexed fragments were processed. The compiled source blocks total 13, with a compiled character count of 61,466, representing a coverage ratio of 1.0 by blocks and 1.004987 by characters relative to the indexed text. The coverage status is full-index.
