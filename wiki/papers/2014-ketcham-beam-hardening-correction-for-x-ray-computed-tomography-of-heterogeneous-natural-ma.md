---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2014-ketcham-beam-hardening-correction-for-x-ray-computed-tomography-of-heterogeneous-natural-ma"
title: "Beam Hardening Correction for X-ray Computed Tomography of Heterogeneous Natural Materials."
status: "draft"
source_pdf: "data/papers/2014 - Beam hardening correction for X-ray computed tomography of heterogeneous natural materials.pdf"
collections:
citation: "Ketcham, Richard A., and Romy D. Hanna. “Beam Hardening Correction for X-ray Computed Tomography of Heterogeneous Natural Materials.” *Computers & Geosciences*, vol. 67, 2014, pp. 49-61. doi:10.1016/j.cageo.2014.03.003. Accessed 2026."
indexed_texts: "12"
indexed_chars: "59848"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "60140"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004879"
coverage_status: "full-index"
source_signature: "db8cfb672af128b9652d2cde167ff02df3364f11"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T15:17:29"
---

# Beam Hardening Correction for X-ray Computed Tomography of Heterogeneous Natural Materials.

## One-line Summary
We present a new empirical method for correcting beam-hardening artifacts in polychromatic X-ray CT data using an expert‑guided iterative optimization of a cubic‑spline‑interpolated linearization function, which can be applied to heterogeneous natural materials without prior calibration. [Ketcham 2014, pp. 1-2, 3‑4]

## Research Question
How can beam‑hardening artifacts be effectively reduced in X‑ray CT of complex, heterogeneous natural specimens when traditional calibration‑based techniques (e.g., phantom‑based polynomial corrections, dual‑energy scanning) are impractical because the materials are not well known or characterized? [Ketcham 2014, pp. 1-3]

## Study Area / Data
CT data were collected from a diverse set of geological and biological specimens:
- a calcite cleavage rhomb (Harding pegmatite, New Mexico) [Ketcham 2014, pp. 5]
- an apatite crystal (Durango, Mexico) [Ketcham 2014, pp. 5-8]
- a small copper cube (9.5 mm) [Ketcham 2014, pp. 8-9]
- a leopard seal (*Hydrurga leptonyx*) skull and mandible [Ketcham 2014, pp. 9-10]
- a fossil mosasaur (*Tethysaurus*) brain case [Ketcham 2014, pp. 10]
- a 10‑cm asphalt concrete core containing multiple rock‑type aggregates [Ketcham 2014, pp. 10-11]

All scanning was performed on the ACTIS scanner at the University of Texas High‑Resolution X‑ray CT Facility, using its microfocal subsystem (225 kV Feinfocus source, image intensifier detector) or high‑energy subsystem (450 kV Comet source, 512‑channel linear detector array). Both sources employ tungsten targets and aluminum windows, producing continuous bremsstrahlung spectra from the tube potential down to ~30 keV, with characteristic tungsten lines at 60–70 keV. Tube potentials ranged from 180 kV to 450 kV; some scans used additional pre‑filtration (e.g., 1.6 mm brass) to harden the beam. [Ketcham 2014, pp. 5, 5‑8]

## Methods
1. **Expert ROI definition**: In a reconstructed CT image, an expert user draws Regions of Interest (ROIs) – rectangles, ellipses, or threshold‑derived contours (optionally eroded) – that capture manifestations of beam hardening while avoiding other artifacts (ring artifacts, EEGE streaks). [Ketcham 2014, pp. 3-4]

2. **Merit function**: Relative CT‑number variation (standard deviation/mean) is computed within ROIs. Four combination strategies exist:
   - *Selected* – a single ROI.
   - *Independent* – sum of per‑ROI variations.
   - *One Material* – variation pooled across multiple ROIs sampling the same material.
   - *Two Materials* – variation minimized across two groups of ROIs representing two distinct materials (e.g., solid and air). [Ketcham 2014, pp. 3-4]

3. **Linearization function**: A monotonically increasing cubic spline with *n* (3–20) evenly spaced nodes along the polychromatic ray‑sum axis *p* = ‑ln(I/I₀). Endpoints are fixed (*m₁*=*p₁*, *mₙ*=*pₙ*). The interior nodes are adjusted via factors *cⱼ* that control fractional increments of rise, ensuring a positive first derivative and, optionally, a positive second derivative (concave‑up). The search region is bounded by the 1:1 line (no correction) and a lower “maximum‑severity” bound from prior manual corrections. [Ketcham 2014, pp. 3-4, 4‑5]

4. **Optimization**: The node positions are iterated using an adapted simplex method constrained within bounds. Each trial transform is applied to the sinogram, a filtered backprojection is performed (often at ½, ¼, or ⅛ resolution to save time), the resulting CT image is re‑normalized so that the mean CT number in each ROI matches the original, and the merit function is evaluated. Convergence typically requires tens to a few hundred reconstructions. [Ketcham 2014, pp. 4-5]

