---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2015-szalaiov-3d-fracture-networks-in-the-crystalline-upper-crust-a-seismic-model-of-the-contine"
title: "3D Fracture Networks in the Crystalline Upper Crust – A Seismic Model of the Continental Deep Drilling Site (South Germany)."
status: "draft"
source_pdf: "data/papers/3D fracture networks in the crystalline upper crust - A new seismic model of the Continental Deep Drilling Site (South Germany)一维钻孔和三位地震的分形关系.pdf"
collections:
citation: "Szalaiová, Eva, et al. “3D Fracture Networks in the Crystalline Upper Crust – A Seismic Model of the Continental Deep Drilling Site (South Germany).” *Geophysical Prospecting*, vol. 63, 2015, pp. 937–56. doi:10.1111/1365-2478.12268."
indexed_texts: "17"
indexed_chars: "80820"
nonempty_source_blocks: "17"
compiled_source_blocks: "17"
compiled_source_chars: "81260"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.005444"
coverage_status: "full-index"
source_signature: "3aa6b8ef22435b5fabcaffc261792d0d87e22888"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:23:47"
---

# 3D Fracture Networks in the Crystalline Upper Crust – A Seismic Model of the Continental Deep Drilling Site (South Germany).

## One-line Summary
This study presents the first comprehensive 3D seismic model of the fault and fracture network in the crystalline upper crust at the KTB site, developing an automated workflow to quantify fractures and assess their connectivity for fluid flow and geothermal potential.

## Research Question
How can 3D seismic reflection data be used to systematically image and quantify the fault and fracture network of the crystalline upper crust at the KTB site, and how can this network be used to assess fracture connectivity and relative permeability?

## Study Area / Data
The study area is the Continental Deep Drilling Site (KTB) in the Zone of Erbendorf–Vohenstrauß (ZEV), Oberpfalz, Southeast Germany. The data comprise a 3D seismic reflection dataset covering a 19×19 km² area down to 16-km depth, recorded with Vibroseis sources, and complementary borehole data from the KTB superdeep drillhole (final depth 9101 m) [Szalaiov 2015, pp. 1-2, 2-4].

## Methods
An automated workflow was developed comprising:
1.  **Large-scale fault identification:** Using structural tensor analysis to calculate local reflector dip and extract faults with dips >45° and high amplitudes [Szalaiov 2015, pp. 4-5].
2.  **Middle-scale fracture identification:** Applying omni-directional log-Gabor filtering and image processing (contrast inversion, horizontal line removal) to enhance and extract fractures visible as discontinuities between reflection elements [Szalaiov 2015, pp. 5-6].
3.  **Validation:** Comparing results with borehole data (FMS micro-cracks, VSP velocity minima, lithology) and induced seismicity focal mechanisms. Fractal analysis (box-counting method) was used to check statistical consistency between 1D borehole and 3D seismic data [Szalaiov 2015, pp. 6-7, 7-9, 9-11].
4.  **Connectivity assessment:** Using probabilistic percolation theory on the binary 3D fracture volume. A fracture density threshold of 30% was used to define potentially permeable sub-volumes, creating a "relative permeability" function [Szalaiov 2015, pp. 11-12, 12-13].

## Key Findings
-   The fault and fracture inventory of the KTB site follows a fractal law consistent with Turcotte's fractionation model, enabling upscaling/downscaling between 1D borehole and 3D seismic data [Szalaiov 2015, pp. 1-2, 7-9].
-   The corresponding 1D, 2D, and 3D fractal dimensions are approximately 0.8, 1.9, and 2.8, respectively [Szalaiov 2015, pp. 1-2, 15-16].
-   The derived 3D distribution of "relative permeability" can serve as a kernel function for inverting hydraulic permeability from field experiments [Szalaiov 2015, pp. 1-2, 12-13].
-   Considering only critically stressed fractures (shear/normal stress ratio ≥0.6) drastically reduces the number of permeable pathways, consistent with the low bulk permeability measured at the site [Szalaiov 2015, pp. 14-15, 15-16].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Fractal dimensions from 3D seismic: D1=0.76±0.08, D2=1.87±0.20, D3=2.81±0.11 | [Szalaiov 2015, pp. 7-9] | Box-counting on middle-scale fractures from 3D seismic volume. | Internal consistency check (D3≈D2+1≈D1+2). |
| Fractal dimensions from KTB borehole data (e.g., micro-cracks D1=0.86, fault zones from VSP D1=0.75) | [Szalaiov 2015, pp. 9-11, 11-12] | 1D box-counting on various borehole logs. | Values agree with 3D seismic results within error bars and scaling law. |
| Induced seismicity focal planes align with NW-SE striking middle-scale fractures | [Szalaiov 2015, pp. 9-11, 11-12] | Comparison of log-Gabor filtered fractures with fault plane solutions from 2000 fluid injection experiment. | Supports authenticity of seismically detected fracture network. |
| 30% fracture density threshold for percolation | [Szalaiov 2015, pp. 11-12, 12-13] | Based on probabilistic percolation theory for 3D cubic arrays. | Used to define "relative permeability" zones. |
| Critically stressed fractures (μ≥0.6) are likely permeable | [Szalaiov 2015, pp. 14-15] | Applied Coulomb criterion using estimated stress field and pore pressure. | Reduces the effective fracture network for fluid flow. |

