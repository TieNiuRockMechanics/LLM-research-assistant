---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2010-zhang-the-planar-shape-of-rock-joints"
title: "The Planar Shape of Rock Joints."
status: "draft"
source_pdf: "data/papers/2010 - The Planar Shape of Rock Joints.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Zhang, Lianyang, and Herbert H. Einstein. \"The Planar Shape of Rock Joints.\" *Rock Mechanics and Rock Engineering*, vol. 43, 2010, pp. 55-68. doi:10.1007/s00603-009-0054-0."
indexed_texts: "12"
indexed_chars: "55528"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "55756"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004106"
coverage_status: "full-index"
source_signature: "0df5bf33e16c45fd79c20befe0e6734bec39650b"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T14:13:29"
---

# The Planar Shape of Rock Joints.

## One-line Summary
This paper presents a review of rock joint planar shapes and a stereological analysis showing that elliptical (rarely circular) shapes are typical for unrestricted joints, while rectangular shapes occur when joints are bounded by geological structures; it also provides methods to characterize joint shape and size from trace length data, highlighting that equal mean trace lengths on two sampling planes can be misleading for inferring equidimensional joints.

## Research Question
What is the planar shape of rock joints, and how can it be reliably inferred and characterized from available trace length observations considering geological constraints and sampling plane orientation effects?

## Study Area / Data
The study synthesizes field observations, experimental data, and previously published trace-length datasets rather than collecting new primary field data. Specific sources include:
- **Woodworth (1896)**: joints in Cambridge Argillite (pelite), sizes ~200 mm, with circular/elliptical discoid joints 13–50 mm diameter. *Source: [Zhang 2010, pp. 2-3]*
- **Bankwitz (1965, 1966)**: metamorphic lithologies (schists, quartzite) and igneous intrusions (diabase, granite) in the Thüringer Schiefergebirge. Described elliptical (ideally circular) fractures and fractures with linear boundaries where terminated by other structures. *Source: [Zhang 2010, pp. 3-4]*
- **Bahat et al. (2003)**: Borsov granite, South Bohemian Pluton; ten exposed joints showing elliptical mirror planes. *Source: [Zhang 2010, pp. 4, 6]*
- **Petit et al. (1994)**: Permian sandstones of the Lodève basin, France; pelites with isolated ellipses (L/H ≈ 1.9), sandstone layers with rectangular joints L/H > 4–5. *Source: [Zhang 2010, pp. 4-6]*
- **Weinberger (2001)**: dolomite layers of the Judea Group, Israel; elliptical fractures from cavities and semi-elliptical from bedding initiation. *Source: [Zhang 2010, pp. 3-4]*
- **Savalli and Engelder (2005)**: layered clastic rocks; circular/elliptical rupture shapes in early growth, transitioning to elliptical or rectangular after intersecting bed boundaries. *Source: [Zhang 2010, pp. 4-5]*
- **Grimsel area, Switzerland**: granitic sheet jointing, exposed both restricted (rectangular) and unrestricted (elliptical) joints. *Source: [Zhang 2010, pp. 5-6]*
- **Locsin (2005) / Becker & Gross (1996) / Saltzman (2001) / Gross et al. (1997) / Baudo (2001)**: layer-perpendicular joints in limestone/dolostone (Geroﬁt Fm.), chalk/chert, sandstone/shale; essentially rectangular with height equal to bed thickness. *Source: [Zhang 2010, pp. 6-7]*
- **Robertson (1970)**: ~9,000 traces from De Beer mine, South Africa; strike and dip trace lengths similar. *Source: [Zhang 2010, pp. 7]*
- **Barton (1977)**: C.S.A. Mine, Cobar, NSW, Australia; chloritic/quartzitic siltstone; joints approximately equidimensional based on wall photographs. *Source: [Zhang 2010, pp. 7]*
- **Einstein et al. (1979)**: southern Connecticut, Monson gneiss; strike and dip trace lengths differed (Table 1), indicating non-equidimensional joints. *Source: [Zhang 2010, pp. 7]*
- **Experimental data**: Daneshy (1973) hydrostone/limestone – point source yields circular, line source yields elliptical shapes; Moriya et al. (2006) Bernburg salt mine – acoustic emission source distributions are elliptical. *Source: [Zhang 2010, pp. 7-8]*

