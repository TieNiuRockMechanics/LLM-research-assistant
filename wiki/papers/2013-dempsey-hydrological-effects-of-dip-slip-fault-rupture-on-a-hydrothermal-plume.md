---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2013-dempsey-hydrological-effects-of-dip-slip-fault-rupture-on-a-hydrothermal-plume"
title: "Hydrological Effects of Dip-Slip Fault Rupture on a Hydrothermal Plume."
status: "draft"
source_pdf: "data/papers/Hydrological effects of dip-slip fault rupture on a hydrothermal plume.pdf"
collections:
citation: "Dempsey, D. E., et al. \"Hydrological Effects of Dip-Slip Fault Rupture on a Hydrothermal Plume.\" *Journal of Geophysical Research: Solid Earth*, vol. 118, 2013, pp. 195–211, doi:10.1029/2012JB009395."
indexed_texts: "21"
indexed_chars: "103410"
nonempty_source_blocks: "21"
compiled_source_blocks: "21"
compiled_source_chars: "103932"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.005048"
coverage_status: "full-index"
source_signature: "facd143752c7376d9f659adf4c872888200a5a07"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T00:58:16"
---

# Hydrological Effects of Dip-Slip Fault Rupture on a Hydrothermal Plume.

## One-line Summary

A numerical modeling study investigates how coseismic pore-pressure changes and fault permeability disruption from normal fault rupture affect heat and mass transfer in a fault-controlled hydrothermal plume, using the Te Kopia geothermal system on the Paeroa Fault, New Zealand, as a case study.

## Research Question

The study addresses two objectives: first, to investigate natural-state geothermal upflow constrained by dip-slip faults operating as fluid flow barriers; second, to address the likely consequences of rupture on that fault for heat and mass transfer through the geothermal system [Dempsey 2013, pp. 2-3]. More broadly, the work investigates near-field effects of normal earthquakes on fault-controlled hydrothermal plumes, examining how coseismic pore-pressure and permeability perturbations affect geothermal upflow along a dip-slip fault [Dempsey 2013, pp. 1-1].

## Study Area / Data

The model is specific to earthquake rupture and natural geothermal convection occurring within the Taupo Volcanic Zone (TVZ), New Zealand, and in particular the Te Kopia geothermal system located on the Paeroa Fault [Dempsey 2013, pp. 2-3]. The TVZ is a productive volcanic arc hosting convective upflow of high-temperature fluids (>250°C) at more than 20 distinct locations [Dempsey 2013, pp. 2-3]. Hydrothermal convection is driven by extensive magmatic intrusion in the lower and middle crust, supplying heat to the upper crust at a depth of 6–8 km [Dempsey 2013, pp. 2-3]. The 30 km long Paeroa Fault is the fastest moving fault in the TVZ with a vertical displacement rate of 1.5 mm yr⁻¹, and the likelihood of a future M > 6 event on the fault is credible [Dempsey 2013, pp. 2-3]. Geothermal expression at Te Kopia occurs almost exclusively in the footwall block and fault scarp, which has been uplifted ~220 m [Dempsey 2013, pp. 2-3]. Te Kopia has an estimated heat output of 125–250 MW [Dempsey 2013, pp. 9-10]. The computational domain for the fluid flow model is 15 × 15 km in plan view and extends to a depth of 8 km [Dempsey 2013, pp. 6-7].

## Methods

The study employs a mixed 2-D/3-D approach combining a mechanical fault model with a fluid flow model [Dempsey 2013, pp. 3-4].

