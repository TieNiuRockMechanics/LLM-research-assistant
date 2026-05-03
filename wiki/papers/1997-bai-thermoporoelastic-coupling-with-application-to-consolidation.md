---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "1997-bai-thermoporoelastic-coupling-with-application-to-consolidation"
title: "Thermoporoelastic Coupling with Application to Consolidation."
status: "draft"
source_pdf: "data/papers/1997 - Thermoporoelastic Coupling with Application to Consolidation.pdf"
collections:
  - "part3-3"
citation: "Bai, M., and Y. Abousleiman. \"Thermoporoelastic Coupling with Application to Consolidation.\" *International Journal for Numerical and Analytical Methods in Geomechanics*, vol. 21, 1997, pp. 121-32."
indexed_texts: "6"
indexed_chars: "26447"
nonempty_source_blocks: "6"
compiled_source_blocks: "6"
compiled_source_chars: "26558"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004197"
coverage_status: "full-index"
source_signature: "115c55d637b89efb4f910633cd45d9ff7b8270a2"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T11:34:07"
---

# Thermoporoelastic Coupling with Application to Consolidation.

## One-line Summary
The paper examines conditions under which fully coupled thermoporoelastic formulations must be maintained versus situations where partial or full decoupling can be justified, using an analytical one‑dimensional non‑isothermal consolidation scenario to illustrate the coupling sensitivity of pressure, temperature, and displacement.

## Research Question
Under what general conditions should the full thermoporoelastic coupling be preserved, and when can a partial or full decoupling technique be applied, as demonstrated in a 1‑D consolidation problem under non‑isothermal conditions?[Bai 1997, pp. 1-2]

## Study Area / Data
The study is not a field investigation but a theoretical analysis of a one‑dimensional consolidation column. The column has height \( h = 100 \, \text{m} \), a laterally confined, rigid, impermeable, and adiabatic base, and an instantaneous top load \( F_0 = 10^8 \, \text{Pa} \). The top boundary (\( x = 0 \)) is drained (\( p = 0 \)) and isothermal (\( T = 0 \)). Initial pore pressure is \( p_0 = 10^4 \, \text{Pa} \) and initial temperature \( T_0 = 100^\circ \text{C} \).[Bai 1997, pp. 4-5] The full set of material parameters used in the comparative analysis is given in Table I.[Bai 1997, pp. 7-9]

## Methods
A **fully coupled thermoporoelastic formulation** (Eqs. 1–3) is presented, coupling momentum, mass, and energy conservation with cross‑dependent terms (e.g., pore‑pressure influence on effective stress, thermal strain effects, etc.).[Bai 1997, pp. 1-3]  
Three **partial decoupling schemes** (Case 1 through Case 3) are described, in which certain coupling terms are omitted based on physical arguments (e.g., neglecting deformation, neglecting thermal convection, or neglecting rate‑change effects of volumetric strain on mass/energy balance).[Bai 1997, pp. 3-4]  
A **1‑D consolidation model** is formulated for a non‑isothermal column without forced convection or internal sources (Eqs. 19–22). The coupled equations are reduced to two simultaneous diffusion‑type equations (Eqs. 26–27), which are solved by **finite Fourier transform** (Eqs. 29–30). Closed‑form series solutions are obtained for pressure (Eq. 38), temperature (Eq. 39), and displacement (Eq. 42).[Bai 1997, pp. 5-7]  
A **comparative analysis** is then performed, evaluating full coupling, total decoupling, and partial decoupling (deformation decoupled, temperature decoupled) using the parameters of Table I and normalized variables.[Bai 1997, pp. 8-9]

## Key Findings
* **Pressure analysis is highly sensitive to coupling.** With full coupling, pressure dissipation is substantially delayed and displays a distinct slope perturbation compared with total decoupling (purely diffusive flow). Partial decoupling that neglects deformation yields a less uniform pressure evolution, while decoupling of temperature gives an intermediate response. Full coupling is critical for realistic pressure predictions. [Bai 1997, pp. 9-10]
* **Temperature and displacement are relatively insensitive to coupling.** Under the tested conditions, the various coupling schemes produce negligibly small discrepancies in temperature and displacement evolution. Sequential decoupled solutions are therefore justifiable for these variables (Figs. 4, 5). [Bai 1997, pp. 10-11]
* **Spatial pressure profiles at late time (\( q = 1000 \))** show the same ordering: full coupling gives the largest pressure magnitudes, temperature decoupling lies in between, and deformation‑decoupled (or totally decoupled) solutions yield the most conservative (lowest) pressure changes. [Bai 1997, pp. 11-12]
* **The above conclusions are conditional on the assumed simplifications** (no forced thermal convection, no fluid or heat sources). Altering these conditions may dramatically modify the results. [Bai 1997, pp. 10-11]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| Full coupling delays pressure dissipation and causes a slope perturbation; total decoupling gives a purely diffusive pressure (Fig. 3). | [Bai 1997, pp. 9-10] | 1‑D consolidation, no convection, no sources, parameters from Table I. | Pressure is the most coupling‑sensitive variable. |
| Partial decoupling that discards deformation produces a less uniform (“radical”) pressure evolution; decoupling temperature gives an intermediate result between full coupling and total decoupling (Fig. 3). | [Bai 1997, pp. 9-10] | Same as above. | Coupling with deformation is important for pressure behaviour. |
| Temperature and displacement solutions are almost identical across all coupling schemes (Figs. 4, 5). | [Bai 1997, pp. 10-11] | Same as above. | Allows sequential solutions from a decoupled thermal transport equation. |
| Spatial pressure distribution at \( q=1000 \) shows that full coupling yields the largest pressure and deformation‑decoupled the smallest; temperature‑decoupled case lies in between (Fig. 6). | [Bai 1997, pp. 11-12] | Same as above. | Spatial variation follows the same trend as temporal evolution. |
| The full coupling results could change significantly if fluid/heat sources or thermal convection are included. | [Bai 1997, pp. 10-11] | Original model assumptions are restrictive. | Decoupling justifications are not universal. |

