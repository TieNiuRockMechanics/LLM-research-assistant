---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi"
title: "Mining-Induced Fracture Network Reconstruction and Anisotropic Mining-Enhanced Permeability Evaluation Using Fractal Theory."
status: "draft"
source_pdf: "data/papers/2025 - Mining-induced fracture network reconstruction and anisotropic mining-enhanced permeability evaluation using fractal theory.pdf"
collections:
  - "zotero new"
citation: "Zhu, Zeyu, et al. \"Mining-Induced Fracture Network Reconstruction and Anisotropic Mining-Enhanced Permeability Evaluation Using Fractal Theory.\" *Journal of Rock Mechanics and Geotechnical Engineering*, vol. 17, 2025, pp. 2256-75, https://doi.org/10.1016/j.jrmge.2024.05.039."
indexed_texts: "18"
indexed_chars: "87528"
nonempty_source_blocks: "18"
compiled_source_blocks: "18"
compiled_source_chars: "87899"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004239"
coverage_status: "full-index"
source_signature: "8bc8af3c76761d4445f0e6854a6ea12177d3350d"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T08:16:17"
---

# Mining-Induced Fracture Network Reconstruction and Anisotropic Mining-Enhanced Permeability Evaluation Using Fractal Theory.

## One-line Summary
本研究通过现场钻孔监测与统计重建，构建了不同采动距离下的三维裂缝网络，并基于分形理论建立了渗透性增强率（PER）模型，实现了对采动裂缝网络各向异性渗透性增强的定量评价。[Zhu 2025, pp. 1-2, 18-19]

## Research Question
- 如何从三维视角表征采动裂缝网络的动态演化？
- 如何建立一个综合模型，定量评估采动增强渗透性的各向异性特征？[Zhu 2025, pp. 1-2, 3]
- 采动过程中裂缝网络的渗透性增强率（PER）呈现怎样的时空演化规律？[Zhu 2025, pp. 1-2]

## Study Area / Data
- 研究地点：中国平顶山煤业集团十矿 Ji14‑31050 工作面。该工作面长 962.9 m，宽 145.6 m，煤层平均倾角 3°，厚度 0~1.3 m（平均 0.5 m）。[Zhu 2025, pp. 3]
- 现场试验布置了 8 个监测钻孔（C1~C8），因 C1、C2、C6 塌孔失效，最终获得 C3、C4、C5、C7、C8 五个钻孔的有效数据。钻孔几何参数见表 1，空间分布见图 1、2。[Zhu 2025, pp. 3-4]
- 采用 CXK12‑Z 钻孔成像仪实时记录孔壁视频，获取裂缝方位、倾角、宽度及沿孔深的分布。技术指标见表 2。[Zhu 2025, pp. 3-4]
- 同时监测了 3 号和 4 号断面的钻孔应力，反映了采动应力变化趋势。[Zhu 2025, pp. 3, 5]
- 数据示例：距工作面 67.5 m 时钻孔 C3 的裂缝参数（表 3）。[Zhu 2025, pp. 9]

## Methods
1. **现场监测与裂缝量化**  
   - 利用 CXK12‑Z 钻孔成像仪获取孔壁视频，通过 JL‑IDOI 后处理平台识别裂缝，导出裂缝的倾向、倾角、交切类型及间距。[Zhu 2025, pp. 3-4, 7]
   - 将孔壁图像向量化并二值化，采用盒计数法计算裂缝分形维数 \(D_B\)，利用投影法计算一维连通性 \(\chi\)。 [Zhu 2025, pp. 5-7]

2. **采动裂缝网络的三维统计重建**  
   - 基于 RJNS3D（Rock Mass Joint Network Simulation 3D）工具箱，采用蒙特卡洛方法重建工程尺度离散裂缝网络（DFN）。[Zhu 2025, pp. 7-8]
   - 关键步骤包括：结构均质区划分→用 Dips 软件进行裂缝方位下半球投影分组及 Fisher 分布校正→利用负指数分布拟合裂缝间距→通过空间几何关系换算线密度至体积密度→推断椭圆裂缝的尺寸分布（均值、方差）→生成三维裂缝网络模型。[Zhu 2025, pp. 7-11]
   - 假设裂缝为椭圆，尺寸服从指数分布，裂缝中心服从泊松分布。[Zhu 2025, pp. 10-11]
   - 重建模型尺寸：x 方向（平行巷道）80 m，y 方向（平行工作面）30 m，z 方向（垂直煤层厚度）20 m。[Zhu 2025, pp. 13]

