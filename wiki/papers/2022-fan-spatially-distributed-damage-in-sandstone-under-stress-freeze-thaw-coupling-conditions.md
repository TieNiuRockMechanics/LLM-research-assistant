---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-fan-spatially-distributed-damage-in-sandstone-under-stress-freeze-thaw-coupling-conditions"
title: "Spatially distributed damage in sandstone under stress-freeze-thaw coupling conditions."
status: "draft"
source_pdf: "data/papers/2022 - Spatially distributed damage in sandstone under stress-freeze-thaw coupling conditions.pdf"
collections:
citation: "Fan, Lifeng, et al. \"Spatially distributed damage in sandstone under stress-freeze-thaw coupling conditions.\" *Journal of Rock Mechanics and Geotechnical Engineering*, vol. 14, 2022, pp. 1910-1922. DOI: 10.1016/j.jrmge.2022.04.007."
indexed_texts: "10"
indexed_chars: "46016"
nonempty_source_blocks: "10"
compiled_source_blocks: "10"
compiled_source_chars: "46224"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.00452"
coverage_status: "full-index"
source_signature: "aa56531f94820fb9096c8fc74f9f6c97c458b8b9"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T05:56:40"
---

# Spatially distributed damage in sandstone under stress-freeze-thaw coupling conditions.

## One-line Summary
Using real-time CT scanning, this study found that under uniaxial stress-freeze-thaw (SFT) coupling, sandstone damage increases with FT cycles and applied stress, and the damage exhibits a spatial gradient distribution where porosity increases exponentially from the center to the surface, rather than being uniformly distributed. [Fan 2022, pp. 1-1, pp. 11-12]

## Research Question
How is the spatially distributed damage in sandstone characterized under coupled stress-freeze-thaw (SFT) conditions, and what are the coupling effects on its spatial gradient? [Fan 2022, pp. 1-1, pp. 1-2]

## Study Area / Data
- **Rock type:** Red sandstone sampled from Yunnan Province, China. [Fan 2022, pp. 2-4]
- **Mineral composition (by XRD):** Quartz (72.2%), clay minerals (10.8%), plagioclase (6.9%), calcite (6.6%), hematite (2.4%), potassium feldspar (1.1%). [Fan 2022, pp. 2-4]
- **Sample dimensions:** Cylindrical cores with diameter D = 6 mm and height h = 12 mm; average mineral particle size ≈ 0.2 mm. [Fan 2022, pp. 2-4]
- **Experimental conditions:** Saturated samples subjected to uniaxial compressive stresses of 0, 10, 20, and 25 MPa; FT cycles of 0, 8, 16, and 24 with temperatures ranging from -20°C to 20°C. [Fan 2022, pp. 1-1, pp. 2-4]
- **Data acquired:** Real-time CT scanning images, volumetric porosity, areal porosity, and local porosity in divided regions from center to surface. [Fan 2022, pp. 7-9, pp. 9-11]

## Methods
1. **Sample preparation and saturation:** Sandstone cores were vacuumed (-0.1 MPa, 6 h) and water-saturated (24 h). [Fan 2022, pp. 2-4]
2. **Stress application:** Uniaxial compressive stress (0–25 MPa, ≤70% peak stress of 40.9 MPa) was applied via a loading device; force maintained constant within 10 N error during FT cycles. [Fan 2022, pp. 2-4]
3. **Freeze-thaw cycling:** Each cycle: cooling to -20°C (held 2 h) and heating to 20°C (held 2 h) for complete freeze/thaw; up to 24 cycles. [Fan 2022, pp. 2-4]
4. **Real-time CT scanning:** Performed at 0, 8, 16, 24 cycles under SFT conditions using a system with X-ray source, FT and loading device, rotating table, and detector; image resolution 16.58 μm. [Fan 2022, pp. 2-4]
5. **Image processing and damage analysis:** A central region (6 mm diameter × 8.804 mm height) was analyzed; matrix/pore segmentation, 3D reconstruction, cross-section binarization; volumetric and areal porosity calculated; local porosity in five overlapping hollow-cylinder regions (equal volume of 83 mm³) used to quantify spatial gradient. [Fan 2022, pp. 4-7, pp. 9-11]
6. **Spatial gradient quantification:** Porosity variation with distance from center fitted by exponential function \( P = P_1 + A e^{(d - d_1)/t} \); gradient coefficient \( k \) calculated as mean slope between adjacent local regions. [Fan 2022, pp. 9-11]

