---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2017-li-uncertainties-in-estimating-the-roughness-coefficient-of-rock-fracture-surfaces"
title: "Uncertainties in Estimating the Roughness Coefficient of Rock Fracture Surfaces."
status: "draft"
source_pdf: "data/papers/2017 - Uncertainties in estimating the roughness coefficient of rock fracture surfaces.pdf"
collections:
  - "zotero new"
citation: "Li, Yanrong, et al. \"Uncertainties in Estimating the Roughness Coefficient of Rock Fracture Surfaces.\" *Bulletin of Engineering Geology and the Environment*, vol. 76, 2017, pp. 1153-1165. doi:10.1007/s10064-016-0994-z."
indexed_texts: "8"
indexed_chars: "38509"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T21:11:56"
---

# Uncertainties in Estimating the Roughness Coefficient of Rock Fracture Surfaces.

## One-line Summary

This study investigates the variability and uncertainty in estimating the rock joint roughness coefficient (JRC) using visual comparison, statistical, and fractal methods based on 223 published joint profiles, proposes new empirical equations less sensitive to sampling interval, and provides an updated visual comparison chart with rules to reduce subjective estimation errors [Li 2017, pp. 1-2; 10-12].

## Research Question

- What are the sources and magnitudes of uncertainties in estimating the joint roughness coefficient (JRC) of rock fracture surfaces when using subjective visual comparison, statistical parameters, and fractal dimensions?
- Which profile parameters and empirical equations are least sensitive to the sampling interval (SI) during digitization, and can they provide more reliable JRC estimates?
- How can the standard JRC visual comparison chart and procedures be improved to mitigate systematic underestimation? [Li 2017, pp. 1-2].

## Study Area / Data

- **Primary dataset**: 223 published rock joint profiles collected from the literature; among them, JRC values for 112 profiles were originally determined via back-calculation from direct shear tests, thus serving as a benchmark [Li 2017, pp. 1-3].
- **Validation samples**: 23 rock joint samples used for direct shear tests to compare estimated and measured peak shear strength [Li 2017, pp. 1-2, 6-8].
- **Type of rock joints**: The dataset includes natural rock fractures and saw-cut planar joints; specific rock types or field locations are not detailed in the provided fragments [Li 2017, pp. 5-6].
- **Standard reference profiles**: The 10 standard JRC profiles (Barton’s chart) are used for visual comparison evaluation [Li 2017, pp. 8-10].

## Methods

- **Digitization of profiles**: The profiles were digitized by constructing vertical lines at each sampling interval (SI) across the profile length and connecting intersection points with the profile to create polylines. A self-developed computer program calculated statistical parameters and fractal dimensions from the digitized data [Li 2017, pp. 3-5].
- **Sampling intervals applied**: Six SIs were used—0.1 mm, 0.2 mm, 0.4 mm, 0.8 mm, 1.6 mm, and 3.2 mm—to examine SI-sensitivity of roughness parameters [Li 2017, p. 5, Fig. 2 ff.].
- **Parameters computed**: Seven parameters were calculated for each profile: maximum height (\(R_z\)), ultimate slope (\(k\)), fractal dimension by hypotenuse-leg method (\(D_{h-L}\)), root mean square of the first deviation (\(Z_2\)), profile elongation index (\(\delta\)), standard deviation of the angle \(i\) (\(\sigma_i\)), and fractal dimension by compass-walking method (\(D_c\)) [Li 2017, pp. 3-5].
- **Empirical model development**: Power-law and linear regressions were fitted between these parameters and JRC; equations with correlation coefficients \(R\) are reported (Eqs. 1–5) [Li 2017, pp. 5-6].
- **Peak shear strength validation**: Average JRC from five proposed equations was input into the Barton (1973) JRC–JCS model; estimated peak shear strength was compared with direct shear test results on 23 samples using a newly developed device; relative error (\(d_e = |s_e - s_t|/s_t \times 100\%\)) was calculated [Li 2017, pp. 6-8].
- **Visual comparison analysis**: JRC estimates from visual comparison (JRC\(_v\)) were compared with JRC from empirical equations (JRC\(_e\)); errors due to non-horizontal main trends and limited scope of standard profiles were illustrated with specific profile examples [Li 2017, pp. 8-10].

## Key Findings

