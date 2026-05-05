---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-chen-correlation-between-shear-induced-asperity-degradation-and-acoustic-emission-energy-in"
title: "Correlation between Shear Induced Asperity Degradation and Acoustic Emission Energy in Single Granite Fracture."
status: "draft"
source_pdf: "data/papers/Correlation between shear induced asperity degradation and acoustic emission energy in single granite fracture.pdf"
collections:
citation: "Chen, Yuedu, and Zhihong Zhao. \"Correlation between Shear Induced Asperity Degradation and Acoustic Emission Energy in Single Granite Fracture.\" *Engineering Fracture Mechanics*, 2020, doi:10.1016/j.engfracmech.2020.107184."
indexed_texts: "10"
indexed_chars: "47311"
nonempty_source_blocks: "10"
compiled_source_blocks: "10"
compiled_source_chars: "46675"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.986557"
coverage_status: "full-index"
source_signature: "29cdfdf699ad09f701462aec9bbe6b17333769c8"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T00:52:21"
---

# Correlation between Shear Induced Asperity Degradation and Acoustic Emission Energy in Single Granite Fracture.

## One-line Summary
This study investigates the correlation between shear-induced asperity degradation and acoustic emission (AE) energy in single granite fractures, proposing a new method for calculating AE b-values based on AE energy.

## Research Question
How does shear-induced asperity degradation correlate with acoustic emission energy in single granite fractures, and can AE energy be used to characterize this damage process?

## Study Area / Data
The study was conducted in a laboratory setting using four cubic fractured granite specimens with a side length of 50 mm. Two specimens contained tension-induced artificial fractures (samples AT1, AT2), and two contained pre-existing natural fractures (samples NA1, NA2). The initial joint roughness coefficient (JRC) values were 16.0, 15.9, 14.6, and 13.5, respectively [Chen 2020, pp. 4-6].

## Methods
Direct shear tests were performed under a constant normal stress of 5 MPa at a shear displacement rate of 0.2 mm/min until a displacement of 5 mm was reached [Chen 2020, pp. 4-6]. Acoustic emission (AE) monitoring was conducted using six PAC Micro-30 sensors (resonant frequency 125 kHz) arranged in two groups on the upper and lower sample surfaces, with a trigger threshold of 40 dB and a sampling rate of 0.5 MHz [Chen 2020, pp. 6-8]. AE source locations were determined using a least-squares interaction technique based on arrival time differences, with an average location error of about 2 mm [Chen 2020, pp. 6-8]. Surface morphology before and after shear was measured using a 3D blue light scanner (OKIO-5M) to quantify asperity degradation volume, focusing on a central 40×40 mm² area to avoid boundary effects [Chen 2020, pp. 6-8].

## Key Findings
1.  A strong correlation exists between shear stress and cumulative AE energy in both artificial and natural fractures, with the cumulative AE energy curve approximating an "S" shape [Chen 2020, pp. 8-10].
2.  AE events are scattered in the pre-peak stage but become localized around the fracture surface in the post-peak stage [Chen 2020, pp. 1-4].
3.  Clusters of AE events with large amounts of energy correspond to the destruction locations of surface asperities and initially occur after entering the post-peak stage [Chen 2020, pp. 1-4, 8-10].
4.  A new method for calculating AE b-values based on AE energy (M = log₁₀(E) + 2) is proposed and is more suitable for predicting surface damage characteristics in granite fractures than the traditional amplitude-based method [Chen 2020, pp. 10-12].
5.  The consistency between AE energy and shear-induced asperity damage volume is found to be good when the detection area increases to a certain larger range of about 25 mm [Chen 2020, pp. 12-14].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Strong correlation between shear stress and cumulative AE energy in artificial and natural fractures. | [Chen 2020, pp. 8-10] | Direct shear tests on granite fractures under 5 MPa normal stress. | Cumulative AE energy curve is approximately "S"-shaped. |
| AE events localize around the fracture surface post-peak. | [Chen 2020, pp. 1-4, 8-10] | AE monitoring during shear. | Scattered pre-peak, localized post-peak. |
| Clusters of high-energy AE events match asperity degradation zones. | [Chen 2020, pp. 8-10] | AE source location and 3D surface scanning. | Occurrence lags behind peak stress. |
| New b-value method (Eq. 6) shows less fluctuation and better correlation with damage type. | [Chen 2020, pp. 10-12] | Calculation using AE energy (E). | Average b-value ~0.65 for artificial fractures, ~0.7 for natural fractures at post-peak. |
| Good correlation between damage volume ratio (αi) and AE energy ratio (βi) when detection area is ~25 mm. | [Chen 2020, pp. 12-14] | Surface divided into 4, 9, and 16 zones. | For 4-zone division, 100% of data points fell within αi=βi±10%. |