## Limitations
* The analysis **neglects forced thermal convection and internal fluid/heat sources**. If these mechanisms are present, the decoupling conclusions may no longer hold.[Bai 1997, pp. 10-11]
* The study is limited to a **one‑dimensional, linear, quasi‑steady elastic** medium with **constant, homogeneous properties**. Non‑linearities, heterogeneities, and multi‑dimensional effects are not addressed.
* The comparative results rely on the **specific material parameters given in Table I**. The sensitivity of coupling could differ for other parameter combinations.
* The solution uses a **finite Fourier transform** that assumes **perfectly drained and isothermal top boundary**; other boundary configurations are not tested.

## Assumptions / Conditions
* Linear, quasi‑steady elastic, fluid‑saturated, non‑isothermal porous medium.[Bai 1997, pp. 2-3]
* 1‑D column of height \( h \) with rigid, impermeable, adiabatic base; top surface is drained (\( p=0 \)) and isothermal (\( T=0 \)).[Bai 1997, pp. 4-5]
* Instantaneous external load \( F_0 \) applied at top; no body forces or internal fluid/heat sources.[Bai 1997, pp. 4-5]
* Forced thermal convection is neglected (\( q_f s T_{,k} \) term omitted); Darcy’s law relates fluid velocity to pressure gradient.[Bai 1997, pp. 4-5]
* Material properties (Lame constants, Biot’s coefficient, permeability, thermal expansion coefficients, etc.) are constant and taken from Table I.[Bai 1997, pp. 7-9]
* Small strains; momentum equilibrium is quasi‑steady.[Bai 1997, pp. 2-3]

## Key Variables / Parameters
* **Displacement** \( u \), **pore pressure** \( p \), **temperature** \( T \) (primary unknowns).
* **Lame constants** \( \lambda \), \( G \) (or \( \nu \) and \( E \)); Young’s modulus \( E = 5 \times 10^9 \, \text{Pa} \), Poisson’s ratio \( \nu = 0.25 \).
* **Biot’s coefficient** \( a = 0.9 \); **thermal expansion factor** \( b = a_T (3\lambda + 2G) \), with fluid expansion coefficient \( a_f = 10^{-5} \, /^\circ\text{C} \), solid expansion coefficient \( a_s = 10^{-6} \, /^\circ\text{C} \).
* **Permeability** \( k = 10^{-9} \, \text{m}^2 \), **fluid dynamic viscosity** \( \mu = 20 \, \text{kg/(m·h)} \), porosity \( n = 0.2 \).
* **Lumped compressibility** \( a^* = n/K_f + (1-n)/K_s \) with fluid bulk modulus \( K_f = 5 \times 10^9 \, \text{Pa} \), solid grain bulk modulus \( K_s = 2 \times 10^{10} \, \text{Pa} \).
* **Thermal conductivities** \( K^*_f = 1000 \, \text{J/(m·h·°C)} \), \( K^*_s = 100 \, \text{J/(m·h·°C)} \); **reference temperature** \( T_0 = 100^\circ \text{C} \).
* **External load** \( F_0 = 10^8 \, \text{Pa} \), **initial pressure** \( p_0 = 10^4 \, \text{Pa} \).
* **Consolidation coefficient** \( c_v = k g / \mu \) with \( g = \lambda + 2G \); **dimensionless time** \( q = c_v t / h^2 \).

## Reusable Claims
1. **Reusable Claim:** In a linear, quasi‑steady, non‑isothermal consolidation problem without forced convection and internal sources, the pressure solution is highly sensitive to thermoporoelastic coupling, while temperature and displacement solutions can be accurately obtained from a decoupled thermal analysis – *provided the material parameters are similar to those in Table I.*  
   *Source:* [Bai 1997, pp. 9-11].
