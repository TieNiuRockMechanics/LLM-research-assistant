---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2003-nakaya-percolation-conditions-in-binary-fractal-fracture-networks-applications-to-rock-frac"
title: "Percolation Conditions in Binary Fractal Fracture Networks: Applications to Rock Fractures and Active and Seismogenic Faults."
status: "draft"
source_pdf: "data/papers/2003 - Percolation conditions in binary fractal fracture networks Applications to rock fractures and active and seismogenic faults.pdf"
collections:
citation: "Nakaya, Shinji, et al. “Percolation Conditions in Binary Fractal Fracture Networks: Applications to Rock Fractures and Active and Seismogenic Faults.” Journal of Geophysical Research, vol. 108, no. B7, 2003, p. 2348. doi:10.1029/2002JB002117."
indexed_texts: "10"
indexed_chars: "48128"
nonempty_source_blocks: "10"
compiled_source_blocks: "10"
compiled_source_chars: "48351"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004633"
coverage_status: "full-index"
source_signature: "15f2b321ce6800cc36a44478994bf993f452f32d"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T12:23:52"
---

# Percolation Conditions in Binary Fractal Fracture Networks: Applications to Rock Fractures and Active and Seismogenic Faults.

## One-line Summary
A Monte Carlo study defines a percolation threshold equation in terms of three fractal parameters (D, a, lmax/L) for two-dimensional random binary fractal fracture networks, validates it against natural fracture and fault patterns, and discusses implications for fluid migration and earthquake activity [Nakaya 2003, pp. 1-1; pp. 12-12].

## Research Question
What is the functional relationship that describes the boundary between percolating and nonpercolating states in a random binary fractal fracture network (RBFFN) characterized by the fractal dimension of fracture spatial distribution (D), the fractal dimension of fracture length distribution (a), and the normalized maximum fracture length (lmax/L), and can this relationship predict connectivity in natural rock fractures and seismogenic fault networks? [Nakaya 2003, pp. 1-4; pp. 7-8].

## Study Area / Data
- **Fracture samples (7 sites, multi-scale):**  
  1. Granite (Kuzu/Nanakura, 6.5 cm × 6.5 cm)  
  2. Andesite (Takayama Village, 75 cm × 75 cm)  
  3. Green tuff (Matsushiro, 6 m × 6 m)  
  4. Sandstone (Norway, traced from Odling & Webman [1991], 10 m × 10 m)  
  5–7. Active faults in Nagano Prefecture, Japan, traced from Research Group for Active Faults in Japan [1991]: sample 5 (50 km × 50 km), sample 6 (50 km × 50 km), sample 7 (100 km × 100 km)  
  [Nakaya 2003, pp. 4-4; pp. 4-6]

- **Observed properties:** All samples exhibit fractal spatial (D) and length (a) distributions within certain scale ranges; samples 1–4 are visibly percolating, samples 5–7 are non‑percolating [Nakaya 2003, pp. 6-7; pp. 12-12].

## Methods
1. **Fractal parameter measurement:**  
   - D from box‑counting on fracture‑center points (box size r = L/k); slope of log N(r) vs. log(1/r) [Nakaya 2003, pp. 1-4].  
   - a and lmax from cumulative fracture‑length distribution: ΔN(l) ∝ l⁻ᵃ, lmax defined as l when ΔN(l)=1 (or maximum length in window, with corrections for window‑truncation) [Nakaya 2003, pp. 4-6].

2. **RBFFN model generation:**  
   - Fracture centers: “fractal fragmentation” selects 2^(Dk) out of 2^(2k) boxes at iteration k (k=1,…,m; m=6) [Nakaya 2003, pp. 6-7].  
   - Fracture lengths assigned from power‑law with exponent a and maximum lmax.  
   - Two orthogonal fracture sets, orientations drawn from normal distributions (mean 90° and 180°, σ=7.5°) [Nakaya 2003, pp. 6-7].  
   - Fractures may cross without interaction.

3. **Percolation simulation:**  
   - Domain L × L; percolation occurs when fractures connect opposite sides.  
   - Percolation probability P = Jₚ/J, with J=10 iterations per parameter set [Nakaya 2003, pp. 7-7].  
   - Parameters swept: D=1.0–2.0, a=0.6–3.0, lmax/L=0.1–1.0 [Nakaya 2003, pp. 6-7].

