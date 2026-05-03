---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-feng-a-fractal-analysis-of-radon-migration-in-discrete-fracture-network-model"
title: "A Fractal Analysis of Radon Migration in Discrete Fracture Network Model."
status: "draft"
source_pdf: "data/papers/2021 - A fractal analysis of radon migration in discrete fracture network model.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Feng, Shengyang, et al. \"A Fractal Analysis of Radon Migration in Discrete Fracture Network Model.\" *Chemosphere*, vol. 266, 2021, p. 129010. doi:10.1016/j.chemosphere.2020.129010."
indexed_texts: "10"
indexed_chars: "49212"
nonempty_source_blocks: "10"
compiled_source_blocks: "10"
compiled_source_chars: "49425"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004328"
coverage_status: "full-index"
source_signature: "ee730d9db35a99068f305fc177b499b92fe7323f"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T03:51:47"
---

# A Fractal Analysis of Radon Migration in Discrete Fracture Network Model.

## One-line Summary
提出一种结合分形理论与离散裂隙网络（DFN）的新型分形DFN模型，用于模拟裂隙介质中氡气迁移，并通过实验验证了模型准确性。

## Research Question
如何建立一种更真实的模拟裂隙岩石中氡气迁移的模型，以克服传统假设将裂隙介质视为均匀各向同性所导致的预测偏差？具体包括：利用分形理论推导裂隙长度和开度的分布，结合DFN描述裂隙几何，并分析分形维数、裂隙方向、对流速度等关键参数对氡扩散系数和呼出率的影响。[Feng 2021, pp. 1-2]

## Study Area / Data
模型验证使用的样本为铀尾矿、水泥和水制成的固化材料，内部嵌入特定DFN参数的塑料片构造裂隙。模型尺寸为0.5 m × 0.5 m，高、低氡浓度边界分别为142,905 Bq/m³ 和8,572 Bq/m³，材料氡产生率为0.12 Bq/m³/s，压差200 Pa。用RAD7测量不同时刻氡浓度计算呼出率。[Feng 2021, pp. 3-5] 分析计算所用参数列于表1、表2和表4，包括最大裂隙长度、最小/最大长度比、分形维数、裂隙数量等。[Feng 2021, pp. 1-6]

## Methods
- **分形DFN模型**：裂隙长度分布遵循分形幂律（式A11），裂隙位置用Poisson分布，方向用von Mises‑Fisher分布（式1），等效开度与长度线性相关（式3）。用Monte Carlo方法生成随机DFN。[Feng 2021, pp. 2-3]
- **氡迁移方程**：在单一裂隙中建立稳态扩散‑对流方程（式4），导出裂隙末端氡通量表达式（式9），对流速度用立方定律（式10）。在DFN节点处建立质量守恒方程（式11），形成稀疏矩阵（式12）求解节点浓度，进而计算氡呼出率（式13）和有效扩散系数（式14‑15）。[Feng 2021, pp. 3-4]
- **数值实现**：开发相应计算机程序，利用稀疏矩阵算法求逆，全局运行次数300次以上以保证有效扩散系数收敛。[Feng 2021, pp. 3-4]
- **实验验证**：设计包含氡源室、裂隙岩石、压力装置、RAD7探测器和干燥装置的实验系统（图3），测量不同时刻氡浓度并按式（16）计算呼出率，与模型预测值对比（相对误差平均8.5%）。[Feng 2021, pp. 4-5]
- **传统模型对比**：用基于Darcy定律的连续介质模型（式17‑18）对同一样本进行计算，表明传统模型因忽略裂隙主导迁移而严重低估氡呼出率。[Feng 2021, pp. 5-6]

