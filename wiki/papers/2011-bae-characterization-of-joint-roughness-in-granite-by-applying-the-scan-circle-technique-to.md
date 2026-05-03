---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2011-bae-characterization-of-joint-roughness-in-granite-by-applying-the-scan-circle-technique-to"
title: "Characterization of Joint Roughness in Granite by Applying the Scan Circle Technique to Images from a Borehole Televiewer."
status: "draft"
source_pdf: "data/papers/2011 - Characterization of Joint Roughness in Granite by Applying the Scan Circle Technique to Images from a Borehole Televiewer.pdf"
collections:
  - "zotero new"
citation: "Bae, Dae-seok, et al. \"Characterization of Joint Roughness in Granite by Applying the Scan Circle Technique to Images from a Borehole Televiewer.\" *Rock Mechanics and Rock Engineering*, vol. 44, 2011, pp. 497-504. DOI: 10.1007/s00603-011-0134-9."
indexed_texts: "6"
indexed_chars: "27268"
nonempty_source_blocks: "6"
compiled_source_blocks: "6"
compiled_source_chars: "27385"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004291"
coverage_status: "full-index"
source_signature: "7783325ee3596f36a2195e52e6481089bfd4f8bc"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T14:16:12"
---

# Characterization of Joint Roughness in Granite by Applying the Scan Circle Technique to Images from a Borehole Televiewer.

## One-line Summary
A fractal‑geometry‑based scan circle technique applied to borehole televiewer (BHTV) images is introduced to efficiently estimate joint roughness coefficient (JRC) in granite, providing average roughness and directional anisotropy from a single borehole survey.

## Research Question
How can joint roughness profiles be rapidly and systematically extracted from borehole televiewer images, quantified by fractal dimension, and translated into JRC values, and how do the results compare with conventional straight‑scan‑line measurements on drill core?

## Study Area / Data
- **Site**: Jurassic granite rock mass at the Korea Atomic Energy Research Institute (KAERI), northwestern Daejeon City, South Korea [Bae 2011, pp. 1-2].
- **Borehole data**: Acoustic BHTV images from the FAC40 Televiewer System (ALT, Luxembourg) with a resolution of 1 pixel = 1 mm; higher‑resolution photo images (up to 20 pixels/mm) can also be used [Bae 2011, pp. 2-3].
- **Selected joint surfaces**: Two joint planes at depth EL. 67.0–67.6 m were analysed [Bae 2011, pp. 2-3].
- **Core samples**: Fracture surfaces from drill core were measured with mechanical profilometry (slice interval 1 mm) for comparison [Bae 2011, pp. 6-7].
- **Reference profiles**: Barton’s ten standard roughness profiles (ISRM 1978) digitised at 20 pixels/mm for calibration of the JRC–fractal dimension relationship [Bae 2011, pp. 3-6].

## Methods
- **BHTV image processing**: Under the WellCAD workspace, sinusoidal joint traces are identified and a reference sine curve defined by dip angle and dip direction is overlaid. Short ruler bars are placed normal to the reference line along the full elliptical circumference of the joint plane [Bae 2011, pp. 2-3].
- **Profile extraction**: The sinusoid images within the bandwidth of the ruler bar are extracted and converted to a straight‑baseline roughness profile [Bae 2011, pp. 2-3].
- **Fractal dimension (D) calculation**: The divider method (modified from Lee et al. 1990; Mandelbrot 1985) is applied with ruler spans *r* = 1, 2, 4, 8, 16, 32, 64 mm. The fractal dimension is:
  \[
  D = -\frac{\log(N + f/r)}{\log r}
  \]
  where *N* is number of full ruler steps and *f* the remaining length shorter than *r* [Bae 2011, pp. 3-6].
- **JRC estimation**: A third‑order polynomial (Equation 2, R² = 0.993) relates *D* to JRC, calibrated on Barton’s ten profiles [Bae 2011, pp. 3-6]:
  \[
  \text{JRC}(D) = 7\,811\,778.9281\,D^3 - 23\,723\,041.6842\,D^2 + 24\,014\,672.3562\,D - 8\,103\,409.7809
  \]
