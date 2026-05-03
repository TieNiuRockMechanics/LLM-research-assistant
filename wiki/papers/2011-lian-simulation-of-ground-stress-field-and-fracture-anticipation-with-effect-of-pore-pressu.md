---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2011-lian-simulation-of-ground-stress-field-and-fracture-anticipation-with-effect-of-pore-pressu"
title: "Simulation of Ground Stress Field and Fracture Anticipation with Effect of Pore Pressure."
status: "draft"
source_pdf: "data/papers/2011 - Simulation of ground stress field and fracture anticipation with effect of pore pressure.pdf"
collections:
citation: "Lian, P. Q., et al. “Simulation of Ground Stress Field and Fracture Anticipation with Effect of Pore Pressure.” *Theoretical and Applied Fracture Mechanics*, 22 Sept. 2011."
indexed_texts: "6"
indexed_chars: "29998"
nonempty_source_blocks: "6"
compiled_source_blocks: "6"
compiled_source_chars: "30123"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004167"
coverage_status: "full-index"
source_signature: "899a2c5bdbc63bc63ab1d2624f7d53da471916a2"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T14:20:41"
---

# Simulation of Ground Stress Field and Fracture Anticipation with Effect of Pore Pressure.

## One-line Summary

Triaxial compression tests on Kenkiyak pre-salt carbonate cores and ADINA finite element simulations that incorporate pore pressure reveal that effective confining pressure controls fracture mode progression, that simulated stress fields match acoustic emission and image‑log data, and that fracture density is highest on structural highs and near faults ( ~8 fractures/m ) while the southeast region is low ( ~1 fracture/m ) [Lian 2011, pp. 1-1, 4‑6, 6‑7].

## Research Question

How does pore pressure influence the tectonic stress field and fracture development in the Kenkiyak pre‑salt reservoir, and how can a numerical simulation that explicitly treats the rock as a porous medium with fault slip improve fracture anticipation compared with conventional approaches that ignore pore‑pressure effects? [Lian 2011, pp. 1-1, 1‑2]

## Study Area / Data

- **Location**: Kenkiyak pre‑salt oilfield, on the nose‑uplifted structure of Kenkiyak in the middle of the Ural‑Emba salt dome, eastern Caspian Basin [Lian 2011, pp. 1-2].
- **Reservoir**: Carboniferous KT‑II carbonate, low porosity (11.5 %), low permeability (0.82 × 10⁻³ µm²), abnormal high pore pressure (80 MPa, coefficient 1.84), normal temperature (91.57 °C), depth > 4180 m, heterogeneous [Lian 2011, pp. 1-2].
- **Structure**: Faults widely present in Carboniferous, mainly N–E and N–W directions; top‑structure map shown in Figure 1 [Lian 2011, pp. 1-2].
- **Cores for triaxial tests**: Eight samples from Well 8016, four from ~4100 m and four from ~4500 m, cut into columns (diameter 25 mm, length‑to‑diameter ratio 2∶1), ends ground to ASTM/ISRM parallelism [Lian 2011, pp. 2-4].
- **Validation wells**: Well 7001, Well 8001 (acoustic‑emission stress measurements); Well 8067, 8062, 8064, 7101 (imaging‑log fracture orientations) [Lian 2011, pp. 4-6].
- **Simulation domain**: 10 km × 10 km (100 km²), target layer thickness 207 m, plus 500 m extend layers above and below; five faults modelled with initial zero displacement [Lian 2011, pp. 4-6].

## Methods

