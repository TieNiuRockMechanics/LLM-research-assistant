---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2019-moein-scaling-of-fracture-patterns-in-three-deep-boreholes-and-implications-for-constrainin"
title: "Scaling of Fracture Patterns in Three Deep Boreholes and Implications for Constraining Fractal Discrete Fracture Network Models."
status: "draft"
source_pdf: "data/papers/2019 - Scaling of Fracture Patterns in Three Deep Boreholes and Implications for Constraining Fractal Discrete Fracture Network Models.pdf"
collections:
  - "1文章:2D-3D分形关系"
  - "2文章钻孔裂缝分形关系"
citation: "Moein, Mohammad Javad Afshari, et al. \"Scaling of Fracture Patterns in Three Deep Boreholes and Implications for Constraining Fractal Discrete Fracture Network Models.\" *Rock Mechanics and Rock Engineering*, vol. 52, 2019, pp. 1723-1743. DOI: 10.1007/s00603-019-1739-7."
indexed_texts: "19"
indexed_chars: "93064"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T23:39:02"
---

# Scaling of Fracture Patterns in Three Deep Boreholes and Implications for Constraining Fractal Discrete Fracture Network Models.

## One-line Summary
本文提出一种基于双幂律模型的分形离散裂缝网络(DFN)生成方法，并系统评估了从一维钻孔裂缝间距数据约束二维/三维分形参数的可能性，发现无法从1D相关维数反推2D/3D参数，同时验证两点相关函数是1D分形维数最稳定可靠的估计方法，并报告了三个深钻孔裂缝分布的分形维数在0.86 – 0.88之间。

## Research Question
- 能否利用深钻孔中的1D裂缝间距分形特性来约束2D和3D裂缝网络模型？具体而言：从1D扫描线/钻孔获得的裂缝间距相关维数(D)是否可以估计2D或3D网络中裂缝中心的相关维数？
- 在1D情况下，哪种分形维数估计方法（盒计数、两点相关函数、幂律拟合）最为稳定和可靠？
- 实际深部钻孔中的裂缝分布是否表现出分形特征？如果是，其分形维数是多少？

## Study Area / Data
- **研究数据**：来自三个位于结晶岩中的深钻孔，分别位于瑞士巴塞尔(Basel)和法国绍尔茨－苏－福雷(Soultz-sous-Forêts)地热场地 [Moein 2019, pp. 1‑2]。
- **数据特征**：实际钻孔的裂缝分布被用于提取1D裂缝间距，应用两点相关函数分析其分形特征，覆盖超过两个数量级的尺度范围 [Moein 2019, pp. 1‑2]。
- **合成数据**：利用乘法级联过程生成具有已知相关维数D、长度指数a的1D、2D和3D合成裂缝分布，用于方法的基准测试和体视学关系评估 [Moein 2019, pp. 4‑6]。

## Methods
1. **裂缝网络生成方法**  
   - 采用双幂律模型，该模型由两个独立参数控制：相关维数D（描述裂缝中心的空间聚类）和长度指数a（控制裂缝长度的幂律分布） [Moein 2019, pp. 1, 3‑4]。  
   - 2D与3D裂缝网络基于乘法级联过程生成。该方法通过递归地将域细分为子块，并为每一块分配概率权重，最终生成满足目标D的分形密度分布；然后再为裂缝分配符合幂律的长度分布（l⁻ᵃ） [Moein 2019, pp. 4‑6]。  
   - 生成参数包括：域长度L、最小裂缝长度lmin、长度指数a、相关维数D、密度常数α；迭代次数n由lmin = L/2ⁿ确定 [Moein 2019, pp. 4‑5]。

2. **分形维数估计方法对比**  
   - 利用合成的1D裂缝间距分布，比较三种估计D的方法：盒计数(box‑counting)、两点相关函数(correlation integral)和幂律拟合(power‑law fitting) [Moein 2019, pp. 1‑2]。  
   - 两点相关函数计算裂缝中心的空间相关函数C(r)，并在对数坐标下求取局部斜率作为D的估计 [Moein 2019, pp. 3‑4, 6‑7]。

