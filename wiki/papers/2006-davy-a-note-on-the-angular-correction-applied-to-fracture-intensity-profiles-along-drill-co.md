---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2006-davy-a-note-on-the-angular-correction-applied-to-fracture-intensity-profiles-along-drill-co"
title: "A Note on the Angular Correction Applied to Fracture Intensity Profiles along Drill Core."
status: "draft"
source_pdf: "data/papers/A note on the angular correction applied to fracture intensity profiles along drill core.pdf"
collections:
citation: "Davy, P., et al. “A Note on the Angular Correction Applied to Fracture Intensity Profiles along Drill Core.” *Journal of Geophysical Research*, vol. 111, 2006, B11408, doi:10.1029/2005JB004121."
indexed_texts: "7"
indexed_chars: "34032"
nonempty_source_blocks: "7"
compiled_source_blocks: "7"
compiled_source_chars: "34177"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004261"
coverage_status: "full-index"
source_signature: "684b52e3395f9913fc45600db3b74c28b872c419"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:27:50"
---

# A Note on the Angular Correction Applied to Fracture Intensity Profiles along Drill Core.

## One-line Summary
This paper derives and validates a new angular correction for borehole fracture intensity data that accounts for a power law fracture length distribution, showing it improves consistency with outcrop data compared to the classical Terzaghi correction.

## Research Question
How should the angular correction applied to fracture intensities measured along drill core be modified when the fracture network has a power law length distribution, and can this correction reconcile orientation discrepancies between borehole and outcrop data?

## Study Area / Data
The study uses data from the Simpevarp investigation site in SE Sweden, which is being studied for a spent nuclear fuel repository. The dataset consists of three flat-lying outcrop maps and three oriented drill cores [Davy 2006, pp. 1-1]. The outcrops were mapped with a fracture trace length resolution down to 0.50 m [Davy 2006, pp. 1-1]. Fractures in the cores were recorded from visual inspection and high-resolution optical borehole imagery, including only fractures whose trace is continuous all around the core and borehole walls [Davy 2006, pp. 1-3].

## Methods
The authors derive an analytical expression for the core fracture intensity (n1D) as a function of the 3D fracture intensity (n3D) for a power law length distribution. They model fractures as infinitely thin, circular disks [Davy 2006, pp. 1-3]. For dipping fractures, the transecting probability is calculated using Monte Carlo simulations where fracture length and center position are stochastically drawn from probability distributions [Davy 2006, pp. 3-4]. The derived correction factor is parameterized and approximated by a polynomial function (Equation 6) [Davy 2006, pp. 4-5]. The correction is tested by comparing the dip distribution ratios between outcrops and boreholes before and after applying the correction [Davy 2006, pp. 5-6].

## Key Findings
1.  For fracture networks with a power law length distribution where the exponent a3D > 3, the classical Terzaghi correction (cosθ) is invalid. The new angular correction factor P(θ) depends on (cosθ)^(a3D-2) and decreases much faster with dip angle θ than the Terzaghi correction [Davy 2006, pp. 4-5].
2.  The discrepancy between the new correction and the Terzaghi correction is significant; for a3D = 4, the intersection probability is 4.5 times smaller than the Terzaghi correction at θ = 80° [Davy 2006, pp. 4-5].
3.  If the power law exponent a3D < 3, or if the lower bound of the length distribution (lmin) is much larger (>5-10 times) than the core diameter, the classical Terzaghi correction applies [Davy 2006, pp. 4-5, 6-7].
4.  Applying the new correction to data from the Simpevarp site achieved consistency between the dip distributions of outcrops and boreholes, whereas the classical Terzaghi correction did not [Davy 2006, pp. 6-7]. The power law exponents predicted by the consistency condition matched those measured from outcrop length distributions [Davy 2006, pp. 6-7].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| The classical Terzaghi correction is no longer valid when fracture networks have a length distribution. | [Davy 2006, pp. 1-1] | Fracture intensity calculated from fractures that fully transect the core. | The core diameter acts as a lower cutoff on the recorded length distribution. |
| For a power law length distribution with exponent a3D > 3, the angular correction factor P(θ) is approximated by Equation 6. | [Davy 2006, pp. 4-5] | Fractures are modeled as circular disks; lmin < d (core diameter). | The approximation error is less than 0.01. |
| The number of intersecting fractures depends on core diameter d as d^(3-a3D). | [Davy 2006, pp. 3-4] | a3D > 3 and lmin < d. | This is counterintuitive: smaller cores intersect more fractures due to the length distribution. |
| Consistency between outcrop and borehole dip distributions was achieved using the new correction. | [Davy 2006, pp. 6-7] | Data from Simpevarp site; outcrops ASM025, ASM026, ASM205 and three boreholes. | The required a3D values (3-3.5 and 4-4.5) matched outcrop measurements. |
| If lmin is significantly larger than the borehole diameter, the Terzaghi correction applies. | [Davy 2006, pp. 5-6] | Power law length distribution with non-negligible lower bound. | For lmin = 10d, the Terzaghi correction is valid. |

