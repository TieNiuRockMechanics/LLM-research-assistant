---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-zhang-experimental-study-on-cryogenic-quenching-characteristics-of-rock-surface-in-liquid-n"
title: "Experimental Study on Cryogenic Quenching Characteristics of Rock Surface in Liquid Nitrogen."
status: "draft"
source_pdf: "data/papers/液氮接触页岩表面淬火传热特性实验_张诚成.pdf"
collections:
citation: "Zhang, Cheng-Cheng, et al. \"Experimental Study on Cryogenic Quenching Characteristics of Rock Surface in Liquid Nitrogen.\" *Journal of Engineering Thermophysics*, vol. 41, no. 7, July 2020, pp. 1735-1742."
indexed_texts: "7"
indexed_chars: "31105"
nonempty_source_blocks: "7"
compiled_source_blocks: "7"
compiled_source_chars: "31251"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004694"
coverage_status: "full-index"
source_signature: "59fe2b4574e2b22f09c29edb6aafe700de530e79"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T11:23:08"
---

# Experimental Study on Cryogenic Quenching Characteristics of Rock Surface in Liquid Nitrogen.

## One-line Summary
This study experimentally investigates how different surface structures (smooth, rough, grooved, sand-coated) of shale affect the quenching heat transfer characteristics when contacted by liquid nitrogen, finding that surface modifications can significantly enhance heat transfer rates.

## Research Question
The research aims to investigate the quenching heat transfer characteristics during the contact between liquid nitrogen and shale rock, and to understand the influence of surface morphology on this process, which is relevant to liquid nitrogen fracturing technology for shale reservoir stimulation [Zhang 2020, pp. 1-2].

## Study Area / Data
The study uses shale rock samples. Samples were processed into discs with a diameter of 80 mm and a height of 30 mm. Four different surface structures were prepared: a smooth surface (S1) polished with 1500-grit sandpaper, a rough surface (S2) polished with 36-grit sandpaper, a grooved surface (S3) with ~300 µm deep grooves, and a sand-coated surface (S4) with adhered quartz sand particles [Zhang 2020, pp. 2-3].

## Methods
1.  **Sample Preparation:** Shale samples were cut and their surfaces prepared via polishing (1500-grit for S1, 36-grit for S2), mechanical grooving (S3), and gluing quartz sand particles (S4). Surfaces were cleaned with distilled water, acetone, and trichloromethane before experiments [Zhang 2020, pp. 2-3].
2.  **Experimental Setup:** A quenching apparatus consisting of a quenching pool, a diversion device, a vacuum system, and a data acquisition system was used. The sample was placed in the pool, and T-type thermocouples were inserted into a 2 mm diameter hole drilled 2 mm from the boiling surface. The setup was designed to ensure one-dimensional heat transfer by insulating the sides with Teflon tape and sealing gaps with glue. Liquid nitrogen was poured onto an inverted funnel to distribute it gently onto the sample surface [Zhang 2020, pp. 2-3].
3.  **Data Processing:** A nonlinear space marching algorithm was used to calculate the surface temperature and heat flux from the thermocouple data (located 2 mm below the surface) and a natural convection boundary condition at the bottom. The natural convection heat transfer coefficient was taken as 25 W/(m²·K) [Zhang 2020, pp. 3-5].
4.  **Characterization:** Contact angle measurements, Scanning Electron Microscopy (SEM), and 3D surface morphology tests were performed on the samples [Zhang 2020, pp. 1-2].