## Key Findings
1. 分形DFN模型收敛所需的全局运行次数约为300。[Feng 2021, pp. 3-4]
2. 保证裂隙连通所需的最小与最大长度比阈值 $(l_{min}/l_{max})_0$ 随裂隙长度分形维数 $D_f$ 增大而减小，两者遵循指数定律：$(l_{min}/l_{max})_0 = 1.61 \times 10^{-4} + 12.23 \exp(-4.2 D_f)$，$R^2 = 0.9705$。[Feng 2021, pp. 5-6]
3. 随着 $D_f$ 增大，模型中长裂隙增多，连通裂隙比例 $f$ 和有效氡扩散系数 $D_{eff}$ 均线性增大。[Feng 2021, pp. 6-7]
4. 在决定裂隙方向的参数（倾角、倾向、其Fisher常数）中，倾角对氡扩散系数影响最大；倾角小于30°时扩散系数随倾角增大而增大，大于30°时则减小。[Feng 2021, pp. 6-7]
5. 氡呼出率随平均对流速度增加呈指数上升；低对流速度的影响可忽略，极高速对流因减少放射性衰变损失而强烈提升呼出率。[Feng 2021, pp. 6-7]
6. 模型存在代表单元体（REV）：$D_{eff}$ 的变异系数随模型尺寸增大而减小，以10%变异系数为基准确定的REV尺寸随 $D_f$ 增大而增加，且遵循指数定律。[Feng 2021, pp. 7-8]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 分形DFN模型可预测裂隙岩石中氡扩散系数和呼出率，验证实验相对误差平均8.5% | [Feng 2021, pp. 4-5, Table 2] | 3块不同 $D_f$ 和裂隙参数的固化样本，模型尺寸0.5 m×0.5 m | 传统连续介质模型预测值远偏低 |
| 全局运行次数300以上时 $D_{eff}$ 收敛 | [Feng 2021, pp. 3-4, Fig. 2] | 模型尺寸1 m³，$l_{max}=0.5$ m，$l_{min}/l_{max}=0.005$，$b=0.001$，$N_t=1000$ | 用于软件开发的运行次数设定 |
| $(l_{min}/l_{max})_0$ 与 $D_f$ 的指数关系 | [Feng 2021, pp. 5-6, Eq. 19] | 3D分形DFN，$f \approx 0.001$ 作为连通判据 | 保证裂隙连通以避免计算无效 |
| $f$ 和 $D_{eff}$ 随 $D_f$ 线性增加 | [Feng 2021, pp. 6-7, Fig. 10] | 与Fig. 9相同的结构参数，$D_f$取1.8–2.8 | 长裂隙增多提高连通性和扩散能力 |
| 倾角是影响 $D_{eff}$ 的最主要方向参数，倾角30°时 $D_{eff}$ 最高 | [Feng 2021, pp. 6-7, Fig. 11] | 3D模型，其余参数同Table 4 | 倾向及其它方向参数影响较小 |
| 氡呼出率 $J_b$ 随平均对流速度 $v$ 指数增长 | [Feng 2021, pp. 6-7, Fig. 12] | $l_{max}=0.5$ m，$l_{min}/l_{max}=7\times10^{-4}$，$D_f=2.4$，边界浓度高值3,445,527 Bq/m³ | 低流速可忽略，高流速因减少衰变而显著增强 |
| REV尺寸随 $D_f$ 指数增大 | [Feng 2021, pp. 7-8, Fig. 13–14] | 2D模型，变异系数<10%，$D_f$=2.2,2.4,2.6,2.8对应的REV为6,11,21,43 m | 分形维数越大，长裂隙越多，REV越大 |

## Limitations
- 模型的有效性依赖于满足 $l_{min} \ll l_{max}$ （式A9），否则需生成大量裂隙以保证连通，大幅增加计算时间；并需设定 $(l_{min}/l_{max})_0$ 阈值。[Feng 2021, pp. 5-6, 10]
- 实验验证仅基于三块铀尾矿固化样本，且裂隙由1 mm塑料片预制，与实际岩石裂隙存在差异；相对误差平均8.5%。[Feng 2021, pp. 4-5]
- REV分析限于2D，且 $D_f$ 最大为2.8，更高 $D_f$ 对应的REV尺寸可达数十米，可能超过实际工程尺度。[Feng 2021, pp. 7-8]
- 模型假设稳态迁移，未考虑瞬态效应。[Feng 2021, pp. 2-3]

## Assumptions / Conditions
- 裂隙长度分布符合分形幂律，且 $l_{min} \ll l_{max}$ （式A3–A9）。[Feng 2021, pp. 9-10]
- 裂隙中心位置服从Poisson分布，方向服从von Mises‑Fisher分布，等效开度与长度成正比（$d = b l$，$b \in [10^{-3},10^{-1}]$）。[Feng 2021, pp. 2-3]
- 氡在单一裂隙中的迁移为稳态扩散-对流，对流速度用立方定律（式10）。[Feng 2021, pp. 2-3]
- DFN内部节点质量守恒，仅连通裂隙参与迁移，孤立和“死端”裂隙忽略。[Feng 2021, pp. 3-4]
- 模型边界为固定氡浓度，内部氡产生率恒定。[Feng 2021, pp. 3-4]
- 在计算REV时以10%的变异系数为判别标准。[Feng 2021, pp. 7-8]

