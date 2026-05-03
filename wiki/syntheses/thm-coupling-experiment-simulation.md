---
type: "synthesis"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
title: "热-水-力（THM）多场耦合实验与数值模拟进展"
sources:
  - "2016-yin-comparison-of-mechanical-properties-in-high-temperature-and-thermal-treatment-granite"
  - "2015-siratovich-saturated-heating-and-quenching-of-three-crustal-rocks-and-implications-for-ther"
  - "2014-kim-effect-of-rapid-thermal-cooling-on-mechanical-rock-properties"
  - "2016-shao-effect-of-temperature-on-permeability-and-mechanical-characteristics-of-lignite"
  - "2015-yu-experimental-investigation-on-mechanical-properties-and-permeability-evolution-of-red-sa"
  - "2014-liu-mechanical-properties-of-qinling-biotite-granite-after-high-temperature-treatment"
  - "2017-sun-numerical-simulation-of-the-heat-extraction-in-egs-with-thermal-hydraulic-mechanical-co"
  - "2018-salimzadeh-a-three-dimensional-coupled-thermo-hydro-mechanical-model-for-deformable-fractur"
  - "2017-luo-experimental-investigation-of-the-hydraulic-and-heat-transfer-properties-of-artificiall"
  - "2019-huang-experimental-investigation-of-seepage-and-heat-transfer-in-rough-fractures-for-enhanc"
  - "2017-chen-experimental-study-on-the-effect-of-fracture-geometric-characteristics-on-the-permeabi"
  - "2021-meng-experimental-study-on-permeability-and-porosity-evolution-of-host-rock-with-varying-da"
  - "2021-meng-experimental-study-on-permeability-evolution-and-nonlinear-seepage-characteristics-of"
  - "2020-yang-an-experimental-study-of-effect-of-high-temperature-on-the-permeability-evolution-and"
---

# 热-水-力（THM）多场耦合实验与数值模拟进展

## Central Question

如何在实验室和数值模型中重现温度-应力-流体压力共同作用下裂隙岩体的非单调渗透率演化及热提取过程？
## Synthesis

综合高温三轴实验、循环淬火实验和从单裂隙到DFN的全耦合THM模拟，结果表明渗透率随温度和应力的演化并非单调“升温增渗”，而是可先降后升，存在300°C和500°C附近的转折点。实验发现，冷却速率和围压显著影响裂纹萌生与闭合；数值模型则强调了裂隙变形、冷缩通道化和热孔弹性对长期热提取效率的控制。目前仍缺乏高效的大规模三维并行求解器。
## Evidence Chain

- Yin (2016) 对比了花岗岩在‘高温后’和‘高温下’加载，发现了弹性模量、峰值应力、破坏模式的系统性差异（HT-UCS-brittle-ductile-transition）。
- Siratovich (2015) 通过对比快速淬火与缓慢冷却，发现淬火大幅提高花岗闪长岩、玄武岩等渗透率近 4 个数量级（thermal-shock-enhances-permeability）。
- Kim (2014) 发现在低中温下进行多次热循环，均质细粒岩石会出现‘裂纹愈合’效应，与非均质粗粒岩石的‘裂纹生长’效应完全相反（crack-healing-vs-growth-by-thermal-shock）。
- Shao (2016) 发现褐煤渗透率在特定温度（~150°C, 350°C）和孔隙压力（0.5-1 MPa, 3.5-5 MPa）区间出现拐点和峰值。
- Yu (2015) 研究了红砂岩在三轴压缩过程中的渗透率演化，将其分为裂纹闭合—弹性—稳定扩展—非稳定扩展—峰后五个阶段。
- 2017-sun基于离散裂隙模型建立THM全耦合有限元，揭示EGS中渗透率-温度-应力的强相互作用
- 2018-salimzadeh提出三维全耦合THM模型并引入增广拉格朗日接触力学，证明冷缩导致裂隙开度先增后因应力重分布而减速
- 2017-luo实验发现粗糙花岗岩裂隙渗流受面积比和围压控制，高温下粘度下降使水力传导系数增大
- 2019-huang通过3D打印和可视化实验给出粗糙度方向对换热的影响
- 2017-chen提出基于裂隙几何特征的FGC渗透率模型
- Meng (2021a) 实时高温三轴渗透试验显示损伤砂岩渗透率先降后升
- Meng (2021b) 揭示了渗流压力与损伤度的耦合影响非单调渗透率
- Yang (2020) 实时高温实验对比高温后处理数据，说明热-力竞争引起的塑性闭合效应
## Disagreements / Tensions

