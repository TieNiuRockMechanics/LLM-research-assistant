---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-gao-discing-behavior-and-mechanism-of-cores-extracted-from-songke-2-well-at-depths-below-4"
title: "Discing Behavior and Mechanism of Cores Extracted from Songke-2 Well at Depths below 4,500 m."
status: "draft"
source_pdf: "data/papers/2022 - Discing behavior and mechanism of cores extracted from Songke-2 well at depths below 4,500 m.pdf"
collections:
  - "zotero new"
citation: "Gao, Mingzhong, et al. \"Discing Behavior and Mechanism of Cores Extracted from Songke-2 Well at Depths below 4,500 m.\" *International Journal of Rock Mechanics and Mining Sciences*, vol. 149, 2022, p. 104976."
indexed_texts: "15"
indexed_chars: "72633"
nonempty_source_blocks: "15"
compiled_source_blocks: "15"
compiled_source_chars: "68747"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.946498"
coverage_status: "full-index"
source_signature: "bf43712bd9f74312781107afe1cae1d2fac597f9"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T05:16:25"
---

# Discing Behavior and Mechanism of Cores Extracted from Songke-2 Well at Depths below 4,500 m.

## One-line Summary
This study reconstructs the 3D fracture morphology of disced cores from the Songke-2 well below 4,500 m, quantifies their surface roughness and intactness, and numerically analyzes the in-situ stress conditions leading to core discing, finding that discing patterns reflect stress states and fracture mechanisms combining tension and shear [Gao 2022, pp. 1-1][Gao 2022, pp. 13-13].

## Research Question
- What are the spatial geometric morphology and surface roughness characteristics of disced cores extracted from the Songke-2 well at depths below 4,500 m? [Gao 2022, pp. 1-1]
- How does the in-situ stress environment influence the formation of saddle-shaped fractures in disced cores, and what is the underlying fracture mechanism? [Gao 2022, pp. 3-3]
- Can a quantitative index be developed to assess the intactness of disced rock samples, and how does it vary with depth? [Gao 2022, pp. 10-11]

## Study Area / Data
- **Songke-2 Well**, Daqing City, Heilongjiang Province, China; part of the Cretaceous Continental Scientific Drilling Project in Songliao Basin (ICDP); total depth 7018 m, with cores obtained beginning at 4000 m [Gao 2022, pp. 3-4].
- Disced cores analyzed from two main depth intervals: 5724.63–5744.61 m (Huoshiling Formation, sedimentary rock) and 6430.80–6441.65 m (Basement, igneous rock) [Gao 2022, pp. 4-5] [Gao 2022, pp. 4-6].
- Stratigraphy below 4500 m: Shahezi Formation (sandstone, siltstone, conglomerate, mudstone interbeds) and Huoshiling Formation (dacite, andesite, tuff, mudstone) [Gao 2022, pp. 3-4].
- Mineral composition data (Table 1) for depths 4800 m, 5100 m, 5600 m, 6400 m: quartz, feldspar, pyrite, carbonate, mica, clay; porosity and hardness categories also reported [Gao 2022, pp. 3-4].
- Mechanical property trends in Songliao Basin: density, elastic modulus, and uniaxial compressive strength increase with depth; Poisson’s ratio decreases sharply around 4800 m then increases [Gao 2022, pp. 4-5].
- In-situ stress data compiled from literature for depths 828.5–4249 m in Songliao Basin (Table 5); general linear increase with depth, with σ_H > σ_V below ~2000 m [Gao 2022, pp. 12-13][Gao 2022, pp. 13-14].

