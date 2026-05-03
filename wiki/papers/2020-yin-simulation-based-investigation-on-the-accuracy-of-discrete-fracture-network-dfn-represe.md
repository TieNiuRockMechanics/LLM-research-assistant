---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-yin-simulation-based-investigation-on-the-accuracy-of-discrete-fracture-network-dfn-represe"
title: "Simulation-Based Investigation on the Accuracy of Discrete Fracture Network (DFN) Representation."
status: "draft"
source_pdf: "data/papers/2020 - Simulation-based investigation on the accuracy of discrete fracture network (DFN) representation.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Yin, Tingchang, and Qingfa Chen. \"Simulation-Based Investigation on the Accuracy of Discrete Fracture Network (DFN) Representation.\" *Computers and Geotechnics*, 2020, doi:10.1016/j.compgeo.2020.103487."
indexed_texts: "13"
indexed_chars: "62121"
nonempty_source_blocks: "13"
compiled_source_blocks: "13"
compiled_source_chars: "62348"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.003654"
coverage_status: "full-index"
source_signature: "284f3092d63a150693d2c3b8e85918db82d941d5"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T03:34:50"
---

# Simulation-Based Investigation on the Accuracy of Discrete Fracture Network (DFN) Representation.

## One-line Summary
基于采样窗口数据采集过程模拟，通过比较原始离散裂隙网络（ODFN）与二次构建的SCDFN模型，评估DFN表征技术的精度，结果表明DFN在结构特征再现上具有较强稳健性，但在工程力学应用时需注意少数模型可能产生超过30%的力学参数偏差。[Yin 2020, pp. 1-1, 12-13]

## Research Question
在实际工程中，DFN模型的校准与验证依赖于从二维露头获取的裂隙数据与模型切片之间的对比，该过程不可避免地引入偏差。本研究旨在回答：**目前的DFN表征技术（通过二维采样窗口获取数据，构建三维模型）能否准确反映原位岩体的真实裂隙系统，尤其在几何与力学性质上可能产生多大程度的偏离？** [Yin 2020, pp. 1-1, 1-2]

## Study Area / Data
- **研究地点**: 广西铜坑锌多金属矿（TZP Mine）№.3号矿块，距南丹县城约46 km。[Yin 2020, pp. 2-2]
- **地质背景**: 出露泥盆系和石炭系地层，发育北西向大厂断裂和北东向黑水沟断裂，主岩为泥灰岩、钙质泥灰岩和页岩。[Yin 2020, pp. 2-2]
- **工程数据**: 205和355中段的8段巷道（露头），剖面约3.4 m×2.2 m，巷道交叉布置以减少方向偏差。[Yin 2020, pp. 2-2, 2-3]
- **裂隙数据**: 三组优势裂隙组（优势产状约281°/88°、37°/48°、189°/71°），间距0.2–10 m，迹长0.5–4 m，壁面光滑至平面状。统计检验表明该区域裂隙分布统计均质（p>0.05）。[Yin 2020, pp. 2-2, 2-3, 3-3]
- **岩石力学参数**: 完整岩石单轴抗压强度UCS≈104 MPa，抗拉强度σₜ≈4.7 MPa，杨氏模量E=5.57e10 Pa，泊松比μ=0.14，黏聚力C=1.66e7 Pa，摩擦角φᵣ=51.34°。[Yin 2020, pp. 2-2, 7-8]
- **DFN输入参数**: 见表1，三组裂隙尺寸分布为正态或对数正态，平均裂隙半径约1.5 m，体密度0.03–0.04 m⁻³。[Yin 2020, pp. 4-4, 4-5]

## Methods
1. **建立原始DFN（ODFN）模型**: 基于真实裂隙数据，利用3DEC生成DFN模型，并通过二维切片与现场裂隙映射对比（P20、P21）进行视觉和参数验证。[Yin 2020, pp. 3-4]
2. **虚拟采样窗口设置**: 在ODFN模型中设置固定位置（中心(0,0,0)）和尺寸（高27 m×宽40 m）的矩形垂直窗口，通过旋转ODFN模型（△α/△β）改变窗口相对方位，模拟不同方向的采样。[Yin 2020, pp. 3-4, 3-5]
3. **裂隙数据采集**: 利用3DEC的Fish语言编程提取与窗口相交的裂隙信息，包括视倾角、迹长、倾向/倾角、位置等。[Yin 2020, pp. 4-4]
4. **数据处理（以窗口120°/60°为例）**:
   - **裂隙组识别**: 使用FractureGrouping，结合Fisher分布拟合。[Yin 2020, pp. 4-5]
   - **真实平均迹长估计**: 采用Kulatilake简化方法，根据N0、N1、N2的占比选择式(2)或(3a-c)，假设迹中心均匀分布。[Yin 2020, pp. 5-6, 6-7]
   - **裂隙直径分布估计**: 假设COVₗ=COVₘ，利用极大似然估计和K-S检验确定最优分布，再通过Mauldon的方法反算直径均值μD和标准差σD。[Yin 2020, pp. 6-6, 6-7]
   - **体密度估计**: 先用Mauldon方法计算面密度λₐ（式5），再结合E(D)和E(sinφ)求体密度λᵥ（式6）。[Yin 2020, pp. 6-6, 6-7]