## Key Findings
1.  The shale surface polished with 36-grit sandpaper (S2) had a smaller water contact angle (34.2°) and higher surface roughness (Ra = 4.129 µm) compared to the smooth surface (S1, contact angle 43.5°, Ra = 1.493 µm). This resulted in a higher Leidenfrost point (LFP) temperature for S2 (-50.6°C) than for S1 (-54.7°C) [Zhang 2020, pp. 5-6].
2.  SEM images revealed multi-scale pore and cavity structures on the rock surface, which provide numerous active nucleation sites for bubbles and weaken the stability of the vapor film [Zhang 2020, pp. 1-2, 5-6].
3.  Compared to the smooth surface (S1), the grooved surface (S3) and sand-coated surface (S4) shortened the quenching time by 20% and 30%, respectively, when the wall temperature decreased from ambient to -100°C [Zhang 2020, pp. 1-2, 5-6].
4.  Grooves and sand particles increase the surface area, leading to more frequent intermittent solid-liquid contact. This allows the system to enter the transition boiling regime at a higher wall superheat, thereby enhancing the surface heat transfer capability [Zhang 2020, pp. 1-2, 5-6].
5.  The sand-coated surface (S4) had the highest film boiling heat transfer coefficient but the lowest critical heat flux (CHF) among the tested surfaces. The reduction in CHF (21.4 kW/m² lower than S1) is attributed to the additional thermal resistance from the glue layer and sand particles [Zhang 2020, pp. 6-8].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Smooth surface (S1) temperature decreased from 25.4°C to LFP at -54.7°C in 182 s. | [Zhang 2020, pp. 5-6] | Initial ambient temperature, liquid nitrogen quenching. | Baseline for comparison. |
| Rough surface (S2) reached LFP at -50.6°C in 159 s. | [Zhang 2020, pp. 5-6] | Polished with 36-grit sandpaper. | Higher LFP than S1 due to increased surface energy and roughness. |
| Grooved (S3) and sand-coated (S4) surfaces shortened cooling time to -100°C by 20% and 30% vs. S1. | [Zhang 2020, pp. 1-2, 5-6] | Wall temperature from ambient to -100°C. | S1 took 200 s, S3 took 160 s, S4 took 140 s. |
| Critical Heat Flux (CHF) for S1 was 95.3 kW/m². | [Zhang 2020, pp. 6-8] | Measured from boiling curve. | Peak heat flux in transition boiling. |
| CHF for sand-coated surface (S4) was 73.9 kW/m². | [Zhang 2020, pp. 6-8] | Measured from boiling curve. | 21.4 kW/m² lower than S1, attributed to additional thermal resistance. |
| Water contact angles for S1 and S2 were 43.5° ± 3.2° and 34.2° ± 1.4°, respectively. | [Zhang 2020, pp. 5-6] | Measured at room temperature. | Used as a proxy for surface wettability with liquid nitrogen. |
| Surface roughness (Ra) for S1 and S2 were 1.493 µm and 4.129 µm, respectively. | [Zhang 2020, pp. 5-6] | Measured via 3D surface morphology. | Higher roughness promotes earlier solid-liquid contact. |
| Groove depth was ~330 µm, approximately 2.5 times the stable vapor film thickness (~120-150 µm). | [Zhang 2020, pp. 5-6] | Measured from 3D morphology. | Grooves disrupt the vapor film. |
| Sand particle height was ~400 µm, about three times the vapor film thickness. | [Zhang 2020, pp. 5-6] | Measured from 3D morphology. | Sand particles can "pierce" the vapor film. |
| Uncertainty in surface temperature and heat flux density was 2.5% and 5%, respectively. | [Zhang 2020, pp. 3-5] | Based on error propagation from thermocouple position and material property measurements. | Provides confidence in the calculated results. |

## Limitations
1.  The study focuses on shale; results may differ for other rock types like sandstone, which has larger mineral grains and pore structures [Zhang 2020, pp. 5-6].
2.  The additional thermal resistance introduced by the glue layer and sand particles on the S4 surface complicates the direct interpretation of its heat transfer performance [Zhang 2020, pp. 6-8].
3.  The contact angle of water was used as a qualitative proxy for the wettability of liquid nitrogen, as direct measurement with liquid nitrogen was not possible [Zhang 2020, pp. 5-6].

## Assumptions / Conditions
1.  Heat transfer in the rock disc was assumed to be one-dimensional (radial temperature distribution was uniform), validated by Fluent simulation [Zhang 2020, pp. 3-5].
2.  The natural convection heat transfer coefficient at the bottom of the sample was assumed to be 25 W/(m²·K) [Zhang 2020, pp. 3-5].
3.  The thermal conductivity and specific heat capacity of the rock were measured at room temperature and assumed constant during the quenching process [Zhang 2020, pp. 3-5].

