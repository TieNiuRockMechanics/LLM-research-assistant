---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2013-kruhl-fractal-geometry-techniques-in-the-quantification-of-complex-rock-structures-a-specia"
title: "Fractal-Geometry Techniques in the Quantification of Complex Rock Structures: A Special View on Scaling Regimes, Inhomogeneity and Anisotropy."
status: "draft"
source_pdf: "data/papers/2013 - Fractal-geometry techniques in the quantification of complex rock structures A special view on scaling regimes, inhomogeneity and anisotropy.pdf"
collections:
citation: "Kruhl, Jörn H. “Fractal-Geometry Techniques in the Quantification of Complex Rock Structures: A Special View on Scaling Regimes, Inhomogeneity and Anisotropy.” *Journal of Structural Geology*, vol. 46, 2013, pp. 2-21, https://doi.org/10.1016/j.jsg.2012.10.002."
indexed_texts: "32"
indexed_chars: "157197"
nonempty_source_blocks: "32"
compiled_source_blocks: "32"
compiled_source_chars: "157930"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004663"
coverage_status: "full-index"
source_signature: "2ea1d4d044a45cb5d95f7bd9874490fbae996278"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T15:01:45"
---

# Fractal-Geometry Techniques in the Quantification of Complex Rock Structures: A Special View on Scaling Regimes, Inhomogeneity and Anisotropy.

## One-line Summary
A review presenting classical and newly developed fractal‑geometry methods to quantify scaling regimes, inhomogeneity, and anisotropy in complex rock structures, discussing their advantages, limitations, and correlations with rock properties and structure‑forming processes.

## Research Question
How can fractal‑geometry techniques be extended beyond simple power‑law description to systematically capture **different scaling behaviour on different scales**, **spatial inhomogeneity**, and **directional anisotropy** of complex rock patterns, and what do these quantifications reveal about material properties and the underlying geological processes?

## Study Area / Data
This is a review article; no single field area is used. The data are **binary patterns extracted from rock structures** (fractures, faults, veins, grain boundaries, crystal distributions, etc.) documented in the literature, covering micrometre to kilometre scales. Sources include outcrop photographs, thin‑section scans, geological maps, and satellite imagery. The paper synthesises evidence from 109 publications (1983‑2012) with 123 double‑logarithmic diagrams [Kruhl 2013, pp. 6-7].

## Methods
The paper reviews and extends the following quantitative techniques (most requiring transformation of the rock structure into a binary pattern):
- **Classical fractal‑geometry methods**: Box Counting (2D), Cantor‑Dust / Spacing‑Population / Interval‑Counting (1D for planar structures), Structured‑Walk (Divider) Method, Area‑Perimeter Method, Mass‑Dimension Method, Correlation‑Dimension Method, and Euclidean‑Distance Mapping [Kruhl 2013, pp. 7-9].
- **Scaling regime detection**: identification of separate linear segments in log‑log plots, often limited by “roll‑off” (undersampling at small scales, censoring at large scales) [Kruhl 2013, pp. 5-6].
- **Inhomogeneity quantification**: Map Counting (gliding‑window Box Counting) producing contour or pixel maps of local fractal dimension [Kruhl 2013, pp. 10-11]; also automated Map Counting (high‑resolution) [Kruhl 2013, pp. 11-13].
- **Anisotropy quantification**: application of 1D fractal methods (modified Cantor‑Dust, Directional Structured‑Walk) along many azimuths (10° down to 1° steps); results are often fitted as an ellipse but can show complex non‑elliptical distributions [Kruhl 2013, pp. 11-13]; the Angle Distribution of Percolation Length method is also mentioned [Kruhl 2013, pp. 11-12].
- **Combined inhomogeneity‑anisotropy**: MORFA (Mapping of Rock Fabric Anisotropy) – a gliding‑window application of the modified Cantor‑Dust method yielding maps of anisotropy intensity and direction [Kruhl 2013, pp. 13-14].
- **Multifractal analysis**: for patterns where a single fractal dimension is insufficient, used e.g. on fracture systems, ore grades, earthquake distributions [Kruhl 2013, pp. 8-9, 14‑15].
- **3D approaches**: mainly extrapolating 2D fractality (add 1 to D), but true 3D Box Counting and serial section analysis are discussed; cautioned for inhomogeneous/anisotropic structures [Kruhl 2013, pp. 9-10].
- **Automated recording**: watershed segmentation, CASRG algorithm, neural‑network‑assisted mineral identification, and computer‑aided microscopy to produce large, high‑resolution binary patterns [Kruhl 2013, pp. 3-4].