- **Scan‑circle JRC**: For a joint surface, 36 half‑elliptical scan circles (starting every 10°, moving clockwise) are analysed to capture directional anisotropy. A full‑circle scan circle gives an average JRC [Bae 2011, pp. 6-7].
- **Validation**: Three straight scan lines (same dip direction) on a core surface are measured with mechanical profilometry and compared with the BHTV scan‑circle result [Bae 2011, pp. 6-7].

## Key Findings
- The scan‑circle technique applied to BHTV images yields both an average JRC (full circle) and the range of directional anisotropy (half‑circle scans) for a single joint surface [Bae 2011, pp. 6-7].
- For the analysed granite joint, 36 half‑circle scans gave JRC values between 9.6 and 14.2; the full‑circle JRC was 11.2, close to the average of the half‑circle estimates (11.8) [Bae 2011, pp. 6-7].
- On a companion core sample, three straight scan lines along the dip direction gave JRC values of 6.00, 8.82, and 10.29; the BHTV scan‑circle JRC for the same joint was 9.6, considered a reasonable average [Bae 2011, pp. 6-7].
- Fractal dimensions of Barton’s standard profiles computed with the 1‑2‑4‑8‑16‑32‑64 mm ruler pattern are slightly lower than those reported by Lee et al. (1990), with an average factor of 0.9981; the overall similarity supports the JRC‑*D* polynomial [Bae 2011, pp. 6-7].
- The method can process large volumes of borehole data efficiently, overcoming the labour‑intensive steps of core‑based straight‑scan surveys [Bae 2011, pp. 7-8].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| BHTV‑derived roughness profiles converted from elliptical sinusoidal traces using ruler bars normal to a reference sine curve. | Bae 2011, pp. 2-3 | WellCAD workspace; 1 mm/pixel resolution; reference line defined by dip direction/dip angle. | Enables extraction of continuous straight‑baseline profiles from the borehole wall. |
| Fractal dimension *D* estimated by divider method with *r* = 1, 2, 4, 8, 16, 32, 64 mm gives a stable log(N+f/r)–log(r) slope. | Bae 2011, pp. 3-6 | Applied to digitised Barton profiles (20 px/mm) and later to BHTV profiles. | Consistent ruler pattern yields linear log‑log plot; residual *f* included. |
| JRC = 7.81×10⁶ D³ − 2.37×10⁷ D² + 2.40×10⁷ D − 8.10×10⁶, R² = 0.993. | Bae 2011, pp. 3-6 | Calibrated on Barton’s ten standard profiles; 1 ≤ D ≤ 1.01343. | Third‑order polynomial with very high correlation. |
| Half‑circle scans (36 orientations) yield JRC = 9.6–14.2; full‑circle JRC = 11.2; half‑circle mean = 11.8. | Bae 2011, pp. 6-7 | Same granite joint surface imaged by BHTV. | Demonstrates anisotropy and agreement of full‑circle with mean JRC. |
| Straight scan lines on core gave JRC = 6.00, 8.82, 10.29; corresponding BHTV scan‑circle JRC = 9.6. | Bae 2011, pp. 6-7 | Core profilometry at 1 mm slice interval; scan lines oriented along dip direction. | Scan‑circle result lies within the range of straight‑line values, supporting its use as an average. |
| Fractal dimension values for Barton’s profiles are lower than those of Lee et al. (1990) by a factor of 0.9981 on average. | Bae 2011, pp. 6-7 | Same Barton profiles digitised; Lee et al. used ruler pattern 2, 4, 6, 8, 10 and second‑order polynomial. | Discrepancy attributed to different ruler intervals and polynomial order. |
| The technique can process thousands of metres of borehole data rapidly under WellCAD. | Bae 2011, pp. 7-8 | Linked GUI functions added to WellCAD; BHTV image input. | Enables early‑stage rock mass classification in large underground projects. |

