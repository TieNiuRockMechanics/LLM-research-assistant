---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2016-qu-study-on-rough-fracture-description-and-fluid-flow-in-rough-fracture"
title: "Study on Rough Fracture Description and Fluid Flow in Rough Fracture."
status: "draft"
source_pdf: "data/papers/2018 - 粗糙裂缝结构的描述及其渗流规律研究.pdf"
collections:
  - "大论文-离散裂缝网络"
citation: "Qu, Guanzheng. \"Study on Rough Fracture Description and Fluid Flow in Rough Fracture.\" PhD dissertation, China University of Petroleum (East China), 2016."
indexed_texts: "31"
indexed_chars: "153930"
nonempty_source_blocks: "31"
compiled_source_blocks: "31"
compiled_source_chars: "145605"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.945917"
coverage_status: "full-index"
source_signature: "34e7e629670fb361050413089284c59c875be4af"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:11:41"
---

# Study on Rough Fracture Description and Fluid Flow in Rough Fracture.

## One-line Summary
This dissertation systematically investigates the description of rough fracture structures and the fluid flow laws within them, using theoretical derivation, physical experiments, and Lattice Boltzmann numerical simulation to study tensile, mismatched, and shear-slipping fractures.

## Research Question
The research aims to address the following core questions:
1.  How to accurately describe the roughness of fracture surfaces and establish a permeability calculation model for tensile fractures?
2.  What are the seepage characteristics and pressure/velocity distribution laws within tensile rough fractures?
3.  How does the non-matching between fracture walls (based on Gaussian distribution) affect fracture permeability?
4.  What is the influence of shear-slipping action on the permeability of different fracture structures (basic units, 2D profiles, 3D rough fractures)?
5.  How to derive a new calculation method for tortuosity based on seepage velocity distribution?

## Study Area / Data
The study utilizes shale core samples from the **Barnett Basin in the United States**. Artificial tensile fractures were created from these cores using the **Brazilian splitting test**. The 3D morphology of the fracture walls was obtained using a **3D profilometer** (NANOVEA company). Random regions of 3mm × 1.5mm were extracted from the scanned surfaces for Lattice Boltzmann simulations.

## Methods
The research employs a combination of **theoretical derivation, physical experiments, and numerical simulation**.
*   **Physical Experiments:** Brazilian splitting test to create tensile fractures; 3D profilometer scanning to obtain fracture wall topography.
*   **Numerical Simulation:** **Lattice Boltzmann Method (LBM)**, specifically the **LBGK-D3Q19 model**, implemented using the commercial software **PowerFLOW**. This method is chosen for its advantage in handling complex boundary conditions at the mesoscale.
*   **Data Analysis & Modeling:**
    *   **Clustering Analysis** to determine the independence of characteristic parameters (tortuosity, roughness, angularity).
    *   **Grey Relational Analysis** to quantify the influence degree of various factors on permeability.
    *   **Orthogonal Experimental Design** combined with Grey Relational Analysis for studying mismatched fractures.
    *   **Fractal Theory** and **Gaussian distribution functions** to generate synthetic rough fracture surfaces with controlled parameters (roughness, fractal dimension, mismatch length, anisotropy coefficient).
    *   Derivation of a **tortuosity calculation formula based on velocity distribution**.

