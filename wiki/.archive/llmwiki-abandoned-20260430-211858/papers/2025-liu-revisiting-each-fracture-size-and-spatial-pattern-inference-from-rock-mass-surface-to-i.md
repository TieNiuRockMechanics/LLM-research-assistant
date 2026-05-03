---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2025-liu-revisiting-each-fracture-size-and-spatial-pattern-inference-from-rock-mass-surface-to-i"
title: "Revisiting Each Fracture Size and Spatial Pattern: Inference from Rock Mass Surface to Interior."
status: "draft"
source_pdf: "data/papers/2025 - Revisiting each fracture size and spatial pattern Inference from rock mass surface to interior.pdf"
collections:
  - "zotero new"
citation: "Liu, Yongqiang, et al. \"Revisiting Each Fracture Size and Spatial Pattern: Inference from Rock Mass Surface to Interior.\" *Journal of Rock Mechanics and Geotechnical Engineering*, vol. 17, 2025, p. 1399, doi:10.1016/j.jrmge.2024.08.026."
indexed_texts: "14"
indexed_chars: "68092"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T15:34:29"
---

# Revisiting Each Fracture Size and Spatial Pattern: Inference from Rock Mass Surface to Interior.

## One-line Summary
提出一种从岩石露头矩形采样窗口中的裂缝迹长推断每个裂缝最可能直径（MPD）与真实空间分布模式的新方法，并通过蒙特卡洛模拟验证，平均直径预测误差约为1 m [Liu 2025, pp. 1-1, 10-11]。

## Research Question
如何从岩石露头表面（cut-plane）观测到的裂缝迹长（trace length）出发，为每一个裂缝确定其最可能直径（MPD），并反演出裂缝在岩体内部的三维真实空间分布模式？核心挑战在于将单一裂缝的迹长与整个露头的统计特征关联起来，同时解决非唯一逆问题 [Liu 2025, pp. 1-1, 2-3]。

## Study Area / Data
- **数值模拟数据**：采用蒙特卡洛方法生成的离散裂缝网络，裂缝直径服从对数正态分布 log N(1.6, 0.4²)，直径范围 1~13 m；在三维裂缝空间内沿 Y=10 m、25 m、40 m 三个切面生成包含迹（contained traces）的二维迹图，用于验证方法 [Liu 2025, pp. 8-9]。
- **工程案例**：将方法应用于某道路工程边坡上的一个采样窗口，具体位置、几何参数和案例结果未从索引片段中确认 [Liu 2025, pp. 1-1, 2-3]。

## Methods
主要步骤框架如下 [Liu 2025, pp. 1-1, 2-8]：  
1. **选定包含迹**：仅使用矩形采样窗口内两端均可观测的包含迹（contained traces，N₂），以消除截尾偏差（censoring bias） [Liu 2025, pp. 3-5]。  
2. **方向偏差校正**：利用矢量方法计算裂缝在各个方向上的实际频率，为多扫描线法提供方向期望值 [Liu 2025, pp. 5-6]。  
3. **估计真实迹长分布参数**：采用多扫描线法（multi-scanline method）估算包含迹的真实平均迹长 mₗ；同时利用样本迹长的均值 m_c 与标准差 s_c，通过分布函数的标准差关系（sₗ = s_c · (mₗ/m_c)）推求真实标准差 sₗ [Liu 2025, pp. 5-7]。  
4. **推导裂缝尺寸分布参数**：假设裂缝尺寸服从对数正态分布，借助迹长与直径的高阶矩关系及克罗夫顿定理（Crofton's theorem），由 mₗ、sₗ 导出直径均值 m_D 和标准差 s_D [Liu 2025, pp. 6-8]。分布模型通过对数正态性验证（比较三阶矩与四阶矩的关系，计算相对误差 RE）确认 [Liu 2025, pp. 7-8]。  
5. **确定单个裂缝的 MPD**：基于立体学原理，建立 MPD 与迹长 l、s_D 之间的经验线性关系 MPD = a·l + b，从而为窗口内每条裂缝赋予最可能直径 [Liu 2025, pp. 4, 8-10]。  
6. **反演空间分布模式**：在获得所有裂缝 MPD 后，利用空间几何关系恢复裂缝在岩体内部的三维真实位置与展布 [Liu 2025, pp. 2-3, 8]。