3. **各向异性 PER 评价模型**  
   - 基于单裂缝立方定律，引入裂缝面分形维数 \(D_{fracture-face}\)、沿流向迂曲分形维数 \(D_T\) 和垂直流向迂曲分形维数 \(D_l\)，推导单裂缝流量方程（式 17）。[Zhu 2025, pp. 14-15]
   - 利用裂缝迹长分布的分形缩放关系（式 12~15），结合裂缝产状积分得到裂缝网络总流量（式 18），进而导出区域渗透率（式 19）。[Zhu 2025, pp. 14-15]
   - 定义渗透性增强率 \(u = d(k/k_0)/d\varepsilon_v\)，并通过二维孔隙度与体积应变的关系（式 24、25）将 PER 与可测量的分形维数联系起来。[Zhu 2025, pp. 15-16]
   - 在重建的三维裂缝网络中，取垂直于 X、Y、Z 主轴的三个截面（MW1、MW2、MW3），分别计算各截面裂缝迹线的分形维数，代入 PER 模型得到三个主方向的 PER。[Zhu 2025, pp. 16-17]

## Key Findings
1. 采动裂缝网络演化可划分为三个典型阶段：**快速生长期**、**稳定生长期**和**弱影响期**。[Zhu 2025, pp. 1, 6-7]
2. 裂缝分形维数和一维连通性在距工作面 >70 m 时增长极慢；30~70 m 时均匀增长；<30 m 时快速增长后趋于饱和。[Zhu 2025, pp. 6-7]
3. 采动增强渗透率（PER）呈现初期缓慢增长、中期快速增长、后期显著下降的演化模式。最大 PER 达到 2490.45。[Zhu 2025, pp. 17-18]
4. 采动裂缝网络的空间分形维数主要集中在 2.40~2.67 之间，随工作面推进先快速上升后略有下降。[Zhu 2025, pp. 17-18]
5. 采动增强渗透性具有强烈的各向异性：z 方向（垂直煤层厚度）的峰值 PER 是 x 方向（垂直厚度方向）的 6.86 倍，是 y 方向（平行工作面推进方向）的 4446.38 倍。[Zhu 2025, pp. 18]
6. 模型计算的渗透率演化趋势与 Adhikary 和 Guo（2015）在澳大利亚某煤矿的现场观测结果一致，验证了模型的可靠性。[Zhu 2025, pp. 18]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 采动裂缝网络可分为快速生长、稳定生长和弱影响三个阶段 | [Zhu 2025, pp. 1, 6-7] | 基于平顶山十矿 Ji14‑31050 工作面的现场钻孔监测数据 | 分形维数和连通性均呈现三阶段演化（图 8） |
| 裂缝分形维数在距工作面 <30 m 时快速上升并趋于饱和 | [Zhu 2025, pp. 6-7] | 五组有效钻孔（C3~C8）的盒计数法分形维数计算 | 未考虑微米级裂缝 |
| PER 沿工作面推进方向呈现“慢增–快增–急降”的演化序列 | [Zhu 2025, pp. 17-18] | 基于重建的三维裂缝网络和分形 PER 模型计算 | 模型以 67.5 m 状态为初始基准 |
| z 方向峰值 PER 是 x 方向的 6.86 倍，是 y 方向的 4446.38 倍 | [Zhu 2025, pp. 18] | 上述模型计算结果 | 强烈的各向异性，y 方向渗透增强极弱 |
| PER 模型计算结果与现场实测渗透率变化趋势吻合良好 | [Zhu 2025, pp. 18] | 引用 Adhikary 和 Guo（2015）的现场数据，采用相对距离归一化比较 | 仅对比演化趋势，未对比绝对值 |
| 采动影响下孔壁裂缝从随机裂缝→分离裂缝→破碎区演化 | [Zhu 2025, pp. 5] | 钻孔 CXK12‑Z 成像仪观测 | 只捕捉毫米级裂缝 |
| 采动引起的钻孔应力呈先升高后降低的变化规律 | [Zhu 2025, pp. 5] | 监测断面 3、4 的平均应力 | 与已有采动应力理论一致 |

