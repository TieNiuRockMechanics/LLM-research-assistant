---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2020-pressacco-numerical-modelling-of-heat-shock-assisted-rock-fracture"
title: "Numerical Modelling of Heat Shock–Assisted Rock Fracture."
status: "draft"
source_pdf: "data/papers/2020 - Numerical modelling of heat shock-assisted rock fracture.pdf"
collections:
  - "论文"
citation: "Pressacco, Martina, and Timo Saksala. “Numerical Modelling of Heat Shock–Assisted Rock Fracture.” *International Journal for Numerical and Analytical Methods in Geomechanics*, vol. 44, 2020, pp. 40–68. Wiley Online Library, doi:10.1002/nag.3004. Accessed 2026."
indexed_texts: "20"
indexed_chars: "96125"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T01:13:50"
---

# Numerical Modelling of Heat Shock–Assisted Rock Fracture.

## One-line Summary

本文通过数值模拟研究热冲击预处理引发的裂纹对岩石单轴抗压强度的影响，提出并比较了两种求解解耦热力问题的交错方案，发现热冲击可显著降低完整花岗岩的强度。[Pressacco 2020, pp. 1-2]

## Research Question

热冲击作为岩石破碎前的预处理方式，其诱发的裂纹如何影响岩石的力学性质，特别是单轴抗压强度？如何在考虑岩石细观非均质性和温度依赖性材料行为的条件下，高效可靠地模拟热-力耦合裂纹扩展过程？[Pressacco 2020, pp. 1-2, 2-4]

## Study Area / Data

研究采用合成的二维异质数值岩石样本进行模拟，未依赖特定现场数据。岩石细观结构由 [[Voronoi tessellation]] 多边形随机簇表示，每个簇被赋予不同矿物（如花岗岩）的力学和热物理性质，以此引入非均质性。材料参数的温度依赖性（弹性模量、比热、导热系数、热膨胀系数）根据文献取值，但具体参数值未在索引片段中确认。[Pressacco 2020, pp. 2-4, 6-7]

## Methods

- **本构模型**：采用基于 [[embedded discontinuity finite element|嵌入式不连续有限元（E-FEM）]] 的岩石断裂模型，源自 Saksala 等[31] 的粘性损伤-嵌入式不连续模型，但去除了应变率相关的 pre‑peak 损伤，仅保留准静态断裂描述。裂纹在单元内以位移跳跃的形式表示，通过 [[Enhanced Assumed Strain (EAS) method|增强假设应变（EAS）方法]] 满足牵引连续性。[Pressacco 2020, pp. 4-5]
- **起裂准则与裂纹扩展**：采用 [[Rankine criterion]]，当单元第一主应力超过抗拉强度时插入不连续面，初始法向与第一主应力方向一致。裂纹可按模式 I 和模式 II 张开，并由牵引-分离定律描述模式混合和软化行为，通过 [[return mapping algorithm|返回映射算法]] 进行应力积分。[Pressacco 2020, pp. 5-6]
- **热-力问题解耦**：由于外部热通量（热冲击）远大于机械耗散产生的热量，将耦合热力问题简化为解耦问题，分两步独立求解温度场和变形/开裂。[Pressacco 2020, pp. 2-4, 6-7]
- **数值实现**：岩石区域用线性三角形有限元离散，热冲击模拟为施加在表面的热通量。提出了两种整体时间积分方案：① **显式-显式动态方案**——热方程用前向欧拉法显式推进，力学部分用显式中心差分法，需对角质量矩阵和稳定时间步长；② **隐式-隐式准静态方案**——热和力学部分均采用隐式欧拉法，力学迭代时使用推导的材料切线刚度矩阵，并采用等温分裂的交错策略。[Pressacco 2020, pp. 7-11]
- **模拟流程**：数值试样首先经受热冲击预处理，计算温度场和热裂纹；随后在固定温度下施加位移控制单轴压缩，直至破坏。[Pressacco 2020, pp. 1-2]

## Key Findings

- 热冲击预处理可以在异质花岗岩数值模型中诱发张拉裂纹，并显著降低其单轴抗压强度，破坏模式为轴向劈裂。[Pressacco 2020, pp. 1-2]
- 显式-显式动态方案与隐式-隐式准静态方案均可求解解耦热力问题，但两种方法的精度和效率对比未在索引片段中详细给出。[Pressacco 2020, pp. 9-11，但具体对比结果未从索引片段中确认]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 热冲击预处理显著降低了花岗岩数值样本的单轴抗压强度 | [Pressacco 2020, pp. 1-2] | 二维 Voronoi 细观结构，解耦热力耦合，嵌入式不连续模型，Rankine 起裂；温度依赖性材料参数；模拟热冲击后再进行单轴压缩 | 仅数值结果，未与物理实验直接对比；未见定量强度降幅数据 |