## Key Findings
1.  **Tensile Fracture Characterization:** Sample tortuosity is around 1.10, angularity ranges from 0.99° to 8.86°, and roughness ranges from 0.062 to 0.162 mm. Tortuosity, roughness, and angularity are not substitutable for each other; all three must be considered for permeability calculation [Qu 2016, pp. 31-32].
2.  **Tensile Fracture Permeability:** The permeability of actual rough fractures is **19%~29% less** than that of the ideal parallel plate model, necessitating the consideration of roughness [Qu 2016, pp. 39-40]. A permeability calculation formula for shale tensile fractures (aperture 0.05-0.40 mm) was derived and verified, with errors within 4% [Qu 2016, pp. 39-40].
3.  **Seepage Characteristics in Tensile Fractures:** Pressure distribution along the flow direction is linear with minor fluctuations. Velocity distribution is non-uniform, with recirculation zones forming near areas of significant surface roughness change. Seepage velocity is related to both wall roughness and the tortuosity of the flow path [Qu 2016, pp. 50-54, 62-63].
4.  **Mismatched Fractures (Gaussian-based):** As mismatch length increases, fracture permeability shows a fluctuating growth trend and tends to stabilize. The permeability of mismatched fractures is slightly lower than that of matched fractures. Aperture and roughness are the most significant factors, followed by fractal dimension, anisotropy coefficient, and mismatch length [Qu 2016, pp. 79-82, 86].
5.  **Shear-Slipping Fractures:** For basic structural units (V-shape, sinusoid, groove), permeability decreases rapidly and then stabilizes as slipping distance increases. For 2D profile structures, permeability shows a general decreasing trend. For 3D rough fractures, permeability decreases with slipping distance. When no contact area exists, slipping reduces permeability; when contact area exists, slipping can increase permeability by creating self-supporting channels [Qu 2016, pp. 103-110].
6.  **Tortuosity Calculation:** A new formula for calculating 2D tortuosity based on velocity distribution was derived and verified using basic structural units and equivalent plate models with contact areas [Qu 2016, pp. 113-127].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Sample tortuosity ~1.10, angularity 0.99°-8.86°, roughness 0.062-0.162 mm. | [Qu 2016, pp. 31-32] | Shale tensile fractures from Barnett Basin. | Parameters are independent; all must be considered. |
| Actual rough fracture permeability is 19%-29% less than parallel plate model. | [Qu 2016, pp. 39-40] | Tensile fractures, aperture 0.05-0.40 mm. | Demonstrates the necessity of roughness correction. |
| Derived permeability formula error < 4%. | [Qu 2016, pp. 39-40] | Formula: k = (b²/12) / (τ² cosα (1+0.1277(ε/b)^0.236)). | Validated with samples 4 and 5. |
| Grey relational coefficients: Aperture (0.9132), Tortuosity (0.6882), Roughness (0.6604), Angularity (0.6549). | [Qu 2016, pp. 40-42] | Tensile fracture permeability influencing factors. | Aperture is the dominant factor, but others are non-negligible. |
| Mismatched fracture permeability increases fluctuatingly with mismatch length and stabilizes. | [Qu 2016, pp. 79-82] | Fractures based on Gaussian distribution, D=2.2, roughness=0.1mm. | Permeability of mismatched fractures is slightly lower than matched ones. |
| Grey relational coefficients for mismatched fractures: Aperture (0.8133), Roughness (0.7437), Fractal Dim. (0.6714), Anisotropy (0.6004), Mismatch Length (0.5868). | [Qu 2016, pp. 84-86] | Orthogonal design and grey relational analysis. | Aperture and roughness are the most important factors. |
| For basic units (V, sinusoid, groove), permeability decreases rapidly then stabilizes with slipping distance. | [Qu 2016, pp. 103-106] | Fixed study object length, no contact area. | Minimum aperture is a key factor for slipping fracture permeability. |
| New tortuosity formula based on velocity distribution verified. | [Qu 2016, pp. 113-127] | V-shape, sinusoid, groove, and equivalent plate models with contact areas. | Formula: τ = v(x)/v'(x). Suitable for 2D and 3D tensile fractures. |

## Limitations
1.  The study on shear-slipping fractures **did not consider the influence of contact area** between fracture walls in the main simulations, although its potential effect is discussed [Qu 2016, pp. 110, 130].
2.  The research **did not consider non-Darcy flow** effects [Qu 2016, p. 130].
3.  The physical experiment method for studying shear-slipping (using copper shims) has inherent errors as it changes the study object size and average aperture [Qu 2016, pp. 93-95].

## Assumptions / Conditions
1.  Tensile fractures are assumed to be fully open (aperture range 0.05-0.40 mm) [Qu 2016, p. 22].
2.  Fluid is assumed to be an **incompressible Newtonian fluid** in steady-state laminar flow [Qu 2016, p. 34].
3.  Simulations maintain a constant **Reynolds number (Re=10)** to ensure Darcy flow conditions [Qu 2016, pp. 37, 48, 78].
4.  **Mach number is far below 0.3**, so fluid compressibility is not considered [Qu 2016, pp. 37, 48, 78].
5.  For generated mismatched fractures, the roughness and fractal dimension of both walls are kept consistent [Qu 2016, p. 71].

