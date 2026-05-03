---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2020-yao-effects-of-fracture-density-roughness-and-percolation-of-fracture-network-on-heat-flow"
title: "Effects of Fracture Density, Roughness, and Percolation of Fracture Network on Heat-Flow Coupling in Hot Rock Masses with Embedded Three-Dimensional Fracture Network."
status: "draft"
source_pdf: "data/papers/2020 - Effects of fracture density, roughness, and percolation of fracture network on heat-flow coupling in hot rock masses with embedded three-dimensional fracture ne.pdf"
collections:
  - "雷恩学派分形研究"
citation: "Yao, Chi, et al. \"Effects of Fracture Density, Roughness, and Percolation of Fracture Network on Heat-Flow Coupling in Hot Rock Masses with Embedded Three-Dimensional Fracture Network.\" *Geothermics*, vol. 87, 2020, 101846. doi:10.1016/j.geothermics.2020.101846."
indexed_texts: "12"
indexed_chars: "59021"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T00:21:42"
---

# Effects of Fracture Density, Roughness, and Percolation of Fracture Network on Heat-Flow Coupling in Hot Rock Masses with Embedded Three-Dimensional Fracture Network.

## One-line Summary

This paper systematically investigates, through a 3D discrete fracture network (DFN) finite element model, how fracture density, roughness, and network percolation govern the heat-flow coupling behavior in hot fractured rock masses, finding percolation to be the decisive factor [Yao 2020, pp. 1-2].

## Research Question

What are the effects of fracture density, fracture surface roughness, and fracture network percolation on the heat-flow coupling process in hot rock masses containing embedded three-dimensional discrete fracture networks? [Yao 2020, pp. 1-2]

## Study Area / Data

The study is primarily numerical and does not specify a particular geographical study area. The numerical model uses a rectangular domain of 100m × 100m for single-fracture verification and a cubic domain of 100m × 100m × 100m for 3D DFN simulations [Yao 2020, pp. 5-6, 7-9]. The material parameters for the model's verification are adopted from a hypothetical scenario (e.g., rock density of 2820 kg/m³, initial rock temperature of 180°C, inlet water temperature of 40°C for verification; 200°C for the primary model) [Yao 2020, pp. 5-6, 2-3]. Rock matrix properties are drawn from literature, citing granite porosity of ~0.05% and limestone porosity of 5-15%, but the modeled rock type is treated as an isotropic continuous porous medium with low permeability relative to the fractures [Yao 2020, pp. 2-3]. 未从索引片段中确认该模型是否针对某个特定的地热田或场地数据进行了校准。

## Methods

The study develops a heat-flow coupled numerical model for fractured rock masses. The fractured rock mass is conceptualized as a rock matrix and an embedded discrete fracture network (DFN) [Yao 2020, pp. 2-3]. Governing equations for fluid flow and heat transfer in both the matrix (a porous medium) and the fractures (zero-thickness elements) are established, incorporating temperature-dependent fluid density and dynamic viscosity [Yao 2020, pp. 1-2, 3-4]. A fracture roughness correction factor is integrated into the flow equation [Yao 2020, pp. 3-4]. For finite element analysis, a custom-developed mesh discretization procedure is used: the rock matrix is discretized into 3D solid tetrahedral elements, and fractures are modeled as zero-thickness triangular elements sharing nodes with the matrix. The meshing process involves inserting fracture nodes, tetrahedral meshing using TetGen, and integrity verification [Yao 2020, pp. 4-5]. This model is implemented via secondary development in the commercial finite element software COMSOL Multiphysics, utilizing its built-in modules for the rock matrix and the Coefficient Form PDE interface for fractures [Yao 2020, pp. 4-5]. The reliability of the model is verified against an analytical solution for a two-dimensional single-fracture heat-flow coupling problem [Yao 2020, pp. 1-2, 5-6]. Percolation probability is studied using Monte-Carlo tests with 10,000 realizations per group [Yao 2020, pp. 1-2, 7-9].

## Key Findings