## Methods
1. **Literature review and classification**: Joints are classified as *unrestricted* (growth not limited by adjacent structures; typically elliptical or approximately circular) and *restricted* (bounded by bedding, pre-existing fractures; typically rectangular or polygonal). *[Zhang 2010, pp. 1-2]*
2. **Stereological analysis**: The general relationship between trace length distribution \( f(l) \) and joint size distribution \( g(a) \) (major axis length \( a \) of an ellipse) for area sampling from Zhang et al. (2002) is used:
   \[
   f(l) = \frac{l}{M \mu_a} \int_{l/M}^{\infty} \frac{g(a)}{\sqrt{(Ma)^2 - l^2}} da, \quad l \ge 0, a \ge M
   \]
   where factor \( M = \frac{\sqrt{\tan^2\beta + 1}}{\sqrt{k^2\tan^2\beta + 1}} \), \( k = a/b \) aspect ratio, \( \beta \) angle between joint major axis and trace line in the joint plane. *[Zhang 2010, pp. 8-9]*
3. **Derived statistics**: For lognormal, negative exponential, and Gamma distributions of \( a \), explicit formulas for mean \( \mu_l \) and standard deviation \( \sigma_l \) of trace lengths are given in Table 2. *[Zhang 2010, pp. 9-10]*
4. **Sensitivity to sampling plane**: Variation of \( \mu_l \) and \( \sigma_l \) with \( \beta \) is plotted for different \( k \) values (Fig. 13). *[Zhang 2010, pp. 9-12]*
5. **Characterization procedures**:
   - **Elliptical joints**: Follow Zhang et al. (2002) – from trace data on multiple sampling windows, assume major axis orientation, compute \( \beta \), then for different \( k \) and distribution forms derive \( \mu_a, \sigma_a \) curves for each window; the correct orientation is where curves intersect at a single point. *[Zhang 2010, pp. 12-13]*
   - **Rectangular joints**: Three methods:
     *Method 1*: Direct measurement of traces on exposed bedding surfaces.
     *Method 2*: Use stereological relationship for parallelograms (Warburton 1980b) with orientation defined by angle between rectangle side and trace line.
     *Method 3*: Approximate rectangles as ellipses of same area and aspect ratio; overlap area ratio \( A_c/A_t = 0.91 \) (Eq. 8), making elliptical characterization adequate. *[Zhang 2010, pp. 12-13]*
6. **Two-step general approach**: (a) Evaluate geologic setting to hypothesize shape (elliptical vs. rectangular); (b) apply the appropriate trace-based characterization. *[Zhang 2010, pp. 11-12]*

## Key Findings
1. **Typical joint shapes**:
   - Unrestricted joints (not bounded by bedding or pre-existing fractures) tend to be **elliptical**, with circular shapes occurring rarely as a special case (Woodworth 1896, Bankwitz 1965, Hodgson 1961, Weinberger 2001, Bahat et al. 2003, Savalli & Engelder 2005). *[Zhang 2010, pp. 2-5]*
   - Restricted joints (limited by bedding boundaries or intersecting fractures) tend to be **rectangular** or similarly bounded polygons, often with large aspect ratios (Petit et al. 1994; Locsin 2005; Fig. 7 Grimsel). *[Zhang 2010, pp. 6-7, 13]*
   - Layer-perpendicular joints in stiffer beds are rectangular and their height equals layer thickness, with L/H > 4–5. *[Zhang 2010, pp. 6-7]*
2. **Fallacy of equal trace lengths implying circular shape**:
   - Even non-equidimensional (elliptical, rectangular) joints can produce approximately equal average trace lengths on two perpendicular sampling planes if the sampling orientations fall within certain \( \beta \) ranges (Figs. 11, 13). Therefore, concluding joints are circular from such equality is unwarranted. *[Zhang 2010, pp. 7-9, 13]*
3. **Orientation sensitivity**:
   - For elliptical joints with large aspect ratio \( k \), the mean and standard deviation of trace lengths remain nearly constant over wide ranges of \( \beta \) (e.g., 40°–140°). This explains why Robertson (1970) and Barton (1977) observed similar trace lengths on differently oriented planes, while Bridges (1976) and Einstein et al. (1979) observed significant differences. *[Zhang 2010, pp. 9-12]*
4. **Elliptical representation of polygonal joints**:
   - An ellipse covers over 90% of a rectangle of the same area and aspect ratio (Eq. 8, \( A_c/A_t = 0.91 \)). For joints with curved ends along straight bedding boundaries, the coverage is even higher. Thus, using elliptical joints to represent rectangular or polygonal joints is usually appropriate. *[Zhang 2010, pp. 12-13]*