## Key Variables / Parameters
*   **Tortuosity (τ):** Ratio of actual seepage path length to apparent path length.
*   **Roughness (ε):** Standard deviation of fracture wall height distribution.
*   **Angularity (θ):** Average inclination angle of the fracture wall.
*   **Fracture Aperture (b):** Distance between fracture walls.
*   **Fractal Dimension (D):** Parameter describing the self-affine roughness of the surface.
*   **Mismatch Length:** Characteristic length scale below which fracture walls become uncorrelated.
*   **Anisotropy Coefficient (b/a):** Ratio describing the directional distribution of roughness.
*   **Permeability (k):** Measure of the fracture's ability to transmit fluid.
*   **Reynolds Number (Re):** Ratio of inertial forces to viscous forces.

## Reusable Claims
1.  For shale tensile fractures, the parameters tortuosity, roughness, and angularity are statistically independent and all must be included in permeability models; they cannot substitute for one another [Qu 2016, pp. 31-32].
2.  The permeability of actual rough tensile fractures is 19% to 29% lower than that predicted by the ideal parallel plate model, highlighting the critical role of surface roughness [Qu 2016, pp. 39-40].
3.  In mismatched fractures (based on Gaussian distribution), aperture and roughness are the primary factors controlling permeability, with grey relational coefficients of 0.8133 and 0.7437, respectively [Qu 2016, pp. 84-86].
4.  The effect of shear-slipping on fracture permeability depends on the presence of contact area: slipping decreases permeability when no contact exists, but can increase it when contact area provides self-supporting flow channels [Qu 2016, pp. 110].
5.  The tortuosity formula derived from velocity distribution, τ = v(x)/v'(x), is accurate for calculating 2D tortuosity and the tortuosity of 3D tensile fractures under low-speed, incompressible flow conditions [Qu 2016, pp. 113-127].

## Candidate Concepts
*   [[Rough Fracture]]
*   [[Fracture Permeability]]
*   [[Tortuosity]]
*   [[Lattice Boltzmann Method]]
*   [[Tensile Fracture]]
*   [[Shear-Slipping Fracture]]
*   [[Mismatched Fracture]]
*   [[Fractal Dimension]]
*   [[Brazilian Splitting Test]]
*   [[Grey Relational Analysis]]
*   [[Clustering Analysis]]
*   [[Parallel Plate Model]]
*   [[Darcy's Law]]
*   [[Shale Gas Reservoir]]

## Candidate Methods
*   [[Lattice Boltzmann Method (LBM)]]
*   [[D3Q19 Model]]
*   [[Brazilian Test]]
*   [[3D Profilometry]]
*   [[Clustering Analysis]]
*   [[Grey Relational Analysis]]
*   [[Orthogonal Experimental Design]]
*   [[Fractal Geometry]]
*   [[Gaussian Distribution Function]]
*   [[Weierstrass-Mandelbrot Function]]

## Connections To Other Work
The dissertation builds upon and references extensive prior work:
*   It adopts the **Lattice Boltzmann Method** validated by scholars like Chen Yaosong, Wang Yiwei, and Du Tezhuan [Qu 2016, pp. 36, 48, 77].
*   It uses the **Brazilian test** and **3D profilometer** approach similar to Xiao et al. [Qu 2016, p. 95].
*   It employs the **Gaussian distribution** and **mismatch length** concept for fracture generation based on models by **Brown** and **Glover** [Qu 2016, pp. 65, 70-71].
*   It compares its findings on roughness correction with formulas from **Lomize, Louis, and Brown** [Qu 2016, pp. 21-22].
*   It discusses the **mechanics of shear-slipping** referencing models from **Warpinski, Renshaw, and Zhou** [Qu 2016, pp. 91-92].
*   It derives a new tortuosity formula, addressing limitations of geometric methods used by **Brown** and others for non-matching fractures [Qu 2016, pp. 112-113].

## Open Questions
1.  How to accurately model and simulate the influence of **contact area** between fracture walls on permeability in mismatched and shear-slipping fractures?
2.  How to develop a universal **permeability calculation formula** for non-mismatched and shear-slipping fracture structures?
3.  What is the effect of **non-Darcy flow** in rough fractures, especially at higher flow rates?
4.  How do **fracturing treatment parameters** (e.g., pump schedule) influence the resulting fracture wall roughness and mismatch characteristics?

## Source Coverage
All non-empty indexed fragments were processed. The compilation strategy was single-pass markdown. The coverage audit shows **31 indexed texts** with a total of **153,930 characters**. The compiled source blocks number **31**, containing **145,605 characters**, resulting in a **coverage ratio by blocks of 1.0** and a **coverage ratio by characters of 0.945917**. The source signature is `34e7e629670fb361050413089284c59c875be4af`, and the coverage status is **full-index**.
