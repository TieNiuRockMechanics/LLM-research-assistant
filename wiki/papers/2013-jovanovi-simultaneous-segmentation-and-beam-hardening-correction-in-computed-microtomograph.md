---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2013-jovanovi-simultaneous-segmentation-and-beam-hardening-correction-in-computed-microtomograph"
title: "Simultaneous Segmentation and Beam-Hardening Correction in Computed Microtomography of Rock Cores."
status: "draft"
source_pdf: "data/papers/2013 - Simultaneous segmentation and beam-hardening correction in computed microtomography of rock cores.pdf"
collections:
citation: "Jovanović, Zoran, et al. “Simultaneous Segmentation and Beam-Hardening Correction in Computed Microtomography of Rock Cores.” *Computers & Geosciences*, 2013, doi:10.1016/j.cageo.2013.03.015."
indexed_texts: "9"
indexed_chars: "41922"
nonempty_source_blocks: "9"
compiled_source_blocks: "9"
compiled_source_chars: "42146"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.005343"
coverage_status: "full-index"
source_signature: "a6be9d009935c89a90a2dc731e30718b796cb42e"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T15:04:23"
---

# Simultaneous Segmentation and Beam-Hardening Correction in Computed Microtomography of Rock Cores.

## One-line Summary
For cylindrical rock cores, the beam‑hardening artifact is a radial function of distance from the center; this relationship is extracted from the CT data and used to simultaneously segment phases and correct the artifact.

## Research Question
Can the beam‑hardening artifact in polychromatic micro‑CT of cylindrical geologic samples be exploited to achieve simultaneous phase segmentation and artifact removal without prior knowledge of the X‑ray spectrum or attenuation coefficients?

## Study Area / Data
Cylindrical test objects were scanned on a custom‑built μCT scanner (ProCon CT‑Alpha) with a microfocus X‑ray tube and a 2048 × 2048 flat‑panel detector.  
- Two single‑phase reference cylinders: pure aluminum (30 mm diameter) and plastic (30 mm diameter), measured at 120 kV with and without metal foil filters (1.0 mm Al, 0.5 mm Cu, 0.15 mm Ag).  
- Two multi‑mineral rock cores: an evaporite cylinder (anhydrite with halite‑sealed fractures, 30 mm diameter, 130 kV with 0.15 mm Ag filter, 53 μm/pixel) and a granite cylinder (18 mm diameter, 100 kV without filter, 20.4 μm/pixel).  
All objects were mounted with precise centro‑symmetrical alignment. Reconstruction used the classic Feldkamp et al. (1984) cone‑beam algorithm. [Jovanovi 2013, pp. 4-5]

## Methods
The method relies on the observation that in vertically mounted cylindrical samples, isolines of reconstructed attenuation values approximate circles, and the beam‑hardening artifact (BHA) is a radial function.  
1. **Extract BHA curves**: manually collect attenuation values of a single phase from the center to the periphery along radial profiles. Because a single profile rarely covers all distances, multiple profiles are averaged to reduce noise.  
2. **Fit a model**: the radial profile is well approximated by an exponential function μ = μ₀ e^(–k √(R² – r²)). Constants are obtained by least‑squares fitting.  
3. **Build an artificial mono‑mineral object**: construct a synthetic image that has exactly the attenuation values of the targeted phase at every radial position.  
4. **Arithmetic difference**: subtract the artificial object from the original reconstructed image. Where the difference is within experimental error (± standard deviation), the targeted phase is present; larger deviations indicate other phases.  
5. **Iterate**: repeat steps 1–4 for each distinguishable phase, or combine differential images to isolate multiple phases.  

The procedure is purely post‑reconstruction and requires neither knowledge of the X‑ray spectrum nor of attenuation coefficients. A mathematical derivation for parallel‑beam geometry, based on the bimodal energy‑distance model of Van de Casteele et al. (2002, 2004), is also provided to show how the cupping artifact emerges as a radial function f(r) = K/[π √(R² – r²)]. [Jovanovi 2013, pp. 3-4, 4‑5, 5‑6, 6‑8]