## Methods
- **3D spatial morphology reconstruction**: PRINCE775 3D laser scanner (max. resolution 0.02 mm, precision 0.03 mm, scan area adjusted for core diameters of 120 mm (shallow) / 90 mm (deep)); 123 rock samples scanned [Gao 2022, pp. 4-6][Gao 2022, pp. 6-8].
- **Surface roughness calculation**: improved cubic covering method to compute fractal dimension `D` of fracture surfaces; two analysis schemes—same-scale nonconcentric method (multiple 1 mm² squares) and different-scale concentric method (rings from center to edge); CATIA reconstruction platform used for cutting [Gao 2022, pp. 6-8].
- **Integrity coefficient `I_DRS`**: defined as true volume of disced region / volume of cylinder with longest generatrix, adjusted for 68% core preservation (I_DRS = true_volume / (0.68 × cylinder_volume) × 100%); 49 typical saddle-shaped samples selected [Gao 2022, pp. 9-11].
- **Numerical simulation**: FLAC3D 6.0 software; Mohr-Coulomb constitutive model; cubic model (900 mm side length), core diameter 120 mm, borehole diameter 180 mm [Gao 2022, pp. 10-11].
  - Mechanical parameters for 6400 m (Table 4, Fig. 15): E derived from fitted equation E=3.4469e^(0.004h); density 2.75 g/cm³, μ=0.233, bulk modulus 2.783×10¹⁰ Pa, shear modulus 1.808×10¹⁰ Pa, cohesion 9.561×10⁷ Pa, friction angle 26°, tensile strength 1.200×10⁷ Pa [Gao 2022, pp. 10-11].
  - 28 initial in-situ stress factor ratios (σ_V, σ_H, σ_h) with σ_V = 173.16 MPa applied to top surface; boundaries zero initial velocity; excavation simulated after equilibration [Gao 2022, pp. 10-11].
  - Failure identified via maximum tensile stress theory; plastic failure distribution examined on Y-Z plane [Gao 2022, pp. 11-12].

## Key Findings
- **Morphology and roughness**:
  - Shallow (sedimentary, ~5700 m) cores exhibit thin discs with coarse, curved (saddle-shaped) fracture surfaces; deep (igneous, ~6400 m) cores are thicker with smooth, flat, horizontal surfaces [Gao 2022, pp. 4-6][Gao 2022, pp. 13-13].
  - Overall fractal dimension `D` shows a nonlinear trend with depth, peaking around 5000–5500 m; sedimentary `D` > igneous `D` [Gao 2022, pp. 6-8].
  - For sedimentary discs (~5730 m, group A), `D` increases from center to edge on both upside and downside surfaces; maximum roughness often located at specific edge positions, possibly linked to rock heterogeneity rather than pure unloading [Gao 2022, pp. 8-9].
  - For deep igneous discs (~6430–6452 m), `D` first increases then decreases from center to edge; central roughness suggests transformation of mode II to mode I cracks, but central low roughness indicates fracture may not initiate there; edge initiation likely [Gao 2022, pp. 9-10].
  - Energy dissipation reasoning: deep rocks release stored elastic energy rapidly under drilling disturbance, producing smoother fractures; fracture propagation speed influences roughness (higher speed → rougher surface) [Gao 2022, pp. 8-9][Gao 2022, pp. 9-10].
- **Integrity coefficient (`I_DRS`)**:
  - Rock samples above ~6000 m have lower `I_DRS` values (less intact, more saddle-shaped) than those below 6000 m, consistent with macroscopic observation [Gao 2022, pp. 9-11][Gao 2022, pp. 13-13].
- **Stress and mechanism**:
  - Only 13 of 28 initial stress cases produced a saddle-shaped distribution of maximum tensile stress extremum at the core stub [Gao 2022, pp. 11-12].
  - Saddle-shaped tensile stress distribution is much more probable under unequal triaxial in-situ stress conditions than under conditions where two horizontal stresses are equal [Gao 2022, pp. 11-12].
  - When max in-situ stress < 1.5 σ_V, saddle-shaped tensile stress patterns appear (e.g., cases 2–5, 9–11, 14); when max stress > 1.5 σ_V and horizontal stress difference ≥ vertical stress, a concave saddle-shaped pattern appears [Gao 2022, pp. 11-12].
  - In Songliao Basin, at depths >2000 m, σ_H > σ_V, meeting conditions for discing occurrence [Gao 2022, pp. 13-13].
  - Plastic failure analysis (Fig. 18) shows tensile failure at core root extending from outside to inside, with tensile failure primarily around core and shear failure in surrounding borehole; discing is a combined tension-shear process [Gao 2022, pp. 12-13].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| Sedimentary cores at ~5700 m have thin discs with coarse, saddle-shaped fractures; igneous cores at ~6400 m have thicker discs with smooth, flat, horizontal fractures. | [Gao 2022, pp. 4-6][Gao 2022, pp. 13-13] | Songke-2 well, depths 5724–5744 m and 6430–6441 m | Macroscopic observation; confirmed by 3D scanning. |
