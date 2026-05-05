---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-li-modeling-of-natural-fractures-and-numerical-simulation-of-hydraulic-fracturing-in-deep-s"
title: "Modeling of Natural Fractures and Numerical Simulation of Hydraulic Fracturing in Deep Shale."
status: "draft"
source_pdf: "data/papers/unknown-year - 深部页岩天然裂缝建模及水力压裂数值模拟.pdf"
collections:
  - "大论文-离散裂缝网络"
citation: "Li, Yaping. \"Modeling of Natural Fractures and Numerical Simulation of Hydraulic Fracturing in Deep Shale.\" Southwest Petroleum University, 2023. Doctoral dissertation."
indexed_texts: "53"
indexed_chars: "264666"
nonempty_source_blocks: "53"
compiled_source_blocks: "53"
compiled_source_chars: "265703"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.003918"
coverage_status: "full-index"
source_signature: "d112e1b8719bbb96c0103da8e0bae3c02c9a4b31"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:50:52"
---

# Modeling of Natural Fractures and Numerical Simulation of Hydraulic Fracturing in Deep Shale.

## One-line Summary

This doctoral dissertation develops improved discrete fracture network (DFN) models for deep shale reservoirs by linking shale mechanical properties to natural fracture density through anisotropic fracture energy theory, then uses these models to simulate hydraulic fracturing and optimize perforation parameters for deep (4000 m) shale gas reservoirs in the southeastern Chongqing region of the Sichuan Basin.

## Research Question

How to establish reliable natural fracture distribution models for deep and ultra-deep shale reservoirs that account for burial depth, tectonic stress, and rock physical properties, and how do these natural fractures interact with hydraulic fractures under various perforation parameters during hydraulic fracturing operations? [Li 2023, pp. 1-4]

## Study Area / Data

The study focuses on the southeastern Chongqing (渝东南) region of the Sichuan Basin, a key target area for shale gas exploitation in China. The target formation is the Silurian Longmaxi (龙马溪组) shale. Data sources include:

- **Core data** from seven test wells: YC4, YY1, QQ1, YQ1, YC8, YC6, and YC7, with burial depths ranging from approximately 125 m to 1170 m [Li 2023, pp. 42-44]
- **Outcrop data** from 45 field measurement points across three tectonic zones (I, II, III) [Li 2023, pp. 47-50]
- **UAV (unmanned aerial vehicle) photogrammetry** using DJI-Phantom 4pro and DJI-M300RTK drones for virtual outcrop fracture mapping [Li 2023, pp. 47-50]
- **Regional tectonic stress data** from statistical regression of in-situ stress measurements for the southwestern China region [Li 2023, pp. 24-26]
- **Rock mechanical test data** from Longmaxi Formation outcrop shale samples including uniaxial, conventional triaxial, and true triaxial compression tests [Li 2023, pp. 29-31]

The study area covers the Longmaxi Formation shale reservoirs with burial depths from shallow (<3500 m) to deep (3500-4500 m) and ultra-deep (>4500 m) zones [Li 2023, pp. 11-13].

## Methods

### 1. Non-uniform Shale Mechanical Model Development
A secondary development of the ABAQUS finite element program was performed using Python scripting to create a non-uniform shale mechanical model based on Weibull statistical damage theory. The elastic modulus non-uniformity parameter m=3 was determined through comparison with uniaxial and triaxial compression test results. The Drucker-Prager failure criterion with cap model and fracture-energy-based damage evolution was adopted [Li 2023, pp. 29-35].

### 2. Two-Dimensional Natural Fracture Mathematical Model (Chapter 3)
Based on Monte Carlo random theory, a 2D discrete fracture model was established using:
- **Point process**: Poisson process for random fracture center positions [Li 2023, pp. 50-52]
- **Fracture length**: Log-normal distribution (μ and σ parameters) [Li 2023, pp. 55-58]
- **Fracture dip/strike**: Von Mises distribution (circular normal distribution) [Li 2023, pp. 61-64]
- **Fracture aperture**: Exponential distribution [Li 2023, pp. 64-67]
- **Fracture shape**: Rectangular and elliptical shapes with aspect ratio ~0.5, determined from UAV virtual outcrop measurements [Li 2023, pp. 55-58]

