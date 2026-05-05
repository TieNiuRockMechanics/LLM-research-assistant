---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2012-radilla-interpreting-tracer-tests-in-the-enhanced-geothermal-system-egs-of-soultz-sous-for"
title: "Interpreting Tracer Tests in the Enhanced Geothermal System (EGS) of Soultz-sous-Forêts Using the Equivalent Stratified Medium Approach."
status: "draft"
source_pdf: "data/papers/Interpreting tracer tests in the enhanced geothermal system (EGS) of Soultz-sous-Forets using the equivalent stratified medium approach.pdf"
collections:
citation: "Radilla, Giovanni, et al. \"Interpreting Tracer Tests in the Enhanced Geothermal System (EGS) of Soultz-sous-Forêts Using the Equivalent Stratified Medium Approach.\" *Geothermics*, vol. 44, 2012, pp. 43–51. Accessed 2026."
indexed_texts: "11"
indexed_chars: "50559"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "50503"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.998892"
coverage_status: "full-index"
source_signature: "a82c000861c681cec5e8f0af73f2f4cf7371e9b9"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T01:02:22"
---

# Interpreting Tracer Tests in the Enhanced Geothermal System (EGS) of Soultz-sous-Forêts Using the Equivalent Stratified Medium Approach.

## One-line Summary

A new interpretation of 2005 tracer tests at the Soultz-sous-Forêts EGS site models three fluid circulation loops as equivalent stratified porous media with log-normal permeability distributions, achieving accurate fits of breakthrough curves at both production wells and linking loop characteristics to a known major fault structure.

## Research Question

How can the tracer test breakthrough curves from the 2005 circulation experiment between injection well GPK3 and production wells GPK2 and GPK4 at Soultz-sous-Forêts be simultaneously modeled, and how do the resulting circulation loop parameters relate to the known 3D fracture network of the granitic reservoir? [Radilla 2012, pp. 1-1]

## Study Area / Data

The study focuses on the Enhanced Geothermal System (EGS) site at Soultz-sous-Forêts, located in the Upper Rhine Graben, France. The site consists of three deep boreholes: GPK2 (5093 m), GPK3 (5111 m), and GPK4 (5270 m), along with GPK1 (3600 m) and reference hole EPS1 (fully cored to 2230 m). [Radilla 2012, pp. 1-1]

Data sources include:
- Tracer test data from the 2005 circulation experiment using 150 kg of 82.5% pure fluorescein, with injection into GPK3 and production from GPK2 and GPK4 over approximately 140 days (July–December 2005). [Radilla 2012, pp. 4-6]
- Injection rate of ~15 l/s (11.9 l/s from GPK2, 3.1 l/s from GPK4), with ~209,000 m³ injected into GPK3, 165,500 m³ discharged from GPK2, and 40,500 m³ from GPK4. [Radilla 2012, pp. 4-6]
- A 3D model of the Soultz fractured reservoir defining 53 structures (39 fracture zones, 8 microseismic structures, 6 VSP-derived structures) between 800 and 6000 m TVDSS, built from well logs, microseismicity recordings, and VSP data. [Radilla 2012, pp. 1-3]
- 1878 open fractures identified on UBI (Ultrasonic Borehole Imager) logs from GPK2, GPK3, and GPK4. [Radilla 2012, pp. 3-3]
- Wellhead pressure recordings: average 40 bar for GPK3, 8 bar for both GPK2 and GPK4. [Radilla 2012, pp. 7-8]

## Methods

**Equivalent Stratified Medium Approach:** Each circulation loop is modeled as a separate heterogeneous porous medium replaced by a stratified medium of uniform porosity with a log-normal permeability distribution. The model is controlled by a single parameter, the stratification factor H = σ_K / K̄, where σ_K is the standard deviation and K̄ is the mean permeability. [Radilla 2012, pp. 6-7]

For a concentration step (Heaviside function), the dimensionless concentration C at distance x and time t is given by:

C = (1/2) erfc( ln((x/Ut)√(1+H²)) / √(2 ln(1+H²)) )

where U = Q/(Aφ) is the mean velocity of the tracer front. [Radilla 2012, pp. 6-7]

**Tracer Injection Modeling:** Since the tracer was injected as a one-day concentration slug, the model uses superposition of a positive concentration step at t=0 and a negative concentration step at t=1 day to produce the breakthrough curve for each loop. [Radilla 2012, pp. 6-7]

