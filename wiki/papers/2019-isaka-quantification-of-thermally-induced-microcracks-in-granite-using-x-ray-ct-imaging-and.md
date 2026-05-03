---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-isaka-quantification-of-thermally-induced-microcracks-in-granite-using-x-ray-ct-imaging-and"
title: "Quantification of Thermally-Induced Microcracks in Granite Using X-Ray CT Imaging and Analysis."
status: "draft"
source_pdf: "data/papers/2019 - Quantification of thermally-induced microcracks in granite using X-ray CT imaging and analysis.pdf"
collections:
  - "zotero new"
  - "论文"
citation: "Isaka, B.L. Avanthi, et al. \"Quantification of Thermally-Induced Microcracks in Granite Using X-Ray CT Imaging and Analysis.\" *Geothermics*, vol. 81, 2019, pp. 152-167. doi:10.1016/j.geothermics.2019.04.007."
indexed_texts: "16"
indexed_chars: "76107"
nonempty_source_blocks: "16"
compiled_source_blocks: "16"
compiled_source_chars: "76470"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.00477"
coverage_status: "full-index"
source_signature: "68e487792ab9aa15cdcd85e2e553589c4c02c47d"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T03:24:08"
---

# Quantification of Thermally-Induced Microcracks in Granite Using X-Ray CT Imaging and Analysis.

## One-line Summary
利用X射线CT成像与三维重建，定量研究了Harcourt花岗岩在加热（25–1000°C）后快速水冷和缓慢炉冷条件下热诱导微裂纹的孔隙空间和网络演化，发现快速冷却导致更显著、更连通的微裂纹损伤。

## Research Question
不同加热终点温度（100–1000°C）和冷却速率（快速水淬 vs. 缓慢炉冷）如何影响花岗岩中热微裂纹的萌生阈值、空间分布、孔隙度、连通性及孔隙网络拓扑结构？

## Study Area / Data
- **岩石类型**：Harcourt花岗岩，采自澳大利亚维多利亚州Mount Alexander。
- **矿物组成（XRD）**：40%斜长石，27%石英，30%黑云母，3%其他；CT图像灰度分析亦得出黑云母约30%，石英+长石约70%。
- **物性**：粒径0.3–1.5 mm，密度2630 kg/m³，单轴抗压强度UCS=160 MPa，弹性模量17 GPa。
- **试样**：直径22.5 mm、高45 mm的圆柱体，按ASTM标准钻取。
- **热处理**：加热速率5°C/min，目标温度（100, 200, 300, 400, 600, 800, 1000°C）下恒温24 h；随后分别进行**快速冷却**（浸入22–23°C水浴）与**缓慢冷却**（随炉冷却，降温速率0.5–1°C/min）。
- **CT扫描**：澳大利亚同步加速器IMBL线站，单色X射线能量53 keV，探测器“Ruby”，分辨率9.7 μm，步长0.1°旋转。

## Methods
1. **图像获取与重建**：投影数据经CSIRO XLI CT软件重建为二维切片，再导入Avizo 9.4.0。
2. **图像预处理**：应用中值滤波去除噪声，然后使用非锐化掩膜滤器增强裂缝边界（Fig.3）。
3. **图像分割**：全局阈值化结合分水岭方法，将每个体素标记为微裂纹（黑色）、黑云母（亮区）或石英+长石（中灰区）（Fig.4）。
4. **孔隙空间定量**：
   - 交互式阈值提取孔隙体素，计算**总孔隙度** \(P = (V_{\text{pore}}/V_{\text{total}})\times100\%\)。
   - 利用**轴连接模块**（z向邻域6体素）分离连通孔隙与孤立孔隙，计算连通孔隙度。
   - **Separate Objects模块**（26邻域，标记扩展2）将连通裂纹网络分成独立团簇。
   - 孔隙度沿高度（z）和直径的分布，计算非均质性系数 \(U_z\)（变异系数）。
5. **孔隙网络模型（PNM）**：基于中轴变换/骨架化的混合算法（Avizo PNM模块），将孔隙空间缩减为中心线骨架，生成等效球（孔隙）与等效喉道网络，给出半径、频数分布及绝对渗透率模拟值。