5. **User iteration**: The corrected image is inspected; ROIs can be adjusted to suppress secondary artifacts, and the correction re‑run until satisfactory. The final spline is then applied to reconstruct the full 3D dataset. [Ketcham 2014, pp. 3-4, 11‑13]

6. **Implementation**: Code is written in IDL with an external C program for backprojection specific to the ACTIS scanner, but the approach is general and can be adapted to any CT system whose reconstruction engine can be invoked from a command‑line or text‑file interface. [Ketcham 2014, pp. 4-5]

## Key Findings
- The optimized linearization curves show substantial diversity: some are purely concave‑up, others exhibit negative second derivative (downward curvature) at low ray sums. Such negative curvature is not predicted by beam‑hardening physics alone and is attributed to partial cancellation of beam hardening by the exponential edge gradient effect (EEGE) in samples with flat edges or corners. [Ketcham 2014, pp. 5, 8‑9, 11]
- For a copper cube, a correction based solely on a solid‑interior ROI gave uniform CT numbers within the metal but left air streaks and rounded edges upon thresholding. A two‑material correction (solid + air) worsened interior uniformity but produced sharp corners and straight edges in the thresholded image. Hence, the optimal correction depends on the user’s objective (density fidelity vs. dimensional metrology). [Ketcham 2014, pp. 8-9]
- In complex natural specimens (leopard seal skull, mosasaur braincase), using air‑only ROIs effectively removed beam hardening in the solid as well, flattening air CT numbers and revealing features such as: correct bone‑to‑tooth contrast (teeth brighter than bone), more uniform mandibular bone density, and previously obscured pore‑filling mineralization. [Ketcham 2014, pp. 9-10, 10]
- The method outperformed manual 2nd‑ or 3rd‑degree polynomial corrections in all test cases, producing more uniform material CT numbers and better artifact suppression. [Ketcham 2014, pp. 5, 8, 9]
- For a highly heterogeneous asphalt‑concrete core, selecting two clasts of the same rock type (based on texture rather than CT number) successfully corrected beam hardening across all aggregate types. [Ketcham 2014, pp. 10-11]
- Linearization always amplifies image noise because the slope of the transform is >1 at high ray sums, spreading the noisiest data over a wider range. [Ketcham 2014, pp. 4-5]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Optimal linearization curves can have negative second derivative (downward curvature) at low ray sums | [Ketcham 2014, pp. 5, 8‑9, 11] | Specimens with flat edges or sharp corners where EEGE partially cancels beam hardening | Explains variation from purely concave‑up shapes expected from beam hardening |
| Air‑ROI‑based merit function can correct beam hardening in the solid for complex natural objects | [Ketcham 2014, pp. 9-10, 10] | When air streaks are dominated by beam hardening and not by other artifacts (EEGE, scattering) | Demonstrated with leopard seal skull and mosasaur braincase; potential over‑correction risk not observed |
| Two‑material (solid+air) correction improves geometric accuracy of threshold‑based solid models at the expense of interior density fidelity | [Ketcham 2014, pp. 8-9] | High‑atomic‑number metal (Cu) cube, 180 kV, filtered beam | Trade‑off analogous to Dewulf et al. (2012) observation that beam‑hardening correction can harm dimensional measurements |
| Spline‑interpolated linearization outperforms low‑degree polynomial corrections for high‑attenuation materials | [Ketcham 2014, pp. 5, 8, 9] | Calcite, apatite, copper samples; comparison with best manually selected 2nd/3rd‑degree polynomials | Supports Hammersberg & Mångård (1998) need for ≥8th degree for industrial materials |
| Method can correct highly heterogeneous multi‑material samples without segmentation | [Ketcham 2014, pp. 10-11] | Asphalt concrete core; ROIs placed on two clasts identified by texture | Resulting single linearization function improved uniformity for all aggregate types |
| Beam‑hardening correction can reveal subtle natural zoning previously obscured by artifacts | [Ketcham 2014, pp. 5-8] | Apatite crystal; large solid ROI after erosion | Second high‑attenuation zone appeared as a distinct compositional rim |
| Linearization increases image noise because transform slope >1 at high ray sums | [Ketcham 2014, pp. 4-5] | Applies to any linearization method | Noise amplification can be mitigated by filtering low‑signal regions (as done for Cu two‑material case) |

