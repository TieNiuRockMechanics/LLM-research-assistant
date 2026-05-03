---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2021-snowdon-analysis-of-crystalline-rock-permeability-versus-depth-in-a-canadian-precambrian-ro"
title: "Analysis of Crystalline Rock Permeability Versus Depth in a Canadian Precambrian Rock Setting."
status: "draft"
source_pdf: "data/papers/2021 - Analysis of Crystalline Rock Permeability Versus Depth in a Canadian Precambrian Rock Setting.pdf"
collections:
  - "2文章钻孔裂缝分形关系"
citation: "Snowdon, Andrew P., et al. \"Analysis of Crystalline Rock Permeability Versus Depth in a Canadian Precambrian Rock Setting.\" *Earth and Space Science*, vol. 8, no. 8, 2021, e2020EA001610."
indexed_texts: "22"
indexed_chars: "109446"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T02:02:48"
---

# Analysis of Crystalline Rock Permeability Versus Depth in a Canadian Precambrian Rock Setting.

## One-line Summary

本研究汇编了加拿大原子能有限公司（AECL）在1970‑1996年间于加拿大地盾七个研究区获取的原位钻孔水力试验渗透率数据，区分等效多孔介质（EPM）岩体和断裂带（FZs），并利用幂律函数量化渗透率随深度的变化关系。

## Research Question

如何定量描述前寒武纪结晶岩中渗透率随深度的变化，并在区分岩体基质与导水断裂带的前提下，确定等效多孔介质和断裂带各自的渗透率‑深度关系？

## Study Area / Data

研究数据来源于加拿大地盾上的七个AECL研究区（RAs）：Chalk River、East Bull Lake、Atikokan、Whiteshell、Underground Research Laboratory（URL）、White Lake 和 Overflow Bay。其中，前五个研究区具有定量水力测试数据（White Lake 和 Overflow Bay 因运行时间短或未完全运行，数据不完整）[Snowdon 2021, pp. 3‑5]。数据覆盖深度约从地表至1 km，主要包括钻孔水力试验获得的渗透率（或水力传导系数）、钻孔电视与声波成像测井判读的裂缝信息、温度测井等。数据集整理自AECL数十年的硬拷贝报告和技术文件 [Snowdon 2021, pp. 1‑2, 5‑5]。

## Methods

1. **数据分类**：利用钻孔影像测井将观测到开放且水力连通的裂缝和断层划分为断裂带（FZs）；其余区域归为等效多孔介质岩体（EPM），EPM包含完整岩石以及闭合、未连通或仅有限连通的小尺度裂隙。部分未明确观测到开放裂缝但渗透率异常高的数据点被赋予低置信度标签，但仍保留在数据集中。进一步将所有数据合并为聚合介质（AM）进行EPM假设下的分析 [Snowdon 2021, pp. 8‑9]。

2. **温度、密度与粘度处理**：为将历史记录中的水力传导系数转换为渗透率，需已知流体密度和动态粘度。对缺失的温度数据，采用各研究区的线性地温梯度（如Atikokan 11.24°C/km, Chalk River 10.55°C/km, East Bull Lake 25.07°C/km, URL 9.9°C/km, Whiteshell 10.09°C/km）进行深度外推；再基于温度和已知盐度信息估算密度与动态粘度 [Snowdon 2021, pp. 6‑8]。

3. **趋势拟合**：对EPM和FZ两类数据分别绘制渗透率‑深度散点图，并使用幂律函数进行拟合：
   \[
   \log_{10}(k) = a + b \log_{10}(d)
   \]
   其中 \(k\) 为渗透率 (m²)，\(d\) 为深度 (m)，\(a\) 与 \(b\) 为拟合参数 [Snowdon 2021, pp. 8‑9]。

## Key Findings