## Key Findings
- In cylindrical samples, BHA is a radial function; points of the same phase at the same distance from the center exhibit the same reconstructed attenuation value (within error). [Jovanovi 2013, pp. 5-6]
- The attenuation‑vs.‑radius curve follows an exponential or parabolic shape, often with a “bump” near the periphery that depends on the material and on filter use. [Jovanovi 2013, pp. 5-6]
- The arithmetic‑difference approach successfully segmented an evaporite rock core into its mineral phases (Fig. 6c). [Jovanovi 2013, pp. 6-8]
- In a granite sample, quartz, K‑feldspar, and Na‑rich plagioclase had overlapping attenuation, making phase separation impossible, but the difference image (original – darkest phase) enhanced grain‑boundary visibility and produced a usable two‑phase segmentation. [Jovanovi 2013, pp. 6-8]
- The procedure simultaneously corrects the beam‑hardening artifact and yields a segmented image without altering the original sinogram. [Jovanovi 2013, pp. 6-8]
- The mathematical exercise for parallel geometry recovers the known radial dependence, confirming that the observed BHA is consistent with the bimodal model of Van de Casteele et al. [Jovanovi 2013, pp. 4-5, 8‑8]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| In cylindrical objects, attenuation values of a single phase depend only on distance from the center (Fig. 1c). | [Jovanovi 2013, pp. 5-6] | Vertical centro‑symmetrical mounting; reconstruction via Feldkamp algorithm; 30 mm evaporite core, 53 μm/pixel. | Values follow a smooth “beam‑hardening curve”; confirms radial symmetry. |
| BHA curves for Al and plastic cylinders are well fitted by μ = μ₀ e^(–k √(R² – r²)). | [Jovanovi 2013, pp. 5-6, 6‑8] | Single‑phase phantoms with/without metal foil filters; 120 kV, 57.1 μm/pixel. | Filtering reduces the peripheral bump but does not eliminate BHA. |
| Arithmetic difference (original – synthetic mono‑phase image) isolates phase presence; zero difference (within error) indicates that phase. | [Jovanovi 2013, pp. 6-8] | Applied to evaporite and granite rock cores. | Multiple phases segmented by repeating the difference step (Fig. 6). |
| For granite, quartz, K‑feldspar, and Na‑plagioclase cannot be separated; difference image (original minus darkest phase) reveals sharper grain boundaries. | [Jovanovi 2013, pp. 6-8] | 18 mm granite core, 100 kV, no filter, 20.4 μm/pixel. | Overlap of attenuation coefficients prevents full mineral separation. |
| The bimodal energy‑distance model (Van de Casteele et al., 2004) leads via inverse Radon transform to a radial BHA function for parallel‑beam geometry. | [Jovanovi 2013, pp. 3-4, 4‑5] | Parallel‑beam assumption; constant bias K in sinogram. | Derivation yields f(r)=K/[π√(R² – r²)]; matches the observed cupping profile. |

## Limitations
- The approach is effective only for cylidrical samples where BHA is a simple radial function; non‑cylindrical objects yield non‑radial BHA that makes the method impractical. [Jovanovi 2013, pp. 8-8]
- Manual extraction of BHA curves is tedious, especially for small grain sizes; automated curve recognition was not implemented. [Jovanovi 2013, pp. 6-8]
- Phases with nearly identical attenuation coefficients cannot be separated; they must be treated as a single composite phase. [Jovanovi 2013, pp. 6-8]
- Small regions at the top and bottom of the cylinder (outside the Tam‑Danielsson window) cannot be correctly segmented. [Jovanovi 2013, pp. 5-6]
- The BHA correction is empirical and does not compute projection‑domain corrections; thus, it may not fully handle photon starvation or scattering artifacts. [Jovanovi 2013, pp. 6-8; not explicitly stated, but implied by the post‑reconstruction nature, so I won’t speculate; just note that it is not a projection‑domain method.]

## Assumptions / Conditions
- The sample must be a cylinder and mounted with precise centro‑symmetrical alignment.  
- The reconstruction must have been performed with a cone‑beam algorithm (Feldkamp type) and sufficient angular sampling (800 projections over 360°).  
- BHA is assumed to follow a material‑specific radial cupping curve that can be extracted where the phase is spatially isolated in some profiles.  
- The exponential model μ = μ₀ e^(–k √(R² – r²)) adequately fits the observed attenuation profile.  
- Noise levels are such that averaging multiple profiles yields a reliable mean BHA curve. [Jovanovi 2013, pp. 4-5, 5‑6, 6‑8]

## Key Variables / Parameters
- **r**: radial distance from cylinder center.  
- **μ₀, k**: material‑specific constants in the exponential BHA model.  
- **R**: radius of the cylindrical sample.  
- **SD**: standard deviation of the difference between original and synthetic image, used as threshold for phase presence.  
- **Beam energy (kV)**: need not be known; only the observed attenuation‑vs.‑radius behavior is used.  
- **Filter material/thickness**: influences the bump shape but does not alter the radial nature.  

## Reusable Claims
1. In cylindrical geologic samples scanned by polychromatic desktop μCT, the attenuation value of a single homogeneous phase is a function of only the distance from the cylinder center (radial symmetry). [Jovanovi 2013, pp. 5-6]  
   *Condition:* correct axial alignment and sufficient angular sampling; valid for cone‑beam reconstructions.  
