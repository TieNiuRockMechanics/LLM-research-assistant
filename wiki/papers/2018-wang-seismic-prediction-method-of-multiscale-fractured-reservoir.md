---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2018-wang-seismic-prediction-method-of-multiscale-fractured-reservoir"
title: "Seismic Prediction Method of Multiscale Fractured Reservoir."
status: "draft"
source_pdf: "data/papers/2018 - Seismic prediction method of multiscale fractured reservoir.pdf"
collections:
  - "part1"
citation: "Wang, Ling-Ling, et al. \"Seismic Prediction Method of Multiscale Fractured Reservoir.\" *Applied Geophysics*, vol. 15, no. 2, June 2018, pp. 240-252. DOI:10.1007/s11770-018-0667-8."
indexed_texts: "10"
indexed_chars: "47095"
nonempty_source_blocks: "10"
compiled_source_blocks: "10"
compiled_source_chars: "46355"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.984287"
coverage_status: "full-index"
source_signature: "343e11c039a83e1bda92bcba0b49cac85c52c3b0"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:08:12"
---

# Seismic Prediction Method of Multiscale Fractured Reservoir.

## One-line Summary
A method combining poststack multidirectional coherence based on the curvelet transform for macroscale fractures and prestack azimuthal anisotropy of attenuation attributes for mesoscale fractures is proposed to predict multiscale fractured reservoirs.

## Research Question
Common prestack fracture prediction methods cannot clearly distinguish multiple-scale fractures (macroscale, mesoscale, and microscopic) in reservoirs [Wang 2018, pp. 1-2]. The study aims to develop a prediction method for macro- and mesoscale fractures based on fracture density distribution [Wang 2018, pp. 1-2].

## Study Area / Data
The method is applied to a seismic physical model of a fractured reservoir from western China [Wang 2018, pp. 4-5]. The 3D model is 100 cm × 100 cm × 20 cm, corresponding to actual dimensions of 10000 m × 10000 m × 2000 m, with a velocity similarity ratio of 1:2 and frequency similarity ratio of 5000:1 [Wang 2018, pp. 4-5]. It contains six layers, with the target Daanzhai layer about 190 m thick, divided into two parts [Wang 2018, pp. 4-5]. The model includes eight groups of fractured zones in a simplified central area and a complex southern area with nine groups of fractured zones, intersecting fractures, fracture clusters, and randomly distributed fractures [Wang 2018, pp. 4-5]. Fracture parameters (length, width, density, spacing, orientation, inclination) and elastic properties (P- and S-wave velocities, Thomsen parameters ε and γ) are defined [Wang 2018, pp. 4-5]. The model was suspended in a water-filled tank, and 3D seismic data were acquired with a wide azimuth and long offset geometry [Wang 2018, pp. 5-7].

## Methods
The proposed method involves two main techniques integrated via fracture density:
1.  **Multidirectional coherence technique based on the curvelet transform** for macroscale fractures (larger than 1/4 wavelength) [Wang 2018, pp. 1-2, 2-3]. Poststack amplitude data are decomposed into multiple scales and directions using the second-generation curvelet transform [Wang 2018, pp. 2-3]. Coherence attributes are calculated for each direction, and the minimum coherence value and its corresponding direction are used to estimate fracture density and orientation [Wang 2018, pp. 2-3].
2.  **Azimuthal anisotropy inversion based on prestack attenuation attributes** for mesoscale fractures (1/4–1/100 wavelength) [Wang 2018, pp. 1-2, 3-4]. This uses the analytical expression for P-wave attenuation versus offset and azimuth in a vertically fractured (HTI) medium derived by Chichinina et al. (2006) [Wang 2018, pp. 3-4]. Prestack gathers are divided by azimuth, and attenuation attributes (e.g., frequency attenuation gradient, absorption quality factor) are inverted [Wang 2018, pp. 3-4, 9-11]. The azimuthal variation of attenuation is fitted to an ellipse, where ellipticity denotes fracture density and the axis orientation denotes fracture strike [Wang 2018, pp. 3-4].
The fracture density distributions from both methods are then combined (e.g., via weighted average or assembly) to produce an integrated prediction of macro- and mesoscale fractures [Wang 2018, pp. 11-12].

