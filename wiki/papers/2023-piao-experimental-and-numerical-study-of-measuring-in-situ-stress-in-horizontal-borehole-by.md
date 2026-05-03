---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-piao-experimental-and-numerical-study-of-measuring-in-situ-stress-in-horizontal-borehole-by"
title: "Experimental and Numerical Study of Measuring In-Situ Stress in Horizontal Borehole by Hydraulic Fracturing Method."
status: "draft"
source_pdf: "data/papers/2023 - Experimental and numerical study of measuring in-situ stress in horizontal borehole by hydraulic fracturing method.pdf"
collections:
citation: "Piao, Shenghao, et al. \"Experimental and Numerical Study of Measuring In-Situ Stress in Horizontal Borehole by Hydraulic Fracturing Method.\" *Tunnelling and Underground Space Technology*, vol. 141, 2023, 105363. Accessed 2026."
indexed_texts: "12"
indexed_chars: "56980"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "53859"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.945226"
coverage_status: "full-index"
source_signature: "88de6051432cca6b837a4d842a76ceccf8696d62"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:33:03"
---

# Experimental and Numerical Study of Measuring In-Situ Stress in Horizontal Borehole by Hydraulic Fracturing Method.

## One-line Summary
This paper derives a theoretical model for interpreting hydraulic fracturing (HF) data in horizontal boreholes, validates it through triaxial laboratory experiments on granite and finite-element simulations, and demonstrates that in-situ principal stresses can be conservatively estimated using simplified formulas under specified assumptions. [Piao 2023, pp. 1-1]

## Research Question
How can in‑situ stress magnitudes and directions be reliably measured in horizontal boreholes using the hydraulic fracturing method, given that existing interpretation principles are designed for vertical (or arbitrarily inclined) boreholes? [Piao 2023, pp. 1-1, 2-3]

## Study Area / Data
- **Field context**: Tianshan Shengli tunnel, China – a long, deep mountainous tunnel explored by horizontal directional geotechnical investigation. [Piao 2023, pp. 1-1]
- **Experimental rock**: 300 × 300 × 300 mm³ granite cubes, cored centrally (20 mm diameter), fitted with copper injection pipes. [Piao 2023, pp. 5-6]
- **Experimental triaxial load**: σ_x = 12 MPa, σ_y = 10 MPa, σ_z = 8 MPa; borehole parallel to Y-axis. [Piao 2023, pp. 5-6]
- **Injection rates tested**: 2 ml/min (Group A), 4 ml/min (Group B), 8 ml/min (Group C), 11 ml/min (Group D). [Piao 2023, pp. 5-6]
- **Numerical model**: Abaqus FEM with cohesive elements; granite properties: E = 16 GPa, ν = 0.25, permeability = 10⁻⁶ m/s, fluid leak‑off 10⁻¹⁴ m/Pa s; triaxial loads (σ_x = 10 MPa, σ_y = 8 MPa, σ_z = 12 MPa, borehole parallel to Z‑axis). [Piao 2023, pp. 9-10]

## Methods
1. **Theoretical derivation**: Enhance previous inclined‑borehole model (Peška et al. 1995, Hossain et al. 2000) for a horizontal wellbore parallel to σ_H. Solve for σ_H and σ_h using breakdown pressure (P_B), shut‑in pressure (P_S), and reopening pressure (P_r), assuming θ = 90° and a reverse‑faulting stress regime (σ_H > σ_h > σ_Z). [Piao 2023, pp. 3-5]
2. **Laboratory experiment**: True triaxial HF simulator with acoustic emission (AE) monitoring. Record P_B, P_S, P_r; map fractures via AE source localization; measure surface crack dimensions. [Piao 2023, pp. 5-6, 6-8]
3. **Numerical simulation**: Cohesive‑element insertion in Abaqus. Two injection rates simulated (2 ml/min and 11 ml/min). Compare stress clouds and pressure–time behavior with experiments; then use model to invert in‑situ stresses and test the theoretical formula. [Piao 2023, pp. 9-10]