4. **Threshold equation fitting:**  
   - P=0.5 contour taken as percolation threshold.  
   - Fitted form: a = m₁(L₀)(D−2)⁴ + m₂(L₀), with L₀ = lmax/L; m₁ and m₂ are exponential functions of L₀ [Nakaya 2003, pp. 8-9].

5. **Validation:**  
   - Measured D, a, lmax/L of natural samples compared to predicted threshold; Table 3 shows measured vs. predicted percolation status [Nakaya 2003, pp. 12-12].

## Key Findings
- The percolation probability P varies continuously with D, a, and lmax/L. Percolation seldom occurs when 0.1 ≤ lmax/L ≤ 0.3 and a ≥ 3.0, or when 0.6 ≤ a ≤ 1.0 [Nakaya 2003, pp. 7-9].
- The percolation threshold is well described by equation (3):  
  a = m₁(L₀)(D−2)⁴ + m₂(L₀), with m₁(L₀)=117.5 exp(−3.926 L₀), m₂(L₀)=3.492 exp(−0.6582 L₀), valid for D < 2, 1 < a ≤ 3, L₀ < 1 [Nakaya 2003, pp. 8-9].
- Fracture density (r) alone does not provide a simple percolation criterion; equation (3) outperforms a density‑based threshold because it directly incorporates the measurable fractal parameters [Nakaya 2003, pp. 9-10].
- Measured parameters of natural fracture networks confirm the threshold: samples 1–4 (granite, andesite, green tuff, sandstone) fall in the percolated domain; active fault samples 5–7 (lmax/L ≈ 0.19–0.25) fall in the nonpercolated domain [Nakaya 2003, pp. 12-12, Table 3].
- For seismogenic faults, if a ≈ 2 (corresponding to b ≈ 1 in Gutenberg‑Richter relation, via a = 2b) and lmax/L = 1, equation (3) gives D > 1.5 as the condition for percolation. This suggests that dynamic fault networks with D₃ − 1 > 1.5 may form connected fluid pathways [Nakaya 2003, pp. 10-12].

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Percolation probability P changes continuously with D (1.0–2.0), a (0.6–3.0), lmax/L (0.1–1.0); rare percolation when 0.1≤lmax/L≤0.3 and a≥3.0, or 0.6≤a≤1.0 | [Nakaya 2003, pp. 7-9] | 2D RBFFN, m=6, J=10 simulations per parameter set, two orthogonal normal fracture sets (σ=7.5°) | P contours plotted in Fig 7; qualitative description |
| Percolation threshold equation (3): a = m₁(L₀)(D−2)⁴ + m₂(L₀), with m₁, m₂ as exponentials of L₀ | [Nakaya 2003, pp. 8-9] | D<2, 1<a≤3, L₀=lmax/L<1; fitted to P=0.5 contours | Empirical; m₁=117.5e^(−3.926L₀), m₂=3.492e^(−0.6582L₀) |
| True fracture density r relates to r₀ (eq. 4) by log r = 0.975 log r₀ | [Nakaya 2003, pp. 9-10] | L=10 m, k=6, D,a,lmax/L as above | Adjustment for fractures extending beyond L×L domain |
| Fracture density isodensity lines do not coincide with percolation threshold (eq. 3); P cannot be expressed simply as a function of r | [Nakaya 2003, pp. 9-10] | Same as above | Therefore eq. 3 is preferred for percolation prediction |
| Measured D, a, lmax/L of natural samples 1–7 (Table 3) match predicted percolation status: samples 1–4 percolated, samples 5–7 nonpercolated | [Nakaya 2003, pp. 12-12] | Fracture traces from Odling & Webman [1991]; fault traces from Research Group for Active Faults in Japan [1991]; | Strong agreement validates eq. 3 for natural fracture networks |
| For a=2 (b≈1), lmax/L=1, percolation requires D>1.5; if D₃−1>1.5, dynamic fault network may percolate | [Nakaya 2003, pp. 10-12] | Using relation a=2b from Gutenberg‑Richter, log S=M−4.07 (Sato, 1979) | Suggests that fluid migration paths can exist when condition met |

