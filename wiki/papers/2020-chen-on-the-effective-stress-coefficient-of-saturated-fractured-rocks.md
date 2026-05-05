---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-chen-on-the-effective-stress-coefficient-of-saturated-fractured-rocks"
title: "On the Effective Stress Coefficient of Saturated Fractured Rocks."
status: "draft"
source_pdf: "data/papers/On the effective stress coefficient of saturated fractured rocks.pdf"
collections:
citation: "Chen, Sicong, et al. \"On the Effective Stress Coefficient of Saturated Fractured Rocks.\" *Computers and Geotechnics*, vol. 123, 2020, 103564. doi:10.1016/j.compgeo.2020.103564."
indexed_texts: "9"
indexed_chars: "43224"
nonempty_source_blocks: "9"
compiled_source_blocks: "9"
compiled_source_chars: "43409"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.00428"
coverage_status: "full-index"
source_signature: "00889e4441376e0ff91f1e9c0b6a60d48290dce1"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T01:08:46"
---

# On the Effective Stress Coefficient of Saturated Fractured Rocks.

## One-line Summary
This study uses discrete element models to determine the effective stress coefficient for saturated fractured rocks, finding that classic effective stress laws for porous media are not applicable due to different volumetric deformation behaviors.

## Research Question
The main aim is to determine the effective stress coefficient of saturated fractured rocks and to investigate its sensitivity to fracture geometries and the mechanical properties of both the intact rock and the fractures [Chen 2020, pp. 1-2].

## Study Area / Data
The study uses numerical simulations with discrete fracture network models built in the discrete element code UDEC. Three types of models were built: regular fracture network I, regular fracture network II, and a random fracture network. The side length of the cubic model is 20 m, and a total of over 300 numerical simulations were performed [Chen 2020, pp. 3-4].

## Methods
Two methods based on discrete element models are presented to determine the effective stress coefficient:
1.  **Bulk Modulus Method (BMM):** Calculates the effective stress coefficient directly from the known bulk modulus of the intact rock and the equivalent bulk modulus of the fractured rock mass using the formula α = 1 - K/Ks [Chen 2020, pp. 2-3].
2.  **Equivalent Strain Method (ESM):** Indirectly determines the effective stress coefficient based on calculated equivalent strains from discrete element method simulations under applied stress and water pressure [Chen 2020, pp. 2-3].
The discrete element method (UDEC) is used, where fractures are treated as contact interfaces between deformable rock blocks, and a fully coupled hydro-mechanical approach is employed [Chen 2020, pp. 3-4].

## Key Findings
- The classic effective stress laws for porous media cannot be extended to fractured rocks, mainly due to different volumetric deformation behaviors [Chen 2020, pp. 1-2].
- The bulk modulus method is inappropriate for fractured rock masses; the equivalent strain method is used for analysis [Chen 2020, pp. 4-5].
- The effective stress coefficient (α) decreases as the normal stiffness (kn) and shear stiffness (ks) of the fracture increase [Chen 2020, pp. 5-8].
- The effective stress coefficient increases with increasing elastic modulus (Es) and Poisson's ratio (νs) of the intact rock [Chen 2020, pp. 5-8].
- The effective stress coefficient is largest in the regular fracture network I and smallest in the random fracture network [Chen 2020, pp. 5-8].
- An empirical model was proposed to predict the effective stress coefficient: α = S * Es * (1 + d * (ks/kn)) * log(kn) * (1 + w * νs) [Chen 2020, pp. 7-8].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| The effective stress coefficient decreases with increasing fracture normal stiffness (kn). | [Chen 2020, pp. 5-8] | Simulations with kn from 10 to 125 GPa/m. | Initial values 0.6-0.8 at kn=10 GPa/m, decrease to 0.1-0.5 at kn=125 GPa/m. |
| The effective stress coefficient generally decreases with increasing ratio of shear to normal stiffness (ks/kn). | [Chen 2020, pp. 5-8] | Simulations with ks/kn from 0.1 to 1.2. | Decrease rate changes at ks/kn=0.5. |
| The effective stress coefficient generally increases with increasing elastic modulus (Es) of the intact rock. | [Chen 2020, pp. 5-8] | Simulations with Es from 20 to 100 GPa. | Increase rate declines with higher Es. |
| The effective stress coefficient generally increases with increasing Poisson's ratio (νs) of the intact rock. | [Chen 2020, pp. 5-8] | Simulations with νs from 0.15 to 0.35. | Increase rate increases with higher νs. |
| The bulk modulus method is invalid for fractured rocks due to anisotropic volumetric deformation affected by Poisson's ratio and fracture shear stiffness. | [Chen 2020, pp. 10-11] | Comparison of BMM and ESM results. | BMM shows discontinuity and approaches infinity near Poisson's ratio of 0.5. |
| The proposed empirical model accurately describes variation trends of α with variables, except for high Es and νs. | [Chen 2020, pp. 8-9] | Model predictions vs. ESM results. | Deviations occur for high elastic modulus and Poisson's ratio. |