| Fractal dimension `D` of fracture surfaces peaks around 5000–5500 m; sedimentary `D` > igneous `D`. | [Gao 2022, pp. 6-8] | 123 rock samples, 3D laser scanning | Improved cubic covering method. |
| In sedimentary discs (~5730 m), `D` increases from center to edge; maximum roughness often occurs at specific edge positions. | [Gao 2022, pp. 8-9] | Core box numbers 3456, 3457, 3461 | Suggests influence of rock heterogeneity. |
| In deep igneous discs (~6400 m), `D` rises then falls from center to edge; central roughness indicates possible crack mode transition. | [Gao 2022, pp. 9-10] | Core box numbers 4206, 4210, 4212, 4219, group C | Edge initiation likely; principle of minimum energy applied. |
| `I_DRS` values lower above 6000 m than below, indicating reduced intactness in shallower disced cores. | [Gao 2022, pp. 9-11][Gao 2022, pp. 13-13] | 49 typical saddle‑shaped samples | Adjusted for 68% core preservation. |
| Saddle-shaped max. tensile stress extremum occurs in 13/28 initial stress cases; probability higher for unequal triaxial stress. | [Gao 2022, pp. 11-12] | FLAC3D simulation, σ_V = 173.16 MPa, 6400 m parameters | Mohr-Coulomb model; conditions listed in Table 3 (bold). |
| Plastic tensile failure at core root propagates from outside to inside; shear failure dominant in surrounding rock. | [Gao 2022, pp. 12-13] | Y-Z plane plastic failure distribution, FLAC3D | Supports combined tension‑shear discing mechanism. |
| Songliao Basin in-situ stress data show σ_H > σ_V below ~2000 m, satisfying discing stress criteria. | [Gao 2022, pp. 13-13][Gao 2022, pp. 12-13] | Literature compilation, depths 828–4249 m | See Table 5. |

## Limitations
- The numerical model uses FLAC3D, a continuous method, which cannot directly simulate fracture formation; failure is inferred from maximum tensile stress theory [Gao 2022, pp. 11-12].
- Mechanical parameters for 6400 m derived from fitting equation and limited triaxial tests (only two sets); tensile strength approximated empirically as one‑tenth of uniaxial strength [Gao 2022, pp. 10-11][Gao 2022, pp. 12-13].
- The `I_DRS` analysis was limited to 49 typical saddle‑shaped samples; rock samples with large surface defects or non‑typical shapes were excluded [Gao 2022, pp. 9-10].
- The study does not provide a direct link between quantified fracture roughness and absolute in‑situ stress magnitudes; only stress‑pattern probabilities are discussed [Gao 2022, pp. 4-6][Gao 2022, pp. 13-13].
- Roughness analysis of deep igneous cores used different‑scale concentric method; conclusions about crack initiation location rely on energy and numerical simulation arguments, not direct fractographic evidence [Gao 2022, pp. 9-10].

## Assumptions / Conditions
- Core discing is primarily driven by in‑situ stress disturbance during drilling/unloading [Gao 2022, pp. 1-2][Gao 2022, pp. 8-9].
- The improved cubic covering method accurately captures fracture surface roughness for 3D scanned disced cores [Gao 2022, pp. 6-8].
- The 68% core preservation ratio is representative for `I_DRS` calculations of Songke‑2 cores [Gao 2022, pp. 9-10].
- Elastic modulus‑depth relationship E=3.4469e^(0.004h) is valid for extrapolation to 6400 m [Gao 2022, pp. 10-11].
- Mohr-Coulomb plasticity with parameters from 6400 m represents deep rock behavior in numerical simulations [Gao 2022, pp. 10-11].
- The first strength theory (max. tensile stress) is an acceptable failure indicator for brittle deep rocks in a continuous model [Gao 2022, pp. 11-12].
- In‑situ stress factors in Table 3 cover the range of realistic Songliao Basin stress states for discing analysis [Gao 2022, pp. 10-11].

## Key Variables / Parameters
- Fractal dimension `D` (fracture spatial geometric morphology) via improved cubic covering method [Gao 2022, pp. 6-8].
- Integrity coefficient `I_DRS` = true volume of disced region / (0.68 × volume of cylinder with longest generatrix) × 100% [Gao 2022, pp. 9-10].
- Initial in‑situ stress ratios: σ_V, σ_H, σ_h (Table 3), with σ_V = 173.16 MPa [Gao 2022, pp. 10-11].
- Mechanical parameters at 6400 m: E = 33.38 GPa (from equation), μ = 0.233, bulk modulus 2.783×10¹⁰ Pa, shear modulus 1.808×10¹⁰ Pa, cohesion 9.561×10⁷ Pa, friction angle 26°, tensile strength 1.200×10⁷ Pa [Gao 2022, pp. 10-11].
- Depth ranges of continuous discing: 5724.63–5744.61 m and 6430.80–6441.65 m [Gao 2022, pp. 4-5][Gao 2022, pp. 4-6].

