---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2006-p-rez-l-pez-on-measuring-the-fractal-anisotropy-of-2-d-geometrical-sets-application-to-the"
title: "On Measuring the Fractal Anisotropy of 2-D Geometrical Sets: Application to the Spatial Distribution of Fractures."
status: "draft"
source_pdf: "data/papers/On measuring the fractal anisotropy of 2-D geometrical sets Application to the spatial distribution of fractures.pdf"
collections:
citation: "Pérez-López, R., and C. Paredes. \"On Measuring the Fractal Anisotropy of 2-D Geometrical Sets: Application to the Spatial Distribution of Fractures.\" *Geoderma*, vol. 134, 2006, pp. 402–14. doi:10.1016/j.geoderma.2006.03.022."
indexed_texts: "9"
indexed_chars: "43111"
nonempty_source_blocks: "9"
compiled_source_blocks: "9"
compiled_source_chars: "43333"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.005149"
coverage_status: "full-index"
source_signature: "99cd3008adb253fedf71c06f5b27e7aa00abc289"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:35:19"
---

# On Measuring the Fractal Anisotropy of 2-D Geometrical Sets: Application to the Spatial Distribution of Fractures.

## One-line Summary
A methodology is presented to estimate the fractal anisotropy of 2D fracture distributions using oriented Cantorian profiles, revealing a perpendicular relationship between the axes of the fractal anisotropy ellipse and the principal stress axes, and allowing for the relative dating of fracture sets.

## Research Question
How can the fractal anisotropy of a 2D spatial distribution of segments be estimated and correlated with structural geometrical parameters and the relative dating of fracture sets? [Paredes 2006, pp. 1-2]

## Study Area / Data
The methodology was applied to the spatial distribution of fault and fracture traces interpreted from digital terrain models (DEM) and aerial photography in the Spanish Central System, specifically a granitic massif near Toledo. [Paredes 2006, pp. 2-3] The analysis used structural maps filtered by stress fields (dynamical maps) for the Permian and Alpine tectonic events. [Paredes 2006, pp. 3-4]

## Methods
1.  **Fractal Anisotropy Measurement:** Fractal anisotropy is defined as the variation of the 1D fractal dimension with the measurement direction. [Paredes 2006, pp. 4-6]
2.  **Cantorian Profiles:** Oriented transects are intersected with the 2D fracture map to create 1D point distributions (Cantorian profiles). [Paredes 2006, pp. 4-6]
3.  **Interval-Counting:** The 1D fractal dimension (D0) for each oriented profile is obtained using the interval-counting (box-counting) technique. [Paredes 2006, pp. 2-3]
4.  **Anisotropy Fractal Analysis (AFA) Code:** A computer code systematically rotates transects (e.g., in 10° steps from N0°E to N180°E) and applies automatic box-counting to obtain a set of (D0, θ) points. [Paredes 2006, pp. 6-8]
5.  **Mass Number Enhancement:** To ensure a sufficient number of intersection points (mass number), multiple parallel transects for each orientation are added into a single combined profile. [Paredes 2006, pp. 6-8]
6.  **Ellipse Fitting:** The (D0, θ) points are plotted in a polar coordinate system, and an ellipse is fitted using a least-squares method to characterize the anisotropy. [Paredes 2006, pp. 6-8]

## Key Findings
1.  The fractal dimension D0 of a 2D fracture map, when measured along oriented transects, describes an ellipse in a polar plot. The long axis (DHmax) represents the maximum fractal dimension, and the short axis (DHmin) represents the minimum. [Paredes 2006, pp. 1-2]
2.  A spatial perpendicular relationship was established between the axes of the fractal anisotropy ellipse and the axes of the stress tensor that produced the fractures: the long axis (DHmax) is normal to the maximum horizontal stress (σHmax). [Paredes 2006, pp. 1-2, 8-10]
3.  Variations in the D0 value for consecutive profiles along the fractal ellipse can be used to define azimuthal filters. A variation greater than 20% was considered the borderline between different fracture sets. [Paredes 2006, pp. 1-2]
4.  Fractal sets with lower fractal dimensions were interpreted as older than those with higher values, as the most recent stress field increases geometrical complexity through reactivation and neoformation. [Paredes 2006, pp. 1-2, 12-13]
5.  The filtered fault families derived from the fractal anisotropy ellipse were in general agreement with those from dynamical maps obtained via classical structural analysis. [Paredes 2006, pp. 1-2]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| The fractal anisotropy of fractures forms an ellipse in a polar plot, with DHmax oriented N168°E (Permian) and ESE-WNW (Alpine). | [Paredes 2006, pp. 6-8] | Applied to filtered dynamical maps of Permian and Alpine fracture sets in the Spanish Central System. | Ellipse parameters are given in Table 1 of the source. |
| The long axis of the fractal anisotropy ellipse (DHmax) is normal to the maximum horizontal stress (σHmax). | [Paredes 2006, pp. 8-10] | Comparison of fractal ellipses with stress tensors from Fault Population analysis. | This perpendicular relationship is a key structural finding. |
| A variation in D0 greater than 20% between neighboring profiles indicates a borderline between different fracture sets. | [Paredes 2006, pp. 1-2, 10-12] | Analysis of the total lineament ellipse. | This criterion was used to divide the ellipse into arc-segments for relative dating. |
| Fractal sets with lower D0 are interpreted as older; those with higher D0 are interpreted as younger or reactivated. | [Paredes 2006, pp. 1-2, 12-13] | Based on the idea that reactivation increases geometrical complexity. | Example: Alpine fracture map (D=1.79) > Permian fracture map (D=1.73). |
| The AFA code uses parallel transects added into a single profile to ensure a sufficient mass number for reliable D0 calculation. | [Paredes 2006, pp. 6-8] | Methodology for obtaining Cantorian profiles. | The fractal dimension of the combined profile (0.89) was similar to the highest individual transect (0.88). |

