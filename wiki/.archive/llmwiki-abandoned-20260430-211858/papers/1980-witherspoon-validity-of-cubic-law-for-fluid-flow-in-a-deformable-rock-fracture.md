---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "1980-witherspoon-validity-of-cubic-law-for-fluid-flow-in-a-deformable-rock-fracture"
title: "Validity of Cubic Law for Fluid Flow in a Deformable Rock Fracture."
status: "draft"
source_pdf: "data/papers/1980 - Validity of Cubic Law for fluid flow in a deformable rock fracture.pdf"
collections:
citation: "Witherspoon, P. A., et al. “Validity of Cubic Law for Fluid Flow in a Deformable Rock Fracture.” *Water Resources Research*, vol. 16, no. 6, Dec. 1980, pp. 1016–1024."
indexed_texts: "8"
indexed_chars: "39334"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T10:34:06"
---

# Validity of Cubic Law for Fluid Flow in a Deformable Rock Fracture.

## One-line Summary
This paper experimentally validates that the cubic law governs laminar fluid flow through both open and stress-closed deformable rock fractures, with permeability uniquely determined by the fracture aperture irrespective of rock type or stress history [Witherspoon 1980, pp. 1-1].

## Research Question
Is the cubic law (Q/Δh ∝ (2b)³) valid for fluid flow in a closed rock fracture where the surfaces are in contact and the aperture decreases under applied normal stress? [Witherspoon 1980, pp. 1-1]

## Study Area / Data
- **Rock types:** Homogeneous intact samples of granite, basalt, and marble from quarries in California [Witherspoon 1980, pp. 2-3].
- **Fracture types:** Artificially induced tension fractures [Witherspoon 1980, pp. 2-3].
- **Test conditions:** Room temperature; filtered water as the fluid under ambient conditions; normal stresses up to 20 MPa [Witherspoon 1980, pp. 2-3].
- **Aperture range:** From 250 μm down to a minimum of 4 μm under maximum stress [Witherspoon 1980, pp. 1-1].
- **Flow geometries:** Radial flow (cylinder with a central hole) and straight flow [Witherspoon 1980, pp. 2-3] [Witherspoon 1980, pp. 8-9].

## Methods
- **Sample preparation:** Tensile fractures were created using a modified Brazilian loading method, producing surfaces orthogonal to the axis of cylindrical samples [Witherspoon 1980, pp. 2-3].
- **Experimental apparatus:** A Riehle testing machine applied axial loads up to 20 MPa. Three linear variable differential transducers (LVDTs) placed 120° apart measured deformation across the fracture, detecting changes as small as 0.4 μm [Witherspoon 1980, pp. 2-3].
- **Aperture determination:** The true aperture (2b) could not be measured directly. It was treated as the sum of an apparent aperture (2bₐ, measured by LVDT displacement) and an unknown residual aperture (2bᵣ), which was a key parameter to be determined by data fitting [Witherspoon 1980, pp. 5-7].
- **Flow measurement:** Flow rates were measured under increasing (loading) and decreasing (unloading) axial stress to investigate the effect of stress history [Witherspoon 1980, pp. 3-5].
- **Law validation procedure:**
    - The cubic law was written in the form Q/Δh = C(2bₐ + 2bᵣ)ⁿ. A least-squares minimization process was used to fit the unknown exponent `n` and residual aperture `2bᵣ` by setting a surface characteristic factor `f = 1` [Witherspoon 1980, pp. 5-7].
    - The same process was repeated using the form Q/Δh = (C/f)(2bₐ + 2bᵣ)³ to determine the factor `f` and `2bᵣ` simultaneously, accounting for deviations from the ideal parallel plate model [Witherspoon 1980, pp. 7-8].

