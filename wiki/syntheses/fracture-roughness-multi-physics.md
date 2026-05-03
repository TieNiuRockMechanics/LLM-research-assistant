---
type: "synthesis"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
title: "裂隙表面粗糙度多尺度表征及其对渗流、传热和剪切强度的影响"
sources:
  - "2010-tatone-a-new-2d-discontinuity-roughness-parameter-and-its-correlation-with-jrc"
  - "2014-jang-determination-of-joint-roughness-coefficients-using-roughness-parameters"
  - "2015-li-relationship-between-joint-roughness-coefficient-and-fractal-dimension-of-rock-fracture"
  - "2016-he-effects-of-surface-roughness-on-the-heat-transfer-characteristics-of-water-flow-through"
  - "2016-luo-the-role-of-fracture-surface-roughness-in-macroscopic-fluid-flow-and-heat-transfer-in-f"
  - "2012-de-dreuzy-influence-of-fracture-scale-heterogeneity-on-the-flow-properties-of-three-dimensi"
  - "2016-hyman-fracture-size-and-transmissivity-correlations-implications-for-transport-simulations"
  - "2016-maillot-connectivity-permeability-and-channeling-in-randomly-distributed-and-kinematically"
  - "2017-briggs-numerical-modeling-of-the-effects-of-roughness-on-flow-and-eddy-formation-in-fractur"
  - "2025-song-a-back-propagation-neural-network-optimized-by-genetic-algorithm-for-rock-joint-roughn"
  - "2025-tian-assessment-method-of-surface-morphology-based-on-100-shear-tests-and-pso-rbf-neural-ne"
---

# 裂隙表面粗糙度多尺度表征及其对渗流、传热和剪切强度的影响

## Central Question

如何从微观分形到宏观JRC统一描述裂隙粗糙度，并量化它对单裂隙和网络中流动非线性、换热系数和剪切强度的影响？
## Synthesis

综合统计参数、分形方法和机器学习在JRC预测中的应用，以及粗糙度对单裂隙和网络THM过程的影响。在微观层面，粗糙度通过沟槽化控制涡流生成和非线性流；在宏观上，粗糙度关联着JRC和剪切强度，ML方法可提高预测精度至误差<7%。粗糙度对OHTC的影响集中在凹槽和凸起，流速在凹槽处最大、换热增加。
## Evidence Chain

- Jang (2014) 和 Li (2015) 确定了统计参数和分形维数与JRC之间的定量关系，并指出了第4条标准剖面的系统偏差（JRC-4th-profile-deviation）。
- Briggs (2017) 利用 LBM 发现了粗糙度控制着裂隙流的涡流生成和强非线性（三区模型），为 Forchheimer 流提供了微观机理解释。
- He (2016) 和 Luo (2016) 确立了单裂隙表面粗糙度对局部换热系数和宏观热突破的影响，指出 Barton 等机械-水力隙宽模型主导了这一过程的宏观表现。
- de Dreuzy (2012) 和 Maillot (2016) 揭示了裂隙内部的非均质性（孔径）和网络拓扑（T/X 交叉）耦合，导致泊松 DFN 与运动学 DFN 的等效渗透率出现系统性差异，且后者通道化更强。
- Hyman (2016) 指出裂隙尺寸与导水性的正相关是控制 DFN 渗透率和溶质突破的一级参数。
- Tian (2025) 通过 100 组试验构建新标准剖面，并用 PSO‑RBF 网络预测 JRC，测试 MAPE 4.79%。
- Song (2025) 使用 GA‑BP 模型融合五维形态参数，JRC 回归 R>0.99，抗剪强度误差 7.25%。
- 传统对比：Z₂ 方法平均误差 ~28%，D_Lee 分形法 ~17%。
## Disagreements / Tensions

