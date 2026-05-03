---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2000-collin-analysis-and-prediction-of-thermal-shock-in-brittle-materials"
title: "Analysis and Prediction of Thermal Shock in Brittle Materials."
status: "draft"
source_pdf: "data/papers/2000 - Analysis and prediction of thermal shock in brittle materials.pdf"
collections:
  - "part2"
  - "zotero new"
citation: "Collin, M., and D. Rowcliffe. “Analysis and Prediction of Thermal Shock in Brittle Materials.” *Acta Materialia*, vol. 48, no. 7, 2000, pp. 1655-1665, doi:10.1016/S1359-6454(00)00011-2."
indexed_texts: "10"
indexed_chars: "47048"
nonempty_source_blocks: "10"
compiled_source_blocks: "10"
compiled_source_chars: "47257"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004442"
coverage_status: "full-index"
source_signature: "dd8e874a5787ac55538c053c20b3528826f69404"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T11:47:06"
---

# Analysis and Prediction of Thermal Shock in Brittle Materials.

## One-line Summary
The indentation-quench method is investigated through experiment and modeling, revealing three regimes of crack growth in brittle materials, and an expression is derived linking the unstable crack growth temperature (DTU) to fracture toughness, enabling prediction of thermal shock resistance.

## Research Question
How can the indentation-quench method be used to analyze and predict the thermal shock resistance of brittle materials, and how do residual stresses and fracture toughness influence crack growth under thermal shock?

## Study Area / Data
Four materials were tested:
- High-purity dense fine-grained alumina (average grain size <5 µm)
- Alumina reinforced with 30 vol% SiC whiskers
- Titanium-based cermet (grade CT530)
- High-alloy high-speed steel (grade ASP2060, selected for its ability to form radial cracks after Vickers indentation)

Material properties, including elastic modulus, Poisson’s ratio, thermal expansion, density, heat capacity, thermal conductivity/diffusivity, are listed in Table 1 [Collin 2000, pp. 2-3]. Experimental measurements of crack growth as a function of temperature difference (DT) were made, along with biaxial bending strengths and cross‑section crack shapes [Collin 2000, pp. 2-5].

## Methods
- **Indentation‑quench test**: Precracks introduced via Vickers indentation (20 s dwell); samples heated in air to desired DT, then quenched by free fall into 30°C water. Crack growth measured on surface; DT intervals 20–40°C [Collin 2000, pp. 1-2, 2-3].
- **Crack shape examination**: Cross‑sections made by fracturing samples in biaxial bending; shape factor a/c evaluated [Collin 2000, pp. 3-4].
- **Stress intensity analysis**: Total stress intensity K_tot = K_thermal + K_residual; K_thermal from polynomial geometric functions for semi‑elliptical cracks under power‑law stress distributions (Eq. 2); K_residual,surf = w_surf P c^{–1.5} [Collin 2000, pp. 4-5].
- **Estimation of surface heat transfer coefficient**: Parity assumed between thermal stress at onset of unstable crack growth and mechanical strength of indented plate; f0 β determined from DTU and biaxial strength; Biot number β and heat transfer coefficient h derived (Eqs. 8–10) [Collin 2000, pp. 6-7].
- **Thermal shock resistance prediction**: Derived expression for DTU based on fracture toughness, elastic modulus, thermal expansion, and Biot number (Eq. 15) [Collin 2000, pp. 7-8].
- **Transient thermal stress calculation**: Finite difference and finite element methods used to compute temperature and stress distributions during quenching (Appendix A) [Collin 2000, pp. 10-11].

## Key Findings
1. **Three regimes of crack growth** observed for all materials [Collin 2000, pp. 2-3]:
   - Regime A: no detectable crack growth at very low DT.
   - Regime B: stable crack growth at medium DT, with small scatter.
   - Regime C: at a certain DT (DTU), some cracks grow unstably to the edge while others remain stable; this defines the onset of unstable growth.
2. **Crack shape evolution**: After quenching, cracks become more elongated in the surface direction (a/c decreases) [Collin 2000, pp. 3-4].
3. **Mechanism of stable/unstable growth**: The interplay between decreasing residual stress intensity and increasing thermal stress intensity with crack length leads to a minimum in K_tot,surf. Stable growth occurs when this minimum is below fracture toughness; unstable growth when it exceeds toughness [Collin 2000, pp. 5-6].
4. **Expression for DTU**: Derived as  
   DTU = A · K_Ic(c_U) · (1–ν)/(Eα) · 1/f0β · 1/√(π a_U)  
   (Eq. 15) showing that toughness directly determines thermal shock resistance; the effect of thermal conductivity is Biot‑number dependent [Collin 2000, pp. 7-8].