## Limitations
1.  The study only tested granite specimens; results may not directly apply to other rock types [Chen 2020, pp. 4-6].
2.  Tests were conducted under a single constant normal stress (5 MPa) [Chen 2020, pp. 4-6].
3.  The correlation between AE energy and damage volume depends on the detection area size [Chen 2020, pp. 12-14].
4.  Boundary effects (e.g., asperity falling off at specimen edges) can contribute to degradation volume but not necessarily to a continuous increase in AE energy [Chen 2020, pp. 12-14].
5.  The crushing of damaged asperities during shear generates AE energy but does not contribute to the measured asperity wearing volume, potentially causing dispersion in the αi-βi correlation [Chen 2020, pp. 12-14].

## Assumptions / Conditions
1.  The granite is assumed to be homogeneous for AE source location calculations [Chen 2020, pp. 6-8].
2.  The AE energy of an electrical signal is proportional to the square of the voltage [Chen 2020, pp. 8-10].
3.  The central 40×40 mm² area of the fracture surface is representative, avoiding boundary effects [Chen 2020, pp. 6-8, 12-14].
4.  The detection area for correlating AE energy and damage volume needs to be sufficiently large (about 25 mm in this study) [Chen 2020, pp. 12-14].

## Key Variables / Parameters
*   **Shear Stress (τ):** Applied shear force per unit area.
*   **Cumulative AE Energy:** Total elastic energy released, calculated by integrating the square of the voltage transient [Chen 2020, pp. 8-10].
*   **AE b-value:** Slope of the frequency-magnitude distribution of AE events, calculated using either amplitude (Eq. 5) or the proposed energy-based magnitude (Eq. 6) [Chen 2020, pp. 10-12].
*   **Damage Volume Ratio (αi):** Ratio of asperity damage volume in a zone to the total damage volume [Chen 2020, pp. 12-14].
*   **AE Energy Ratio (βi):** Ratio of cumulative AE energy in a zone to the total AE energy [Chen 2020, pp. 12-14].
*   **Detection Area Size:** The spatial scale over which AE energy and damage are correlated (~25 mm) [Chen 2020, pp. 12-14].

## Reusable Claims
1.  **Condition:** For single granite fractures under direct shear. **Claim:** There is a strong correlation between shear stress and cumulative acoustic emission energy, with the energy curve following an "S"-shape that reflects the crack development process [Chen 2020, pp. 8-10].
2.  **Condition:** When analyzing AE data from sheared granite fractures. **Claim:** Clusters of AE events with large energy are localized around the fracture surface post-peak and correspond spatially to the destruction locations of surface asperities [Chen 2020, pp. 8-10].
3.  **Condition:** For calculating AE b-values in granite fracture shear tests. **Limitation:** The energy-based magnitude formula (M = log₁₀(E) + 2) produces b-values with less fluctuation and a better correlation with observed surface damage characteristics than the traditional amplitude-based formula [Chen 2020, pp. 10-12].
4.  **Condition:** For quantifying the relationship between AE energy and asperity damage volume. **Limitation:** A good correlation is achieved when the analysis detection area is increased to a certain size (approximately 25 mm in this study) [Chen 2020, pp. 12-14].

## Candidate Concepts
*   [[Asperity degradation]]
*   [[Acoustic emission (AE)]]
*   [[AE energy]]
*   [[AE b-value]]
*   [[Direct shear test]]
*   [[Rock fracture]]
*   [[Shear stress]]
*   [[Gouge formation]]
*   [[Fracture permeability]]

## Candidate Methods
*   [[Direct shear test]]
*   [[Acoustic emission monitoring]]
*   [[3D blue light scanning]]
*   [[AE source location]]
*   [[b-value calculation (energy-based)]]
*   [[Surface damage quantification]]

## Connections To Other Work
The study builds on prior work using AE to monitor rock fracture behavior [Chen 2020, pp. 4-6]. It addresses limitations of post-mortem methods like 3D laser scanning and interrupted methods like X-ray CT scanning by using continuous AE monitoring [Chen 2020, pp. 1-4]. The proposed b-value method relates to seismological concepts (Gutenberg-Richter law) applied to laboratory-scale AE [Chen 2020, pp. 10-12]. The discussion on linking AE energy to permeability via a gouge production factor (cf) connects to models of shear effects on fracture flow [Chen 2020, pp. 12-14].

## Open Questions
1.  Can the quantitative relationship between cumulative AE energy and fracture permeability be established through hydraulic tests? [Chen 2020, pp. 12-14]
2.  How do varying normal stresses and shear rates affect the observed correlations? [Chen 2020, pp. 4-6]
3.  Do the findings hold for other rock types beyond granite? [Chen 2020, pp. 4-6]

## Source Coverage
All non-empty indexed fragments were processed. The compilation is based on 10 indexed text blocks containing a total of 47,311 characters. The compiled page incorporates content from all 10 source blocks, covering 46,675 characters, resulting in a coverage ratio by characters of 0.986557. The coverage status is full-index.