5. **SCDFN模型构建与验证**: 基于估算的参数，采用试错法调整输入参数，使得SCDFN模型切片与ODFN窗口的裂隙迹线形态相似，且P20、P21值接近；最后通过逆旋转恢复真实裂隙方位。[Yin 2020, pp. 6-7, 7-7]
6. **代表体积元（REV）确定**: 仅对ODFN进行，通过5个位置、尺寸递增（2.5–50 m）的DFN模型，以P30、P32确定几何REV；以ER和UCSR确定力学REV；综合取唯一REV=30 m。[Yin 2020, pp. 7-7, 9-10, 10-10]
7. **力学参数计算**: 构建DFN-DEM混合模型（3DEC），采用Mohr-Coulomb准则和Coulomb滑移，通过虚设节理模拟有限尺寸裂隙，数值单轴压缩试验获得岩石质量的ER和UCSR。[Yin 2020, pp. 7-9, 9-10]
8. **对比分析**: 对42个不同窗口方向（7个倾角×6个倾向）的SCDFN（或SCDFN-DEM）模型，计算P30、P32、ER、UCSR，并与ODFN进行相对误差（R.E.）比较。[Yin 2020, pp. 10-11, 11-12]

## Key Findings
1. **几何性质波动较小**: 42个SCDFN模型的P30和P32变异系数分别为7.44%和6.49%，均值与ODFN接近，R.E.值全部低于30%，多数低于15%。[Yin 2020, pp. 11-11, 11-12]
2. **力学性质波动较大**: ER和UCSR的变异系数分别为12.90%和16.21%，少数模型R.E.接近或超过30%，但多数仍低于30%，均值与ODFN相近。[Yin 2020, pp. 11-11, 11-12]
3. **结构表征稳健性**: DFN技术在刻画岩体裂隙图案方面具有相当的稳健性，尽管采样窗口方向不同，仍能较好地再现结构特征。[Yin 2020, pp. 12-12]
4. **偏差放大效应**: 几何参数的微小差异可引起力学参数的较大偏差（“多米诺骨牌效应”），因此在工程力学分析中需格外谨慎。[Yin 2020, pp. 12-12]
5. **方向影响不显著**: 对于裂隙系统相对随机的岩体（如研究区），窗口方向变化对DFN技术再现结构特征的能力影响可忽略。[Yin 2020, pp. 12-12]
6. **采样偏差仍然存在**: 尽管窗口较大，所获样品能够反映主要分布特征，但裂隙组平均产状的识别仍存在偏差，某些高倾角组的倾向可能偏差达180°。[Yin 2020, pp. 11-11, 12-12]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| P30变异系数7.44%，P32变异系数6.49% | [Yin 2020, pp. 11-11] | 42个不同窗口方向的SCDFN模型，尺寸30 m | 指示结构密度再现的稳定性 |
| ER变异系数12.90%，UCSR变异系数16.21% | [Yin 2020, pp. 11-11] | 同上，基于DFN-DEM模型计算 | 力学参数灵敏度更高 |
| 全部几何参数R.E.<30%，多数<15%；少数力学参数R.E.接近或超过30% | [Yin 2020, pp. 11-12] | 相对误差(ODFN为基准) | 几何表征精确，力学表征偶有失准 |
| 裂隙组平均产状识别可出现180°偏差 | [Yin 2020, pp. 11-11] | 特定窗口方向，高倾角组 | 方向偏差是显著的采样局限 |
| P20、P21 trace graph对比高度吻合 | [Yin 2020, pp. 6-7, 10-11, Fig. 17] | 42个SCDFN模型切片相对于采样窗口 | 验证了模型重建的可靠性 |
| ODFN REV: P30=20 m, P32=10 m, ER=30 m, UCSR=20 m, 统一取30 m | [Yin 2020, pp. 9-10, 10-10] | 单轴压缩数值试验，尺寸2.5–50 m | REV取值保守，保证参数代表性 |