## Reusable Claims
- CLAIM: In the Songke‑2 well, cores from sedimentary strata (~5700 m) display thin, coarse‑surfaced saddle‑shaped discs, while cores from igneous strata (~6400 m) are thicker with smooth, flat, horizontal fracture surfaces. CONDITIONS: Depths >4500 m, Huoshiling Formation vs. basement rock. LIMITATIONS: Observation limited to two depth intervals. [Gao 2022, pp. 4-6][Gao 2022, pp. 13-13]
- CLAIM: Fractal dimension `D` of disced core fracture surfaces, calculated via the improved cubic covering method, shows a nonlinear trend with depth and is higher for sedimentary rocks than for igneous rocks. CONDITIONS: 3D laser‑scanned surfaces from 123 core samples; 1 mm² analysis squares. LIMITATIONS: Non‑typical samples excluded. [Gao 2022, pp. 6-8]
- CLAIM: In deep igneous disced cores (~6400 m), the fractal dimension `D` of fracture surfaces increases then decreases from center to edge, implying possible crack mode transition (mode II to mode I) and edge‑initiated fracture. CONDITIONS: Different‑scale concentric analysis; Songke‑2 well igneous core sections. LIMITATIONS: Inferred from roughness trend and minimum energy principle. [Gao 2022, pp. 9-10]
- CLAIM: The integrity coefficient `I_DRS`, defined as true disced‑region volume divided by 68% of the circumscribing cylinder volume, is lower for disced cores above 6000 m than below 6000 m, indicating higher intactness in deeper disced cores. CONDITIONS: 49 saddle‑shaped samples from Songke‑2 well. LIMITATIONS: Only saddle‑shaped samples considered; preservation factor 0.68 may be site‑specific. [Gao 2022, pp. 9-11]
- CLAIM: Numerical simulations show that saddle‑shaped distributions of extreme maximum tensile stress at the core stub are more likely under unequal three‑directional in‑situ stresses than under conditions with two equal horizontal stresses. CONDITIONS: Mohr‑Coulomb model, σ_V = 173.16 MPa, 28 lateral pressure coefficient combinations. LIMITATIONS: Continuous FLAC3D model; failure inferred from stress state. [Gao 2022, pp. 11-12]
- CLAIM: When the maximum in‑situ stress is < 1.5 σ_V, saddle‑shaped tensile stress patterns occur; when it exceeds 1.5 σ_V and horizontal stress difference ≥ vertical stress, a concave saddle‑shaped pattern appears. CONDITIONS: Examined numerical cases 2–5, 9–11, 14 and 6, 7, 12, 23, 24. LIMITATIONS: Specific to model geometry and parameters. [Gao 2022, pp. 11-12]
- CLAIM: Core discing is a combined tension‑shear process; tensile fracture at the core root propagates from outside to inside, while shear failure occurs primarily in the surrounding borehole rock. CONDITIONS: Based on FLAC3D plastic failure analysis of disced cores at 6400 m depth. LIMITATIONS: Not directly validated by micro‑fracture observations. [Gao 2022, pp. 12-13]

## Candidate Concepts
- [[core discing]]: cracking of a core into saddle‑shaped discs during drilling, associated with in‑situ stress disturbance [Gao 2022, pp. 1-2]
- [[fractal dimension of fracture surfaces]]: `D` used to quantify roughness; computed via improved cubic covering method [Gao 2022, pp. 6-8]
- [[integrity coefficient of disced rock sample (I_DRS)]]: volumetric index for intactness of disced cores, adjusting for core preservation [Gao 2022, pp. 9-10]
- [[saddle-shaped core fractures]]: concave fracture morphology linked to unequal tri‑axial stress and excavation unloading [Gao 2022, pp. 3-3][Gao 2022, pp. 10-11]
- [[tension-shear discing mechanism]]: core failure involving both tensile (mode I) and shear (mode II) components, with external‑to‑internal propagation [Gao 2022, pp. 12-13][Gao 2022, pp. 13-13]
- [[minimum energy dissipation principle in rock fracture]]: fracture mode selection favors lowest energy path; used to explain roughness trends [Gao 2022, pp. 9-10]
- [[in‑situ stress indicator via core discing]]: disc shape, thickness, and roughness reflect stress environment magnitude and anisotropy [Gao 2022, pp. 1-1][Gao 2022, pp. 13-13]