3. **边界效应处理**  
   - 针对2D DFN，检验了两种边界处理方法：移除伸出域外的裂缝、修剪伸出部分（使中心移入域内）对分形参数估计的影响 [Moein 2019, pp. 6‑7]。

4. **实际钻孔数据处理**  
   - 采用两点相关函数应用于三个深钻孔的观测裂缝分布，评估其分形尺度范围和分形维数D [Moein 2019, pp. 1‑2]。

## Key Findings
1. **1D→2D/3D的推断不可行**  
   “无法从通过网络的扫描线得到的裂缝间距1D相关维数估计2D和3D分形尺度参数，即使长度指数是已知的” [Moein 2019, pp. 1‑2]。
2. **两点相关函数是最优方法**  
   在1D合成数据上，两点相关函数给出的相关维数估计最稳定、最可靠 [Moein 2019, pp. 1‑2]。
3. **实际钻孔的分形特性**  
   “对三个深钻孔的观测裂缝分布应用两点相关函数显示，分布在超过两个数量级的尺度上是分形的，且分形维数在0.86 – 0.88之间” [Moein 2019, pp. 1‑2]（裂缝组也得到相似结果，细节未从索引片段中确认）。
4. **合成案例的验证**  
   - 当输入D=1.5时，生成网络的相关函数在1 – 100 m范围内斜率为1.5，符合预期 [Moein 2019, pp. 6‑7]。  
   - 长度分布的累积频率对数曲线斜率为1 – a，与Bonnet et al. (2001) 一致 [Moein 2019, pp. 6‑7]。
5. **边界效应的影响**  
   当长度指数a > 1.5时，移除伸出域外的裂缝对相关函数的影响小于a较小的情况；修剪处理在长裂缝长度上比移除方法引起的偏差更小 [Moein 2019, pp. 6‑7, 7‑9]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 无法从1D扫描线相关维数估计2D/3D相关维数 | [Moein 2019, pp. 1‑2] | 使用合成裂缝网络，已知长度指数a，基于乘法级联生成的2D/3D DFN | 结论基于体视学分析；具体数值关系未在片段中详述 |
| 两点相关函数是1D分形维数最稳定可靠的估算方法 | [Moein 2019, pp. 1‑2] | 合成1D裂缝间距数据作为基准 | 比较了盒计数、两点相关函数和幂律拟合三种方法 |
| 三个深钻孔的裂缝分布分形维数D = 0.86 – 0.88，尺度范围 > 两个数量级 | [Moein 2019, pp. 1‑2] | 巴塞尔和Soultz结晶岩钻孔，应用两点相关函数 | 裂缝组也有类似结果，但具体数值未在片段中给出 |
| 生成网络的相关函数斜率在1–100 m保持常数1.5，验证D=1.5输入 | [Moein 2019, pp. 6‑7] | 500 m域，lmin=2 m，D=1.5，a=2，α=0.3 | 密度分布和DFN实现均通过乘法级联生成 |
| 长度分布的log‑log累积频率斜率为1 – a，与理论一致 | [Moein 2019, pp. 6‑7] | 同上生成网络 | 引用Bonnet et al. (2001) |
| 边界处理对a > 1.5的DFN相关函数影响较小；修剪对长裂缝累积分布影响小于移除 | [Moein 2019, pp. 6‑7, 7‑9] | 比较a=1.5和a=2.5的实例 | 基于Darcel et al. (2003b) 以a=2为过渡区的理论 |

## Limitations
- 索引片段并未覆盖论文的完整局限性讨论。可确认的方法限制包括：乘法级联生成网络时，并非所有输出网络都能保持输入的D（尤其是Levy‑Lee生成器），本研究所用方法对D和a适用特定范围 [Moein 2019, pp. 4‑5]。
- 边界处理方式（移除/修剪）会影响DFN的统计特性，特别是在长裂缝和小a值时更为显著 [Moein 2019, pp. 6‑7]。
- 实际应用仅限于三个钻孔，且都是结晶岩环境；其通用性未在片段中确认。
- 论文中可能包含其他局限性，如模型假设、数据质量、推断到更大尺度的不确定性等，但从提供的片段中未确认。

