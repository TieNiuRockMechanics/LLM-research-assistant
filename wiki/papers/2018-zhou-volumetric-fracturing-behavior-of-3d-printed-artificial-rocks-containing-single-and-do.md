---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2018-zhou-volumetric-fracturing-behavior-of-3d-printed-artificial-rocks-containing-single-and-do"
title: "Volumetric Fracturing Behavior of 3D Printed Artificial Rocks Containing Single and Double 3D Internal Flaws under Static Uniaxial Compression."
status: "draft"
source_pdf: "data/papers/Volumetric fracturing behavior of 3D printed artificial rocks containing single and double 3D internal flaws under static uniaxial compression.pdf"
collections:
citation: "Zhou, T., et al. \"Volumetric Fracturing Behavior of 3D Printed Artificial Rocks Containing Single and Double 3D Internal Flaws under Static Uniaxial Compression.\" *Engineering Fracture Mechanics*, 2018, doi:10.1016/j.engfracmech.2018.11.030."
indexed_texts: "13"
indexed_chars: "64931"
nonempty_source_blocks: "13"
compiled_source_blocks: "13"
compiled_source_chars: "62471"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.962114"
coverage_status: "full-index"
source_signature: "4aaadc2f0ab908e5f2f4d6e4ad640a8284b715a5"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:47:18"
---

# Volumetric Fracturing Behavior of 3D Printed Artificial Rocks Containing Single and Double 3D Internal Flaws under Static Uniaxial Compression.

## One-line Summary
This study uses 3D printing to fabricate artificial rocks with single and double penny-shaped internal flaws, investigating how flaw geometry influences mechanical properties and 3D crack growth under uniaxial compression.

## Research Question
How do flaw number, flaw inclination angle (α), and ligament angle (β) influence the mechanical properties and volumetric fracturing behavior of rocks containing 3D internal flaws under static uniaxial compression? [Zhou 2018, pp. 1-3]

## Study Area / Data
The study uses laboratory experiments on 3D printed artificial rock samples. The samples are prismatic (60 × 30 × 30 mm) and made from a transparent resin (Accura® 60) using Stereolithography (SLA) 3D printing. They contain pre-existing, penny-shaped 3D internal flaws with a radius (a) of 5 mm and an aperture of 2 mm. Parameters varied include flaw number (single or double), flaw inclination angle α (0°, 30°, 60°, 90° for single flaws; fixed at 45° for double flaws), and ligament angle β (45°, 65°, 85°, 105° for double flaws). The ligament length (b) is 5 mm. [Zhou 2018, pp. 4-6]

## Methods
- **Sample Preparation:** Samples were fabricated using an SLA-based 3D printer (Viper si2) with Accura® 60 resin. The workflow involved creating a 3D CAD model, digital slicing, layer-by-layer printing, and post-processing (grinding and polishing) to transparentize the samples. [Zhou 2018, pp. 4-6]
- **Testing:** Static uniaxial compression tests were conducted on a servo-controlled testing system (TAW-2000) at a loading rate of 2 mm/min. [Zhou 2018, pp. 6-8]
- **Monitoring:** Two high-speed cameras (FASTCAM SA1.1) were used to record 3D crack growth in real-time from two orthogonal directions. Frame rates were 100,000 fps for single-flawed samples and up to 150,000 fps for double-flawed samples to capture coalescence. [Zhou 2018, pp. 6-8]
- **Analysis:** Mechanical properties (compressive strength σc, axial strain at peak εa, initiation stress of first wing crack σ1) were measured. Crack propagation velocities were calculated from high-speed video sequences. 3D FEM numerical modeling using ANSYS was also conducted to analyze stress distributions. [Zhou 2018, pp. 6-8, 13-15]

