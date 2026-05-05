---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2017-ahokposi-modelling-groundwater-fractal-flow-with-fractional-differentiation-via-mittag-leff"
title: "Modelling Groundwater Fractal Flow with Fractional Differentiation via Mittag-Leffler Law."
status: "draft"
source_pdf: "data/papers/Modelling groundwater fractal flow with fractional differentiation via Mittag-Leffler law.pdf"
collections:
citation: "Ahokposi, D. P., Abdon Atangana, and D. P. Vermeulen. \"Modelling Groundwater Fractal Flow with Fractional Differentiation via Mittag-Leffler Law.\" *European Physical Journal Plus*, vol. 132, 2017, art. 165, doi:10.1140/epjp/i2017-11434-8."
indexed_texts: "8"
indexed_chars: "36110"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "36315"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.005677"
coverage_status: "full-index"
source_signature: "0ce1084f50c0907f81efbd599c5df6d9542874ed"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:33:44"
---

# Modelling Groundwater Fractal Flow with Fractional Differentiation via Mittag-Leffler Law.

## One-line Summary
This study proposes a new groundwater fractal flow model using the Atangana-Baleanu fractional derivative with a Mittag-Leffler kernel, proves the existence and uniqueness of its positive solution, and validates it against field data from fractured rock aquifers.

## Research Question
How can the limitations of classical and power-law-based fractional derivatives in modeling groundwater fractal flow be overcome to better represent the non-local, memory-dependent, and fractal nature of flow in complex fracture networks?

## Study Area / Data
The study uses experimental data from four constant discharge tests conducted in a typical fractured crystalline rock aquifer of the Northern Limb (Bushveld Complex) in the Limpopo Province, South Africa. The four boreholes (BPAC1, BPAC2, BPAC3, and BPAC4) are located on faults [Ahokposi 2017, pp. 1-2, 14-17]. Data collection followed SANS 10299-4:2003 standards, using a pump test rig with submersible pumps and a variable speed drive to maintain constant discharge rates [Ahokposi 2017, pp. 14-17].

## Methods
The authors employ the Atangana-Baleanu fractional derivative in the Caputo sense, which is based on a non-local and non-singular kernel given by the generalized Mittag-Leffler function [Ahokposi 2017, pp. 1-3]. They prove the existence and uniqueness of a positive solution for the new model using fixed-point theorems [Ahokposi 2017, pp. 3-5]. The model is solved numerically using three different schemes: implicit, explicit, and Crank-Nicholson methods [Ahokposi 2017, pp. 1-2, 5-14]. A numerical approximation for the fractional integral is derived and applied [Ahokposi 2017, pp. 7-8]. The stability of the solution method is analyzed [Ahokposi 2017, pp. 5-6].

## Key Findings
The new fractional model based on the Mittag-Leffler law provides a more suitable framework for modeling groundwater fractal flow than previous models based on classical or power-law fractional derivatives [Ahokposi 2017, pp. 1-2, 16-17]. The model's positive solution exists and is unique under certain conditions [Ahokposi 2017, pp. 3-5]. Numerical simulations show the model's behavior with varying fractal dimension (d) and parameter (θ) [Ahokposi 2017, pp. 12-13]. Comparison with experimental data from four boreholes using a fractional order α=0.75 shows agreement between the theoretical model and field observations [Ahokposi 2017, pp. 14-17].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| The Atangana-Baleanu fractional derivative is defined using the generalized Mittag-Leffler function. | [Ahokposi 2017, pp. 2-3] | α ∈ [0,1] | Derivative in Caputo sense. |
| The existence and uniqueness of a positive solution for the new model are proven using fixed-point theorems. | [Ahokposi 2017, pp. 3-5] | Assumes boundedness and Lipschitz conditions on the function f. | Proof relies on the contraction mapping principle. |
| Numerical solutions are derived using implicit, explicit, and Crank-Nicholson schemes. | [Ahokposi 2017, pp. 5-14] | Discretization of the spatial and temporal domains. | Includes recursive formulas for each scheme. |
| Field data from four constant discharge tests in fractured rock aquifers are compared to model simulations. | [Ahokposi 2017, pp. 14-17] | Boreholes BPAC1-BPAC4 in the Bushveld Complex, South Africa. | Fractional order α=0.75 used in comparison. |
| The new model is argued to be more suitable for real-world problems due to the non-local, non-singular kernel and memory effect. | [Ahokposi 2017, pp. 1-2, 16-17] | Contrasted with power-law fractional derivatives that have singularity at the origin. | The Mittag-Leffler function induces memory effects important for groundwater flow. |

