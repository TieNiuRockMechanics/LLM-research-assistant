---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2015-abdollahipour-numerical-investigation-of-effect-of-crack-geometrical-parameters-on-hydrauli"
title: "Numerical Investigation of Effect of Crack Geometrical Parameters on Hydraulic Fracturing Process of Hydrocarbon Reservoirs."
status: "draft"
source_pdf: "data/papers/2015 - Numerical investigation on the effect of crack geometrical parameters in hydraulic fracturing process of hydrocarbon reservoirs.pdf"
collections:
  - "审稿人让引用"
citation: "Abdollahipour, A., et al. \"Numerical Investigation of Effect of Crack Geometrical Parameters on Hydraulic Fracturing Process of Hydrocarbon Reservoirs.\" *Journal of Mining & Environment*, 22 Dec. 2015. Accessed 2026."
indexed_texts: "8"
indexed_chars: "35957"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "35212"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.979281"
coverage_status: "full-index"
source_signature: "135c0aa2494d8778345bc2e80238fbe31dba127e"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T15:56:00"
---

# Numerical Investigation of Effect of Crack Geometrical Parameters on Hydraulic Fracturing Process of Hydrocarbon Reservoirs.

## One-line Summary
Numerical investigation using higher order displacement discontinuity method (HODDM) to determine optimal crack spacing, length, and perforation phase angle for hydraulic fracturing in horizontal and vertical wells, validated against experimental and field data.

## Research Question
How do initial crack geometrical parameters (spacing, length, pattern, and perforation phase angle) influence hydraulic fracture propagation, crack interference, and production efficiency in hydrocarbon reservoirs?

## Study Area / Data
The study uses a generic 2D model based on field data [26] with a wellbore radius R=0.1 m, depth 2500 m, far-field principal stresses σv=64 MPa (vertical), σh=47 MPa (horizontal), internal pressure P=30 MPa. Rock properties: modulus of elasticity E=40 GPa, Poisson ratio ν=0.2, fracture toughness KIC=3 MPa√m (source lists “mMPa3”), compressive strength 110 MPa, tensile strength 17.5 MPa. The rock is assumed impermeable with uniform pressure in perforated fractures (PFs). Verification uses a central slant crack problem (analytical solution) and laboratory tests on rock-like specimens (σc=28 MPa, E=15 GPa, σt=3.81 MPa, ν=0.21). [Abdollahipour 2015, pp. 1-4]

## Methods
Higher order displacement discontinuity method (HODDM) with cubic displacement discontinuity elements and special crack tip elements (4 sub‑elements). Far‑field in‑situ stresses were transformed to local normal and shear stresses on each element and summed with boundary conditions. Stress intensity factors KI and KII were computed from opening and sliding displacement discontinuities using plane‑strain LEFM formulas. Crack initiation angle was determined by the maximum tangential stress mixed‑mode fracture criterion [27]. Propagation was modeled up to 20 steps. A normalized spacing factor β = S/L (S = spacing, L = fracture length) was introduced. Symmetry was exploited via image elements [39]. [Abdollahipour 2015, pp. 2-4]