## Key Findings
1. **Porosity increase:** Volumetric porosity rises with FT cycles; the increase is accelerated by higher uniaxial stress (increment of 33.54% at 0 MPa, 65.85% at 10 MPa, 158.29% at 20 MPa after 24 cycles). [Fan 2022, pp. 7-9]
2. **Spatial gradient distribution:** Under SFT, damage is not uniform; porosity increases exponentially with distance from the sample center, with external regions damaged more than internal ones. [Fan 2022, pp. 9-11, pp. 11-12]
3. **Gradient evolution with FT cycles:** The damage gradient coefficient increases with FT cycles; at 0 and 10 MPa, its increasing rate decreases, while at 20 MPa, the rate increases with cycles. [Fan 2022, pp. 11-12]
4. **Accelerated surface cracking:** Higher stress leads to earlier microcrack formation (after 8 cycles at 20 MPa vs. 16 cycles at 10 MPa); samples at 25 MPa failed with penetrating cracks after 4 cycles. [Fan 2022, pp. 7-9]
5. **Exponential model fit:** The relation between local porosity and distance from center is well described by the exponential function (R² > 0.9 for all stress levels). [Fan 2022, pp. 11-12]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Volumetric porosity increases from 2.126% to 2.839% (0 MPa, 0→24 FT cycles; increment 33.537%) | [Fan 2022, pp. 7-9] | Saturated red sandstone; uniaxial stress 0 MPa; FT cycles 0–24; real-time CT | Porosity quantification excludes 25 MPa due to early failure |
| Volumetric porosity increases from 2.196% to 3.642% (10 MPa, 0→24 FT cycles; increment 65.847%) | [Fan 2022, pp. 7-9] | Same as above, with 10 MPa uniaxial stress | |
| Volumetric porosity increment of 158.291% at 20 MPa (0→24 FT cycles) | [Fan 2022, pp. 7-9] | Same as above, with 20 MPa uniaxial stress | |
| Areal porosity increases by 27.93% (0 MPa), 117.22% (10 MPa), 187.14% (20 MPa) after 24 cycles | [Fan 2022, pp. 7-9] | Cross-section binarization from CT images | Similar trend to volumetric porosity |
| Microcracks form after 16 cycles at 10 MPa, after 8 cycles at 20 MPa; penetrating cracks at 4 cycles for 25 MPa | [Fan 2022, pp. 7-9] | 3D reconstruction and surface observation under SFT | |
| Porosity vs. distance from center follows exponential function with R² > 0.9 (Tables 2-4) | [Fan 2022, pp. 9-11] | Fitting parameters provided for 0, 10, 20 MPa at various FT cycles | Equation: P = P₁ + A e^((d-d₁)/t) |
| Spatial gradient coefficient k increases with FT cycles; increasing rate decreases at 0/10 MPa, increases at 20 MPa | [Fan 2022, pp. 11-12] | Mean slope between five local regions | |

## Limitations
- The study focused on uniaxial compressive SFT coupling; effects of confining pressure-freeze-thaw coupling remain uninvestigated. [Fan 2022, pp. 11-12]
- Only one rock type (red sandstone) was tested; findings may not directly generalize to other lithologies. [Fan 2022, pp. 2-4]
- The stress level of 25 MPa led to sample failure after 4 FT cycles, so quantitative porosity results were only obtained for 0, 10, and 20 MPa. [Fan 2022, pp. 7-9]
- Image resolution (16.58 μm) may limit detection of finer microcracks or nano-scale pores. [Fan 2022, pp. 2-4]
- Water saturation effects on spatial damage gradient were not explicitly examined under varying degrees of saturation. [Fan 2022, pp. 11-12]

## Assumptions / Conditions
- The uniaxial compressive stress was maintained ≤70% of peak stress (≈28 MPa) to avoid unstable crack propagation during the experiment. [Fan 2022, pp. 2-4]
- Samples were fully saturated (vacuum saturation for 6 h at -0.1 MPa, then water immersion for 24 h). [Fan 2022, pp. 2-4]
- Freezing to -20°C for 2 h and thawing to 20°C for 2 h were assumed sufficient for complete thermal equilibration throughout the sample. [Fan 2022, pp. 2-4]
- The analyzed region (excluding ends to avoid end effects) is representative of the whole sample's damage evolution. [Fan 2022, pp. 4-7]
- Local regions of equal volume (83 mm³) and overlapping divisions provide a reasonable estimate of the spatial gradient. [Fan 2022, pp. 9-11]
- The exponential function P = P₁ + A e^((d-d₁)/t) is an empirical fit and does not necessarily imply a mechanistic model of pore formation. [Fan 2022, pp. 9-11]

## Key Variables / Parameters
- **Independent variables:** Uniaxial compressive stress (0, 10, 20, 25 MPa); number of FT cycles (0, 8, 16, 24). [Fan 2022, pp. 1-1]
- **Dependent variables:** Volumetric porosity; areal porosity; local porosity in five regions; spatial gradient coefficient k. [Fan 2022, pp. 7-9, pp. 9-11]
- **Fixed parameters:** Sample diameter (6 mm), height (12 mm); saturation procedure; FT temperature range (-20°C to 20°C); image resolution (16.58 μm); peak stress of saturated red sandstone (40.9 MPa). [Fan 2022, pp. 2-4]
- **Fitting parameters:** P₁, A, t, d₁ in exponential model for each stress/cycle combination. [Fan 2022, pp. 9-11]