## Key Findings
- **微裂纹演化**：无论冷却方式，**≤200°C**下无显著微裂纹（对应UCS无下降）；**300°C**时试样外缘出现微裂纹；**400°C**以上晶间裂纹沿石英、长石、黑云母晶界合并；**800°C**以上出现穿晶裂纹。黑云母裂纹较少，主为解理张开。
- **孔隙度**：总孔隙度随温度升高，且快速冷却始终高于慢冷（600°C: 3.1% vs 2.0%; 800°C: 7.7% vs 6.4%; 1000°C: 11.0% vs 7.8%）。连通孔隙占比亦快冷更高（600°C: 67.8% vs 37.8%; 1000°C: 96.9% vs 95.2%）（Table 3）。
- **非均质性**：600°C时微裂纹分布非均质性强（变异系数~20%），800°C时降至~11%，表明强烈裂纹化趋于各向同性。
- **孔隙网络**：快冷下等效孔径和喉道范围更宽（600°C快冷孔隙半径1–2000 μm，慢冷1–1000 μm；800°C快冷1–3300 μm），孔喉数量随温度增加。1000°C时虽然最大半径略降，但细孔喉数量激增，网络更密集、连通性更好（Fig.14, 16）。
- **模拟渗透率**：600°C快冷样品约0.97 D，慢冷约0.21 D（作者提示可能高估）。

## Core Evidence Table
| Evidence / 证据 | Source / 来源 | Conditions / 条件 | Notes / 注释 |
|----------------|---------------|--------------------|--------------|
| 200°C以下无可见微裂纹，UCS无变化；300°C出现边缘裂纹 | pp. 6-7, Fig.6 | 5°C/min升温+24h恒温，9.7μm分辨率 | 快冷裂纹更明显 |
| 总孔隙度数据：快冷3.1(600),7.7(800),11.0(1000); 慢冷2.0,6.4,7.8 | Table 3 [Isaka 2019, pp. 11] | CT体素计算 | 基数为% |
| 连通孔隙占比：快冷67.8→96.9%，慢冷37.8→95.2% | Table 3 | 同上 | 快冷连通性显著 |
| 非均质性系数Uz：快冷20/11/16%，慢冷21/11/12%（600/800/1000°C） | pp. 9-11, Eq.3 | 切片面积孔隙度变异系数 | 800°C非均质最低 |
| 等效孔隙半径范围：快冷600°C 1-2000 μm, 800°C 1-3300 μm；慢冷600°C 1-1000 μm | pp. 11-13, Fig.16 | PNM提取 | 快冷大孔更多 |
| 黑云母无穿晶裂纹，仅解理张开；长石/石英损伤重 | pp. 6-7, 9, Fig.10 | 至800°C/1000°C观测 | 矿物稳定性差异 |
| 模拟绝对渗透率：快冷600°C 0.97D，慢冷0.21D | p.13 | Avizo PNM | 作者指出可能高估 |

## Limitations
- CT分辨率为9.7 μm，低于此尺度的微裂纹未能捕获。
- 仅采用单一加热速率（5°C/min）和恒温24h，未讨论其他热机制的影响；热梯度被忽略（<0.3°C/mm），但未来需详细评估。
- 样品为Harcourt花岗岩单一岩性，结论推广到其他花岗岩需谨慎。
- 快速冷却为水浴淬火，慢冷为炉冷，与实际储层条件（流体对流冷却、压力等）存在差异。
- PNM渗透率模拟值可能因拓扑简化而高估，未与实测值对比。
- 分割方法（全局阈值+分水岭）仍受主观阈值选择影响。

## Assumptions / Conditions
- 矿物微裂纹主要由热膨胀系数各向异性及不匹配导致，加热时热梯度可忽略（<0.3°C/mm）。
- CT灰度值反映矿物密度和原子序数，据此进行相分离。
- 连通性分析选择6体素邻域（z向）和26邻域分离团簇。
- 试样处理为常压，无围压。
- 水浴体积足够大，水温变化可忽略。
- 恒温24 h确保试样内部温度均匀。

