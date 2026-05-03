---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2022-viswanathan-from-fluid-flow-to-coupled-processes-in-fractured-rock-recent-advances-and-new"
title: "From Fluid Flow to Coupled Processes in Fractured Rock: Recent Advances and New Frontiers."
status: "draft"
source_pdf: "data/papers/2022 - From Fluid Flow to Coupled Processes in Fractured Rock Recent Advances and New Frontiers.pdf"
collections:
citation: "Viswanathan, H. S., et al. \"From Fluid Flow to Coupled Processes in Fractured Rock: Recent Advances and New Frontiers.\" *Reviews of Geophysics*, vol. 60, no. 4, 2022."
indexed_texts: "84"
indexed_chars: "417765"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T10:44:57"
---

# From Fluid Flow to Coupled Processes in Fractured Rock: Recent Advances and New Frontiers.

## One-line Summary

综述回顾了裂隙岩体中流体流动到热-水-力-化（T-H-M-C）耦合过程的最新研究进展，强调通过整合现场与实验室实验、物理模拟及基于机器学习的不确定性量化来预测复杂裂隙系统的行为 [Viswanathan 2022, pp. 1-1]。

## Research Question

如何通过多尺度观测、物理建模和机器学习模拟器的集成，实现对裂隙岩体中受耦合过程控制的流体流动、溶质运移及力学变形行为的定量预测与不确定性量化 [Viswanathan 2022, pp. 1-1]？

## Study Area / Data

未指定特定地理区域；研究覆盖多种地下应用场景，包括CO₂封存、核废料处置、氢储存、地热能开发、核不扩散监测与油气开采等，涉及从分钟到千年的多时间尺度耦合过程 [Viswanathan 2022, pp. 2-3]。数据来源涵盖专用现场试验场地、原位钻孔传感数据（如分布式光纤温度/声波传感 DTS/DAS）、实验室岩石物理实验与数值模拟生成的数据 [Viswanathan 2022, pp. 5-6]。

## Methods

- **现场观测与监测技术**：利用钻孔分布式光纤传感（DFOS）实现温度（DTS）、应变和地震波场（DAS）的高时空分辨率监测，结合全波形反演（FWI）与机器学习进行地球物理成像 [Viswanathan 2022, pp. 5-6]；开发基于应力的层析成像法反演离散裂隙网络几何 [Viswanathan 2022, pp. 6-7]。
- **实验室实验**：在可控条件下复现原位温度、压力与应力，使用光学、X射线及声学方法直接观测裂隙几何与流动过程 [Viswanathan 2022, pp. 4-5]。
- **数值模拟**：基于离散裂隙网络与升尺度连续介质模型，利用高性能计算实现T-H-M-C耦合过程的力学化模拟 [Viswanathan 2022, pp. 4-5]。
- **不确定性量化与模拟器**：应用机器学习与图论构建仿真器（emulators），将力学模型加速三至四个数量级，以支持鲁棒不确定性量化和近实时分析 [Viswanathan 2022, pp. 4-5]。

## Key Findings

- 现场实验与密集监测提供了可约束模型的裂隙流动定量测量值 [Viswanathan 2022, pp. 1-2]。
- 实验室实验通过直接观测揭示了岩石属性、应力、位移和化学作用对裂隙开度与流动的单一裂隙级影响 [Viswanathan 2022, pp. 4-5]。
- 力学模型与机器学习仿真器的结合使得复杂裂隙网络的流动与运移不确定性量化成为可能 [Viswanathan 2022, pp. 4-5]。
- 分布式光纤传感技术显著提升了裂隙传播检测与微地震事件定位能力，但目前受限于单分量测量 [Viswanathan 2022, pp. 5-6]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 通过整合现场实验、实验室实验、模拟和不确定性量化，极大改善了对裂隙系统中流动与运移的预测能力 | [Viswanathan 2022, pp. 1-1] | 适用于CO₂封存、核废料处置、地热等多种应用 | 综述核心论点 |
| 80%的美国能源与50%的饮用水供应源于地下，裂隙是主要流动通道 | [Viswanathan 2022, pp. 1-2] | 基于Hubbard et al. (2015) 数据 | 强调裂隙研究的社会经济重要性 |
| 分布式声波传感（DAS）已用于检测裂隙传播与微地震定位，但单分量测量是当前限制 | [Viswanathan 2022, pp. 5-6] | 应用于非常规储层与结晶岩 | 技术优势与局限并存 |
| 机器学习仿真器可将裂隙模型计算加速3-4个数量级 | [Viswanathan 2022, pp. 4-5] | 使用图论与机器学习方法 | 使近实时分析成为可能 |
| 核不扩散监测需探测地下核爆产生的气体，其渗漏可在几分钟到数月内发生 | [Viswanathan 2022, pp. 2-3] | 涉及核爆引发的T-H-M-C过程 | 时间尺度跨度极大 |