1. **Triaxial compression tests with pore pressure**: HTHP triaxial equipment (TerraTek); eight oil‑drained cores divided into two groups, each tested at different combinations of confining pressure and pore pressure (see Table 1). After failure, cores were sectioned into thin sections to observe micro‑fracture patterns [Lian 2011, pp. 2-4].
2. **Finite‑element stress‑field simulation**: ADINA software used for a three‑dimensional elastic‑plastic model of the reservoir; rock treated as a fluid‑filled porous medium; pore pressure explicitly included; five faults assumed initially with no relative displacement but allowed to slip when force differences develop; 176 bodies, 109 440 grids. Three boundary‑condition scenarios applied:
   - (1) 110 MPa pressure on top surface, 40 MPa pore pressure, other boundaries constrained, model balanced;
   - (2) 110 MPa top pressure, 130 MPa on undersurface (simulating uplift), other boundaries constrained;
   - (3) 110 MPa top, 105 MPa N–S normal stress, 99 MPa E–W normal stress, undersurface constrained (lateral tectonic movement) [Lian 2011, pp. 4-6].
3. **Rock‑failure criteria**: Griffith (tension) and Mohr–Coulomb (shear) criteria define tensile rupture factor \(I_t = r_t / [r]\) and shear rupture factor \(I_n = s_n / [s]\) [Lian 2011, pp. 6-7].
4. **Total rupture rate**: \(I_{total} = a I_t + b I_n\), with \(a = 0.32\) and \(b = 0.68\) derived from core observations of tension‑ and shear‑failure proportions in Wells 234, 7001, 8001, 8016 [Lian 2011, pp. 6-7].
5. **Fracture‑density prediction (binary method)**:
   \[
   x = a_1 I^2 + a_2 \quad \text{for } I < I_c;\quad
   x = a_1 I^2 + a_2 + a_3 (A + a_4) \quad \text{for } I > I_c
   \]
   with critical rupture rate \(I_c = 0.8\) (corresponds to 80 % of peak stress). Coefficients \(a_1, a_2, a_3, a_4\) calibrated using fracture density, rupture rate, and strain energy \(A\) from four wells (Table 3). Resulting values: \(a_1 = 1.43\), \(a_2 = ‑0.05\), \(a_3 = 0.0125\), \(a_4 = ‑920\) [Lian 2011, pp. 6-7].
6. **Strain energy density**: \(dW/dV\) computed from effective stresses using Sih’s formula; minima of SED are interpreted as potential failure locations [Lian 2011, pp. 6-7].
7. **Validation**: Acoustic‑emission tests on Wells 7001 and 8001 compared with simulated stresses; image‑log rose diagrams used to check fracture orientation against maximum horizontal stress direction [Lian 2011, pp. 4-6].

## Key Findings

