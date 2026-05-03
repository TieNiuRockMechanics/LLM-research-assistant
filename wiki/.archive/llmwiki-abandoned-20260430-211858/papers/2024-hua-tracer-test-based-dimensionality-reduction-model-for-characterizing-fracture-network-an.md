---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2024-hua-tracer-test-based-dimensionality-reduction-model-for-characterizing-fracture-network-an"
title: "Tracer-Test-Based Dimensionality Reduction Model for Characterizing Fracture Network and Predicting Flow and Transport in Fracture Aquifer."
status: "draft"
source_pdf: "data/papers/2024 - Tracer-test-based dimensionality reduction model for characterizing fracture network and predicting flow and transport in fracture aquifer.pdf"
collections:
citation: "Hua, Cong, et al. \"Tracer-Test-Based Dimensionality Reduction Model for Characterizing Fracture Network and Predicting Flow and Transport in Fracture Aquifer.\" *Journal of Hydrology*, vol. 630, 2024, 130773. Accessed 2026."
indexed_texts: "15"
indexed_chars: "73524"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T14:38:57"
---

# Tracer-Test-Based Dimensionality Reduction Model for Characterizing Fracture Network and Predicting Flow and Transport in Fracture Aquifer.

## One-line Summary
基于示踪突破曲线（TBC）拐点数量构建平行裂缝降维模型（DRM），以实现裂缝网络表征和注采条件下流动与溶质运移预测。

## Research Question
如何从交叉孔示踪试验的突破曲线形状中直接提取主要流动路径信息，并构建足够简单、可反演的降维模型来表征裂缝网络，同时保持对独立抽注条件下示踪浓度和温度的预测能力？

## Study Area / Data
- **实验室尺度**：透明 3D 打印裂缝网络物理模型，包含 7 条交叉裂缝，裂缝长度遵循幂律分布（3.0–21.0 cm），宽度固定为 15.7 cm，倾角满足 Fisher 分布，走向统一，形成共轭裂缝网络模式 [Hua 2024, pp. 3-4]。
- **现场尺度合成模型**：横向 1000 m、垂向 200 m 的裂缝网络模型，用于验证 DRM 在野外条件下的可靠性 [Hua 2024, pp. 5-6]。
- **观测数据**：实验室脉冲示踪试验获取的出口电导率（转示踪浓度）时间序列（TBC）和表面温度热图像；数值模拟生成的出口浓度和温度时间序列 [Hua 2024, pp. 3-4]。

## Methods
- **实验室物理模拟**：采用透明 3D 打印裂缝网络模型，以 630 mL/min 恒速注入冷水，随后脉冲注入 60 ℃ 含蓝色染料与 NaCl 的热水 20 s，再切换回冷水；同时用 CCD 相机、热像仪和电导率记录仪监测出口 [Hua 2024, pp. 3-4]。
- **数值模拟**：建立与实验室相同几何的三维数值模型，顺序求解流动、示踪运移和热传输控制方程（Eqs. 1‑6），考虑温度对流体密度和粘度的影响，忽略温度对弥散系数及热物性的影响（基于温度 <100 ℃ 假设），并通过调整基质空气‑树脂混合权重系数（θ=0.86）使模拟 TBC 与实验观测吻合 [Hua 2024, pp. 4-5]。
- **DRM 构建原则**：利用校准数值模型揭示 TBC 形状与裂缝网络内优先流路径的关系，确定优先流路径数量等于 TBC 中拐点数量（含浓度峰值和下降段明显放缓点）；据此构造由等数量平行裂缝组成的 DRM [Hua 2024, pp. 1-1, 7-8]。
- **未知参数反演**：DRM 中的关键参数（如裂缝间距或基质渗透率）通过贝叶斯随机反演或截断奇异值分解等确定性反演算法推断，正演模型遵循 Eqs. 1‑6 [Hua 2024, pp. 5-6]。
- **验证**：在实验室和野外合成模型上，使用构建 DRM 时所用抽注速率之外的独立速率，计算降维模型预测结果与离散裂缝网络（DFN）模型值的相对误差 RI 进行评估 [Hua 2024, pp. 5-6]。

