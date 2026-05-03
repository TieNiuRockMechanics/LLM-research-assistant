---
type: "paper"
paper_id: "2016-hyman-fracture-size-and-transmissivity-correlations-implications-for-transport-simulations"
title: "Fracture size and transmissivity correlations Implications for transport simulations in sparse three-dimensional discrete fracture networks following a truncate"
status: "draft"
source_pdf: "data/papers/2016 - Fracture size and transmissivity correlations Implications for transport simulations in sparse three-dimensional discrete fracture networks following a truncate.pdf"
citation: "Hyman, J. D., et al. \"Fracture Size and Transmissivity Correlations: Implications for Transport Simulations in Sparse Three-Dimensional Discrete Fracture Networks Following a Truncated Power Law Distribution of Fracture Size.\" *Water Resources Research*, vol. 52, no. 6, 2016, pp. 4806–4825. doi:10.1002/2016WR018806. Accessed 2026."
indexed_texts: "20"
indexed_chars: "98299"
compiled_at: "2026-04-27T19:34:43"
---

# Fracture size and transmissivity correlations: Implications for transport simulations in sparse three-dimensional discrete fracture networks following a truncated power law distribution of fracture size

## One-line Summary

本文系统研究了裂缝尺寸与导水率之间采用不同相关性（完美相关、半相关、不相关及常数关系）对稀疏三维离散裂隙网络（DFN）中流动与溶质传输模拟结果的影响，发现采用正相关性会导致更早的突破时间和更高的有效渗透率，但传输路径主要由裂隙网络几何决定[Hyman 2016, pp.1-1, 2-3]。

## Research Question

- 裂缝尺寸与导水率之间的不同函数关系（假设完全相关、半相关、完全不相关）如何影响稀疏三维离散裂隙网络中的流动与传输模拟结果？[Hyman 2016, pp.1-1]
- 特别是，这些关系对有效渗透率、保守溶质的突破时间以及网络内传输发生位置的影响是什么？[Hyman 2016, pp.2-3]

## Study Area / Data

- 研究基于一个半通用（semigeneric）的合成DFN模型，该模型松散地基于瑞典福斯马克（Forsmark）场地的受干扰花岗岩，该场地是瑞典用于乏核燃料地下处置库的潜在宿主岩层[Hyman 2016, pp.3-4]。
- 网络包含三组圆形裂隙，方向遵循Fisher分布；裂隙半径从截断幂律分布中采样，幂律指数α在2.38–2.7之间，上、下截止半径与域尺寸之比分别为0.56和0.015[Hyman 2016, pp.4-5]。
- 计算域为边长为1000 m的立方体，共生成约11804条裂隙，平均P32值为0.057 m⁻¹（仅连接入口和出口的背斜网络）[Hyman 2016, pp.4-5]。
- 所用DFN生成参数（表1）基于SKB对Forsmark场地的详细调查结果[Hyman 2016, pp.4-5]。
- 未从索引片段中确认具体的野外实测数据细节或验证数据集，仅提及采用Posiva流量日志（PFL）进行软校准[Hyman 2016, pp.5-6]。

## Methods

1. **DFN生成**：采用三组圆形裂隙，方向由Fisher分布生成（参数见表1），半径由截断幂律分布采样（公式2）[Hyman 2016, pp.3-5]。每条裂隙被分配均匀孔径（代表变孔径的平均值），并使用立方定律（Cubic Law）建立孔径与导水率之间的关系[Hyman 2016, pp.4-5]。
2. **四种尺寸-导水率关系**（表2）：
   - **相关模型**：\(\log(T) = \log(a r^b)\)，其中 \((a,b) = (1.3 \times 10^{-9}, 0.5)\)。
   - **半相关模型**：\(\log(T) = \log(a r^b) + \sigma_T N(0,1)\)，其中 \(\sigma_T = 0.7\)。
   - **不相关模型**：\(\log(T) = \mu_T + \sigma_T N(0,1)\)，其中 \(\mu_T = -18.79, \sigma_T = 0.8\)。
   - **常数模型**：\(\log(T) = \mu_T = -18.79\)。
   参数选择确保所有模型的平均导水率相同，两个随机模型（半相关与不相关）的孔径和导水率分布相似[Hyman 2016, pp.6-7]。
3. **流动模拟**：使用PETSc工具箱的PFLOTRAN并行求解器，求解稳态单相流，不考虑重力。边界条件为：沿流向（垂直轴）设恒定压差，侧向边界无流动[Hyman 2016, pp.7-8]。
4. **传输模拟**：在稳态流动场中，从入口平面（z=0）均匀注入保守溶质粒子，通过求解路径线方程追踪每个粒子的轨迹，计算突破时间和有效渗透率等指标[Hyman 2016, pp.7-8]。