## Limitations
- The study assumes the elastic parameters of fractured rocks are identical under saturated and dry conditions, ignoring potential wetting-induced weakening [Chen 2020, pp. 9-10].
- Only drained conditions are considered [Chen 2020, pp. 9-10].
- Isolated fractures and fracture dead-ends are removed during modeling, which may affect results [Chen 2020, pp. 9-10].
- The scale of the fractured rock model (20 m side length) is fixed; the influence of scale is questionable [Chen 2020, pp. 9-10].
- Three-dimensional effects and unsaturated states are not considered [Chen 2020, pp. 9-10].
- There are no available experimental investigations on the effective stress coefficient in saturated fractured rocks to validate the numerical findings [Chen 2020, pp. 9-10].

## Assumptions / Conditions
- Rock blocks are treated as isotropic elastic materials [Chen 2020, pp. 3-4].
- Fracture shear strength is described by the Coulomb slip model [Chen 2020, pp. 3-4].
- Stress-displacement relations in normal and shear directions are linear, governed by fracture normal stiffness (kn) and shear stiffness (ks) [Chen 2020, pp. 3-4].
- The effective stress coefficient of a single rock fracture is assumed to be 1 in the simulations [Chen 2020, pp. 9-10].
- Drained conditions are applied, with constant vertical stress and increasing water pressure [Chen 2020, pp. 3-4].

## Key Variables / Parameters
- **Effective stress coefficient (α)**: The primary variable of interest.
- **Fracture normal stiffness (kn)**: A key mechanical property of fractures.
- **Fracture shear stiffness (ks)**: Often expressed as a ratio k = ks/kn.
- **Elastic modulus of intact rock (Es)**: A mechanical property of the rock matrix.
- **Poisson's ratio of intact rock (νs)**: A mechanical property of the rock matrix.
- **Fracture network geometry**: Includes regular (I, II) and random patterns, with characteristics like orientation, spacing, and density [Chen 2020, pp. 3-4].

## Reusable Claims
- For saturated fractured rocks, the effective stress coefficient (α) is not a constant (like 1 for Terzaghi) but depends on the mechanical contrast between intact rock and fractures. α decreases as fracture stiffness (kn, ks) increases and increases as intact rock stiffness (Es, νs) increases [Chen 2020, pp. 5-8, 10-11].
- The classic bulk modulus method (α = 1 - K/Ks) is invalid for fractured rocks because their volumetric deformation is anisotropic and sensitive to Poisson's ratio and fracture shear stiffness [Chen 2020, pp. 4-5, 10-11].
- The effective stress coefficient is influenced by the global geometry of the fracture network; more regular networks (e.g., orthogonal sets) yield a higher α than random networks [Chen 2020, pp. 5-8].
- An empirical model (Eq. 14) can predict α for saturated fractured rocks using parameters with clear physical meanings (Es, νs, kn, ks/kn, network geometry factor S) [Chen 2020, pp. 7-8].

## Candidate Concepts
- [[effective stress coefficient]]
- [[fractured rocks]]
- [[discrete element method]]
- [[discrete fracture network]]
- [[bulk modulus]]
- [[equivalent strain]]
- [[fracture stiffness]]
- [[poroelasticity]]

## Candidate Methods
- [[Bulk Modulus Method]]
- [[Equivalent Strain Method]]
- [[Discrete Element Method (UDEC)]]
- [[Monte Carlo simulation]] for generating random fracture networks [Chen 2020, pp. 3-4].

## Connections To Other Work
- The study builds on and critiques the classic effective stress laws of Terzaghi and Biot for porous media [Chen 2020, pp. 1-2].
- It references the work of Tuncay and Corapcioglu on the first effective stress law for saturated fractured porous rocks [Chen 2020, pp. 1-2].
- The numerical method for determining equivalent elastic compliance is based on Min et al. [Chen 2020, pp. 2-3].
- The findings are relevant to applications like injection-induced earthquakes, geothermal extraction, and CO2 sequestration mentioned in the introduction [Chen 2020, pp. 1-2].

## Open Questions
- How do fracture geometrical parameters like density, length, orientation, and configuration systematically affect the effective stress coefficient? [Chen 2020, pp. 8-9].
- What is the effect of isolated fractures and fracture dead-ends, which were removed in this study? [Chen 2020, pp. 9-10].
- Does the scale of the fractured rock mass influence the effective stress coefficient? [Chen 2020, pp. 9-10].
- How do three-dimensional effects and unsaturated conditions affect the coefficient? [Chen 2020, pp. 9-10].
- Can experimental investigations be designed to validate these numerical findings? [Chen 2020, pp. 9-10].

## Source Coverage
All non-empty indexed fragments were processed. The coverage audit indicates 9 indexed fragments with 43,224 characters, resulting in a coverage ratio of 1.0 by blocks and 1.00428 by characters, confirming full-index coverage [Coverage audit].