- EPM岩体的渗透率随深度呈现下降趋势，该趋势可由幂律关系描述 [Snowdon 2021, pp. 8‑9]。
- 断裂带渗透率显著高于同深度EPM岩体，且离散度更大；其渗透率‑深度关系亦可用幂律拟合，但拟合效果与参数不同于EPM [Snowdon 2021, pp. 8‑9]。
- 此前虽然已认识到渗透率随深度递减，但定量化程度不足；本研究通过区分EPM与FZ，为精确表征裂隙岩体渗透性提供了基准 [Snowdon 2021, pp. 2‑3]。
- 温度梯度的线性外推虽简单，但在低渗透率区域被证明是准确的 [Snowdon 2021, pp. 8‑8]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| EPM岩体渗透率随深度呈幂律递减 | [Snowdon 2021, pp. 8‑9] | 数据取自Chalk River, East Bull Lake, Atikokan, Whiteshell, URL 五个研究区；剔除了识别为开放导水断裂带的测段 | 幂律拟合参数的具体数值未从索引片段中确认 |
| 断裂带渗透率高于EPM，且深度‑渗透率关系也可用幂律描述 | [Snowdon 2021, pp. 8‑9] | 断裂带由钻孔电视/声波成像测井判识为开放且水力连通 | 离散度更大，拟合效果异于EPM |
| 各研究区地温梯度分别为11.24, 10.55, 25.07, 9.9, 10.09°C/km | [Snowdon 2021, pp. 6‑8] | 基于多个文献的已有温度数据线性回归 | 用于外推缺失温度，进而计算密度和粘度 |
| AECL的七个研究区仅五个具备定量水力数据，White Lake 和 Overflow Bay 数据不全 | [Snowdon 2021, pp. 3‑5] | 研究区为代表性研究场地，非候选处置库场址 | White Lake与Overflow Bay未形成完整测试记录 |

## Limitations

- 原始数据存在缺失（温度、密度、粘度），虽通过地温梯度外推补全，但可能引入误差；不过在低渗透率区域线性外推的准确性尚可接受 [Snowdon 2021, pp. 8‑8]。
- 部分渗透率数据缺乏明确的裂缝观测记录，通过渗透率值推断为断裂带并降低置信度，这一分类方式具有主观性 [Snowdon 2021, pp. 8‑9]。
- 数据集仅覆盖加拿大地盾的五个有限研究区，空间代表性不足，直接外推至整个地盾或其它结晶岩地区需谨慎。
- 幂律拟合仅描述总体趋势，未考虑断裂网络的几何连通性与尺度效应。

## Assumptions / Conditions

- 钻孔漏失/水力测试段中未识别到开放裂缝的区域，其渗透率被假设为代表EPM岩体，即使包含小尺度或充填的非导水裂缝，仍认为对整体水力特性影响有限 [Snowdon 2021, pp. 8‑9]。
- 研究区地下水温度梯度在垂向上保持线性，且地温场稳定 [Snowdon 2021, pp. 6‑8]。
- 流体密度和动态粘度仅受温度和盐度控制，且盐度可通过区域地球化学信息合理估计 [Snowdon 2021, pp. 6‑8]。
- 幂律函数足以表征渗透率‑深度的经验关系，该方法借鉴了以往在地表水文过程中的应用 [Snowdon 2021, pp. 8‑9]。

## Key Variables / Parameters

- **渗透率 \(k\)** [m²]  
- **深度 \(d\)** [m]  
- **幂律拟合参数 \(a\)（截距）和 \(b\)（指数）**  
- **温度梯度** [°C/km]，各研究区不同（如Atikokan 11.24°C/km）  
- **流体密度和动态粘度**，由温度和盐度导出  
- **水力传导系数**，与渗透率通过流体属性关联  
- **断裂标识**（开放/闭合、水力连通性）

## Reusable Claims

1. 在加拿大地盾前寒武纪结晶岩中，剔除了大型活动断裂带后，等效多孔介质（EPM）岩体的渗透率随深度可用幂律关系 \(\log_{10}(k) = a + b \log_{10}(d)\) 描述，呈显著下降趋势。[Snowdon 2021, pp. 8‑9]  
   **适用条件**：低渗透结晶岩环境；深度范围约0‑1000 m；数据集需通过影像测井去除已识别的导水断裂带；水力测试段以单孔压水/注水试验为主。  
   **限制**：该关系为经验拟合，未包含力学或化学耦合影响；外推至更大深度或不同应力场区域时需验证。