## Key Findings

- 采用尺寸-导水率相关模型的网络比采用不相关或常数模型的网络具有更高的有效渗透率和更早的突破时间[Hyman 2016, pp.1-1, 2-3]。
- 裂隙网络几何（即裂隙的空间分布与连通性）在决定传输具体发生在网络内的位置方面起主要作用[Hyman 2016, pp.1-2, 2-3]。
- 尺寸-导水率关系则主要控制流动与传输的速度（时间尺度），而非路径本身[Hyman 2016, pp.1-2, 2-3]。
- 在包含随机项（半相关与不相关模型）的分布中，导水率分布呈现更宽的尾部（高值更多、低值更多且方差更大），而确定性相关模型由于半径的截断幂律分布而具有明确的截止[Hyman 2016, pp.6-7]。

## Limitations

- 模拟中未考虑重力，也未考虑基质中的流动或扩散[Hyman 2016, pp.7-8]。
- 每条裂隙被赋予均匀孔径，忽略裂隙内孔径非均匀性（但Makedonska等人发现这对稀疏DFN中传输特性影响很小）[Hyman 2016, pp.4-5]。
- 仅使用了立方定律，尽管已有研究指出孔径-导水率关系的选择会影响传输特性（如二次律），但本文未进行对比[Hyman 2016, pp.4-5]。
- 完美相关模型完全忽略导致同尺寸裂隙导水性差异的机械、化学及水文过程；半相关模型虽引入随机项，但仍未解释物理成因，且需要额外的现场数据来校准其参数[Hyman 2016, pp.5-6]。
- 不相关模型假定尺寸与导水率之间不存在任何关系，这可能高估了不确定性[Hyman 2016, pp.5-6]。

## Reusable Claims

- 在稀疏三维DFN中，采用裂缝尺寸与导水率正相关模型时，有效渗透率可显著高于无相关模型，且突破时间更早[Hyman 2016, pp.1-1]。
- 裂隙网络几何（而非尺寸-导水率关系）主导传输发生的位置；尺寸-导水率关系主要影响流动速度和时间尺度[Hyman 2016, pp.2-3]。
- 包含随机项的尺寸-导水率模型（半相关与不相关）会产生更宽的导水率分布和更厚的尾部，导致更多的高导水率和低导水率裂隙[Hyman 2016, pp.6-7]。
- 软校准方法（如匹配Posiva流量日志分布而非具体数据）可用于校准完美相关模型的参数，但半相关模型需要更多现场数据支持[Hyman 2016, pp.5-6]。

## Candidate Concepts

- [[离散裂隙网络 (DFN)]]
- [[立方定律]]
- [[Fisher分布]]
- [[截断幂律分布]]
- [[有效渗透率]]
- [[突破时间]]
- [[裂隙尺寸-导水率相关性]]
- [[稀疏裂隙网络]]
- [[合成DFN模型]]
- [[PFLOTRAN]]
- [[PETSc]]

## Candidate Methods

- [[PFLOTRAN并行流动求解器]]
- [[PETSc数值工具箱]]
- [[路径线粒子追踪]]
- [[Fisher分布抽样算法 (Wood, 1994)]]
- [[完美相关模型参数软校准方法]]
- [[半相关模型随机项生成方法]]
- [[稳态单相流与保守溶质传输模拟]]

## Open Questions

- 裂缝尺寸与导水率之间真正的函数形式是什么？目前仍存在争议，对数正态、幂律等模型均有提出且参数范围巨大[Hyman 2016, pp.1-2]。
- 如何从现场数据同时约束半相关模型中的确定性与随机参数？其物理基础尚未明确[Hyman 2016, pp.5-6]。
- 在包含基质扩散、重力或非立方律的情况下，上述四种关系对传输特性的相对影响是否会改变？（未从索引片段中确认，但为合理推断。）
- 校准后的参数是否具有场址可迁移性？（未从索引片段中确认。）

## Source Coverage

本页信息基于论文提供的以下索引片段（共20个索引片段中给出的前8个）：

- [Hyman 2016, pp.1-1]
- [Hyman 2016, pp.1-2]
- [Hyman 2016, pp.2-3]
- [Hyman 2016, pp.3-4]
- [Hyman 2016, pp.4-5]
- [Hyman 2016, pp.5-6]
- [Hyman 2016, pp.6-7]
- [Hyman 2016, pp.7-8]

其余12个索引片段未提供，部分结论可能缺失信息。