- 关于裂隙内热交换是否可用局部热平衡（LTE）假设，多数EGS模拟采用LTNE，但个别模型为简化仍用LTE
- 渗透率与有效应力的经验关系（指数型、幂律型）在深层地热条件下的适用性缺乏统一认识
- Meng 等强调热塑性变形导致孔裂隙闭合，而另一些研究将弱化归因于矿物相变膨胀。
- 关于热应力的作用性质存在不同观点：Yin (2016) 将其视为一种加剧损伤的‘伪围压’，而传统三轴理论认为围压应该增加强度和延性。
## Boundary Conditions

- 大多数数值研究限于单裂隙或二维模型，三维多分支真实几何模拟计算成本高
- 实验室推导的粗糙裂隙关系升尺度到现场裂隙网络仍有不确定性
- 氮气作为渗流介质，静水/三轴应力达数十 MPa，最高温度 650 °C，适用于完整或含单裂缝的沉积岩
- 实时高温实验与高温后处理实验条件有本质区别
## Writing Uses

- 文献综述中可用于梳理EGS模拟方法的发展脉络
- 方法部分可引用作为THM耦合建模的基础
- 撰写一篇关于地热和深层化石能源开采中储层物性演化的综述，讨论多场耦合的共性与差异
- 为深部能源开发提供定量化的储层增产效果预测的理论基础
## Source Papers

- [2016-yin-comparison-of-mechanical-properties-in-high-temperature-and-thermal-treatment-granite](../papers/2016-yin-comparison-of-mechanical-properties-in-high-temperature-and-thermal-treatment-granite.md)
- [2015-siratovich-saturated-heating-and-quenching-of-three-crustal-rocks-and-implications-for-ther](../papers/2015-siratovich-saturated-heating-and-quenching-of-three-crustal-rocks-and-implications-for-ther.md)
- [2014-kim-effect-of-rapid-thermal-cooling-on-mechanical-rock-properties](../papers/2014-kim-effect-of-rapid-thermal-cooling-on-mechanical-rock-properties.md)
- [2016-shao-effect-of-temperature-on-permeability-and-mechanical-characteristics-of-lignite](../papers/2016-shao-effect-of-temperature-on-permeability-and-mechanical-characteristics-of-lignite.md)
- [2015-yu-experimental-investigation-on-mechanical-properties-and-permeability-evolution-of-red-sa](../papers/2015-yu-experimental-investigation-on-mechanical-properties-and-permeability-evolution-of-red-sa.md)
- [2014-liu-mechanical-properties-of-qinling-biotite-granite-after-high-temperature-treatment](../papers/2014-liu-mechanical-properties-of-qinling-biotite-granite-after-high-temperature-treatment.md)
- [2017-sun-numerical-simulation-of-the-heat-extraction-in-egs-with-thermal-hydraulic-mechanical-co](../papers/2017-sun-numerical-simulation-of-the-heat-extraction-in-egs-with-thermal-hydraulic-mechanical-co.md)
- [2018-salimzadeh-a-three-dimensional-coupled-thermo-hydro-mechanical-model-for-deformable-fractur](../papers/2018-salimzadeh-a-three-dimensional-coupled-thermo-hydro-mechanical-model-for-deformable-fractur.md)
- [2017-luo-experimental-investigation-of-the-hydraulic-and-heat-transfer-properties-of-artificiall](../papers/2017-luo-experimental-investigation-of-the-hydraulic-and-heat-transfer-properties-of-artificiall.md)
- [2019-huang-experimental-investigation-of-seepage-and-heat-transfer-in-rough-fractures-for-enhanc](../papers/2019-huang-experimental-investigation-of-seepage-and-heat-transfer-in-rough-fractures-for-enhanc.md)
- [2017-chen-experimental-study-on-the-effect-of-fracture-geometric-characteristics-on-the-permeabi](../papers/2017-chen-experimental-study-on-the-effect-of-fracture-geometric-characteristics-on-the-permeabi.md)
- [2021-meng-experimental-study-on-permeability-and-porosity-evolution-of-host-rock-with-varying-da](../papers/2021-meng-experimental-study-on-permeability-and-porosity-evolution-of-host-rock-with-varying-da.md)
- [2021-meng-experimental-study-on-permeability-evolution-and-nonlinear-seepage-characteristics-of](../papers/2021-meng-experimental-study-on-permeability-evolution-and-nonlinear-seepage-characteristics-of.md)
- [2020-yang-an-experimental-study-of-effect-of-high-temperature-on-the-permeability-evolution-and](../papers/2020-yang-an-experimental-study-of-effect-of-high-temperature-on-the-permeability-evolution-and.md)