## Key Findings
- **Theoretical formula for horizontal borehole**: In a reverse‑faulting regime with borehole parallel to σ_H, fracture initiates at the borehole bottom (θ = 90°), giving σ_h = P_S and σ_H = 3σ_h – P_r. [Piao 2023, pp. 4-5]
- **Fracture initiation location**: Unlike vertical wells, cracks initiate in the middle section of the horizontal borehole due to free fluid flow in the completion interval. [Piao 2023, pp. 8-9]
- **Injection rate effects**: Higher rates produce longer, narrower cracks (aspect ratio increases). P_B generally increases with rate, but at 11 ml/min (Group D) P_B decreased, attributed to leak‑off when injection exceeds the tip opening capacity. [Piao 2023, pp. 6-8, 8-9]
- **Pump‑pressure behavior**: Pressure rises non‑linearly; after P_B, the pressure cannot sustain fracture opening because only part of the fluid concentrates at the crack. [Piao 2023, pp. 8-9]
- **Numerical vs. experimental**: Max error < 15% for P_B, P_S, P_r. Discrepancies arise from mesh coarseness, fluid parameter settings, and pre‑existing joints in rock. [Piao 2023, pp. 9-10]
- **Formula validation**: Theoretical σ_H is slightly overestimated, σ_h slightly underestimated relative to design values; errors mostly < 20%. The formula is conservative and usable for design. [Piao 2023, pp. 10-11]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| σ_h = P_S ; σ_H = 3σ_h – P_r for horizontal borehole | [Piao 2023, pp. 4-5] | Borehole parallel to σ_H; reverse‑faulting stress (σ_H > σ_h > σ_Z); θ = 90°; impermeable, homogeneous, isotropic, elastic rock; no pore pressure | Initiation position perpendicular to σ_h assumed. |
| Fracture length increases, width decreases with injection rate (Group A: 107 mm, 1.3 mm; Group D: 180 mm, 0.4 mm) | [Piao 2023, pp. 6-8] | Triaxial 12/10/8 MPa, granite cubes, rates 2–11 ml/min | Aspect ratio from 82.3 (A) to 450 (D). |
| P_B positively correlated with injection rate, except Group D where P_B decreased | [Piao 2023, pp. 8-9] | Same as above | Leak‑off dominates at high rate (Linkov 2011). |
| Numerical simulation errors (vs. experiments): P_B 5.57‑6.65%, P_S 8.69‑11.74%, P_r 9.51‑14.41% | [Piao 2023, pp. 10-12] | Simulation loads σ_x=10, σ_y=8, σ_z=12 MPa; granite properties in Table 3 | Mesh refinement and sample heterogeneity account for differences. |
| Theoretical vs. design values: σ_H error 0.84‑19.2%, σ_h error 18.92‑23.62% for five stress levels | [Piao 2023, pp. 11-12] | Five design scenarios (σ_H/σ_h/σ_v from 12/10/8 to 20/18/16 MPa) | Conservative estimate: σ_H overpredicted, σ_h underpredicted. |

## Limitations
- The derived formulas do **not** account for injection rate, fluid viscosity, or borehole radius; they assume uniform pressure and zero leak‑off during initiation. [Piao 2023, pp. 11-11]
- Applicable only when: (1) no pre‑existing fractures in the test interval; (2) non‑aquifer, non‑saturated zone; (3) σ_v is the minimum principal stress; (4) rock has high permeability (e.g., granite). [Piao 2023, pp. 11-11]
- The numerical model is limited to a single, quasi‑3D fracture surface; full HF network formation is not simulated. [Piao 2023, pp. 11-11]
- Experimental rock samples contain natural joints that cause complex branching not captured in the homogeneous numerical model. [Piao 2023, pp. 6-8, 10-11]

## Assumptions / Conditions
- Borehole axis is **parallel** to the maximum horizontal principal stress σ_H. [Piao 2023, pp. 3-5]
- Rock is continuous, homogeneous, isotropic, linearly elastic, and impermeable. [Piao 2023, pp. 3-5]
- Stress regime: σ_H > σ_h > σ_Z (reverse faulting). [Piao 2023, pp. 3-5]
- Fracture initiates at θ = 90° (bottom of horizontal borehole). [Piao 2023, pp. 4-5]
- Pore pressure P_P is assumed zero. [Piao 2023, pp. 4-5]
- Tensile strength T is approximated as T = P_B – P_r. [Piao 2023, pp. 4-5]
- In numerical model, cohesive elements have zero thickness, same elastic properties as rock, damage initiated at 5 mm displacement. [Piao 2023, pp. 9-10]