## Limitations
- 仅评估了少数几何（P30、P32）和力学（ER、UCSR）参数，不足以全面表征天然裂隙网络的复杂性，如渗透率、连通性等未被考虑。[Yin 2020, pp. 12-13]
- 平均迹长估计在某些窗口下可能不准确（如N2接近N时式(2)失效，需依托Chen et al.的建议处理）。[Yin 2020, pp. 5-6, 6-7]
- SCDFN生成基于二维窗口数据，固有的方向、尺寸、截断和截尾偏差无法完全消除。[Yin 2020, pp. 12-13]
- 数值试验中，当DFN-DEM模型尺寸超过20 m时计算非常耗时且网格生成常失败，故采用Kulatilake等的子模型方法，可能引入额外假定。[Yin 2020, pp. 9-10]
- 假设所有裂隙面为圆盘形，若天然裂隙形状偏离圆盘（如多边形），则文中关于直径分布估计和面积计算的方法需重新评估。[Yin 2020, pp. 13-13]

## Assumptions / Conditions
- 裂隙面为圆盘形，这是估算真实迹长和直径分布的基础假设。[Yin 2020, pp. 2-2, 13-13]
- 迹线中心在垂直窗口内随机均匀分布，用于Kulatilake方法。[Yin 2020, pp. 1-2, 5-5]
- 裂隙产状服从Fisher分布。[Yin 2020, pp. 4-5, 4-6]
- 真实迹长变异系数COVₗ等于测量迹长变异系数COVₘ，用于反推裂隙直径分布。[Yin 2020, pp. 6-6]
- 岩体力学行为遵循Mohr-Coulomb塑性模型和Coulomb滑移模型，且有限尺寸裂隙通过虚设节理处理，虚设节理强度等于完整岩石强度。[Yin 2020, pp. 7-8, 9-9]
- 研究区裂隙网络统计均质，结构域划分有效（p>0.05）。[Yin 2020, pp. 2-3]
- 采样窗口垂直固定，通过旋转ODFN模型改变窗口相对于裂隙网络的方向。[Yin 2020, pp. 3-5]

## Key Variables / Parameters
- **几何变量**: P30（单位体积裂隙条数，m⁻³），P32（单位体积裂隙面积，m²/m³），P20（单位面积裂隙条数，m⁻²），P21（单位面积裂隙长度，m/m²），λᵥ（体密度），μₗ（真实平均迹长），μₘ（测量平均迹长），COVₗ，COVₘ，μD（裂隙直径均值），σD（标准差），Fisher常数κ。[Yin 2020, pp. 1-1, 4-4, 4-6, 5-6, 6-6, 6-7]
- **力学变量**: ER（岩体杨氏模量，Pa），UCSR（岩体单轴抗压强度，Pa）；完整岩石: UCS, σₜ, E, μ, C, φᵣ；裂隙: JKN, JKS, Cf, φf；虚设节理: JKN1, JKS1, Cf1, φf1, σtf1。[Yin 2020, pp. 7-8, 9-9, 9-10]
- **模型变量**: △α/△β（ODFN绕中心旋转角），窗口尺寸（w=40 m, h=27 m），DFN模型域（60 m×100 m×50 m），REV尺寸（30 m）。[Yin 2020, pp. 3-5, 4-5, 10-10]

## Reusable Claims
1. **DFN结构表征精度**: 对于随机裂隙为主的岩体，DFN技术能够高保真再现三维结构特征，P30和P32的相对误差通常<30%，且变异系数低于10%。[Yin 2020, pp. 11-11, 12-12]（条件：裂隙网络相对随机、采样窗口足够大、数据处理时进行严谨的偏差校正。）
2. **DFN力学预测偏差**: 即便几何参数高度一致，DFN模型导出的力学参数ER和UCSR仍可能出现超过30%的偏差，说明结构上的微小差异可通过“多米诺骨牌效应”放大，在工程安全分析中需增加安全裕度。[Yin 2020, pp. 12-12]（条件：采用3DEC DFN-DEM方法，有充分验证。）
3. **采样窗口方向影响**: 对于非层状、非柱状节理、非稀疏裂隙的岩体，采样窗口方向对DFN最终结构表征的稳健性影响较小，但产状识别仍可能出现偏差（如高倾角组倾向180°误差）。[Yin 2020, pp. 12-12, 11-11]（条件：统计均质域内，裂隙分布相对杂乱。）
4. **迹长估计简化方法适用性**: 当N0/N和N1/N满足相应条件时，采用Kulatilake简化公式(2)、(3a-c)可有效估计真实平均迹长，但必须注意N2接近N时的失效情形（宜采用Chen et al.的修正）。[Yin 2020, pp. 5-6, 6-7]（条件：垂直矩形窗口，迹中点均匀分布假设。）
5. **Mauldon密度估计**: 通过N1和N2可直接计算面密度λₐ，再结合E(D)和E(sinφ)可实现体密度的转换，适用于采样窗口迹线观测数据。[Yin 2020, pp. 6-7]（条件：窗口内裂隙迹线可见性良好。）

