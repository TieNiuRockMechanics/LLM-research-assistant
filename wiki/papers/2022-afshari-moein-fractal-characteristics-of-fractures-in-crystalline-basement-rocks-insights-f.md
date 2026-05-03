---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-afshari-moein-fractal-characteristics-of-fractures-in-crystalline-basement-rocks-insights-f"
title: "Fractal Characteristics of Fractures in Crystalline Basement Rocks: Insights from Depth-Dependent Correlation Analyses to 5 km Depth."
status: "draft"
source_pdf: "data/papers/2022 - Fractal characteristics of fractures in crystalline basement rocks Insights from depth-dependent correlation analyses to 5 km depth.pdf"
collections:
  - "1文章:2D-3D分形关系"
  - "2文章钻孔裂缝分形关系"
  - "3文章 裂缝网络联通渗透性"
citation: "Afshari Moein, Mohammad Javad, et al. “Fractal Characteristics of Fractures in Crystalline Basement Rocks: Insights from Depth-Dependent Correlation Analyses to 5 km Depth.” *International Journal of Rock Mechanics & Mining Sciences*, vol. 155, 2022, art. 105138. doi:10.1016/j.ijrmms.2022.105138."
indexed_texts: "17"
indexed_chars: "84921"
nonempty_source_blocks: "17"
compiled_source_blocks: "17"
compiled_source_chars: "81187"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.95603"
coverage_status: "full-index"
source_signature: "6af444634e5b12c32f1bd45247fbb6dfc64cf769"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T05:32:14"
---

# Fractal Characteristics of Fractures in Crystalline Basement Rocks: Insights from Depth-Dependent Correlation Analyses to 5 km Depth.

## One-line Summary
本研究采用归一化相关积分法分析莱茵地堑六口深钻孔（最深 5 km）裂缝的空间分布，揭示裂缝排列遵循分形标度律（分形维数 0.85–0.9），且无系统性的深度依赖性；岩心与成像测井数据的差异源于局部低维裂缝区，而非成像分辨率不足。

## Research Question
1. 应用相关积分法分析六口井的裂缝排列，判断其是否遵循幂律标度，如是，则确定分形维数及适用的尺度范围。  
2. 比较 Soultz 场地五口钻井的裂缝标度特征。  
3. 对比 Soultz 岩心记录与相邻井成像测井的标度特征。  
4. 沿数据集划分子区间进行标度分析，考察标度律随深度的平稳性。  
以上目标来自 [Afshari 2022, pp. 2-4] 中“the objects of this paper are”段

## Study Area / Data
- **研究区**：欧洲上莱茵地堑（Upper Rhine Graben）的 Soultz‑sous‑Forêts 增强型地热系统（EGS）场地（法国）和 Basel 地热项目（瑞士），两地相距约 150 km。[Afshari 2022, pp. 2-4]  
- **钻孔与数据集**：共六个深钻孔（见表），全部穿透结晶基底。Soultz 五口井：GPK1、GPK2、GPK3、GPK4（成像测井）和 EPS1（连续岩心）；Basel 一口井：BS‑1（成像测井）。成像测井主要来自超声成像（UBI，GPK2/3/4/BS‑1）和微电阻率成像（FMI，GPK1）。[Afshari 2022, pp. 4-4]  
- **数据特征**：所有数据集均包含真垂直深度（TVD）和经钻孔倾斜校正的真倾角与倾向。岩心数据集 EPS1 来自 810 m 连续岩心（1417–2227 m），包含 2997 条裂缝，宽度（aperture）信息完整，约 75% 的裂缝宽度 < 1 mm。[Afshari 2022, pp. 2-4; pp. 4-4] 成像测井难以分辨宽度 < 1–3 mm 的裂缝。[Afshari 2022, pp. 4-4]  
- **裂缝统计**（见表）：BS‑1（2600–5000 m，UBI，1164 条裂缝）；GPK1（1960–3600 m，FMI，593 条）；GPK2（1420–3800 m，UBI，1785 条）；GPK3（1420–5000 m，UBI，1926 条）；GPK4（1420–5000 m，UBI，2115 条）；EPS1（1417–2227 m，岩心，2997 条）。[Afshari 2022, pp. 4-4]  

