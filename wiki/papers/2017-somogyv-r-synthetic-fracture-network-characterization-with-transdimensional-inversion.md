---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2017-somogyv-r-synthetic-fracture-network-characterization-with-transdimensional-inversion"
title: "Synthetic Fracture Network Characterization with Transdimensional Inversion."
status: "draft"
source_pdf: "data/papers/2017 - Synthetic fracture network characterization with transdimensional inversion.pdf"
collections:
citation: "Somogyvár, M., et al. \"Synthetic Fracture Network Characterization with Transdimensional Inversion.\" *Water Resources Research*, vol. 53, 2017, pp. 5104–23. DOI: 10.1002/2016WR020293."
indexed_texts: "19"
indexed_chars: "93380"
nonempty_source_blocks: "19"
compiled_source_blocks: "19"
compiled_source_chars: "93828"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004798"
coverage_status: "full-index"
source_signature: "80d51fcd9971bd718fe7aad9df256f4a7153bb2e"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:04:25"
---

# Synthetic Fracture Network Characterization with Transdimensional Inversion.

## One-line Summary
A novel transdimensional inversion method using reversible jump Markov Chain Monte Carlo (rjMCMC) is presented to reconstruct 2D cross-well discrete fracture network geometries from synthetic tracer tomography experiments [Somogyv 2017, pp. 1-1].

## Research Question
How can the geometry of a discrete fracture network (DFN) be characterized between boreholes using spatially distributed hydraulic and transport experiments, given that the number of fractures is unknown a priori? [Somogyv 2017, pp. 1-2].

## Study Area / Data
The study uses two synthetic test cases: a simple hypothetical DFN with one main connecting fracture and an outcrop-based DFN modeled after the Tschingelmad outcrop from the upper Aar valley in the Grimsel region of the Central Alps, Switzerland [Somogyv 2017, pp. 8-9]. Data are generated from simulated conservative tracer tomography experiments conducted in vertical cross-sections between two wells [Somogyv 2017, pp. 2-3].

## Methods
The methodology involves three main components:
1.  **Forward Modeling:** Conservative tracer transport is simulated using a fast implicit finite difference model that neglects matrix diffusion and assumes an impermeable matrix [Somogyv 2017, pp. 2-3].
2.  **Transdimensional Inversion:** The reversible jump Markov Chain Monte Carlo (rjMCMC) algorithm is used to iteratively update DFN geometries by adding, deleting, or shifting fracture segments, thereby varying the number of model parameters [Somogyv 2017, pp. 3-4].
3.  **Result Processing:** The ensemble of accepted DFN realizations is analyzed using fracture probability maps and multidimensional scaling (MDS) to identify probable fracture locations and cluster representative network geometries [Somogyv 2017, pp. 9-10].

## Key Findings
- The transdimensional inversion procedure successfully identifies major transport pathways in the investigated domain for both the simple hypothetical and outcrop-based cases [Somogyv 2017, pp. 11-12, 16-17].
- The method produces an ensemble of thousands of DFN realizations, which are used to generate fracture probability maps that highlight the locations of hydraulically active fractures [Somogyv 2017, pp. 11-12].
- Multidimensional scaling reveals clusters of equally probable DFN realizations, showing that multiple network geometries can fit the observed tracer data [Somogyv 2017, pp. 12-14].
- The inversion is sensitive to the discretization length, which controls the resolution of the reconstructed fractures [Somogyv 2017, pp. 16-17].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| The rjMCMC algorithm allows for the calibration of fracture geometries and numbers during inversion. | [Somogyv 2017, pp. 1-1] | Applied to 2D cross-well DFN reconstruction from tracer tomography. | Core methodological contribution. |
| The forward model uses a finite difference approach, assumes an impermeable matrix, and neglects matrix diffusion. | [Somogyv 2017, pp. 2-3] | Simulating conservative tracer transport in a DFN. | Approximation considered appropriate for formations like crystalline rock. |
| In the simple hypothetical case, the inversion identified the main connecting fracture and source-receiver connections with high probability. | [Somogyv 2017, pp. 11-12] | Ensemble of 30,000 realizations; 2000 discarded as burn-in. | Demonstrates method's capability on a simple geometry. |
| In the outcrop-based case, the fracture probability map reproduced the two loosely connected fractured zones of the original network. | [Somogyv 2017, pp. 16-17] | Ensemble of 30,000 realizations; 2000 discarded as burn-in. | Shows application to a more complex, field-derived geometry. |
| MDS mapping of the ensemble subset shows that realizations in the outcrop-based case are more similar to each other than in the hypothetical case. | [Somogyv 2017, pp. 16-17] | Applied to a thinned subset of 300 realizations. | Indicates less equivalent tracer pathways in the more complex case. |