## Key Findings
- **Validity of the cubic law exponent:** For all rock types and flow geometries, the fitted exponent `n` was consistently close to 3. The fitted values ranged from 3.01 to 3.10 across all runs, confirming the cubic relation Q ∝ (2b)³ [Witherspoon 1980, pp. 3-5].
- **Validity for closed fractures:** The cubic law remains valid whether the fracture surfaces are held open or are being closed under stress. The results are not dependent on rock type [Witherspoon 1980, pp. 1-1].
- **Uniqueness of permeability:** Permeability was uniquely defined by the fracture aperture (2b) and was independent of the stress history (loading vs. unloading cycles) used in the investigation [Witherspoon 1980, pp. 1-1].
- **Deviations and correction factor:** Deviations from the ideal parallel plate concept cause an apparent reduction in flow. This can be incorporated into the cubic law by the factor `f` (Q/Δh = (C/f)(2b)³). The fitted factor `f` varied from 1.04 to 1.65 in the investigations, with f > 1 as predicted by theory [Witherspoon 1980, pp. 1-1] [Witherspoon 1980, pp. 7-8].
- **Behavior of the factor f:** The values of `f` generally decreased with successive loading/unloading runs (e.g., from 1.21 to 1.04 for granite with straight flow). This may indicate that the fracture surfaces became progressively better mated during cyclic loading [Witherspoon 1980, pp. 7-8].
- **Influence of flow geometry:** Radial flow data deviated more from the ideal cubic law (f=1.0) than straight flow data (e.g., maximum f values of 1.49 vs 1.21 for granite). This might be caused by the more complicated effects of roughness in a radial flow field [Witherspoon 1980, pp. 7-8].
- **Conceptual model of a closing fracture:** The fracture is visualized as being controlled by the strength of contacting asperities. These contact areas can withstand significant stresses while maintaining interconnected void spaces for fluid to flow as the aperture decreases. The overall geometrical effect can still be represented by a measurement of 2b [Witherspoon 1980, pp. 1-1] [Witherspoon 1980, pp. 8-9].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| Fitted exponent `n` ranges from 3.01 to 3.10 across 12 tests | [Witherspoon 1980, pp. 3-5] | Granite, basalt, and marble; straight and radial flow; f=1.0 assumed | Validates the cubic relationship (n=3) over apertures from 4 to 250 μm. |
| Fitted factor `f` ranges from 1.04 to 1.65 across 12 tests | [Witherspoon 1980, pp. 7-8] | Same rock types, both flow geometries; Q/Ah = (C/f)(2b)³ assumed | f > 1.0, quantifying flow reduction due to surface roughness and contact. |
| f decreased from 1.21 to 1.04 for granite with straight flow over 3 runs | [Witherspoon 1980, pp. 7-8] | Cyclic loading on a single granite sample | Suggests progressive surface mating under cyclic stress. |
| Maximum f=1.49 for granite radial flow vs f=1.21 for straight flow | [Witherspoon 1980, pp. 7-8] | Granite, comparing radial and straight flow geometries | Suggests roughness effects are more complex under radial flow. |

## Limitations
- **Minimum aperture constraint:** The investigation was limited to a minimum aperture of 4 μm under a maximum normal stress of 20 MPa [Witherspoon 1980, pp. 1-1].
- **Flow geometry:** Results for radial flow showed larger deviations from the ideal cubic law, and the Reynolds number is difficult to define in this setting [Witherspoon 1980, pp. 7-8].
- **Stress type:** The study was conducted under normal stress only, whereas general field situations involve both normal and shear deformations [Witherspoon 1980, pp. 8-9].
- **Scale:** A potential size effect exists when determining hydraulic properties from rock specimens of different dimensions, which was not analyzed here but noted in prior work [Witherspoon 1980, pp. 8-9].
- **Direct aperture measurement:** The true aperture (2b) during closure could not be measured directly; it was inferred by fitting a residual aperture term [Witherspoon 1980, pp. 5-7].

