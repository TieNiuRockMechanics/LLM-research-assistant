---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2008-baker-automatic-detection-of-anisotropic-features-on-rock-surfaces"
title: "Automatic Detection of Anisotropic Features on Rock Surfaces."
status: "draft"
source_pdf: "data/papers/Automatic detection of anisotropic features on rock surfaces.pdf"
collections:
citation: "Baker, Bodey R., et al. \"Automatic Detection of Anisotropic Features on Rock Surfaces.\" *Geosphere*, vol. 4, no. 2, 2008, pp. 418-28. doi:10.1130/GES00145.1."
indexed_texts: "10"
indexed_chars: "45861"
nonempty_source_blocks: "10"
compiled_source_blocks: "10"
compiled_source_chars: "45411"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.990188"
coverage_status: "full-index"
source_signature: "da5cab5b4aaf521d262598d87d46747067f1d9c0"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T00:48:17"
---

# Automatic Detection of Anisotropic Features on Rock Surfaces.

## One-line Summary
An automatic technique based on fractal analysis is developed to detect and quantify anisotropic roughness features on rock surfaces from digital point cloud data.

## Research Question
How can anisotropic features on rock surfaces be automatically detected and characterized from digitally acquired data sets?

## Study Area / Data
The method is applied to synthetic surfaces and to digitally mapped point clouds of natural rock surfaces from four field examples: (1) Permian sandstones with brittle shear zones at Cullercoats, northeast England (55°2'1.43"N; 1°25'53.90"W); (2) the footwall surface of the neotectonic Yavansu fault near Kuşadası, Turkey (37°49'29"N; 27°15'57"E); (3) Proterozoic Heavitree quartzite with spaced fractures at Ormiston Gorge, central Australia (23°37'38"S; 132°43'38"E); and (4) Devonian Taunus quartzite in an aggregate quarry at Trechtingshausen, Germany (50°01'00"N; 7°49'45"E) [Baker 2008, pp. 4-5, 5-8, 8-10].

## Methods
The workflow involves: 1) Transforming the point cloud using principal components analysis (PCA) to align the surface normal with the z-axis and the direction of maximum variance with the x-axis. 2) For each of R rotations about the z-axis, sampling N parallel profiles perpendicular to the plane of best fit. 3) Calculating the fractal dimension (a measure of roughness) for each profile using the compass walking technique. 4) Computing the mean roughness and its variance for each orientation. 5) Calculating surface anisotropy (a) as the roundness of the polar plot (0 < a < 1, where 1 is isotropic). 6) Identifying directions of maximum (R_max) and minimum roughness by applying a moving average to the smoothed roughness vs. orientation data [Baker 2008, pp. 2-4, 4-4].

## Key Findings
- The method can accurately determine the direction of maximum roughness (R_max) and roughness isotropy, but these values are strongly dependent on the choice of an appropriate compass length range relative to the scale of the surface feature [Baker 2008, pp. 4-4].
- Analysis of natural examples suggests a significant change in roughness value, anisotropy, and anisotropy direction can exist across different scales of observation, supporting a self-affine rather than self-similar fractal geometry for rock surfaces [Baker 2008, pp. 8-10].
- For the Cullercoats sandstone, large-scale roughness was dominated by conjugate shear zones, while smaller-scale roughness was influenced by sedimentary bedding [Baker 2008, pp. 4-5].
- For the Yavansu fault surface, large-scale roughness was dominated by comb fractures perpendicular to slip, contrary to some previous studies that found surfaces smoothest parallel to slip [Baker 2008, pp. 5-8].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| Synthetic surface with wavelength 1 unit, amplitude 0.15 units, oriented at 0°. Analyzed with CLR 0.64–0.11, R_max detected at 0°, a=0.26. | [Baker 2008, pp. 4-4] | Compass length range (CLR) 0.64–0.11. | Correct detection of orientation and high anisotropy. |
| Same synthetic surface analyzed with CLR 0.11–0.02, R_max detected at 38.1°, a=0.71. | [Baker 2008, pp. 4-4] | CLR 0.11–0.02. | Incorrect detection; compass range too small for the feature scale. |
| Cullercoats sandstone: Large-scale analysis (CLR 2 cm–3.35 mm) detected high roughness at 30° and 156°, a=0.83. | [Baker 2008, pp. 4-5] | CLR 2 cm–3.35 mm. | Roughness orientations perpendicular to brittle shear zones. |
| Cullercoats sandstone: Small-scale analysis (CLR 3.5–0.06 mm) detected R_max at 45°, a=0.80. | [Baker 2008, pp. 4-5] | CLR 3.5–0.06 mm. | Dominated by smaller-scale features like bedding. |
| Yavansu fault: Large-scale analysis (CLR 64–11 cm) detected R_max at 60°, a=0.69. | [Baker 2008, pp. 5-8] | CLR 64–11 cm. | Roughness dominated by comb fractures perpendicular to slip. |
| Yavansu fault: Small-scale analysis (CLR 11–2 cm) detected R_max at 51°, a=0.84. | [Baker 2008, pp. 5-8] | CLR 11–2 cm. | Less coherent plot, possibly including excavation marks. |