## Limitations
- The method relies on an expert user to define ROIs; inexperienced placement can lead to over‑correction or secondary artifacts (e.g., jiggle among spline nodes causing harmful undulations). [Ketcham 2014, pp. 11-13, 3‑4]
- It does not correct non‑beam‑hardening artifacts such as ring artifacts, scattering, or EEGE streaks; these can persist or be amplified, potentially contaminating the correction if not excluded from ROIs. [Ketcham 2014, pp. 3, 8‑9, 11]
- Requires a reconstruction engine accessible from a command‑line interface; proprietary systems that do not expose such an interface cannot directly use the present implementation. [Ketcham 2014, pp. 5]
- For samples that fill the field of view (few low ray‑sum values), the correction function may exhibit a sharp offset near the minimum ray sum, potentially introducing a thin rind artifact. [Ketcham 2014, pp. 10-11]
- The “optimal” correction is non‑unique: different merit functions yield different linearization curves, and the choice depends on the user’s specific objective (e.g., density homogeneity vs. geometric accuracy). [Ketcham 2014, pp. 8-9]
- Noise amplification at high ray sums is inevitable because the slope of the linearization curve must exceed 1; for severe corrections this may require post‑correction filtering. [Ketcham 2014, pp. 4-5, 8‑9]

## Assumptions / Conditions
- The primary artifact to be corrected is polychromatic beam hardening; other artifacts can be sufficiently separated by expert ROI placement. [Ketcham 2014, pp. 3-4, 11]
- Fixing the endpoints of the linearization function to the data extremes does not impair the ability to find an optimal solution. [Ketcham 2014, pp. 3-4]
- The relative standard deviation within a ROI appropriately quantifies beam‑hardening severity, assuming that the material inside the ROI is intrinsically uniform. [Ketcham 2014, pp. 3-4]
- Using a single linearization curve is sufficient; the approach does not try to separate the contributions of multiple materials (in contrast to segmentation‑based methods). [Ketcham 2014, pp. 3-4, 11]
- The X‑ray source spectrum is not known or used; the correction is purely empirical. [Ketcham 2014, pp. 3]
- When air ROIs are employed for solid correction, it is assumed that the air variations are dominated by beam hardening, not by EEGE or scattering. [Ketcham 2014, pp. 9-10]

## Key Variables / Parameters
- Number of spline nodes (*n*, typically 3–20) [Ketcham 2014, pp. 4-5]
- Constraint on second derivative (positive vs. free) [Ketcham 2014, pp. 4-5]
- Merit function combination mode (Selected, Independent, One Material, Two Materials) [Ketcham 2014, pp. 3-4]
- ROI geometry (box, ellipse, thresholded contour + erosion margin) [Ketcham 2014, pp. 3-4]
- Resolution reduction factor for optimization (2, 4, 8) [Ketcham 2014, pp. 4-5]
- Re‑normalization method (exact ROI‑mean matching for ≤2 materials, linear best‑fit for ≥3 independent ROIs) [Ketcham 2014, pp. 4-5]
- Lower bound for the transform (the “maximum‑severity” curve) [Ketcham 2014, pp. 3-4]

## Reusable Claims
1. **Claim**: A spline‑interpolated linearization function, optimized using CT‑number variation in expert‑defined ROIs, can reduce beam‑hardening artifacts in heterogeneous natural materials without prior calibration.  
   *Condition*: The user can identify ROIs that are dominated by beam hardening and free of other artifacts.  
   *Limitation*: May introduce over‑correction or secondary artifacts if interactions with EEGE are not accounted for; requires user iteration and expertise. [Ketcham 2014, pp. 3-4, 5, 11‑13]

2. **Claim**: Beam‑hardening artifacts manifested in surrounding air (dark/light streaks) can be used to correct the solid phase, provided those air variations are primarily caused by beam hardening.  
   *Condition*: Air ROIs are placed on streaks that result from long polychromatic ray paths through the solid; other streak sources (EEGE) are minimal.  
   *Limitation*: Potential over‑correction of the solid (bright centers, dark rims) if air streaks have a significant non‑beam‑hardening component; best when air artifacts are visually dominated by beam hardening. [Ketcham 2014, pp. 9-10, 10]

3. **Claim**: For high‑attenuation materials with sharp edges, a merit function that includes both solid and air ROIs yields better geometric fidelity (straight edges, sharp corners) in thresholded images than a solid‑only correction.  
   *Condition*: High atomic number/density material (e.g., copper); the scan objective is dimensional metrology rather than internal density accuracy.  
   *Limitation*: The interior CT numbers become less representative of true attenuation; noise is amplified at high ray sums, requiring post‑reconstruction filtering. [Ketcham 2014, pp. 8-9]

4. **Claim**: Low‑degree (2nd, 3rd) polynomial linearization is frequently insufficient for geological and industrial materials; spline‑based optimization can capture the necessary complexity.  
   *Condition*: Materials with moderate to high effective atomic number and density (e.g., calcite, apatite, copper).  
   *Limitation*: The optimal spline function is sample‑specific and not transferable between scan configurations without re‑optimization. [Ketcham 2014, pp. 3, 5, 8]

