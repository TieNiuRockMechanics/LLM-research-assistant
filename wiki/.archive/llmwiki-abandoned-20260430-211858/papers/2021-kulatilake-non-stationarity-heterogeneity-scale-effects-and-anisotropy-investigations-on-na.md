---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2021-kulatilake-non-stationarity-heterogeneity-scale-effects-and-anisotropy-investigations-on-na"
title: "Non-Stationarity, Heterogeneity, Scale Effects, and Anisotropy Investigations on Natural Rock Joint Roughness Using the Variogram Method."
status: "draft"
source_pdf: "data/papers/2021 - Non-stationarity, heterogeneity, scale effects, and anisotropy investigations on natural rock joint roughness using the variogram method.pdf"
collections:
  - "zotero new"
citation: "Kulatilake, Pinnaduwa H. S. W., et al. \"Non-Stationarity, Heterogeneity, Scale Effects, and Anisotropy Investigations on Natural Rock Joint Roughness Using the Variogram Method.\" *Bulletin of Engineering Geology and the Environment*, vol. 80, 2021, pp. 6121–43. doi:10.1007/s10064-021-02321-3. Accessed 2026."
indexed_texts: "15"
indexed_chars: "72917"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T03:00:39"
---

# Non-Stationarity, Heterogeneity, Scale Effects, and Anisotropy Investigations on Natural Rock Joint Roughness Using the Variogram Method.

## One-line Summary
The variogram method is applied to a 1 m × 1 m natural rock joint surface to quantify how non‑stationarity, heterogeneity, scale‑related parameters, and anisotropy influence roughness, revealing that heterogeneity—rather than sample size—drives the scale‑effect controversy and that the predominant roughness direction aligns with the shear direction [Kulatilake 2021, pp. 1‑2].

## Research Question
How do non‑stationarity, heterogeneity, joint size (scale), and direction (anisotropy) affect fractal roughness parameters (fractal dimension *D* and amplitude parameter *Kv*) when rock joint roughness is quantified by the variogram method, and can these factors explain contradictory scale‑effect findings in the literature? [Kulatilake 2021, pp. 1‑2, 3‑4].

## Study Area / Data
- **Location**: Heshangnong quarry, Qingshi Town, Changshan County, Zhejiang Province, China, a large open‑pit excavation in calcareous slate [Kulatilake 2021, pp. 4‑6].
- **Rock joint**: A single natural joint surface of size 1 m × 1 m, formed by a shear fracture; the main shearing direction was approximately parallel to the X‑direction of the joint [Kulatilake 2021, pp. 1‑2, 6‑7].
- **Data acquisition**: Surface geometry captured by a laser scanner with a spatial measurement resolution of ± 0.10 mm [Kulatilake 2021, pp. 6‑7].
- **Digitised profiles**: Roughness profiles were extracted at a data spacing of 0.5 mm in both the X‑ and Y‑directions. For Z‑X profiles (along the axes of ridges and troughs) and Z‑Y profiles (perpendicular to them), various section lengths were cut and linear trends removed to obtain “residual roughness” data [Kulatilake 2021, pp. 7‑9].

## Methods
- **Variogram method**: For each profile *Z(X)*, the variogram \(2\gamma(X,h) = E[(Z(X+h)-Z(X))^2]\) was computed for small lags *h*. Under the assumption of a Gaussian process with stationary increments, the behaviour \(\gamma \propto h^{2H}\) at \(h\to 0\) yields the Hurst exponent *H*, from which the fractal dimension *D* = 2 − *H* and the amplitude parameter *Kv* was obtained from the intercept [Kulatilake 2021, pp. 6‑7].
- **Trend removal**: Global linear trends were removed from all profiles to produce residual roughness data. This allowed comparison of raw and residual results to assess the effect of non‑stationarity [Kulatilake 2021, pp. 7‑9].
- **Linearity check**: The linear relationship between log(variogram) and log(*h*) was tested by regression; only profiles with a multiple linear correlation coefficient *R* > 0.85 were retained for parameter calculation [Kulatilake 2021, pp. 6‑7, 9‑11].
- **Heterogeneity investigation**: The joint surface was subdivided into sections of different sizes (500 mm, 250 mm, 125 mm) in both the X‑ and Y‑directions. Summary statistics and spatial variability of *D*, *Kv*, and *D*×*Kv* were compared among sections [Kulatilake 2021, pp. 9‑11].
- **Scale investigation**: Profile lengths of 1000 mm, 500 mm, 250 mm, and 125 mm were analysed to examine the effect of joint size on the fractal parameters [Kulatilake 2021, pp. 9‑11].
- **Anisotropy investigation**: Roughness parameters calculated for Z‑X profiles (parallel to the main ridge/trough axis) were compared with those for Z‑Y profiles (perpendicular to it) [Kulatilake 2021, pp. 6‑11].