## Limitations
1.  The box-counting analysis is extremely sensitive to the chosen range of inner and outer cut-off limits for power-law fitting. [Paredes 2006, pp. 8-10]
2.  The relative dating based on fractal anisotropy must be interpreted carefully within the context of structural and geological advice, as fault sets can be reactivated. [Paredes 2006, pp. 10-12]
3.  The fractal dimension difference between the Permian and Alpine maps (1.73 vs 1.79) was considered poorly significant for establishing a definitive structural fractal criterion. [Paredes 2006, pp. 8-10]

## Assumptions / Conditions
1.  The spatial distribution of faults is controlled by a particular tectonic stress regime, and the fractal dimension is related to the stress tensor. [Paredes 2006, pp. 2-3]
2.  Fractal anisotropy is the spatial variability of the fractal dimension in relation to the orientation of the measure. [Paredes 2006, pp. 2-3]
3.  The intersection between a spatial fault distribution and a transect produces a 1D point distribution with a Cantorian structure. [Paredes 2006, pp. 4-6]
4.  Ancient fracture sets yield lower fractal dimensions than more recent, reactivated fracture sets. [Paredes 2006, pp. 10-12]
5.  The structural map must contain fracture traces ranging over a minimum of three orders of magnitude to be geometrically representative. [Paredes 2006, pp. 3-4]

## Key Variables / Parameters
*   **D0:** 1D fractal dimension obtained from interval-counting on a Cantorian profile.
*   **θ:** Orientation (azimuth) of the transect.
*   **DHmax:** Maximum horizontal fractal dimension (long axis of the fractal ellipse).
*   **DHmin:** Minimum horizontal fractal dimension (short axis of the fractal ellipse).
*   **σHmax:** Maximum horizontal stress.
*   **σHmin:** Minimum horizontal stress.
*   **C.A.:** Coefficient of anisotropy.
*   **Mass Number:** The number of intersection points in a Cantorian profile.

## Reusable Claims
1.  **Condition:** For a 2D spatial distribution of fractures generated by a tectonic stress field. **Claim:** The fractal anisotropy, represented as an ellipse in a polar plot of D0 vs. θ, has its long axis (DHmax) oriented perpendicular to the maximum horizontal stress (σHmax). [Paredes 2006, pp. 1-2, 8-10]
2.  **Condition:** When analyzing the fractal anisotropy ellipse of a composite fracture map. **Claim:** A variation in the 1D fractal dimension (D0) greater than 20% between neighboring oriented profiles can be used as a criterion to distinguish between different fracture sets. [Paredes 2006, pp. 1-2, 10-12]
3.  **Condition:** In a region with multiple superimposed tectonic events. **Claim:** Fracture sets with lower fractal dimensions can be interpreted as older and less reactivated, while sets with higher fractal dimensions indicate younger or more reactivated sets with greater geometrical complexity. [Paredes 2006, pp. 1-2, 12-13]

## Candidate Concepts
*   [[Fractal anisotropy]]
*   [[Cantorian profile]]
*   [[Dynamical map]]
*   [[Stress tensor]]
*   [[Fracture reactivation]]
*   [[Box-counting]]
*   [[Interval-counting]]

## Candidate Methods
*   [[Anisotropy Fractal Analysis (AFA) code]]
*   [[Oriented transect method]]
*   [[Mass number enhancement via parallel transects]]
*   [[Least-squares ellipse fitting to polar data]]

## Connections To Other Work
*   Builds on the Cantor's Dust analysis of spatial fault distribution first developed by Velde et al. (1990) and revised by Harris et al. (1991). [Paredes 2006, pp. 4-6]
*   Extends the work of Pérez-López et al. (2000), who first obtained 2D fractal anisotropy but without a robust methodology. [Paredes 2006, pp. 4-6]
*   Uses Fault Population analysis techniques (e.g., Angelier, 1979; Etchecopar et al., 1981) to filter fracture patterns by stress field. [Paredes 2006, pp. 3-4]
*   The interval-counting technique is referenced from Hasting and Sugihara (1993) and Volland and Kruhl (2004). [Paredes 2006, pp. 2-3]

## Open Questions
1.  How robust is the 20% variation threshold for separating fracture sets across different geological settings and scales?
2.  Can this fractal anisotropy methodology be reliably applied to fracture networks where reactivation is pervasive and obscures the original stress field signatures?
3.  What is the precise relationship between the coefficient of anisotropy (C.A.) and the mechanical properties of the rock or the intensity of the stress field?

## Source Coverage
All non-empty indexed fragments were processed. The compilation used 9 source blocks containing 43,111 characters. The compiled page contains 43,333 characters, resulting in a coverage ratio by characters of 1.005. The coverage status is full-index.