## Limitations

- 分布式光纤传感目前仅提供单分量测量，虽有多光纤电缆方案被提出，但全应变张量的实际解析尚未实现 [Viswanathan 2022, pp. 5-6]。
- 钻孔记录分析面临数据量过大的存储、传输与处理挑战 [Viswanathan 2022, pp. 6-7]。
- 综述本身覆盖范围极广（从实验室到现场、从力学模拟到不确定性量化），具体技术的定量效果对比未在本索引片段中提供。

## Assumptions / Conditions

- 模型与监测方法的有效性依赖于专用现场试验场地提供的高分辨率约束数据 [Viswanathan 2022, pp. 7-7]。
- 实验室实验依赖对原位条件的精确复现（压力、温度、应力）才能填补现场观测的知识空白 [Viswanathan 2022, pp. 4-5]。
- 机器学习仿真器的构建基于物理模型生成的数据集，其外推能力假设训练场景覆盖目标参数空间 [Viswanathan 2022, pp. 4-5]。

## Key Variables / Parameters

- 裂隙开度（fracture aperture）、渗透率（permeability）
- 温度（T）、水压（H）、应力与应变（M）、化学浓度（C）——即T-H-M-C耦合参数
- 离散裂隙网络几何参数（密度、长度、方位）
- 机器学学习仿真器的加速比（3-4个数量级）[Viswanathan 2022, pp. 4-5]
- 时间尺度跨域（分钟至千年）[Viswanathan 2022, pp. 2-3]

## Reusable Claims

- 裂隙虽占据岩体极小体积，但常常主导流体流动与溶质运移行为，这一属性在CO₂封存、核废料处置、地热及油气开采中均成立 [Viswanathan 2022, pp. 1-1]。
- 分布式声波传感（DAS）结合低噪声底板应变测量，可有效检测非常规储层中水力压裂后的裂隙传播至邻井的动态，这一能力依赖于现代DAS询问器的亚纳应变级分辨力 [Viswanathan 2022, pp. 5-6]。
- 机器学习模拟器可将基于物理的裂隙流动-运移模型加速3-4个数量级，从而支持多情景不确定性量化；该加速效果的前提是模拟器基于充分的物理模型训练 [Viswanathan 2022, pp. 4-5]。
- 专用长期现场试验场（密集表征与监测）对于验证裂隙流预测模型、发展概念模型和测试新监测技术不可或缺，尽管其部署在工业项目中可能成本过高 [Viswanathan 2022, pp. 7-7]。

## Candidate Concepts

- [[thermo-hydro-mechanical-chemical coupling]]
- [[fracture aperture]]
- [[discrete fracture network]]
- [[distributed fiber optic sensing]]
- [[full waveform inversion]]
- [[mechanical fracture deformation]]
- [[seismic anisotropy in fractured media]]
- [[subsurface uncertainty quantification]]

## Candidate Methods

- [[distributed temperature sensing DTS]]
- [[distributed acoustic sensing DAS]]
- [[machine learning emulator]]
- [[stress-based tomography fracture characterization]]
- [[borehole image log analysis]]
- [[high performance computing fracture simulation]]
- [[multifidelity surrogate modeling]]

## Connections To Other Work

索引片段未直接提供与其他具体论文的比较或关联关系。从主题上可连接到国家科学院2015年报告《Characterization, Modeling, Monitoring and Remediation》[Viswanathan 2022, pp. 3-4] 和 DOE 2015年圆桌报告中关于耦合过程的关键需求 [Viswanathan 2022, pp. 3-4]；技术上连接至 TOUGH-FLAC 等 T-H-M 数值模拟代码 [Viswanathan 2022, pp. 6-7]。其余具体论文关系未从片段中确认。

## Open Questions

- 如何从单分量DAS测量突破至全应变张量解析 [Viswanathan 2022, pp. 5-6]？
- 在大数据范式下，如何有效融合多源噪声数据以改进地下模拟约束 [Viswanathan 2022, pp. 3-4]？
- 化学过程主导的长期（千年尺度）裂隙行为预测如何验证 [Viswanathan 2022, pp. 2-3]？

## Source Coverage

本页依据索引片段共84段，覆盖了综述的引言（Introduction）、四大核心主题（现场观测、实验室实验、T-H-M-C模拟、不确定性量化与仿真器）的概述和高层级要点。片段集中于摘要、论文框架和部分技术详描（尤其是DFOS部分），对具体模拟算法、各应用领域的定量案例、升尺度方法及化学耦合细节的覆盖可能不足。缺失的重要部分包括：各章节的详细综述内容、具体数值模拟算法的比较、机器学习仿真器的训练策略、以及所有具体文献的独立结论。