## Key Findings
1.  **Negligible non‑stationarity effect** – For Z‑Y profiles of 1000 mm and 500 mm, the fractal parameters *D*, *Kv*, and *D*×*Kv* computed from raw data and from residual (detrended) data were very similar, indicating that the non‑stationarity of the profiles had a negligible impact on the quantified roughness [Kulatilake 2021, pp. 1‑2, 9‑11].
2.  **Significant heterogeneity** – The 750–1000 mm section of the 250 mm Z‑Y profiles exhibited notably higher average roughness parameter values and greater variability with respect to the X‑coordinate than the other three 250 mm sections (0–250 mm, 250–500 mm, 500–750 mm), demonstrating pronounced spatial heterogeneity of roughness on the joint surface [Kulatilake 2021, pp. 9‑11].
3.  **Scale effect is negligible when comparing profile lengths** – The computed fractal parameter values showed no substantial dependence on joint size (i.e., the length of the measured profile) for the investigated lengths, casting doubt on the existence of a pure scale effect on this surface [Kulatilake 2021, pp. 1‑2, 9‑11].
4.  **Heterogeneity may explain contradictory scale effects** – The authors suggest that the confounding positive, negative, and absent scale effects reported in earlier studies likely stem from roughness heterogeneity across the measured surfaces, a factor that had not been systematically isolated in previous roughness quantification [Kulatilake 2021, pp. 1‑2, 3‑4].
5.  **Strong anisotropy controlled by shear direction** – Roughness in the X‑direction (parallel to the axes of the ridges and troughs) was found to be considerably lower than that in the Y‑direction (perpendicular to the ridge/trough axis). This anisotropic pattern is consistent with the joint having originated from a shear fracture whose main shearing direction was approximately parallel to the X‑direction [Kulatilake 2021, pp. 1‑2, 6‑7].
6.  **Profile linearity was generally satisfactory** – All Z‑X profiles and the vast majority of Z‑Y profiles yielded *R* > 0.85 in the variogram log‑log regression, confirming the applicability of the power‑law variogram model. The only exception was the 750–1000 mm section of the 250 mm Z‑Y profiles, where 23 out of 101 profiles failed the linearity criterion and were excluded from the summary statistics [Kulatilake 2021, pp. 9‑11].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Negligible difference between *D*, *Kv*, and *D*×*Kv* values computed from raw vs. residual roughness data for 1000 mm and 500 mm Z‑Y profiles | [Kulatilake 2021, pp. 9‑11] | 101 profiles per length; linear trend removal; 0.5 mm data spacing; variogram with 7 small‑lag points | The closeness of raw and residual results implies non‑stationarity does not bias the fractal parameters. |
| Higher mean and variability of roughness parameters in the 750–1000 mm section of the 250 mm Z‑Y profiles compared to the other three 250 mm sections | [Kulatilake 2021, pp. 9‑11] | 101 profiles per section; variogram analysis on residual roughness; profiles with *R* ≤ 0.85 excluded for that section | Indicates substantial heterogeneity; the 750–1000 mm zone is distinct from the rest of the surface. |
| Fractal parameter values did not change systematically with increasing profile length (1000, 500, 250, 125 mm) | [Kulatilake 2021, pp. 9‑11] | Both Z‑X and Z‑Y direction profiles; residual roughness data | Supports the conclusion of negligible scale effect for this surface. |
| Z‑X profiles show significantly lower roughness than Z‑Y profiles, matching the visually observed ridge‑and‑trough orientation | [Kulatilake 2021, pp. 1‑2, 6‑11] | Profiles taken parallel (X) and perpendicular (Y) to the main ridge axis; shear fracture joint | Anisotropy confirmed; low roughness along the shear direction. |
| All Z‑X profiles and most Z‑Y profiles yielded *R* > 0.85, except 23 profiles from one 250 mm Z‑Y section | [Kulatilake 2021, pp. 9‑11] | Regression of log(variogram) vs. log(*h*) for early lags | The power‑law variogram model fits well for nearly all profiles; the problematic zone coincides with the observed heterogeneity. |