**Mechanical Fault Model:** Coseismic stress changes are modeled by considering displacement of an inclined, frictional contact surface embedded in a 2-D, plane-strain, elastic-viscous-plastic crust using the finite element software Abaqus/Standard [Dempsey 2013, pp. 4-5]. The model domain is 60 × 25 km, loaded by extensional velocity boundary conditions of 12 mm yr⁻¹ [Dempsey 2013, pp. 4-5]. Deformation is linear elastic below yield, limited by Mohr-Coulomb failure in the upper crust transitioning to viscous creep in the lower crust at 6–8 km depth [Dempsey 2013, pp. 4-5]. The fault dips at 65° and intersects the crust to a depth of 15 km [Dempsey 2013, pp. 4-5]. The seismic cycle is approximated by a 220 yr loading period followed by a 60 s seismic period with a weakened friction coefficient of 0.2 [Dempsey 2013, pp. 4-5]. Dynamic equilibrium is observed after 10 seismic cycles, and results from the 12th cycle are exported to the fluid flow model [Dempsey 2013, pp. 4-5].

**Stress-to-Pressure Conversion:** Coseismic stress changes are converted to pore-pressure perturbations using Skempton's equation: Δpf = (B/3)Δσkk, with B = 0.7 for fractured crystalline rock [Dempsey 2013, pp. 4-5]. The assumption is that coseismic stress changes are sufficiently rapid that induced fluid transport is negligible during the seismic period [Dempsey 2013, pp. 4-5].

**Fluid Flow Model:** Fluid flow is modeled using the Finite Element Heat and Mass (FEHM) transfer code, capable of modeling multiphase, multicomponent Darcy flow through permeable media [Dempsey 2013, pp. 5-6]. The governing equations are derived from energy and mass conservation [Dempsey 2013, pp. 5-6]. A hydrothermal plume is produced by applying a radial Gaussian temperature boundary condition at the base of the model, with temperatures ranging from 150°C at the edge to 340°C in the center [Dempsey 2013, pp. 6-7]. The fault is represented as a 2 m wide impermeable zone using an inclined mesh with a permeability contrast of -4 orders of magnitude relative to surrounding rock [Dempsey 2013, pp. 7-7]. Two zones of permeability are used: an upper 2 km zone of Quaternary volcanic strata and a lower fractured greywacke basement, with an exponentially decreasing permeability profile with depth [Dempsey 2013, pp. 6-7].

**Permeability Disruption Simulation:** To approximate fault gouge rupture, a stochastic, spatially correlated fluctuation field with a power-law exponent of -1.3 is superimposed upon the low-permeability fault plane, imposing a mean increase of 2.3 orders of magnitude and a maximum increase of 4 orders of magnitude [Dempsey 2013, pp. 7-8]. A set of 100 simulations is performed to study mean effects and variability [Dempsey 2013, pp. 7-8].

## Key Findings

1. **Short-term effects dominated by pore-pressure changes:** The immediate effect of the modeled earthquake is to increase mass flux through the geothermal system by 740 kg s⁻¹, an increase of 206% over the natural-state rate of 360 kg s⁻¹ [Dempsey 2013, pp. 11-12]. Excess flow recedes with half-, quarter-, and one-eighth-maximum flows recorded 2.6, 5.8, and 9 days after the earthquake [Dempsey 2013, pp. 12-13].

2. **Near-surface pressure changes dominate surface effects:** Deep pressure changes from slip-arrest at the base of the fault have a negligible effect on surface geothermal expression; near-surface horizontal compression caused by fault block movement results in a large increase in surface heat and mass flow [Dempsey 2013, pp. 15-16].

3. **Longer-term elevated mass flux from permeability increase:** Changes in fault permeability produce a smaller short-term effect but play an important role in longer-term circulation configuration. Mass flow builds to a new steady state approximately 5% higher than preseismic flow rates [Dempsey 2013, pp. 15-16].

4. **Upflow migration:** Following an increase in cross-fault permeability, upflow migrates from the footwall scarp into the hanging wall and away from the fault, because rising fluids are no longer deflected by the fault [Dempsey 2013, pp. 1-1, 15-16].

5. **Cross-fault heat transfer:** Preseismic cross-fault heat flux was dominantly conductive and totaled ~10 MW; immediately following the earthquake, this increased to ~215 MW of heat transfer from the footwall to the hanging wall for depths shallower than 6 km [Dempsey 2013, pp. 15-16].