5. **Claim**: The “best” beam‑hardening correction is task‑dependent; no single linearization function yields simultaneous optimality for both density uniformity and geometric accuracy.  
   *Condition*: When the specimen contains multiple materials or when EEGE is present.  
   *Limitation*: The user must explicitly decide the objective before selecting ROIs and merit function strategy. [Ketcham 2014, pp. 8-9]

## Candidate Concepts
- [[beam hardening]]
- [[linearization (CT)]]
- [[exponential edge gradient effect]]
- [[polychromatic X-ray CT]]
- [[merit function]]
- [[filtered backprojection]]
- [[cubic spline interpolation]]
- [[CT artifact]]
- [[ring artifact]]
- [[streak artifact]]
- [[CT number normalization]]
- [[sinogram]]
- [[monoenergetic attenuation]]

## Candidate Methods
- [[spline-interpolated beam hardening correction]]
- [[iterative optimization of linearization function]]
- [[ROI-based merit function for CT artifact quantification]]
- [[adapted simplex method for CT correction]]
- [[expert-guided empirical beam hardening correction]]
- [[air-based beam hardening correction]]
- [[two-material beam hardening correction]]
- [[low-resolution surrogate reconstruction for optimization]]

## Connections To Other Work
- The linearization concept was introduced by Herman (1979) using 2nd‑ or 3rd‑degree polynomials for low‑density biological tissue; Hammersberg & Mångård (1998) showed that at least 8th‑degree polynomials are required for industrial materials such as aluminum and steel. [Ketcham 2014, pp. 3]
- The “wedge” calibration technique (packing specimen in attenuating powder) was demonstrated by Ketcham & Carlson (2001) to virtually eliminate beam hardening, but at the cost of longer scan times and complications for 3D visualization. [Ketcham 2014, pp. 2]
- Dual‑energy scanning (Van Geet et al., 2000) and energy‑based modeling (Van de Casteele et al., 2002, 2004; De Man et al., 2001) attempt to separate photoelectric and Compton contributions but require calibration phantoms and simplify the X‑ray spectrum. [Ketcham 2014, pp. 3]
- Segmentation‑based iterative methods: Krumm et al. (2008) generate material‑specific linearization functions by segmenting the object and ray‑tracing through each material; Van Gompel et al. (2011) additionally estimate the X‑ray spectrum and material properties iteratively; Kyriakou et al. (2010) use forward projection of segmented data to create correction volumes. These methods assume a limited number of homogeneous materials and successful automated segmentation, which can be confounded by the complexity of natural geological specimens. [Ketcham 2014, pp. 3, 11]
- The exponential edge gradient effect (EEGE), described by Joseph & Spital (1981), causes negative streaking along straight edges; in this study, EEGE is invoked to explain the negative second derivative seen in many optimized linearization curves, as the EEGE partially cancels beam hardening along edge‑grazing paths. [Ketcham 2014, pp. 3-4, 11]
- Dewulf et al. (2012) cautioned that beam‑hardening correction can sometimes degrade dimensional accuracy; our two‑material vs. solid‑only correction for the copper cube confirms this trade‑off. [Ketcham 2014, pp. 8-9]

## Open Questions
- What is the systematic relationship between scan parameters (X‑ray spectrum, filtration, specimen geometry) and the shape of the empirically derived linearization curve? [Ketcham 2014, pp. 11]
- How does the presence of strong non‑beam‑hardening artifacts (scatter, rings) affect the convergence and robustness of the optimization, and can the method be extended to jointly estimate those artifacts? [Ketcham 2014, pp. 3, 11]
- Can the expert‑driven ROI selection be automated, e.g., by detecting streaks and bright/dark rims via image analysis, to make the method fully unsupervised? [Ketcham 2014, pp. 3-4]
- Under what conditions does the spline‑based approach offer significant improvement over well‑chosen high‑degree polynomial corrections, and are there simpler functional forms that would suffice for certain material classes? [Ketcham 2014, pp. 3, 8]
- Could the single‑linearization‑curve concept be combined with a segmentation step to provide material‑specific transforms while still avoiding rigorous calibration? [Ketcham 2014, pp. 3, 11]
- What is the best practice for ROI placement to avoid introducing secondary artifacts while maximizing correction efficacy across different sample types? [Ketcham 2014, pp. 11-13]

## Source Coverage
- All 12 non‑empty indexed text fragments from the source paper (Ketcham, R.A., Hanna, R.D., 2014. Beam hardening correction for X‑ray computed tomography of heterogeneous natural materials. Computers & Geosciences 67, 49–61) were processed.
- Total source characters indexed: 59,848; compiled source characters: 60,140.
- Coverage ratio by blocks: 1.0; coverage ratio by characters: 1.004879.
- Compile strategy: single‑pass‑markdown; coverage status: full‑index.