## Assumptions / Conditions
- **Flow regime:** Laminar flow of fluids [Witherspoon 1980, pp. 1-1].
- **Fluid and temperature:** Filtered water at ambient (room temperature) conditions [Witherspoon 1980, pp. 2-3].
- **Rock matrix:** The matrix permeability of the granite, basalt, and marble samples was negligibly low and could be ignored [Witherspoon 1980, pp. 2-3].
- **Initial validation:** The cubic law for an open fracture of parallel planar plates was taken as an established fact, valid for apertures as low as 0.2 μm [Witherspoon 1980, pp. 1-1].
- **Flow law form:** The cubic law was first tested by assuming the factor for surface characteristics, `f`, was 1.0 [Witherspoon 1980, pp. 5-7].
- **Deformation measurement:** Net mechanical fracture deformation was computed by subtracting the deformation of an intact rock sample from the total measured deformation of the fractured sample [Witherspoon 1980, pp. 3-5].
- **Physical model:** A closing fracture is idealized as two surfaces where contacts are point-like asperities that deform elastically without significantly changing contact area, maintaining interconnected flow paths [Witherspoon 1980, pp. 8-9].

## Key Variables / Parameters
- **2b:** Fracture aperture [Witherspoon 1980, pp. 1-1].
- **2bₐ:** Apparent aperture half width (measured mechanically) [Witherspoon 1980, pp. 9-9].
- **2bᵣ:** Residual aperture half width (fitted parameter) [Witherspoon 1980, pp. 9-9].
- **Q:** Flow rate [Witherspoon 1980, pp. 1-1].
- **Δh:** Difference in hydraulic head [Witherspoon 1980, pp. 1-1].
- **C:** Proportional constant in cubic law dependent on flow geometry and fluid properties [Witherspoon 1980, pp. 1-1].
- **f:** Fracture surface characteristic factor accounting for deviations from ideal parallel plates [Witherspoon 1980, pp. 1-2] [Witherspoon 1980, pp. 9-9].
- **n:** Exponent in the generalized fracture flow law Q/Δh ∝ (2b)ⁿ; ideally n=3 [Witherspoon 1980, pp. 9-9].
- **σₓ:** Axial (normal) stress [Witherspoon 1980, pp. 9-9].
- **ε:** Height of asperities [Witherspoon 1980, pp. 1-2].

## Reusable Claims
### Claim 1: Universality of the Cubic Law for Laminar Fracture Flow
The cubic law (Q ∝ (2b)³) is valid for laminar flow in deformable rock fractures whether they are open or mechanically closed under normal stress, provided that the effective hydraulic aperture is used. This validity is independent of rock type (tested on granite, basalt, marble) and the loading/unloading stress history [Witherspoon 1980, pp. 1-1] [Witherspoon 1980, pp. 3-5].
- **Evidence:** A least-squares fit of an exponent `n` on flow data from 4 to 250 μm apertures under 0-20 MPa stress yielded values between 3.01 and 3.10.
- **Conditions:** Laminar flow, negligible matrix permeability, normal stresses up to 20 MPa, apertures down to 4 μm, artificially induced tension fractures.
- **Limitations:** Not confirmed for shear deformation, apertures below 4 μm, or where Reynolds numbers are high or ill-defined.

### Claim 2: Quantifying Flow Reduction with Surface Factor f
Deviations from the ideal cubic law can be quantified by a multiplicative factor f, modifying the law to Q/Δh = (C/f)(2b)³, where f is always ≥ 1 and captures the apparent reduction in flow due to surface roughness, contact, and flow path tortuosity [Witherspoon 1980, pp. 1-1] [Witherspoon 1980, pp. 1-2].
- **Evidence:** Fitting experimental data with this model produced realistic f values ranging from 1.04 to 1.65.
- **Conditions:** The deviation metric (e/2b > 0.065) from earlier work by Lomize is referenced as a condition where such a correction becomes necessary [Witherspoon 1980, pp. 1-2].