## Methods
- **归一化相关积分（NCI）**：对每条裂缝沿钻孔的位置序列计算归一化相关积分 \(C_2(r/L) = \frac{2N_p(r/L)}{N_t(N_t-1)} = \Lambda (r/L)^{D_2}\)，其中 \(N_t\) 为裂缝总数，\(N_p(r/L)\) 为中心距小于 \(r/L\) 的裂缝对数目，\(D_2\) 为相关维（分形维数），\(\Lambda\) 为标度系数。分析在归一化区间 \(r/L = 0.001–0.1\) 内进行，边界效应（\(r/L > 0.1\)）和小尺度欠采样（\(r/L < 0.001\)）被排除。[Afshari 2022, pp. 4-5]  
- **斜率函数与合规判断**：定义局部斜率 \(\text{Local Slope} = d\{\log[C_2(r/L)]\}/d(r/L)\)。通过线性拟合得到 \(D_2\) 和 \(\Lambda\)，其标准偏差由拟合斜率的标准差给出。同时与乘性级联过程（MCP）生成的分形分布的期望斜率函数对比，判断分形行为。[Afshari 2022, pp. 5-5]  
- **深度依赖分析**：采用移动窗口法（窗口含 500 或 1000 条裂缝，50% 重叠），计算每个窗口的 \(D_2\) 和 \(\Lambda\)。通过合成数据验证，至少需要 500 条裂缝才能获得稳健的 \(D_2\) 估计。[Afshari 2022, pp. 7-8]  
- **岩心与成像测井的可比性处理**：为评价分辨率的影响，将 EPS1 岩心数据中宽度 < 1 mm 的裂缝剔除（剩余 738 条），重复 NCI 分析。[Afshari 2022, pp. 5-5]  