- 关于分形维数的计算，Jang (2014) 强调在整个分规范围内回归相关性最高，而此前 Kulatilake 等人 (1997) 推荐使用忽略两端平坦段的“合适范围”，两者在方法论上存在根本分歧（D-to-JRC-relation-method-dependent）。
- 关于粗糙度对宏观流热的影响，Luo (2016) 指出其重要性强烈依赖所选的机械-水力隙宽经验模型。
- 神经网络模型过度依赖训练数据的覆盖范围和 JRC 标签的准确性，部分数据集的 JRC 通过反算获得，存在不确定性。
## Boundary Conditions

- 所有这些结论都基于低速层流假设，不适用于高速湍流或含有大量活动填充物的开裂情况。
- 实验室尺度的轮廓线（~100 mm）能否直接代表米级至公里级储层裂隙的力学水利行为？这种尺度的升尺度缺乏物理基础。
- 多数粗糙度表征忽略了法向应力下的接触点分布及其对渗流通道曲折度和各向异性的影响。
## Writing Uses

- 可用于撰写一篇关于裂隙表面粗糙度多尺度定量化及其对EGS渗流和热传导行为的跨尺度影响的前沿综述。
- 在特定实验方法章节（如单裂隙渗流传热试验）或在 EGS 产热量数值模拟的敏感性分析中，论证为何必须考虑粗糙度。
- 提出基于多源形态参数的 JRC 智能评估框架，替代传统标准曲线对比法。
- 在边坡稳定性分析中，引入更准确的节理强度参数。
## Source Papers

- [2010-tatone-a-new-2d-discontinuity-roughness-parameter-and-its-correlation-with-jrc](../papers/2010-tatone-a-new-2d-discontinuity-roughness-parameter-and-its-correlation-with-jrc.md)
- [2014-jang-determination-of-joint-roughness-coefficients-using-roughness-parameters](../papers/2014-jang-determination-of-joint-roughness-coefficients-using-roughness-parameters.md)
- [2015-li-relationship-between-joint-roughness-coefficient-and-fractal-dimension-of-rock-fracture](../papers/2015-li-relationship-between-joint-roughness-coefficient-and-fractal-dimension-of-rock-fracture.md)
- [2016-he-effects-of-surface-roughness-on-the-heat-transfer-characteristics-of-water-flow-through](../papers/2016-he-effects-of-surface-roughness-on-the-heat-transfer-characteristics-of-water-flow-through.md)
- [2016-luo-the-role-of-fracture-surface-roughness-in-macroscopic-fluid-flow-and-heat-transfer-in-f](../papers/2016-luo-the-role-of-fracture-surface-roughness-in-macroscopic-fluid-flow-and-heat-transfer-in-f.md)
- [2012-de-dreuzy-influence-of-fracture-scale-heterogeneity-on-the-flow-properties-of-three-dimensi](../papers/2012-de-dreuzy-influence-of-fracture-scale-heterogeneity-on-the-flow-properties-of-three-dimensi.md)
- [2016-hyman-fracture-size-and-transmissivity-correlations-implications-for-transport-simulations](../papers/2016-hyman-fracture-size-and-transmissivity-correlations-implications-for-transport-simulations.md)
- [2016-maillot-connectivity-permeability-and-channeling-in-randomly-distributed-and-kinematically](../papers/2016-maillot-connectivity-permeability-and-channeling-in-randomly-distributed-and-kinematically.md)
- [2017-briggs-numerical-modeling-of-the-effects-of-roughness-on-flow-and-eddy-formation-in-fractur](../papers/2017-briggs-numerical-modeling-of-the-effects-of-roughness-on-flow-and-eddy-formation-in-fractur.md)
- [2025-song-a-back-propagation-neural-network-optimized-by-genetic-algorithm-for-rock-joint-roughn](../papers/2025-song-a-back-propagation-neural-network-optimized-by-genetic-algorithm-for-rock-joint-roughn.md)
- [2025-tian-assessment-method-of-surface-morphology-based-on-100-shear-tests-and-pso-rbf-neural-ne](../papers/2025-tian-assessment-method-of-surface-morphology-based-on-100-shear-tests-and-pso-rbf-neural-ne.md)