## Key Variables / Parameters
-   Wall Superheat (°C)
-   Surface Temperature (°C)
-   Heat Flux Density (kW/m²)
-   Leidenfrost Point (LFP) Temperature (°C)
-   Critical Heat Flux (CHF) (kW/m²)
-   Surface Roughness, Ra (µm)
-   Contact Angle (°)
-   Quenching Time (s)

## Reusable Claims
1.  **Condition:** For shale surfaces contacted by liquid nitrogen. **Claim:** Increasing surface roughness from Ra=1.493 µm to Ra=4.129 µm via 36-grit sandpaper polishing increases the Leidenfrost point temperature and shortens the film boiling duration. **Limitation:** Specific to the shale type and polishing methods used in this study [Zhang 2020, pp. 5-6].
2.  **Condition:** For shale surfaces with engineered structures (grooves or sand coating) quenched in liquid nitrogen. **Claim:** Grooved and sand-coated surfaces reduce the time required to cool from ambient to -100°C by 20% and 30%, respectively, compared to a smooth surface, by promoting earlier transition to transition boiling. **Limitation:** The sand-coated surface introduces additional thermal resistance that lowers the critical heat flux [Zhang 2020, pp. 1-2, 5-6, 6-8].
3.  **Condition:** During film boiling on a rock surface in liquid nitrogen. **Claim:** The multi-scale pore and cavity structures inherent to rock surfaces provide abundant nucleation sites for bubbles, which can weaken vapor film stability. **Limitation:** The degree of effect depends on the rock's mineral composition and resulting surface morphology [Zhang 2020, pp. 1-2, 5-6].

## Candidate Concepts
- [[Leidenfrost point]]
- [[Film boiling]]
- [[Transition boiling]]
- [[Nucleate boiling]]
- [[Critical heat flux]]
- [[Quenching heat transfer]]
- [[Surface wettability]]
- [[Surface roughness]]
- [[Vapor film stability]]
- [[Liquid nitrogen fracturing]]

## Candidate Methods
- [[Space marching algorithm]] for inverse heat conduction
- [[Quenching curve analysis]]
- [[3D surface morphology characterization]]
- [[Scanning Electron Microscopy (SEM)]]
- [[Contact angle measurement]]

## Connections To Other Work
The study builds upon and compares its findings with previous research on surface effects in quenching:
-   It references work by Li et al. on sandstone quenching in liquid nitrogen, noting that shale has a lower LFP temperature (-54.7°C vs. -45°C) due to its denser surface with fewer pores [Zhang 2020, pp. 5-6].
-   It cites studies on metal surfaces, such as Lee et al., which found that groove structures enhance heat transfer by promoting intermittent solid-liquid contact [Zhang 2020, pp. 5-6].
-   It mentions research by Kim et al. on nanoparticle surfaces that cause vigorous solid-liquid contact during film boiling, destabilizing the vapor film [Zhang 2020, pp. 2-3, 5-6].
-   The introduction notes that most prior quenching studies focused on metals with water or cryogenic fluids, highlighting the novelty of studying rock, a natural porous medium [Zhang 2020, pp. 2-3].

## Open Questions
1.  How do the quenching characteristics vary with different types of shale (e.g., varying clay content, mineralogy)?
2.  What is the optimal geometry (depth, spacing) for grooves or the optimal size/distribution for sand particles to maximize heat transfer enhancement without excessive thermal resistance?
3.  How do the findings translate to the dynamic, high-pressure conditions of an actual downhole liquid nitrogen fracturing operation?

## Source Coverage
All non-empty indexed fragments were processed. The compilation is based on 7 indexed fragments containing a total of 31,105 characters. The compiled source blocks account for 31,251 characters, resulting in a coverage ratio by characters of 1.004694. The coverage status is "full-index".