## Limitations

- 数值模型限于二维，无法反映真实的三维裂纹网络和矿物分布 [Pressacco 2020, pp. 2-4]。
- 解耦假设依赖外部热通量主导条件，当热冲击强度较低或机械变形显著时可能不适用 [Pressacco 2020, pp. 2-4, 6-7]。
- 采用固定裂纹法向假设（裂纹面插入后法向不变），可能无法准确模拟拉伸/剪切混合模式下裂纹的转动 [Pressacco 2020, pp. 5-6]。
- 本构模型未考虑应变率效应和预峰值损伤速率，不适用于高应变率问题 [Pressacco 2020, pp. 4-5]。
- 模拟仅针对单轴压缩工况，未考察三轴、拉伸或循环荷载下的表现 [Pressacco 2020, pp. 1-2]。
- 隐式方案的材料切线刚度推导基于线性屈服函数，对于非线性硬化/软化场景可能需要更复杂的切线模量 [Pressacco 2020, pp. 10-11]。
- 显式方案面临临界时间步长的限制，可能影响计算效率，但片段未提供具体稳定性条件或加速措施（除质量缩放外）[Pressacco 2020, pp. 9-10]。

## Assumptions / Conditions

- **解耦条件**：外部热通量在热冲击过程中占绝对主导，机械耗散生成的热量可忽略，因此热-力问题可分解为连续的热分析和随后的力学分析 [Pressacco 2020, pp. 2-4, 6-7]。
- **裂纹模型**：嵌入式不连续为具有残余强度的粘聚裂纹，裂纹两侧温度连续，但热通量不连续；裂纹法向在插入后保持固定（固定裂纹法向）[Pressacco 2020, pp. 5-6, 7]。
- **起裂假设**：材料抗拉强度控制裂纹萌生，采用 Rankine 准则，适用于以张拉断裂为主的硬岩 [Pressacco 2020, pp. 5-6]。
- **岩石非均质性**：通过 Voronoi 镶嵌赋予不同多边形的材料属性，代表矿物尺度的非均质性，但矿物内部视为均质 [Pressacco 2020, pp. 2-4]。
- **热物性**：弹性模量、比热、导热系数、热膨胀系数均为温度的函数，但具体函数形式未在片段中给出 [Pressacco 2020, pp. 6-7, 9]。
- **力学加载**：压缩试验为准静态位移加载，采用等温分裂后忽略温度变化引起的附加应变率 [Pressacco 2020, pp. 9-10]。
- **连续体假设**：采用基于标准连续介质的有限元，小变形框架，热应变公式为 εθ = α(θ)Δθ I [Pressacco 2020, pp. 6-7]。

## Key Variables / Parameters

- θ —— 温度
- qn —— 表面法向热通量
- E(θ) —— 温度相关弹性模量
- c(θ) —— 温度相关比热容
- k(θ) —— 温度相关导热系数
- α(θ) —— 温度相关热膨胀系数
- εθ —— 热应变张量，εθ = α(θ)Δθ I
- αd —— 位移跳跃向量（模式 II 和 I 分量）
-  _λ —— 模式 I 和 II 的裂纹张开/滑动增量向量
- κ —— 描述软化的内变量（及其率）
- ϕt, ϕs —— 牵引力空间中的屈服函数，分别对应拉伸和剪切模式
- σ —— 应力张量
- tΓd —— 裂纹面上的牵引力向量
- Etan —— 材料切线刚度张量（隐式方案用）
- ld —— 单元内嵌入的间断长度
- Ae —— 含间断的单元面积
- 岩石抗拉强度 —— Rankine 起裂准则的阈值
- 岩石单轴抗压强度 —— 表征预处理效果的关键指标

## Reusable Claims

1. **热冲击可显著降低硬岩的单轴抗压强度**  
   在二维异质 Voronoi 细观结构表示的数值花岗岩试样中，先施加表面热通量模拟热冲击，再进行单轴压缩，结果显示强度明显下降，且破坏模式为轴向劈裂。  
   *条件*：解耦热力分析，嵌入式不连续模型，Rankine 起裂，考虑温度依赖性材料参数，热冲击强度足以诱发裂纹。  
   *限制*：纯数值结果，未与实验数据校准；仅针对完整、均质趋势的花岗岩；未评估不同热冲击参数（持续时间和强度）的敏感性 [Pressacco 2020, pp. 1-2]。