## Key Variables / Parameters
- $l_{max}$, $l_{min}$, $l_{min}/l_{max}$：最大、最小裂隙长度及比值
- $D_f$：裂隙长度分形维数
- $N_t$：裂隙总数
- $b$：开度-长度比例系数
- 裂隙方向：倾角（dip）、倾向（dip direction）及其Fisher常数（$k$）
- $D$：氡扩散系数（空气中 $1.05 \times 10^{-5}~m^2/s$）
- $v$：对流速度
- $a$：氡产生率（Bq/m³/s）
- $C$：氡浓度（Bq/m³）
- $J$：氡通量（Bq/m²/s）
- $J_b$：氡呼出率
- $D_{eff}$：有效氡扩散系数
- $f$：连通裂隙体积比
- REV size：代表单元体尺寸
- 模型尺寸、边界浓度、压差等 [Feng 2021, pp. 2-10, Notation]

## Reusable Claims
- 当裂隙连通比 $f \approx 0.001$ 时，可作为3D分形DFN模型产生连通裂隙的 $l_{min}/l_{max}$ 阈值。[Feng 2021, pp. 5-6]
- 阈值 $(l_{min}/l_{max})_0$ 与 $D_f$ 满足指数关系 $(l_{min}/l_{max})_0 = 1.61\times10^{-4} + 12.23\exp(-4.2D_f)$，$R^2=0.9705$。[Feng 2021, pp. 6, Eq. 19]
- 分形DFN模型计算氡有效扩散系数需至少300次Monte Carlo实现以保证收敛。[Feng 2021, pp. 3-4]
- $D_f$ 增大导致长裂隙增多，连通裂隙比例和 $D_{eff}$ 均线性增加。[Feng 2021, pp. 6-7]
- 裂隙方向参数中，倾角对氡迁移影响最大，倾角约30°时 $D_{eff}$ 达到峰值。[Feng 2021, pp. 6-7]
- 氡呼出率随平均对流速度指数增长，低流速影响可忽略。[Feng 2021, pp. 6-7]
- REV尺寸随 $D_f$ 增加而指数增长。[Feng 2021, pp. 7-8]

## Candidate Concepts
- [[fracture reservoir]]
- [[fractal dimension]]
- [[discrete fracture network (DFN) model]]
- [[von Mises-Fisher distribution]]
- [[representative elementary volume (REV)]]
- [[radon exhalation rate]]
- [[effective radon diffusivity]]
- [[Monte Carlo method]]
- [[sparse matrix algorithm]]
- [[cubic law]]
- [[pipe model for fracture flow]]

## Candidate Methods
- [[fractal DFN model for radon migration]]
- [[stochastic generation of fracture lengths by power-law with fractal dimension]]
- [[Poisson process for fracture locations]]
- [[von Mises-Fisher orientation model]]
- [[mass balance assembly at DFN nodes]]
- [[sparse matrix inversion for large DFN]]
- [[experimental validation using solidified tailings with embedded fractures and RAD7 monitor]]
- [[comparison with conventional homogeneous radon migration model]]

## Connections To Other Work
- 传统氡迁移理论假设裂隙介质均匀各向同性（Rogers and Nielson, 1991; Mosley et al., 1997），而本模型克服了该限制。[Feng 2021, pp. 1-2]
- 裂隙的统计分布和分形特征借鉴了Kulatilake et al. (1995, 1999)、Kim and Schechter (2009)、Miao et al. (2015)等对裂隙网络分形描述的研究。[Feng 2021, pp. 2, 9-10]
- DFN方法在流体（地下水、CO₂、油气）运移中已有广泛应用（Baghbanan and Jing, 2007; Junkin et al., 2017），但尚未用于放射性气体；本工作首次将分形DFN与氡衰变耦合。[Feng 2021, pp. 1-2]
- 分形DFN模型借鉴了Velde et al. (1991)的裂隙分形分析和Wang and Cheng (2020)的二维分形渗透率模型。[Feng 2021, pp. 2, 11]

## Open Questions
- 目前索引片段未明确列出进一步研究问题。模型可扩展至非稳态氡迁移、更复杂的裂隙表面形态以及现场尺度验证，但此类方向未在文中讨论。

## Source Coverage
所有10个非空索引片段均已处理（100%块覆盖）。编译源字符数49,425，覆盖率1.004328（by chars）。索引片段完整收录于[Feng 2021, pp. 1-12]。
