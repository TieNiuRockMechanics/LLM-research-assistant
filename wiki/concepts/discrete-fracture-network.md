---
type: "concept"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "离散裂隙网络 (DFN)"
aliases:
  - "DFN"
  - "Discrete Fracture Network"
  - "discrete fracture network"
  - "离散裂缝网络"
  - "discrete fracture network"
  - "stochastic fracture network"
  - "3D DFN"
  - "fracture system"
sources:
  - "1995-watanabe-fractal-geometry-characterization-of-geothermal-reservoir-fracture-networks"
  - "2007-baghbanan-hydraulic-properties-of-fractured-rock-masses-with-correlated-fracture-length-and"
  - "2009-xu-a-new-computer-code-for-discrete-fracture-network-modelling"
  - "2009-kim-estimation-of-fracture-porosity-of-naturally-fractured-reservoirs-with-no-matrix-porosi"
  - "2012-de-dreuzy-influence-of-fracture-scale-heterogeneity-on-the-flow-properties-of-three-dimensi"
  - "2013-davy-a-model-of-fracture-nucleation-growth-and-arrest-and-consequences-for-fracture-density"
  - "2013-lang-fractured-reservoir-modeling-method-based-on-discrete-fracture-network-model"
  - "2016-bonneau-impact-of-a-stochastic-sequential-initiation-of-fractures-on-the-spatial-correlatio"
  - "2016-hyman-fracture-size-and-transmissivity-correlations-implications-for-transport-simulations"
  - "2016-maillot-connectivity-permeability-and-channeling-in-randomly-distributed-and-kinematically"
  - "2016-liu-critical-hydraulic-gradient-for-nonlinear-flow-through-rock-fracture-networks-the-roles"
  - "2017-lei-the-use-of-discrete-fracture-networks-for-modelling-coupled-geomechanical-and-hydrologi"
  - "2018-dong-储层裂缝随机建模方法研究进展"
  - "2019-hyman-linking-structural-and-transport-properties-in-three-dimensional-fracture-networks"
  - "2020-hyman-flow-channeling-in-fracture-networks-characterizing-the-effect-of-density-on-preferen"
  - "2021-huang-development-and-application-of-three-dimensional-discrete-fracture-network-modeling-a"
  - "2021-hyman-scale-bridging-in-three-dimensional-fracture-networks-characterizing-the-effects-of-v"
  - "2023-ojeda-discrete-fracture-network-dfn-analysis-to-quantify-the-reliability-of-borehole-derive"
  - "2023-yoon-effects-of-dead-end-fractures-on-non-fickian-transport-in-three-dimensional-discrete-f"
  - "2024-yin-p-clet-number-dependent-longitudinal-dispersion-in-discrete-fracture-networks"
  - "2025-zhang-intelligent-construction-method-for-rock-slope-fracture-network-model-based-on-discre"
  - "2025-zhao-characterizing-the-intrinsic-complexity-of-natural-fracture-networks-a-novel-fractal-b"
  - "2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi"
  - "2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers"
  - "2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai"
---

# 离散裂隙网络 (DFN)

## Definition

将岩体中的裂隙作为离散几何对象（如线段、圆盘、椭圆），通过统计参数（位置、产状、长度、开度等）显式生成网络，用于模拟渗流、溶质运移、热传导和力学行为。
## Aliases

- DFN
- Discrete Fracture Network
- discrete fracture network
- 离散裂缝网络
- discrete fracture network
- stochastic fracture network
- 3D DFN
- fracture system
## Boundary

假设岩块不透水或基质渗流可忽略；需要大量几何统计参数，且网络生成常基于泊松过程或分形模型；真实裂隙的空间相关性和成因机制往往被简化。
## Related Methods

- stochastic-DFN-generation
- fractal-DFN-generation
- dfn-permeability-simulation
- kinematic-fracture-generation
- sequential-parent-daughter-poisson-process
- recursive-cell-culture
- multi-scale-dfn-modelling
- monte-carlo-dfn
- 3dec-simulation
- rjns3d-toolbox
- fractal-topography-dfn
- fracgen
- upscaling-gan
- dfn-flow-simulation
- dfn-inversion
## Related Claims

- DFN-flow-channelization
- REV-existence-depends-on-aperture-variance
- kinematic-dfn-permeability-lower
- Poisson-vs-kinematic-connectivity
- size-T-correlation-important
- Jc-dominance-by-aperture
- dfn-requires-realistic-clustering-and-scaling
- dfn-epm-equivalence-depends-on-spatial-rev
- dead-end-fractures-enhance-solute-tailing
- fracture-density-controls-flow
## Source Papers