- **Percolation as a Decisive Factor:** The percolation of the fracture network is the decisive factor affecting heat-flow coupling. The average outlet flow rate of a percolating network is much larger than that of a non-percolating network under the same fracture density [Yao 2020, pp. 1-2].
- **Effect of Fracture Density on Flow:** The average outlet flow rate has a positive relationship with fracture density, with the slope of the curve increasing as density increases. At the same density, the average outlet flow rate decreases with time due to increasing fluid viscosity as the rock matrix cools [Yao 2020, pp. 6-7].
- **Effect of Fracture Density on Temperature:** The relationship between average outlet temperature and fracture density is categorized into two curve types: convex and concave. The curve transitions from convex to concave as fracture density increases, with thermal breakthrough occurring earlier at higher densities, leading to a prominent "long-tail" effect [Yao 2020, pp. 6-7].
- **Effect of Roughness:** The study intends to investigate the effects of fracture roughness on heat-flow coupling, and its correction factor is included in the model's flow equation [Yao 2020, pp. 1-2, 3-4]. 未从索引片段中确认关于粗糙度对热-流耦合效应的具体定量结论。
- **Percolation Threshold:** A percolation threshold of `P_c = 2.281` was determined from density-probability curves for various fracture diameters, where curves intersect at the same point [Yao 2020, pp. 7-9].

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| Average outlet flow rate positively relates to fracture density, and the curve's slope increases with density. | [Yao 2020, pp. 6-7] | 3D DFN model, 100m cube domain, fracture diameter 20m, uniform distribution. | Seepage capacity increase due to more channels. |
| At the same fracture density, the average outlet flow rate decreases with time. | [Yao 2020, pp. 6-7] | 3D DFN model, transient simulation of 30 years. | Attributed to increased fluid viscosity from matrix cooling. |
| Average outlet temperature curve form (convex vs. concave) changes with increasing fracture density. | [Yao 2020, pp. 6-7] | 3D DFN model. | Linked to earlier thermal breakthrough at high densities. |
| Percolation probability curves for different fracture diameters intersect at a single point, `P_c = 2.281`. | [Yao 2020, pp. 7-9] | Monte-Carlo tests (10,000 times per group), varying fracture density and diameter. | Defines a percolation threshold in terms of a specific density measure `ρ'`. |
| The reliability of the numerical model is confirmed by strong agreement with an analytical solution for a 2D single-fracture heat-flow problem. | [Yao 2020, pp. 5-6] | Temperature variation with time (at x=40, 60, 80m) and with position (at t=10, 50, 100 d) were compared. | Used material parameters from Table 1 in the paper. |
| The percolation of the fracture network is the decisive factor affecting heat-flow coupling. | [Yao 2020, pp. 1-2] | Comparing models with identical fracture density (1.97) that are either percolating or non-percolating. | The outlet flow rate is drastically higher in the percolating case. |

## Limitations

- The model assumes the rock matrix is an isotropic continuous porous medium, which may not capture the full complexity of rock heterogeneity [Yao 2020, pp. 2-3].
- Despite using a 3D DFN, the fracture network is modeled with zero-thickness elements, which simplifies the fracture geometry [Yao 2020, pp. 1-2].
- The maximum temperature considered is 200°C to ensure water remains in a fluid state describable by Darcy's law, limiting the model's applicability to higher-enthalpy supercritical systems [Yao 2020, pp. 2-3].
- The numerical model, while verified against a 2D analytical single-fracture solution, is a specific implementation in COMSOL Multiphysics. 未从索引片段中确认该模型是否经过其他现场数据或实验结果的验证。
- The definition of fracture density (`ρ'`) used in the percolation study is based on the excluded volume concept [Yao 2020, pp. 5-6]. 未从索引片段中确认其与其他常用密度指标（如 P32）的具体换算关系。

## Assumptions / Conditions

- **Model Structure:** Fractured rock mass is composed of a discrete fracture network and a rock matrix. Fractures are modeled as zero-thickness elements sharing nodes with the matrix [Yao 2020, pp. 1-2].
- **Rock Matrix:** The rock matrix is assumed to be an isotropic, continuous porous medium with permeability that is small relative to that of the fracture network. Seepage in the rock matrix is considered [Yao 2020, pp. 2-3].
- **Fluid State:** The initial water pressure is 6 MPa. The maximum temperature is 200°C, ensuring water is always in a liquid state and can be described by Darcy's law [Yao 2020, pp. 2-3].
- **Fracture Pressure:** Pressure on the upper and lower surfaces of a fracture is assumed to be similar due to the small fracture thickness [Yao 2020, pp. 3-4].
- **Temperature Dependence:** Fluid density and dynamic viscosity are functions of temperature [Yao 2020, pp. 1-2, 3-4].
- **Simulation Setup:** Investigations on fracture density and percolation use a 100m × 100m × 100m domain with equal-diameter disk fractures uniformly distributed in space. Inlet temperature is 20°C, and total calculation time is 30 years [Yao 2020, pp. 6-7, 7-9].

## Key Variables / Parameters

- **Geometric Parameters:** Fracture density ( `ρ'` ), fracture diameter, fracture thickness (`d_fr`), fracture surface roughness (represented by a correction factor `η` and relative surface roughness `R_a`), percolation probability (`p`), percolation threshold (`ρ'_c = 2.281`) [Yao 2020, pp. 3-4, 5-6, 7-9].
- **Physical Properties:** Fluid density (`ρ_f`), dynamic viscosity (`μ_f`), specific heat capacity (`c_p`), thermal conductivity (`k`), rock matrix density (`ρ_p`), rock matrix permeability (`k_p`), storage coefficient of fracture (`S_f`) [Yao 2020, pp. 3-4].
- **Performance Indicators:** Average outlet flow rate, average outlet temperature [Yao 2020, pp. 2-3, 6-7].
- **Coupling Variables:** Temperature (T), fluid pressure (p) [Yao 2020, pp. 3-4].
- **Numerical Parameters:** Time (total 30 years, step 0.1 years) [Yao 2020, pp. 6-7].