## Key Findings
- The multidirectional coherence technique based on the curvelet transform successfully identifies faults and macroscale fractured zones, providing continuous fracture density distributions at these locations, but is insensitive to mesoscale fractures [Wang 2018, pp. 7-9, 11-12].
- The azimuthal anisotropy of the prestack frequency attenuation gradient attribute is the most sensitive and effective for predicting mesoscale fractures, identifying fracture clusters consistent with the model [Wang 2018, pp. 9-11, 11-12].
- Using attenuation attributes alone for macroscale fractures leads to discontinuous fracture density distributions and potential misinterpretation [Wang 2018, pp. 11-12].
- The integrated prediction method based on combining fracture densities from both techniques overcomes the discontinuity problem, accurately distinguishes fracture scales, and identifies fractured zones [Wang 2018, pp. 1-2, 11-12].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Fracture density for macroscale fractures is calculated as `FI = 1.0 - (Cl)min`, where `(Cl)min` is the minimum coherence value across L directions. | [Wang 2018, pp. 2-3] | Based on poststack data decomposed via curvelet transform. | Equation (2) in the paper. |
| Fracture orientation for macroscale fractures is given by `FR = 90 / (L-1) * (l-1) + 180 / L`. | [Wang 2018, pp. 2-3] | Corresponds to the direction `l` of minimum coherence. | Equation (3) in the paper. |
| The azimuthal attenuation `1/Q` for P-waves in an HTI medium is approximated by `1/Q(θ, I) ≈ 1/2 [C1 + C2 sin²θ + C3 sin²θ cos2(I-Is) + C4 sin²θ sin2(I-Is)]`. | [Wang 2018, pp. 3-4] | For incidence angles 0–40°, aspect ratio α < 0.01, liquid-filled fractures. | Simplified form (Equation 6) from Chichinina et al. (2006). |
| The frequency attenuation gradient attribute successfully identified seven fracture clusters in the complex area of the physical model, consistent with the model design. | [Wang 2018, pp. 9-11] | Applied to prestack azimuthal data from the physical model. | Compared to amplitude, maximum energy, and absorption quality factor attributes. |
| The integrated fracture density map (weighted average or assembly) shows enhanced continuity of faults/macroscale zones and clear identification of mesoscale zones. | [Wang 2018, pp. 11-12] | Combination of results from curvelet coherence (macroscale) and frequency attenuation gradient (mesoscale). | Figure 13 in the paper. |

## Limitations
- The method is insensitive to microscale fractures (<<1/100 wavelength), which can only be observed by electron microscopy in cores [Wang 2018, pp. 2-3].
- The multidirectional coherence technique for macroscale fractures is insensitive to mesoscale fractures [Wang 2018, pp. 7-9].
- When attenuation attributes are used to predict macroscale fractures, the resulting fracture density distributions are discontinuous and may be misinterpreted [Wang 2018, pp. 11-12].
- The parameters ∆N, ∆I N, and ∆T in the attenuation model are difficult to calculate for the equivalent physical model and were estimated by fitting [Wang 2018, pp. 7-9].
- The schemes for dividing directions (for macroscale) and azimuths (for mesoscale) must be the same during data processing, and the fitting of directional/azimuthal data should be consistent [Wang 2018, pp. 11-12].

## Assumptions / Conditions
- Fractured zones are modeled as Horizontal Transverse Isotropy (HTI) media, except for those with variable inclination [Wang 2018, pp. 4-5].
- The physical model uses an equivalent method to simulate fractured zones, representing groups of fractures [Wang 2018, pp. 4-5].
- The azimuthal attenuation model (Equation 6) is valid for incidence angles of 0–40° and aspect ratio α < 0.01 for liquid-filled fractures [Wang 2018, pp. 3-4].
- The fracture density values from the two prediction methods range from 0 to 1 and can be directly combined without normalization [Wang 2018, pp. 11-12].