5. **R‑curve behavior**: Alumina and reinforced alumina show discontinuous crack growth and a higher toughness at DTU than from as‑indented crack length, consistent with grain‑localized bridging and R‑curve behavior [Collin 2000, pp. 9-10].
6. **Practical use**: The method can rank materials and define application‑specific limits (e.g., DT10 for critical components, DTU for mainly thermal loads) [Collin 2000, pp. 9-10].

## Core Evidence Table

| Evidence                                                                 | Source                   | Conditions                                                                 | Notes                                                                                   |
|--------------------------------------------------------------------------|--------------------------|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Crack growth vs DT divided into three regimes (A, B, C)                  | [Collin 2000, pp. 2-3]   | Four materials quenched into 30°C water; mean crack growth measured          | Regime C starts at DTU; values for alumina 160°C, reinforced alumina ~260–280°C, etc. |
| DTU values: alumina 160°C, reinforced alumina 260–280°C, cermet 280°C, steel 400°C | [Collin 2000, pp. 2-3, 6-7] | Indentation loads and crack sizes specified                                 | DTU is a conservative limit; larger precracks reduce it.                              |
| Crack shapes become elongated (a/c < 1) after quenching                  | [Collin 2000, pp. 3-4]   | Alumina: from semicircular (a/c=1) to 0.7; steel: kidney‑shaped to 0.39      | Used in stress intensity calculations                                                  |
| K_tot,surf minimum occurs when dK_thermal/dc equals –dK_residual/dc       | [Collin 2000, pp. 5-6]   | Assumes constant a/c, R‑curve derivative zero                                 | Leads to Eq. 13: K_thermal = 3 K_residual at DTU                                       |
| Estimated fracture toughness at DTU for alumina: 3.96 MPa√m              | [Collin 2000, pp. 8-9]   | From Eq. 15 using known f0β and DTU for 4 mm plate                          | Higher than KIc from as‑indented crack (2.93 MPa√m), supporting R‑curve behavior      |
| Surface heat transfer coefficient for alumina ~34,000 W/(m²K)            | [Collin 2000, pp. 6-7]   | Derived from biaxial strength and DTU; compares with literature 10,000–60,000 | f0β=0.40, β=2.8                                                                        |
| DT10 defined as DT causing 10% crack length increase                      | [Collin 2000, pp. 9-10]  | Suggested for critical applications                                           | Offers conservative limit for combined thermal/mechanical loads                       |

## Limitations
- The analysis does not fully explain the absence of crack growth in Regime A; it is attributed mainly to low surface heat transfer coefficient below 100°C, but this is not fully resolved [Collin 2000, pp. 8-9].
- The derivation of DTU assumes a constant crack shape factor a/c and neglects R‑curve derivatives [Collin 2000, pp. 7-8].
- The model relies on parity between thermal stress and mechanical strength; systematic investigations of different conditions are needed to refine empirical heat transfer coefficients [Collin 2000, pp. 8-9].
- For high‑speed steel, only grade ASP2060 forms radial cracks; alternative precracking methods are required for other grades [Collin 2000, pp. 2-3].
- R‑curve measurement was outside the scope; qualitative indications of R‑curve behavior are drawn from crack growth patterns [Collin 2000, pp. 9-10].

## Assumptions / Conditions
- The crack shape is approximated as semi‑elliptical, and the shape factor a/c is treated as constant during certain calculations [Collin 2000, pp. 3-4, 7].
- Parity is assumed between the thermal stress at the onset of unstable crack growth and the mechanical strength of the indented plate (biaxial bending) [Collin 2000, pp. 6-7].
- For simplicity, the derivative of KIc with respect to crack length is set to zero when deriving DTU [Collin 2000, pp. 7-8].
- The residual stress factor w_surf is assumed to be a material constant, and w_surf > w_deep as measured on glass [Collin 2000, pp. 5].
- Quenching medium is water at 30°C; the surface heat transfer coefficient is considered constant but actually varies with surface temperature [Collin 2000, pp. 8-9].

## Key Variables / Parameters
- DT: temperature difference between furnace and quenching medium
- DTU: DT at onset of unstable crack growth
- DT10: DT causing 10% crack length increase
- K_thermal, K_residual, K_tot: stress intensities
- KIc(c): crack‑size‑dependent fracture toughness
- E: elastic modulus
- α: coefficient of thermal expansion
- ν: Poisson’s ratio
- σ_biax: biaxial bending strength
- P: indentation load, c: surface crack half‑length, a: crack depth
- a/c: crack shape factor
- f0 β: parameter representing fraction of total DT that determines maximum surface stress
- β: Biot number (β = h r / k)
- h: surface heat transfer coefficient
- k: thermal conductivity
- r: plate half‑thickness
- w_surf: residual stress factor