## Reusable Claims

1.  In discrete fracture network models of fractured rock masses, the percolation state of the network acts as a decisive, binary control on the system's bulk fluid transport capacity, with percolating networks exhibiting significantly higher average outlet flow rates than non-percolating networks at identical fracture densities [Yao 2020, pp. 1-2, 7-9].
    - **Conditions:** 3D DFN model with a low-permeability rock matrix and uniform, random distribution of identical disk-shaped fractures.
    - **Limitations:** Claim is based on numerical simulations comparing two specific models; generalizability beyond the tested geometries and boundary conditions requires further verification.

2.  As fracture density increases in a 3D fractured rock mass, the average outlet flow rate increases non-linearly, and the slope of this relationship increases with density, indicating a greater-than-linear gain in flow capacity. However, this gain diminishes over time as the cooling rock matrix reduces fluid temperature, increases its viscosity, and thus decreases the flow rate [Yao 2020, pp. 6-7].
    - **Conditions:** Heat-flow coupled model with temperature-dependent fluid properties; constant boundary pressure gradient.
    - **Limitations:** The specific shape of this relationship is dependent on the fracture network geometry and the matrix's thermal properties.

3.  A specific percolation threshold can be identified where curves plotting percolation probability against a defined fracture density measure for different constant fracture diameters intersect at a single point (defined as `ρ'_c = 2.281` in this study) [Yao 2020, pp. 7-9].
    - **Conditions:** The claim applies when using a density measure derived from the excluded volume concept for uniformly distributed, equal-diameter disk fractures examined via Monte Carlo simulation.
    - **Limitations:** This threshold is specific to the density definition and fracture system geometry used in the study. Its universality for other fracture shapes or size distributions is unconfirmed from the provided fragments.

## Candidate Concepts

- [[discrete fracture network]]
- [[heat-flow coupling]]
- [[percolation theory]]
- [[fracture density]]
- [[fracture roughness]]
- [[enhanced geothermal system]]
- [[thermal breakthrough]]
- [[excluded volume concept]]
- [[fracture reservoir]]
- [[fractured rock mass]]

## Candidate Methods

- [[finite element method]]
- [[COMSOL Multiphysics simulation]]
- [[monte carlo simulation]]
- [[zero-thickness element modeling]]
- [[tetrahedral mesh generation]]
- [[discrete fracture network modeling]]
- [[coefficient form PDE]]

## Connections To Other Work

- **DFN and THM coupling models:** The study builds upon prior work by Chen et al. (2013), who proposed governing equations for heat-flow coupling in 2D DFN and used COMSOL, and Sun et al. (2016), who further developed a THM coupling model for 2D fractured rock masses [Yao 2020, pp. 2-2]. This work explicitly extends these efforts into a 3D framework.
- **Fracture roughness:** The research connects to the findings of Luo et al. (2016), who discovered that fracture surface roughness significantly affects the mechanical, hydraulic, thermal, and transport properties of single fractures, by incorporating a roughness correction factor [Yao 2020, pp. 2-2, 3-4].
- **Temperature-dependent fluid properties:** This model addresses a limitation of the 3D model by Chen et al. (2018), which used a pipe network method but did not consider the effect of temperature on fluid density and dynamic viscosity [Yao 2020, pp. 2-2].
- **Percolation:** The study adopts the [[excluded volume concept]] by Balberg et al. (1984) to systematically define fracture density for percolation analysis [Yao 2020, pp. 5-6].

## Open Questions

- 未从索引片段中确认：What are the specific quantitative effects of fracture roughness on the system-level evaluation indicators (average outlet temperature and flow rate)?
- 未从索引片段中确认：How generalizable is the identified percolation threshold (`ρ'_c = 2.281`) to fracture networks with non-uniform size distributions, non-planar fractures, or an anisotropic orientation distribution?
- 未从索引片段中确认：What is the computational cost of the full 3D mesh generation and finite element solution, and what are its limitations for modeling field-scale fractured reservoirs with tens of thousands of fractures?

## Source Coverage

本页面依据论文的12个索引片段生成，这些片段完整覆盖了摘要、引言、方法论（包括控制方程）、数值验证、部分结果和讨论。关键信息，特别是关于裂缝密度和逾渗效应的定量结论以及控制方程的核心公式，均有具体片段支持。然而，关于裂缝粗糙度对热-流耦合效应的具体研究结果、详细的讨论与结论部分内容，未在索引片段中完全呈现。页面中已据此标注无法确认的部分。