## Key Variables / Parameters
- **In‑situ stresses**: σ_H (max. horizontal), σ_h (min. horizontal), σ_Z (vertical). [Piao 2023, pp. 3-5]
- **HF pressures**: breakdown pressure P_B, shut‑in pressure P_S, reopening pressure P_r. [Piao 2023, pp. 1-2]
- **Injection rate**: 2, 4, 8, 11 ml/min. [Piao 2023, pp. 5-6]
- **Fracture geometry**: length, width, aspect ratio. [Piao 2023, pp. 6-8]
- **Rock properties**: Young’s modulus 16 GPa, Poisson ratio 0.25, density 3000 kg/m³, permeability 10⁻⁶ m/s, fluid leak‑off 10⁻¹⁴ m/Pa s. [Piao 2023, pp. 9-10]

## Reusable Claims
- In a horizontal borehole aligned with σ_H and under reverse‑faulting conditions (σ_H > σ_h > σ_Z), the minimum horizontal stress equals the shut‑in pressure (σ_h = P_S), provided no pre‑existing fractures and pore pressure can be neglected. [Piao 2023, pp. 4-5]
- Under the same assumptions, the maximum horizontal stress can be approximated as σ_H = 3σ_h – P_r, assuming fracture propagation perpendicular to σ_h. [Piao 2023, pp. 4-5]
- The theoretical formula consistently overestimates σ_H and underestimates σ_h relative to design values, making it a conservative tool for tunnel support design. [Piao 2023, pp. 10-11]
- Laboratory HF in granite under triaxial loading shows that fracture geometry (length, width, aspect ratio) is strongly dependent on injection rate; faster rates produce longer, narrower fractures. [Piao 2023, pp. 6-8]
- The breakdown pressure P_B first increases with injection rate but may decrease if the rate exceeds the fracture‑tip opening capacity, causing fluid leak‑off. [Piao 2023, pp. 8-9]

## Candidate Concepts
- [[horizontal directional investigation]]
- [[in-situ stress measurement]]
- [[hydraulic fracturing (HF)]]
- [[horizontal borehole]]
- [[breakdown pressure]]
- [[shut-in pressure]]
- [[reopening pressure]]
- [[cohesive element method]]
- [[true triaxial testing]]
- [[acoustic emission (AE) source localization]]
- [[reverse faulting stress regime]]
- [[point stress criterion]]

## Candidate Methods
- [[hydraulic fracturing in-situ stress measurement in horizontal borehole]]
- [[laboratory hydraulic fracturing with true triaxial loading]]
- [[acoustic emission based fracture mapping]]
- [[finite element simulation with cohesive elements (Abaqus)]]
- [[inversion of in-situ stress from HF pressure records]]
- [[horizontal wellbore stress transformation using Euler angles]]

## Connections To Other Work
- **Inclined borehole models**: Extended work of Peška et al. (1995) and Hossain et al. (2000) to horizontal wellbores. [Piao 2023, pp. 3-5]
- **HF fundamentals**: Haimson (1978), Haimson & Zhao (1991), Rummel (1987), Leijon et al. (1989) provided basis for breakdown and scale effects. [Piao 2023, pp. 1-2]
- **Injection rate effects**: Similar to observations by Chuprakov et al. (2014) and Chen et al. (2016) in vertical wells; phenomena explained by Linkov (2011). [Piao 2023, pp. 6-8, 8-9]
- **Field application**: Ma et al. (2021) introduced horizontal directional investigation for the Tianshan Shengli tunnel. [Piao 2023, pp. 1-1]

## Open Questions
- What is the influenc an accurate measurement of the initiation angle θ on the calculated stresses, and how can θ be reliably determined in the field? [Piao 2023, pp. 11-11]
- How do fluid viscosity and injection rate specifically modify the relationship between P_B, P_s, P_r and in‑situ stress magnitudes? [Piao 2023, pp. 11-11]
- What are the characteristics of fully three‑dimensional fracture networks in horizontal boreholes, beyond the quasi‑3D surface studied here? [Piao 2023, pp. 11-11]
- Can the theoretical formulas be extended to cases where pore pressure and pre‑existing fractures are present? [Piao 2023, pp. 11-11]

## Source Coverage
All 12 non‑empty indexed fragments were processed. Coverage ratio by source blocks: 1.0 (12 of 12). Coverage ratio by characters: 0.945 (53,859 of 56,980 indexed characters).
