---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2012-roy-fractal-analysis-and-thermal-elastic-modeling-of-a-subvolcanic-magmatic-breccia-the-rol"
title: "Fractal Analysis and Thermal-Elastic Modeling of a Subvolcanic Magmatic Breccia: The Role of Post-Fragmentation Partial Melting and Thermal Fracture in Clast Size Distributions."
status: "draft"
source_pdf: "data/papers/Fractal analysis and thermal-elastic modeling of a subvolcanic magmatic breccia The role of post-fragmentation partial melting and thermal fracture in clast size distributions.pdf"
collections:
citation: "Roy, Samuel G., et al. \"Fractal Analysis and Thermal-Elastic Modeling of a Subvolcanic Magmatic Breccia: The Role of Post-Fragmentation Partial Melting and Thermal Fracture in Clast Size Distributions.\" *Geochemistry, Geophysics, Geosystems*, vol. 13, no. 5, 12 May 2012, Q05009. doi:10.1029/2011GC004018. Accessed 12 May 2026."
indexed_texts: "21"
indexed_chars: "100432"
nonempty_source_blocks: "21"
compiled_source_blocks: "21"
compiled_source_chars: "100870"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004361"
coverage_status: "full-index"
source_signature: "2aeadec9c5a7ecef2383f6bf9d377a03357c2bdf"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T00:47:47"
---

# Fractal Analysis and Thermal-Elastic Modeling of a Subvolcanic Magmatic Breccia: The Role of Post-Fragmentation Partial Melting and Thermal Fracture in Clast Size Distributions.

## One-line Summary
This study uses fractal analysis and thermal-elastic modeling to show that the clast size distribution in a subvolcanic magmatic breccia was initially formed by explosion but was subsequently modified by post-fragmentation partial melting and thermal fracture.

## Research Question
The research investigates the mechanisms of breccia formation and the secondary processes that modify clast size and shape distributions in a subvolcanic magmatic breccia, specifically examining the roles of partial melting and thermal fracture [Roy 2012, pp. 1-2].

## Study Area / Data
The study focuses on the Shatter Zone, a concentric magmatic breccia zone along the contact of the Cadillac Mountain Granite intrusion on Mount Desert Island, Maine, USA [Roy 2012, pp. 2-3]. The Shatter Zone is divided into three breccia types (Type 1, 2, and 3) based on fragmentation degree and proximity to the intrusion [Roy 2012, pp. 6-7]. Data were collected from 14 imaged outcrops, yielding 12,732 clasts for analysis [Roy 2012, pp. 7-8].

## Methods
The study employed fractal analysis methods including clast size distribution (CSD), boundary roughness fractal dimension (Dr), and clast circularity analysis [Roy 2012, pp. 6-7]. Thermal-elastic modeling was performed using the finite element method (COMSOL Multiphysics) to simulate conductive heat transfer and thermal stress in clasts immersed in a granitic matrix [Roy 2012, pp. 11-12]. The solidus temperature for the Bar Harbor Formation clasts was calculated using PerpleX [Roy 2012, pp. 14-15].

## Key Findings
- The initial brecciation was caused by a subvolcanic explosion, as indicated by fractal dimensions (Ds > 3) for coarse clast populations [Roy 2012, pp. 10-11].
- Post-fragmentation modification by partial melting and thermal fracture altered the original clast size distributions, boundary roughness, and circularity [Roy 2012, pp. 11-12].
- Partial melting was most effective in Type 3 breccia (adjacent to the intrusion), where small clasts (<1 cm radius) reached supersolidus temperatures within seconds, leading to their disaggregation and a shift from fractal to non-fractal size distributions [Roy 2012, pp. 15-16].
- Thermal fracture preferentially affected angular clasts with high surface-area-to-volume ratios, potentially increasing circularity and further modifying size distributions [Roy 2012, pp. 19-20].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Ds values for coarse clasts (>1.25 cm) in Types 1 and 2 are >3, consistent with explosive brecciation. | [Roy 2012, pp. 8-10] | Analysis of clast size distributions from outcrop images. | Ds values indicate high stress-loading fragmentation mechanism. |
| Circularity increases and boundary roughness (Dr) decreases with proximity to the Cadillac Mountain Granite. | [Roy 2012, pp. 10-11] | Data from 433 clasts across Shatter Zone types. | Suggests post-breccia modification of clast shapes. |
| Thermal modeling shows clasts with radii <1 cm in Type 3 breccia (75% matrix) reach 720°C solidus within 4 seconds. | [Roy 2012, pp. 15-16] | 2D outcrop model with Ti=900°C, Tc=650°C. | Explains rapid disaggregation of small clasts. |
| Thermal stress analysis shows tensile stresses exceeding rock strength in diabase clast corners and interior. | [Roy 2012, pp. 19-20] | 2D clast model with Ti=900°C, Tc=650°C. | Indicates potential for thermal fracture, especially in angular clasts. |
| Type 3 Bar Harbor Formation clast CSD fits an exponential (non-fractal) trend. | [Roy 2012, pp. 8-10] | CSD analysis of 5,675 clasts. | Interpreted as result of extensive partial melting. |

