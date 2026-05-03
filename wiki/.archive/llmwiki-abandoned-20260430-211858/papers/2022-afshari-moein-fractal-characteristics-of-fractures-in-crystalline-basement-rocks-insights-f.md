---
type: "paper"
schema_version: "paper-v2-2026-04-28"
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
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T10:38:10"
---

# Fractal Characteristics of Fractures in Crystalline Basement Rocks: Insights from Depth-Dependent Correlation Analyses to 5 km Depth.

## One-line Summary
基于六口深钻孔（最深5 km）的一维裂缝数据集，应用归一化相关积分方法揭示结晶基底岩石中裂缝空间排列遵循分形标度律，其相关维数 D₂ 主要集中于 0.85–0.9 的窄幅范围，但来自岩心的完整裂缝数据集显示出对分形行为的偏离 [Afshari 2022, pp. 1-2]。

## Research Question
- 确定六口井中的裂缝空间排列是否符合幂律标度；若符合，求解其分形维数及适用尺度范围。
- 对比 Soultz 场地五口井之间的裂缝标度特征。
- 对比 Soultz 由岩心日志与邻近井中图像测井获得的标度特征。
- 检验沿数据集的子区间中标度律随深度的平稳性 [Afshari 2022, pp. 2-4]。

## Study Area / Data
- **研究区**：上莱茵地堑 (Upper Rhine Graben, URG)，一个新生代裂谷系统，延伸超过300 km [Afshari 2022, pp. 2-4]。
- **钻孔与数据集**：
    - **Soultz-sous-Forêts 地热场地（法国）**：五口井，包括 GPK1、GPK2、GPK3、GPK4 的图像测井数据集（深度达 5 km）和 EPS1 的连续岩心数据集（810 m），岩心数据集包含了几乎所有的裂缝，而图像测井数据集少有小于 1–3 mm 开度的裂缝 [Afshari 2022, pp. 1-2][Afshari 2022, pp. 4-5]。
    - **Basel 地热项目（瑞士）**：一口井 BS-1，深度5 km，从 2.557 km 到 5 km 使用超声钻孔成像仪 (UBI) 获取图像，识别出 1164 条天然裂缝 [Afshari 2022, pp. 4-4]。
- 所有六个数据集均包含真垂直深度 (TVD) 以及经钻孔倾角校正的裂缝真倾角和倾向 [Afshari 2022, pp. 2-4]。
- 一个出自 Soultz 的由超声电视测井获得的裂缝数据集，因被发现有诱导裂缝污染而被排除在本分析之外 [Afshari 2022, pp. 4-5]。

## Methods
- **归一化相关积分 (Normalized Correlation Integral, NCI)**：
    - 使用公式：`C₂(r/L) = 2 N_p(r/L) / [N_t(N_t - 1)] = Λ [r/L]^D₂`，其中 N_t 是裂缝总数，N_p(r/L) 是中心距小于 r/L 的裂缝对的数量，L 是域尺寸，D₂ 是相关维数，Λ 是常数 [Afshari 2022, pp. 4-5]。
    - NCI 的计算是在 0.0001–1.0 的 100 个对数分布归一化距离上进行的，每十进制有 25 个值 [Afshari 2022, pp. 5-5]。
    - 通过在五个相邻点的窗口上进行无重叠线性拟合，计算局部斜率和标度系数，每十进制产生五对值 [Afshari 2022, pp. 5-5]。
    - 报告的 D₂ 和 Λ 值是在归一化范围 0.001–0.1 内局部斜率和系数的均值；D₂ 的误差是该范围内15个局部斜率的标准差 [Afshari 2022, pp. 5-5]。
- **分形参考模型**：使用乘法级联过程 (Multiplicative Cascade Process, MCP) 生成具有任何相关维数（0到1）的单分形裂缝分布，作为评估真实数据分形符合度的参考 [Afshari 2022, pp. 5-5]。
- **深度依赖性分析**：在较短的子区间上进行标度分析，以检验标度律随深度的平稳性。在进行此项分析前，利用合成数据集评估了获得稳健 D₂ 估计所需的最小裂缝数量 [Afshari 2022, pp. 7-8]。