6. **Reservoir heat content:** The pore-pressure perturbation causes a maximum reduction in reservoir heat content of ~60–80 TJ, minor compared to the absolute reservoir size of ~9000 PJ [Dempsey 2013, pp. 13-14]. Permeability disruption causes orders-of-magnitude larger perturbation to reservoir heat content over 10 years [Dempsey 2013, pp. 14-15].

7. **Plume structure:** An impermeable fault severely impairs coupling between fluid flow in the footwall and hanging wall blocks. In the footwall, an upflow zone transporting 115 MW is coupled to a 100 MW upflow zone in the hanging wall via a 10 MW cross-fault conductive link [Dempsey 2013, pp. 15-16].

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Immediate mass flux increase of 206% (740 kg s⁻¹ above natural state of 360 kg s⁻¹) following modeled M=5.7 earthquake | [Dempsey 2013, pp. 11-12] | Modeled normal fault earthquake with 0.83 m single-event displacement, 25 km surface rupture | Compared to 40-200% increases observed for M 6.9-7.3 earthquakes in Montana, Idaho, Italy |
| Excess flow half-life of 2.6 days; signal undetectable after ~20 days | [Dempsey 2013, pp. 12-13] | Pore-pressure perturbation only, no permanent permeability change | Decay governed by power-law, not exponential as observed by Briggs (1991) |
| Cross-fault heat transfer increases from ~10 MW (conductive) to ~215 MW (advective) immediately after fault gouge disruption | [Dempsey 2013, pp. 15-16] | Fault core permeability increased by mean of 2.3 orders of magnitude | Reduces to 80 MW after one week, 50 MW after two months |
| Upflow migrates from footwall scarp into hanging wall following fault permeability increase | [Dempsey 2013, pp. 15-16] | Permanent increase in cross-fault permeability | Migration would be halted/reversed by hydrothermal mineralization sealing |
| Reservoir heat content reduction of ~60-80 TJ from pore-pressure perturbation | [Dempsey 2013, pp. 13-14] | Upper 2 km reservoir, preseismic value ~9000 PJ | Perturbation is minor compared to absolute reservoir size |
| Steady-state mass flow increase of ~14-15 kg s⁻¹ (about 5%) from permeability disruption | [Dempsey 2013, pp. 14-15] | Mean of 100 stochastic fault plane rupture simulations | Sensitive to degree of fault damage |
| Footwall upflow transports 115 MW, hanging wall 100 MW, with 10 MW cross-fault conductive link | [Dempsey 2013, pp. 15-16] | Impermeable fault core (4 orders of magnitude reduction) | Cross-fault coupling is dominantly conductive (>90%) |
| Modeled earthquake magnitude M=5.7 derived from 0.83 m displacement, 4 GPa shear modulus, 25 km rupture length | [Dempsey 2013, pp. 5-6] | Plane-strain mechanical model, 12th seismic cycle | Consistent with credible M>6 event likelihood on Paeroa Fault |
| Skempton coefficient B=0.7 used for fractured crystalline rock | [Dempsey 2013, pp. 4-5] | Coseismic stress-to-pressure conversion | Value from Talwani et al. (1999), also used by Deng et al. (2010) |
| Surface heat flux anomaly of >20 W m⁻² at footwall scarp at 1 day post-earthquake | [Dempsey 2013, pp. 11-12] | Total pore-pressure anomaly (surface + deep components) | Anomaly is order of magnitude less at 62 days, and again at 3 years |

## Limitations