## Key Findings
- 在同时注‑抽条件下，复杂裂缝网络中的流动与运移主要通过少量（本实验中为 3 条）优先流路径发生，且这些优先路径在不同抽注速率下保持稳定；其数量与 TBC 中的拐点数目一致，拐点包括浓度峰和下降段的明显放缓点 [Hua 2024, pp. 1-1, 6-7, 7-8]。
- 裂缝交汇处的流量分配与裂缝的交汇角无显著相关性；优先流路径的结构由井位、宏观裂缝几何形状以及非均匀温度分布引起的水力梯度和密度驱动流量共同决定 [Hua 2024, pp. 7-8]。
- 基于 TBC 构建的平行裂缝 DRM 能够在与建模不同抽注速率下仍较准确地预测试验出口的示踪浓度和温度，验证了降维策略的有效性 [Hua 2024, pp. 5-6]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 实验室 3D 打印裂缝网络中识别出 3 条优先流路径，对应 TBC 中的 3 个拐点 | [Hua 2024, pp. 6-7] | 7 条裂缝、单一走向、共轭模式；注入速率 630 mL/min，脉冲 60 ℃ 热水 | 优先流路径数量与 TBC 拐点数一致的直接物理证据 |
| 优先流路径的相对流量大小在不同抽注速率下保持不变，即优先路径结构稳定 | [Hua 2024, pp. 7-8] | 同一裂缝几何、井位及水温对比（最大温差约 40 ℃） | 为 DRM 在不同工况下的预测能力提供基础 |
| 流量比在裂缝交汇处与交汇角无关（如 90° 和 45° 交汇处未表现出比例固定关系） | [Hua 2024, pp. 7-8] | 仅基于给定几何和温度条件的数值分析 | 否定“交汇角控制分流”的简单假设 |
| 数值模型通过调整基质空气‑树脂混合系数（θ=0.86）能够匹配实测 TBC | [Hua 2024, pp. 4-5] | 实验室尺度、裂隙开度 1.0 mm、空气/树脂热导率固定 | 表明基质有效参数可被标定，支撑 DRM 反演可行性 |
| 用 630 mL/min 条件下的 TBC 构建的 DRM 能预测 200–1200 mL/min 范围内的出口浓度和温度，相对误差在可接受范围 | [Hua 2024, pp. 5-6] | 同一实验室裂缝几何，现场合成模型另行验证 | 证实 DRM 外推预测能力 |

## Limitations
- 索引片段未提供完整的参数反演精度以及野外合成模型下 DRM 的具体相对误差值；此外，现场尺度验证仅限于单个合成网络模型，实际非均质场的适用性未从片段中确认 [Hua 2024, pp. 5-6]。
- 实验室表面温度测量仅为流体内部温度的定性参考，存在因 3.0 mm 树脂层热传导引起的偏差 [Hua 2024, pp. 3-4]。
- 数值模型假设温度低于 100 ℃，忽略温度对示踪弥散系数及水、岩热物性的影响，且假定对流占优而忽略扩散作用；这些简化在高温或低流速条件下可能不成立 [Hua 2024, pp. 4-5]。
- 实验中裂缝网络为 7 条裂缝的简单共轭系统，长度服从幂律分布、宽度均匀，与自然裂缝网络的复杂几何可能有差异；走向统一主要是为了方便观察，可能削弱了方法的普适性限制条件 [Hua 2024, pp. 3-4]。

## Assumptions / Conditions
- 模型适用于同时注‑抽（双井对）操作的裂缝含水层，流动由对流主导 [Hua 2024, pp. 4-5, 7-8]。
- 裂缝网络内优先流路径稳定，其数量可由 TBC 拐点唯一确定；且这些路径可近似为平行裂缝 [Hua 2024, pp. 1-1]。
- 构建 DRM 时不要求已知原始裂缝网络的细节，仅需一条高质量的交叉孔 TBC [Hua 2024, pp. 1-1, 5-6]。
- 流体性质变化仅考虑温度引起的密度和粘度变化，示踪剂视为惰性、不影响流体物性 [Hua 2024, pp. 4-5]。
- 地下温度低于 100 ℃，不考虑沸腾或相变；适用于浅层地壳条件 [Hua 2024, pp. 4-5]。

## Key Variables / Parameters
- **形态参数**：TBC 拐点数量（含峰值数目和下降段放缓点数目），对应平行裂缝 DRM 中的裂缝条数。
- **流动变量**：各优先流路径的流量、流量比（交汇处上支与下支流量之比）、水力梯度、抽注速率（200–1200 mL/min 实验室；现场尺度 2–3 m³/min）。
- **物理参数**：裂缝水力开度（1.0 mm）、空气和树脂热导率、基质混合权重系数 θ、流体密度和粘度‑温度关系。
- **验证指标**：相对误差 RI（公式 7），比较降维模型（DRM）与原始离散裂缝网络（DFN）模型出口浓度/温度的时间序列偏差。

## Reusable Claims
1. **优先流路径数量等于 TBC 拐点数**：在注‑抽双井条件下，复杂裂缝介质中的溶质运移主要通过少数稳定优先路径发生，这些路径的数目恰好对应于 TBC 上的所有浓度峰值和浓度下降阶段的明显放缓点 [Hua 2024, pp. 1-1, 6-7]。  
   *适用条件*：脉冲或连续示踪注入、同时注‑抽的强迫对流情景；TBC 需有可识别的拐点。  
   *证据基础*：基于 3D 打印物理模型和数值模拟，裂缝几何为7条共轭裂缝，脉冲热水注入 20 s。  
   *限制*：尚未在更复杂、多级次的自然裂缝系统中验证；TBC 拐点的自动识别方法未在此讨论。