2. **E-FEM 结合 EAS 方法可在标准低阶单元中模拟牵引连续的嵌入式裂纹**  
   通过引入位移跳跃和 Heaviside 函数增强应变，并利用 L2 正交条件强加裂纹面牵引连续性，最终简化为局部牵引连续形式 tΓd = σ·n。  
   *条件*：使用线性三角形单元，忽略间断梯度，固定裂纹法向，小变形假设。  
   *限制*：裂纹法向固定，不适用于裂纹偏转复杂的场景；未考虑接触/摩擦效应；推导基于 EAS 方法的简化 [Pressacco 2020, pp. 4-5]。

3. **解耦热力方案在外部热通量占主导时可用于模拟热冲击致裂**  
   在热冲击阶段忽略机械变形对温度场的影响，可先求解瞬态热传导，再将温度场作为体载荷输入力学分析，分别采用显式‑显式动态或隐式‑隐式准静态交错迭代。  
   *条件*：外部加热为主导，材料耗散可忽略；热物性随温度变化；力学分析为等温分裂。  
   *限制*：不适用于热流与机械功耦合强烈的情况（如高速摩擦）；质量缩放和稳定时间步长需根据网格尺寸调整 [Pressacco 2020, pp. 6-11]。

## Candidate Concepts

- [[thermal shock pretreatment]]
- [[heat shock-assisted rock fracture]]
- [[embedded discontinuity finite element]]
- [[rock fracture mechanics]]
- [[uniaxial compressive strength]]
- [[axial splitting failure mode]]
- [[Voronoi tessellation]]
- [[Rankine criterion]]
- [[cohesive crack model]]
- [[thermomechanical uncoupling]]
- [[staggered solution scheme]]
- [[rock heterogeneity]]

## Candidate Methods

- [[Embedded Discontinuity FEM]]
- [[Enhanced Assumed Strain (EAS) method]]
- [[Voronoi mesostructure generation]]
- [[Explicit-explicit dynamic integration]]
- [[Implicit-implicit quasi-static integration]]
- [[Return mapping algorithm]]
- [[Multi-surface plasticity]]
- [[Staggered thermomechanical split]]
- [[Rankine failure initiation]]

## Connections To Other Work

- 本文模型是在 Saksala 等[31] 的粘性损伤-嵌入式不连续模型基础上的修改，主要去除了应变率相关的 pre‑peak 损伤部分 [Pressacco 2020, pp. 4-5]。
- 前期会议论文（Pressacco & Saksala[17]）已初步报告热冲击可降低硬岩抗压强度，本工作扩展了系统仿真和方案比较 [Pressacco 2020, pp. 2-2]。
- 文中列举了相关数值研究，如 Tang 等[19] 的损伤力学模拟、Yu 等[20] 的细观结构模型、Xiao 等[21] 的尺度效应以及 Zhou & Bi[22] 的通用粒子动力学方法，但未从索引片段中确认本文与这些工作在参数或模型上的直接继承或对比 [Pressacco 2020, pp. 2-2]。
- 主题上与 [[microwave-assisted rock breaking]]、[[thermal spallation drilling]]、[[thermal cracking in brittle solids]] 等概念相关，但本文明确区分了微波加热的不同机理，未做进一步关联 [Pressacco 2020, pp. 2-2]。

## Open Questions

- 热冲击的最优强度、持续时间和循环方式（单次 vs. 多次）如何影响强度降幅和能量效率？[未从索引片段中确认]
- 显式动态方案与隐式准静态方案在计算精度、稳定性和效率上的定量对比结果如何？[未从索引片段中确认]
- 模型能否预测真实花岗岩在实验室热冲击-压缩试验中的裂纹形态和强度变化？[未从索引片段中确认]
- 岩石细观结构的随机性是否会对预处理效果造成显著分散？[片段仅提及测试了不同随机结构，但未给出统计结果] [Pressacco 2020, pp. 2-4]
- 三维效应、围压条件以及不同岩石类型（如大理岩、砂岩）对热冲击辅助断裂的响应如何？[未从索引片段中确认]
- 嵌入式不连续模型能否自动捕捉压缩诱导的翼裂纹和剪切带交互作用？[未从索引片段中确认]

## Source Coverage

本知识页基于论文提供的 20 个索引片段生成，实际可用片段覆盖了文章的前 11 页（摘要至解法部分），具体包括：研究背景与动机、文献简要回顾、岩石本构模型推导（含 E-FEM 基理、EAS 方法、牵引连续条件和 Rankine 准则）、热应变定义、热力问题强形式及解耦论述、以及整体求解方案（显式-显式动态和隐式-隐式准静态）。未覆盖的片段预计包含详细的数值算例、参数敏感性分析、显式与隐式方案的计算性能对比、与实验数据的校准以及结论部分。因此，有关预处理参数定量影响、能量节省潜力、模型验证结果等重要信息在本页中缺失。使用者应查阅原文完整结果以获取完整的证据链。