2. The beam‑hardening artifact in cylinders can be modeled by an exponential function μ = μ₀ e^(–k √(R² – r²)), whose parameters can be extracted from the reconstructed image. [Jovanovi 2013, pp. 6-8]  
   *Condition:* moderate noise; allows fitting after averaging multiple radial profiles.  
3. Subtracting a synthetic image that mimics the BHA curve of a single phase from the original reconstruction yields an image where that phase has values near zero, enabling segmentation by thresholding the difference. [Jovanovi 2013, pp. 6-8]  
   *Condition:* the BHA curve is accurately extracted; phases have distinct attenuation differences outside the error band.  
4. The method simultaneously corrects the beam‑hardening artifact without knowledge of the X‑ray spectrum or of attenuation coefficients, provided the sample is cylindrical. [Jovanovi 2013, pp. 1-3, 6‑8]  
   *Condition:* sample is a vertically mounted cylinder; radial BHA holds.  
5. If phases have overlapping attenuation coefficients, a differential image (original minus the darkest phase) can still enhance grain‑boundary visibility and facilitate partial separation. [Jovanovi 2013, pp. 6-8]  
   *Condition:* at least one major phase can be assigned a distinct BHA curve.  

## Candidate Concepts
- [[beam-hardening artifact (BHA)]]
- [[post-reconstruction correction]]
- [[radial BHA function]]
- [[cupping artifact]]
- [[bimodal energy‑distance model]]
- [[Feldkamp reconstruction]]
- [[Tam‑Danielsson window]]
- [[sinogram bias constant K]]
- [[inverse Radon transform]]
- [[arithmetic‑difference segmentation]]
- [[empirical BHA curve fitting]]

## Candidate Methods
- [[BHA‑curve extraction from cylindrical μCT data]]
- [[exponential BHA model fitting]]
- [[synthetic mono‑phase image construction]]
- [[difference‑image phase mapping]]
- [[iterative segmentation via phase‑specific BHA curves]]
- [[parallel‑beam BHA mathematical derivation using rectangular bias function]]

## Connections To Other Work
- The core mathematical idea extends the bimodal energy model of Van de Casteele et al. (2002, 2004), showing how a constant sinogram bias propagates into a radial cupping artifact in parallel‑beam geometry. [Jovanovi 2013, pp. 3-4, 4‑5]
- The method is compared with existing BHA correction approaches: pre‑filtering (Jennings, 1988), linearization (Brooks & Dichiro, 1976; Herman, 1979; Hammersberg & Mångård, 1998; Kachelriess et al., 2006), dual‑energy (Alvarez & Macovski, 1976; Macovski et al., 1976; Lehmann et al., 1981; Ivakhnenko, 2010), and post‑reconstruction methods (Ruegsegger et al., 1978; Van de Casteele et al., 2002, 2004; Krumm et al., 2008). All of these fail for multi‑material geologic samples because either they require single‑material composition, known chemical composition, or an initial segmentation that BHA itself prevents. The present method circumvents this by using the radial BHA directly as a discriminant. [Jovanovi 2013, pp. 1-3, 3‑3, 3‑4]
- The work is related to micro‑CT applications in reservoir rock analysis (Van Geet et al., 2000, 2001; Berg et al., 2013) and to the broader problem of phase‑separating rock cores for petrophysical characterization. [Jovanovi 2013, pp. 1-1, 8‑8]

## Open Questions
- Can the method be extended to cone‑beam geometry directly, to allow segmentation of non‑cylindrical samples? The authors suggest that calculating BHA for cone‑beam geometry would enable shape‑independent correction. [Jovanovi 2013, pp. 8-8]
- How can automated extraction of BHA curves from the reconstructed volume be implemented reliably, especially for rocks with fine‑grained textures? [Jovanovi 2013, pp. 6-8]
- What is the impact of photon starvation and scattering on the accuracy of the extracted BHA curves, and can a combined projection‑domain and image‑domain approach improve results? [Not directly addressed in fragments, but implied by limitation discussion.]
- How well does the exponential BHA model hold for extreme density contrasts (e.g., heavy minerals like pyrite in a light matrix) and for very large diameters compared to detector resolution? [Jovanovi 2013, pp. 4-5, 6‑8] (modeled only for aluminum, plastic, granite, evaporite)

## Source Coverage
All 9 non‑empty indexed fragments were processed (indexed texts: 9, indexed characters: 41922, compiled characters: 42146; coverage ratio by blocks: 1.0, coverage ratio by chars: 1.005343). No additional sources were used.