## Key Findings
1. **MPD 可求解性**：当裂缝尺寸服从对数正态分布时，MPD 存在有意义的非零解；若假设指数分布或伽马分布，概率密度在 D=0 处取最大值，与天然裂缝不符 [Liu 2025, pp. 3-5]。  
2. **模拟验证精度**：三个切面的 MPD 预测值与真实直径对比，平均绝对误差（MAE）约为 1 m；在 50 m² 露头、含有 300 余条直径 1~13 m 裂缝的场景中，该误差被认为可接受 [Liu 2025, pp. 10-11]。  
3. **MPD 分布合理性**：推断得到的 MPD 集合服从对数正态分布（KS 检验 p 值为 0.037~0.043），与真实直径分布接近 [Liu 2025, pp. 10-11]。  
4. **大裂缝贡献主要误差**：预测误差可能主要由大型裂缝引起，因为大裂缝的绝对误差空间更大 [Liu 2025, pp. 10-11]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 采用多扫描线法估计 mₗ，避免传统采样窗口法（Kulatilake & Wu 1984b）在处理仅含包含迹时失效率 mₗ=0 的问题 | [Liu 2025, pp. 5-7] | 仅对包含迹（R₀=0, R₂=1）有效；扫描线数取 m=2N₂+N₁ | 使用矢量方法提供方向期望值 |
| 由迹长矩关系推导 m_D 与 s_D 的公式 (23) 可解析求解，并通过克罗夫顿定理的高阶矩验证对数正态假设 | [Liu 2025, pp. 6-8] | 裂缝尺寸须服从对数正态分布；迹长与直径的分布模型需相同 | 若 RE 值不满足则分布假设不成立 |
| 蒙特卡洛模拟中三个切面的 MPD 经验关系分别为 MPD=1.034l+0.909 (Y=25 m)、1.036l+0.948 (Y=10 m)、1.033l+0.901 (Y=40 m) | [Liu 2025, pp. 9-10] | 裂缝直径对数正态 log N(1.6,0.4²)，下限 1 m，上限 13 m | 线性关系依赖于该模拟数据集的 s_D |
| MPD 预测的 MAE 约 1 m，MAPE 未给出具体值，误差主要来自大裂缝 | [Liu 2025, pp. 10-11] | 露头尺寸约 50 m²，裂缝数量>300 | 文中称可接受，但未与工程容忍度对比 |

## Limitations
- 方法假设裂缝为无厚度的圆形盘状结构，对其他形状（如多边形、方形）的推广仅属前景性提及，未给出验证 [Liu 2025, pp. 2-3]。
- 裂缝尺寸必须服从对数正态分布，指数分布和伽马分布无法获得有意义的 MPD [Liu 2025, pp. 3-5]。
- 依赖于包含迹的子集，窗口内大量截尾迹未直接进入 MPD 推断，可能导致信息损失 [Liu 2025, pp. 3-5]。
- 文中工程应用实例仅在摘要和方法概述中提及，其实际参数、预测精度与适用条件未从索引片段中确认。
- 蒙特卡洛模拟仅使用了一个特定的裂缝集参数（log N(1.6, 0.4²)），方法对不同变异性参数和分布模型的敏感性未充分展示。

## Assumptions / Conditions
- 裂缝为无厚度的圆形盘 [Liu 2025, pp. 2-3]。
- 裂缝尺寸的总体分布为对数正态分布 [Liu 2025, pp. 3-5, 6-8]。
- 迹长分布 f(l) 与裂缝尺寸分布 g(D) 共用相同的变异系数（COV）和标准差（s_D = sₗ），且分布类型一致 [Liu 2025, pp. 1-2, 6-7]。
- 研究只使用矩形采样窗口内两端可观测的包含迹，假定这些迹能代表露头裂缝的全貌 [Liu 2025, pp. 3-5]。
- 方向偏差校正中，所有裂缝的倾向预先未知，故设 di=120% 平均迹长，该假设可能引入误差 [Liu 2025, pp. 5-6]。
- 多扫描线法需在窗口内均匀铺设正交扫描线，扫描线数量按 m=2N₂+N₁ 设置 [Liu 2025, pp. 6-7]。
- 蒙特卡洛模拟的裂缝网络为单组、平行切割，实际岩体可能更复杂 [Liu 2025, pp. 8-9]。

## Key Variables / Parameters
- **迹长 (l)**：裂缝与露头相交形成的线段长度；重点是包含迹的观测值 [Liu 2025, pp. 2-3]。
- **最可能直径 (MPD)**：使直径条件概率密度函数取最大值的直径，每条裂缝独立确定 [Liu 2025, pp. 2-4]。
- **真实迹长分布参数**：均值 mₗ、标准差 sₗ；通过多扫描线法和标准差关系式估算 [Liu 2025, pp. 5-7]。
- **裂缝尺寸分布参数**：直径均值 m_D、标准差 s_D；由 mₗ 和 sₗ 通过式 (23) 导出 [Liu 2025, pp. 6-8]。
- **采样窗口参数**：宽度 w、高度 h；用于方向概率和多扫描线法计算 [Liu 2025, pp. 5-6]。
- **扫描线参数**：扫描线长度 Lⱼ、相对视倾角 φⱼ、预期相交数 Mⱼ；m 为扫描线总数 [Liu 2025, pp. 6-7]。
- **高阶矩验证量**：E(D⁴)/E(D²) 与 4E(l³)/3E(l) 的比较；用于判断对数正态假设是否成立，相对误差 (RE) 见式 (25) [Liu 2025, pp. 7-8]。

