---
type: "synthesis"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
title: "裂缝网络几何对渗流、传热与溶质运移的控制"
sources:
  - "2020-chen-equivalent-permeability-distribution-for-fractured-porous-rocks-correlating-fracture-a"
  - "2020-chen-equivalent-permeability-distribution-for-fractured-porous-rocks-the-influence-of-fract"
  - "2020-yao-effects-of-fracture-density-roughness-and-percolation-of-fracture-network-on-heat-flow"
  - "2021-hyman-scale-bridging-in-three-dimensional-fracture-networks-characterizing-the-effects-of-v"
  - "2021-xu-裂隙网络对岩体试件单轴压缩力学特性影响研究"
  - "2022-unknown-can-we-infer-the-percolation-status-of-3d-fractured-media-from-2d-outcrops"
  - "2022-zhu-enhancing-fracture-network-characterization-a-data-driven-outcrop-based-analysis"
  - "2022-viswanathan-from-fluid-flow-to-coupled-processes-in-fractured-rock-recent-advances-and-new"
  - "2023-gao-heat-extraction-performance-of-fractured-geothermal-reservoirs-considering-aperture-var"
  - "2023-yoon-effects-of-dead-end-fractures-on-non-fickian-transport-in-three-dimensional-discrete-f"
  - "2024-yin-p-clet-number-dependent-longitudinal-dispersion-in-discrete-fracture-networks"
  - "2024-shaoqun-dong-relationship-between-box-counting-fractal-dimension-and-properties-of-fracture"
---

# 裂缝网络几何对渗流、传热与溶质运移的控制

## Central Question

裂隙密度、长度分布、开度变化和拓扑连通性如何决定流体流动的通道化、热突破和溶质反常传输？
## Synthesis

DFN模拟和逾渗分析表明，等效渗透率与裂缝密度服从幂律或指数关系，逾渗阈值是流动突破的关键。裂缝长度-开度关联和孔径变异性显著重组网络流场、加剧通道化并改变活性表面积，导致热提取效率快速衰减。在逾渗阈值附近，死端裂隙占比最大，产生强烈的非菲克拖尾，弥散系数与Péclet数呈普适幂律标度。这些发现强调仅用平均参数不能可靠估计传导能力，必须计入几何非均质性和拓扑连通性。
## Evidence Chain

- DFN 渗透率统计分布 (Chen 2020a,b)
- 逾渗对热-流耦合的决定性影响 (Yao 2020)
- 真实孔径分布导致尺度桥接 (Hyman 2021)
- 合成岩体模型 (SRM) 力学响应 (Xu 2021)
- 2022-unknown-can-we-infer 提出了2D露头与3D网络渗透状态的定量关系。
- 2022-zhu-enhancing-fracture 用拓扑三元图、连通性指数(CB)和应力依赖的渗透模型展示了连通到导流的鸿沟。
- 2022-viswanathan-from-fluid-flow 发现仅临界应力裂缝开启时渗透率增加仅8%，而全开放时增加262%。
- 2023-gao-heat-extraction 发现孔径非均质性导致有效流动面积占比极低（<40%）。
- Yoon (2023) 发现死端裂隙占比在逾渗阈值处最大，产生最强拖尾。
- Yin (2024) 提出考虑大裂隙的特征 Péclet 数，使所有 DFN 的弥散系数坍缩为单条标度曲线。
- Dong (2024) 建立了分形维数与裂缝数量、长度和方向的定量关系。
## Disagreements / Tensions

- 对于 DFN 中长度-开度关联模型的选取（恒断裂韧度 vs 恒驱动应力），导致等效渗透率差异可达数量级。
- 高密度网络中，逾渗阈值附近二维和三维连通性差异显著，简化模型可能低估实际渗透率。
- 不同裂缝尺寸分布（幂律 vs 指数）对逾渗阈值和弥散的影响尚未完全统一。
- 对于网络连通性到渗透率的转化，不同模拟方法（如连续介质、离散网络、图论模型）给出的定量预测差异显著。
## Boundary Conditions

- 硬岩（花岗岩、片麻岩、石灰岩）低基质渗透率，裂隙以离散面或线表征，层流达西流。
- 主要基于2D/3D随机DFN；不考虑基质扩散；裂缝面内均匀开度。
- 适用于所有裂缝性储层，但在低应力差、所有裂缝均开放的理想条件下，几何连通性与水力传导的关系更强。
## Writing Uses

- 为现场水力试验（抽水/注水）解译提供概念模型。
- 指导地热储层靶向井位部署以提高扫掠效率。
- 用于核废料处置、地热储层评估等场景，从裂缝密度和方向直接估算弥散风险。
- 设计示踪试验时，根据估计的逾渗状态预测试验时长和解释方法。
## Source Papers

- [2020-chen-equivalent-permeability-distribution-for-fractured-porous-rocks-correlating-fracture-a](../papers/2020-chen-equivalent-permeability-distribution-for-fractured-porous-rocks-correlating-fracture-a.md)
- [2020-chen-equivalent-permeability-distribution-for-fractured-porous-rocks-the-influence-of-fract](../papers/2020-chen-equivalent-permeability-distribution-for-fractured-porous-rocks-the-influence-of-fract.md)
- [2020-yao-effects-of-fracture-density-roughness-and-percolation-of-fracture-network-on-heat-flow](../papers/2020-yao-effects-of-fracture-density-roughness-and-percolation-of-fracture-network-on-heat-flow.md)
- [2021-hyman-scale-bridging-in-three-dimensional-fracture-networks-characterizing-the-effects-of-v](../papers/2021-hyman-scale-bridging-in-three-dimensional-fracture-networks-characterizing-the-effects-of-v.md)
- [2021-xu-裂隙网络对岩体试件单轴压缩力学特性影响研究](../papers/2021-xu-裂隙网络对岩体试件单轴压缩力学特性影响研究.md)
- [2022-unknown-can-we-infer-the-percolation-status-of-3d-fractured-media-from-2d-outcrops](../papers/2022-unknown-can-we-infer-the-percolation-status-of-3d-fractured-media-from-2d-outcrops.md)
- [2022-zhu-enhancing-fracture-network-characterization-a-data-driven-outcrop-based-analysis](../papers/2022-zhu-enhancing-fracture-network-characterization-a-data-driven-outcrop-based-analysis.md)
- [2022-viswanathan-from-fluid-flow-to-coupled-processes-in-fractured-rock-recent-advances-and-new](../papers/2022-viswanathan-from-fluid-flow-to-coupled-processes-in-fractured-rock-recent-advances-and-new.md)
- [2023-gao-heat-extraction-performance-of-fractured-geothermal-reservoirs-considering-aperture-var](../papers/2023-gao-heat-extraction-performance-of-fractured-geothermal-reservoirs-considering-aperture-var.md)
- [2023-yoon-effects-of-dead-end-fractures-on-non-fickian-transport-in-three-dimensional-discrete-f](../papers/2023-yoon-effects-of-dead-end-fractures-on-non-fickian-transport-in-three-dimensional-discrete-f.md)
- [2024-yin-p-clet-number-dependent-longitudinal-dispersion-in-discrete-fracture-networks](../papers/2024-yin-p-clet-number-dependent-longitudinal-dispersion-in-discrete-fracture-networks.md)
- [2024-shaoqun-dong-relationship-between-box-counting-fractal-dimension-and-properties-of-fracture](../papers/2024-shaoqun-dong-relationship-between-box-counting-fractal-dimension-and-properties-of-fracture.md)