- **SI-sensitivity grouping**: Parameters \(k\), \(R_z\), and \(D_{h-L}\) exhibit lower sensitivity to sampling interval, whereas \(Z_2\), \(\delta\), \(\sigma_i\), and \(D_c\) are significantly affected by SI changes [Li 2017, pp. 1-5].
- **Preferred parameters for JRC estimation**: \(k\), \(R_z\), and \(D_{h-L}\) are recommended over more SI-sensitive parameters because they reflect high-order waviness, which correlates better with JRC, and they are simpler to compute [Li 2017, pp. 5-6].
- **New empirical equations**: Two separate sets of power-law equations with strong linear correlations (e.g., \(R = 0.8158\) for JRC vs. \(k\) in Eq. 3; exact equations for all parameters are given but not fully reproduced in fragments) are proposed for JRC estimation [Li 2017, pp. 1-2, 5-6].
- **Visual comparison underestimation**: Subjective visual comparison underestimates JRC by generally less than two units; this bias arises from ignoring the main profile trend and the limited coverage of the 10 standard profiles [Li 2017, pp. 1-2, 8-10].
- **Error quantification**: The absolute error \(|JRC_v - JRC_e|\) distributes with 11.5% ≥ 8, 15.5% 6–8, 16.0% 4–6, 20.4% 2–4, and 36.6% < 2 [Li 2017, pp. 10-11]. Relative error \(d_e\) in peak shear strength estimation: 29% of samples within 5% error, 42% with 5–10%, 17% 10–15%, 8% 15–20%, and 4% > 20% [Li 2017, pp. 8-10].
- **Updated visual chart**: The standard profile chart is modified by realigning profiles to horizontal main trend and adding an explicit y-axis scale bar with maximum height (\(R_z\)); basic rules for visual comparison are proposed: remove main trend before comparison, and use \(R_z\) as a primary criterion when no obvious match exists [Li 2017, pp. 10-12].

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| \(k\), \(R_z\), and \(D_{h-L}\) show low sensitivity to sampling interval; \(Z_2\), \(\delta\), \(\sigma_i\), \(D_c\) show high sensitivity | [Li 2017, pp. 5-6] | 112 profiles with SI from 0.1 to 3.2 mm; parameters defined in Appendix | Sensitivity evaluated through shifts in correlation coefficients |
| JRC can be estimated by \(JRC = 80.37 k^{0.6238}\) ( \(R = 0.8158\)) | [Li 2017, pp. 5-6] | Based on the collection of 223 joint profiles | Power-law preferred over linear to avoid negative JRC for planar joints |
| Visual comparison underestimates JRC by less than two units on average | [Li 2017, pp. 1-2, 8-10] | Comparison between JRC\(_v\) and JRC\(_e\) from empirical equations | Attributed to non-horizontal main trend and limited standard profile scope |
| 29% of peak shear strength estimates from the new device have relative error < 5%, 42% within 5–10% error | [Li 2017, pp. 8-10] | 23 rock joint samples tested | Uses Barton (1973) JRC–JCS model; basic friction angle and JCS input from device |
| After removing main trend, a profile originally matched to ISRM 10–12 better matched ISRM 18–20 (JRC=19.2) | [Li 2017, pp. 8-10] | Example profile from Jia (2011) | Demonstrates influence of profile trend on visual JRC assignment |
| \(D_c\) hardly exceeds 1.05 even for very rough fractures, while its correlation with JRC is sensitive to SI and method | [Li 2017, pp. 5-6] | All studied profiles | \(D\) by box-counting shows weaker JRC correlation than compass-walking and h–L methods |

## Limitations

- The study relies on digitized profiles obtained from the literature; re-sampling inherent in the digitization process may introduce minor errors, though pixel-analysis artifacts were avoided [Li 2017, pp. 3-5].
- The direct shear test validation is limited to 23 samples; broader rock types and joint surface conditions are not covered in the provided fragments [Li 2017, pp. 6-8].
- The proposed equations are derived from the collected 223 profiles dataset; their generalizability to other profile populations or scales is not explicitly confirmed within the fragments [Li 2017, pp. 1-2].
- The influence of three-dimensional surface roughness is not addressed; all analyses are based on 2D profiles [Li 2017, pp. not explicitly stated in fragments but implied by focus on profile parameters].