## Limitations
-   Seismic resolution limits detection to "middle-scale" fractures (minimum size ~50 m); smaller fractures are below the wavelength limit [Szalaiov 2015, pp. 4-5].
-   The method cannot distinguish between open and healed (closed) fractures from seismic reflections alone [Szalaiov 2015, pp. 14-15].
-   Processing artefacts cannot be fully excluded as a cause for some detected features [Szalaiov 2015, pp. 5-6].
-   The percolation-based connectivity assessment is a statistical model; its adequacy requires validation through hydraulic/thermal modelling and field measurements [Szalaiov 2015, pp. 13-14].

## Assumptions / Conditions
-   The metamorphic crust of the ZEV is a typical example that has undergone numerous phases of ductile and brittle deformation [Szalaiov 2015, pp. 1-2].
-   Abrupt displacements within seismic reflections represent real geological fractures [Szalaiov 2015, pp. 4-5].
-   The fractal distribution of faults is scale-invariant (Turcotte's fractionation model) [Szalaiov 2015, pp. 6-7].
-   A cell in the percolation model is "open" if it is crossed by a seismically detected fracture [Szalaiov 2015, pp. 12-13].
-   The current stress field and pore pressure gradients are linear with depth as approximated from borehole data [Szalaiov 2015, pp. 14-15].

## Key Variables / Parameters
-   **Fractal Dimension (D):** D1 (1D), D2 (2D), D3 (3D).
-   **Fracture Density:** Percentage of fractured voxels in a sub-volume.
-   **Critical Percolation Threshold (p_c):** ~30% for 3D cubic arrays.
-   **"Relative Permeability":** A qualitative measure derived from fracture density above the percolation threshold.
-   **Stress Ratio (μ):** Shear to effective normal stress ratio on a fracture plane (μ ≥ 0.6 indicates critically stressed).

## Reusable Claims
-   In crystalline crust that has undergone intense deformation, the fault and fracture network can follow a fractal distribution with 1D, 2D, and 3D dimensions of approximately 0.8, 1.9, and 2.8, respectively, allowing upscaling between borehole and seismic data [Szalaiov 2015, pp. 1-2, 7-9].
-   A combination of structural tensor analysis and log-Gabor filtering can be used to automatically extract large-scale and middle-scale fracture networks from 3D seismic data in complex crystalline terrains [Szalaiov 2015, pp. 4-5, 5-6].
-   The 3D distribution of fracture density, when interpreted via percolation theory, can provide a statistical estimate of fracture connectivity and a "relative permeability" function suitable as a kernel for permeability inversion [Szalaiov 2015, pp. 11-12, 12-13].
-   Considering only critically stressed fractures (Coulomb criterion with μ ≥ 0.6) significantly reduces the estimated permeable fracture network, aligning with observed low bulk permeability [Szalaiov 2015, pp. 14-15].

## Candidate Concepts
-   [[Fracture network]]
-   [[Fractal dimension]]
-   [[Percolation theory]]
-   [[Relative permeability]]
-   [[Critically stressed fractures]]
-   [[Seismic attribute analysis]]
-   [[Crystalline upper crust]]

## Candidate Methods
-   [[Structural tensor analysis]]
-   [[Log-Gabor filtering]]
-   [[Box-counting method]]
-   [[Percolation theory application]]
-   [[Coulomb failure criterion]]

## Connections To Other Work
-   Builds on previous seismic studies of major faults at KTB by Wiederhold (1992) and Hirschmann (1996b) [Szalaiov 2015, pp. 1-2].
-   Compares with borehole fracture analyses by Hirschmann and Lapp (1994) and Hirschmann et al. (1997) [Szalaiov 2015, pp. 1-2, 13-14].
-   Uses Turcotte's (1997) fractionation model for fractal analysis and percolation theory [Szalaiov 2015, pp. 6-7, 11-12].
-   Validates against induced seismicity data from Bohnhoff et al. (2004) [Szalaiov 2015, pp. 9-11].
-   Method is noted as similar to work at the Kevitsa site, Finland (Koivisto et al., 2012) [Szalaiov 2015, pp. 13-14].
-   Fractal dimension D2=1.9 is consistent with findings of Zimmermann et al. (2003) for the KTB site [Szalaiov 2015, pp. 13-14].

## Open Questions
-   Can the developed automated workflow be successfully applied to other crystalline crust sites with different tectonic histories?
-   How does the inclusion of healed (closed) fractures in the seismic model affect the accuracy of the connectivity and permeability assessment?
-   Can the "relative permeability" kernel function be reliably calibrated and inverted using hydrothermal field experiments at sites with higher permeability than KTB?

## Source Coverage
All 17 non-empty indexed fragments were processed. The compiled source characters (81260) represent a coverage ratio of 1.005444 relative to the indexed characters (80820), indicating full-index coverage.