## Reusable Claims
- The indentation‑quench method can reveal three crack growth regimes: no growth (low DT), stable growth (medium DT), unstable growth (above DTU) [Collin 2000, pp. 2-3].
- Stable crack growth under thermal shock is governed by the competition between decreasing residual stress intensity and increasing thermal stress intensity with crack extension [Collin 2000, pp. 5-6].
- Unstable crack growth occurs when the minimum of total stress intensity at the surface exceeds the fracture toughness of the material [Collin 2000, pp. 5-6].
- A predictive expression for DTU is DTU = A · K_Ic(c_U) · (1–ν)/(Eα) · 1/f0β · 1/√(π a_U), where A = 3/(4F √π) [Collin 2000, pp. 7-8].
- Fracture toughness is of primary importance for thermal shock resistance; doubling KIc doubles DTU independently of Biot number, whereas the effect of thermal conductivity depends strongly on β [Collin 2000, pp. 7-8].
- For severe heat transfer (water quenching), increasing toughness is more effective than increasing thermal conductivity in raising DTU [Collin 2000, pp. 7-8].
- The presence of residual stress makes the indentation‑quench method more sensitive and enables definition of specific DT values (DT10, DTU) tailored to applications [Collin 2000, pp. 9-10].
- R‑curve behavior in alumina is indicated by discontinuous crack growth at the microstructural scale and by an apparent toughness increase at DTU relative to the as‑indented value [Collin 2000, pp. 9-10].
- The method can be applied to a wide range of brittle materials, including ceramics, cermets, and steels that form indentation cracks [Collin 2000, pp. 9-10].
- For mild heat transfer (e.g., air cooling), strength (or toughness) and thermal conductivity are equally effective in improving thermal shock resistance; for severe transfer, toughness dominates [Collin 2000, pp. 7-8].

## Candidate Concepts
- [[indentation-quench method]]
- [[thermal shock resistance]]
- [[R-curve behavior]]
- [[grain-localized bridging]]
- [[Biot number]]
- [[surface heat transfer coefficient]]
- [[f0-beta parameter]]
- [[residual stress intensity]]
- [[thermal stress intensity]]
- [[stable crack growth (thermal shock)]]
- [[unstable crack growth (thermal shock)]]
- [[DTU (unstable crack growth temperature)]]
- [[DT10 (10% crack growth temperature)]]
- [[parity between thermal and mechanical stress]]

## Candidate Methods
- [[Vickers indentation precracking]]
- [[biaxial bending strength test]]
- [[finite difference method (transient thermal stress)]]
- [[finite element method (transient thermal stress)]]
- [[polynomial stress intensity functions for semi-elliptical cracks]]
- [[indentation fracture mechanics (K_residual)]]
- [[quenching-strength test]]
- [[heat equation (transient)]]

## Connections To Other Work
- The quenching-strength test is a common benchmark for thermal shock resistance [Hasselman, 1970; Lewis, 1983] [Collin 2000, pp. 1-2].
- Indentation techniques for thermal shock studies have been used with various quench media (air, helium, liquid nitrogen, water) and evaluation methods [Faber et al., 1981; Marshall et al., 1984; Johnson-Walls et al., 1985; Gong et al., 1992; Osterstock, 1993; Choi and Salem, 1994; Andersson and Rowcliffe, 1996] [Collin 2000, pp. 1-2, 10].
- The concept of parity between thermal stress at fracture and mechanical strength is a starting point for many earlier investigations [Faber et al., 1981; Marshall et al., 1984] [Collin 2000, pp. 6].
- R‑curve behavior in alumina and related bridging mechanisms have been documented by Steinbrech et al. (1983), Cook et al. (1987), Bennison and Lawn (1989), Swanson et al. (1987), and others [Collin 2000, pp. 9-10, 10].
- Thermal shock resistance parameters R and R′, based on strength, were proposed by Hasselman (1970) [Collin 2000, pp. 8].
- The f0β – Biot number relation and fitting expression (Eq. 10) are consistent with Manson (1958) and Noda et al. (1989) [Collin 2000, pp. 6-7].
- Surface heat transfer coefficient values for alumina in water are compared with measurements by Kim et al. (1991) and Singh et al. (1981) [Collin 2000, pp. 7].

## Open Questions
- The precise cause of the absence of crack growth in Regime A, beyond low surface heat transfer coefficient, remains to be fully clarified [Collin 2000, pp. 8-9].
- Alternative methods for introducing precracks in high‑speed steel grades that do not form radial cracks are needed [Collin 2000, pp. 2-3].
- A complete quantitative prediction of DTU requires knowledge of the R‑curve; systematic R‑curve measurements were not performed here [Collin 2000, pp. 9-10].
- Empirical databases of surface heat transfer coefficients for different materials, plate thicknesses, and quench media would enhance the method’s practical usability [Collin 2000, pp. 8-9].

## Source Coverage
This page was fully compiled from the indexed fragments only. All 10 non‑empty source blocks were processed (total indexed characters: 47,048; compiled characters: 47,257; coverage ratio by blocks: 1.0). No external information was added.