## Limitations
- Fractures are modeled as straight lines, which may segment undulating natural fractures, shifting length distributions [Nakaya 2003, pp. 4-6].
- Fractures extending beyond the sampling window are misrepresented as shorter, potentially underestimating lmax [Nakaya 2003, pp. 4-6].
- Fractal behavior may be range‑limited; only linear sections of log‑log plots used, and upper fractal limit (exponential cutoff) may affect lmax [Nakaya 2003, pp. 4-6].
- Box‑counting on large windows can yield anomalously high D for large r, causing log‑log curvature; this was handled by selecting appropriate scaling ranges [Nakaya 2003, pp. 4-6].
- The RBFFN model assumes two orthogonal, normally distributed fracture sets; actual fracture orientations may be more complex [Nakaya 2003, pp. 6-7].
- Monte Carlo simulations used m=6 (fragmentation steps) and J=10 realizations per parameter set; statistical robustness may be limited [Nakaya 2003, pp. 7-7].
- Equation (3) is empirical, derived from fitting P=0.5 contours, not from fundamental percolation theory [Nakaya 2003, pp. 8-10].
- The study is restricted to two‑dimensional networks; three‑dimensional fractal parameters and their relation to 2D measures are needed for full application to field data [Nakaya 2003, pp. 11-12].

## Assumptions / Conditions
- Domain is square L × L; percolation requires connection across opposite sides [Nakaya 2003, pp. 7-7].
- Fracture centers are placed by a recursive fragmentation process that preserves the box‑counting fractal dimension D [Nakaya 2003, pp. 6-7].
- Fracture length distribution is a pure power law with exponent a and upper cutoff lmax [Nakaya 2003, pp. 4-6].
- Fracture orientations are restricted to two orthogonal sets with normally distributed deviations (mean 90° and 180°, σ=7.5°) [Nakaya 2003, pp. 6-7].
- Fractures cross without any mechanical interaction [Nakaya 2003, pp. 7-7].
- Parameter ranges considered: 1.0≤D≤2.0, 0.6≤a≤3.0, 0.1≤lmax/L≤1.0 [Nakaya 2003, pp. 6-7].
- m=6 and J=10 held constant in all simulations [Nakaya 2003, pp. 7-7].
- Natural fracture samples are traced from published maps and assumed to adequately represent the fracture network geometry [Nakaya 2003, pp. 4-6; Table 3].

## Key Variables / Parameters
- D: fractal dimension of spatial distribution of fracture centers (box‑counting) [Nakaya 2003, pp. 1-4].
- a: fractal dimension (negative exponent) of fracture length distribution; a=2b for earthquake catalogues [Nakaya 2003, pp. 4-6; pp. 10-12].
- lmax: maximum fracture length; L: domain length; L₀ = lmax/L [Nakaya 2003, pp. 1-4, 6-7].
- m: number of fragmentation iterations (m=6) [Nakaya 2003, pp. 6-7].
- J: number of Monte Carlo realizations per (D,a,lmax/L) set (J=10) [Nakaya 2003, pp. 7-7].
- P: percolation probability, defined as frequency of networks connecting domain boundaries [Nakaya 2003, pp. 7-7].
- r₀: apparent fracture density from eq. 4; r: adjusted true fracture density via eq. 5 [Nakaya 2003, pp. 9-10].

## Reusable Claims
- **Claim:** In 2D random binary fractal fracture networks, when 0.1 ≤ lmax/L ≤ 0.3 and a ≥ 3.0, or 0.6 ≤ a ≤ 1.0, percolation is rare.  
  *Source:* [Nakaya 2003, pp. 7-9]  
  *Condition:* RBFFN with D∈[1.0,2.0], two orthogonal normal fracture sets, m=6, J=10.

- **Claim:** The percolation threshold for such networks is given by a = 117.5 e^(−3.926 L₀) (D−2)⁴ + 3.492 e^(−0.6582 L₀), where L₀ = lmax/L, valid for D < 2, 1 < a ≤ 3, L₀ < 1.  
  *Source:* [Nakaya 2003, pp. 8-9]  
  *Condition:* Same RBFFN configuration; empirical fit to P=0.5 contour.

- **Claim:** The percolation threshold cannot be reduced to a single fracture‑density (cumulative length per area) criterion; the fractal parameters D, a, and lmax/L are necessary.  
  *Source:* [Nakaya 2003, pp. 9-10]  
  *Condition:* Based on disagreement between eq. 3 and isodensity lines; true r from eq. 5.

- **Claim:** Natural fracture networks with lmax/L < 0.25 and a < 3 are unlikely to percolate.  
  *Source:* [Nakaya 2003, pp. 10-12]  
  *Condition:* Observation from threshold equation and natural sample data.