## Key Findings
- **分形标度的存在与范围**：五个成像测井数据集（BS‑1、GPK1/2/3/4）的 NCI 在至少两个数量级的尺度上呈线性，表明裂缝空间排列遵循分形标度律。相关维 \(D_2\) 集中在 **0.85–0.90**，标度系数 \(\Lambda\) 在 **1.49–2.3** 之间。[Afshari 2022, pp. 5-5; pp. 5-7]  
- **岩心数据与成像测井的差异**：EPS1 完整岩心数据的 \(D_2 = 0.8 \pm 0.09\)，且斜率函数偏离期望曲线，分形行为较差。剔除 < 1 mm 裂缝后，\(D_2\) 反而降至 0.71，表明差异**并非**成像测井分辨率不足所致。[Afshari 2022, pp. 5-5; pp. 11-11]  
- **局部低维区成因**：深度依赖分析显示，EPS1 在 **1750–2070 m** 深度段 \(D_2\) 显著降低（500 和 1000 裂缝窗口的最低值约 0.7），而该段以上和以下的 \(D_2\) 均值在 0.85–1.0，与成像测井一致。该区间包含一个 **130 m 几乎无裂缝的间隔**（1920–2050 m），在其他 Soultz 井中未见。因此，岩心数据的整体低 \(D_2\) 主要由这一局部结构异常区造成。[Afshari 2022, pp. 8-9; pp. 11-11]  
- **深度平稳性**：除 EPS1 的局部扰动外，所有成像测井（BS‑1、GPK2/3/4）的深度剖面均未显示 \(D_2\) 或 \(\Lambda\) 随深度的系统性变化，标度律在垂直方向具有平稳性。BS‑1 中最上部 400 m 的古风化带虽然裂缝密度极高，但其 \(D_2\) 仍与深部一致。[Afshari 2022, pp. 9-11; pp. 11-11]  
- **\(\Lambda\) 与裂缝密度的关系**：利用 MCP 合成数据（固定 \(D_2\)，不同裂缝数）发现，\(\Lambda\) 值虽然散布在 1–2.25（与天然裂缝相似），但与裂缝**密度无系统性依赖关系**。[Afshari 2022, pp. 5-7; pp. 11-12]  

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 成像测井裂缝排列的分形维数 \(D_2\) 在 **0.85–0.90**，\(\Lambda\) 在 **1.49–2.3** | [Afshari 2022, pp. 5-5; Table 2] | 基于 NCI，归一化区间 0.001–0.1；测井类型为 UBI 或 FMI；裂缝宽度可能 > 1–3 mm | 覆盖 Soultz 五口井和 Basel BS‑1；分形行为在米至数百米尺度上成立 |
| EPS1 岩心全数据 \(D_2 = 0.8 \pm 0.09\)，剔除 < 1 mm 裂缝后 \(D_2 = 0.71 \pm 0.09\) | [Afshari 2022, pp. 5-5; Table 2] | 归一化区间 0.001–0.1；岩心提供完整裂缝检测 | 全数据分形行为较差；分辨率不是差异原因 |
| EPS1 在 1750–2070 m 深度段出现低 \(D_2\)（~0.7），对应一段 130 m 几乎无裂缝的间隔 | [Afshari 2022, pp. 8-9; pp. 11-11] | 500 和 1000 裂缝滑动窗口分析；该段以上/以下 \(D_2\)≈0.85–1.0 | 局部结构异常造成岩心整体 \(D_2\) 偏低 |
| BS‑1、GPK2/3/4 的 \(D_2\) 和 \(\Lambda\) 深度剖面无系统性变化 | [Afshari 2022, pp. 9-11] | 500 裂缝滑动窗口；BS‑1 包含高密度古风化带 | 标度律平稳，与深度无关 |
| 合成数据表明，至少 **500 条裂缝** 才能得到稳健的 \(D_2\) 估计 | [Afshari 2022, pp. 7-8] | MCP 生成 1D 分形网络，\(D_2=0.75\)；100 次随机抽样 | 作为深度依赖分析的窗口大小依据 |
| \(\Lambda\) 与裂缝密度无系统性关系 | [Afshari 2022, pp. 5-7; pp. 11-12] | MCP 合成数据，固定 \(D_2\)，不同裂缝数 | \(\Lambda\) 可能受其他因素（如空隙度）控制 |

## Limitations
- **方法固有局限**：NCI 在 \(r/L > 0.1\) 时受边界效应影响，在 \(r/L < 0.001\) 时因裂缝密集区欠采样而偏离线性。因此，分形标度仅可在 **0.001–0.1** 的归一化区间内评估。[Afshari 2022, pp. 4-5]  
- **成像测井分辨率不确定性**：成像测井对裂缝的可检测性取决于工具频率、孔径、测井速度及裂缝蚀变程度等，难以给出统一的最小可识别宽度，研究采用 1–3 mm 作为粗略估计。[Afshari 2022, pp. 4-4]  
- **EPS1 岩心与成像测井的直接对比缺失**：EPS1 的成像测井数据因包含诱导缝而不可靠，故未能进行同井对比，增加了差异解释的不确定性。[Afshari 2022, pp. 4-5]  
- **局部异常可能不代表整体**：EPS1 在 1750–2070 m 的低维区可能受控于岩浆流动组构或局部古应力影，其成因尚不明，因此将该结论外推至其他地点或尺度时需谨慎。[Afshari 2022, pp. 11-11]  
- **单分形假设**：本研究假设裂缝系统为单分形，即一个分形维数足以描述其空间特征，未检验多分形谱的可能性。[Afshari 2022, pp. 4-5]  