## Key Findings
1. Fractal‑geometry techniques provide a quantitative language for the “ill‑defined geometries” of natural rock structures, bridging nature, experiment and modelling [Kruhl 2013, pp. 15-16].
2. Rock patterns typically exhibit **different scaling behaviour on different scales** (scaling regimes), **inhomogeneity** (spatial variation of fractal dimension), and **anisotropy** (direction‑dependent complexity) – all geologically informative [Kruhl 2013, pp. 15-16].
3. Interpolation (filling gaps) and extrapolation across scales are possible **only if** the pattern is homogeneous and shows the same fractality over the entire range; these preconditions are often unfulfilled [Kruhl 2013, pp. 15-16].
4. Fluctuations in fractal measurements (e.g. cyclic steps in log‑log plots) can indicate **pattern regularity** and may reflect variations or interactions of pattern‑forming processes, not mere inaccuracies [Kruhl 2013, pp. 15-16].
5. Future development is needed in: (i) new methods for anisotropy and inhomogeneity, (ii) 3D quantification, (iii) further automation for large‑scale high‑resolution patterns, and (iv) integrated studies linking natural structures, experiments, and simulations [Kruhl 2013, pp. 16-16].

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Frequency distribution of fractal intervals from 109 publications: most natural structures show fractality over only 1‑2 orders of magnitude; rare cases extend to 6‑7 orders. | [Kruhl 2013, pp. 6-7] (Fig. 5) | Survey of 123 log‑log diagrams (1983‑2012) | Intervals <1 order of magnitude are acceptable only with strict methodology. |
| The “roll‑off” effect at small scales is caused by incomplete recording (truncation) or by a transition to Euclidean geometry (e.g., straight crystal faces). At large scales, low‑number statistics (censoring) scatters data. | [Kruhl 2013, pp. 5-6] (Fig. 3) | Censoring and truncation are common in field‑based fracture maps; thin‑section studies (100% outcrop) usually lack truncation. | Roll‑off defines the upper and lower limits of valid fractal scaling. |
| Pattern regularity (e.g., triadic Koch curve) produces cyclic steps in log‑log plots; those steps disappear as randomness increases. | [Kruhl 2013, pp. 5-6] (Fig. 4) | Observed with the Structured‑Walk Method on regular vs. irregular Koch islands. | Such deviations can be used to quantify pattern regularity. |
| Map Counting (gliding‑window Box Counting) applied to a 2.5 × 2.5 m syenite mineral distribution pattern, with 10 cm window and 5 mm steps, produced a colour map of fractal dimension variation across 254,400 measurements. | [Kruhl 2013, pp. 10-11] (Fig. 8) | Automated high‑resolution recording is a prerequisite; window must be large enough for statistics. | Inhomogeneity mapping reveals flow structures not visible in the field. |
| Anisotropy of a fracture pattern measured by automated modified Cantor‑Dust method (1° azimuthal steps) yields a point distribution that cannot be well fitted by an ellipse; analysis of complementary pattern (rock fragments vs. fractures) gives similar ellipticity but different scatter. | [Kruhl 2013, pp. 12-13] (Fig. 11) | Requires high‑resolution pattern and many scan‑lines. Both pattern and background should be quantified. | The geometry of the data‑point distribution represents the azimuthal scaling behaviour, not simple strain. |
| Combined inhomogeneity‑anisotropy mapping (MORFA) on a syenite pattern (circle of 20 cm diameter shifted in 5 cm steps, 1804 measurements) produced a pixel map of anisotropy intensity (1 to ~1.7) with directions of lowest fractal dimension aligned with long grain axes. | [Kruhl 2013, pp. 13-14] (Fig. 12) | Large, highly resolved patterns needed; method detects diffuse magmatic shear structures. | Provides information unobtainable by single methods. |
| Particle size distributions in fault rocks show fractal dimensions of ~1.97 (pillar‑of‑strength model), ~2.58 (constrained comminution), and ~2.84 (plane‑of‑fragility), reflecting different fragmentation processes. | [Kruhl 2013, pp. 14-15] | Derived from literature review; references to Allègre et al. (1982), Sammis et al. (1987), Turcotte (1986a). | Log‑normal size distributions may appear under extensional stress. |
| Fractal analysis of sutured quartz grain boundaries can serve as a geothermometer (temperature and strain rate of metamorphism). | [Kruhl 2013, pp. 14-15] | Based on Kruhl and Nega (1996), Takahashi et al. (1998). | Applicable to dynamically recrystallized quartz. |