2. **Reusable Claim:** Partial decoupling that retains only the influence of temperature on deformation and pressure (i.e., solving thermal diffusion first, then using that result to drive pressure and displacement) yields an intermediate pressure response that lies between fully coupled and totally decoupled solutions; it may be acceptable only if deformation effects on fluid flow are negligible.  
   *Source:* [Bai 1997, pp. 9-10].
3. **Reusable Claim:** For stiff materials or small loading where elastic deformation and thermal convection are negligible, the thermoporoelastic system reduces to a sequential scheme: first solve heat conduction (Eq. 13) to get temperature, then solve pressure diffusion (Eq. 12) with the temperature field as input.  
   *Source:* [Bai 1997, pp. 3-4] (Case 1).
4. **Reusable Claim:** If the influence of rate changes of elastic volumetric deformation on both fluid flow and thermal transport is negligible, the system can be solved in three decoupled steps: (i) thermal diffusion (Eq. 18) → temperature; (ii) pressure diffusion with thermal source (Eq. 17) → pressure; (iii) mechanical equilibrium (Eq. 16) → displacement, using the previously computed \( p \) and \( T \).  
   *Source:* [Bai 1997, pp. 4-5] (Case 3).
5. **Reusable Claim:** The full coupling terms that affect pressure dissipation (e.g., deformation‑driven flow and thermal contraction/expansion) are essential to capture the delay and slope perturbation observed in the column consolidation; omitting them leads to an overly rapid pressure decline.  
   *Source:* [Bai 1997, pp. 9-10] and Fig. 3.
6. **Reusable Claim:** The analytical solutions derived via finite Fourier transform (Eqs. 38, 39, 42) provide exact, closed‑form series representations for 1‑D non‑isothermal consolidation under the given boundary conditions and can be used as benchmarks for numerical codes in coupled THM modelling.  
   *Source:* [Bai 1997, pp. 6-8].

## Candidate Concepts
* [[thermoporoelastic coupling]]
* [[partial decoupling]]
* [[fully coupled thermoporoelastic formulation]]
* [[1-D consolidation]]
* [[non-isothermal consolidation]]
* [[poroelasticity]]
* [[thermoelasticity]]
* [[Biot’s coefficient]]
* [[thermal expansion factor]]
* [[effective stress]]
* [[forced thermal convection]]
* [[lumped compressibility]]
* [[column problem]]
* [[finite Fourier transform]]
* [[dimensionless time q]]
* [[consolidation coefficient]]

## Candidate Methods
* [[finite Fourier transform solution for 1-D consolidation]]
* [[sequential decoupling methods]]
* [[coupled THM modelling]]
* [[comparative coupling analysis]]
* [[analytical thermoporoelastic solutions]]

## Connections To Other Work
* The paper’s fully coupled thermoporoelastic formulation is taken from previous works: Bai & Roegiers (1994) [Ref. 1], Elsworth (1994) [Ref. 2], Jing et al. (1995) [Ref. 3], and Smith & Booker (1993) [Ref. 4].[Bai 1997, pp. 2-3]
* Classic consolidation theories: Biot’s 3‑D consolidation theory (1941) [Ref. 5], Cryer’s comparison (1962) [Ref. 6], and Terzaghi’s theoretical soil mechanics (1943) [Ref. 8] provide the foundation for the 1‑D column model.[Bai 1997, pp. 12-12]
* The DECOVALEX international cooperative project on coupled THM processes (Jing et al. 1995) is explicitly mentioned as a context for multi‑physics coupling in radioactive waste repositories.[Bai 1997, pp. 12-12]

## Open Questions
* How would the addition of **forced thermal convection** (\( q_f s T_{,k} \) term) alter the necessity for full coupling in pressure, temperature, and displacement predictions? The present analysis notes that its omission may be a critical assumption.[Bai 1997, pp. 10-11]
* What is the influence of **internal fluid or heat sources** on the coupling sensitivity? The conclusions state that results could be dramatically modified if such sources are present.[Bai 1997, pp. 10-11]
* To what extent do **heterogeneities** (e.g., spatially varying permeability, stiffness) and **non‑linear** material behaviour change the conditions under which decoupling is acceptable?
* Are the findings transferable to **two‑ or three‑dimensional geometries** and to **mixed boundary conditions** (e.g., partially drained or thermally insulated boundaries)?
* For parameter sets markedly different from those in Table I (e.g., very low permeability, high compressibility), does the ranking of coupling sensitivities (pressure most sensitive, temperature/displacement least sensitive) still hold?

## Source Coverage
All six non‑empty indexed fragments were processed. Full‑text coverage: 6 of 6 source blocks compiled (block‑level ratio 1.0), corresponding to 26,558 source characters with a character‑level coverage ratio of 1.004 (full‑index). No parts of the printed text were omitted; all equations, table, figures, and discussion are represented.
