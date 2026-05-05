---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-tang-基于有限体积方法的复杂裂缝数值模拟研究-research-on-numerical-simulation-of-complex-fractures-based-on-fin"
title: "基于有限体积方法的复杂裂缝数值模拟研究 [Research on Numerical Simulation of Complex Fractures Based on Finite Volume Method]."
status: "draft"
source_pdf: "data/papers/2023 - 基于有限体积方法的复杂裂缝数值模拟研究.pdf"
collections:
  - "大论文-离散裂缝网络"
citation: "Tang, Chao. \"基于有限体积方法的复杂裂缝数值模拟研究 [Research on Numerical Simulation of Complex Fractures Based on Finite Volume Method].\" Doctoral dissertation, Southwest Petroleum University, 2019."
indexed_texts: "59"
indexed_chars: "290341"
nonempty_source_blocks: "59"
compiled_source_blocks: "59"
compiled_source_chars: "291641"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004477"
coverage_status: "full-index"
source_signature: "4f5f34cd7001ca9a5ee885676888e6269fe748f9"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-04T23:16:14"
---

# 基于有限体积方法的复杂裂缝数值模拟研究 [Research on Numerical Simulation of Complex Fractures Based on Finite Volume Method].

## One-line Summary

This doctoral dissertation develops static fracture network characterization methods using multifractal theory and percolation theory, and establishes a finite volume method-based numerical simulation framework for complex multi-scale fractured reservoirs, applied to shale gas multi-stage fractured horizontal wells and waterflooding in fractured oil reservoirs.

## Research Question

The research addresses three main problems in fractured reservoir characterization and simulation: (1) the inability of Poisson point processes to describe the clustering effect of fracture networks, (2) the lack of quantitative methods for evaluating fracture network connectivity, and (3) the limitations of existing numerical methods (finite difference and finite element) in handling complex fracture geometries while maintaining local mass conservation [Tang 2019, pp. 1-6].

## Study Area / Data

The study uses synthetic models and field data from a carbonate fractured reservoir block, where seismic attribute body data (ant tracking data) were used to identify fracture networks at different depths [Tang 2019, pp. 41-44]. The shale gas application uses parameters from literature [Tang 2019, pp. 107-111]. The fractured oil reservoir waterflooding application uses a 100m × 100m model domain [Tang 2019, pp. 132-136].

## Methods

The dissertation employs several interconnected methodological approaches:

**Static Fracture Network Modeling:** Multifractal methods are used to generate fracture centroid distributions with clustering effects, replacing the traditional Poisson random process. The method uses a generalized fractal spectrum (Eq. 2-16) with correlation dimension Dq=2 to control fracture positioning [Tang 2019, pp. 37-41]. Fracture orientations are modeled using Von-Mises distribution (2D) and bimodal Fisher distribution (3D) [Tang 2019, pp. 34-37]. Fracture sizes follow log-normal or power-law distributions [Tang 2019, pp. 30-34].

**Connectivity Analysis:** Percolation theory combined with Monte Carlo simulation is applied to quantify fracture network connectivity. An improved dimensionless fracture density expression (Eq. 2-36) incorporating excluded volume concepts accounts for fracture direction distribution effects [Tang 2019, pp. 51-55]. A new connectivity degree scaling relationship (Eq. 2-37) incorporating the correlation dimension is proposed [Tang 2019, pp. 55-58].

**Finite Volume Discretization:** The flow governing equations are discretized using a cell-centered finite volume method on unstructured grids. The method uses Gauss numerical integration for surface fluxes, with super-relaxation correction for non-orthogonal diffusion terms [Tang 2019, pp. 62-68]. For convection terms, a bounded high-order upwind scheme is constructed by applying the Convection Boundedness Criterion to QUICK format [Tang 2019, pp. 127-132].

**Multi-scale Fracture Treatment:** Large-scale fractures are dimensionally reduced to 2D surface elements (3D) or 1D line elements (2D) within the mesh, while small-scale natural micro-fractures are treated as a dual-continuum medium with the matrix [Tang 2019, pp. 111-114, 129-132]. A dimensionless fracture opening coefficient is introduced to preserve virtual volume for flow continuity [Tang 2019, pp. 111-114].

**Shale Gas Model:** The model incorporates Langmuir isothermal adsorption, Knudsen diffusion, and slip effects for gas flow in micro-nano pores, with apparent permeability correction (Eq. 4-14) [Tang 2019, pp. 111-114].