## Limitations
- **Scale range**: Most natural structures are fractal over only 1‑2 orders of magnitude; some intervals are <1 order, requiring strict methodology [Kruhl 2013, pp. 6-7].
- **Incomplete recording**: Gaps in outcrop (e.g., lichen cover, precipitation) and manual simplification introduce bias; incomplete structures are often used without discussion [Kruhl 2013, pp. 2-3].
- **Binary transformation**: Manual or automated thresholding can distort pattern complexity; wrong mineral classification introduces larger errors than boundary shifts [Kruhl 2013, pp. 3-3].
- **2D extrapolation to 3D**: Assumes homogeneity and isotropy, which are rarely met; no established 3D anisotropy quantification exists [Kruhl 2013, pp. 9-10].
- **Method sensitivity**: Different fractal methods yield different dimensions for the same pattern; box‑counting can be applied to patterns that are not suitable (e.g., simple geometries) [Kruhl 2013, pp. 4-5, 8‑9].
- **Data‑analysis subjectivity**: Visual definition of scaling regimes, short measurement ranges, small data sets, and black‑box software are common pitfalls [Kruhl 2013, pp. 4-5].

## Assumptions / Conditions
- The rock structure can be adequately represented as a **binary pattern**; colour, composition, and crystallographic data are not considered [Kruhl 2013, pp. 1-2].
- Complex patterns consist of **simple, similar, clearly smaller parts** that are repeated in a diffuse way over some range of scales [Kruhl 2013, pp. 2-3].
- A power‑law relationship (N ∼ s⁻ᴰ) is assumed over the scaling interval; deviations are used to detect scaling regimes, regularities, or limits [Kruhl 2013, pp. 5-5].
- For interpolation (gap filling) or extrapolation, the pattern must be **homogeneous** and show the **same fractality** across the entire range [Kruhl 2013, pp. 3-3, 15‑16].
- Anisotropy analysis by scan‑line methods assumes a **circular analysis area** to avoid bias from unequal scan‑line lengths; the pattern should be homogeneous within that circle [Kruhl 2013, pp. 12-13].

## Key Variables / Parameters
- **Fractal dimension D** (box‑counting, Cantor‑dust, structured‑walk, etc.) – the exponent characterising complexity.
- **Scaling regimes** and **thresholds between regimes** – changes in slope in log‑log plots.
- **Upper and lower limits of fractality** (roll‑off points) – determined by censoring, truncation, or Euclidean geometry onset.
- **Inhomogeneity**: spatial variation of D, rendered as contour or pixel maps from gliding‑window methods.
- **Anisotropy of fractal dimension**: azimuthal distribution of D, often summarized by an ellipse with axial ratio (AAD) and orientation, or studied in full directional pattern.
- **Multifractal spectrum** – when a single D does not capture the whole pattern.
- **Window size, step size, scan‑line spacing, number of azimuths** – control resolution and statistical significance of inhomogeneity/anisotropy maps.

## Reusable Claims
- **Method applicability**: “Fractal geometry methods are only applicable to the quantification of complex structures. They fail in quantifying simple structures or yield results that appear useful but are meaningless.” [Kruhl 2013, pp. 4-5] (Condition: pattern must be complex and extend over a range of scales.)
- **Roll‑off interpretation**: “The ‘roll‑off’ effect is related to large objects with low numbers (‘censoring’) … and to incomplete recording of small parts of the structure (‘truncation’).” [Kruhl 2013, pp. 5-6] (Condition: applies to many field‑measured fracture patterns; thin‑section studies may lack truncation.)
- **Scaling regimes**: “Different fractality on different scales is standard, not the exception … The thresholds between scaling regimes represent thresholds between different pattern‑forming processes.” [Kruhl 2013, pp. 9-10] (Condition: when the pre‑existing fabric/composition varies with scale.)
- **Inhomogeneity quantification**: “Map Counting … typically provides a contour map or a pixel map with colour or grey‑scale shading.” [Kruhl 2013, pp. 10-11] (Condition: requires large, highly resolved patterns; window size must balance statistics vs. spatial detail.)
- **Anisotropy characterisation**: “The geometry of the data‑point distribution … represents the anisotropy of structure complexity or, in other words, the directional scaling behaviour of the structure.” [Kruhl 2013, pp. 12-13] (Condition: analysis within a circular area, many azimuths, and equal scan‑line coverage.)
- **Complementary quantification**: “Since the two complementary parts of a ‘complete’ pattern have independent geological meaning, quantifying both of them is advisable.” [Kruhl 2013, pp. 12-13] (e.g., fracture lines vs. rock fragments.)
- **Grain boundary geothermometry**: “The fractal shape of sutured quartz grain boundaries … application as a geothermometer.” [Kruhl 2013, pp. 15-16] (Condition: dynamically recrystallized quartz, calibrated against temperature and strain rate.)
- **Fragmentation models**: “Particle size distributions in fault rocks show variation of fractal dimensions … ~1.97 → ‘pillar of strength’, ~2.58 → ‘constrained comminution’, ~2.84 → ‘plane of fragility’.” [Kruhl 2013, pp. 14-15] (Condition: fractal fragmentation; log‑normal may occur under extension.)
- **Interpolation/extrapolation warning**: “Extrapolation … only works if the structure (i) is homogeneous and (ii) shows the same scaling behaviour over the entire range of scale. In many cases these conditions are not fulfilled.” [Kruhl 2013, pp. 4-5].
- **Automated pattern preparation risk**: “If single crystals are wrongly classified, the pattern’s complexity is more strongly changed than by inaccuracies … during recording of the crystals’ boundaries.” [Kruhl 2013, pp. 3-3] (Condition: automated mineral classification vs. manual boundary drawing.)