## Limitations
The paper does not explicitly list limitations. However, the complexity of the new fractional model and the need for numerical solutions may present computational challenges. The validation is limited to a specific fractured crystalline rock aquifer type.

## Assumptions / Conditions
The model assumes the groundwater flow can be described by a fractal dimension (d) and an additional parameter (θ) [Ahokposi 2017, pp. 2-3]. The existence and uniqueness proofs assume the function f(r, t, h) is bounded and satisfies a Lipschitz condition [Ahokposi 2017, pp. 3-5]. The numerical stability analysis assumes the non-linear operator is Lipschitz [Ahokposi 2017, pp. 5-6].

## Key Variables / Parameters
- `h(r, t)`: Hydraulic head as a function of radius and time.
- `d`: Fractal dimension.
- `θ`: A parameter in the modified fractal flow equation.
- `K`: Hydraulic conductivity.
- `S₀`: Storativity.
- `α`: Fractional order (0 < α < 1).
- `AB(α)`: A normalization function for the Atangana-Baleanu derivative with properties AB(0)=AB(1)=1.
- `Eα`: Generalized Mittag-Leffler function.

## Reusable Claims
- The Atangana-Baleanu fractional derivative, based on the non-local and non-singular Mittag-Leffler kernel, is more suitable for modeling groundwater fractal flow than derivatives based on the singular power-law kernel, as it avoids unrealistic predictions near fractures and incorporates memory effects [Ahokposi 2017, pp. 1-2].
- For the proposed fractal flow model, a positive solution exists and is unique if the source term satisfies certain boundedness and Lipschitz conditions, and if a contraction constant K < 1 [Ahokposi 2017, pp. 3-5].
- The numerical solution of the fractional fractal flow model can be obtained stably using implicit, explicit, or Crank-Nicholson schemes when the condition `1 - (α/AB(α))K1 + (αT^α/(AB(α)Γ(α+1)))K2 < 1` holds, where K1 and K2 are Lipschitz constants [Ahokposi 2017, pp. 5-6].

## Candidate Concepts
- [[Fractal flow]]
- [[Fractional differentiation]]
- [[Mittag-Leffler function]]
- [[Atangana-Baleanu derivative]]
- [[Non-local kernel]]
- [[Fractured aquifer]]
- [[Fixed-point theorem]]
- [[Memory effect]]

## Candidate Methods
- [[Fixed-point theorem for existence and uniqueness]]
- [[Implicit numerical scheme]]
- [[Explicit numerical scheme]]
- [[Crank-Nicholson numerical scheme]]
- [[Perturbation method with integral transform]]
- [[Numerical approximation of fractional integral]]

## Connections To Other Work
The paper builds on Barker's generalized flow equation and variable flow dimension approach [Ahokposi 2017, pp. 1-2]. It addresses limitations of the model by Chang and Yortsos that used a fractal dimension D [Ahokposi 2017, pp. 1-2]. It improves upon the fractional model by Ninghu et al. (2015) which used the Caputo derivative with a power-law kernel [Ahokposi 2017, pp. 1-2]. The Atangana-Baleanu derivative used is introduced in works by Atangana and Baleanu (2016) [Ahokposi 2017, pp. 1-2].

## Open Questions
- How does the model perform for different types of fractured aquifers (e.g., karst, porous media with fractures)?
- What is the physical interpretation of the parameter θ in the context of fracture networks?
- How sensitive is the model to the choice of the fractional order α, and can it be estimated from field data?
- Can the model be extended to multi-dimensional or heterogeneous fracture systems?

## Source Coverage
All non-empty indexed fragments were processed. The compilation used 8 source blocks containing 36,110 characters. The compiled page contains 36,315 characters, resulting in a coverage ratio of 1.005677 by character count. The coverage status is full-index.