### Claim 3: Permeability as a Unique Function of Aperture
The fracture flow permeability is a unique function of the aperture and is independent of the stress path (loading vs. unloading) used to achieve that aperture [Witherspoon 1980, pp. 1-1].
- **Evidence:** Data points from loading and unloading cycles on the same rock sample fall on the same line correlating flow rate per unit head (Q/Δh) to aperture (2b), indicating no hysteresis effect on permeability for a given aperture [Witherspoon 1980, pp. 3-5] [Witherspoon 1980, pp. 5-7].
- **Conditions:** Artificially induced fractures in granite, basalt, and marble under normal stress cycling up to 20 MPa.

### Claim 4: Conceptual Model of Flow in a Closing Fracture
The flow in a stress-closed fracture is controlled by a network of interconnected openings between contacting asperities. The bulk hydraulic behavior of this complex geometry can be reduced to an equivalent parallel-plate aperture (2b), establishing a strong dependence of flow on aperture size [Witherspoon 1980, pp. 1-1] [Witherspoon 1980, pp. 8-9].
- **Evidence:** Successful fitting of the cubic law demonstrates that aperture measurement (2b) dominantly controls the hydraulic response, even when the fracture is “closed” and flow paths are tortuous.
- **Conditions:** The model assumes asperities form areas of contact that deform elastically and withstand significant stress without a significant change in contact area.

## Candidate Concepts
- [[cubic law]]
- [[fracture aperture]]
- [[deformable rock fracture]]
- [[fracture roughness]]
- [[asperities]]
- [[normal stress]]
- [[hydraulic permeability of fractures]]
- [[laminar flow]]
- [[fracture reservoir]]
- [[stress-dependent permeability]]

## Candidate Methods
- [[radial flow test]]
- [[Brazilian loading method]]
- [[least-squares fitting for non-linear flow law]]
- [[cyclic loading permeability test]]
- [[linear variable differential transducer (LVDT) measurement]]

## Connections To Other Work
- **Prior work establishing the cubic law:** The study builds on the work of Boussinesq [1868] and others who validated the cubic law for open, parallel planar plates down to apertures of 0.2 μm [Witherspoon 1980, pp. 1-1].
- **Deviation factor f:** The method of incorporating deviations from the ideal law using a factor `f` is based on the work of Lomize [1951], who developed an empirical equation for roughness also applicable to non-parallel fracture walls [Witherspoon 1980, pp. 1-2].
- **Dispute regarding the cubic law exponent:** Sharp [1970] and Sharp and Maini [1972] disputed the cubic law for natural fractures, suggesting an exponent of 2 based on an “effective” aperture concept. However, Gale [1975] countered that their data would fit the cubic law if correlated with the actual physical aperture [Witherspoon 1980, pp. 1-2].
- **Scale effect:** The investigation references Witherspoon et al. [1979] regarding a potential size effect when measuring the hydraulic properties of fractures in specimens of different dimensions, connecting the lab-scale validation to field-scale applications [Witherspoon 1980, pp. 8-9].

## Open Questions
- What are the mechanical and hydraulic behaviors of a fracture deforming under combined normal and shear stress, which is more representative of field conditions? [Witherspoon 1980, pp. 8-9]
- What is the exact nature of the “potential size effect” that could alter the hydraulic behavior when scaling from laboratory specimens to in-situ field fractures? [Witherspoon 1980, pp. 8-9]
- How does the contact area of asperities evolve under high stress, and what is its precise role in controlling flow in deep subsurface fractures? [Witherspoon 1980, pp. 8-9]

## Source Coverage
This wiki page was compiled using 8 sequential index excerpts, covering pages 1 through 9 of the final published paper [Witherspoon 1980, pp. 1-9]. The coverage includes the abstract/introduction, methodology, key results, discussion, and notation sections, providing a comprehensive overview of the paper’s core empirical validation and model. The excerpts contain detailed experimental results (Tables 1 and 2, Figures 5-8) and the central arguments. However, some details may be missing, such as a complete review of the introduction’s literature, the full derivation of all equations, a detailed run-by-run description from Iwai [1976], or the specific contents of the later, uncaptured references list beyond the first few entries shown.
