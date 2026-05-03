---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-zhao-shear-related-roughness-classification-and-strength-model-of-natural-rock-joint-based"
title: "Shear-Related Roughness Classification and Strength Model of Natural Rock Joint Based on Fuzzy Comprehensive Evaluation."
status: "draft"
source_pdf: "data/papers/2021 - Shear-related roughness classification and strength model of natural rock joint based on fuzzy comprehensive evaluation.pdf"
collections:
  - "zotero new"
citation: "Zhao, Yanlin, et al. \"Shear-Related Roughness Classification and Strength Model of Natural Rock Joint Based on Fuzzy Comprehensive Evaluation.\" *International Journal of Rock Mechanics & Mining Sciences*, vol. 137, 2021, article no. 104550. Accessed 2026."
indexed_texts: "16"
indexed_chars: "77376"
nonempty_source_blocks: "16"
compiled_source_blocks: "16"
compiled_source_chars: "72614"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.938456"
coverage_status: "full-index"
source_signature: "6f0488abc8c33a8a166f574d2ce1ce42f7cfbe97"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T04:42:27"
---

# Shear-Related Roughness Classification and Strength Model of Natural Rock Joint Based on Fuzzy Comprehensive Evaluation.

## One-line Summary
The study proposes a fracture roughness coefficient (FRC) using fuzzy comprehensive evaluation (FCE) that integrates multiple morphological parameters, and develops an improved FRC‑JCS shear strength model, validated against direct shear tests on natural rock joints.

## Research Question
How can the joint surface roughness of natural rock joints be quantitatively classified and shear strength accurately predicted by comprehensively considering the influence of multi‑morphology parameters (height and textural) through fuzzy comprehensive evaluation?

## Study Area / Data
- **Location**: Jinchuan Mining Area, China (roadway at the 1098 level), where rock masses are broken under high in‑situ stress.
- **Rock types**: marble, lherzolite, and amphibolite (three natural joints per type, saw‑cut planar joints for basic friction angle, and intact specimens for mechanical properties).
- **Data acquisition**:  
  – Direct shear tests (CNL condition) at normal stresses of 0.4, 0.8, 1.2, and 1.6 MPa on mated natural joints (specimen dimensions 200 × 150 × 150 mm³).  
  – 3‑D laser scanning (Talysurf CLI 2000, 0.5 mm sampling interval) to extract surface morphology; profiles parallel to shear direction (8–10 mm spacing) averaged.  
  – Digitized Barton & Choubey standard JRC profiles (0.5 mm SI) for calibration.

## Methods
1. **Morphological parameter measurement**:  
   - Amplitude: \(S_m\), \(S_q\), \(S_s\) (skewness), \(S_k\) (kurtosis).  
   - Textural: \(Z_2\) (RMS gradient), \(S_i\) (RMS of asperity angle facing shear direction), \(S_c\) (mean summit curvature).  
   - Strong correlations found: \(Z_2\) vs. \(S_i\) (\(R^2=0.992\)), and \(S_q/S_m \approx 1.13\). Other parameters showed no obvious dependence on \(S_i\).
2. **Fuzzy Comprehensive Evaluation (FCE)** for roughness classification:  
   - Evaluation factor set \(U = \{S_i, S_q, S_c, S_k\}\) chosen based on sensitivity to shear (order: \(S_i > S_q > S_c > S_k\)).  
   - Evaluation grades \(V\) = {1, 2, …, 10} (very smooth to extreme roughness).  
   - Gaussian membership function, boundaries derived from standard profiles and measured data.  
   - Factor weights via Analytic Hierarchy Process (AHP): judgment matrix built on Saaty’s 1–9 scale; obtained weight vector \(A = (0.56, 0.26, 0.12, 0.06)\) for \(S_i, S_q, S_c, S_k\) (consistency ratio 0.045 < 0.1).  
   - Comprehensive evaluation: \(B = A\cdot R\) then defuzzified by weighted mean (k=2) to obtain Fracture Roughness Coefficient \(FRC = 2Q\).  
   - For whole joint surface, profiles weighted by Gaussian function emphasising rougher profiles: \(FRC = \sum w(i) FRC_i\).
3. **New shear strength model**:  
   \( \tau_p = \sigma_n \tan\left[FRC\cdot \log(JCS/\sigma_n) + \phi_b\right] \)  
   (replace JRC in Barton’s model with FRC).  
