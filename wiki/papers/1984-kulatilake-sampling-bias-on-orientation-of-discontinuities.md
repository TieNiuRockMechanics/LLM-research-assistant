---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "1984-kulatilake-sampling-bias-on-orientation-of-discontinuities"
title: "Sampling Bias on Orientation of Discontinuities."
status: "draft"
source_pdf: "data/papers/1984 - Sampling bias on orientation of discontinuities.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Kulatilake, P. H. S. W., and T. H. Wu. \"Sampling Bias on Orientation of Discontinuities.\" *Rock Mechanics and Rock Engineering*, vol. 17, 1984, pp. 243-253."
indexed_texts: "3"
indexed_chars: "12155"
nonempty_source_blocks: "3"
compiled_source_blocks: "3"
compiled_source_chars: "11904"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.97935"
coverage_status: "full-index"
source_signature: "7b4664c46b3c5bae8ef33ca5a8bcc654a3ecbbdc"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T10:54:16"
---

# Sampling Bias on Orientation of Discontinuities.

## One-line Summary
This paper derives the probability of intersection between a thin circular disc of finite diameter and a vertical rectangular window, and uses this probability to develop a weighting function for correcting orientation bias in discontinuity surveys [Kulatilake 1984, pp. 1-5]; [Kulatilake 1984, pp. 5-10].

## Research Question
In discontinuity surveys, biases are introduced in sampling for geometrical properties. While Terzaghi (1965) developed a correction for planar discontinuities of infinite size, the shape and size of both the discontinuity and the exposure also influence the probability of intersection when discontinuities have finite size and intersect finite-size exposures. This paper aims to derive a correction for orientation data that accounts for the finite size of disc-shaped discontinuities intersecting a finite rectangular sampling window [Kulatilake 1984, pp. 1-5].

## Study Area / Data
The method is applied to dip directions and dip angles collected from the red shales of the Conemaugh Shale Formation in southeastern Ohio, U.S.A. The data were obtained from a vertical rectangular window of width w = 0.9 m and height h = 0.6 m, making an angle of 90 degrees with north (γ = π/2). The shears were exposed in windows and their orientations measured by Williams (1982) [Kulatilake 1984, pp. 10-11].

## Methods
Discontinuities are modeled as thin circular discs with a finite diameter D. The probability that a disc of a given diameter intersects a vertical rectangular window is derived based on the hypothesis: the probability of intersection is proportional to the volume within which the center of the disc must lie for an intersection to occur.

The total volume V is composed of:
- V₁, a parallelepiped volume = 2whx₀
- V₂, half oblique cylinder volume = (πD²/8) * w * sinθ * cosβ
- V₃, half oblique cylinder volume = (πD²/8) * h * cosθ

The coordinate x₀ is derived from the condition that a disc just touches the window corner, leading to x₀ = (D/2)(cos²θ sin²β + cos²β)^(1/2).

Two distinct cases of disc orientation relative to the window are treated separately (Fig. 1a and Fig. 1b). The resulting probability of intersection expressions include terms for window dimensions w and h, disc diameter D, dip θ, and angle β (the difference between dip direction and strike of the sampling plane). Simplified expressions are derived for the limiting case where window dimensions are large compared to disc diameter (D/h → 0, D/w → 0).

A weighting function W, inversely proportional to the probability of intersection, is defined to correct observed frequencies. For practical application, 12 different angular combinations between dip direction α and strike of the sampling plane γ are identified (Fig. 3), and appropriate expressions for β and the weighting functions are tabulated (Table 1). Corrected (unbiased) frequencies are obtained by multiplying observed frequencies by the weighting function and normalizing by the total unbiased number [Kulatilake 1984, pp. 1-5]; [Kulatilake 1984, pp. 5-10].

## Key Findings
For the Conemaugh Shale dataset, the bias correction was found to be small, and the relative frequencies were not sensitive to the ratio D/h within the range from D/h = 1/4 to D/h → 0. The corrected frequencies for an example orientation pair (θ=30°, α=170°, D/h=1/4) changed minimally from the observed frequency (observed: 0.027, corrected: 0.029) [Kulatilake 1984, pp. 10-11].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Probability of intersection for a finite disc with a vertical rectangular window: Pr ∝ Dwh(cos²θ sin²β+cos²β)^(1/2) + (πD²/4)w cosβ sinθ + (πD²/4)h cosθ | [Kulatilake 1984, pp. 5-10] | Disc orientation per Fig. 1a; window dimensions w, h; disc diameter D | General expression Eq. (15) and (16) |
| Large-window approximation: Pr ∝ D(cos²θ sin²β + cos²β)^(1/2) | [Kulatilake 1984, pp. 5-10] | D/h → 0 and D/w → 0, orientation per Fig. 1a | Eq. (17) |
| Weighting function for Fig. 1a orientation, finite window: W = [(cos²θ sin²β + cos²β)^(1/2) + (πD/4h) cosβ sinθ + (πD/4w) cosθ]⁻¹ | [Kulatilake 1984, pp. 5-10] | Window dimensions w, h, disc diameter D | Eq. (20) |
| Weighting function for Fig. 1a orientation, large window: W = (cos²θ sin²β + cos²β)^(-1/2) | [Kulatilake 1984, pp. 5-10] | D/h → 0 and D/w → 0 | Eq. (21) |
| Weighting function for Fig. 1b orientation, finite window: W = [(cos²θ cos²β + sin²β)^(1/2) + (πD/4h) sinβ sinθ + (πD/4w) cosθ]⁻¹ | [Kulatilake 1984, pp. 5-10] | Window dimensions w, h, disc diameter D | Eq. (22) |
| Weighting function for Fig. 1b orientation, large window: W = (cos²θ cos²β + sin²β)^(-1/2) | [Kulatilake 1984, pp. 5-10] | D/h → 0 and D/w → 0 | Eq. (23) |
| Conemaugh Shale example: For (θ=30°, α=170°) with D/h=1/4, W=0.999, observed frequency 0.027 corrected to 0.029; for D/h → 0, W=1.15, corrected frequency 0.029. | [Kulatilake 1984, pp. 10-11] | w=0.9 m, h=0.6 m, γ=90° | Bias correction small; relative frequencies insensitive to D/h in range 1/4 to 0 |