## Limitations
- The study is restricted to a single natural joint surface from one quarry; the generalisability of the findings to other rock types, joint origins, or scales remains uncertain (not confirmed from the provided index segments).
- Only one measurement resolution (0.5 mm data spacing) was used; the effect of changing measurement resolution on scale‑effect conclusions was not investigated within this work (not confirmed from the provided index segments).
- The variogram analysis relies on the “early part” of the variogram and a linear log‑log fit with *R* > 0.85; profiles failing this criterion were discarded, which may bias heterogeneity representations in the anomalous zone.
- The inference that scale‑effect controversy is caused by roughness heterogeneity is based on interpretation of the results from this single surface; direct comparative experiments with multiple heterogeneous and homogeneous surfaces are not presented (not confirmed from the provided index segments).

## Assumptions / Conditions
- The joint surface height *Z(X)* is modelled as a Gaussian process with stationary increments and zero mean [Kulatilake 2021, pp. 6‑7].
- For *h* → 0, the variogram follows a power law \(2\gamma(h) \propto h^{2H}\) (a self‑affine fractal behaviour) [Kulatilake 2021, pp. 6‑7].
- The linear correlation between log(variogram) and log(*h*) must exceed *R* > 0.85 for the fractal parameters to be considered reliable; profiles with lower *R* are excluded from statistical summaries [Kulatilake 2021, pp. 6‑7, 9‑11].
- Removal of the global linear trend from raw profiles is assumed to render the data sufficiently stationary for investigating the non‑stationarity effect [Kulatilake 2021, pp. 7‑9].
- The lag *h* used in the variogram calculation must satisfy *hd* = 1.76 for the given data density *d* (2 data per mm), yielding a minimum *h* of 0.88 mm; in practice the minimum *h* was set to 1 mm and then increased by a factor of 1.2 for seven lags [Kulatilake 2021, pp. 7‑9].

## Key Variables / Parameters
- **Fractal dimension (*D*)**: measure of profile autocorrelation (roughness complexity); *D* = 2 − *H* [Kulatilake 2021, pp. 6‑7].
- **Amplitude parameter (*Kv*)**: describes the magnitude (amplitude) of roughness; derived from the intercept of the log‑log variogram plot [Kulatilake 2021, pp. 6‑7].
- **Combined parameter *D*×*Kv***: used as an overall roughness indicator [Kulatilake 2021, pp. 9‑11].
- **Hurst exponent (*H*)**: scaling exponent obtained from the slope of log(variogram) vs. log(*h*); slope = 2*H* [Kulatilake 2021, pp. 6‑7].
- **Linear correlation coefficient (*R*)**: quality criterion for the log‑log linearity of the variogram; threshold > 0.85 [Kulatilake 2021, pp. 6‑7].
- **Profile length and section**: 1000 mm, 500 mm, 250 mm, 125 mm; used to assess scale and heterogeneity [Kulatilake 2021, pp. 9‑11].
- **Profile direction**: Z‑X (parallel to ridge axis) and Z‑Y (perpendicular); used to assess anisotropy [Kulatilake 2021, pp. 7‑11].

## Reusable Claims
1.  **Claim**: For the studied 1 m × 1 m shear‑fracture joint, non‑stationarity removed by a global linear trend has a negligible effect on the variogram‑based fractal parameters *D* and *Kv*. **Conditions**: Laser‑scanned surface with 0.5 mm data spacing; variogram computed for seven small lags starting at 1 mm; comparison of raw and detrended profiles. **Limitations**: Verified only for a single surface and measurement resolution; generalisability unknown. [Kulatilake 2021, pp. 1‑2, 9‑11]
2.  **Claim**: Roughness heterogeneity can be detected by comparing summary statistics and spatial variability of fractal parameters across sub‑sections of a large joint; on the investigated surface, one sub‑section (750–1000 mm in the Y‑direction) showed distinctly higher *D*, *Kv*, and *D*×*Kv* values than the other sections. **Conditions**: Profiles of 250 mm length, 101 profiles per section, residual roughness data, variogram method, and 0.5 mm spacing. **Limitations**: The identified heterogeneity may be specific to this joint and scale; the underlying geological cause (e.g., local alteration, shear‑stress variation) is not confirmed from the index segments. [Kulatilake 2021, pp. 9‑11]
3.  **Claim**: The direction of minimum roughness on a shear‑fracture joint coincides with the main shearing direction; in this case, roughness in the X‑direction (parallel to the ridge/trough axis) was markedly lower than in the perpendicular Y‑direction. **Conditions**: Surface generated by a shear fracture; roughness quantified by the variogram method on residual profiles. **Limitations**: Limited to one case; verification across multiple shear fractures is not provided. [Kulatilake 2021, pp. 1‑2, 6‑11]
4.  **Claim**: The pervasive contradiction in published scale‑effect results (positive, negative, or no scale effect) may be attributed to previously unaccounted roughness heterogeneity rather than to a genuine scale dependence of fractal parameters. **Conditions**: Inference drawn from the observation that on a single surface, where scale‑effect is absent, strong heterogeneity exists. **Limitations**: This is an interpretive hypothesis, not experimentally proven by systematically varying heterogeneity across multiple joints; the provided index segments do not report a direct test. [Kulatilake 2021, pp. 1‑2, 3‑4]