## Assumptions / Conditions

- JRC values for the 112 profiles used in SI analysis were originally back-calculated from direct shear tests and serve as reference “true” JRC [Li 2017, pp. 2-3].
- The power-law form is preferred over linear for JRC estimation because linear models can produce non-zero JRC for perfectly planar joints [Li 2017, pp. 5-6].
- High-order waviness has a closer relationship with JRC than low-order waviness, justifying the preference for \(k\), \(R_z\), and \(D_{h-L}\) [Li 2017, pp. 5-6].
- Visual comparison errors are assessed under the assumption that empirical equation-derived JRC\(_e\) values provide a reliable reference [Li 2017, pp. 8-10].
- The peak shear strength validation assumes the Barton (1973) JRC–JCS model is applicable, and the basic friction angle and JCS are correctly input [Li 2017, pp. 6-8].

## Key Variables / Parameters

- **JRC**: Joint Roughness Coefficient, target variable to be estimated [Li 2017, pp. 1-2].
- **\(Z_2\)**: Root mean square of the first deviation of the profile [Li 2017, pp. 1-2, 10-12].
- **\(\sigma_i\)**: Standard deviation of the angle \(i\) [Li 2017, pp. 1-2, 10-12].
- **\(R_z\)**: Maximum height of the profile (vertical distance between highest peak and lowest valley) [Li 2017, pp. 1-2, 10-12].
- **\(L\)**: Projected length of the profile [Li 2017, pp. 1-2].
- **\(k\)**: Ultimate slope, equal to \(R_z / L\) [Li 2017, pp. 1-2, 5-6].
- **\(\delta\)**: Profile elongation index [Li 2017, pp. 1-2].
- **\(D_c\)**: Fractal dimension via compass-walking method [Li 2017, pp. 1-2, 5-6].
- **\(D_{h-L}\)**: Fractal dimension via hypotenuse-leg (h–L) method [Li 2017, pp. 1-2, 5-6].
- **\(D\)** (general): Fractal dimension of the profile; measurement method-dependent [Li 2017, pp. 2-3].
- **SI**: Sampling interval (in mm), critical control factor for parameter values [Li 2017, pp. 2-5, 10].
- **\(R\)**: Correlation coefficient of regression equations [Li 2017, pp. 5-6].
- **\(d_e\)**: Relative error between estimated and direct-shear peak shear strength [Li 2017, pp. 6-8].

## Reusable Claims

1. **Low-SI-sensitivity parameters**: Ultimate slope (\(k\)), maximum height (\(R_z\)), and fractal dimension from the hypotenuse-leg method (\(D_{h-L}\)) are robust to changes in sampling interval, making them preferable for JRC estimation relative to \(Z_2\), \(\sigma_i\), \(\delta\), or \(D_c\). *Conditions*: Valid for 2D profiles digitized at SIs ranging from 0.1 to 3.2 mm. *Limitations*: Only tested on the analyzed dataset. [Li 2017, pp. 5-6]
2. **Power-law JRC–\(k\) equation**: The equation \(JRC = 80.37 k^{0.6238}\) with \(R = 0.8158\) provides JRC estimates without producing negative values for planar joints. *Conditions*: Derived from 223 published profiles; \(k\) defined as \(R_z/L\). *Limitations*: Correlation coefficient indicates moderate scatter; not validated outside the studied dataset. [Li 2017, pp. 5-6]
3. **Visual JRC underestimation and correction**: Visual comparison alone underestimates JRC by up to two units primarily because (a) the main trend of the profile is not horizontal in the standard chart and (b) the 10 standard profiles do not encompass all roughness types. Removing the main trend (by subtracting a linear fit) before comparison and using \(R_z\) as a supplementary criterion reduces this bias. *Conditions*: Applicable when using Barton’s 10 standard JRC profiles. *Limitations*: Quantified error based on comparisons with empirical equations; the two-unit bias is an average, individual cases may deviate more. [Li 2017, pp. 1-2, 8-10]
4. **Sampling-interval-dependent equation necessity**: The degree of correlation between JRC and parameters like \(Z_2\), \(\sigma_i\), and \(\delta\) shifts systematically with SI; therefore, separate regression equations are required for different SIs when using these parameters. *Conditions*: For SI values of 0.1, 0.2, 0.4, 0.8, 1.6, 3.2 mm. *Limitations*: The shift is parameter-dependent; using SI-insensitive parameters avoids this complication. [Li 2017, pp. 2-5]