## Limitations
- 钻孔成像仪受煤层深色影响，只能捕捉毫米级裂缝，未能考虑微米级裂缝对气体渗流的贡献。[Zhu 2025, pp. 4, 18]
- 裂缝网络重建基于蒙特卡洛方法，未考虑采矿扰动对煤层裂缝发育的力学机理，可能导致重建模型存在一定误差。[Zhu 2025, pp. 18-19]
- 重建过程假设裂缝为同一均质区内的单一组，且裂缝间距服从负指数分布，尺寸服从指数分布；这种简化可能与实际复杂地质条件存在偏差。[Zhu 2025, pp. 8-11]
- PER 模型中忽略了不同分形维数之间的定量关系以及体积应变与分形维数的耦合，仅通过二维截面分形维数等效估计三维迂曲维数，属于等效统计层次。[Zhu 2025, pp. 16-17, 18]
- 现场监测数据有限（5 个有效钻孔），样本量较小，可能影响统计参数的可靠性。[Zhu 2025, pp. 3]

## Assumptions / Conditions
- 裂缝基本形状为椭圆，同组裂缝的长短轴比（k）为常数。[Zhu 2025, pp. 10]
- 裂缝中心点服从泊松分布，一维间距分布可用负指数函数拟合。[Zhu 2025, pp. 8]
- 研究区域的裂缝岩体属于同一结构均质区，无需进行多区划分。[Zhu 2025, pp. 8]
- 裂缝尺寸分布服从指数分布（通过与实际交切数的对比验证）。[Zhu 2025, pp. 10-11]
- 宏观流体流动方向分别与 X、Y、Z 主轴一致，用对应截面的分形维数代表 PER 模型中的相关维数。[Zhu 2025, pp. 16]
- 裂缝面分形维数 \(D_{fracture-face}\) 在裂缝网络演化过程中变化可忽略。[Zhu 2025, pp. 15]
- 裂缝宽度与迹长满足线性比例关系（n=1），以保证自相似性和分形特征。[Zhu 2025, pp. 14]
- 初始状态取距工作面 67.5 m 时的裂缝网络模型。[Zhu 2025, pp. 16]

## Key Variables / Parameters
- \(D_B\)：裂缝网络盒计数分形维数 [Zhu 2025, pp. 5-6]
- \(\chi\)：沿钻孔方向的一维连通性 [Zhu 2025, pp. 5-6]
- \(l\)：一维裂缝线密度（m⁻¹） [Zhu 2025, pp. 8]
- \(l_v\)：裂缝体积密度（m⁻³） [Zhu 2025, pp. 10-12]
- \(m_a\)：椭圆裂缝平均直径 [Zhu 2025, pp. 12]
- \(\sigma^2\)：椭圆裂缝直径方差 [Zhu 2025, pp. 12]
- \(D_f\)：裂缝迹长分布的分形维数 [Zhu 2025, pp. 14]
- \(D_T\)：沿流动方向的迂曲分形维数 [Zhu 2025, pp. 15]
- \(D_l\)：垂直流动方向的迂曲分形维数 [Zhu 2025, pp. 15]
- \(l_{max}, l_{min}\)：裂缝最大/最小迹长 [Zhu 2025, pp. 14]
- \(\varepsilon_v\)：体积应变 [Zhu 2025, pp. 15]
- \(\phi\)：二维孔隙度 [Zhu 2025, pp. 15]
- \(u\) (PER)：渗透性增强率，定义为 \(d(k/k_0)/d\varepsilon_v\) [Zhu 2025, pp. 15]
- \(a, \theta\)：裂缝的平均倾向和倾角 [Zhu 2025, pp. 14]

## Reusable Claims
- **采动裂缝网络演化阶段**：采动引起的裂缝网络可划分为快速生长、稳定生长和弱影响三个阶段，对应分形维数和连通性的不同增长特征。[Zhu 2025, pp. 1, 6-7]
- **PER 演化序列**：采动增强渗透率随工作面推进呈现“缓慢增长→快速增长→显著下降”的典型规律。[Zhu 2025, pp. 1, 17-18]
- **各向异性量级**：在特定地质和开采条件下，垂直煤层方向（z）的峰值 PER 可比垂直厚度方向（x）高一个数量级（6.86 倍），比平行推进方向（y）高出三个数量级（4446.38 倍）。[Zhu 2025, pp. 18]
- **分形 PER 模型公式**：公式（23）提供了基于分形维数和体积应变的 PER 计算表达式，允许通过三维截面分形维数间接评估各向异性渗透增强。[Zhu 2025, pp. 15]
- **重建技术流程**：基于蒙特卡洛和 RJNS3D 工具箱的“现场钻孔数据→方位校正→间距拟合→尺寸推断→三维网络生成”的裂缝网络重建方法，适用于缺少露头的深部工程。[Zhu 2025, pp. 7-11]