### 3. Three-Dimensional DFN Model Based on Rock Physical Properties (Chapter 4)
An improved DFN modeling method was developed by:
- Establishing a quantitative relationship between shale mechanical parameters and natural fracture volume density using anisotropic fracture energy theory [Li 2023, pp. 70-73]
- Calculating fracture volume density (Dvf) from rock compression test data using energy balance equations [Li 2023, pp. 73-75]
- Converting volume density to fracture count in the model volume [Li 2023, pp. 75-77]
- Models were built in MATLAB and post-processed in COMSOL Multiphysics [Li 2023, pp. 70-73]

### 4. Hydraulic Fracturing Numerical Simulation (Chapters 5-6)
The RFPA (Realistic Failure Process Analysis) method was used for hydraulic fracturing simulation, which:
- Uses damage smear method (DSM) to handle discontinuities without remeshing [Li 2023, pp. 87-90]
- Incorporates Biot consolidation theory and modified Terzaghi effective stress principle for fluid-mechanical coupling [Li 2023, pp. 87-90]
- Assigns Weibull-distributed mechanical parameters to represent shale heterogeneity [Li 2023, pp. 87-90]

Perforation parameters analyzed include: perforation direction (0°, 45°, 90° relative to vertical stress), perforation spacing (0.25 m, 0.5 m, 1 m), perforation count (3, 5, 9), and staggered perforation arrangements [Li 2023, pp. 93-96].

## Key Findings

1. **Non-uniformity parameter**: The elastic modulus non-uniformity parameter m=3 best matches experimental results for Longmaxi shale across different bedding angles [Li 2023, pp. 35-38].

2. **2D model applicability**: The 2D discrete fracture model based on core data is reliable when model size exceeds 5 m; larger models produce more stable and accurate results [Li 2023, pp. 67-70].

3. **3D model validation**: The 3D DFN model based on rock physical properties was validated against core fracture data from seven test wells, with simulated P10 (linear density) and P32 (volume density) values closely matching measured data [Li 2023, pp. 81-84].

4. **Fracture density vs. depth**: Fracture density does not continuously increase with burial depth; for the YC6 area, fracture development is highest around 3000 m depth, and density decreases beyond 3000 m due to increased energy requirements for fracture formation under higher confining pressure [Li 2023, pp. 81-84].

5. **Natural fractures reduce initiation pressure**: Natural fractures in the reservoir effectively reduce the initiation pressure of hydraulic fractures by serving as structural weak planes [Li 2023, pp. 93-96].

6. **Perforation direction**: For deep reservoirs with predominantly high-angle oblique natural fractures, perforation direction perpendicular to natural fracture orientation is the dominant perforation direction; 45° inclined perforations show the best fracturing effect [Li 2023, pp. 103-107].

7. **Staggered perforation**: Staggered perforation arrangements effectively reduce initiation pressure and avoid casing damage compared to symmetric arrangements, while enabling better communication between hydraulic and natural fractures [Li 2023, pp. 114-117].

8. **Perforation density effects**: Perforation density significantly affects initiation pressure and hydraulic fracture propagation morphology; excessive perforation count causes stress interference between perforations, leading to local fragmentation near the casing [Li 2023, pp. 111-114].

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Elastic modulus non-uniformity parameter m=3 determined from uniaxial/triaxial tests | [Li 2023, pp. 35-38] | Longmaxi shale, different bedding angles (0°-90°) | Validated against experimental peak strength data |
| 2D model size ≥5 m required for reliable fracture density | [Li 2023, pp. 67-70] | YC6 well core data, model sizes 1-50 m | Larger models converge to measured density values |
| 3D DFN model P10=3.6 vs measured 3.7 for YY1 well | [Li 2023, pp. 81-84] | 10m×10m×10m model, YY1 well 125-315 m depth | Model data averaged over multiple random realizations |
| Fracture density peaks at ~3000 m depth for YC6 area | [Li 2023, pp. 81-84] | Depths 500-5000 m, southwestern China stress regime | P32 values: 3.21 (500m) to 5.13 (3000m) to 5.09 (5000m) |
| Natural fractures reduce initiation pressure in reservoir | [Li 2023, pp. 93-96] | 10m×10m model, YC6 well parameters, 679-782 m depth | Compared with and without natural fractures |
| 45° perforation direction optimal for deep reservoirs | [Li 2023, pp. 103-107] | 4000 m burial depth, σv=100.8 MPa, σH=102.69 MPa | Lower initiation pressure, better natural fracture communication |
| Staggered 5-perforation arrangement effective | [Li 2023, pp. 114-117] | 4000 m depth, 0.5 m spacing | Avoids casing damage, forms complex fracture network |
| Log-normal distribution best describes fracture length | [Li 2023, pp. 55-58] | UAV outcrop data from three tectonic zones | Parameters μ≈0.05-0.34, σ≈0.46-0.51 |
| Von Mises distribution for fracture orientation | [Li 2023, pp. 61-64] | Core and outcrop data, southeastern Chongqing | κf=30 for dip, κs=80 for strike |
| Exponential distribution for fracture aperture | [Li 2023, pp. 64-67] | Multi-well core data, southeastern Chongqing | λ≥0.5, >60% fractures have aperture <1 mm |

