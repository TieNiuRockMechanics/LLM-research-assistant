---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2014-mcclure-an-investigation-of-stimulation-mechanisms-in-enhanced-geothermal-systems"
title: "An Investigation of Stimulation Mechanisms in Enhanced Geothermal Systems."
status: "draft"
source_pdf: "data/papers/An investigation of stimulation mechanisms in Enhanced Geothermal Systems.pdf"
collections:
citation: "McClure, Mark W., and Roland N. Horne. “An Investigation of Stimulation Mechanisms in Enhanced Geothermal Systems.” *International Journal of Rock Mechanics & Mining Sciences*, 2014, doi:10.1016/j.ijrmms.2014.07.011. Accessed 2026."
indexed_texts: "28"
indexed_chars: "138367"
nonempty_source_blocks: "28"
compiled_source_blocks: "28"
compiled_source_chars: "138921"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004004"
coverage_status: "full-index"
source_signature: "bee24e9f132777103bb8f780158f0dd77e858df6"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:29:32"
---

# An Investigation of Stimulation Mechanisms in Enhanced Geothermal Systems.

## One-line Summary
The paper proposes that stimulation in Enhanced Geothermal Systems (EGS) often involves a mixed-mechanism where new fractures initiate from and propagate off preexisting natural fractures, reconciling field observations of flow localization with high injection pressures.

## Research Question
What are the primary mechanisms of hydraulic stimulation in Enhanced Geothermal Systems (EGS), and how can the apparent contradiction between flow localizing at preexisting fractures and bottomhole pressure exceeding the minimum principal stress be explained?

## Study Area / Data
The study reviews ten historical EGS projects conducted in granitic rock: Cooper Basin, Soultz, Fenton Hill, Hijiori, Ogachi, Desert Peak, Rosemanowes, Basel, Le Mayet, and Fjällbacka. Data include injection pressures, microseismicity, wellbore flow logs, and fault observations from these projects [Mc 2014, pp. 3-6].

## Methods
Computational modeling was performed using CFRAC, a discrete fracture network (DFN) simulator that fully couples fluid flow with stresses induced by fracture deformation. The model assumes single-phase liquid water, isothermal flow, zero matrix permeability, and linear elastic deformation. Simulations investigated conditions for pure shear stimulation (PSS) and an example of mixed-mechanism stimulation (MMS) [Mc 2014, pp. 7-9].

## Key Findings
1.  Pure shear stimulation (PSS) is only possible under specific geological conditions: a percolating natural fracture network with adequate initial transmissivity and storativity (e.g., thick fault zones) [Mc 2014, pp. 9-11].
2.  When these conditions are not met, injection pressure rises to the minimum principal stress, leading to the opening of natural fractures and the propagation of new fractures (splays or extensions) from them, resulting in mixed-mechanism stimulation (MMS) [Mc 2014, pp. 6-7, 11-12].
3.  A review of ten EGS projects shows that bottomhole pressure typically approached or exceeded the minimum principal stress, while flow localized at discrete zones correlated with preexisting fractures, observations consistent with MMS [Mc 2014, pp. 3-6].
4.  In MMS, propagating new fractures may terminate against preexisting fractures, creating a complex network. This can lead to flow localization and, upon shut-in, closure of natural fractures that hydraulically isolates newly formed fractures [Mc 2014, pp. 12-13].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| In simulation A1 (baseline PSS), pressure remained below σ_min with a percolating, high-storativity network. | [Mc 2014, pp. 9-11] | Percolating network, high storativity (E0=5 cm), high initial transmissivity. | Demonstrates ideal conditions for PSS. |
| In simulation A2, low initial transmissivity caused pressure to exceed σ_min, forming a new hydraulic fracture. | [Mc 2014, pp. 9-11] | Very low initial transmissivity (e0=0.01 mm). | Shows PSS fails if initial transmissivity is too low. |
| In simulation A3, low storativity led to unrealistically rapid propagation of stimulation. | [Mc 2014, pp. 9-11] | Low storativity (E0=0.5 mm), crack-like fractures. | Highlights the need for sufficient fluid storage in fractures. |
| In simulation C (MMS), new fractures propagated off slipping natural fractures, and flow localized. | [Mc 2014, pp. 12-13] | Non-percolating natural network, many potential forming fractures. | Demonstrates MMS behavior and fracture closure effects. |
| At most reviewed EGS projects, estimated BHP exceeded or approached σ_min. | [Mc 2014, pp. 3-6] | Various EGS projects in granitic rock. | Suggests conditions for fracture opening were common. |
| At most reviewed EGS projects, flow from the wellbore localized at discrete zones correlated with natural fractures. | [Mc 2014, pp. 3-6] | Various EGS projects. | Contradicts expectation of axial fracture propagation from wellbore. |
| At Fenton Hill, mini-frac tests showed opening pressures ~15 MPa above inferred σ_min, suggesting natural fractures not optimally oriented opened. | [Mc 2014, pp. 14-15] | Phase II Fenton Hill reservoir. | Supports hypothesis of natural fracture opening. |
| At Desert Peak, injection below σ_min caused limited, reversible shear stimulation; injection above σ_min caused larger, permanent injectivity increase. | [Mc 2014, pp. 13-14] | Well 27-15, Desert Peak. | Suggests new fracture propagation was more effective than shear stimulation alone. |