## Candidate Concepts

- [[joint roughness coefficient (JRC)]]
- [[rock joint shear strength]]
- [[fracture roughness]]
- [[sampling interval effect]]
- [[fractal dimension of rock fractures]]
- [[visual comparison method for JRC]]
- [[Barton’s standard JRC profiles]]
- [[peak shear strength of rock joints]]
- [[high-order waviness vs. low-order waviness]]

## Candidate Methods

- [[empirical JRC estimation from statistical parameters]]
- [[fractal dimension methods for rock joints — compass-walking, box-counting, hypotenuse-leg (h–L)]]
- [[profile digitization with varying sampling intervals]]
- [[direct shear test for JRC back-calculation]]
- [[trend removal by least-square fitting for JRC visual comparison]]
- [[Barton’s JRC–JCS shear strength model]]
- [[least-square regression for empirical JRC equations]]

## Connections To Other Work

- **Reference to Barton (1973)**: The JRC–JCS model by Barton is used as the constitutive framework for peak shear strength estimation in validation tests; the study directly builds upon Barton’s standard 10 JRC profiles for visual comparison and proposes modifications [Li 2017, pp. 6-8, 8-10].
- **Comparison with prior empirical equations**: Li and Zhang (2015) and Li and Huang (2015) previously proposed empirical correlations between JRC and parameters such as \(R_z\), \(k\), \(\delta\), and fractal dimension; the present study extends this by analyzing SI-sensitivity and proposing updated equations [Li 2017, pp. 2-3].
- **Tatone and Grasselli (2010)** findings on SI: It is noted that Tatone and Grasselli found \(Z_2\)-JRC correlations to be sensitive to SI, motivating the comprehensive SI analysis in this study [Li 2017, pp. 2-3].
- **Yu and Vayssade (1991)** influence: They discussed SI-induced shifts in \(Z_2\), \(\sigma_i\), and structure function (SF) correlations with JRC, which is directly examined and extended in this work [Li 2017, pp. 2-3].
- **Gao and Wong (2015)**: Acknowledged for digitization via pixel analysis; this study uses a different digitization method to avoid thickness artifacts [Li 2017, pp. 3-5].
- **Jia (2011)**: Provides specific JRC visual comparison data used to illustrate main-trend and scope errors [Li 2017, pp. 8-10].
- **Broader context**: The work connects to topics such as [[fracture roughness characterization]] for [[rock mass deformability]] and [[shear strength prediction]], and the role of [[scale effects in rock joint roughness]].

## Open Questions

- How do the proposed low-SI-sensitivity parameters (\(k\), \(R_z\), \(D_{h-L}\)) perform at sampling intervals finer than 0.1 mm or coarser than 3.2 mm? [Li 2017, pp. 5-6]
- What is the influence of 3D surface roughness on the JRC estimation and the SI-sensitivity pattern observed in 2D profiles? This is not addressed in the provided fragments.
- How transferable are the empirical equations to different rock types, weathering states, or scale ranges beyond the 223-profile dataset used? The fragments do not specify geological conditions.
- Can the updated visual chart with trend removal and \(R_z\) scale alone eliminate systematic underestimation, or does it require complementary quantitative adjustment? The evidence shows improvement but not full error elimination [Li 2017, pp. 10-12].

## Source Coverage

- **Number of index fragments used**: 8, covering the paper from abstract through results, discussion, to appendix.
- **Spatial coverage**: The fragments cover the abstract (pp. 1-2), introduction/background (pp. 2-3), methods/digitization procedure (pp. 3-5), results and discussion with SI sensitivity, empirical equations, and validation via direct shear tests (pp. 5-8), visual comparison error analysis (pp. 8-10), and conclusions plus appendix definitions (pp. 10-13).
- **Possible missing information**: The specific regression equations for \(R_z\), \(D_{h-L}\), and other parameters beyond Eq. 3 are mentioned but not fully detailed in the fragments; raw datasets and detailed geological/field conditions of the profiles are not included; the exact computational procedure for the newly developed shear strength estimation device is not described; the full reference list is partially present, so some connections to other work may be missed.