## Key Findings
1.  **Mechanical Properties:** Flaw geometry significantly affects strength and deformation. The single-flawed sample with α=60° had the lowest σc (99.9 MPa) and εa (2.38%). For double-flawed samples, σc and εa generally increased as β changed from 45° to 105°. Increasing the flaw number from one to two decreased the average σc and εa. [Zhou 2018, pp. 6-8]
2.  **Crack Initiation:** The initiation stress of the first wing crack (σ1) is influenced by α and β. However, the ratio σ1/σc is approximately 55% and appears largely independent of flaw geometry, except for the sample with β=65°. [Zhou 2018, pp. 8-10]
3.  **3D Crack Growth:** Wing and anti-wing cracks initiated at flaw tips and wrapped around the flaw edge, propagating only a limited distance (approximately 1-1.5 times the flaw length). Final, burst-like failure was caused by the unstable propagation of secondary cracks generated after the peak stress. [Zhou 2018, pp. 8-10, 10-11]
4.  **Crack Coalescence:** In double-flawed samples, coalescence patterns depend on β. Wing cracks from inner tips did not coalesce except when β=105°. Coplanar and petal cracks were also observed. [Zhou 2018, pp. 8-10]
5.  **Crack Velocity:** Wing and secondary cracks propagated in an unstable, jump-like manner. The mean maximum velocity of wing cracks was about 60% that of secondary cracks. The maximum secondary crack velocity was higher in single-flawed samples (977 m/s) than in double-flawed samples (831 m/s). [Zhou 2018, pp. 10-11]
6.  **Special Cases:** Samples with α=0° and 90° did not generate macroscopic wing or secondary cracks; instead, they showed oblique cracks and plastic deformation. FEM modeling confirmed low tensile stresses at flaw tips for these orientations. [Zhou 2018, pp. 11-13, 13-15]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Single flawed sample with α=60° has lowest σc (99.9 MPa) and εa (2.38%). | [Zhou 2018, pp. 6-8] | Single flaw, α=60° | Decreased by ~12.2% and 37.5% compared to intact sample. |
| Double flawed sample with β=45° has lowest σc (79.3 MPa) and εa (1.92%). | [Zhou 2018, pp. 6-8] | Double flaws, β=45° | Decreased by 30.3% and 49.6% compared to intact sample. |
| σc and εa increase by ~10% as β changes from 45° to 105°. | [Zhou 2018, pp. 6-8] | Double flaws, β from 45° to 105° | General trend for double-flawed samples. |
| Average σc and εa decrease by 21.8% and 28.3% when flaw number increases from one to two. | [Zhou 2018, pp. 6-8] | Comparison of single vs. double flaws | Flaw number has a greater effect than α or β. |
| Wing and anti-wing cracks propagate only ~1-1.5 times the initial flaw length. | [Zhou 2018, pp. 8-10] | Single flaw, α=30° | Observed via high-speed camera. |
| Wing cracks from inner tips of double flaws do not coalesce, except when β=105°. | [Zhou 2018, pp. 8-10] | Double flaws, various β | Coalescence pattern depends on ligament angle. |
| Mean maximum wing crack velocity is ~60% of mean maximum secondary crack velocity. | [Zhou 2018, pp. 10-11] | All flawed samples | Calculated from high-speed video. |
| Maximum secondary crack velocity is 977 m/s (single flaw) vs. 831 m/s (double flaws). | [Zhou 2018, pp. 10-11] | Single vs. double flaws | Flaw number affects secondary crack velocity. |
| Samples with α=0° and 90° show no macrocracks, only oblique cracks and plastic deformation. | [Zhou 2018, pp. 11-13, 13-15] | Single flaw, α=0° and 90° | FEM shows low tensile stresses at flaw tips. |
| Ratio σ1/σc is approximately 55% and independent of flaw number. | [Zhou 2018, pp. 10-11, 13-15] | Single and double flaws | Except for sample with β=65°. |

## Limitations
- The high-speed camera had limited storage (8 GB), restricting continuous recording to ~0.7 seconds at 100,000 fps, requiring manual triggering and pausing of the loading machine. [Zhou 2018, pp. 6-8]
- The final 3D crack growth in the single-flawed sample with α=60° failed to be recorded. [Zhou 2018, pp. 6-8]
- The study was conducted under static uniaxial compression at room temperature; behavior under dynamic loading or confining pressure was not investigated. [Zhou 2018, pp. 6-8]
- The physical mechanism behind the formation of slowly generated oblique cracks at flaw tips requires further numerical or theoretical study. [Zhou 2018, pp. 11-13]

## Assumptions / Conditions
- The Accura® 60 resin material is a suitable analogue for mimicking brittle and hard rocks. [Zhou 2018, pp. 4-6]
- The penny-shaped flaw is a valid and simple model for studying 3D crack growth in brittle materials. [Zhou 2018, pp. 4-6]
- The prismatic sample geometry (2:1 length-to-width ratio) is acceptable for the study. [Zhou 2018, pp. 4-6]
- Tests were performed under room temperature (~20°C). [Zhou 2018, pp. 6-8]
- The FEM model used the same mechanical properties as the intact 3DP sample (σc=113.8 MPa, density=1200 kg/m³, E=3.5 GPa, ν=0.4). [Zhou 2018, pp. 13-15]