## Candidate Methods
- [[improved cubic covering method for fractal dimension]] [Gao 2022, pp. 6-8]
- [[same-scale nonconcentric surface roughness analysis]] [Gao 2022, pp. 6-8]
- [[different-scale concentric surface roughness analysis]] [Gao 2022, pp. 6-8]
- [[3D laser scanning reconstruction of fracture surfaces (PRINCE775)]] [Gao 2022, pp. 4-6]
- [[integrity coefficient I_DRS volume‑ratio calculation]] [Gao 2022, pp. 9-10]
- [[FLAC3D Mohr-Coulomb core discing simulation]] [Gao 2022, pp. 10-12]
- [[maximum tensile stress theory for brittle failure identification]] [Gao 2022, pp. 11-12]

## Connections To Other Work
- Previous research by Lu et al. (2018) suggested saddle‑shaped cores form after excavation in unbalanced in‑situ stress environments [Gao 2022, pp. 3-3].
- Jaeger and Cook (1963) linked core discing to tensile failure; Obert and Stephenson (1965) inferred shear failure [Gao 2022, pp. 1-2].
- Corthésy and Leite (2008) argued that discing can be caused by tensile, tensile‑shear, or shear plastic failures [Gao 2022, pp. 2-3].
- Huang et al. (2016) proposed time‑dependent axial stress/strain relationships for disc formation [Gao 2022, pp. 2-3].
- Kaga et al. (2003) linked core discing to minimum principal stress coinciding with drilling direction [Gao 2022, pp. 2-3].
- Liu et al. (1997) examined central vs. peripheral crack initiation in discing [Gao 2022, pp. 2-3].
- Zhang et al. (2014) studied discing using stress and energy principles [Gao 2022, pp. 8-9].
- Zhao et al. (2003) defined minimum energy consumption for dynamic rock failure (E_fmin = σ_i²/2E) used here for fracture‑energy reasoning [Gao 2022, pp. 8-9].
- Boudet et al. (1995) found that higher fracture speed produces rougher surfaces, supporting roughness‑energy interpretation [Gao 2022, pp. 9-10].
- In‑situ stress measurements in Songliao Basin were compiled from multiple sources (Zhang et al. 2001, Meng 2015, Shen et al. 2008, Tan 2009, Peng 2008, Zhang 2014) [Gao 2022, pp. 12-14].

## Open Questions
- Can the specific discing patterns (thickness, roughness, curvature) be directly inverted to quantify absolute in‑situ stress magnitudes, rather than only indicating stress state probabilities? [Gao 2022, pp. 4-6][Gao 2022, pp. 13-13]
- What is the role of rock heterogeneity, bedding, and vein intrusions in controlling the location of maximum roughness and fracture initiation during discing? [Gao 2022, pp. 6-8][Gao 2022, pp. 8-9]
- How do drilling parameters (e.g., bit type, rotation speed, cooling) interact with in‑situ stress to produce the observed variations in disc thickness and fracture smoothness? [Gao 2022, pp. 1-2][Gao 2022, pp. 4-6]
- Are the fracture‑initiation and propagation conclusions (outside‑to‑inside, mode‑II‑to‑mode‑I transition) directly verifiable through micro‑fractographic analysis or acoustic emission monitoring? [Gao 2022, pp. 9-10][Gao 2022, pp. 12-13]
- How does the `I_DRS` index correlate with conventional rock quality indices (e.g., RQD) and can it be standardized for different core diameters and preservation percentages? [Gao 2022, pp. 9-10]

## Source Coverage
- All 15 non‑empty indexed fragments were processed.
- Coverage ratio by blocks: 1.0
- Coverage ratio by characters: 0.9465 (68,747 compiled out of 72,633 indexed characters).
- Data coverage: full-index; single-pass-markdown compilation.
- Source signature: bf43712bd9f74312781107afe1cae1d2fac597f9.
