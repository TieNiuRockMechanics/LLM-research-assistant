---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2021-wang-semi-analytical-model-for-pumping-tests-in-discretely-fractured-aquifers"
title: "Semi-Analytical Model for Pumping Tests in Discretely Fractured Aquifers."
status: "draft"
source_pdf: "data/papers/2021 - Semi-analytical model for pumping tests in discretely fractured aquifers.pdf"
collections:
  - "雷恩学派分形研究"
citation: "Wang, Lei, et al. \"Semi-Analytical Model for Pumping Tests in Discretely Fractured Aquifers.\" *Journal of Hydrology*, vol. 593, 2021, p. 125737. Accessed 2026."
indexed_texts: "15"
indexed_chars: "72524"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T03:14:41"
---

# Semi-Analytical Model for Pumping Tests in Discretely Fractured Aquifers.

## One-line Summary
本文提出一种用于离散裂隙含水层抽水试验的半解析模型，可在拉普拉斯空间耦合二维含水层流与一维裂隙流，仅需对裂隙分段并利用数值反演快速获得复杂裂隙网络中井筒降深的瞬态响应 [Wang 2021, pp. 1-1]。

## Research Question
如何高效、准确地模拟具有随机分布、有限导水性和任意相交特征的离散裂隙网络中，定流量抽水引起的井筒远近场瞬态降深行为？

## Study Area / Data
未从索引片段中确认具体研究区域或实测数据。论文为理论模型建模与验证，以设定参数下的平行非交叉裂隙网络、任意分布非相交裂隙网络和相交裂隙网络（含孤立裂隙）作为概念算例进行讨论 [Wang 2021, pp. 1-1, 9]。

## Methods
模型建立基于裂隙-含水层耦合思想，具体流程如下：
1. **含水层模型**：假设无限延伸、等厚的承压含水层，满足二维达西非稳态流控制方程，并在方程中引入代表井和裂隙作用的点源/面源源汇项 [Wang 2021, pp. 2-3]。
2. **离散裂隙模型**：将裂隙视为一维达西通道，分为双节点模型（两端均与节点相连）和单节点模型（一端封闭）。每条裂隙按长度划分为若干段，每段上的表面流量视为未知 [Wang 2021, pp. 5-7]。
3. **耦合策略**：在拉普拉斯空间，通过裂隙壁上的降深连续性和流量等效条件，将含水层基本解与离散裂隙段流量联系起来，形成关于裂隙表面流量、节点流量和节点降深的线性方程组 [Wang 2021, pp. 1-1, 8]。
4. **求解与反演**：采用高斯消去法求解拉普拉斯空间矩阵，然后应用 Stehfest 数值拉普拉斯反演算法将结果转换到时域，获得井筒任意时刻降深 [Wang 2021, pp. 1-1, 8-9]。
该方法的主要优势在于，只需对裂隙进行分段，不需要对整个含水层域进行离散，极大地降低了处理复杂裂隙网络时的计算量 [Wang 2021, pp. 1-1]。

## Key Findings
- 模型可以模拟三类具有代表性的复杂裂隙网络配置：平行非交叉裂隙、任意分布非相交裂隙以及相交裂隙网络（包含孤立裂隙） [Wang 2021, pp. 1-1]。
- 通过与文献中“扩展井”结果的对比，验证了所提半解析解的正确性 [Wang 2021, pp. 1-1]。
- 该解以分段积分形式解析‑数值耦合，兼顾了复杂网络几何的灵活性和相比全数值方法更低的计算代价。具体的降深曲线形态、敏感参数分析等定量结论未从索引片段中确认 [Wang 2021, pp. 9]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 承压含水层二维达西非稳态控制方程（含井和裂隙的源汇项） | Wang 2021, pp. 2-3 | 无限延伸、等厚、均质承压含水层，上下边界封闭 | 公式(1.1)‑(1.2) |
| 离散裂隙流假设为一维达西流，推导了双节点模型中降深与流量的关系 | Wang 2021, pp. 6-7 | 裂隙宽度远小于长度，裂隙内沿轴向流动 | 公式(13)‑(17) |
| 在拉普拉斯空间利用通量与降深等效条件构建耦合线性方程组，用高斯消去法求解 | Wang 2021, pp. 1-1, 8-9 | 未知数为裂隙表面分段流量、节点流量和节点降深 | 总未知数数目为 Ntsur+Ntrat+Nnode |
| 最终井筒降深解通过 Stehfest 数值拉普拉斯反演获得 | Wang 2021, pp. 1-1, 9 | 采用无量纲井半径 r_wD=0.001 | 补充材料 S3 描述反演细节 |
| 模型可处理平行非交叉、任意分布非相交以及相交裂隙网络 | Wang 2021, pp. 1-1 | 离散裂隙网络，各裂隙具有独立走向、长度和导水性 | 摘要与实验结果声明 |

## Limitations
- 索引片段中未发现明确说明的局限性章节；据模型假设推断，其主要局限包括裂隙内仅考虑一维达西流，忽略裂隙储水效应或非达西效应。
- 含水层为无限延伸的均匀水层，未能考虑边界效应或非均质分布。
- 暂未涉及野外实际抽水数据的应用验证，片段只提及理论案例 [Wang 2021, pp. 9]。

## Assumptions / Conditions
模型推导基于下列明确假设 [Wang 2021, pp. 2-3]：
- 承压含水层无限延伸、水平、等厚 b，具有均匀的水力传导系数 K_m 和比储水系数 S_sm，且上下边界封闭。
- 抽水过程中忽略含水层内的温度变化。
- 每口井以恒定流量 Q 抽水，可与裂隙相交或不相交。
- 含水层内为二维达西渗流，井半径为 r_w。
- 裂隙宽度远小于其长度，裂隙内假设为一维达西流。
- 离散裂隙系统由 N_f 条裂隙组成，每条裂隙具有全长 L_fn、水力传导系数 K_fn、宽度 w_fn、与 x 轴的夹角 θ_n 以及起始位置 (x_ofn, y_ofn)。
- 模型在拉普拉斯空间推导，并通过 Stehfest 算法数值反演到时域。