## Limitations
1.  Model matches with sparse field data (microseismicity, pressures) are highly nonunique [Mc 2014, pp. 3-3].
2.  Simulations are two-dimensional and assume homogeneous, isotropic, linear elastic rock [Mc 2014, pp. 7-7].
3.  The model does not include proppant transport or thermal effects [Mc 2014, pp. 7-7].
4.  The location, orientation, and length of newly forming fractures must be specified in advance in the model [Mc 2014, pp. 8-9].

## Assumptions / Conditions
1.  Single-phase liquid water flow (no proppant), isothermal conditions [Mc 2014, pp. 7-7].
2.  Zero matrix permeability; all flow occurs in fractures [Mc 2014, pp. 7-7].
3.  Rock deformation is homogeneous, isotropic, and linear elastic [Mc 2014, pp. 7-7].
4.  Fracture sliding follows Coulomb's law with a constant coefficient of friction [Mc 2014, pp. 7-7].
5.  New fractures can only form if fluid pressure exceeds the minimum principal stress (except for splay fractures) [Mc 2014, pp. 8-9].

## Key Variables / Parameters
-   **Fracture Transmissivity (T):** Controls fluid flow rate; increases with pressure and sliding displacement [Mc 2014, pp. 7-8].
-   **Fracture Storativity (S):** Ability of fractures to store fluid; highly nonlinear, increasing with fluid pressure [Mc 2014, pp. 8-9].
-   **Stress Anisotropy:** Difference between principal stresses; influences fracture orientation and opening pressure [Mc 2014, pp. 8-9].
-   **Injection Pressure / Rate:** Operational parameter that determines if pressure exceeds σ_min [Mc 2014, pp. 8-9].
-   **Fracture Network Percolation:** Existence of connected pathways through the natural fracture network [Mc 2014, pp. 9-11].
-   **Initial Fracture Transmissivity (e0):** Transmissivity of closed natural fractures before stimulation [Mc 2014, pp. 9-11].

## Reusable Claims
1.  Pure shear stimulation in EGS requires a percolating natural fracture network with adequate initial transmissivity and storativity to prevent pressure buildup above the minimum principal stress [Mc 2014, pp. 9-11].
2.  In formations lacking thick, porous fault zones, injection at specified rate will likely cause pressure to exceed the minimum principal stress, leading to the opening of natural fractures and propagation of new fractures (mixed-mechanism stimulation) [Mc 2014, pp. 11-12].
3.  The localization of flow into discrete zones at the wellbore, correlated with natural fractures, is a common observation in EGS projects and is consistent with fracture initiation from preexisting features [Mc 2014, pp. 3-6].
4.  Closure of natural fractures during shut-in or flowback can hydraulically isolate newly formed fractures, potentially reducing well productivity [Mc 2014, pp. 12-13].
5.  Field experiments at Desert Peak demonstrate that injection above the minimum principal stress (likely causing new fracture propagation) can be more effective at creating permanent permeability enhancement than injection below it (limited to shear stimulation) [Mc 2014, pp. 13-14].

## Candidate Concepts
-   [[Mixed-mechanism stimulation]]
-   [[Pure shear stimulation]]
-   [[Discrete fracture network]]
-   [[Shear stimulation]]
-   [[Hydraulic fracture propagation]]
-   [[Fracture initiation from natural fractures]]
-   [[Splay fractures]]
-   [[Pressure-limiting behavior]]
-   [[Thermal short-circuiting]]
-   [[Zonal isolation]]

## Candidate Methods
-   [[Discrete fracture network modeling]]
-   [[Coupled hydro-mechanical simulation]]
-   [[Tendency for shear stimulation test]]
-   [[Pressure transient analysis]]
-   [[Microseismic monitoring]]
-   [[Production logging]]
-   [[Wellbore imaging logs]]
-   [[Core analysis]]

## Connections To Other Work
The paper builds on and critiques the prevailing EGS concept of pure shear stimulation (PSS) [Mc 2014, pp. 2-3]. It references early EGS projects (Fenton Hill, Rosemanowes) where flow localization and complex microseismicity challenged the single planar fracture model [Mc 2014, pp. 2-3]. The MMS concept is linked to modeling approaches used in shale gas hydraulic fracturing [Mc 2014, pp. 2-3]. It discusses interpretations of field data from specific projects by other authors, such as Pine and Batchelor [6] on Rosemanowes and Brown [34] on Fenton Hill [Mc 2014, pp. 14-15].

## Open Questions
1.  How can stimulation mechanisms (PSS vs. MMS) be reliably diagnosed in the field using pressure transient analysis, coring, or other techniques? [Mc 2014, pp. 13-14, 257]
2.  What are the optimal stimulation designs (e.g., use of proppant, zonal isolation, horizontal wells) for EGS if mixed-mechanism stimulation is common? [Mc 2014, pp. 16-17]
3.  How can the huge volumes of fluid injected during EGS stimulation be stored in formations without thick, porous fault zones if fracture opening does not occur? [Mc 2014, pp. 11-12]
4.  What is the role of splay fractures in connecting shearing natural fractures when fluid pressure is below the minimum principal stress? [Mc 2014, pp. 6-7]

## Source Coverage
All non-empty indexed fragments were processed. The coverage audit indicates a coverage ratio by blocks of 1.0 and by characters of 1.004004, confirming full-index coverage of the supplied material.