## Candidate Concepts
- [[采动裂缝网络]]
- [[分形维数]]
- [[渗透性增强率]]
- [[各向异性渗透性]]
- [[离散裂缝网络]]
- [[盒计数法]]
- [[迂曲分形维数]]
- [[裂缝体积密度]]
- [[Fisher 分布]]
- [[负指数间距分布]]

## Candidate Methods
- [[钻孔成像技术]]
- [[RJNS3D 工具箱]]
- [[蒙特卡洛裂缝网络重建]]
- [[裂缝迹长分形标度律]]
- [[基于分形的 PER 模型]]
- [[椭圆裂缝尺寸推断法]]
- [[Dips 软件裂缝分组]]
- [[投影法计算一维连通性]]

## Connections To Other Work
- 采动裂缝分形特征研究：Xie et al. (1999), Yu et al. (2000), Gao et al. (2012, 2021), Zhang et al. (2020a), Cao and Shi (2023), Vega and Kovscek (2022)。[Zhu 2025, pp. 2]
- 煤岩渗透性实验与模型：Qi et al. (2009), Chen et al. (2016), Xue et al. (2022), Jia and Zou (2021), Wang and Chen (2020), Li et al. (2022)。[Zhu 2025, pp. 2-3]
- 裂缝网络渗透率数值模拟：Baghbanan and Jing (2008), Long and Witherspoon (1985), Miao et al. (2015a), Liu et al. (2016), Si et al. (2015), Poulsen et al. (2018), Khanal et al. (2019)。[Zhu 2025, pp. 2-3]
- 采动增强渗透性概念与模型：Xie et al. (2013, 2015), Zhang et al. (2016, 2017, 2020b), Ma et al. (2014), Xie et al. (2020)。[Zhu 2025, pp. 2-3]
- 裂缝尺寸推断与网络重建技术：Jin (2014), Gao et al. (2016), Zhang (2011a, 2011b, 2011c)。[Zhu 2025, pp. 7, 12]
- 模型验证对比：Adhikary and Guo (2015) 现场渗透率监测。[Zhu 2025, pp. 18]

## Open Questions
- 如何将微米级裂缝和基质渗透性纳入采动增强渗透率评价模型？[Zhu 2025, pp. 18]
- 如何利用微震事件等信息校正蒙特卡洛重建的裂缝网络，以提高其与实际岩体结构的吻合度？[Zhu 2025, pp. 19]
- PER 模型中多分形维数（\(D_f\), \(D_T\), \(D_l\)）与体积应变之间的定量耦合关系尚未建立，需进一步理论探索。[Zhu 2025, pp. 15]
- 模型目前仅在单一工作面验证，对不同地质条件、不同开采方法的普适性有待检验。[Zhu 2025, pp. 18]
- 如何在工程尺度上实现三维裂缝网络中流体流动的直接模拟，以验证分形等效模型的精度？[Zhu 2025, pp. 3, 15]

## Source Coverage
本文档涵盖所提供的所有 18 个非空索引片段文献来源：[Zhu 2025, pp. 1-2], [Zhu 2025, pp. 2-2], [Zhu 2025, pp. 2-3], [Zhu 2025, pp. 3-3], [Zhu 2025, pp. 3-5], [Zhu 2025, pp. 5-7], [Zhu 2025, pp. 7-7], [Zhu 2025, pp. 7-9], [Zhu 2025, pp. 9-11], [Zhu 2025, pp. 11-13], [Zhu 2025, pp. 13-14], [Zhu 2025, pp. 14-15], [Zhu 2025, pp. 15-17], [Zhu 2025, pp. 17-18], [Zhu 2025, pp. 18-19], [Zhu 2025, pp. 19-19], [Zhu 2025, pp. 19-20], [Zhu 2025, pp. 20-20]。  
- 索引文本块：18  
- 索引字符总数：87528  
- 编译后字符数：87899  
- 块覆盖率：1.0  
- 字符覆盖率：1.00424  
- 来源签名：8bc8af3c76761d4445f0e6854a6ea12177d3350d  
所有非空索引片段均已被处理并纳入本页面。