- **Fracture‑mode progression with effective confining pressure**: Thin sections show that as effective confining pressure increases, the sequence of fracture types is: shear plane → high‑angle crack → conjugate shear cracks → net fractures; rock texture damage becomes increasingly severe [Lian 2011, pp. 1-1, 2‑4].
- **Stress‑field simulation accuracy**: Simulated tectonic stresses at well locations match acoustic‑emission measured values within 5 % (Table 2). The maximum horizontal principal stress direction is NW–SE, consistent with image‑log‑derived fracture orientations (Figure 11) [Lian 2011, pp. 4-6].
- **Displacement and structure**: The total displacement from the simulation coincides with the practical formation map; fault displacements replicate the actual slip (Figure 10) [Lian 2011, pp. 4-6].
- **Pore‑pressure distribution**: Maximum simulated pore pressure reaches 105 MPa, exceeding the present formation pressure of 80 MPa, implying that new fractures could form to release overpressure [Lian 2011, pp. 4-6].
- **Fracture‑density heterogeneity**: Predicted fracture density varies widely: ~8 fractures/m on structural highs and near faults; ~1 fracture/m in the southeast part (Figure 14). Development is attributed to extrusion during tectonic movements and elevated pore pressure [Lian 2011, pp. 6-7].
- **SED as fracture indicator**: Strain‑energy‑density contours are similar to total failure factor distribution; SED minima correspond to potential fracture locations [Lian 2011, pp. 7-8].

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| “Shear plane, high angle crack, conjugate shear cracks and net fractures will gradually appear and the rock texture is damaged more and more seriously with the increase of effective conﬁning pressure.” | [Lian 2011, pp. 1-1, 2‑4] | Group 1: confining pressure 50–80 MPa, pore pressure 40 MPa; Group 2: confining pressure 85 MPa, pore pressure 0–60 MPa; cores from ~4100 m and ~4500 m. | Thin‑section analysis of eight samples; effective confining pressure ranged from 10 to 40 MPa (Group 1) and 25 to 85 MPa (Group 2). |
| “The simulation results indicate that the total displacement coincides with the practical formation, the simulated tectonic stress ﬁts with the values measured by acoustic emission testing, and the direction of major horizontal principal stress is consistent with the imaging log interpretation data.” | [Lian 2011, pp. 1-1, 4‑6] | Three boundary‑condition scenarios; rock modelled as porous medium with pore pressure; five faults with slip allowed. | Error <5 % for Wells 7001, 8001; NW–SE maximum horizontal stress matches rose maps of Wells 8067, 8062, 8064, 7101. |
| “The highest pore pressure in the simulated zone is up to 105 MPa, the present formation pressure is 80 MPa, lower than the highest pore pressure in the simulation.” | [Lian 2011, pp. 4-6] | Simulation with fault‑screening effect and undrained fluid in fault‑controlled blocks. | Suggests new fractures may generate to decompress. |
| “Cracks develop easily on the structural high position and near the fault (about 8 fractures per meter). However, the southeast part has low fracture density (about 1 fracture per meter).” | [Lian 2011, pp. 6-7] | Binary method with \(a_1=1.43, a_2=-0.05, a_3=0.0125, a_4=-920\); calibrated with Wells 234, 7001, 8001, 8016. | \(I_c = 0.8\); coupling of extrusion and elevated pore pressure drives fracturing. |
| “Strain energy density (SED) contours … correspond to the minima SED.” and “may be constructed to predict potential locations of fracture” | [Lian 2011, pp. 7-8] | SED computed from simulated effective stress tensors using \(E, \nu\). | SED distribution similar to total failure factor cloud. |

## Limitations

The paper does not explicitly discuss limitations; the following are inferred from the described methodology and data:

- The triaxial tests used only eight cores from two depth intervals in a single well (Well 8016); the results may not capture the full range of mechanical variability in the heterogeneous carbonate reservoir [Lian 2011, pp. 2-4].
- Fracture‑density calibration of the binary method relies on measurements from only four wells; the coefficients \(a_1, a_2, a_3, a_4\) are site‑specific [Lian 2011, pp. 6-7].
- The finite‑element simulation assumes elastic‑plastic behaviour with static boundary conditions; time‑dependent effects (e.g., pore‑pressure diffusion during tectonic events) are not explicitly modelled [Lian 2011, pp. 4-6].
- The critical rupture rate \(I_c = 0.8\) (80 % of peak stress) is based on general rock‑mechanics experiments; its applicability to the specific reservoir units is not independently verified [Lian 2011, pp. 6-7].

## Assumptions / Conditions

- Rock is a porous elastic‑plastic medium fully saturated with fluid; Terzaghi’s effective stress theorem is adopted: \(\sigma = S - P\) [Lian 2011, pp. 1-2, 4‑6].
- Faults are initially locked (zero relative displacement) but can slip when differential forces develop [Lian 2011, pp. 1-1, 4‑6].
- Fracture initiation follows Griffith (tension) and Mohr–Coulomb (shear) criteria [Lian 2011, pp. 4-6].
- Total rupture rate is a linear combination of normalized tensile and shear failure factors, with proportions \(a=0.32\) and \(b=0.68\) obtained from core observation [Lian 2011, pp. 6-7].
- Fracture density below the threshold \(I_c = 0.8\) is a quadratic function of rupture rate; above \(I_c\), it additionally depends linearly on strain energy [Lian 2011, pp. 6-7].
- Pore‑pressure increase in fault‑controlled blocks due to fluid entrapment and tectonic extrusion is a key driver of fracturing [Lian 2011, pp. 4-6, 6‑7].

## Key Variables / Parameters