## Limitations
- Small-scale fracture variations cannot be uniquely resolved, as adjacent fractures can yield similar tracer responses [Somogyv 2017, pp. 17-18].
- The method is currently implemented for 2D cross-sections; extending to 3D would increase computational time and reduce convergence rate [Somogyv 2017, pp. 17-18].
- The discrete nature of the DFN updates increases the risk of the algorithm becoming trapped in local minima compared to continuous problems [Somogyv 2017, pp. 14-16].
- The inversion does not calibrate fracture apertures, which are held constant [Somogyv 2017, pp. 3-4].

## Assumptions / Conditions
- The rock matrix is impermeable and does not react with the tracer; matrix diffusion is neglected [Somogyv 2017, pp. 2-3].
- Fracture conductivity follows the cubic law (parallel plate model) [Somogyv 2017, pp. 2-3].
- Fracture apertures are constant and uniform for each fracture set during inversion [Somogyv 2017, pp. 3-4].
- Prior statistical information (e.g., fracture length distribution, intensity) is available to guide the inversion [Somogyv 2017, pp. 3-4].
- Source and receiver points are connected to the DFN via fixed fractures, properties of which are assumed known from borehole measurements [Somogyv 2017, pp. 6-7].

## Key Variables / Parameters
- Fracture inclination and aperture (for each set) [Somogyv 2017, pp. 8-9].
- Discretization length (resolution of the forward model) [Somogyv 2017, pp. 4-6].
- Fracture intensity (total fracture length per area) [Somogyv 2017, pp. 4-6].
- Fracture length distribution (FLD), often approximated by a power law [Somogyv 2017, pp. 3-4].
- Likelihood variance (controls acceptance rate in rjMCMC) [Somogyv 2017, pp. 7-8].
- Probabilities for update moves (addition, deletion, shift) [Somogyv 2017, pp. 6-7].

## Reusable Claims
- Transdimensional inversion using rjMCMC can reconstruct the geometry of a discrete fracture network from tracer tomography data without fixing the number of fractures a priori [Somogyv 2017, pp. 1-1].
- Fracture probability maps derived from an ensemble of rjMCMC realizations can identify the locations of hydraulically active fractures relevant for transport [Somogyv 2017, pp. 11-12].
- The method is capable of exploring multiple, equally probable DFN realizations that fit the observed data, which can be analyzed using clustering techniques like multidimensional scaling [Somogyv 2017, pp. 12-14].
- The resolution of the reconstructed fracture network is controlled by the chosen discretization length [Somogyv 2017, pp. 16-17].

## Candidate Concepts
- [[discrete fracture network]]
- [[tracer tomography]]
- [[transdimensional inversion]]
- [[fracture probability map]]
- [[hydraulically active fracture]]
- [[fracture length distribution]]
- [[fracture intensity]]

## Candidate Methods
- [[reversible jump Markov Chain Monte Carlo]]
- [[Metropolis-Hastings-Green acceptance criterion]]
- [[multidimensional scaling]]
- [[fracture probability mapping]]
- [[implicit finite difference method]]

## Connections To Other Work
- The study builds on the suggestion by Dorn et al. [2013] to use variable dimension DFN inversion [Somogyv 2017, pp. 1-2].
- It applies the rjMCMC concept, popularized by Green [1995] and used in geosciences for seismic tomography (Bodin and Sambridge, 2009) and tracer tomography in porous media (Jiménez et al., 2016) [Somogyv 2017, pp. 3-4].
- It contrasts with continuum models (e.g., equivalent continuum, stochastic continuum) that approximate fractured rock as a heterogeneous porous medium [Somogyv 2017, pp. 1-2].
- It addresses the challenge of calibrating highly parameterized DFN models, which previous methods tackled by fixing fracture numbers or adjusting only hydraulic properties [Somogyv 2017, pp. 1-2].

## Open Questions
- How can the method be extended to three-dimensional DFN reconstruction? [Somogyv 2017, pp. 17-18].
- Can fracture apertures be included as inverted parameters, and what additional constraints or data would be required? [Somogyv 2017, pp. 17-18].
- How can the misfit calculation be refined (e.g., using weighted errors or travel times) to improve inversion performance? [Somogyv 2017, pp. 17-18].
- Can the framework integrate additional data types (e.g., from hydraulic tomography or near-surface geophysics) to reduce non-uniqueness? [Somogyv 2017, pp. 17-18].

## Source Coverage
All 19 non-empty indexed fragments were processed. The compiled source blocks total 19, with a compiled character count of 93,828. The coverage ratio by blocks is 1.0, and by characters is 1.004798, indicating full-index coverage [Coverage audit].