## Reusable Claims
1. **仅当裂缝尺寸服从对数正态分布时，基于概率的 MPD 才有非零、实际意义的解；若假设指数或伽马分布，MPD 位于 D=0，与天然露头观测矛盾 [Liu 2025, pp. 3-5]。** 适用条件：裂缝直径分布未知，试图通过含概率密度最大值的推导 MPD。  
2. **在矩形采样窗口中，若仅使用包含迹（R₀=0, R₂=1），传统 Kulatilake & Wu (1984b) 方法会错误给出 mₗ=0；此时应采用多扫描线法，并取扫描线数 m=2N₂+N₁ 以得到可靠的平均迹长估计 [Liu 2025, pp. 5-7]。** 适用条件：窗口内存在可计数的 N₁ 和 N₂。  
3. **从迹长统计到裂缝尺寸统计的推导可通过高阶矩关系实现：m_D 和 s_D 由 mₗ、sₗ 通过式 (23) 计算，并借助克罗夫顿定理的高阶矩验证对数正态假设 [Liu 2025, pp. 6-8]。** 限制：需确认迹长样本满足对数正态分布，且式 (24) 的 RE 值可接受。  
4. **在 Monte Carlo 模拟环境中，MPD 与迹长近似呈线性关系，线性系数依赖 s_D；当 s_D 固定时，可直接通过拟合方程 MPD=1.034l+0.909 等快速估算 [Liu 2025, pp. 9-10]。** 适用条件：裂缝直径范围 1~13 m，对数正态 log N(1.6, 0.4²)；推广前需重新标定 s_D。  
5. **针对 50 m² 规模的裂缝露头，MPD 预测的平均绝对误差约为 1 m，可为该尺度下的工程判定提供参考，但大尺寸裂缝的预测误差可能更大 [Liu 2025, pp. 10-11]。** 证据来自仿真，实际工程使用需结合现场数据验证。

## Candidate Concepts
- [[fracture size distribution]]  
- [[discrete fracture network (DFN)]]  
- [[stereology]]  
- [[trace length estimation]]  
- [[sampling window bias correction]]  
- [[orientation bias correction]]  
- [[Monte Carlo simulation of fractures]]  
- [[Crofton’s theorem]]  
- [[rock mass characterization]]  
- [[fracture spatial pattern]]  

## Candidate Methods
- [[multi-scanline method]]  
- [[rectangular sampling window technique]]  
- [[vector method for orientation frequency]]  
- [[high-order moment relationship]]  
- [[log-normal distribution fitting]]  
- [[Kolmogorov-Smirnov (KS) test]]  
- [[maximum likelihood estimation for spatial patterns]]  
- [[spatial geometric inversion]]  

## Connections To Other Work
- **与 Kulatilake & Wu (1984b)** 对比：本研究指出其方法在仅使用包含迹时失效，进而引入多扫描线法进行改进 [Liu 2025, pp. 5-6]。  
- **与 Zhang & Einstein (1998, 2000)** 继承：在迹长分布估计、矩关系和克罗夫顿定理验证方面沿用并扩展了他们的框架，不同处在于最终目标是每条裂缝的 MPD 而不仅是总体分布 [Liu 2025, pp. 1-2, 6-7]。  
- **与 Villaescusa & Brown (1992)** 的关系：同样涉及利用高阶矩验证裂缝尺寸分布类型，可作为比较基准；本文将其思路推进至个体裂缝推断 [Liu 2025, pp. 1-2]。  
- 基于片段，未发现与其他工作的直接定量对比。

## Open Questions
- 当裂缝尺寸不服从对数正态分布时，是否存在替代的 MPD 求解思路？未从索引片段中确认。
- 方法在非圆盘状裂缝（如多边形或高斯曲面）下的适用性与修正方案未给出理论和实验支持 [Liu 2025, pp. 2-3]。
- 工程案例的具体参数、MPD 预测表现以及与现场实测直径的对比结果未在片段中披露。
- 对裂缝密度高、迹线大量截断的露头，仅依赖包含迹会否丢失关键大尺度信息？该方法对窗口大小和迹线数量的敏感性未充分讨论。
- 能否将 MPD 反演与离散裂缝网络（DFN）建模管道无缝衔接，使推断结果直接用于后续渗流或稳定性分析？片段未涉及。

## Source Coverage
本知识页依据 14 个索引片段编制，覆盖了论文的摘要、引言、方法描述（第 2‑3 节）以及蒙特卡洛模拟结果（第 4 节）的核心内容。关于工程案例应用（第 5 节）、讨论与结论部分的关键阐述未包含在片段中，因此该方法在实际现场条件下的表现、不确定性量化以及与既往方法的全面对比等可能未完整捕捉。本页所有陈述均严格取自所提供的片段；存在不确定性处已标注“未从索引片段中确认”。