**Three Circulation Loops:** Loops 1 and 2 connect GPK3 to GPK2 (explaining early arrival and tailing respectively), and loop 3 connects GPK3 to GPK4. The measured concentrations are related to loop concentrations via dilution ratios accounting for external fluid from the rock formation. [Radilla 2012, pp. 6-7]

**Fracture Analysis Methods:**
- Box counting method (1D equivalent of 2D method by Velde et al., 1990, 1991) for fracture spacing and fractal dimension analysis. [Radilla 2012, pp. 3-3]
- Power law analysis of fracture width distributions following Bonnet et al. (2001). [Radilla 2012, pp. 3-3]
- Fracture equivalent conductivity estimation using the Snow (1969)/Oda (1986) model with Poiseuille flow assumption. [Radilla 2012, pp. 3-3]

**Permeability Calculation:** Darcy's law was applied using wellhead pressure data, flow rates, and well casing specifications to calculate pressure gradients and mean permeability-to-porosity ratios (K̄/φ) for each loop. [Radilla 2012, pp. 7-8]

## Key Findings

1. **Accurate simultaneous fit:** The equivalent stratified medium model achieved a very accurate fit of the fluorescein concentration curves for both production wells GPK2 and GPK4, unlike previous attempts that could not simultaneously fit both wells. [Radilla 2012, pp. 6-7]

2. **Three circulation loop parameters:** Mean arrival times were 13.9 days (loop 1), 60.2 days (loop 2), and 188.2 days (loop 3). Stratification factors were H=0.56 (loop 1), H=0.94 (loop 2), and H=0.72 (loop 3), indicating loop 2 is the most heterogeneous and loop 1 the least heterogeneous. [Radilla 2012, pp. 6-7]

3. **Dilution ratios:** Dilution ratios (Qi/QGPK) were 0.08 (loop 1), 0.18 (loop 2), and 0.06 (loop 3), showing that geothermal fluid from the rock formation dominates the discharged fluids. [Radilla 2012, pp. 6-7]

4. **Cumulative tracer recovery:** Total asymptotic cumulative tracer recovery was 21.65% (loop 1: 6.33%, loop 2: 14.07%, loop 3: 1.25%), consistent with Sanjuan et al. (2006)'s value of 25.3% but with different loop contributions. [Radilla 2012, pp. 7-8]

5. **Loop characteristics:** Loop 1 appears very permeable and narrow (mean permeability ~2 Da for φ=0.05, fluid volume ~1100 m³), while loops 2 and 3 are less permeable and wider (loop 2: ~1.1 Da, ~10,900 m³; loop 3: ~0.35 Da, ~3000 m³). [Radilla 2012, pp. 8-8]

6. **Fault connection:** A well-known major fault in the Soultz Graben intersects GPK3 at 4775 m MD and corresponds to a casing leak in GPK2 at 3900 m MD, but does not intersect GPK4's bottom hole. This fault could explain the rapid tracer circulation in loop 1. [Radilla 2012, pp. 1-3]

7. **Fracture clustering:** Fractal dimension D=1.6 for both GPK3 and GPK4 indicates clustered fracture organization around main fault corridors. [Radilla 2012, pp. 3-3]

8. **Power law decay slope:** The GPK2 concentration decay slope of -0.9256 in log-log coordinates rules out matrix diffusion as the dominant tailing mechanism. [Radilla 2012, pp. 4-6]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| Mean arrival times: loop 1 = 13.9 d, loop 2 = 60.2 d, loop 3 = 188.2 d | [Radilla 2012, pp. 6-7] | Equivalent stratified medium model with log-normal permeability | Confirms permeability differences between loops |
| Stratification factors: H₁=0.56, H₂=0.94, H₃=0.72 | [Radilla 2012, pp. 6-7] | Same model | Loop 2 most heterogeneous, loop 1 least |
| Dilution ratios: 0.08, 0.18, 0.06 for loops 1, 2, 3 | [Radilla 2012, pp. 6-7] | Same model | External fluid dominates production |
| Total cumulative tracer recovery = 21.65% | [Radilla 2012, pp. 7-8] | Sum of three loop recoveries | Consistent with Sanjuan et al. (2006) value of 25.3% |
| Loop 1 mean permeability ~2 Da (φ=0.05), volume ~1100 m³ | [Radilla 2012, pp. 8-8] | Assumed loop length 600 m, φ=0.05 | Very permeable and narrow |
| Loop 2 mean permeability ~1.1 Da (φ=0.05), volume ~10,900 m³ | [Radilla 2012, pp. 8-8] | Same assumptions | Less permeable, wider |
| Fractal dimension D = 1.6 for GPK3 and GPK4 | [Radilla 2012, pp. 3-3] | Box counting method on UBI fracture data | Indicates clustered fracture organization |
| Major fault intersects GPK3 at 4775 m MD, casing leak in GPK2 at 3900 m MD | [Radilla 2012, pp. 1-3] | 3D structural model | Does not intersect GPK4 bottom hole |
| GPK2 concentration decay slope = -0.9256 | [Radilla 2012, pp. 4-6] | Log-log plot of dimensionless concentration | Rules out matrix diffusion |
| Mean fracture conductivities: GPK2 = 5.38×10³ m/s, GPK3 = 6.22×10⁵ m/s, GPK4 = 1.55×10¹ m/s | [Radilla 2012, pp. 3-4] | Snow/Oda model with Poiseuille assumption | Relative values only; large standard deviations |
| Variation coefficients Cv: GPK3=29, GPK2=5, GPK4=4564 | [Radilla 2012, pp. 3-4] | Same conductivity data | GPK4 has highest dispersion |