- The model uses a single-porosity description that enforces thermal equilibrium between fluid and rock matrix, preventing modeling of temperature transients documented at mid-ocean ridge hydrothermal systems [Dempsey 2013, pp. 11-12].
- The plane-strain assumption limits applicability to the middle sections of a normal fault; the model cannot investigate hydrological effects near lateral fault tips [Dempsey 2013, pp. 3-4].
- The model does not account for local topography, permeability heterogeneity, or complex fault geometry [Dempsey 2013, pp. 9-10].
- The inclined mesh does not account for the topographical offset between two fault blocks that naturally evolves after many seismic cycles [Dempsey 2013, pp. 7-7].
- The model does not consider the effects of mechanical or chemical sealing of the fault gouge in the postseismic period [Dempsey 2013, pp. 7-8].
- The approach employs one-way coupling between mechanical and hydrothermal systems; two-way coupling (e.g., fluid diffusion controlling aftershock distribution) is not represented [Dempsey 2013, pp. 15-16].
- The model ignores dynamic effects such as wave propagation and rate-state friction in the mechanical model [Dempsey 2013, pp. 4-5].
- The modeled mass flow decline does not reproduce the exponential decay observed by Briggs (1991) or the linear decrease proposed by Muir-Wood and King (1993) [Dempsey 2013, pp. 12-13].
- Pressure-dependent permeability effects (fracture aperture changes with pore-pressure) are not accounted for [Dempsey 2013, pp. 12-13].
- The model does not include a surrounding fault damage zone with higher permeability [Dempsey 2013, pp. 7-7].
- The back-tilted footwall block evolution at Te Kopia (gradual lowering of water table) is not accounted for [Dempsey 2013, pp. 9-10].

## Assumptions / Conditions

- Coseismic stress changes are sufficiently rapid that induced fluid transport is negligible during the seismic period (undrained assumption) [Dempsey 2013, pp. 4-5].
- The fault is 2 m wide and impermeable, behaving as a partition between fluid flow in adjacent fault blocks [Dempsey 2013, pp. 1-1].
- The along-strike length of the fault is much greater than its depth, justifying the plane-strain assumption [Dempsey 2013, pp. 3-4].
- The dimension of the fault is large compared to the diameter of the geothermal plume [Dempsey 2013, pp. 7-8].
- Stress changes from the 2-D mechanical model are extrapolated to 3-D without alteration in the along-strike dimension [Dempsey 2013, pp. 7-8].
- An elastic modulus of 10¹⁰ Pa and a Poisson's ratio of 0.25 (drained parameters) are used; the authors note that use of drained parameters has minimal impact on model outcomes compared to undrained parameters [Dempsey 2013, pp. 5-6].
- The depth to the brittle-ductile transition (6–8 km) is determined by material parameters, a temperature gradient of 35°C km⁻¹, and a bulk strain rate of 6 × 10⁻¹⁵ s⁻¹ [Dempsey 2013, pp. 4-5].
- The upper 2 km of the TVZ is characterized by low-density Quaternary volcanic strata; below this, fluid flow is hosted within fractured greywacke basement rock [Dempsey 2013, pp. 6-7].
- Permeability decreases exponentially with depth to approximate pore compaction and fracture closure effects [Dempsey 2013, pp. 6-7].
- The fault core permeability reduction of 4 orders of magnitude is constant with depth [Dempsey 2013, pp. 7-7].
- The stochastic permeability fluctuation on the fault plane uses a power-law with exponent -1.3, based on observations from fractured oil reservoirs [Dempsey 2013, pp. 7-8].

## Key Variables / Parameters