**Two-Phase Flow Model:** IMPES sequential solution method is used for oil-water two-phase flow, with pressure solved implicitly and saturation solved explicitly [Tang 2019, pp. 131-132].

## Key Findings

1. **Fractal characterization of fracture networks:** The multifractal method effectively describes non-uniform fracture distributions with clustering effects. For 2D models, stronger clustering corresponds to correlation dimension closer to 1; for 3D models, closer to 2 [Tang 2019, pp. 1-6, 55-58].

2. **Connectivity thresholds:** For uniformly distributed fixed-length fracture networks, the critical dimensionless fracture density is 3.5. As clustering effect increases, the critical density value increases, overall network connectivity decreases, but local connectivity increases [Tang 2019, pp. 1-6, 55-58].

3. **Finite volume method advantages:** Compared to other discrete methods, the finite volume method balances flexibility and accuracy, suitable for complex boundary problems. Applying boundedness conditions to high-order upwind schemes improves accuracy for saturation discontinuities at large-scale fractures and suppresses non-physical oscillations [Tang 2019, pp. 1-6, 127-132].

4. **Shale gas adsorption/desorption:** Adsorption and desorption mainly occur within the stimulated reservoir volume, providing pressure supplementation but having insignificant impact on productivity. As matrix pore size increases, Knudsen diffusion and slip effects on shale gas productivity gradually weaken [Tang 2019, pp. 1-6, 121-127].

5. **Fracture control on saturation distribution:** Fractures have significant control over saturation distribution. Small-scale fracture clustering increases the complexity of oil-water front morphology, while large-scale fractures exert stronger control over the oil-water front [Tang 2019, pp. 1-6, 135-142].

6. **Fracture direction and connectivity:** Fracture network connectivity is not only related to fracture density but also to fracture direction distribution. As direction distribution transitions from isotropic to anisotropic, connectivity first increases then decreases [Tang 2019, pp. 51-55].

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| Critical dimensionless fracture density for uniform fixed-length networks is 3.5 | [Tang 2019, pp. 55-58] | 2D, uniform direction distribution, fixed-length fractures | Verified through Monte Carlo simulation with characteristic lengths 5, 10, 20 |
| Correlation dimension Dc=1.69 and capacity dimension 1.81 for real carbonate reservoir fracture data | [Tang 2019, pp. 41-44] | Seismic attribute body data from a specific oilfield block | Multifractal method generated networks with Dc=1.68 (0.6% error) vs Poisson process Dc=1.79 (5.9% error) |
| Finite volume method results match Eclipse commercial software for conventional gas well model | [Tang 2019, pp. 107-111] | 2000m×2000m×50m reservoir, 15 fracturing stages, infinite conductivity fractures | Good agreement in daily gas production curves |
| Bounded QUICK scheme suppresses non-physical oscillations at saturation discontinuities | [Tang 2019, pp. 127-132] | Oil-water two-phase flow with large-scale fractures | Compared against first-order upwind (smooth but inaccurate) and standard QUICK (oscillatory) |
| Adsorption/desorption has insignificant effect on shale gas productivity | [Tang 2019, pp. 121-127] | Multi-stage fractured horizontal well, Langmuir volumes 0.002-0.006 m³/kg | Main effect is pressure supplementation in stimulated volume |
| Large-scale fractures control saturation distribution more than small-scale fractures | [Tang 2019, pp. 135-142] | 100m×100m fractured reservoir waterflooding model | Compared models with and without large-scale fractures |
| Fracture orientation affects water breakthrough time | [Tang 2019, pp. 138-142] | Single large-scale fracture at 0°, 45°, 90° to injection-production line | Smaller angle leads to earlier breakthrough and faster water cut rise |

## Limitations

1. The small-scale fracture network was simplified as an equivalent dual-continuum medium rather than explicitly represented, which may not capture local clustering effects on flow [Tang 2019, pp. 156-158].

2. The shale gas model assumes single-component methane and does not consider competitive adsorption effects [Tang 2019, pp. 99-102].

3. The model does not consider stress sensitivity of fractures or temperature field coupling [Tang 2019, pp. 156-158].

4. The IMPES method requires strict time step limitations for stability, and sequential solution shows differences from fully implicit solution in early production periods [Tang 2019, pp. 117-121].

5. The 3D fracture network modeling and simulation capability is limited; the methods presented are still far from practical engineering application for large-scale 3D problems [Tang 2019, pp. 156-158].

6. The percolation model's validity for densely fractured systems remains debated, especially when using continuous percolation models to study random fracture networks [Tang 2019, pp. 16-19].