4. **Comparison with published models**: JRC‑JCS (Barton & Choubey), Jang et al.‘s, Lee et al.‘s models.

## Key Findings
- The proposed FRC is generally higher than the conventionally calculated JRC (whole surface: \(FRC = 2.26 \, JRC^{0.747}\)), reflecting the multi‑parameter influence and weighting of steep profiles.
- FRC‑JCS model predicts peak shear strength with an **average estimation error of 6.83%**, outperforming JRC‑JCS (18.1%), Jang et al.‘s (24.8%), and Lee et al.‘s (10.4%).
- The JRC‑JCS and Jang et al.‘s models systematically **underestimate** shear strength of natural joints; the proposed model brings predictions closest to measured values.
- \(Z_2\) has a strong positive linear relationship with \(S_i\); \(S_m, S_q, S_s, S_k, S_c\) show no obvious dependence on \(S_i\).
- The ratio \(S_q/S_m\) is approximately 1.13 across specimens.

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Average error of FRC‑JCS model = 6.83% | Zhao et al. 2021, Table 8, Fig. 14-15 | Natural joints (marble, lherzolite, amphibolite), CNL, σ_n = 0.4–1.6 MPa | Error defined as \(\lvert\tau_{pe} - \tau_{pp}\rvert / \tau_{pe} \times 100\%\) |
| JRC‑JCS model average error = 18.1%, Lee et al. = 10.4%, Jang et al. = 24.8% | Zhao et al. 2021, Table 8 | Same test conditions | Shows systematic underestimation by other models |
| Whole‑surface roughness relationship: \(FRC = 2.26\,JRC^{0.747}\) | Zhao et al. 2021, Eq. (32), Fig. 13 | All specimens | Derived from FCE‑based FRC vs. calculated JRC |
| \(Z_2 = 0.0182 S_i\) (\(R^2=0.992\)) | Zhao et al. 2021, Eq. (8), Fig. 7 | Natural joints | Strong linear correlation, supports substitution in FCE factor set |
| FRC‑JCS model form: \(\tau_p = \sigma_n \tan[FRC \cdot \log(JCS/\sigma_n) + \phi_b]\) | Zhao et al. 2021, Eq. (34) | Uses FRC in place of JRC | JCS = UCS for non‑weathered rock |

## Limitations
- The FRC and model are developed and tested only on three non‑weathered rock types (marble, lherzolite, amphibolite) from a single mining area; generalisation to other lithologies and weathered joints remains unverified.
- The evaluation factor set includes only four parameters (\(S_i, S_q, S_c, S_k\)); other morphological descriptors (e.g., fractal parameters) are not considered.
- The model assumes CNL boundary conditions; constant normal stiffness (CNS) behaviour was not investigated.
- The weight vector in FCE is derived from AHP based on a single judgment matrix; alternative weighting or membership functions might yield different FRC values.
- The direct shear tests were conducted at moderate normal stresses (0.4–1.6 MPa); extrapolation to higher stress ranges is not validated.

## Assumptions / Conditions
- Rock joints are **clean, non‑weathered, without cohesive infill**.
- The joint‑wall compressive strength (JCS) equals the intact unconfined compressive strength (UCS) for non‑weathered joints.
- Shear tests performed under **constant normal load (CNL)** at a displacement rate of 0.5 mm/min.
- Surface roughness is characterised by profiles parallel to the shear direction, individually averaged, then weighted by roughness height to represent the whole joint.
- The contribution of morphological parameters to shear resistance follows the order \(S_i > S_q > S_c > S_k\); this assumption is embedded in the AHP judgment matrix.

## Key Variables / Parameters
- **Amplitude parameters**: \(S_m\) (arithmetic mean height), \(S_q\) (root‑mean‑square height), \(S_s\) (skewness), \(S_k\) (kurtosis)
- **Textural parameters**: \(Z_2\) (RMS gradient), \(S_i\) (RMS of shear‑facing asperity angle), \(S_c\) (mean summit curvature)
- **Fuzzy evaluation factors**: \(S_i, S_q, S_c, S_k\)
- **Fracture Roughness Coefficient (FRC)**: \( FRC = 2 \frac{\sum_{j=1}^{10} b_j^2\, j}{\sum_{j=1}^{10} b_j^2} \); whole‑surface FRC uses profile weights \(w(i) = F_i/\sum F_i\)
- **Joint Roughness Coefficient (JRC)**: calculated via Tse & Cruden’s \(JRC = 32.2 + 32.47 \log Z_2\)
- **Basic friction angles**: marble 28.1°, lherzolite 29.7°, amphibolite 31.2°
- **Rock strength**: UCS (marble 66.9 MPa, lherzolite 67.7 MPa, amphibolite 53.9 MPa), tensile strength (2.10, 1.97, 1.78 MPa respectively)