## Assumptions / Conditions
- 裂缝系统的空间分布 **假设为单分形**，因此相关维 \(D_2\) 等同于分形维数。[Afshari 2022, pp. 4-5]  
- NCI 分析的 **有效归一化范围固定为 0.001–0.1**，并假设在该范围内分形标度律成立。[Afshari 2022, pp. 4-5]  
- 成像测井未完全采样宽度 < 1–3 mm 的裂缝，但岩心数据表明**剔除细缝不影响基本结论**。[Afshari 2022, pp. 5-5; pp. 11-11]  
- 深度依赖分析要求 **每个搜索窗口至少包含 500 条裂缝**，以保证 \(D_2\) 估计的可靠性。[Afshari 2022, pp. 7-8]  
- 研究将钻孔中识别的裂缝视为 **单一裂缝网络** 的代表，未区分主裂缝带和背景裂缝。[Afshari 2022, pp. 11-12]  

## Key Variables / Parameters
- 归一化相关积分 \(C_2(r/L)\) [Afshari 2022, pp. 4-5]  
- 相关维（分形维数）\(D_2\) – 表征空间聚集程度（0–1，值越小聚集越强）[Afshari 2022, pp. 5-7]  
- 幂律标度系数 \(\Lambda\) – 拟合线在 \(r/L = 1\) 处的截距（对数空间）[Afshari 2022, pp. 5-5]  
- 归一化距离 \(r/L\) – 裂缝中心距与系统总长度之比 [Afshari 2022, pp. 4-5]  
- 裂缝计数 \(N_t\) – 钻孔内识别的裂缝总数 [Afshari 2022, pp. 4-5]  
- 滑动窗口中的裂缝数（500 或 1000）– 用于深度依赖分析的基本单元 [Afshari 2022, pp. 7-8]  
- 裂缝密度 – 单位长度裂缝条数（m⁻¹）[Afshari 2022, pp. 7-7]  

## Reusable Claims
1. **在莱茵地堑结晶基底岩石中，基于成像测井识别的裂缝空间排列在米至数百米尺度上表现出分形标度，分形维数 \(D_2\) 集中在 0.85–0.90，且随深度无系统性变化**。条件：仅适用于成像测井（UBI/FMI）可分辨的裂缝（宽度 ⪆ 1–3 mm）；方法为归一化相关积分，分析尺度 0.001–0.1 归一化区间。来源：[Afshari 2022, pp. 5-5; pp. 9-11; Table 2]。  
2. **岩心数据提供的完整裂缝采样可导致分形维数偏低（EPS1 全数据 \(D_2 = 0.8\)），但这并非成像分辨率差异的普遍效应，而是局部深度段（1750–2070 m）裂缝聚集异常所致**。该段包含一段 130 m 几乎无裂缝的间隔，其 \(D_2\) 低至 ~0.7，而以上和以下区间 \(D_2\) 恢复至 0.85–1.0。条件：仅适用于 EPS1 孔；异常段的结构成因未明确。来源：[Afshari 2022, pp. 8-9; pp. 11-11]。  
3. **裂缝数量的增加不直接导致 \(\Lambda\) 值的变化；\(\Lambda\) 与裂缝密度之间无简单映射关系**。条件：基于 MCP 合成数据（域长 1000 m，\(D_2=0.75\)）；多次实现的 \(\Lambda\) 分布与天然数据重叠，但中位数不随密度单调移动。来源：[Afshari 2022, pp. 5-7; pp. 11-12]。  
4. **进行深度依赖的分形分析时，至少需要 500 条裂缝才能获得稳健的 \(D_2\) 估计**。条件：使用 1D 合成分形网络验证，\(D_2=0.75\)；少于 500 条时估计值的离散度急剧增大。来源：[Afshari 2022, pp. 7-8]。  
5. **单一一维裂缝数据集的标度参数（\(D_2\), \(\Lambda\)）可用于表征整个钻孔长度的裂缝空间组织，前提是数据集具有平稳性**。在所研究的莱茵地堑钻孔中，除 EPS1 的局部异常外，未见深度依赖趋势。条件：分析需覆盖全长测井段；异常段需单独识别。来源：[Afshari 2022, pp. 11-12]。  