## Assumptions / Conditions

- Fracture networks exhibit fractal self-similarity in rock fragmentation processes [Tang 2019, pp. 14-16]
- Shale gas reservoir is a single-phase flow system (water cannot enter matrix micropores) [Tang 2019, pp. 99-102]
- Isothermal flow processes in all models [Tang 2019, pp. 99-102, 118-119]
- Matrix-microfracture system follows Warren-Root dual-porosity dual-permeability model [Tang 2019, pp. 118-119]
- Large-scale fractures are dimensionally reduced (2D surface elements in 3D, 1D line elements in 2D) [Tang 2019, pp. 111-114, 129-132]
- Fluid is slightly compressible, rock is rigid [Tang 2019, pp. 118-119]
- Capillary pressure is continuous at matrix-fracture interfaces [Tang 2019, pp. 131-132]
- Gravity effects are neglected in shale gas model [Tang 2019, pp. 99-102]
- Gas diffusion in shale matrix is a non-equilibrium quasi-steady-state process [Tang 2019, pp. 99-102]

## Key Variables / Parameters

- **Dc** — Correlation dimension of fracture centroid distribution (dimensionless); controls clustering intensity [Tang 2019, pp. 37-41]
- **ρex** — Improved dimensionless fracture density incorporating excluded volume and direction distribution (dimensionless) [Tang 2019, pp. 51-55]
- **ρc** — Critical dimensionless fracture density at percolation threshold (dimensionless); equals 3.5 for uniform 2D networks [Tang 2019, pp. 55-58]
- **Ie** — Fracture network connectivity degree (dimensionless); defined by Eq. 2-37 [Tang 2019, pp. 55-58]
- **dhf** — Dimensionless fracture opening (dimensionless); used to describe relative opening of hydraulic fractures [Tang 2019, pp. 111-114]
- **Kn** — Knudsen number (dimensionless); characterizes gas flow regime in nanopores [Tang 2019, pp. 111-114]
- **VL, pL** — Langmuir volume (m³/kg) and Langmuir pressure (MPa); describe adsorption isotherm [Tang 2019, pp. 111-114]
- **α** — Shape factor for matrix-fracture transfer (m⁻²) [Tang 2019, pp. 118-119]
- **Sf** — Surface vector of control volume face [Tang 2019, pp. 62-68]
- **Ef, Tf** — Orthogonal and non-orthogonal components of surface vector decomposition [Tang 2019, pp. 79-84]

## Reusable Claims

1. **Multifractal method for fracture positioning:** Using multifractal methods with correlation dimension Dq=2 to control fracture centroid generation produces networks with clustering effects that better match real fracture distributions than Poisson processes, with relative errors below 1% for both correlation and capacity dimensions [Tang 2019, pp. 41-44].

2. **Percolation threshold for uniform fracture networks:** For 2D finite systems with uniformly distributed fixed-length fractures and random orientations, the critical dimensionless fracture density (using the improved definition incorporating excluded volume) is approximately 3.5, below which the network has essentially no permeability contribution [Tang 2019, pp. 55-58].

3. **Clustering reduces overall connectivity:** Increasing fracture network clustering (decreasing correlation dimension) increases the percolation threshold, meaning more fractures are needed to achieve network-wide connectivity, even though local connectivity within clusters increases [Tang 2019, pp. 55-58].

4. **Bounded high-order upwind scheme:** Applying the Convection Boundedness Criterion to QUICK format creates a bounded scheme that maintains second-order accuracy while suppressing non-physical oscillations at saturation discontinuity interfaces in fractured media [Tang 2019, pp. 127-132].

5. **Dimensionless fracture opening for flow continuity:** Introducing a dimensionless fracture opening coefficient in dimensionally-reduced fracture models creates virtual volume space that ensures flow continuity and prevents instantaneous fluid passage through fractures, while enabling equivalent simulation of stimulated reservoir volume parameters [Tang 2019, pp. 111-114].

6. **Large-scale fractures dominate saturation distribution:** In fractured reservoirs, large-scale fractures exert significantly stronger control over saturation distribution than small-scale fractures, making identification and characterization of large-scale fracture systems critical for waterflooding optimization [Tang 2019, pp. 135-142].

7. **Fracture orientation affects connectivity non-monotonically:** As fracture direction distribution transitions from isotropic to strongly anisotropic, network connectivity first increases (reaching maximum at slight preferred orientation) then decreases, indicating that optimal connectivity requires both directional spread and a degree of preferred orientation [Tang 2019, pp. 51-55].