## Limitations
- The accuracy of R_max and anisotropy detection is strongly dependent on selecting a compass length range appropriate for the scale of the surface feature of interest [Baker 2008, pp. 4-4].
- The precision of the point cloud, determined by the photogrammetry workflow (camera resolution, accuracy of surveyed points), limits the minimum usable compass length [Baker 2008, pp. 8-10].
- The method analyzes roughness along 1D profiles; extending it to 3D closed surfaces requires further development [Baker 2008, pp. 8-10].
- The maximum compass length is chosen arbitrarily as ~1/20 of the diagonal length of the 3D model [Baker 2008, pp. 8-10].

## Assumptions / Conditions
- Rock surface roughness is a self-affine fractal feature, meaning its statistical properties are retained on different scales in different directions [Baker 2008, pp. 1-1].
- The sampled parallel profiles are representative of the surface's roughness in a given orientation [Baker 2008, pp. 2-4].
- The compass walking technique provides a reliable measure of fractal dimension for the profile data [Baker 2008, pp. 2-4].

## Key Variables / Parameters
- **Compass Length Range (CLR):** The range of step sizes used in the compass walking fractal dimension calculation. Critical for isolating features at specific scales [Baker 2008, pp. 4-4, 8-10].
- **Anisotropy (a):** A measure of the roundness of the roughness polar plot, where 0 < a < 1 and 1 represents a perfectly isotropic (circular) surface [Baker 2008, pp. 4-4].
- **R_max:** The orientation (theta) of maximum roughness detected by the analysis [Baker 2008, pp. 4-4].
- **Number of profiles (N):** The number of parallel profiles sampled for each orientation [Baker 2008, pp. 2-4].
- **Number of rotations (R):** The number of different orientations at which profiles are sampled [Baker 2008, pp. 2-4].

## Reusable Claims
- The direction of maximum roughness (R_max) and surface anisotropy can be automatically detected from 3D point cloud data using a fractal analysis method based on profile sampling and the compass walking technique [Baker 2008, pp. 2-4, 4-4].
- The detected roughness anisotropy is scale-dependent; different compass length ranges can isolate features of different wavelengths, such as fault corrugations versus fracture traces [Baker 2008, pp. 4-5, 5-8].
- The method allows for the comparison of surface anisotropy across scales and the isolation of rock surface features within a specific range of wavelengths through careful selection of compass lengths [Baker 2008, pp. 1-2].

## Candidate Concepts
- [[Surface roughness]]
- [[Anisotropy]]
- [[Fractal analysis]]
- [[Self-affine fractal]]
- [[Fault surface morphology]]
- [[Deformation bands]]
- [[Joint Roughness Coefficient (JRC)]]

## Candidate Methods
- [[Compass walking technique]]
- [[Principal components analysis (PCA)]]
- [[Fractal dimension calculation]]
- [[Digital photogrammetry]]
- [[Point cloud analysis]]
- [[Polar plot visualization]]

## Connections To Other Work
- The method is similar to those of Renard et al. (2006) and Thomas et al. (1999) in analyzing surface anisotropy, but differs in using fractal analysis [Baker 2008, pp. 1-2].
- Findings on the Yavansu fault contrast with studies by Power and Tullis (1991) and Sagy et al. (2007), who found fault surfaces smoothest parallel to slip [Baker 2008, pp. 5-8].
- The work builds on the premise that digital mapping techniques (e.g., Lidar, photogrammetry) facilitate data acquisition for geoscience, as noted by McCaffrey et al. (2005) [Baker 2008, pp. 1-2].
- The analysis of self-affine properties relates to work by Kulatilake and Um (1999) and Brown and Scholz (1985) [Baker 2008, pp. 1-1, 8-10].

## Open Questions
- How can the method be extended to systematically study roughness variations spatially across subdomains of a rock face? [Baker 2008, pp. 8-10]
- Can Fourier series and wavelet analysis techniques be integrated to calculate industry standards like the Joint Roughness Coefficient (JRC)? [Baker 2008, pp. 8-10]
- How can the method be applied to the surface analysis of geometrical objects with closed surfaces in three dimensions? [Baker 2008, pp. 8-10]

## Source Coverage
All 10 non-empty indexed fragments were processed. The compiled source blocks total 10, with 45,411 characters compiled from 45,861 indexed characters, resulting in a coverage ratio by characters of 0.990188. The coverage status is full-index.