5. **Characterization methods**:
   - Elliptical joints can be characterized from multiple trace windows using the intersection method of Zhang et al. (2002) to infer aspect ratio and size distribution. *[Zhang 2010, pp. 11-12]*
   - Rectangular joints can be handled by direct measurement, Warburton’s stereological relationship, or the elliptical approximation. *[Zhang 2010, pp. 12-13]*

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Unrestricted joints mostly elliptical; circular shapes rare. | Woodworth (1896), Bankwitz (1965), Hodgson (1961), Petit et al. (1994), Weinberger (2001), Bahat et al. (2003), Savalli & Engelder (2005). *[Zhang 2010, pp. 2-6]* | No adjacent faults, bedding boundaries, or pre-existing fractures limiting propagation. | Plumose/feather morphology on joint surfaces often correlates with elliptical boundaries. |
| Restricted joints (bounded by beds, pre-existing fractures) are rectangular. | Petit et al. (1994), Locsin (2005), Grimsel observations (Fig. 7). *[Zhang 2010, pp. 5-7]* | Growth limited by less deformable layers or existing fractures. | Height often equals layer thickness in sedimentary sequences. |
| Equal average trace lengths on two sampling planes do NOT imply circular joints. | Zhang et al. (2002) analysis; Figs. 11, 13; Robertson (1970), Barton (1977) vs. Bridges (1976), Einstein et al. (1979). *[Zhang 2010, pp. 7-12]* | Non-equidimensional (elliptical) joints with deterministic or random major axes. | \( \beta \) values may place both sampling planes in a plateau region of the \( \mu_l \) curve. |
| Stereological relationship for elliptical joints (Eq. 1) enables joint size distribution estimation. | Zhang et al. (2002). *[Zhang 2010, pp. 8-10]* | Requires assumption of joint size distribution form (lognormal, negative exponential, Gamma) and knowledge of \( \beta \). | Table 2 provides explicit formulas for \( \mu_l, \sigma_l \). |
| Mean and std trace length vary slowly with \( \beta \) for high aspect ratios. | Fig. 13, for lognormal, neg. exponential, Gamma distributions. *[Zhang 2010, pp. 9-12]* | \( k = 4, 8 \); \( \beta \) ranges 40°–140° show little change. | Explains field observations of approximately equal trace lengths despite non-circular joints. |
| Ellipse covers 91% of rectangle with same area and aspect ratio. | Geometry analysis (Eqs. 3–8). *[Zhang 2010, pp. 12-13]* | Centers aligned; rectangle and ellipse have identical \( k \). | Coverage >0.91 if ends are curved while sides are straight (bed-bounded). |
| Joints in stiffer layers have rectangular shape, L/H > 4–5. | Petit et al. (1994) sandstone layers; Locsin (2005) multiple cases. *[Zhang 2010, pp. 6-7]* | Layered sedimentary rocks with stiffness contrast. | “Layer perpendicular joints”. |
| Hydraulic fractures from point source → circular; line source → elliptical, tending to circular with growth. | Daneshy (1973); Moriya et al. (2006) AE ellipses. *[Zhang 2010, pp. 7-8]* | Laboratory and in-situ salt mine experiments. | Supports the conceptual model of initial circular/elliptical growth. |

## Limitations
- The actual 3D shape of joints at a given site is rarely known because rock masses are inaccessible in three dimensions; all inferences are based on surface traces or limited exposures. *[Zhang 2010, pp. 1-2]*
- “Because so many factors affect the shape of joints, it is possible that the real joint shape is different from what was described above.” (Summary) *[Zhang 2010, pp. 13]*
- The classification into elliptical and rectangular is a simplification; real joints can have irregular, polygonal, or non-planar shapes. *[Zhang 2010, pp. 2, 3]*
- The stereological method assumes an *a priori* distribution form for joint size and requires knowledge of \( \beta \) (major axis orientation) which is usually unobserved; trial orientations are needed. *[Zhang 2010, pp. 11-12]*
- The literature review is based on a selection of published cases and does not encompass all rock types or tectonic settings. *[Zhang 2010, pp. 4]*