## Key Findings
- **分形行为与维数**：所有五个图像测井数据集（BS-1, GPK1/2/3/4）在从米级到数百米级的所有可评估尺度上，其裂缝空间排列均遵循分形行为，相关维数 D₂ 集中在 0.85–0.9 的窄幅范围内 [Afshari 2022, pp. 1-2]。
- **岩心数据的偏离**：EPS1 岩心数据集显示出对分形行为的显著偏离，其最佳拟合的相关维数 D₂ 为 0.8，略低于邻近井中图像测井获得的值。去除开度较小的裂缝后，其结果与图像测井数据一致 [Afshari 2022, pp. 1-2][Afshari 2022, pp. 5-7]。
- **分形维数与密度的关系**：合成的1D分形数据测试表明，D₂ 随裂缝数量的增加而急剧增加，直到裂缝数量达到 2000条/千米，此后估计值相对稳定。真实数据中图像测井给出的 D₂ 范围为 0.85–0.9，而高密度的岩心数据 D₂ 值为 0.8，这与合成数据中 D₂ 随 N 增加而先增后稳的趋势相符 [Afshari 2022, pp. 5-7]。
- **Λ值的控制因素**：Λ 值与裂缝密度 (fracture density) 无关，这表明它可能更多地反映了裂缝网络的其他属性 [Afshari 2022, pp. 5-7]。
- **稳健估计的条件**：要获得稳健的 D₂ 估计，需要的最小裂缝数量约为 300 条 [Afshari 2022, pp. 7-8]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 图像测井数据集的裂缝空间排列遵循分形行为，相关维数 D₂ 在 0.85–0.9 范围内。 | [Afshari 2022, pp. 1-2] | 六个深钻孔中的五个UBI图像测井数据集；归一化相关积分分析；评估尺度为米级至数百米级。 | 幂律适用范围为归一化距离 0.001–0.1。 |
| BS-1 井的 D₂ = 0.85 ± 0.04。 | [Afshari 2022, pp. 5-7] | 井段长 2600 m，平均裂缝密度 0.49 m⁻¹。 | 幂律尺度范围：2–239 m。数据来自 Table 2。 |
| GPK1 井的 D₂ = 0.89 ± 0.04。 | [Afshari 2022, pp. 5-7] | 井段长 2224 m，平均裂缝密度 0.27 m⁻¹。 | 幂律尺度范围：2–160 m。数据来自 Table 2。 |
| GPK2 井的 D₂ = 0.90 ± 0.03。 | [Afshari 2022, pp. 5-7] | 井段长 2380 m，平均裂缝密度 0.75 m⁻¹。 | 幂律尺度范围：2–236 m。数据来自 Table 2。 |
| GPK3 井的 D₂ = 0.88 ± 0.02。 | [Afshari 2022, pp. 5-7] | 井段长 3580 m，平均裂缝密度 0.53 m⁻¹。 | 幂律尺度范围：4–359 m。数据来自 Table 2。 |
| GPK4 井的 D₂ = 0.88 ± 0.05。 | [Afshari 2022, pp. 5-7] | 井段长 3580 m，平均裂缝密度 0.59 m⁻¹。 | 幂律尺度范围：4–352 m。数据来自 Table 2。 |
| EPS1 岩心数据集的 D₂ = 0.8 ± 0.09，偏离其他图像测井的窄范围。 | [Afshari 2022, pp. 5-7] | 岩心段长 810 m，平均裂缝密度 3.7 m⁻¹，包含几乎所有裂缝。 | 去除小于1–3 mm开度的裂缝后，结果与图像测井数据一致。数据来自 Table 2。 |
| 裂缝密度 (fracture density) 不影响标度系数 Λ。 | [Afshari 2022, pp. 5-7] | 合成1D分形裂缝网络的测试结果。 | 这与对 D₂ 的影响不同，D₂ 在一定程度上受裂缝数量影响。 |
| 约300个数据点足以表征跨越三个数量级的空间分布，用于估计相关维数 D₂。 | [Afshari 2022, pp. 7-8] | 通过与合成数据的敏感性分析对比得出。 | 引用自 [34] 对数据点的建议，并在此得到验证。 |

## Limitations
- 图像测井数据集的分辨率有限，无法可靠识别开度小于 1–3 mm 的裂缝，导致其裂缝集合不完整，而岩心数据集则能捕捉到这些裂缝 [Afshari 2022, pp. 1-2]。
- 一维数据集无法提取关于裂缝长度分布的信息 [Afshari 2022, pp. 2-2]。
- 存在一个不可评估的最大尺度（数百米），因为幂律范围的上限受井段长度限制 [Afshari 2022, pp. 1-2]。
- 有关深度依赖性和平稳性分析的具体结果未从索引片段中确认。

## Assumptions / Conditions
- 假设裂缝空间分布可以用分形理论描述，即其相关积分在双对数坐标上遵循直线关系 [Afshari 2022, pp. 2-2]。
- 分析基于一维钻孔数据，将裂缝位置视为点过程。
- 假设归一化相关积分方法能实现不同长度数据集之间的直接比较 [Afshari 2022, pp. 2-4][Afshari 2022, pp. 4-5]。
- MCP 模型作为零假设模型，用于评估实际数据在归一化范围 0.001–0.1 内符合单分形行为的程度 [Afshari 2022, pp. 5-5]。

## Key Variables / Parameters
- **D₂**：相关维数（Correlation Dimension），表征裂缝空间分布的聚类程度。D₂ 值越低，聚类程度越高；D₂ 为1或接近1表示空间分布可由泊松过程模拟 [Afshari 2022, pp. 5-7]。
- **Λ (Lambda)**：标度系数（Scaling Coefficient），幂律拟合线的偏移量 [Afshari 2022, pp. 5-7]。
- **N_t**：裂缝总数 [Afshari 2022, pp. 4-5]。
- **L**：域尺寸（如钻孔段长度） [Afshari 2022, pp. 4-5]。
- **r/L**：归一化距离 [Afshari 2022, pp. 4-5]。
- **C₂(r/L)**：归一化相关积分 [Afshari 2022, pp. 4-5]。
- **fracture density**：裂缝密度（每米裂缝数），影响 D₂ 的估计，尤其当裂缝总数较少时 [Afshari 2022, pp. 5-7]。
- **fracture aperture**：裂缝开度，图像测井的识别下限（1-3 mm）是导致岩心和图像数据集结果差异的关键因素 [Afshari 2022, pp. 1-2]。