## Key Variables / Parameters
- **Independent Variables:** Flaw number (single, double), flaw inclination angle (α), ligament angle (β).
- **Dependent Variables:** Uniaxial compressive strength (σc), axial strain at peak stress (εa), initiation stress of first wing crack (σ1), crack propagation velocity, crack coalescence pattern, failure mode.
- **Controlled Parameters:** Sample size (60x30x30 mm), flaw radius (a=5 mm), flaw aperture (2 mm), ligament length (b=5 mm for double flaws), loading rate (2 mm/min), material (Accura® 60 resin). [Zhou 2018, pp. 4-6, 6-8]

## Reusable Claims
- Under uniaxial compression, 3D wing cracks initiated at the tips of penny-shaped internal flaws in brittle resin propagate only a limited distance (1-1.5 times the flaw radius) before arresting, unlike 2D through-going flaws where wing cracks can grow stably and split the sample. [Zhou 2018, pp. 10-11]
- The ratio of the first crack initiation stress to the uniaxial compressive strength (σ1/σc) is approximately 55% and is largely independent of the number of pre-existing flaws (one or two) in the tested 3D printed resin material. [Zhou 2018, pp. 10-11, 13-15]
- The maximum propagation velocity of secondary cracks (which cause final failure) is higher in specimens with a single pre-existing 3D internal flaw than in those with two parallel flaws under uniaxial compression. [Zhou 2018, pp. 10-11]
- When the normal direction of a 3D penny-shaped internal flaw is nearly parallel (0°) or perpendicular (90°) to the maximum compression, the tensile stress at the flaw tip is significantly reduced, impeding the growth of wing cracks and leading to a different failure mode involving plastic deformation. [Zhou 2018, pp. 11-13, 13-15]

## Candidate Concepts
- [[Volumetric fracturing]]
- [[3D internal flaw]]
- [[Penny-shaped crack]]
- [[Wing crack]]
- [[Anti-wing crack]]
- [[Secondary crack]]
- [[Crack coalescence]]
- [[Brittle fracture]]
- [[Stress intensity factor]]

## Candidate Methods
- [[Stereolithography (SLA) 3D printing]]
- [[Static uniaxial compression test]]
- [[High-speed photography]]
- [[3D FEM numerical modeling]]
- [[Image-measuring technique]]

## Connections To Other Work
- The study validates its 3D printing approach by comparing wing crack patterns in a single-flawed sample (α=30°) with those observed in PMMA, silica glass, and polyester resin in previous studies. [Zhou 2018, pp. 11-13]
- It contrasts the limited propagation of 3D wing cracks with the stable growth of 2D wing cracks reported in earlier research on materials like sandstone and PMMA. [Zhou 2018, pp. 10-11]
- The observation of petal cracks in double-flawed samples is noted to be similar to findings in PMMA specimens with 3D surface flaws. [Zhou 2018, pp. 8-10]
- The formation of oblique cracks is compared to en echelon cracks in shear zones from 2D flaw tips in PMMA. [Zhou 2018, pp. 11-13]
- The study builds on prior work that identified Accura® 60 resin as suitable for mimicking brittle rocks. [Zhou 2018, pp. 4-6]

## Open Questions
- What is the precise physical mechanism underlying the formation of slowly generated oblique cracks at the tips of 3D flaws? [Zhou 2018, pp. 11-13]
- How would the fracturing behavior change under dynamic loading conditions or under confining pressure? [Zhou 2018, pp. 6-8]
- Can the findings be generalized to other rock-like materials or to flaws with different geometries (e.g., non-penny-shaped)? [Zhou 2018, pp. 4-6]
- How does the plastic deformation observed in samples with α=0° and 90° affect the long-term stability of rock structures with similarly oriented flaws? [Zhou 2018, pp. 13-15]

## Source Coverage
All non-empty indexed fragments were processed. The compilation is based on 13 indexed source blocks containing a total of 64,931 characters. The compiled page incorporates information from all 13 blocks, covering 62,471 characters, resulting in a coverage ratio of 1.0 by blocks and 0.962 by characters. The source signature is `4aaadc2f0ab908e5f2f4d6e4ad640a8284b715a5`.
