---
type: "paper"
paper_id: "2020-chen-equivalent-permeability-distribution-for-fractured-porous-rocks-the-influence-of-fract"
title: "Equivalent Permeability Distribution for Fractured Porous Rocks: The Influence of Fracture Network Properties."
status: "draft"
source_pdf: "data/papers/2020 - Equivalent Permeability Distribution for Fractured Porous Rocks The Influence of Fracture Network Properties.pdf"
citation: "Chen, Tao. \"Equivalent Permeability Distribution for Fractured Porous Rocks: The Influence of Fracture Network Properties.\" *Geofluids*, vol. 2020, 2020, article ID 6751349, 12 pp., https://doi.org/10.1155/2020/6751349."
indexed_texts: "12"
indexed_chars: "56247"
compiled_at: "2026-04-27T19:41:53"
---

# Equivalent Permeability Distribution for Fractured Porous Rocks: The Influence of Fracture Network Properties.

## One-line Summary

本研究使用多重边界方法（multiple boundary method）对二维随机离散裂隙模型进行等效渗透率升尺度分析，发现等效渗透率张量分量的统计分布强烈依赖于裂隙几何属性，其直方图形状随裂隙长度和数量增加从幂律分布向对数正态分布转变 [Chen 2020, pp. 1-2, pp. 4-6]。

## Research Question

裂隙网络几何属性（如裂隙长度、裂隙数量、裂隙密度）如何影响裂隙多孔岩石的等效渗透率分布？特别关注等效渗透率张量不同分量（kxx、kyy、kxy）的统计特征及其随裂隙参数的变化规律 [Chen 2020, pp. 1-2, pp. 4-6]。

## Study Area / Data

本研究无实际野外研究区，基于随机生成的二维离散裂隙模型（DFM）进行数值模拟。模型域为 20 m × 20 m，裂隙长度服从幂律分布，下限 lmin 从 4 m 变化至 10 m，上限 lmax 固定为 40 m，裂隙数量 N 从 50 变化至 125 [Chen 2020, pp. 2-3]。面裂隙强度 P21 范围为 0.79 至 4.03 m/m²，与 Äspö 硬岩实验室的测量数据范围一致 [Chen 2020, pp. 8-9]。基质渗透率的具体值未从索引片段中确认。

## Methods

采用多重边界方法（multiple boundary method）进行等效渗透率升尺度计算。在线性边界条件下，利用 MATLAB Reservoir Simulation Toolbox (MRST) 对离散裂隙模型进行网格划分和稳态流问题求解，基于达西定律的矩阵形式计算等效渗透率张量分量 [Chen 2020, pp. 3-4]。裂隙网络通过 ADFNE 代码随机生成，采用幂律长度分布和随机中心位置 [Chen 2020, pp. 2-3]。对于每个裂隙几何参数组合（lmin 和 N），生成十个实现以获取统计结果 [Chen 2020, pp. 8-9]。

## Key Findings

- 等效渗透率张量分量 kxx、kyy 和 kxy 的直方图形状显著不同。kxx 和 kyy 在裂隙长度和数量较低时呈幂律分布，随裂隙长度和数量增加逐渐转变为对数正态分布；kxy 呈对称的正态分布，其取值范围随裂隙长度和数量扩大 [Chen 2020, pp. 4-6, pp. 6-8]。
- 对角线等效渗透率张量分量（kxx 和 kyy）的均值随无量纲裂隙密度 ρ 线性增加 [Chen 2020, pp. 8-9]。
- 对角线分量与裂隙网络几何之间存在强相关性：k′xx 和 k′yy 随裂隙长度和数量增大而增大 [Chen 2020, pp. 8-9]。
- 当裂隙较少且较短时，大量网格块被基质渗透率主导（裂隙未穿透或低于逾渗阈值），导致等效渗透率偏低 [Chen 2020, pp. 4-6]。

## Limitations

- 本研究采用二维模型，假设裂隙垂直延伸，其连通性和等效渗透率可能与三维模型存在差异；尽管在高裂隙密度下可通过适当校正预测三维等效渗透率，但二维到三维的推广取决于具体地质背景 [Chen 2020, pp. 9-10]。
- 三维升尺度方法面临数据可用性、采样偏差校正、缺乏自然裂隙岩石基准模型以及高效计算平台等限制 [Chen 2020, pp. 9-10]。
- 对于幂律长度分布，每个参数组合仅生成十个随机实现，但结果显示统计结果相对稳定 [Chen 2020, pp. 8-9]。
- 模型域大小（20 m × 20 m）是对场尺度数据可用性和计算成本的折中 [Chen 2020, pp. 8-9]。

## Reusable Claims

- 对于对角线等效渗透率张量分量（kxx 和 kyy），其直方图形状随裂隙长度和数量增加从幂律分布变为对数正态分布 [Chen 2020, pp. 4-6]。
- 等效渗透率对角分量的均值随裂隙密度线性增加 [Chen 2020, pp. 8-9]。
- 裂隙网络几何属性（裂隙长度、数量）与等效渗透率对角分量之间存在强相关性 [Chen 2020, pp. 8-9]。
- 当裂隙网络连通性较差（如裂隙未穿透网格块或低于渗流阈值）时，等效渗透率由基质渗透率主导，呈现幂律分布 [Chen 2020, pp. 4-6]。
- 使用仅计算单一边界流量的单边界方法可能会低估等效渗透率；线性边界条件更接近地下真实流况，其计算结果与分析解吻合较好 [Chen 2020, pp. 3-4]。
- 二维模型结果向三维推广时，需根据具体地质背景和裂隙几何特征进行校正 [Chen 2020, pp. 9-10]。

## Candidate Concepts

- [[裂隙多孔岩石]]
- [[等效渗透率张量]]
- [[离散裂隙模型]]
- [[幂律长度分布]]
- [[裂隙网络连通性]]
- [[代表单元体积]]
- [[基质渗透率]]
- [[升尺度方法]]

## Candidate Methods

- [[多重边界方法]]
- [[线性边界条件]]
- [[MRST]]
- [[ADFNE代码]]
- [[有限元网格划分]]
- [[稳态流模拟]]

## Open Questions

- 如何将二维裂隙模型的等效渗透率统计分布可靠地推广到三维自然裂隙系统？
- 在不同裂隙几何参数下，等效渗透率张量分量出现幂律-对数正态转变的临界条件（如裂隙密度、长度比）是什么？
- 更现实的裂隙网络（如考虑裂隙开度-长度相关、裂缝胶结作用）如何影响等效渗透率分布？
- 如何开发高效计算平台以支持大规模三维离散裂隙模型的流动模拟和升尺度分析？

## Source Coverage

本文索引片段覆盖了论文页码 pp. 1–2、pp. 2–3、pp. 3–4、pp. 4–6、pp. 6–8、pp. 8–9、pp. 9–10。所有结论均源自这些片段。