## Reusable Claims
### Claim 1:
- **Claim**：在结晶基底岩石中，当使用分辨率有限（难以识别<1–3 mm开度裂缝）的图像测井时，裂缝的空间分布呈现相关系数 D₂ 在 0.85–0.9 之间的单分形行为，该行为在米级至数百米级尺度均成立。
- **Conditions**: 上莱茵地堑的花岗岩基底；钻孔深度达5 km；使用归一化相关积分法分析超声波钻孔电视 (UBI) 衍生的裂缝位置数据。
- **Evidence**: 五口井（BS-1, GPK1/2/3/4）的分析结果，所有 D₂ 值均在此窄幅范围内 [Afshari 2022, pp. 1-2][Afshari 2022, pp. 5-7]。
- **Caveats**: 这仅限于无法识别微小裂缝的数据集；分形行为的最大尺度受限于钻孔长度。

### Claim 2:
- **Claim**：当纳入微小裂缝（开度<1–3 mm）时，裂缝网络会偏离上述分形行为，表现为 D₂ 值降低（如降至 0.8），这表明微小裂缝的加入改变了整体网络的空间聚类特征。
- **Conditions**: 对比来自同一场地（Soultz）的完整岩心数据和有限分辨率的图像测井数据。
- **Evidence**: EPS1 岩心数据的 D₂ = 0.8 ± 0.09，去除此类小裂缝后结果与图像测井一致 [Afshari 2022, pp. 1-2]。
- **Caveats**: 岩心数据仅有 810 m 长，其密度远高于其他图像测井数据，这可能也影响了 D₂ 的估计 [Afshari 2022, pp. 5-7]。

### Claim 3:
- **Claim**：为了对裂缝空间分布的 D₂ 进行稳健估计，数据集需要包含至少 300 个数据点。
- **Conditions**: 使用归一化相关积分法。
- **Evidence**: 基于合成数据的敏感性分析，验证了现有文献中的提议 [Afshari 2022, pp. 7-8]。
- **Caveats**: 此阈值是基于单分形 D₂=0.75 的合成数据测试得出。

## Candidate Concepts
- [[fractal dimension (D₂)]]
- [[power-law scaling]]
- [[fracture network characterization]]
- [[borehole image log]]
- [[Normalized Correlation Integral (NCI)]]
- [[Multiplicative Cascade Process (MCP)]]
- [[fracture density]]
- [[spatial distribution of fractures]]
- [[crystalline basement rocks]]
- [[Enhanced Geothermal System (EGS)]]

## Candidate Methods
- [[Normalized Correlation Integral analysis]]
- [[Multiplicative Cascade Process (MCP) for fractal generation]]
- [[1D fractal analysis of borehole data]]
- [[sensitivity analysis with synthetic fracture networks]]

## Connections To Other Work
- **方法对比**：本研究采用的归一化相关积分法被认为是对先前用于一维裂缝数据的间距频率分布法的改进，因为后者被发现即使在合成分形数据集上也可能不稳定 [Afshari 2022, pp. 2-2]。相关方法可连接到 [[box-counting method]] 和 [[power-law fitting to spacing data]]。
- **D₂ 下限与裂缝强度**：文中引用了文献 [35] 提出的观点，即标度系数 Λ 与裂缝强度有关。然而，本研究通过合成数据测试发现，Λ 与裂缝密度（1D强度）无关 [Afshari 2022, pp. 5-7]。可连接到关于 [[relationship between Λ and fracture intensity]] 的讨论。
- **最小数据量要求**：文中评估了文献 [34] 提出的需要 300 个数据点以表征空间分布的建议，并通过合成数据验证了这一阈值对估计 D₂ 的有效性 [Afshari 2022, pp. 7-8]。可连接到关于 [[sample size requirements for fractal analysis]] 的研究。

## Open Questions
- 岩心与图像测井数据的 D₂ 差异是单纯由开度识别下限造成的，还是也受到数据集长度和数据采集方式（连续岩心 vs. 不连续测井）差异的影响？未从索引片段中确认。
- 文中提及要对数据集子区间进行标度分析以检验深度平稳性，该部分的具体结果未从索引片段中确认。
- 在地下工程应用中，如何将 D₂ 和 Λ 值直接映射到对流体流动至关重要的裂缝网络联通性和渗透性参数？未从索引片段中确认。

## Source Coverage
本页依据论文《Fractal Characteristics of Fractures in Crystalline Basement Rocks》的 17 个索引片段生成。内容覆盖了摘要、引言、研究区与方法、关键结果及参数控制分析部分。部分信息可能缺失，尤其是关于标度律随深度的平稳性分析结果。