| Variable/Parameter | Description / Value | Source |
|-------------------|---------------------|--------|
| Pore pressure, \(P\) | 40 MPa (triaxial test, group 1), 0–60 MPa (group 2); present reservoir 80 MPa; simulation up to 105 MPa | [Lian 2011, pp. 2-4, 4‑6] |
| Confining pressure | 50–85 MPa (triaxial tests) | [Lian 2011, pp. 2-4] |
| Effective confining pressure | Confining pressure – pore pressure | [Lian 2011, pp. 2-4] |
| Compressive resistance | 78–403.2 MPa (Table 1) | [Lian 2011, pp. 2-4] |
| Young’s modulus, \(E\) | 36 060–62 310 MPa | [Lian 2011, pp. 2-4] |
| Poisson’s ratio, \(\nu\) | 0.15–0.34 | [Lian 2011, pp. 2-4] |
| Bulk modulus | 26 600–62 450 MPa | [Lian 2011, pp. 2-4] |
| Tensile rupture factor, \(I_t\) | \(I_t = r_t / [r]\) | [Lian 2011, pp. 6-7] |
| Shear rupture factor, \(I_n\) | \(I_n = s_n / [s]\) | [Lian 2011, pp. 6-7] |
| Total rupture rate, \(I_{total}\) | \(I_{total} = 0.32 I_t + 0.68 I_n\) | [Lian 2011, pp. 6-7] |
| Critical rupture rate, \(I_c\) | 0.8 | [Lian 2011, pp. 6-7] |
| Binary method coefficients | \(a_1=1.43,\ a_2=-0.05,\ a_3=0.0125,\ a_4=-920\) | [Lian 2011, pp. 6-7] |
| Strain energy density, \(dW/dV\) | Computed from effective stresses; formula in Eq. (5) | [Lian 2011, pp. 6-7] |
| Fracture density, \(x\) | ~1 m⁻¹ (SE) to ~8 m⁻¹ (structural highs, near faults) | [Lian 2011, pp. 6-7] |

## Reusable Claims

- **Claim**: Under triaxial compression, carbonate rocks from the Kenkiyak KT‑II formation exhibit a progression of failure modes—shear plane → high‑angle crack → conjugate shear cracks → net fractures—as effective confining pressure increases, with concurrent intensification of rock‑texture damage.  
  *Source*: [Lian 2011, pp. 1-1, 2‑4]  
  *Conditions*: Effective confining pressure range ~10–85 MPa; carbonate cores tested with controlled pore pressure (0–60 MPa); depth ~4100–4500 m.  
  *Limitations*: Findings based on only eight samples from a single well; generalisability to other depths or facies not established.

- **Claim**: A three‑dimensional finite‑element simulation of tectonic stress that incorporates pore‑pressure and fault‑slip effects can reproduce measured stress orientations and magnitudes (error < 5 %) and match observed displacements in the Kenkiyak field.  
  *Source*: [Lian 2011, pp. 1-1, 4‑6]  
  *Conditions*: Model constructed with ADINA, elastic‑plastic constitutive law, rock treated as a fluid‑filled porous medium, three specific boundary‑condition scenarios, and five faults that may slip.  
  *Limitations*: Validation uses acoustic‑emission data from two wells and image‑log data from four wells; may not capture all temporal variations.

- **Claim**: Fracture density can be predicted by a binary method that combines total rupture rate (a weighted sum of Griffith tension and Mohr–Coulomb shear factors) with strain energy density, assuming a critical rupture threshold \(I_c=0.8\).  
  *Source*: [Lian 2011, pp. 6-7]  
  *Conditions*: Calibration requires known fracture density, rupture rate, and strain energy from at least four calibration wells; coefficients must be recalculated for each field.  
  *Limitations*: The method is empirical; the threshold \(I_c\) is taken from generic rock‑mechanics experiments and may vary with lithology.

- **Claim**: In the Kenkiyak reservoir, structural highs and areas adjacent to faults exhibit fracture densities of ~8 fractures/m, whereas the southeast part shows only ~1 fracture/m, driven by tectonic extrusion and elevated pore pressure.  
  *Source*: [Lian 2011, pp. 4-6, 6‑7]  
  *Conditions*: Under the modelled stress state with pore pressure reaching up to 105 MPa.  
  *Limitations*: Applies to the specific tectonic and pore‑pressure evolution of this field; may not hold if pore‑pressure generation mechanisms differ.