## Candidate Concepts
- [[离散裂隙网络 (DFN)]]
- [[统计均质结构域]]
- [[圆盘形裂隙假设]]
- [[Fisher分布]]
- [[采样偏差 (方向偏差/尺寸偏差/截断偏差/截尾偏差)]]
- [[迹线中点均匀分布假设]]
- [[代表体积元 (REV)]]
- [[虚设节理 (Fictitious Joint)]]
- [[多米诺骨牌效应 (结构对力学影响的放大效应)]]
- [[二维采样窗口]]
- [[3DEC软件]]
- [[P20/P21/P30/P32密度指标]]
- [[Kolmogorov-Smirnov检验]]
- [[极大似然估计]]

## Candidate Methods
- [[Kulatilake垂直矩形窗口迹长估计法]]
- [[Mauldon裂隙面密度及体密度估计法]]
- [[基于迹长数据的裂隙直径分布反算方法 (Mauldon 1998)]]
- [[3DEC DFN-DEM混合建模技术]]
- [[基于旋转矩阵的裂隙网络定向虚拟采样]]
- [[采样窗口试错法校准与验证DFN模型]]
- [[递增尺寸模型确定REV (几何+力学)]]
- [[Fisher常数最大似然估计及聚类分析]]
- [[Kulatilake等子模型法解决大规模DFN-DEM计算问题]]

## Connections To Other Work
- **裂隙产状分布**: 已有研究认为裂隙产状近似服从Fisher分布 [Yin 2020, pp. 4-5]，前人如Kulatilake、Zheng等使用类似处理。
- **迹长估计**: Kulatilake PHSU，Wu TH (1984) 提出的垂直窗口估计平均迹长方法是本研究核心，其简化形式参考 Wu & Kulatilake (2011) [Yin 2020, pp. 5-6, 14-14]。
- **密度估计**: Mauldon M (1998) 提出的面密度与体密度关系式 [Yin 2020, pp. 6-7]。
- **裂隙直径分布反演**: 采用Mauldon (1998) 的方法，并参考Han et al. (2016) 的最大似然估计和K-S检验确定最优分布 [Yin 2020, pp. 6-7, 14-14]。
- **DFN验证方法**: 常用切片与现场迹线图对比，如Wang et al. (2004), Bandpey et al. (2018) [Yin 2020, pp. 2-2, 14-14]。
- **裂隙不连续性持久度**: Shang et al. (2018) 研究了地质不连续面的持久性量化，强调了现场观察与推测的复杂性 [Yin 2020, pp. 14-14]。
- **裂隙分形特征**: Bonnet et al. (2001), Galindo-Torres et al. (2015) 讨论了裂隙网络的分形标度与连通性 [Yin 2020, pp. 14-14]。
- **岩体分类与REV**: Bieniawski (1989), Palmstrom (2005), Wu & Kulatilake (2012) 等工作关联岩体结构评级与REV [Yin 2020, pp. 14-14]。
- **3DEC数值模型**: Itasca (2013), Laghaei et al. (2018) 等采用DFN-DEM模拟节理岩体行为 [Yin 2020, pp. 14-14]。

## Open Questions
- 本研究仅用P30、P32、ER、UCSR四个指标，其他关键参数如渗透率、裂隙连通度、剪切强度各向异性等如何受DFN表征精度影响？须进一步研究。[Yin 2020, pp. 12-13]
- 研究假设裂隙面为圆盘形，若真实形状为多边形或其他不规则形态，当前的直径分布估计和体积密度换算方法需如何修正？[Yin 2020, pp. 13-13]
- 针对少数SCDFN模型出现力学性质R.E. >30%的情况，是否存在系统性原因（如特定窗口方向或裂隙组），能否通过改进采样策略或数据融合降低此类偏差？
- 当前REV仅基于ODFN确定，对于不同SCDFN模型，REV是否存在差异？采用统一REV评价所有模型是否掩盖了局部非均质影响？
- 文中数值试验当尺寸大于20 m时计算困难，采用子模型近似；若采用更高效的计算方法或更大规模的并行计算，能否获得更精确的力学REV，从而提升结论普适性？

## Source Coverage
All 13 non-empty indexed source blocks (covering 62,121 indexed characters) were processed in a single pass. The coverage ratio by blocks is 1.0, and by characters is 1.003654 (compiled characters: 62,348). The source signature is `284f3092d63a150693d2c3b8e85918db82d941d5`. No indexed content was omitted.