## Candidate Concepts
- [[scaling regimes]]
- [[pattern inhomogeneity]]
- [[pattern anisotropy]]
- [[fractal dimension]]
- [[self‑similarity]]
- [[self‑affine]]
- [[roll‑off effect]]
- [[truncation]]
- [[censoring]]
- [[textural vs structural fractality]]
- [[constrained comminution]]
- [[pillar of strength model]]
- [[plane of fragility model]]
- [[multifractals]]
- [[self‑organized criticality]]
- [[binary pattern]]
- [[pattern regularity]]
- [[Cantor set]]
- [[percolation length]]

## Candidate Methods
- [[Box Counting]]
- [[Cantor‑Dust Method]]
- [[Spacing‑Population Technique]]
- [[Interval‑Counting Technique]]
- [[Structured‑Walk Method]]
- [[Divider Method]]
- [[Area‑Perimeter Method]]
- [[Mass‑Dimension Method]]
- [[Density‑Dimension Method]]
- [[Correlation‑Dimension Method]]
- [[Euclidean‑Distance Mapping]]
- [[Map Counting]]
- [[Automated Map Counting]]
- [[Directional Structured‑Walk Method]]
- [[MORFA (Mapping of Rock Fabric Anisotropy)]]
- [[Angle Distribution of Percolation Length]]
- [[Multifractal analysis]]
- [[3D Box Counting]]
- [[gliding‑window (kriging) procedure]]

## Connections To Other Work
- Foundational fractal‑geometry texts: Mandelbrot (1967, 1977, 1982), Kaye (1989, 1993), Feder (1988), Falconer (1990), Turcotte (1997) – cited throughout.
- **Fracture and fault scaling**: Bonnet et al. (2001), Castaing et al. (1996), Nicol et al. (1996), Walsh & Watterson (1993), and many others – provide examples of scaling regimes and anisotropy.
- **Particle fragmentation**: Blenkinsop (1991), Sammis et al. (1987), Korvin (1989), Billi & Storti (2004), Şu̧teanu et al. (2000) – link size distributions to fragmentation processes.
- **Vein systems**: Gillespie et al. (1999, 2001), Johnston & McCaffrey (1996), Kruhl (1994) – power‑law and log‑normal thickness distributions.
- **Grain‑boundary and fabric analysis**: Kruhl & Nega (1996), Takahashi et al. (1998), Peternell & Kruhl (2009), Peternell et al. (2010, 2011) – methods for inhomogeneity and anisotropy of magmatic/metamorphic fabrics.
- **Earthquake and seismicity patterns**: Turcotte (1986b), Smalley et al. (1987), Hirata & Imoto (1991), Kagan (2010) – multifractal and spatial clustering analyses.
- **Ore deposit and permeability applications**: Blenkinsop (1994, 1995), Ford & Blenkinsop (2008a, 2009), Ledésert et al. (2010) – fractal analysis of mineralisation, fluid flow, and reservoir properties.

## Open Questions
- What controls the remarkable self‑similarity of fracture patterns over many orders of magnitude (mm to 10 km) in some settings, while most structures show multiple scaling regimes? [Kruhl 2013, pp. 9-10]
- How can 3D anisotropy of complex rock fabrics be directly quantified by fractal‑geometry methods, rather than pieced together from 2D sections? [Kruhl 2013, pp. 9-10, 15‑16]
- To what extent do the “second‑order” fractal dimensions (fractality of anisotropy/inhomogeneity maps) capture geologically meaningful information, and when does condensing them into a single number lose essential details? [Kruhl 2013, pp. 13-14]
- Can the systematic deviations from strict power‑law (cyclic stepping) be reliably used as a **pattern regularity meter**, and what processes produce such regularities in natural deformation patterns? [Kruhl 2013, pp. 5-6]
- What are the quantitative relationships between the thresholds of scaling regimes and the mechanical/lithological layering of the crust? [Kruhl 2013, pp. 9-10]
- How can the automated recording and binary coding methods be made robust enough to handle the fuzziness and incompleteness of natural structures without introducing systematic bias? [Kruhl 2013, pp. 3-4]

## Source Coverage
All 32 non‑empty indexed fragments from the paper were processed.  
Indexed characters: 157,197  
Compiled characters: 157,930  
Coverage ratio by blocks: 1.0  
Coverage ratio by chars: 1.004663  
Source signature: `2ea1d4d044a45cb5d95f7bd9874490fbae996278`  
Coverage status: full‑index.