## Reusable Claims
- FOR saturated red sandstone with uniaxial compressive stress up to ~70% of peak strength AND FT cycles between -20°C and 20°C: local porosity increases exponentially with distance from the sample center, with damage concentrating near the surface. This claim may not hold for dry samples, different rock types, or triaxial stress states. [Fan 2022, pp. 9-11, pp. 11-12]
- FOR similar sandstone and SFT conditions: the spatial damage gradient coefficient increases with FT cycles; at low stress (e.g., 0–10 MPa) its rate of increase diminishes, whereas at higher stress (20 MPa) the rate of increase accelerates with cycles. Generalizability to other stress ranges or rock types is not confirmed. [Fan 2022, pp. 11-12]
- FOR identical experimental conditions: applied uniaxial stress accelerates the formation of microcracks and penetrating cracks during FT cycles, with failure occurring earlier under higher stress. This supports the concept of a positive coupling effect but should not be extrapolated beyond the tested stress/cycle window. [Fan 2022, pp. 7-9]
- FOR CT-based evaluation of SFT damage: volumetric porosity and areal porosity show consistent increasing trends, with larger increments at higher stress levels, providing a quantitative basis for damage assessment. Applicable only when imaging resolution and segmentation methods are comparable. [Fan 2022, pp. 7-9]
- FOR modeling spatial damage under SFT: an exponential function (R² > 0.9) adequately describes the radial porosity variation, but the physical mechanism behind the fitted parameters remains empirical. [Fan 2022, pp. 9-11]

## Candidate Concepts
- [[spatially distributed damage]]
- [[freeze-thaw (FT) cycles]]
- [[uniaxial stress]]
- [[stress-freeze-thaw (SFT) coupling]]
- [[gradient coefficient (damage)]]
- [[volumetric porosity]]
- [[areal porosity]]
- [[real-time CT scanning]]
- [[mesostructure deterioration]]
- [[mineral particle shedding]]
- [[exponential porosity-distance relationship]]
- [[frost heaving force]]
- [[compaction and crack propagation stages]]

## Candidate Methods
- [[real-time CT scanning with FT and loading device]]
- [[vacuum saturation treatment]]
- [[2D/3D CT image reconstruction and segmentation]]
- [[binarization of cross-section CT images]]
- [[local region division for spatial gradient analysis]]
- [[exponential fitting of porosity-distance data]]
- [[mean gradient coefficient calculation from adjacent regions]]

## Connections To Other Work
- The findings are placed in the context of prior studies on FT-induced damage (mass loss, strength reduction, P-wave velocity, etc.) and limited work on coupled SFT effects. [Fan 2022, pp. 1-1, pp. 1-2]
- The gradient analysis method follows Fan et al. (2020b), which investigated spatial gradient distributions of thermal shock damage in granite. [Fan 2022, pp. 9-11]
- References to studies on pore structure changes under FT with confining pressure (Liu et al., 2019) and loading/unloading effects (Zhang et al., 2020b) highlight the gap in understanding spatially distributed damage under coupled conditions. [Fan 2022, pp. 1-2, pp. 13-13]
- The study addresses calls for more detailed investigation into non-uniform damage distributions suggested by surface observations in Zhu et al. (2021). [Fan 2022, pp. 1-2]
- The damage model of Wang (1990, 1992) for low cycle fatigue is acknowledged but not directly appliedhere; the present study focuses on experimental quantification rather than constitutive modeling. [Fan 2022, pp. 1-2]

## Open Questions
- How does confining pressure (triaxial stress) affect the spatial gradient of FT-induced damage? [Fan 2022, pp. 11-12]
- What is the influence of water saturation degree on the spatial distribution and gradient evolution? [Fan 2022, pp. 11-12]
- Can the empirical exponential relationship be linked to a mechanistic model involving frost heave pressure and mineral particle cohesion? [Fan 2022, pp. 9-11, pp. 11-12]
- Do other rock types (e.g., granite, limestone) exhibit similar spatial gradient behavior under SFT? [Fan 2022, pp. 2-4]
- What is the role of sample size and boundary effects on the observed gradient, particularly the surface damage concentration? [Fan 2022, pp. 2-4, pp. 9-11]
- How do longer FT cycles (beyond 24) influence the gradient coefficient and its rate of change? [Fan 2022, pp. 11-12]

## Source Coverage
All 10 non-empty indexed fragments from the document were processed and incorporated into this page. **Coverage statistics:** indexed texts = 10; indexed characters ≈ 46,016; compiled source blocks = 10; compiled source characters ≈ 46,224; coverage ratio by blocks = 1.0; coverage ratio by chars ≈ 1.0045 (slight excess due to inclusion of full tables and captions). No indexed information was omitted.