## Candidate Concepts

- [[discrete fracture network]]
- [[dual porosity dual permeability model]]
- [[percolation theory]]
- [[fractal dimension]]
- [[multifractal method]]
- [[finite volume method]]
- [[cell-centered control volume]]
- [[unstructured mesh]]
- [[Knudsen diffusion]]
- [[slip effect]]
- [[Langmuir adsorption]]
- [[dimensionless fracture density]]
- [[excluded volume]]
- [[correlation dimension]]
- [[connectivity degree]]
- [[percolation threshold]]
- [[IMPES method]]
- [[convection boundedness criterion]]
- [[non-orthogonal correction]]
- [[dimensional reduction of fractures]]
- [[stimulated reservoir volume]]
- [[cluster effect]]
- [[fracture network connectivity]]
- [[equivalent permeability]]

## Candidate Methods

- [[multifractal fracture network generation]]
- [[Monte Carlo percolation simulation]]
- [[finite volume method on unstructured grids]]
- [[bounded QUICK scheme]]
- [[super-relaxation non-orthogonal correction]]
- [[cell-centered finite volume discretization]]
- [[Gauss numerical integration]]
- [[IMPES sequential solution]]
- [[Newton-Raphson iteration]]
- [[matrix preconditioning]]
- [[dimensional reduction for large-scale fractures]]
- [[excluded volume calculation for dimensionless density]]
- [[two-point correlation function for fractal analysis]]
- [[box-counting method for capacity dimension]]
- [[scanline method for directional fractal dimension]]
- [[Von-Mises distribution for fracture orientation]]
- [[bimodal Fisher distribution for 3D fracture orientation]]
- [[log-normal distribution for fracture size]]
- [[power-law distribution for fracture size]]

## Connections To Other Work

The dissertation builds upon and extends several research traditions:

- **Fractal analysis of fractures:** Extends Barton and Larsen (1985) box-counting methods and Bunde and Havlin (1995) mass dimension methods, incorporating Babadagli (2001) scanline dimension for directional characterization [Tang 2019, pp. 14-16].

- **Percolation theory in fracture networks:** Extends Berkowitz (1995) continuous percolation model and Mourzenko et al. (2000-2005) systematic studies, proposing improved dimensionless density expressions that account for direction distribution [Tang 2019, pp. 16-19].

- **Finite volume method in reservoir simulation:** Builds on Brad (1989) introduction of finite volume concepts to reservoir simulation, Amado (1994) triangular grid implementation, and Yao Jun's team (2010-2015) discrete fracture model with finite volume method [Tang 2019, pp. 23-25].

- **Embedded discrete fracture models:** Connects to Zhou Fangqi and Huang Chaoqin (2014) embedded DFN models and Bosma et al. (2017) multiscale finite volume discrete fracture modeling [Tang 2019, pp. 19-21].

- **Shale gas flow mechanisms:** Extends Javadpour (2009) nanopore flow model and Kamidakiadis et al. (1991) slip boundary research for effective viscosity correction [Tang 2019, pp. 111-114].

- **Warren-Root dual medium model:** Applies the classical Barenblatt-Zheltov (1960) and Warren-Root (1963) framework for matrix-microfracture interaction [Tang 2019, pp. 19-21].

## Open Questions

1. How can the multifractal static modeling method be further improved to better capture the spatial correlation between fracture orientation and clustering patterns?

2. What is the appropriate scale transition criterion for determining which fractures should be treated as discrete versus continuum in multi-scale models?

3. How does the bounded high-order upwind scheme perform under highly heterogeneous permeability fields with extreme contrasts between matrix and fractures?

4. Can the percolation-based connectivity analysis be extended to three-dimensional fracture networks with complex intersection geometries?

5. How should the dimensionless fracture opening coefficient be calibrated against field data for specific reservoir conditions?

6. What is the impact of stress-dependent fracture aperture changes on the connectivity and flow behavior predicted by the static percolation model?

7. How can the finite volume method be adapted for coupled thermo-hydro-mechanical problems in fractured reservoirs?

## Source Coverage

All non-empty indexed fragments were processed. The coverage audit confirms: 59 indexed text blocks, 290,341 indexed characters, 59 non-empty source blocks, 59 compiled source blocks, 291,641 compiled characters, coverage ratio by blocks = 1.0, coverage ratio by characters = 1.004477, coverage status = full-index. The compilation strategy was single-pass markdown with a single-pass character budget of 320,000.