## Key Variables / Parameters
- **含水层参数**：水力传导系数 K_m、比储水系数 S_sm、厚度 b
- **裂隙参数**：裂隙总数 N_f，单条裂隙的水力传导系数 K_fn、宽度 w_fn、全长 L_fn、方位角 θ_n、起始点位置 (x_ofn, y_ofn)
- **井参数**：井数 M、各井恒定抽水流量 Q_wε、井半径 r_w（或无量纲 r_wD）
- **流动变量**：降深 s_m (含水层)、s_fn (裂隙)；裂隙壁面流量 q_fn,1, q_fn,2；节点流量 Q_fwi
- **无量纲量**：无量纲降深 s_mD、无量纲时间 t_D、无量纲坐标 (x_D,y_D)、无量纲裂隙长度 L_fDn、无量纲流量 q_fDni, Q_fDwi
- **变换空间变量**：拉普拉斯变量 p

## Reusable Claims
1. **最小离散化策略**：对于有限导水离散裂隙网络中的抽水问题，只需对裂隙自身进行分段离散化，无需对周围含水层生成网格，即可耦合求解整个系统的瞬态降深。这大幅降低了数值预处理和计算成本 [Wang 2021, pp. 1-1]。
   *适用条件：* 裂隙宽度远小于长度（可使用一维流近似），含水层满足无限均质承压条件且结构单一。
   *限制：* 未考虑基质块内部的二维/三维压力扩散细节，裂隙之间的基岩仍通过解析基本解表达。

2. **多模式裂隙网络通用处理**：同一套拉普拉斯空间矩阵框架可统一处理非相交裂隙、平行裂隙以及交叉裂隙网络（包括孤立端点的裂隙），通过节点流量平衡自动决定各段汇/源属性 [Wang 2021, pp. 1-1, 8]。
   *适用条件：* 裂隙系统可由一系列具有确定几何和导水参数的直线段表示，所有连接通过节点实现。
   *证据：* 模型被用于平行非交叉、任意分布非相交及相交裂隙三类算例，摘要与讨论部分均陈述此能力。

3. **通量‑降深等效耦合与数值反演求解流程**：在拉普拉斯空间，将裂隙壁面流量视作未知，通过降深连续性和达西流量等效条件建立线性方程组；该方程组可通过标准高斯消去法求解，拉普拉斯域结果再经由 Stehfest 算法反演到时域 [Wang 2021, pp. 1-1, 8-9]。
   *适用条件：* 含水层和裂隙流均为线性达西流，边界条件为无限远降深零，并满足初始静水条件。
   *限制：* Stehfest 反演对某些类型的时间函数可能不稳定，文中未讨论该情况下误差。

## Candidate Concepts
- [[discrete fracture network (DFN)]]
- [[semi-analytical solution]]
- [[pumping test drawdown]]
- [[confined aquifer]]
- [[Laplace transform in hydrogeology]]
- [[fracture network connectivity]]
- [[Darcy flow]]
- [[wellbore storage and skin effect]] (文中未涉及，但为抽水试验常见概念)

## Candidate Methods
- [[semi-analytical model for discretely fractured aquifers]]
- [[Laplace space matrix construction and Gauss elimination]]
- [[Stehfest numerical Laplace inversion]]
- [[discrete fracture segmentation method]]
- [[flux and drawdown continuity coupling]]
- [[analytical element method for fractures]]

## Connections To Other Work
- 文中将所提模型与一种“扩展井”解进行对比，以验证正确性，但索引片段未给出具体参考文献 [Wang 2021, pp. 1-1]。
- 引言部分提及双孔隙度/双渗透率方法（如 Boulton and Streltsova, 1977; Gerke and van Genuchten, 1993）以及 DFN 数值模拟方法（如 Olorode et al., 2013; Xu et al., 2017），并将本工作定位为对离散裂隙抽水问题的一种解析‑数值替代方案，旨在避免标准 DFN 数值方法中全域网格加密带来的计算负担 [Wang 2021, pp. 1-2, 2]。但索引片段未展示与上述工作的定量比较。
- 从主题上，本模型可与 [[dual-porosity model]]、[[analytical solution for fractured wells]]、[[embedded discrete fracture method]] 等概念和方法建立联系，并可为 [[fracture reservoir characterization]] 中的压力瞬态分析提供工具。

## Open Questions
- 索引片段中未提出明确的开放问题。
- 可推测的后续方向包括：将模型扩展至非承压或越流含水层系统；考虑裂隙储水、非达西流或部分穿透井情形；开展系统的参数敏感性分析（如裂隙密度、方位角、导水性对比的影响）；以及将结果用于真实裂隙场地数据的反演解释。上述方向均未从索引片段中确认。

## Source Coverage
本页依据 15 份索引片段编写，覆盖了论文的标题、摘要、引言（部分）、方法与模型推导的绝大部分（基本假设、含水层模型、离散裂隙模型、耦合求解框架）以及少量结果描述。主要缺失内容包括：
- “Results and discussion” 部分的具体算例几何、参数取值和降深曲线图形；
- 与“扩展井”解以及其他数值方法的定性与定量比较细节；
- 参数敏感性分析或工程建议；
- 结论、局限性声明与后续工作展望。
总体而言，对方法的数学架构和求解逻辑覆盖较为充分，但对模型的表现、验证细节和应用边界的信息存在明显欠缺。