## Limitations
- **Scale effect**: The borehole diameter (76 mm) limits the accessible joint surface length; roughness parameters may not fully represent larger in‑situ joint extents [Bae 2011, pp. 7-8].
- **Image mismatching**: High dip angle joints can suffer from image mismatch between upper and lower surfaces due to drilling‑induced fragmentation, especially near fracture zones or fault boundaries [Bae 2011, pp. 6-7].
- **Directional uncertainty**: Straight‑scan‑line derived JRC can over‑ or underestimate shear resistance depending on sliding direction; half‑circle scans only indicate anisotropy range, not a full directional function [Bae 2011, pp. 6-7].
- **Statistical requirement**: To reduce scale and local heterogeneity effects, results should be analysed statistically per joint set using multiple boreholes [Bae 2011, pp. 7-8].
- **Validation gap**: No direct shear tests were performed to confirm the relationship between scan‑circle JRC and mechanical behaviour [Bae 2011, pp. 7-8].

## Assumptions / Conditions
- Natural rock joint profiles are **self‑affine** fractals, justifying the divider method [Bae 2011, pp. 3-6].
- Barton’s ten standard profiles provide an adequate reference for JRC calibration [Bae 2011, pp. 3-6].
- **Ruler pattern** of 1, 2, 4, 8, 16, 32, 64 mm yields a sufficiently stable fractal dimension; other patterns may give different D values [Bae 2011, pp. 3-6].
- BHTV acoustic image resolution of 1 pixel = 1 mm; photo‑image resolution can be up to 20 pixels/mm, affecting profile detail [Bae 2011, pp. 2-3].
- The WellCAD software environment is available and the custom GUI functions have been correctly implemented [Bae 2011, pp. 1-2, 3‑6].
- The borehole diameter is standard (76 mm) and the granite rock mass is that of the KAERI site [Bae 2011, pp. 1-2].

## Key Variables / Parameters
- **Fractal dimension (D)**: dimensionless, computed from the log‑log slope.
- **Joint Roughness Coefficient (JRC)**: dimensionless, range 0–20 [Bae 2011, pp. 1-2].
- **Number of steps (N)** for a given ruler span *r* [Bae 2011, pp. 3-6].
- **Ruler span (r)**: mm, series 1, 2, 4, 8, 16, 32, 64 mm [Bae 2011, pp. 3-6].
- **Remaining length (f)**: mm, portion shorter than *r* at the end of a profile [Bae 2011, pp. 3-6].
- **Dip angle and dip direction**: define the reference sine curve orientation [Bae 2011, pp. 2-3].
- **Scan‑circle type**: full circle (360°) or half‑circle; number of rotations (e.g., 36 half circles at 10° intervals) [Bae 2011, pp. 6-7].
- **Profile resolution**: 1 pixel/mm (BHTV) or 20 pixels/mm (photo) [Bae 2011, pp. 2-3].
- **Borehole diameter**: 76 mm (implicit in the equipment) [Bae 2011, pp. 7-8].

## Reusable Claims
1. **Claim**: Using the divider method with ruler spans 1, 2, 4, 8, 16, 32, 64 mm on digitised rock joint profiles provides a stable fractal dimension for self‑affine roughness.  
   *Condition*: The profile length is large relative to the chosen ruler spans; the total number of steps N and residual f are counted.  
   *Limitation*: Other ruler progressions may yield slightly different D values. [Bae 2011, pp. 3-6]

2. **Claim**: The fractal dimension D of Barton’s ten standard roughness profiles can be related to the JRC range by a third‑order polynomial with R² = 0.993, enabling JRC estimation from D without visual comparison.  
   *Condition*: The same ruler pattern (1, 2, 4, 8, 16, 32, 64 mm) and Equation 2 are used.  
   *Limitation*: The relationship is valid for JRC 0–20; for other roughness scales or rock types, recalibration may be needed. [Bae 2011, pp. 3-6]

3. **Claim**: A scan‑circle (full elliptical circumference) extracted from a BHTV image of a borehole wall can provide an average JRC for a joint, while half‑circle scans reveal the range of directional anisotropy.  
   *Condition*: Joint dip orientation is correctly identified; the ruler‑bar extraction is performed normal to the reference sine curve.  
   *Limitation*: The borehole diameter limits the scanned surface length; image mismatches at sharp edges may require manual correction. [Bae 2011, pp. 2-3, 6‑7, 7‑8]

