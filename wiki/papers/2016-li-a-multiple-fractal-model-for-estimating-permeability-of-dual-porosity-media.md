---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2016-li-a-multiple-fractal-model-for-estimating-permeability-of-dual-porosity-media"
title: "A Multiple Fractal Model for Estimating Permeability of Dual-Porosity Media."
status: "draft"
source_pdf: "data/papers/A multiple fractal model for estimating permeability of dual-porosity media.pdf"
collections:
citation: "Li, Bo, et al. \"A Multiple Fractal Model for Estimating Permeability of Dual-Porosity Media.\" *Journal of Hydrology*, vol. 540, 2016, pp. 659-669. doi:10.1016/j.jhydrol.2016.06.059. Accessed 2026."
indexed_texts: "13"
indexed_chars: "64890"
nonempty_source_blocks: "13"
compiled_source_blocks: "13"
compiled_source_chars: "65067"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.002728"
coverage_status: "full-index"
source_signature: "323c0dc4c7560f99afb2cbc2419e63df889a8920"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:28:25"
---

# A Multiple Fractal Model for Estimating Permeability of Dual-Porosity Media.

## One-line Summary
A multiple fractal model is proposed to estimate the permeability of dual-porosity media by incorporating the fractal properties of both fracture networks and porous matrices.

## Research Question
How can the permeability of dual-porosity media be estimated using a model that accounts for the fractal scaling laws governing the size distributions of both fracture apertures and pore/capillary diameters?

## Study Area / Data
The study is theoretical and uses model parameters. The validity of the fractal aperture distribution is verified by comparing calculated results with in-situ measurement data from Li and Zhang (2010) on compacted, cracked soil and from Xiong (2011) on fracture networks from the Three Gorges ship lock, Chongqing, China [Li 2016, pp. 6-7]. The model construction uses parameters such as model dimensions (L0, H0, W0), orientation angles (α, θ), fractal dimensions (De, Dp, Dtf, Dtp), and maximum apertures/diameters (emax, kmax) [Li 2016, pp. 7-9].

## Methods
The model assumes the porous matrix is a bundle of tortuous capillaries and that fracture networks are randomly distributed. The aperture distribution of fractures is verified to follow a fractal scaling law [Li 2016, pp. 3-4]. Analytical expressions are derived for the fractal aperture distribution (Eq. 9), total flow rate (Eq. 22), total equivalent permeability (Eq. 23), and a dimensionless permeability (K+) defined as the ratio of matrix permeability to fracture network permeability (Eq. 24) [Li 2016, pp. 4-5, 5-6]. Fluid flow in fractures obeys the cubic law, and flow in capillaries obeys the modified Hagen-Poiseuille equation [Li 2016, pp. 4-5]. The Monte Carlo method is used to generate fracture apertures [Li 2016, pp. 3-4].

## Key Findings
The dimensionless permeability (K+) is closely correlated with the structural parameters (α, θ, Dtf, Dtp, De, Dp, emax, kmax) of the dual-porosity media [Li 2016, pp. 7-9]. K+ is more sensitive to the fractal dimension for the size distribution of fracture aperture (De) than to that for pore/capillary diameter (Dp) [Li 2016, pp. 9-9]. The maximum pore/capillary diameter (kmax) has a greater impact on K+ than the maximum fracture aperture (emax) [Li 2016, pp. 9-9]. The dimensionless permeability calculated using the fractal aperture distribution has close values to those from models using a lognormal aperture distribution, especially when De < 1.5 [Li 2016, pp. 9-10].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Fractal aperture distribution follows N(≥e) = (emax/e)^De. | [Li 2016, pp. 3-4] | emin/emax ≤ 10^-3 | Necessary condition for fractal scaling. |
| Total flow rate in fractures Qf is given by Eq. (14). | [Li 2016, pp. 4-5] | 1 ≤ Dtf ≤ 2, 1 ≤ De ≤ 2, emin/emax ≤ 10^-3 | Simplified from Eq. (13) under these conditions. |
| Equivalent permeability of fracture networks Kf is given by Eq. (16). | [Li 2016, pp. 5-6] | Derived from Qf and Darcy's law. | |
| Equivalent permeability of porous matrix Km is given by Eq. (21). | [Li 2016, pp. 5-6] | Based on bundle of tortuous capillaries. | |
| Dimensionless permeability K+ = Km/Kf is given by Eq. (24). | [Li 2016, pp. 5-6] | Ratio of matrix to fracture permeability. | |
| K+ is more sensitive to De than to Dp. | [Li 2016, pp. 9-9] | Based on empirical fits (Eqs. 31a, 31b). | Exponent on De (1.92) > exponent on Dp (0.58). |
| kmax has a greater impact on K+ than emax. | [Li 2016, pp. 9-9] | Based on empirical fit (Eq. 31c). | Exponent on kmax (4.10) > exponent on emax (3.10). |
| K+ from fractal aperture distribution is close to that from lognormal distribution. | [Li 2016, pp. 9-10] | Especially when De < 1.5. | Difference generally within one order of magnitude. |