## Assumptions / Conditions
- Joints are assumed to be planar; three-dimensional surface morphology is acknowledged but treated separately. *[Zhang 2010, pp. 1-2]*
- Joints can be categorized as *unrestricted* (elliptical approximation) or *restricted* (rectangular/polygonal approximation). *[Zhang 2010, pp. 1-2]*
- For stereological analysis, joints are ellipses with a constant aspect ratio \( k \) and a major axis orientation that is either deterministic or uniformly random. *[Zhang 2010, pp. 8]*
- The joint size distribution \( g(a) \) is assumed to be lognormal, negative exponential, or Gamma. *[Zhang 2010, pp. 9-10]*
- True trace length distribution has been corrected for sampling biases (Priest & Hudson 1981; Zhang & Einstein 2000). *[Zhang 2010, pp. 9, 12]*
- Rectangular joints can be approximated as parallelograms (right angles) for Warburton’s stereological relationship. *[Zhang 2010, pp. 12]*
- The elliptical approximation for rectangles uses equal area and equal aspect ratio, with major axes aligned. *[Zhang 2010, pp. 12-13]*

## Key Variables / Parameters
- Joint planar shape: [[elliptical joint shape]] (incl. circular), [[rectangular joint shape]], polygonal
- Aspect ratio \( k = a/b \) (ellipse) or \( L/W \) (rectangle)
- Joint size: major axis length \( a \) (ellipse), length \( L \) or width \( W \) (rectangle)
- Joint size distribution \( g(a) \), mean \( \mu_a \), standard deviation \( \sigma_a \)
- Trace length \( l \), mean \( \mu_l \), standard deviation \( \sigma_l \)
- Angle \( \beta \) between joint major axis and trace line in the joint plane
- Stereological factor \( M = \frac{\sqrt{\tan^2\beta + 1}}{\sqrt{k^2\tan^2\beta + 1}} \)
- Sampling plane orientation (controls \( \beta \))

## Reusable Claims
1. **Claim**: In the absence of confining geological structures, rock joints predominantly assume elliptical planar shapes, with purely circular shapes being rare.  
   **Conditions**: Unrestricted joints; based on extensive field observations (Woodworth 1896, Bankwitz 1965, Petit et al. 1994, etc.) and experimental studies (Daneshy 1973, Moriya et al. 2006).  
   **Limitation**: Planarity is a simplification; the joints may possess three-dimensional surface morphology. *[Zhang 2010, pp. 2-6, 13]*

2. **Claim**: Equality of mean trace lengths on two differently oriented sampling planes cannot be used as sufficient evidence that joints are equidimensional (circular). Non-equidimensional elliptical joints with suitable major axis orientation can produce approximately equal mean trace lengths on perpendicular planes.  
   **Conditions**: Sampling planes may both lie in \( \beta \) ranges where the \( \mu_l \)–\( \beta \) curve is flat, especially for \( k \ge 2 \).  
   **Limitation**: Without independent knowledge of the joint major axis orientation, the actual \( \beta \) values are unknown. *[Zhang 2010, pp. 8-12, Fig. 11, Fig. 13]*

3. **Claim**: The stereological procedure of Zhang et al. (2002) can estimate the aspect ratio, major axis orientation, and size distribution of elliptical joints from trace length data collected on at least two differently oriented sampling windows, by intersecting the \( \mu_a \)–\( k \) and \( \sigma_a \)–\( k \) curves.  
   **Conditions**: Joints are approximately elliptical; size distribution is lognormal, negative exponential, or Gamma; sampling biases have been removed; the major axis orientation is constant over the joint set.  
   **Limitation**: Requires multiple sampling windows with known relative orientations; sensitive to distributional assumptions. *[Zhang 2010, pp. 11-12]*

4. **Claim**: Polygonal (including rectangular) joints can be represented by equivalent ellipses with the same area and aspect ratio, because the overlapping area exceeds 91% (and more for joints with curved tips). This allows applying elliptical-joint characterization methods to rectangular/polygonal joints.  
   **Conditions**: The rectangle/ellipse centers and major axes are aligned; the aspect ratio is preserved.  
   **Limitation**: The method is an approximation; highly irregular polygons may deviate. *[Zhang 2010, pp. 12-13, Eqs. 3-8]*

5. **Claim**: Joints bounded by bedding planes or intersecting pre-existing fractures (restricted joints) tend to be rectangular, with the joint height often equal to the thickness of the fractured layer and large length-to-height ratios (>4).  
   **Conditions**: Mechanically layered sedimentary rocks where a stiffer layer fractures while adjacent weaker layers remain intact.  
   **Limitation**: The rectangular shape is inferred from trace measurements and limited 3D exposure; actual boundaries may be irregular. *[Zhang 2010, pp. 6-7]*