## Candidate Concepts
- [[rock joint roughness]]
- [[self‑affine fractals]]
- [[variogram]]
- [[fractal dimension]]
- [[Hurst exponent]]
- [[roughness heterogeneity]]
- [[scale effect]]
- [[anisotropy]]
- [[non‑stationarity]]
- [[shear fracture]]
- [[joint roughness coefficient (JRC)]]

## Candidate Methods
- [[variogram method for roughness]]
- [[laser scanning profilometry]]
- [[modified 2‑D divider method]]
- [[roughness‑length method]]
- [[spectral method]]
- [[line scaling method]]
- [[linear trend removal for stationarity]]
- [[log‑log regression for fractal parameters]]

## Connections To Other Work
- **Barton (1973) JRC**: The paper acknowledges JRC as a widely used field index but notes its shortcomings for accurate quantification, motivating the fractal approach [Kulatilake 2021, pp. 2‑3].
- **Statistical roughness parameters**: Table 1 lists 19 statistical parameters/functions (e.g., CLA, RMS, *Z*₂, structure function) previously proposed, categorised as amplitude, slope/spatial, or combined measures; the variogram method is positioned as a fractal complement [Kulatilake 2021, pp. 2‑3].
- **Previous fractal applications by the authors**: The study extends work by Kulatilake et al. (1995, 1997, 1998, 2006) and Kulatilake & Um (1999) on modified divider and variogram methods for self‑affine rock joint profiles; it also relates to Ge et al. (2014) who compared variogram and modified 2‑D divider approaches [Kulatilake 2021, pp. 3‑4, 4‑6].
- **Scale‑effect controversy**: The paper directly addresses contradictory findings by Bandis et al. (1981), Fardin et al. (2001, 2004), Cravero et al. (2001) (negative scale effect), Leal‑Gomes (2003) and Fardin (2008) (positive scale effect), and Swan & Zongi (1985), Maerz et al. (1990), Cravero et al. (1995) (mixed effects), proposing heterogeneity as a unifying explanation [Kulatilake 2021, pp. 3‑4].
- **Anisotropy quantification**: The work builds on the degree of apparent anisotropy (*Kₐ*) proposed by Belem et al. (2000) and on the three‑method anisotropy comparison by Ge et al. (2014) (variogram, triangular plate, light source), applying the variogram approach to a shear‑fracture surface [Kulatilake 2021, pp. 4‑6].

## Open Questions
- Is the dominant role of heterogeneity in generating apparent scale effects a general phenomenon across different rock types, joint genesis conditions, and measurement techniques? (not addressed in the provided index segments)
- How does measurement resolution interact with heterogeneity when the variogram method is applied at scales finer or coarser than 0.5 mm? (the provided index segments examine only one resolution)
- Can a quantitative heterogeneity index be defined to predict whether scale‑effect artefacts will emerge in a given roughness quantification? (not confirmed from the index segments)
- To what extent do the conclusions hold for joints that are not formed by shear fracture, or for surfaces with multiple intersecting sets of ridges and troughs? (not investigated in the current work per the index segments)

## Source Coverage
- **Index segments available**: 15 segments covering the abstract (pp. 1‑2), major parts of the introduction/literature review (pp. 2‑4), study area and data acquisition (pp. 4‑6), the variogram method description (pp. 6‑7), data preparation and profile selection (pp. 7‑9), and partial results focusing on non‑stationarity and heterogeneity (pp. 9‑11).
- **Potential gaps**: The provided segments do **not** include the complete results for all profile lengths, the full anisotropy comparison statistics, the discussion and interpretation of scale‑effect mechanisms in light of the results, the conclusions section, or any supplementary material. Detailed numerical tables (beyond summary statements) and figures are referenced but not reproduced. Therefore, the wiki page necessarily relies on the text summaries available in the index fragments; quantitative parameter values, statistical test outcomes, and broader discussion points could not be verified from the fragments.