## Limitations
- The thermal-elastic models assume instantaneous immersion of clasts in a superheated matrix and are restricted to conductive heat transfer corrected for latent heat [Roy 2012, pp. 11-12].
- The 3D spherical clast model assumes all clasts experience the same average exposure to magma, which may not capture the proximity effects seen in the 2D outcrop models [Roy 2012, pp. 16-17].
- The thermal fracture model does not account for the dynamic nature of stress during fracture propagation or the anisotropic, heterogeneous nature of the Bar Harbor Formation [Roy 2012, pp. 19-20].

## Assumptions / Conditions
- The spatial gradient in breccia types (1 to 3) represents a temporal evolutionary sequence from initial explosion to advanced modification [Roy 2012, pp. 10-11].
- A single fragmentation-emplacement event occurred in the Shatter Zone [Roy 2012, pp. 14-15].
- The area of a clast that achieved supersolidus temperatures was eventually disaggregated and dispersed by matrix magma flow and chemical diffusion [Roy 2012, pp. 11-12].
- The solidus temperature for the Bar Harbor Formation is approximately 720°C [Roy 2012, pp. 14-15].

## Key Variables / Parameters
- **Fractal Dimension (Ds):** Measures clast size distribution; Ds > 2.5 indicates explosive fragmentation [Roy 2012, pp. 3-4].
- **Boundary Roughness Fractal Dimension (Dr):** Measures clast boundary complexity; decreases with modification [Roy 2012, pp. 6-7].
- **Circularity (C):** Measures clast compactness; increases with modification [Roy 2012, pp. 6-7].
- **Temperatures:** Intrusion (Ti), Clast (Tc), Solidus (Tsolidus) [Roy 2012, pp. 14-15].
- **Thermal Properties:** Thermal conductivity (k), density (ρ), specific heat (Cp), latent heat (L) [Roy 2012, pp. 14-15].
- **Matrix Volume Percentage:** Varies from ~16% (Type 1) to ~75% (Type 3) [Roy 2012, pp. 7-8].

## Reusable Claims
- In a subvolcanic magmatic breccia, fractal dimensions (Ds) greater than 3 for coarse clast populations are indicative of an explosive fragmentation mechanism [Roy 2012, pp. 10-11].
- Post-fragmentation partial melting in a superheated magma matrix can effectively modify clast size distributions by preferentially disaggregating small clasts, leading to a shift from fractal to non-fractal trends [Roy 2012, pp. 15-16].
- Thermal fracture induced by rapid heating can occur in angular clasts with high surface-area-to-volume ratios, potentially producing new clasts and increasing circularity [Roy 2012, pp. 19-20].
- The spatial gradient in breccia development (from clast-supported to matrix-supported) can be interpreted as a temporal evolutionary sequence driven by thermal processes [Roy 2012, pp. 10-11].

## Candidate Concepts
- [[Fractal dimension]]
- [[Clast size distribution]]
- [[Magmatic breccia]]
- [[Partial melting]]
- [[Thermal fracture]]
- [[Subvolcanic system]]
- [[Contact metamorphism]]
- [[Explosive volcanism]]

## Candidate Methods
- [[Fractal analysis]]
- [[Thermal-elastic modeling]]
- [[Finite element method]]
- [[Clast circularity analysis]]
- [[Boundary roughness analysis]]
- [[Image analysis (NIH ImageJ)]]

## Connections To Other Work
- The study builds on fractal analysis methods applied to breccias in various settings, including abrasive, hydraulic, and explosive breccias [Roy 2012, pp. 3-4].
- It connects to research on thermal processes in magmatic systems, such as partial melting of xenoliths and thermal cracking [Roy 2012, pp. 11-12].
- The work references studies on the Cadillac Mountain intrusive complex and the Coastal Maine Magmatic Province [Roy 2012, pp. 2-3].

## Open Questions
- How do anisotropic and heterogeneous properties of wall rocks (like the Bar Harbor Formation) affect the actual patterns of thermal fracture and partial melting?
- What is the precise quantitative contribution of thermal fracture versus partial melting to the final clast size distribution in different breccia types?
- Can the spatial-temporal evolutionary sequence inferred for the Shatter Zone be confirmed with absolute dating methods?

## Source Coverage
All 21 non-empty indexed fragments were processed. The compiled source blocks total 21, with a compiled character count of 100,870. The coverage ratio by blocks is 1.0, and by characters is 1.004361, indicating full-index coverage.