## Limitations

1. The 2D fracture model uses simplified line segments as fracture geometry, not accounting for fracture aperture effects on shape [Li 2023, pp. 67-70].
2. The 3D DFN model assumes fractures as planar geometric shapes (rectangles, ellipses) which may not fully capture natural fracture complexity [Li 2023, pp. 84-87].
3. The RFPA hydraulic fracturing simulation uses a 2D cross-section extracted from the 3D model, which may not capture full 3D fracture propagation behavior [Li 2023, pp. 93-96].
4. The model does not consider the effect of mineral filling on fracture mechanical properties in the DFN model construction, though this is partially addressed in the hydraulic fracturing simulations [Li 2023, pp. 67-70].
5. Casing damage analysis during perforation fracturing is acknowledged but not deeply investigated as it falls outside the study scope [Li 2023, pp. 111-114].
6. The study relies on outcrop shale samples for mechanical testing due to the high cost and limited availability of deep core samples, though outcrop samples from the same formation are considered representative [Li 2023, pp. 26-29].
7. The model validation relies on limited well data (seven wells) and the random nature of Monte Carlo simulation requires multiple realizations for statistical reliability [Li 2023, pp. 81-84].

## Assumptions / Conditions

1. Shale is treated as a transversely isotropic continuous body with horizontal bedding (β=0°) for the study area [Li 2023, pp. 73-75].
2. Fracture positions follow a Poisson process (complete spatial randomness) when no specific clustering data is available [Li 2023, pp. 50-52].
3. Fractures are assumed to be disc-shaped (circular) in the DFN model, with geometric simplification to rectangles or ellipses [Li 2023, pp. 52-55].
4. The Weibull distribution with m=3 adequately represents the heterogeneity of Longmaxi shale mechanical properties [Li 2023, pp. 29-31].
5. Core fracture data from shallow wells can be extrapolated to predict deep reservoir fracture distributions using the established mechanical relationship [Li 2023, pp. 81-84].
6. The "pure" shale (low initial fracture density) outcrop samples are used for compression tests to calculate fracture volume density, assuming minimal pre-existing damage [Li 2023, pp. 73-75].
7. Regional tectonic stress follows statistical regression patterns established for southwestern China [Li 2023, pp. 24-26].
8. Fracture length distribution follows log-normal distribution, fracture orientation follows Von Mises distribution, and aperture follows exponential distribution based on statistical analysis of measured data [Li 2023, pp. 55-67].

## Key Variables / Parameters

| Variable | Description | Value/Range | Source |
|----------|-------------|-------------|--------|
| m | Elastic modulus non-uniformity parameter | 3 | [Li 2023, pp. 35-38] |
| P10 | Linear fracture density (fractures/m) | 0.34-4.16 (varies by well) | [Li 2023, pp. 52-55] |
| P32 | Volume fracture density (m²/m³) | 3.21-5.13 (varies by depth) | [Li 2023, pp. 81-84] |
| Dvf | Fracture volume density from energy theory | Calculated from Eq. 4-2 | [Li 2023, pp. 73-75] |
| σv | Vertical stress at 4000 m | 100.8 MPa | [Li 2023, pp. 38-42] |
| σH | Maximum horizontal stress at 4000 m | 102.69 MPa | [Li 2023, pp. 38-42] |
| σh | Minimum horizontal stress at 4000 m | 71.04 MPa | [Li 2023, pp. 38-42] |
| E (shale matrix) | Elastic modulus | 20000 MPa | [Li 2023, pp. 87-90] |
| E (fracture matrix) | Elastic modulus | 13000 MPa | [Li 2023, pp. 87-90] |
| σc (shale matrix) | Compressive strength | 120 MPa | [Li 2023, pp. 87-90] |
| σc (fracture matrix) | Compressive strength | 28.8 MPa | [Li 2023, pp. 87-90] |
| μ (log-normal) | Fracture length mean parameter | 0.05-0.34 | [Li 2023, pp. 58-61] |
| σ (log-normal) | Fracture length dispersion parameter | ~0.5 | [Li 2023, pp. 58-61] |
| κf (Von Mises) | Fracture dip concentration parameter | 30 | [Li 2023, pp. 77-81] |
| κs (Von Mises) | Fracture strike concentration parameter | 80 | [Li 2023, pp. 77-81] |
| λ (exponential) | Fracture aperture distribution parameter | ≥0.5 | [Li 2023, pp. 64-67] |
| Kf (aspect ratio) | Fracture shape length-to-width ratio | ~0.5 | [Li 2023, pp. 55-58] |
| Model size | DFN model dimensions | 10m×10m×10m (3D) | [Li 2023, pp. 77-81] |
| Perforation spacing | Optimal spacing for deep reservoir | 0.5 m | [Li 2023, pp. 111-114] |
| Perforation direction | Optimal for deep reservoir | 45° inclined | [Li 2023, pp. 103-107] |