| Variable | Value/Range | Description |
|----------|-------------|-------------|
| Fault dip angle | 65° | Consistent with average dip of TVZ faults |
| Fault depth extent | 15 km | Intersection depth of planar fault |
| Fault core thickness | 2 m | Within range of field observations (<10 m) |
| Fault core permeability contrast | -4 orders of magnitude | Relative to depth-dependent background |
| Skempton's coefficient (B) | 0.7 | For fractured crystalline rock |
| Extensional velocity boundary | 12 mm yr⁻¹ | Applied to mechanical model |
| Single-event displacement | 0.83 m | Modeled coseismic fault slip |
| Modeled earthquake magnitude | ~M 5.7 | Derived from displacement, shear modulus, rupture length |
| Shear modulus | 4 GPa | Used in magnitude calculation |
| Surface permeability | -13.8 log(m²) | At z = 0 |
| Contact permeability | -14.5 log(m²) | At z = -2 km |
| Basal permeability | -14.7 log(m²) | At z = -8 km |
| Thermal conductivity | 2.5 W m⁻¹ K⁻¹ | Rock matrix |
| Rock density | 2800 kg m⁻³ | |
| Rock specific heat capacity | 1000 J kg⁻¹ K⁻¹ | |
| Basal temperature range | 150–340°C | Radial Gaussian distribution |
| Natural-state mass flux | 360 kg s⁻¹ | From geothermal upflow zone |
| Immediate postseismic excess mass flux | 740 kg s⁻¹ | 206% increase |
| Preseismic cross-fault heat transfer | ~10 MW | Conductive |
| Postseismic cross-fault heat transfer | ~215 MW | Advective, immediately after rupture |
| Reservoir heat content (preseismic) | ~9000 PJ | Upper 2 km of model domain |
| Permeability fluctuation mean increase | 2.3 orders of magnitude | On fault plane after disruption |
| Permeability fluctuation max increase | 4 orders of magnitude | On fault plane after disruption |
| Temperature gradient | 35°C km⁻¹ | Used in mechanical model |
| Bulk strain rate | 6 × 10⁻¹⁵ s⁻¹ | Used in mechanical model |

## Reusable Claims

- Coseismic pore-pressure changes from normal fault rupture cause a short-term (several weeks) increase in heat and mass fluxes at the surface of a hydrothermal system, dominated by near-surface horizontal compression rather than deep slip-arrest effects [Dempsey 2013, pp. 1-1, 15-16].
- An impermeable fault core operating as a fluid-flow barrier causes geothermal upflow to localize along the fault plane in both the footwall (where fluids are physically deflected) and the hanging wall (due to thermodynamic stability along a heated partition and horizontal hydrostatic pressure from downflow) [Dempsey 2013, pp. 15-16].
- Permanent increases in cross-fault permeability from fault gouge disruption lead to migration of geothermal upflow from the footwall into the hanging wall and away from the fault, with a sustained ~5% increase in steady-state mass flow [Dempsey 2013, pp. 15-16].
- The diffusive processes governing postseismic pore-pressure redistribution are additive; the full phenomenon can be modeled as a superposition of its constituent surface and deep components [Dempsey 2013, pp. 12-13].
- Cross-fault conductive heat transfer across a 2 m thick fault core is small (~10 MW) compared to total vertical heat transfer (~200 MW), indicating weak thermal coupling between adjacent fault blocks [Dempsey 2013, pp. 9-10].
- The position of a deep heat source relative to a structural permeability barrier (fault) controls plume structure: a heat source confined to the footwall produces tight, concentrated upflow deflected along the fault, while displacement into the hanging wall produces a larger, more distributed upflow zone [Dempsey 2013, pp. 9-10].

## Candidate Concepts

- [[dip-slip fault]]
- [[hydrothermal plume]]
- [[coseismic pore-pressure change]]
- [[fault permeability disruption]]
- [[Skempton coefficient]]
- [[Taupo Volcanic Zone]]
- [[Paeroa Fault]]
- [[Te Kopia geothermal system]]
- [[fault gouge]]
- [[structural permeability]]
- [[fluid-flow barrier]]
- [[brittle-ductile transition]]
- [[Mohr-Coulomb failure]]
- [[poroelastic effect]]
- [[geothermal reservoir heat content]]
- [[cross-fault permeability]]
- [[conjugate convection]]
- [[hydraulic diffusivity]]
- [[normal fault earthquake]]
- [[seismic cycle]]

## Candidate Methods

