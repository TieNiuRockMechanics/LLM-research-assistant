---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2009-carpinteri-a-fractal-interpretation-of-size-scale-effects-on-strength-friction-and-fracture"
title: "A Fractal Interpretation of Size-Scale Effects on Strength, Friction and Fracture Energy of Faults."
status: "draft"
source_pdf: "data/papers/A fractal interpretation of size-scale effects on strength, friction and fracture energy of faults.pdf"
collections:
citation: "Carpinteri, Alberto, and Marco Paggi. \"A Fractal Interpretation of Size-Scale Effects on Strength, Friction and Fracture Energy of Faults.\" *Chaos, Solitons and Fractals*, vol. 39, 2009, pp. 540-546. doi:10.1016/j.chaos.2007.01.075. Accessed 2026."
indexed_texts: "5"
indexed_chars: "24834"
nonempty_source_blocks: "5"
compiled_source_blocks: "5"
compiled_source_chars: "24968"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.005396"
coverage_status: "full-index"
source_signature: "f53f8c411ebee43e392b6a3b737a657b446235a8"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:27:42"
---

# A Fractal Interpretation of Size-Scale Effects on Strength, Friction and Fracture Energy of Faults.

## One-line Summary
This paper proposes a unifying fractal geometry framework to explain the observed size-scale effects where large faults exhibit lower strength, lower friction coefficient, and higher fracture energy compared to small-scale laboratory specimens.

## Research Question
How can the anomalous size-scale effects on the strength, friction coefficient, and fracture energy of faults, from laboratory to planetary scale, be systematically interpreted?

## Study Area / Data
The study synthesizes and analyzes experimental data from multiple sources across different scales:
- Laboratory scale: Direct shear tests on rock joint replicas (specimen size b from 50 to 400 mm) by Bandis et al. [19].
- Intermediate scale: Borehole stress measurements (b from 2 to 10 m) by Brudy et al. [29] and Zoback et al. [30].
- Natural fault scale: Data from the Gole-Larghe fault zone in the Italian Alps (b ~ 1 km) by Di Toro et al. [26,28].
- Fracture energy data: Compiled laboratory and large-scale measurements from Li [33].

## Methods
The authors apply fractal geometry and Renormalization Group Theory to derive power-law scaling laws for mechanical properties. The key methodological steps are:
1.  Modeling the contact domain between rough fault surfaces as a fractal set with non-integer dimension.
2.  Deriving scaling laws for nominal normal pressure (σ₀), nominal shear strength (τ₀), and nominal friction coefficient (f₀) as functions of the characteristic linear size (b) and the fractal dimensions of the contact domains for normal (D_r) and shear (D_s) resistance.
3.  Extending the framework to the slip-weakening model to derive a scaling law for fracture energy (G), assuming the critical slip displacement (w_c) scales linearly with fault size (b).

## Key Findings
1.  The nominal shear strength (τ₀) decreases with increasing specimen size (b) according to a power law: log₁₀τ₀ = log₁₀τ* - (2 - D_s)log₁₀b. Experimental data from Bandis et al. [19] yield a fractal dimension D_s ≈ 1.66 for the shear contact domain [Carpinteri 2009, pp. 2-3].
2.  The nominal friction coefficient (f₀) decreases with increasing size (b) according to: log₁₀f₀ = log₁₀f* - (D_r - D_s)log₁₀b. A best-fit to combined laboratory, borehole, and natural fault data gives (D_r - D_s) ≈ 0.28, implying D_r ≈ 1.94 [Carpinteri 2009, pp. 3-5].
3.  The nominal fracture energy (G) scales with fault size (b) as G ∝ b^(D_s - 1). With D_s ≈ 1.66, this predicts an exponent of ~0.66. A best-fit to compiled data yields an exponent of 0.67, in close agreement [Carpinteri 2009, pp. 5-6].
4.  The proposed fractal interpretation provides a consistent explanation for data across all scales, challenging alternative explanations like melt lubrication that cannot account for intermediate-scale borehole data [Carpinteri 2009, pp. 3-5].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Scaling law for nominal shear strength: log₁₀τ₀ = log₁₀τ* - (2 - D_s)log₁₀b | [Carpinteri 2009, pp. 2-3] | Derived from fractal contact model and Renormalization Group Theory. | D_s is the fractal dimension of the shear contact domain. |
| Experimental determination of D_s ≈ 1.66 from shear tests on rock joint replicas. | [Carpinteri 2009, pp. 2-3] | Data from Bandis et al. [19], specimen sizes from 50 to 400 mm. | Supports the scaling law for shear strength. |
| Scaling law for nominal friction coefficient: log₁₀f₀ = log₁₀f* - (D_r - D_s)log₁₀b | [Carpinteri 2009, pp. 3-5] | Derived from a fractal Coulomb law linking normal and tangential stresses. | f* is the scale-invariant fractal friction coefficient. |
| Best-fit to friction data gives (D_r - D_s) ≈ 0.28, implying D_r ≈ 1.94. | [Carpinteri 2009, pp. 3-5] | Combined data from lab tests (Bandis et al.), boreholes (Brudy et al., Zoback et al.), and natural faults (Di Toro et al.). | Demonstrates consistent size-scale effect across 5 orders of magnitude in size. |
| Scaling law for fracture energy: G ∝ b^(D_s - 1) | [Carpinteri 2009, pp. 5-6] | Derived from slip-weakening model with τ₀ scaling and w_c ∝ b. | Assumes critical slip displacement scales linearly with fault size. |
| Best-fit to fracture energy data yields an exponent of 0.67. | [Carpinteri 2009, pp. 5-6] | Data compiled by Li [33], including lab and large-scale measurements. | Closely matches the predicted exponent of 0.66 from D_s ≈ 1.66. |