2. **优先路径稳定性与流量分配的非角度依赖性**：给定井位和宏观裂缝几何，优先流路径的相对流量分布不受抽注速率变化影响；裂缝交汇处的流量比与裂缝交汇角度无明显相关，而主要受井间水力梯度和温度诱导的密度流控制 [Hua 2024, pp. 7-8]。  
   *适用条件*：最大温度对比约 40 ℃，单一走向的共轭裂缝网络，强制注‑抽。  
   *证据基础*：数值模拟对比了不同交汇角（90°、45°）下流量比的演变，并观察到抽速增加时流量差异扩大但路径排名不变。  
   *限制*：未验证在非均匀地热梯度、多相流或裂缝闭合‑张开的动态条件是否成立。

3. **平行裂缝 DRM 的跨工况预测能力**：利用某一注‑抽速率下获得的 TBC 构建的平行裂缝 DRM，在反演得到关键参数后，能够较准确地预测不同注‑抽速率下的出口示踪浓度和温度 [Hua 2024, pp. 5-6]。  
   *适用条件*：同一井位和裂缝网络，不同速率须在相似流态范围内，且反演算法需充分约束。  
   *证据基础*：实验室尺度测试（630 mL/min 用于建模，200–1200 mL/min 用于验证）和现场合成模型验证（2 m³/min 建模，3 m³/min 验证），使用相对误差 RI 指标。  
   *限制*：实际现场应用中，TBC 质量、多解性和非唯一性可能影响预测可靠性，这些方面未在片段中详细定量示出。

## Candidate Concepts
- [[dimensionality reduction model]]
- [[tracer breakthrough curve]]
- [[preferential flow path]]
- [[fracture network characterization]]
- [[cross-hole tracer test]]
- [[3D-printed fracture model]]
- [[hydraulic tomography]]
- [[transport in fractured aquifer]]
- [[inversion of fracture properties]]

## Candidate Methods
- [[parallel fracture model]]
- [[Bayesian inversion]]
- [[truncated singular value decomposition]]
- [[numerical simulation of flow and heat transport in fractures]]
- [[tracer injection experiment design]]
- [[electrical conductivity-based concentration monitoring]]

## Connections To Other Work
- 本文中 DRM 的构建利用了 [[hydraulic tomography]] 的思路，但通过 TBC 形态直接确定降维结构，区别于传统的基于网格的反演 [Hua 2024, pp. 1-2]。
- 裂缝网络生成参考了基于统计分布的 [[stochastic fracture network generation]] 方法（如幂律长度分布、Fisher 分布朝向） [Hua 2024, pp. 1-2]。
- 反演方法可选用 [[Bayesian inversion]] (Vrugt, 2016) 或 [[truncated singular value decomposition]] (Doherty, 2004) 算法 [Hua 2024, pp. 5-6]；数值模型中忽略了温度对弥散及热物性的影响，引用了 Chi et al. (2020)、Mehrer (2007)、Yan et al. (2023) 作为依据 [Hua 2024, pp. 4-5]。

## Open Questions
- 当场地的裂缝网络包含大量死端或孤立裂缝时，TBC 拐点是否仍能准确指示主导优先路径的数量？（索引片段未涵盖相关讨论）
- 如何从受观测噪声影响的野外 TBC 中可靠识别拐点（尤其浓度下降段的“明显放缓点”）？（未从索引片段确认自动化或定量方法）
- 平行裂缝假设在强非均质性或三维交叉通道显著时，是否会引起无法接受的预测偏差？（未从索引片段确认误差分解）
- 温度异常（脉冲热水）对优先路径结构的干扰在长期持续温差下是否仍然可忽略？（片段中仅评估了 20 s 脉冲，长期效应未确认）

## Source Coverage
本页内容基于论文索引中的 15 个片段，覆盖了摘要、引言、实验室方法、数值模拟设置、部分结果分析以及 DRM 构建与验证的概述。  
- **已知覆盖**：研究动机、物理模型几何、示踪试验操作步骤、数值模型的主要假设与验证、优先流路径的识别与稳定性、TBC 形态与路径数量的关系、DRM 测试策略。  
- **可能缺失的信息**：详细的参数反演结果、现场合成模型的预测误差定量值、DRM 控制方程的显式形式、与其他降维或全阶次模型的定量对比、讨论部分的全部限制与适用性分析、结论的完整总结。因此，本页中涉及反演精度、极端条件下的表现等部分标为“未从索引片段中确认”。