- [[Finite Element Heat and Mass transfer code (FEHM)]]
- [[Abaqus/Standard finite element modeling]]
- [[plane-strain mechanical fault model]]
- [[Skempton pore-pressure conversion]]
- [[stochastic permeability fluctuation field]]
- [[radial Gaussian temperature boundary condition]]
- [[exponentially decreasing permeability profile]]
- [[mixed 2-D/3-D modeling approach]]
- [[seismic cycle spin-up procedure]]
- [[linear interpolation between unstructured and structured grids]]

## Connections To Other Work

- The mechanical model was originally developed to investigate postseismic stress rotation [Nüchter and Ellis, 2010], fault energetics [Dempsey et al., 2012a], and frictional failure over multiple seismic cycles [Dempsey et al., 2012b] [Dempsey 2013, pp. 3-4].
- The FEHM code has been used to model convection in air [Stauffer et al., 1997], groundwater convection modified by dynamic permeability in heated [Dempsey et al., 2012c] and cool environments [Chaudhuri et al., 2009] [Dempsey 2013, pp. 5-6].
- The coseismic stress change pattern is similar to volumetric strain changes obtained by Ge and Stover [2000] using a 3-D elastic displacement model [Dempsey 2013, pp. 5-6].
- The study builds on observations of hydrological effects of earthquakes cataloged by Muir-Wood and King [1993], Rojstaczer et al. [1995], Quilty and Roeloffs [1997], and others [Dempsey 2013, pp. 1-2].
- The approach of using Skempton's coefficient to convert stress changes to pore-pressure changes follows Quilty and Roeloffs [1997], Grecksch et al. [1999], and Zhang and Huang [2011] [Dempsey 2013, pp. 1-2].
- The modeled fluid flow shares similarities with analytical and numerical solutions to conjugate conduction-natural-convection problems in vertically partitioned domains [Sakakibara et al., 1992; Kahveci, 2007] and inclined domains [Varol et al., 2010] [Dempsey 2013, pp. 9-10].
- The study connects to observations of geyser periodicity changes following earthquakes [Ingebritsen and Rojstaczer, 1996; Husen et al., 2004; Vandemeulebrouck et al., 2008] [Dempsey 2013, pp. 2-3].
- The pore-pressure diffusion approach coupled to Mohr-Coulomb failure has been used to model aftershock sequences [Lindman et al., 2010] [Dempsey 2013, pp. 3-4].

## Open Questions

- How would two-way coupling between the mechanical and hydrothermal systems (where fluid flow anomalies induce subsequent fault failure) affect the modeled outcomes? [Dempsey 2013, pp. 15-16]
- What are the timescales and effects of hydrothermal mineralization and self-sealing of fault gouge in the postseismic period on the migration of upflow into the hanging wall? [Dempsey 2013, pp. 14-15]
- How would a dual-porosity description of fracture flow affect the modeling of postseismic temperature transients? [Dempsey 2013, pp. 11-12]
- What role does pressure-dependent permeability (fracture aperture changes with pore-pressure) play in the postseismic decay of mass flow? [Dempsey 2013, pp. 12-13]
- How would the inclusion of a fault damage zone with higher permeability surrounding the fault core affect the modeled plume structure and postseismic response? [Dempsey 2013, pp. 7-7]
- How do hydrological effects differ near the lateral tips of normal faults where the plane-strain assumption is invalid? [Dempsey 2013, pp. 3-4]

## Source Coverage

All 21 non-empty indexed fragments were processed. The compilation covers the full paper from title through references, including the abstract, introduction (sections 1 and 1.1), numerical methods (sections 2, 2.1, 2.2, 2.3, 2.3.1, 2.3.2), results (sections 3, 3.1, 4, 4.1, 4.2, 5, 5.1), conclusion (section 6), acknowledgments, and references. Coverage ratio by blocks: 1.0 (21/21). Coverage ratio by characters: 1.005.