## Candidate Concepts

- [[pore pressure]]
- [[effective stress]]
- [[triaxial compression test]]
- [[fracture density prediction]]
- [[binary method for fracture density]]
- [[Griffith failure criterion]]
- [[Mohr-Coulomb failure criterion]]
- [[acoustic emission]]
- [[finite element simulation]]
- [[strain energy density (SED)]]
- [[tectonic stress field]]
- [[fault slip]]
- [[carbonate reservoir]]
- [[abnormal high pressure]]
- [[rock rupture rate]]
- [[elastic-plastic constitutive model]]

## Candidate Methods

- [[Triaxial compression test with pore pressure control]]
- [[ADINA finite element simulation with fault slip and pore pressure]]
- [[Acoustic emission stress measurement]]
- [[Imaging log fracture orientation analysis]]
- [[Rupture rate calculation (Griffith and Mohr-Coulomb)]]
- [[Binary method for fracture density (rupture rate + strain energy)]]
- [[Strain energy density (SED) mapping]]

## Connections To Other Work

- Earlier simulations of tectonic stress fields often did not treat the rock as a porous medium and thus neglected pore pressure, potentially causing errors [Lian 2011, pp. 1-2]. This study explicitly builds on that gap by incorporating pore pressure and fault slip into the ADINA model.
- The paper references hydraulic‑fracturing studies that explored pore‑pressure effects on breakdown pressure and initiation (Zoback et al. 1977, Ikeda & Tsukahara 1989, Bohloli & Pater 2006) [Lian 2011, pp. 1-1, 7‑8].
- The use of Griffith and Mohr–Coulomb failure criteria for fracture prediction follows work by Song (1999) and Oda et al. (1993) [Lian 2011, pp. 1-1, 7‑8].
- The binary method for fracture density is related to “two‑factor methods” proposed by Ding et al. (1998) and Serata et al. (1992) [Lian 2011, pp. 6-7, 7‑8].
- The strain‑energy‑density concept for fracture location is taken from Sih (1991) [Lian 2011, pp. 6-7].
- Geological modelling of the Kenkiyak pre‑salt reservoir follows Chen et al. (2008) [Lian 2011, pp. 1-2].

## Open Questions

- How transferable are the calibrated binary‑method coefficients (\(a_1, a_2, a_3, a_4\)) to other carbonate fields with different diagenetic histories? [inferred from the site‑specific calibration, not discussed in paper]
- Does the critical rupture rate \(I_c = 0.8\) hold for all rock types in the Kenkiyak reservoir, or does it vary with porosity, cementation, or pore‑fluid chemistry? [not examined in the study]
- How does the dynamic evolution of pore pressure during progressive fault slip affect the timing and location of fracture generation beyond the static equilibrium simulations presented? [only a single‑state pore‑pressure field was computed]
- Could coupling of the stress model with a fluid‑flow simulator improve the prediction of abnormal pressure zones and associated fractures? [suggested by the observation that current pressure is lower than simulated maximum pressure]
- What is the minimum number of calibration wells required to reliably apply the binary method in a new area? [method used four wells here]
- Are there other failure mechanisms (e.g., grain‑scale breakage, dissolution) that contribute to fractures but are not captured by the Griffith/ Mohr–Coulomb criteria? [thin sections showed grain stripping, but only macroscopic criteria were used]

## Source Coverage

All non‑empty indexed fragments were processed and compiled into this page. Coverage metrics: 6 indexed texts, 29 998 indexed characters, 6 non‑empty source blocks, 6 compiled source blocks, 30 123 compiled source characters. Coverage ratio by blocks: 1.0; coverage ratio by characters: 1.004167. Source signature: `899a2c5bdbc63bc63ab1d2624f7d53da471916a2`. No textual content from the paper was omitted; all evidence presented is derived solely from the supplied fragments.