## Assumptions / Conditions
- **双幂律模型**：裂缝网络由裂缝中心的空间分布（由相关维数D表征）和裂缝长度分布（由长度指数a表征）共同描述，两者均为幂律 [Moein 2019, pp. 3‑4]。
- **参数范围**：基于文献，2D露头观测给出的D在1.3 – 2之间，a在1.3 – 3.5之间 [Moein 2019, pp. 3‑4]；在生成和分析中，取1 < D ≤ 2（2D/3D）和a > 1 [Moein 2019, pp. 4‑5]。
- **裂缝长度有界**：裂缝长度介于lmin和lmax之间，lmax由域长度L和a决定 [Moein 2019, pp. 4‑5]；最小长度lmin用于限定迭代次数和裂缝总数。
- **乘法级联过程**：通过递归地将域细分为2×2（2D）或2×2×2（3D）子块并分配概率权重来产生分形密度分布 [Moein 2019, pp. 4‑5]。
- **长度分布分配**：使用离散逆变换方法将裂缝中心映射到概率密度图，并为每个中心独立分配符合幂律的长度 [Moein 2019, pp. 5‑6]。
- **边界效应分析**：假定无限域行为作为参考，比较完全移除伸出裂缝与修剪伸出部分两种策略 [Moein 2019, pp. 6‑7]。

## Key Variables / Parameters
- **D**：裂缝中心的空间相关维数（1 < D ≤ 2 in 2D），表征聚类程度 [Moein 2019, pp. 1, 3‑4]。
- **a**：裂缝长度的幂律指数（a > 1），控制大裂缝与小裂缝的比例 [Moein 2019, pp. 1, 3‑4]。
- **α**：裂缝密度常数，出现在长度分布公式n(l,L) dl = α·Lᴰ·l⁻ᵃ dl中 [Moein 2019, pp. 3‑4, 4‑5]。
- **lmin / lmax**：最小裂缝长度和最大裂缝长度，后者受域长和长度分布约束 [Moein 2019, pp. 4‑5]。
- **L**：域长度（2D正方形边长） [Moein 2019, pp. 4‑5]。
- **n**：乘法级联的迭代次数，由n = log₂(L/lmin) 确定 [Moein 2019, pp. 4‑5]。
- **Nt**：总裂缝数，由α、L、D和长度分布积分得到 [Moein 2019, pp. 4‑5]。
- **C(r)**：两点相关函数，用于估计相关维数D；通过对数间隔的r计算C(r)并取其局部斜率 [Moein 2019, pp. 3‑4, 6‑7]。

## Reusable Claims
1. **1D分形维数估计方法选择**：对于钻孔或扫描线上的1D裂缝间距数据，两点相关函数比盒计数法和幂律拟合更稳定和可靠，应优先使用 [Moein 2019, pp. 1‑2]。  
   *条件*：假设裂缝中心分布为分形且数据覆盖至少两个数量级。
2. **1D数据约束2D/3D网络的局限性**：即使已知长度指数a，也无法从1D扫描线/钻孔的裂缝间距相关维数唯一地估计2D或3D裂缝网络的相关维数D，因此不能将1D分形参数直接作为2D/3D DFN模型的输入约束 [Moein 2019, pp. 1‑2]。  
   *证据*：基于合成裂纹网络的体视学分析。
3. **实际深部钻孔的分形维数范围**：在巴塞尔和Soultz深部结晶岩中，裂缝间距分布的分形维数D约为0.86–0.88，且该标度关系在超过两个数量级的尺度上成立 [Moein 2019, pp. 1‑2]。  
   *限制*：仅基于三个钻孔，未从片段中确认是否适用于其他地质环境。
4. **DFN生成中的边界处理建议**：在对DFN进行建模时，若a > 1.5，直接移除伸出域外的裂缝对空间相关函数的影响不大；但当关注长裂缝的数量分布时，修剪方法比彻底移除更能保持累积长度分布的特性 [Moein 2019, pp. 6‑7, 7‑9]。
5. **乘法级联DFN的验证方法**：可通过计算裂缝中心的相关函数C(r)的log‑log斜率来验证生成网络的目标D，以及通过检查裂缝长度累积分布的log‑log斜率是否为1 – a来验证长度指数 [Moein 2019, pp. 6‑7]。