- [1995-watanabe-fractal-geometry-characterization-of-geothermal-reservoir-fracture-networks](../papers/1995-watanabe-fractal-geometry-characterization-of-geothermal-reservoir-fracture-networks.md)
- [2007-baghbanan-hydraulic-properties-of-fractured-rock-masses-with-correlated-fracture-length-and](../papers/2007-baghbanan-hydraulic-properties-of-fractured-rock-masses-with-correlated-fracture-length-and.md)
- [2009-xu-a-new-computer-code-for-discrete-fracture-network-modelling](../papers/2009-xu-a-new-computer-code-for-discrete-fracture-network-modelling.md)
- [2009-kim-estimation-of-fracture-porosity-of-naturally-fractured-reservoirs-with-no-matrix-porosi](../papers/2009-kim-estimation-of-fracture-porosity-of-naturally-fractured-reservoirs-with-no-matrix-porosi.md)
- [2012-de-dreuzy-influence-of-fracture-scale-heterogeneity-on-the-flow-properties-of-three-dimensi](../papers/2012-de-dreuzy-influence-of-fracture-scale-heterogeneity-on-the-flow-properties-of-three-dimensi.md)
- [2013-davy-a-model-of-fracture-nucleation-growth-and-arrest-and-consequences-for-fracture-density](../papers/2013-davy-a-model-of-fracture-nucleation-growth-and-arrest-and-consequences-for-fracture-density.md)
- [2013-lang-fractured-reservoir-modeling-method-based-on-discrete-fracture-network-model](../papers/2013-lang-fractured-reservoir-modeling-method-based-on-discrete-fracture-network-model.md)
- [2016-bonneau-impact-of-a-stochastic-sequential-initiation-of-fractures-on-the-spatial-correlatio](../papers/2016-bonneau-impact-of-a-stochastic-sequential-initiation-of-fractures-on-the-spatial-correlatio.md)
- [2016-hyman-fracture-size-and-transmissivity-correlations-implications-for-transport-simulations](../papers/2016-hyman-fracture-size-and-transmissivity-correlations-implications-for-transport-simulations.md)
- [2016-maillot-connectivity-permeability-and-channeling-in-randomly-distributed-and-kinematically](../papers/2016-maillot-connectivity-permeability-and-channeling-in-randomly-distributed-and-kinematically.md)
- [2016-liu-critical-hydraulic-gradient-for-nonlinear-flow-through-rock-fracture-networks-the-roles](../papers/2016-liu-critical-hydraulic-gradient-for-nonlinear-flow-through-rock-fracture-networks-the-roles.md)
- [2017-lei-the-use-of-discrete-fracture-networks-for-modelling-coupled-geomechanical-and-hydrologi](../papers/2017-lei-the-use-of-discrete-fracture-networks-for-modelling-coupled-geomechanical-and-hydrologi.md)
- [2018-dong-储层裂缝随机建模方法研究进展](../papers/2018-dong-储层裂缝随机建模方法研究进展.md)
- [2019-hyman-linking-structural-and-transport-properties-in-three-dimensional-fracture-networks](../papers/2019-hyman-linking-structural-and-transport-properties-in-three-dimensional-fracture-networks.md)
- [2020-hyman-flow-channeling-in-fracture-networks-characterizing-the-effect-of-density-on-preferen](../papers/2020-hyman-flow-channeling-in-fracture-networks-characterizing-the-effect-of-density-on-preferen.md)
- [2021-huang-development-and-application-of-three-dimensional-discrete-fracture-network-modeling-a](../papers/2021-huang-development-and-application-of-three-dimensional-discrete-fracture-network-modeling-a.md)
- [2021-hyman-scale-bridging-in-three-dimensional-fracture-networks-characterizing-the-effects-of-v](../papers/2021-hyman-scale-bridging-in-three-dimensional-fracture-networks-characterizing-the-effects-of-v.md)
- [2023-ojeda-discrete-fracture-network-dfn-analysis-to-quantify-the-reliability-of-borehole-derive](../papers/2023-ojeda-discrete-fracture-network-dfn-analysis-to-quantify-the-reliability-of-borehole-derive.md)
- [2023-yoon-effects-of-dead-end-fractures-on-non-fickian-transport-in-three-dimensional-discrete-f](../papers/2023-yoon-effects-of-dead-end-fractures-on-non-fickian-transport-in-three-dimensional-discrete-f.md)
- [2024-yin-p-clet-number-dependent-longitudinal-dispersion-in-discrete-fracture-networks](../papers/2024-yin-p-clet-number-dependent-longitudinal-dispersion-in-discrete-fracture-networks.md)
- [2025-zhang-intelligent-construction-method-for-rock-slope-fracture-network-model-based-on-discre](../papers/2025-zhang-intelligent-construction-method-for-rock-slope-fracture-network-model-based-on-discre.md)
- [2025-zhao-characterizing-the-intrinsic-complexity-of-natural-fracture-networks-a-novel-fractal-b](../papers/2025-zhao-characterizing-the-intrinsic-complexity-of-natural-fracture-networks-a-novel-fractal-b.md)
- [2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi](../papers/2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi.md)
- [2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers](../papers/2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers.md)
- [2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai](../papers/2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai.md)