## Limitations
- The analysis assumes the contact domains for normal and shear resistance are characterized by single, constant fractal dimensions (D_r and D_s) across all scales.
- The scaling law for fracture energy relies on the assumption that critical slip displacement (w_c) scales linearly with fault size (b), based on the correlation by Scholz et al. [37] and Scholz [38].
- The model does not incorporate dynamic effects such as slip-weakening or rate-and-state dependent friction laws, which are alternative explanations for low fault strength.

## Assumptions / Conditions
- Fault surfaces are self-affine fractals with well-defined fractal dimensions [Carpinteri 2009, pp. 1-2].
- The applied normal load is a scale-invariant quantity [Carpinteri 2009, pp. 2-3].
- The fractal Coulomb law links the fractal normal and tangential stresses [Carpinteri 2009, pp. 3-5].
- The critical fault displacement (w_c) is positively correlated with fault length (b), specifically w_c ∝ b [Carpinteri 2009, pp. 5-6].

## Key Variables / Parameters
- **b**: Characteristic linear size of the specimen or fault.
- **D_r**: Fractal dimension of the contact domain for normal stress (found to be ~1.94).
- **D_s**: Fractal dimension of the contact domain for shear strength (found to be ~1.66).
- **σ₀**: Nominal normal pressure.
- **τ₀**: Nominal shear strength.
- **f₀**: Nominal friction coefficient.
- **G**: Fracture energy (energy release rate).
- **w_c**: Critical fault displacement.
- **σ*, τ*, f***: Scale-invariant fractal mean pressure, shear strength, and friction coefficient, respectively.

## Reusable Claims
- The nominal friction coefficient of faults decreases with increasing fault size according to a power law, with an exponent related to the difference in fractal dimensions of the normal and shear contact domains (D_r - D_s) [Carpinteri 2009, pp. 3-5].
- The fracture energy of faults scales with fault size to a power of approximately 0.66-0.67, which is a direct consequence of the fractal scaling of shear strength and the linear scaling of critical slip displacement [Carpinteri 2009, pp. 5-6].
- Fractal geometry provides a unifying framework that can consistently explain the size-scale effects on strength, friction, and fracture energy observed from laboratory to natural fault scales, challenging explanations based solely on dynamic weakening mechanisms like melt lubrication [Carpinteri 2009, pp. 3-5].

## Candidate Concepts
- [[Fractal geometry]]
- [[Self-affine fractals]]
- [[Renormalization Group Theory]]
- [[Size-scale effects]]
- [[Fractal contact mechanics]]
- [[Slip-weakening model]]
- [[Fractal friction]]

## Candidate Methods
- [[Fractal analysis of contact domains]]
- [[Power-law scaling derivation via Renormalization Group Theory]]
- [[Multi-scale experimental data synthesis]]

## Connections To Other Work
- Builds on the application of Renormalization Group Theory to disordered materials by Wilson [9] and earlier work by the authors on scaling laws for strength and toughness [10,11].
- Extends fractal contact analyses by Borri-Brunetto et al. [12,17] and Chiaia [18].
- Provides a fractal interpretation for the experimental size-scale effects on shear strength reported by Bandis et al. [19].
- Offers an alternative to the melt lubrication hypothesis proposed by Di Toro et al. [26] for explaining low fault friction.
- Discusses the scaling of critical slip displacement with fault size, referencing correlations by Marrett and Allmendinger [34], Gillespie et al. [35], Watterson [36], and Scholz et al. [37,38].

## Open Questions
- How do dynamic processes (e.g., seismic slip velocity, temperature rise) interact with the static fractal scaling laws proposed?
- Can the fractal dimensions D_r and D_s be predicted from measurable properties of fault gouge or surface topography?
- Does the linear scaling of critical slip displacement (w_c ∝ b) hold universally across different tectonic settings and fault types?

## Source Coverage
All non-empty indexed fragments were processed. The compilation is based on 5 indexed text blocks containing a total of 24,834 characters. The compiled page incorporates content from all 5 source blocks, resulting in 24,968 characters of source material. The coverage ratio by blocks is 1.0, and by characters is 1.005, indicating full-index coverage.