## Reusable Claims

1. **For Longmaxi shale, the elastic modulus non-uniformity parameter m=3 provides the best match between Weibull statistical damage model predictions and experimental compression test results across different bedding angles.** This parameter should be used when modeling shale mechanical behavior in the southeastern Chongqing region. [Li 2023, pp. 35-38]

2. **A 2D discrete fracture model based on core data requires a minimum model size of 5 m to reliably represent reservoir fracture distribution; models larger than 5 m produce increasingly stable and accurate results.** This size threshold applies to models constrained by measured core linear density. [Li 2023, pp. 67-70]

3. **Natural fracture volume density (P32) does not increase monotonically with burial depth; for the YC6 area, fracture density peaks around 3000 m depth and decreases at greater depths due to increased energy requirements for fracture formation under higher confining pressure.** This relationship is specific to the southwestern China tectonic stress regime. [Li 2023, pp. 81-84]

4. **In deep shale reservoirs (4000 m), perforation direction perpendicular to the dominant natural fracture orientation is the optimal perforation direction, and 45° inclined perforations relative to the vertical stress direction show the best fracturing performance.** This applies to reservoirs with predominantly high-angle oblique natural fractures. [Li 2023, pp. 103-107]

5. **Staggered perforation arrangements effectively reduce initiation pressure and avoid casing damage compared to symmetric perforation layouts, while enabling better communication between hydraulic and natural fractures to form complex fracture networks.** This applies to deep reservoir fracturing with natural fractures present. [Li 2023, pp. 114-117]

6. **Natural fractures in shale reservoirs reduce hydraulic fracture initiation pressure, cause non-uniform water pressure distribution, and guide hydraulic fracture propagation away from the principal stress direction, forming complex fracture networks essential for shale gas production.** Ignoring natural fractures in simulation leads to significant deviation from actual fracturing behavior. [Li 2023, pp. 93-96]

7. **The log-normal distribution best describes shale reservoir natural fracture length, the Von Mises distribution best describes fracture orientation (dip and strike), and the exponential distribution best describes fracture aperture, based on statistical analysis of southeastern Chongqing shale data.** These distributions apply to macroscopic tectonic fractures in Longmaxi Formation shale. [Li 2023, pp. 55-67]

8. **For deep reservoirs with high-angle oblique natural fractures, perforation density significantly affects initiation pressure and hydraulic fracture propagation morphology; excessive perforation count causes stress interference leading to local fragmentation near the casing.** An optimal perforation spacing of approximately 0.5 m in a 2 m perforation section is recommended. [Li 2023, pp. 111-114]

## Candidate Concepts

- [[discrete fracture network (DFN)]]
- [[natural fracture modeling]]
- [[hydraulic fracturing]]
- [[shale gas reservoir]]
- [[Monte Carlo simulation]]
- [[Weibull distribution]]
- [[non-uniformity parameter]]
- [[fracture volume density]]
- [[anisotropic fracture energy]]
- [[perforation optimization]]
- [[deep shale reservoir]]
- [[Longmaxi Formation]]
- [[tectonic stress]]
- [[fracture initiation pressure]]
- [[fracture propagation]]
- [[staggered perforation]]
- [[Von Mises distribution]]
- [[log-normal distribution]]
- [[RFPA (Realistic Failure Process Analysis)]]
- [[damage smear method]]
- [[point process]]
- [[marked point process]]
- [[fracture density (P10, P32)]]
- [[transversely isotropic shale]]
- [[bedding plane]]
- [[fracture shape (rectangular, elliptical)]]
- [[UAV photogrammetry]]
- [[virtual outcrop]]