## Candidate Concepts
[[fractal dimension]], [[correlation dimension]], [[power-law scaling]], [[normalized correlation integral]], [[discrete fracture network]], [[stationarity]], [[fracture clustering]], [[monofractal]], [[scale invariance]], [[borehole imaging log]], [[core dataset]], [[fracture intensity]], [[lacunarity]], [[multiplicative cascade process]]

## Candidate Methods
[[normalized correlation integral method]], [[slope function analysis]], [[moving window depth-dependent clustering]], [[multiplicative cascade process (MCP) for generating synthetic fractal patterns]], [[box-counting (Cantor’s Dust) comparison]], [[comparison of core and image log datasets]]

## Connections To Other Work
- 与 **Ledésert et al. (1993)** 的比较：此前用盒计数法（Cantor Dust）分析同一 EPS1 岩心，得到的分形维数（0.3–0.55）系统偏低，且发现低维区在 1800–2000 m，与本研究的结论一致；但其提出的分形维数随深度增加的趋势未得到本研究的支持。[Afshari 2022, pp. 11-11]  
- 与 **Afshari Moein et al. (2019)** 的联系：前文利用非归一化相关积分法分析 GPK3、GPK4 和 BS‑1 的裂缝，发现分形维数 0.86–0.88，并指出单个裂缝组也有分形特征（\(D_2 \approx 0.65–0.75\)）。本研究改用归一化形式以增强不同长度数据集的可比性。[Afshari 2022, pp. 2-4]  
- 与 **Du Bernard et al. (2002)** 和 **Brixel et al. (2020)** 的呼应：在单个断层损伤带中获得的 \(D_2\)（0.85–0.91 和 0.81–0.87）与本研究成像测井结果相近，暗示不同尺度、不同地质背景下裂缝空间组织的分形维数可能具有一致性。[Afshari 2022, pp. 11-12]  
- 与 **Bour et al. (2002)** 及 **Davy et al. (2010)** 的普遍标度模型的关联：本研究结果支持裂缝系统可用单分形描述，但岩心数据的局部扰动提示标度平稳性需经检验；\(\Lambda\) 的物理意义（可能与空隙度有关）仍需厘清，呼应分形—空隙度（lacunarity）的分析方向。[Afshari 2022, pp. 11-12]  
- 对 **DFN 建模**的意义：利用钻孔获得的一维分形参数（\(D_2\), \(\Lambda\)）和立体关系，可为深部岩体的三维离散裂缝网络生成提供约束，特别是在仅能依赖测井数据的情况下。[Afshari 2022, pp. 12-12]  

## Open Questions
- EPS1 在 1750–2070 m 的低维异常区的**地质成因**是什么？是否与局部岩浆流动组构或古应力影有关？（暂未确认）[Afshari 2022, pp. 11-11]  
- **\(\Lambda\) 的物理控制因素**是什么？初步排除裂缝密度后，是否与空隙度（lacunarity）、裂缝长度分布或其他网络属性相关？[Afshari 2022, pp. 11-12]  
- 分形维数是否为**多分形谱的一部分**？目前的单分形假设是否需要放松？[Afshari 2022, pp. 4-5]  
- 在 **其他地质环境**（如沉积岩、变质岩）中，裂缝空间分形维数是否具有类似的窄范围？[Afshari 2022, pp. 11-12]  
- 如何从一维分形参数**外推三维裂缝网络**的等效参数？立体关系（如 Darcel et al. 2003）的适用性在深部结晶岩中需验证。[Afshari 2022, pp. 12-12]  

## Source Coverage
All 17 non‑empty indexed fragments were compiled and processed to produce this wiki page. The source coverage by blocks is **100%** (17 out of 17), and by characters is approximately **95.6%** (81187 out of 84921 indexed characters). No facts have been invented beyond these sources.