4. **Claim**: For a granite joint, the BHTV scan‑circle JRC (9.6) fell within the range of three straight scan‑line JRC values (6.00–10.29) measured on the same joint in a drill core, indicating that the scan‑circle method can serve as a practical substitute for multiple straight scans.  
   *Condition*: The scan lines on the core are oriented along the dip direction; the BHTV image and profilometry resolution are comparable.  
   *Limitation*: Only one joint and three straight lines were tested; generalizability requires more data. [Bae 2011, pp. 6-7]

5. **Claim**: The proposed technique overcomes the labour‑intensive steps of isolating joints from core, manually measuring profiles, and computing fractal dimensions for numerous joints, making it feasible to process thousands of metres of borehole data in underground projects.  
   *Condition*: WellCAD is available with the added GUI functions; BHTV images cover the borehole wall.  
   *Limitation*: Scale effect and drilling‑induced artefacts must be addressed through statistical analysis per joint set. [Bae 2011, pp. 7-8]

## Candidate Concepts
- [[Joint Roughness Coefficient (JRC)]]
- [[fractal dimension]]
- [[borehole televiewer (BHTV)]]
- [[scan circle technique]]
- [[self-affine fractal]]
- [[WellCAD]]
- [[FAC40 Televiewer]]
- [[divider method]]
- [[Barton’s standard roughness profiles]]
- [[half-scan circle]]
- [[full-scan circle]]
- [[dip angle and dip direction]]
- [[fracture roughness anisotropy]]

## Candidate Methods
- [[Scan circle roughness extraction from BHTV images]]
- [[Divider method for fractal dimension of joint profiles]]
- [[BHTV image processing for sinusoidal joint trace extraction]]
- [[Third-order polynomial calibration of JRC to fractal dimension]]
- [[Comparison of scan‑circle and straight‑scan‑line JRC on core]]

## Connections To Other Work
- **Lee et al. (1990)**: The divider method and fractal dimension approach is directly compared; this study’s fractal dimension values are slightly lower (average factor 0.9981) due to different ruler patterns and a third‑order polynomial [Bae 2011, pp. 3-6, 6‑7].
- **Barton and Choubey (1977)**: The JRC concept and the ten standard profiles form the basis of the calibration [Bae 2011, pp. 1-2].
- **Kulatilake et al. (1997, 1998, 1999, 2006)**: Self‑affine roughness quantification and the line‑scaling, variogram, and roughness‑length methods provide the theoretical background for treating joint profiles as self‑affine fractals [Bae 2011, pp. 3-6, 8].
- **Huang et al. (1992)**, **Miller et al. (1990)**, **Odling (1994)**: Previous work on fractal characterisation of rock joint profiles supports the use of fractal dimension for JRC estimation [Bae 2011, pp. 1-2].
- **Franklin and Maerz (1986)**, **Maerz et al. (1987)**, **Unal et al. (2004)**, **Fardin et al. (2004)**: Alternative roughness measurement techniques (photo‑analysis, laser scanning) are cited as precursors to this automated borehole‑based method [Bae 2011, pp. 1-2].

## Open Questions
- How well does the scan‑circle JRC correlate with direct shear strength for different joint sets, and what scale corrections are needed for borehole diameters other than 76 mm? [Bae 2011, pp. 7-8]
- Can statistical averaging by joint set from multiple boreholes sufficiently reduce the scale effect, and what is the minimum sample size required? [Bae 2011, pp. 7-8]
- What is the optimal number and spacing of half‑scan circles to reliably capture directional anisotropy for highly anisotropic joints? [Bae 2011, pp. 6-7]
- How can image mismatches at high‑dip‑angle joints be automatically detected and corrected without manual comparison with core photos? [Bae 2011, pp. 6-7]

## Source Coverage
All non‑empty indexed fragments from the paper were processed. Coverage metrics:  
- Number of indexed text blocks: 6  
- Compiled source blocks: 6  
- Coverage ratio by blocks: 1.0 (full)  
- Total indexed characters: 27 268  
- Compiled characters: 27 385  
- Coverage ratio by characters: 1.004 (essentially complete)