2. 断裂带的渗透率通常比同深度EPM岩体高数个数量级，且渗透率‑深度关系离散度高，但仍可用幂律形式拟合。[Snowdon 2021, pp. 8‑9]  
   **适用条件**：断裂带定义为基于钻孔影像判别的开放、水力连通构造；数据来自加拿大地盾5个研究区。  
   **限制**：未区分断裂的产状、充填物和近期活动性，碎裂程度的影响未定量化。

3. 对于历史钻孔数据，当地层温度测值缺失时，可利用研究区线性地温梯度进行深度插值外推，并进一步估算流体密度和粘度，以完成渗透率与水力传导系数的转换。[Snowdon 2021, pp. 6‑8]  
   **适用条件**：低渗透结晶岩环境，热对流可忽略；已有若干深度的温度测值支持梯度计算。  
   **限制**：线性假设可能在高渗透或对流活跃区域失效；盐度若非实测，其估算误差会传播到粘度/密度。

## Candidate Concepts

- [[permeability-depth relationship]]
- [[equivalent porous medium]]
- [[fracture zone]]
- [[crystalline rock]]
- [[deep geologic repository]]
- [[hydraulic conductivity]]
- [[power law fitting]]
- [[Canadian Shield]]
- [[borehole hydraulic testing]]
- [[fractured rock hydrogeology]]
- [[temperature gradient correction]]
- [[fluid density and viscosity estimation]]

## Candidate Methods

- [[power law regression of permeability-depth data]]
- [[fracture identification from borehole televiewer and acoustic televiewer]]
- [[linear temperature gradient extrapolation for missing downhole data]]
- [[density and viscosity calculation from temperature and salinity]]
- [[permeability classification by confidence level from indirect evidence]]
- [[aggregate medium approach for fractured rock]]

## Connections To Other Work

- 幂律函数在多种水文过程中的适用性已由 Cardenas (2008)、Harman et al. (2009)、Rupp & Selker (2005)、Selker et al. (1999) 和 Snowdon & Craig (2015) 等研究报道，本研究将其引入结晶岩渗透率‑深度关系建模 [Snowdon 2021, pp. 8‑9]。
- 渗透率随深度下降的总体趋势曾被 W. Sanford (2017) 指出“缺乏良好量化”，本研究填补了这一空缺 [Snowdon 2021, pp. 2‑3]。
- 对裂隙网络作为优先流动路径的认识与 Tsang et al. (2015) 一致，本研究通过区分 EPM 与 FZ 实现了分别表征 [Snowdon 2021, pp. 2‑3]。
- 前期 AECL 的研究着重于场地表征方法与验证，如 Stone (1984)、Brown & Kamineni (1989)、Read (1990a, 1990b) 等，其数据是本研究的基础 [Snowdon 2021, pp. 1‑2, 5‑5]。
- 关于加拿大地盾 DGR 的可行性，早期由 Atomic Energy of Canada Limited (1994) 和 Davison, Chan, and Brown (1994) 提出，并最终由 NWMO 推荐为 APM 方案 [Snowdon 2021, pp. 1‑1]。本研究的渗透率关系可为 DGR 安全评价提供输入。

## Open Questions

未从索引片段中确认。可能包括：
- 幂律关系在更深部（>1 km）是否依然成立？
- 断裂带渗透率的分散性如何与具体的断裂几何、应力场关联？
- 是否可将 EPM 和 FZ 的渗透率关系耦合进区域尺度地下水模型？
- 温度梯度外推方法在盐度梯度显著或对流存在时的偏差如何量化？

## Source Coverage

本页依据论文的 22 个索引片段生成。片段主要覆盖了引言（背景、DGR 概念、AECL 研究动机）、研究区与数据描述（七个研究区的历史、钻孔数与测试类型）、部分方法细节（数据分类原则、温度处理、幂律拟合），以及概要性关键发现。具体的幂律拟合参数值（a 和 b）、详细的散点图/统计量、讨论部分的机理解释、与前人模型的定量对比等重要信息尚未在索引片段中出现，因此本页的 Core Evidence 和 Reusable Claims 偏向定性或半定量陈述。若需精确量化结果，须参考原文全文。