## Limitations
The correction was derived under the assumption of disc-shaped discontinuities. The application to the Conemaugh Shale showed a small bias correction, which may not hold for datasets with different window geometries, discontinuity size distributions, or orientation distributions [Kulatilake 1984, pp. 1-5]; [Kulatilake 1984, pp. 10-11].

## Assumptions / Conditions
- Discontinuities are thin circular discs of finite diameter D [Kulatilake 1984, pp. 1-5].
- The sampling window is a vertical plane of rectangular shape with width w and height h [Kulatilake 1984, pp. 1-5].
- The probability of intersection is proportional to the volume in which the disc center must lie to intersect the window [Kulatilake 1984, pp. 1-5].
- For the large-window simplification, D/h → 0 and D/w → 0 are assumed [Kulatilake 1984, pp. 5-10].

## Key Variables / Parameters
- D: disc diameter
- w, h: width and height of the vertical rectangular window
- θ: dip angle of the disc
- α: dip direction (measured clockwise from north, 0 to 2π)
- γ: strike of the sampling plane (measured clockwise from north, 0 to π)
- β: angular difference between the strike of the sampling plane and the orientation of the disc (derived from α and γ; specific expressions given in Table 1 for 12 cases)
- Pr(I|D, θ, β, h, w): probability of intersection event
- W(θ, β, D, h, w): weighting function for bias correction

## Reusable Claims
- For a thin circular disc of diameter D and a vertical rectangular window (w × h), when the disc orientation follows Fig. 1a, the probability of intersection for large windows (D/h → 0, D/w → 0) is proportional to D(cos²θ sin²β + cos²β)^(1/2) [Kulatilake 1984, pp. 5-10].
- The weighting function for the same large-window case is W = (cos²θ sin²β + cos²β)^(-1/2) [Kulatilake 1984, pp. 5-10].
- In the red shales of the Conemaugh Shale Formation (southeastern Ohio), with a vertical window (w=0.9 m, h=0.6 m), the correction for orientation bias was small and the resulting frequencies were insensitive to the ratio D/h between 1/4 and 0 [Kulatilake 1984, pp. 10-11].

## Candidate Concepts
- [[sampling bias on orientation of discontinuities]]
- [[thin circular disc model for joints]]
- [[probability of intersection of disc with rectangular window]]
- [[weighting function for orientation bias]]
- [[Conemaugh Shale Formation discontinuities]]

## Candidate Methods
- [[geometric probability model for discontinuity intersection]]
- [[correction of orientation data using probability of intersection]]
- [[weighting function for bias correction in orientation surveys]]

## Connections To Other Work
- Terzaghi, R. (1965): Developed a correction for orientation data for planar discontinuities of infinite size [Kulatilake 1984, pp. 1-5].
- Baecher et al. (1977) and Bridges (1976): Represented joints as thin circular discs in discontinuity modeling [Kulatilake 1984, pp. 1-5].
- Glynn et al. (1978): Modeled discontinuities as Poisson planes [Kulatilake 1984, pp. 1-5].
- Robertson (1970): Reported that strike length and dip length of discontinuities were approximately equal, supporting the disc model [Kulatilake 1984, pp. 1-5].
- Williams, R. L. (1982): Provided the Conemaugh Shale orientation data used for the numerical example [Kulatilake 1984, pp. 10-11].

## Open Questions
Whether the derived correction produces significant changes in orientation distributions for other window sizes, discontinuity size distributions, or rock mass settings beyond the Conemaugh Shale example remains to be tested. The sensitivity analysis in the paper was limited to a single dataset and a narrow range of D/h [Kulatilake 1984, pp. 10-11], noting that findings confirm small bias for this case only; extrapolation is not confirmed.

## Source Coverage
All non-empty indexed fragments were processed. Source metrics: indexed_texts = 3, compiled_source_blocks = 3, coverage_ratio_by_blocks = 1.0, coverage_ratio_by_chars = 0.97935, source_signature = 7b4664c46b3c5bae8ef33ca5a8bcc654a3ecbbdc.