## Limitations
1.  The analysis assumes fractures are infinitely thin, circular disks. Extension to more complex geometries would require numerical methods [Davy 2006, pp. 1-3].
2.  The correction procedure assumes that the core position is not correlated with the fracture network [Davy 2006, pp. 3-4].
3.  The comparison between outcrops and boreholes cannot fully guarantee that the fracturing distribution is identical at depth (e.g., no depth effect) [Davy 2006, pp. 6-7].
4.  The correction is biased for strictly horizontal or vertical fractures, where the correction factor can take infinite values [Davy 2006, pp. 5-6].

## Assumptions / Conditions
1.  Fracture intensity is calculated from fractures that fully transect the core [Davy 2006, pp. 1-1].
2.  The fracture network has a fractal density and a power law length distribution [Davy 2006, pp. 1-3].
3.  Fracture length, density, and orientations are reasonably independent [Davy 2006, pp. 1-3].
4.  The core is a vertical cylinder [Davy 2006, pp. 1-3].
5.  For the analytical solution, the power law exponent a3D is much larger than 3 and lmin is smaller than the core diameter d [Davy 2006, pp. 3-4].

## Key Variables / Parameters
-   **a3D**: Power law exponent of the 3D fracture length distribution.
-   **D3D**: Fractal dimension of the fracture network density.
-   **d**: Diameter of the drill core.
-   **l**: Fracture length (diameter of the disk model).
-   **lmin, lmax**: Lower and upper bounds of the power law length distribution.
-   **θ (theta)**: Fracture dip angle (for a vertical borehole).
-   **P(θ)**: Angular correction factor (transecting probability relative to a horizontal fracture).
-   **n1D**: Fracture intensity measured along the core (1D measure).
-   **n3D**: 3D fracture intensity.

## Reusable Claims
1.  **Condition**: When analyzing borehole fracture intensity data from networks with a power law length distribution where a3D > 3 and lmin < d. **Claim**: The classical Terzaghi correction (cosθ) significantly overestimates the frequency of fractures subparallel to the borehole. A correction factor dependent on (cosθ)^(a3D-2) must be applied instead [Davy 2006, pp. 1-1, 4-5].
2.  **Condition**: When the lower bound of the fracture length distribution (lmin) is greater than approximately 5-10 times the core diameter. **Claim**: The classical Terzaghi correction (cosθ) is valid for correcting borehole fracture intensity data [Davy 2006, pp. 5-6, 6-7].
3.  **Condition**: For a vertical borehole sampling a fracture network with a power law length distribution. **Claim**: The number of fractures intersecting the core scales with core diameter as d^(3-a3D), meaning smaller cores may intersect more fractures if a3D > 3 [Davy 2006, pp. 3-4].

## Candidate Concepts
-   [[Terzaghi correction]]
-   [[Fracture intensity]]
-   [[Power law distribution]]
-   [[Fractal fracture network]]
-   [[Stereology]]
-   [[Borehole imagery]]
-   [[Nuclear waste repository]]

## Candidate Methods
-   [[Monte Carlo simulation]]
-   [[Angular correction]]
-   [[Stereological analysis]]
-   [[Outcrop-borehole consistency analysis]]

## Connections To Other Work
The paper revisits the Terzaghi correction [Terzaghi, 1965] and addresses inconsistencies noted in previous studies [e.g., Peacock et al., 2003]. It builds on work regarding fractal and power law models for fracture networks [Bonnet et al., 2001; Davy et al., 1990; Bour et al., 2002] and their hydraulic implications [Bour and Davy, 1997, 1998; de Dreuzy et al., 2000, 2001a, 2001b]. The data and context are part of the site investigation for the Swedish Nuclear Fuel and Waste Management Company (SKB) [Svensk Kärnbränslehantering (SKB), 2004, 2005].

## Open Questions
1.  What is the actual lower bound (lmin) of the power law length distribution for microfractures, and how does it vary? This has important consequences for the applicable correction [Davy 2006, pp. 5-6].
2.  How can the correction be extended to non-vertical boreholes and more complex fracture geometries (e.g., non-circular disks)? [Davy 2006, pp. 1-3, 3-4].
3.  How do superficial fracturing processes, which may produce predominantly horizontal fractures, affect the consistency between shallow outcrops and deeper boreholes? [Davy 2006, pp. 1-1].

## Source Coverage
All non-empty indexed fragments were processed. The compilation used 7 source blocks containing a total of 34,032 characters. The compiled page contains 34,177 characters, resulting in a coverage ratio by characters of 1.004. The coverage status is full-index.