## Key Findings
- For isolength perforated fractures, β=1.0 (spacing equals fracture length) yields the best combination of crack propagation and permeability, avoiding near‑wellbore tortuosity or pinching [Abdollahipour 2015, pp. 4-6]. For β<0.75, interference reduces propagation.
- When outer fractures are longer than inner ones (L1 > L2), near‑wellbore tortuosity increases; the optimum spacing for this configuration is β=2.0 [Abdollahipour 2015, pp. 6-8].
- When inner fractures are longer (L2 > L1), outer fractures may arrest early; best performance occurs at β=1.25 [Abdollahipour 2015, pp. 6-8].
- The best overall propagation occurs when all PFs are of equal length; the worst case is longer outer cracks [Abdollahipour 2015, pp. 8-9].
- In vertical wells with perforation phase angle φ=60°, best results occur at a starting angle β=30°; cracks oriented more than 45° from σH did not propagate [Abdollahipour 2015, pp. 8-9].
- With phase angle φ=120°, all PFs fully propagated except those exactly perpendicular to σH (β=30° and 90°). This phase angle yields better overall crack propagation than φ=60° [Abdollahipour 2015, pp. 8-9].
- Field data by Yu et al. [40] show that cumulative gas production increases with fracture spacing up to the fracture length, then plateaus, consistent with the isolength β=1 optimum [Abdollahipour 2015, pp. 4-6].

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| Isolength PFs: β=1, 1.5, 2 give complete propagation away from wellbore; β=1 recommended for higher permeability because closer cracks increase permeability. | [Abdollahipour 2015, pp. 4-6] | 2D HODDM, impermeable rock, σv=64 MPa, σh=47 MPa, uniform P=30 MPa, max. tangential stress criterion, 20 steps. | Agrees with Yu et al. [40] field observation: optimum spacing ≈ fracture length. |
| Longer outer cracks, inner short: increased tortuosity; β=2.0 is the best case. | [Abdollahipour 2015, pp. 6-8] | Same model; L1 > L2 (outer longer). | |
| Longer inner cracks: outer cracks arrested; β=1.25 is the best case. | [Abdollahipour 2015, pp. 6-8] | Same model; L2 > L1 (inner longer). | |
| Perforation phase angle φ=60°: only cracks within 45° of σH propagate; best at starting angle β=30°. | [Abdollahipour 2015, pp. 8-9] | Vertical well, same rock properties; starting angle β measured from σH. | |
| φ=120°: all cracks propagate except β=30° and 90° (perpendicular to σH); overall better than φ=60°. | [Abdollahipour 2015, pp. 8-9] | Vertical well. | |
| HODDM with 4 crack tip elements predicts SIFs with <0.2% error for the central slant crack problem. | [Abdollahipour 2015, pp. 3-4] | 45° slant crack, l/b=0.1; analytical KI=KII=σ√(πb) sin²β (and sinβ cosβ). | Validation of numerical method. |
| HODDM crack propagation paths match experimental results of rock-like specimens with three cracks under uniaxial compression (β=0°,45°,90°). | [Abdollahipour 2015, pp. 4-6] | Specimen geometry Figure 4; properties: σc=28 MPa, E=15 GPa, σt=3.81 MPa, ν=0.21. | Verification of propagation capability. |

## Limitations
- 2D plane‑strain model; real field conditions are three‑dimensional and involve fluid leak‑off, proppant transport, and pore‑pressure changes (not considered) [Abdollahipour 2015, pp. 1-2].
- Rock is assumed impermeable and subjected to uniform internal pressure in PFs; fluid flow and pressure gradients are neglected.
- Maximum propagation limited to 20 steps; long‑term interference and production decline beyond this are not captured.
- Validation cases limited to one specific laboratory specimen configuration and one field dataset (Yu et al. [40]).
- Only two perforation phase angles (60°, 120°) were analyzed; no continuous optimization was performed.

## Assumptions / Conditions
- Homogeneous, isotropic, linear elastic rock mass.
- Far‑field principal stresses are aligned with the wellbore: σH (horizontal, 47 MPa) and σv (vertical, 64 MPa). Wellbore axis horizontal or vertical as stated in each case.
- Crack initiation governed by the maximum tangential stress mixed‑mode fracture criterion [27] within the LEFM framework.
- All PFs are pressurized uniformly at P=30 MPa at the start of each step.
- Symmetry used so that only half of the wellbore domain is modeled, with image elements accounting for the missing half [39].
- Cubic DD elements and special crack tip elements are employed throughout; background element length held constant at 1 cm unless otherwise noted.

## Key Variables / Parameters
- β (spacing factor) = S/L, where S is fracture spacing (m) and L is fracture length (m).
- L1, L2: lengths of outer and inner perforated fractures when not equal (L1 > L2 or L2 > L1).
- Phase angle φ: 60° or 120° in vertical well perforation studies.
- Starting angle β (also called β in the phase‑angle section): inclination of the first crack set relative to σH.
- Far‑field stresses: σv = 64 MPa, σh = 47 MPa.
- Internal pressure: P = 30 MPa.
- Rock properties: E = 40 GPa, ν = 0.2, KIC = 3 MPa√m, compressive strength 110 MPa, tensile strength 17.5 MPa.
- Wellbore radius: R = 0.1 m; depth: 2500 m.