## Limitations
The model assumes all fractures cut through the entire model, which may not represent short fractures [Li 2016, pp. 10-10]. It assumes fracture walls are well-mated [Li 2016, pp. 4-5]. The model does not account for stress effects on aperture or complex fracture geometries like intersections and dead-ends [Li 2016, pp. 10-10].

## Assumptions / Conditions
The size distribution of fracture aperture follows the fractal scaling law, which requires emin/emax ≤ 10^-3 [Li 2016, pp. 3-4]. The porous matrix is represented by a bundle of tortuous capillaries whose diameter distribution follows a fractal scaling law [Li 2016, pp. 5-6]. Fluid flow in each fracture obeys the cubic law [Li 2016, pp. 4-5]. The fracture walls are well-mated, so the tortuosity dimension Dtf characterizes surface roughness [Li 2016, pp. 4-5].

## Key Variables / Parameters
- De: Fractal dimension for size distribution of fracture aperture.
- Dp: Fractal dimension for size distribution of pore/capillary diameter.
- Dtf: Fractal dimension of nonlinear streamline of fluid flow in fractures.
- Dtp: Fractal dimension of nonlinear streamline of fluid flow in pore/capillary.
- emax: Maximum fracture aperture.
- kmax: Maximum pore/capillary diameter.
- α: Orientation of fracture width direction.
- θ: Fracture plane dip with respect to flow direction.
- L0, H0, W0: Length, height, and width of the model.

## Reusable Claims
- The dimensionless permeability (K+) of dual-porosity media is more sensitive to the fractal dimension for fracture aperture distribution (De) than to the fractal dimension for pore/capillary diameter distribution (Dp) [Li 2016, pp. 9-9].
- The maximum pore/capillary diameter (kmax) has a greater impact on the dimensionless permeability than the maximum fracture aperture (emax) [Li 2016, pp. 9-9].
- For a first-order estimation, the dimensionless permeability calculated using a fractal aperture distribution yields values close to those from a lognormal aperture distribution, particularly when the fractal dimension De is less than 1.5 [Li 2016, pp. 9-10].
- The proposed multiple fractal model does not involve any empirical constants without clear physical meanings [Li 2016, pp. 1-1].

## Candidate Concepts
- [[dual-porosity media]]
- [[fractal dimension]]
- [[permeability]]
- [[fracture network]]
- [[porous matrix]]
- [[aperture distribution]]
- [[tortuosity]]
- [[cubic law]]
- [[fractal scaling law]]

## Candidate Methods
- [[fractal scaling law]]
- [[Monte Carlo method]]
- [[cubic law]]
- [[modified Hagen-Poiseuille equation]]
- [[box-counting method]]
- [[analytical modeling]]

## Connections To Other Work
The model extends previous fractal permeability models for porous media (e.g., Yu and Li, 2001; Yu and Cheng, 2002) and fractured media (e.g., Miao et al., 2015a; Liu et al., 2015) by incorporating both fracture and matrix fractal properties [Li 2016, pp. 1-2]. It addresses a gap where the fractal dimension for fracture aperture distribution was not included in prior models [Li 2016, pp. 2-3]. The work compares its results with models using lognormal aperture distributions [Li 2016, pp. 9-10].

## Open Questions
Future work could explore more sophisticated models that account for fractures of various lengths that do not necessarily cut through the entire model [Li 2016, pp. 10-10]. The influence of stress on the fractal parameters and permeability could be investigated.

## Source Coverage
All 13 non-empty indexed fragments were processed. The compiled source blocks total 13, with a coverage ratio by blocks of 1.0 and by characters of 1.002728, indicating full-index coverage.