## Key Variables / Parameters
- **预加热温度**：100, 200, 300, 400, 600, 800, 1000°C
- **冷却方式**：快速（水淬）、缓慢（炉冷，0.5–1°C/min）
- **矿物组成**：斜长石40%，石英27%，黑云母30%；石英α–β相变573°C
- **CT参数**：53 keV，分辨率9.7 μm
- **加热速率**：5°C/min，恒温时间24 h
- **图像处理**：中值滤波、非锐化掩膜、全局阈值+分水岭
- **分析参数**：孔隙度 \(P\)、连通孔隙度、非均质性系数 \(U_z\)、相邻体素邻域6/26、标记扩展2
- **PNM参数**：中轴骨架化、等效孔/喉半径、频数分布、模拟渗透率

## Reusable Claims
- 对Harcourt花岗岩，200°C为热微裂纹的安全阈值温度（在给定加热条件下）[pp. 1-2,6-7]。
- 300°C时快速冷却已能诱发边缘微裂纹，慢冷下裂纹极微 [pp. 6-7]。
- 600°C以上总孔隙度急剧增大，与石英相变有关；快速冷却使孔隙度比慢冷高约50–80% [Table 3, p.9]。
- 连通孔隙度占比在≥800°C时无论冷速均>90%，快速冷却下600°C即达68% [Table 3]。
- 微裂纹分布非均质性随温度升高至800°C后显著降低，表明热损伤趋于各向同性 [pp. 9-11]。
- 黑云母颗粒对热冲击开裂的抗性明显强于石英和长石 [pp. 6-9]。
- 快速冷却造成的热冲击应力使孔隙网络更复杂（更宽的半径范围、更多的孔喉数量） [pp. 11-13]。
- 冷却速率是控制深部储层花岗岩热损伤程度的关键因素，快冷诱导更连通的微裂纹网络 [p.13-15]。

## Candidate Concepts
- [[thermal microcracking]]
- [[intergranular cracks]]
- [[intragranular cracks]]
- [[thermal expansion mismatch]]
- [[α–β quartz transition]]
- [[CT image segmentation]]
- [[pore network model (PNM)]]
- [[connected porosity]]
- [[heterogeneity coefficient]]
- [[thermal shock]]
- [[cooling rate effect]]

## Candidate Methods
- [[X-ray computed tomography (CT)]]
- [[3D image reconstruction]]
- [[global thresholding]]
- [[watershed segmentation]]
- [[median filter]]
- [[unsharp masking filter]]
- [[axis connectivity analysis]]
- [[separate objects module]]
- [[pore network model extraction by skeletonization]]
- [[porosity calculation from CT voxels]]

## Connections To Other Work
- 热裂纹阈值温度（本研究200°C）与Chaki et al. (2008)、David et al. (1999)等对多种花岗岩的阈值范围（80–200°C）一致。
- 晶间裂纹优先于晶内出现的现象与Gomez-Heras et al. (2019a)等的观察相符。
- 石英相变（573°C）后孔隙度剧增，支持Somerton (1992)和Chaki et al. (2008)的论断。
- 前人CT研究（Fan et al., 2018; Yang et al., 2017; Zhao et al., 2017）多关注加热后的静态损伤，本研究首次引入不同冷却速率并构建PNM。
- 与Kumari et al. (2017b, 2018)、Isaka et al. (2018)的力学实验结果形成互补，微观解释宏观强度变化。
- 热冲击理论与Richter and Simmons (1974)关于温度梯度引起微裂纹的机制吻合。
- PNM提取方法基于Dong and Blunt (2009)、Wildenschild and Sheppard (2013)等发展的技术。

## Open Questions
- PNM渗透率模拟值如何与实验室实测渗透率对应？高估程度如何？（作者计划另行发表）
- 不同加热速率及不恒温条件对微裂纹网络的具体影响。
- 施加围压条件下，热微裂纹的起裂阈值及连通性是否改变？
- 冷却介质（水、空气、CO₂等）的差异是否会产生不同的裂纹形态？
- 多次热循环（加热－冷却）产生的累积损伤模式。
- 其他花岗岩类型（矿物比例、粒间结合方式不同）是否具有相似的冷却速率敏感性？
- 实际地热储层中，热冲击引起的渗透率改造区半径如何定量评估？

## Source Coverage
所有提供的16个非空索引文本片段均已处理，覆盖全部论文内容。按文本块计覆盖率为100%，按字符计覆盖率为100.48%（编译后总字符数76,470，原始索引字符数76,107）。未引入任何来源外信息。