## Candidate Concepts
- [[fractal discrete fracture network (DFN)]]
- [[dual power-law model]]
- [[correlation dimension]]
- [[length exponent]]
- [[two-point correlation function]]
- [[box-counting method]]
- [[multiplicative cascade process]]
- [[stereological relationship]]
- [[borehole fracture spacing]]
- [[scale invariance]]
- [[fracture reservoir]]

## Candidate Methods
- [[Multiplicative Cascade DFN Generation]]
- [[Two-point Correlation Integral for Fractal Dimension]]
- [[Box-counting for 1D fracture patterns]]
- [[Power-law fitting of fracture size distribution]]
- [[Discrete Inverse Transform for fracture center placement]]
- [[Stereological analysis of 1D–2D–3D fracture networks]]
- [[Boundary treatment methods in DFN (remove vs. trim)]]

## Connections To Other Work
- 双幂律模型的基础框架来自Bonnet et al. (2001)，该文详细总结了裂缝网络的分形特征与测量方法 [Moein 2019, pp. 3‑4]。
- 相关维数D和长度指数a的文献参考范围引用自Bonnet et al. (2001) 和 Renshaw (1999) [Moein 2019, pp. 3‑4]。
- 边界效应分析基于Darcel et al. (2003b) 的发现，即分形DFN行为在a = 2处发生转变 [Moein 2019, pp. 6‑7]。
- 本研究与作者前期工作相关联：Afshari Moein et al. (2018a) 提出基于应力波动的裂缝网络概率成像；Afshari Moein et al. (2018b) 探讨了诱发微震活动与裂缝网络分形特性的相似性，并建立了统计模型预测最大震级 [Moein 2019, pp. 2‑3]。
- 与水力压裂/增强型地热系统(EGS)的微震b值研究存在潜在联系，提及Alghalandis et al. (2013) 的工作 [Moein 2019, pp. 2‑3]。
- 裂缝网络生成方法中的乘法级联实现参考了Harthong et al. (2012) 和 Verscheure et al. (2012) [Moein 2019, pp. 4‑5]。
- 从主题上，本文可连接到 [[fractal geometry in rock fractures]]、[[DFN model calibration]]、[[1D to 3D upscaling]] 等概念。

## Open Questions
- 在什么样的具体条件下，1D分形参数可以为3D DFN提供有限形式的约束（例如与其他信息联合反演）？索引片段未涉及。
- 论文实际部分可能探讨了裂缝组分维数的差异，但我们只见到“裂缝组也获得相似结果”的片段，具体如何定义裂缝组、是否使用了定向数据的分析尚不清楚。
- 两点相关函数在实际不完整钻孔采样情况下的鲁棒性如何？未被片段覆盖。
- 分形维数0.86–0.88这一经验范围能否用于区分不同类型的裂缝系统或应力状态？未从片段中确认。
- 边界处理在3D DFN中是否有类似效应？已知3D生成与2D类似，但片段中对3D边界效应未明确讨论。

## Source Coverage
本页面依据 **7** 个索引片段（共提供8个片段，其中片段7和8涉及边界效应和3D生成），对应于论文第1‑9页。覆盖范围集中于：
- 摘要、引言（背景与目标）
- 裂缝网络生成方法的详细描述（乘法级联）
- 2D边界效应分析
- 3D生成的初步介绍
- 实际钻孔结果的概要

**重要缺失**：未提供论文的结果章节（包括详细的分形估计结果、敏感性分析、不同裂缝组的结果）、讨论部分（例如将1D结果联系到2D/3D模型的进一步思考、实际工程意义）、结论以及可能存在的局限性讨论部分。此外，提供的片段截止于第9页，而论文共约20页，因此大部分应用和讨论内容缺失。本页面中关于“裂缝组也得到类似结果”等细节均为片段中未充分展开的部分，已标记为未确认。