## Reusable Claims
- Claim: A fracture roughness coefficient (FRC) derived from fuzzy comprehensive evaluation of the parameters \(S_i, S_q, S_c, S_k\) can replace JRC in Barton’s model, yielding the shear strength criterion \(\tau_p = \sigma_n \tan[FRC\cdot \log(JCS/\sigma_n) + \phi_b]\).  
  Condition: Applicable to clean, non‑weathered natural rock joints under CNL conditions; validated for marble, lherzolite, and amphibolite with \(\sigma_n\) 0.4–1.6 MPa.
- Claim: The FRC is systematically larger than the JRC calculated from \(Z_2\) and follows \(FRC = 2.26 \, JRC^{0.747}\) for whole‑joint surfaces.  
  Condition: As above; relationship based on nine joints from three rock types.
- Claim: The RMS gradient \(Z_2\) and the shear‑facing asperity angle \(S_i\) are strongly linearly correlated (\(Z_2 = 0.0182 S_i, R^2 = 0.992\)).  
  Condition: Valid for the natural joints tested; may simplify roughness parameter selection in similar rocks.
- Claim: The JRC‑JCS model and the Jang et al. model tend to underestimate peak shear strength of natural rock joints, while the FRC‑JCS model reduces the average estimation error to ~6.8%.  
  Condition: Based on direct shear tests of three rock types; observed under CNL with normal stresses ≤1.6 MPa.

## Candidate Concepts
- [[Fracture Roughness Coefficient (FRC)]]
- [[Fuzzy Comprehensive Evaluation (FCE)]]
- [[Rock joint shear strength]]
- [[Morphological parameters of rock joints]]
- [[Analytic Hierarchy Process (AHP)]]
- [[CNL direct shear test]]
- [[JRC-JCS model]]
- [[Shear-related roughness classification]]

## Candidate Methods
- [[Fuzzy comprehensive evaluation with Gaussian membership function]]
- [[3D laser scanning for joint surface morphology]]
- [[AHP-based weight determination for multi-factor evaluation]]
- [[Direct shear testing under constant normal load]]
- [[Profiling of rock joints along shear direction]]
- [[Talymap analysis for roughness parameters]]

## Connections To Other Work
- **Barton & Choubey (1977)**: JRC‑JCS model serves as the baseline; standard profiles digitised and used to calibrate FCE grade boundaries.
- **Tse & Cruden (1979)**: relationship \(JRC = 32.2 + 32.47 \log Z_2\) used to compute JRC from \(Z_2\).
- **Grasselli & Egger (2003), Grasselli (2006)**: contributions on 3‑D surface parameters and shear strength models referenced; the current FRC‑JCS model aims to overcome limitations of single‑parameter descriptions.
- **Jang et al. (2010), Lee et al. (2014)**: modified JRC‑JCS models used for comparison; the proposed model shows lower estimation error.
- **Cao et al. (2012)**: work on morphology variation under shear cited to justify the sensitivity order \(S_i > S_q > S_c > S_k\).
- **Zhao (1997)**: JMC concept and joint matching effects acknowledged.

## Open Questions
- How does the FRC‑JCS model perform under constant normal stiffness (CNS) conditions and at higher normal stresses?
- Can the FCE‑based roughness classification be extended to include three‑dimensional surface parameters (e.g., contact area, dip angle of asperities) without over‑parametrisation?
- Is the proposed weighting (AHP with fixed judgment matrix) robust across a wider range of rock types and joint weathering grades?
- How does scale dependency of roughness parameters affect the FRC and the derived strength predictions?
- Would alternative membership functions (triangular, trapezoidal) or defuzzification methods change the FRC values significantly?

## Source Coverage
This page was compiled exclusively from the indexed fragments of Zhao et al. (2021). All **16 non‑empty indexed text blocks** (77,376 characters total) were processed. The compiled content represents **100% of blocks** and **93.8% of the indexed characters**; no external facts were injected. The coverage signature is `6f0488abc8c33a8a166f574d2ce1ce42f7cfbe97`.