- **Claim:** For seismogenic fault networks where a = 2 (b = 1) and lmax/L = 1, the condition for percolation is D > 1.5; in three dimensions this translates to D₃ − 1 > 1.5.  
  *Source:* [Nakaya 2003, pp. 10-12]  
  *Condition:* Based on Gutenberg‑Richter relation and Sato’s log S = M−4.07; assumes fractal spatial distribution with D₃ = D + 1.

- **Claim:** Measured fractal parameters of sandstone (Norway), granite, andesite, and green tuff indicate percolating networks, while active fault traces in Nagano Prefecture are nonpercolating, consistent with the binary fractal threshold.  
  *Source:* [Nakaya 2003, pp. 12-12, Table 3]  
  *Condition:* Using traces from Odling & Webman [1991] and Research Group for Active Faults in Japan [1991]; parameter ranges as given.

## Candidate Concepts
- [[binary fractal fracture network]]
- [[percolation threshold]]
- [[fractal dimension D (spatial)]]
- [[fractal dimension a (length)]]
- [[maximum fracture length lmax]]
- [[fractal fragmentation method]]
- [[random binary fractal fracture network (RBFFN)]]
- [[fracture network connectivity]]
- [[percolation probability]]
- [[fracture density]]
- [[seismogenic fault network]]
- [[fluid migration in fractures]]
- [[Gutenberg-Richter b-value]]
- [[magnitude-fault area scaling]]

## Candidate Methods
- [[box-counting method]]
- [[power-law length distribution fitting]]
- [[fractal fragmentation for fracture center placement]]
- [[Monte Carlo percolation simulation]]
- [[percolation probability calculation]]
- [[2D fracture network generation with power-law lengths]]
- [[exponential curve fitting for threshold coefficients]]
- [[comparison of measured vs. predicted percolation status]]

## Connections To Other Work
- The fractal nature of fracture spatial distributions and earthquake hypocenters has been documented by many (e.g., Kagan & Knopoff 1980; Hirata & Imoto 1991) [Nakaya 2003, pp. 1-1].
- Power‑law fault length distributions are linked to the Gutenberg‑Richter relation and fault area–magnitude scaling (e.g., Sato 1979; Turcotte 1997) [Nakaya 2003, pp. 1-4; pp. 10-12].
- Bour & Davy (1997) provided a percolation threshold in terms of fracture density for random fault networks; the present study extends this by incorporating fractal parameters D, a, lmax/L and shows that density alone is insufficient [Nakaya 2003, pp. 8-10].
- Fracture maps from Odling & Webman (1991) used as sample 4 and as reference [Nakaya 2003, pp. 1-4; pp. 4-6; pp. 12-12].
- Active fault traces from Research Group for Active Faults in Japan (1991) used for samples 5–7 [Nakaya 2003, pp. 4-6; pp. 12-12].
- Wilson (2001) noted range‑limited fractality and scale transitions, influencing the handling of log‑log plots in the present work [Nakaya 2003, pp. 4-6].
- The relationship between b‑value and fractal dimension (e.g., Hirata 1989a) underpins the seismological application [Nakaya 2003, pp. 10-12].
- Fluid migration and seismicity interaction discussed in context of Byerlee (1993), Miller et al. (1996), Yamashita (1997) and field examples (Matsushiro swarm, Kobe earthquake) [Nakaya 2003, pp. 10-12].

## Open Questions
- The relationship between two‑dimensional fractal parameters (from outcrop or scanline sampling) and three‑dimensional fracture networks remains to be quantified [Nakaya 2003, pp. 11-12].
- Application of the binary fractal percolation condition to real seismic catalogs requires measurement of three‑dimensional fractal parameters and their temporal evolution [Nakaya 2003, pp. 11-12].
- Whether temporally varying fractal parameters can track fluid migration and seismicity in hydraulic fracturing or natural systems is an open question [Nakaya 2003, pp. 11-12].
- The effect of more complex orientation distributions, fracture interaction, and finite thickness of faults on the percolation threshold has not been explored [Nakaya 2003, pp. 6-7; pp. 11-12].
- The validity of eq. 3 for D ≥ 2 or a outside (1,3] has not been tested [Nakaya 2003, pp. 8-9].

## Source Coverage
All non‑empty indexed fragments were processed.  
- Indexed texts: 10  
- Nonempty source blocks: 10  
- Compiled source blocks: 10  
- Compiled source characters: 48,351  
- Coverage ratio by blocks: 1.0  
- Coverage ratio by characters: 1.004633  
- Source signature: `15f2b321ce6800cc36a44478994bf993f452f32d`  
- Compilation strategy: single‑pass‑markdown