## Candidate Methods

- [[Weibull statistical damage model]]
- [[Monte Carlo random simulation]]
- [[DFN modeling with point and marked point processes]]
- [[anisotropic fracture energy density method]]
- [[RFPA hydraulic-mechanical coupling simulation]]
- [[Drucker-Prager cap model]]
- [[ABAQUS secondary development (Python scripting)]]
- [[COMSOL Multiphysics post-processing]]
- [[MATLAB fracture network generation]]
- [[UAV-based virtual outcrop mapping]]
- [[FracPaQ image processing]]
- [[Von Mises distribution for angular data]]
- [[Brazilian disc test for fracture toughness]]
- [[true triaxial numerical simulation]]
- [[damage smear method (DSM)]]
- [[Biot consolidation theory]]
- [[modified Terzaghi effective stress principle]]
- [[log-normal distribution fitting]]
- [[exponential distribution fitting]]
- [[convex hull algorithm for fracture plane ordering]]

## Connections To Other Work

The dissertation builds upon and connects to several research streams:

1. **DFN modeling**: Extends the foundational work of Baecher (1983) on discrete fracture network modeling by improving the point process density determination method through rock mechanical theory [Li 2023, pp. 15-17].

2. **Equivalent DFN methods**: References Ren et al. (2017) and Ma et al. (2019, 2020) who used theoretical methods (E-DFN) to reduce fracture count in point processes for improved computational efficiency [Li 2023, pp. 15-17].

3. **Hydraulic fracture-natural fracture interaction**: Builds on the classic experimental work of Warpinski and Teufel (1987) on hydraulic fracture propagation through natural discontinuities, which was used for model validation [Li 2023, pp. 90-93].

4. **RFPA method**: Applies the Realistic Failure Process Analysis method developed by Tang and Tang (2011) for rock failure simulation, extending it to hydraulic fracturing in heterogeneous shale with natural fractures [Li 2023, pp. 87-90].

5. **Shale mechanical properties**: References experimental work by Hou et al. (2015, 2018) on Longmaxi shale anisotropic mechanical characteristics under different bedding angles [Li 2023, pp. 26-29].

6. **Regional stress characterization**: Uses stress regression data from He Jian (2017) for southwestern China and Jing Feng (2009) for mainland China [Li 2023, pp. 24-26].

7. **Fracture toughness prediction**: Applies the fracture toughness prediction model from Jin Yan et al. (2008) for deep shale using logging data [Li 2023, pp. 73-75].

8. **Perforation fracturing**: Connects to experimental studies by Zhang et al. (2018), Shi et al. (2021), and Shan et al. (2021, 2022) on perforation parameters and near-wellbore fracture propagation [Li 2023, pp. 17-21].

## Open Questions

1. How do micro-scale fractures (nanometer to micrometer scale) interact with macro-scale tectonic fractures during hydraulic fracturing, and can a multi-scale DFN model be developed to capture this interaction? [Li 2023, pp. 117-119]

2. Can the improved DFN method be extended to field-scale (hundreds of meters) horizontal well multi-stage fracturing simulations while maintaining computational efficiency? [Li 2023, pp. 117-119]

3. How do temperature effects in ultra-deep reservoirs (>4500 m) influence the mechanical properties of shale and the fracture density-depth relationship established in this study? [Li 2023, pp. 117-119]

4. What is the optimal combination of perforation parameters (direction, spacing, count, arrangement) for specific deep reservoir conditions with varying natural fracture distributions? [Li 2023, pp. 114-117]

5. How does the mineral filling composition of natural fractures (calcite, pyrite, clay minerals) quantitatively affect hydraulic fracture propagation in deep reservoirs? [Li 2023, pp. 100-103]

6. Can composite numerical methods (e.g., discrete element-finite element, displacement discontinuity-finite element) better capture the complex hydraulic fracturing process in naturally fractured deep shale reservoirs? [Li 2023, pp. 117-119]

## Source Coverage

All 53 non-empty indexed fragments were processed in a single compilation pass. The indexed text contains 264,666 characters across 53 source blocks, and the compiled output contains 265,703 characters from 53 compiled source blocks. The coverage ratio by blocks is 1.0 (100%) and by characters is 1.004. The source signature is d112e1b8719bbb96c0103da8e0bae3c02c9a4b31. Coverage status: full-index.