## Reusable Claims
- For isolength hydraulic fractures in horizontal wells under a stress regime with σv > σh, arranging the spacing equal to the fracture length (β = 1) avoids crack interference and promotes straight propagation, thereby optimizing permeability. This claim applies to homogeneous impermeable brittle rocks under 2D plane‑strain conditions with uniform internal pressure and crack initiation determined by the maximum tangential stress criterion. [Abdollahipour 2015, pp. 4-6, 8-9]
- Introducing unequal fracture lengths increases near‑wellbore tortuosity; the least productive configuration is longer outer fractures. The best performance for unequal lengths occurs at a spacing factor around 1.25–2 times the longer fracture length, depending on which set is longer. [Abdollahipour 2015, pp. 6-8]
- In vertical wells, a perforation phase angle of 120° outperforms 60°, enabling full propagation of all perforated fractures except those exactly perpendicular to the minimum horizontal stress direction. This finding holds under the same rock mechanical and stress assumptions. [Abdollahipour 2015, pp. 8-9]
- HODDM with four crack tip elements can predict mode‑I and mode‑II stress intensity factors within 0.2% of analytical solutions for a central slant crack, and accurately reproduces crack coalescence patterns observed in laboratory tests on rock‑like specimens. [Abdollahipour 2015, pp. 3-6]

## Candidate Concepts
- [[Fracture reservoir]]
- [[Hydraulic fracturing]]
- [[Crack propagation]]
- [[Crack interference]]
- [[Near-wellbore tortuosity]]
- [[Pinching (hydraulic fracture)]]
- [[Stimulated reservoir volume (SRV)]]
- [[Displacement discontinuity method (DDM)]]
- [[Higher order displacement discontinuity method (HODDM)]]
- [[Crack tip element]]
- [[Maximum tangential stress criterion]]
- [[Perforation phase angle]]
- [[Normalized spacing factor (β)]]
- [[Stress intensity factor (SIF)]]
- [[Crack arrest]]

## Candidate Methods
- [[Higher order displacement discontinuity method (HODDM)]]
- [[Cubic element formulation for DDM]]
- [[Special crack tip element for DDM]]
- [[Maximum tangential stress mixed mode fracture criterion]]
- [[2D HF propagation modeling with constant pressure internal boundary]]
- [[Image element symmetry in boundary element methods]]

## Connections To Other Work
- The isolength β=1 optimum aligns with the field production data of Yu et al. [40], where cumulative gas production increased with spacing until it equaled fracture length and then plateaued [Abdollahipour 2015, pp. 4-6, 8-9].
- The development of HODDM builds on earlier displacement discontinuity formulations by Shou & Crouch [32] and Fatehi Marji et al. [35] for higher‑order elements and special crack tip treatment [Abdollahipour 2015, pp. 2-4].
- The study’s focus on competing fracture propagation and interference extends prior numerical HF work (e.g., Zhang & Chen [20], Huang et al. [21]) by incorporating variable crack lengths and perforation phase angles [Abdollahipour 2015, pp. 1-2, 9-11].

## Open Questions
- How would the optimum β vary under different far‑field stress ratios or wellbore orientations? (Only one stress regime was tested.)
- What is the influence of fluid viscosity, leak‑off, and proppant transport on the observed crack interference patterns?
- Does the optimum β=1 hold for multi‑stage fracturing with more than four perforation clusters?
- Can a 3D HODDM implementation capture out‑of‑plane propagation and more realistic wellbore failure modes?
- What is the sensitivity of the perforation phase angle optimum to rock anisotropy and natural fracture networks?

## Source Coverage
All 8 non‑empty indexed fragments were processed. Compilation used 35,212 source characters out of 35,957 indexed characters (coverage ratio 0.979). Source signature: 135c0aa2494d8778345bc2e80238fbe31dba127e. No fragment omitted.