6. **Claim**: For elliptical joints with aspect ratio \( k \ge 4 \), the mean and standard deviation of trace lengths are nearly constant over a wide range of \( \beta \) (roughly 40°–140°), which can mask the non-equidimensional nature in field trace-length surveys that use only two sampling planes.  
   **Conditions**: Joint size distribution is lognormal, negative exponential, or Gamma; applies to the expected value.  
   **Limitation**: The specific plateau width depends on the underlying size distribution parameters; actual field data may show scatter. *[Zhang 2010, pp. 9-12, Fig. 13]*

## Candidate Concepts
- [[unrestricted joint]]
- [[restricted joint]]
- [[elliptical joint shape]]
- [[rectangular joint shape]]
- [[polygonal joint]]
- [[joint aspect ratio]]
- [[stereological relationship]]
- [[trace length distribution]]
- [[joint size distribution]]
- [[sampling plane orientation effect]]
- [[joint surface morphology]]
- [[plumose structure]]
- [[joint fringe]]
- [[hydraulic fracture shape]]
- [[layer perpendicular joints]]
- [[fractography]]

## Candidate Methods
- [[Zhang et al. (2002) stereological method for elliptical joints]]
- [[Warburton (1980b) stereological method for parallelograms]]
- [[elliptical approximation of rectangular joints]]
- [[direct measurement of joint traces on bedding surfaces]]
- [[two-step joint shape determination (geologic evaluation + trace characterization)]]

## Connections To Other Work
- **Zhang et al. (2002)** Geotechnique 52(6):419–433 – provided the foundational stereological relationship for elliptical discontinuities used throughout the analysis. *[Zhang 2010, pp. 8-12]*
- **Warburton (1980b)** Int. J. Rock Mech. Min. Sci. 17:305–316 – developed stereological interpretation for joints with parallelogram shapes, referenced for rectangular joint characterization. *[Zhang 2010, pp. 12]*
- **Baecher et al. (1977) / Warburton (1980a)** – circular disk models; contrast with non-circular shapes discussed. *[Zhang 2010, pp. 7-8]*
- **Dershowitz et al. (1993)** FracMan – uses polygons to represent joints, noting that ellipses and polygons can be interconverted. *[Zhang 2010, pp. 8, 12]*
- **Woodworth (1896)**, **Bankwitz (1965, 1966)** – classic field studies on joint surface morphology and elliptical shapes. *[Zhang 2010, pp. 2-4]*
- **Petit et al. (1994)** – detailed shape ratios for joints in pelites and sandstones; differentiated elliptical (unrestricted) and rectangular (restricted) shapes. *[Zhang 2010, pp. 5-6]*
- **Weinberger (2001)**, **Bahat et al. (2003)**, **Savalli & Engelder (2005)** – recent field and experimental evidence on elliptical rupture propagation. *[Zhang 2010, pp. 4-5]*
- **Robertson (1970)**, **Barton (1977)**, **Bridges (1976)**, **Einstein et al. (1979)** – trace length observations used to illustrate the pitfalls of inferring shape from equal/different mean trace lengths. *[Zhang 2010, pp. 7, 9-12]*
- **Locsin (2005)**, **Becker & Gross (1996)**, **Saltzman (2001)**, **Gross et al. (1997)**, **Baudo (2001)** – case studies of layer-perpendicular rectangular joints. *[Zhang 2010, pp. 6-7]*
- **Daneshy (1973)**, **Moriya et al. (2006)** – experimental studies supporting elliptical growth. *[Zhang 2010, pp. 7-8]*

## Open Questions
- The true 3D shape of joints at a site remains unobservable with current techniques; methods to verify the inferred shape without full 3D exposure are lacking. *[Zhang 2010, pp. 1-2]*
- The effects of non-planarity and irregular boundaries on stereological inversion need further investigation. *[Zhang 2010, pp. 3, 13]*
- How to incorporate mixed shape populations (e.g., a joint set containing both elliptical and rectangular members) into characterization procedures. *[Zhang 2010, pp. 2]*
- The applicability of the elliptical approximation for polygonal joints with few sides (triangles, quadrilaterals) beyond the rectangular case. *[Zhang 2010, pp. 12-13]*

## Source Coverage
All 12 non-empty indexed source blocks from the PDF [Zhang, 2010, pp. 1-2, 2-3, 3-4, 4-6, 6-7, 7-8, 8-9, 9-12, 12-13, 13, 13-14, 14] were processed. The compiled blocks contain 55,756 characters, covering 100% of the indexed text by blocks, with a character coverage ratio of 1.004 (slight rounding differences). No sources outside these fragments were used.