## Limitations

- The model does not account for diffusion processes; dispersion is attributed solely to permeability heterogeneity. [Radilla 2012, pp. 6-7]
- Porosity values for the fracture network between wells are unknown; calculations were performed for two assumed values (φ=0.05 and φ=0.02). [Radilla 2012, pp. 7-8]
- Experimental measurements for GPK4 appear to have been interrupted shortly before the concentration peak arrival, making predictions beyond 150 days highly speculative. [Radilla 2012, pp. 6-7]
- Fracture conductivity calculations are relative values based on geometric parameters and are not physically significant in terms of quantitative realistic flows. [Radilla 2012, pp. 3-4]
- GPK2 was not tested for fractal dimension due to lack of fracture data. [Radilla 2012, pp. 3-3]
- Drawing conclusions based on model predictions for times beyond 150 days remains highly speculative. [Radilla 2012, pp. 6-7]

## Assumptions / Conditions

- Each circulation loop is treated as an equivalent stratified porous medium with uniform porosity and log-normal permeability distribution. [Radilla 2012, pp. 6-7]
- The distance between injection and production wells at open hole level is approximately 600 m, and the equivalent porous media for the loops are assumed to be 600 m long. [Radilla 2012, pp. 7-8]
- Poiseuille flow is assumed within individual fractures for conductivity estimation. [Radilla 2012, pp. 3-3]
- A global and homogeneous pressure gradient is assumed in the reservoir for conductivity calculations. [Radilla 2012, pp. 3-3]
- Rock matrix is not assumed to be impermeable (relaxing the assumption from Gentier et al., 2010). [Radilla 2012, pp. 1-3]
- The tracer was injected at a constant flow rate during one day (concentration slug). [Radilla 2012, pp. 6-7]

## Key Variables / Parameters

- **H (stratification factor):** Standard deviation to mean permeability ratio (σ_K / K̄), quantifying heterogeneity of each loop. [Radilla 2012, pp. 6-7]
- **U (mean velocity):** Mean tracer front velocity in the equivalent porous medium, U = Q/(Aφ). [Radilla 2012, pp. 6-7]
- **K̄ (mean permeability):** Mean permeability of each circulation loop treated as equivalent porous medium. [Radilla 2012, pp. 7-8]
- **σ_K (permeability standard deviation):** Standard deviation of the log-normal permeability distribution. [Radilla 2012, pp. 7-8]
- **Qi (loop flow rate):** Volumetric flow rate circulating in each loop. [Radilla 2012, pp. 6-7]
- **Qe (external flow rate):** Flow rate of external fluid from the rock formation at zero tracer concentration. [Radilla 2012, pp. 6-7]
- **D (fractal dimension):** Derived from power law exponent of fracture spacing distribution; D = a + 1. [Radilla 2012, pp. 3-3]
- **κ_i (fracture equivalent conductivity):** Estimated from fracture width and spacing using κ_i = (g/12ν)(W³_i/S_i). [Radilla 2012, pp. 3-3]
- **Cv (variation coefficient):** Ratio of standard deviation to mean of fracture conductivities along well paths. [Radilla 2012, pp. 3-4]
- **CTR (cumulative tracer recovery):** Asymptotic cumulative tracer recovery as percentage of total injected mass. [Radilla 2012, pp. 7-8]

## Reusable Claims

- The equivalent stratified medium approach with log-normal permeability distribution can simultaneously model tracer breakthrough curves at multiple production wells in fractured geothermal reservoirs, where discrete fracture network models with impermeable matrix fail. [Radilla 2012, pp. 6-7] — Valid when treating circulation loops as equivalent porous media; limited to cases where matrix diffusion is not the dominant transport mechanism.