## Key Variables / Parameters
- **Fracture Density (FI):** A dimensionless measure of fracture intensity, derived from coherence or attenuation anisotropy [Wang 2018, pp. 2-3, 3-4].
- **Fracture Orientation (FR, Is):** The strike direction of fractures, derived from the direction of minimum coherence or the axis of the attenuation ellipse [Wang 2018, pp. 2-3, 3-4].
- **Frequency Attenuation Gradient:** A prestack seismic attribute sensitive to energy loss with frequency, used for mesoscale fracture prediction [Wang 2018, pp. 9-11].
- **Absorption Quality Factor (Q):** A measure of seismic attenuation; its azimuthal variation is used for fracture characterization [Wang 2018, pp. 3-4, 9-11].
- **Thomsen Parameters (ε, γ):** Anisotropy parameters describing the fractured medium [Wang 2018, pp. 4-5].

## Reusable Claims
- The multidirectional coherence technique based on the curvelet transform provides continuous fracture density distributions for faults and macroscale fractures but is insensitive to mesoscale fractures [Wang 2018, pp. 7-9, 11-12].
- The azimuthal anisotropy of the prestack frequency attenuation gradient is the most sensitive attribute for predicting mesoscale fractures in the studied physical model [Wang 2018, pp. 9-11].
- Combining fracture density distributions from poststack coherence (macroscale) and prestack attenuation anisotropy (mesoscale) overcomes the discontinuity problem inherent in using attenuation attributes alone for macroscale features [Wang 2018, pp. 11-12].
- For accurate multiscale fracture prediction, the directional/azimuthal data division and fitting procedures must be consistent between the macro- and mesoscale methods [Wang 2018, pp. 11-12].

## Candidate Concepts
- [[Multiscale fractures]]
- [[Fracture density]]
- [[Seismic anisotropy]]
- [[Curvelet transform]]
- [[Azimuthal anisotropy]]
- [[Prestack attenuation attributes]]
- [[HTI medium]]
- [[Fractured reservoir]]

## Candidate Methods
- [[Multidirectional coherence technique]]
- [[Curvelet transform]]
- [[Azimuthal anisotropy inversion]]
- [[Frequency attenuation gradient]]
- [[Absorption quality factor (Q) inversion]]
- [[Data fusion based on fracture density]]

## Connections To Other Work
- The study builds on the fracture scale classification by MacBeth and Li (1999) [Wang 2018, pp. 1-2].
- The theoretical basis for azimuthal anisotropic attenuation is the QVOA expression derived by Chichinina et al. (2006) [Wang 2018, pp. 1-2, 3-4].
- The multidirectional coherence technique is based on prior work by Zheng et al. (2009) and Zhang et al. (2011) [Wang 2018, pp. 2-3].
- The integrated prediction approach is compared to the multiscale integrated method of Chen (2016) [Wang 2018, pp. 2-3].
- The physical model construction and data are referenced from Wang et al. (2017) [Wang 2018, pp. 4-5].

## Open Questions
- How can the integration method (weighted average vs. assembly) be optimized to best emphasize either macroscale or mesoscale fractures depending on the exploration objective?
- How can the method be extended or adapted to predict microscale fractures, which are beyond seismic resolution?
- How robust is the method when applied to field seismic data with lower signal-to-noise ratio and more complex overburden effects compared to a controlled physical model?

## Source Coverage
All non-empty indexed fragments were processed. The compilation is based on 10 indexed text blocks containing 47,095 characters. The compiled source blocks total 10, with 46,355 characters, resulting in a coverage ratio by characters of 0.984287. The coverage status is full-index.