- A stratification factor H < 1 indicates relatively homogeneous flow paths, while H approaching 1 indicates strong heterogeneity; at Soultz, loop 1 (H=0.56) is the least heterogeneous and loop 2 (H=0.94) is the most heterogeneous. [Radilla 2012, pp. 6-7] — Valid for log-normal permeability distributions in equivalent stratified media.

- The fractal dimension D=1.6 for fracture spacing in the Soultz granite indicates clustered fracture organization around main fault corridors, consistent with known damage zone architecture. [Radilla 2012, pp. 3-3] — Valid for the Soultz reservoir; the power law exponent of 1.6 also appears in the fracture width distribution.

- A major fault intersecting GPK3 at 4775 m MD and GPK2 via a casing leak at 3900 m MD, but missing GPK4's bottom hole, provides a structural explanation for the fast, narrow, high-permeability loop 1 and the absence of direct short-circuiting to GPK4. [Radilla 2012, pp. 8-8] — Valid within the 3D structural model of Sausse et al. (2010).

- The power law decay slope of -0.9256 for GPK2 concentration in log-log coordinates rules out matrix diffusion as the dominant tailing mechanism, which would typically produce a slope of -3/2. [Radilla 2012, pp. 4-6] — Valid as a diagnostic; however, slopes different from -3/2 can also occur with matrix diffusion in some cases.

## Candidate Concepts

- [[Enhanced Geothermal System (EGS)]]
- [[Equivalent stratified porous medium]]
- [[Discrete fracture network]]
- [[Tracer test]]
- [[Breakthrough curve]]
- [[Stratification factor]]
- [[Log-normal permeability distribution]]
- [[Fracture connectivity]]
- [[Circulation loop]]
- [[Damage zone]]
- [[Fractal dimension of fractures]]
- [[Matrix diffusion]]
- [[Fracture conductivity]]
- [[Upper Rhine Graben]]

## Candidate Methods

- [[Equivalent stratified medium approach]]
- [[Box counting method for fracture spacing]]
- [[Power law analysis of fracture distributions]]
- [[Snow-Oda fracture conductivity model]]
- [[Tracer breakthrough curve modeling]]
- [[Darcy's law for loop permeability estimation]]
- [[Superposition of concentration steps for slug injection]]
- [[Particle tracking on discrete fracture network]]

## Connections To Other Work

- Sanjuan et al. (2006) performed the original tracer test analysis using a dispersive transfer model and proposed the three-loop conceptual model. The present work reinterprets their data with a different modeling approach. [Radilla 2012, pp. 1-1]
- Gentier et al. (2010) attempted to model the same breakthrough curves using particle tracking on a discrete fracture network with impermeable rock matrix, fitting GPK2 but failing to simultaneously fit GPK4. [Radilla 2012, pp. 1-1]
- Sausse et al. (2010) built the 3D structural model of the Soultz fractured reservoir used for comparison with the tracer test model. [Radilla 2012, pp. 1-3]
- Fourar (2006) and Fourar and Radilla (2009) developed the equivalent stratified medium approach applied in this study. [Radilla 2012, pp. 6-7]
- Nowamooz (2010) proved the approach suitable for modeling tracer transport in laboratory-scale real rough fractures. [Radilla 2012, pp. 6-7]
- Becker and Shapiro (2000) discussed factors causing long tracer concentration tailing in breakthrough curves. [Radilla 2012, pp. 4-6]
- The study references the work of Tsang (1995), Meigs et al. (1996), Haggerty and Gorelick (1995), and Haggerty et al. (2000) on matrix diffusion and power law tailing behavior. [Radilla 2012, pp. 4-6]

## Open Questions

- Can the equivalent stratified medium approach be validated with longer-duration tracer tests that capture the GPK4 concentration peak?
- How sensitive are the calculated loop permeabilities to the assumed porosity values, and can independent porosity measurements constrain these estimates?
- Does the model remain valid for other tracer types (e.g., naphthalene sulfonate tracers also analyzed in the 2005 tests)?
- How do the three circulation loops evolve over time with continued geothermal operation?
- Can the approach be extended to account for matrix diffusion effects in addition to permeability heterogeneity?

## Source Coverage

All 11 non-empty indexed fragments were processed. The compiled source blocks total 11 out of 11, with 50,503 characters compiled from 50,559 indexed characters. Coverage ratio by blocks: 1.0. Coverage ratio by characters: 0.9989. Coverage status: full-index.
