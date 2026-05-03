---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2021-wei-a-smart-productivity-evaluation-method-for-shale-gas-wells-based-on-3d-fractal-fracture"
title: "A Smart Productivity Evaluation Method for Shale Gas Wells Based on 3D Fractal Fracture Network Model."
status: "draft"
source_pdf: "data/papers/2021 - A smart productivity evaluation method for shale gas wells based on 3D fractal fracture network model.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Wei, Yunsheng, et al. \"A Smart Productivity Evaluation Method for Shale Gas Wells Based on 3D Fractal Fracture Network Model.\" *Petroleum Exploration and Development*, vol. 48, no. 4, Aug. 2021, pp. 911-922. 10.1016/S1876-3804(21)60076-9. Accessed 2026."
indexed_texts: "10"
indexed_chars: "49358"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T01:59:05"
---

# A Smart Productivity Evaluation Method for Shale Gas Wells Based on 3D Fractal Fracture Network Model.

## One-line Summary
本研究提出一种集成三维分形离散裂缝网络生成、嵌入式离散裂缝流动模拟与多代理MCMC智能历史拟合的页岩气井产能评价方法 [Wei 2021, pp. 1-2]。

## Research Question
如何高效表征压裂后页岩储层中跨尺度的复杂裂缝系统（天然裂缝+人工裂缝），并在保持计算效率的同时，通过自动历史拟合反演关键参数以准确预测气井长期产能？[Wei 2021, pp. 1-2, 6-7]

## Study Area / Data
案例井为昭通地区页岩气藏的一口水平井A。该井区块天然裂缝主要为两组，中位方位角0°/180°（近南北走向），中位倾角80°，裂缝延伸长度多处于0–100 m。页岩基质孔隙度约5.5%–6.5%，原始基质渗透率约(1.0–10.0)×10⁻⁸ μm²。该井于2015年8月完成分段压裂并返排投产。模拟区域尺寸为1700 m×400 m×20 m，正交网格划分为170×40×4，模拟16段共48簇压裂 [Wei 2021, pp. 7-8]。

## Methods
- **三维分形离散裂缝网络（FDFN）生成**：采用基于乘法级联过程的算法生成天然裂缝，裂缝中心空间分布由分形维数Dc和成对校正函数控制，裂缝长度服从幂律分布；并利用等效面积法将圆盘形裂缝修正为矩形，以贴近实际形态 [Wei 2021, pp. 2-4]。算法可靠性先通过二维模型进行验证 [Wei 2021, pp. 4-5]。
- **裂缝系统耦合与流动模拟**：将生成的三维分形天然裂缝与人工压裂缝耦合，用嵌入式离散裂缝模型（EDFM）在正交网格上模拟流体流动。EDFM通过处理非相邻连接对（NNC）的传导率来刻画裂缝‑基质及裂缝间的流量交换，在保证精度的同时只需极少的裂缝网格 [Wei 2021, pp. 5-6]。
- **多相流动数学模型**：基于黑油模型，考虑气‑水两相（忽略组分传质）、气体滑脱效应、应力敏感（渗透率指数衰减）、毛管力与重力，建立压力控制方程并采用有限差分离散 [Wei 2021, pp. 5-6]。
- **智能历史拟合**：开发基于神经网络代理的多代理马尔科夫链‑蒙特卡洛（NN-MCMC）历史拟合模块。工作流包括初始化、训练神经网络代理模型、MCMC采样产生候选解、对每个匹配参数独立计算误差并利用设定阈值筛选出可接受解集，最终基于统计结果进行产能预测 [Wei 2021, pp. 7-8]。

## Key Findings
1. **分形参数可控制裂缝网络的等效流动能力**：同一组分形参数（Dc、Dl、α）虽能生成不同分布形态和几何形状的裂缝系统，但其等效渗透率和压力动态响应几乎相同，证明分形参数可在保留关键数学信息的同时提升天然裂缝的表征精度 [Wei 2021, pp. 2]。
2. **EDFM在复杂裂缝网络模拟中兼具精度与效率**：与同等尺度下的LGR和PEBI方法相比，EDFM所需的裂缝网格数最少（640 vs. 2296/1975），总计算时间最短（120 s vs. 257/185 s），且产气动态与精细网格解接近 [Wei 2021, pp. 6-7, 表3, 图7]。
3. **NN-MCMC方法可实现高效、多解的历史拟合与不确定性评估**：对昭通水平井实例，通过13个拟合参数获取了75个可接受的历史拟合解，统计得到P50参数值，并据此预测了定底流压1.5 MPa条件下20年的气水产量 [Wei 2021, pp. 8-10, 表7, 图11]。
4. **二维分形裂缝生成算法可靠，可用于支撑三维模型**：在10 m×10 m范围内生成9326条裂缝，反算得到的分形参数与输入值高度一致，验证了算法可推广至三维 [Wei 2021, pp. 4-5, 表1]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 2D分形裂缝生成验证：输入Dc=1.60, Dl=1.50, α=3.50，反算得到Dc=1.51, Dl=1.52, α=3.35，中位方位角几乎完全匹配 | [Wei 2021, pp. 4-5, 表1] | 生成区域10 m×10 m，最小缝长0.05 m | 验证了分形裂缝生成算法的可靠性 |
| EDFM、PEBI、LGR计算效率对比：EDFM总网格7440，计算120 s；PEBI总网格5817，185 s；LGR总网格9096，257 s | [Wei 2021, pp. 6-7, 表3] | 基础网格6800，201个时间步 | EDFM有效减少了裂缝网格数和计算时间 |
| 昭通水平井A历史拟合统计P50结果：有效缝高18.2 m，裂缝半长99 m，人工缝导流能力28.6×10⁻³ μm²·m，天然缝导流能力1.35×10⁻³ μm²·m，簇效率79.5% | [Wei 2021, pp. 9-10, 表7] | 基于75次可接受历史拟合解 | 采用NN-MCMC方法获得的多解统计结果 |
| 相同分形参数产生的不同几何形状裂缝网络具有几乎相同的等效渗透率与压力响应 | [Wei 2021, pp. 2] | 引用先前研究 [8-11] | 为分形参数控制裂缝网络流动能力提供理论依据 |

## Limitations
- EDFM依赖正交网格，处理超多交叉裂缝时的网格构建和适应性未在片段中详述。
- NN-MCMC历史拟合的精度受限于代理模型的训练质量和MCMC采样的搜索范围，各参数筛选阈值需人为设定，可能影响解的代表性 [Wei 2021, pp. 7-8]。
- 案例验证仅限于昭通地区一口水平井，方法的普适性未从索引片段中确认。
- 裂缝通过等效面积法简化为矩形，可能与真实裂缝形态存在偏差 [Wei 2021, pp. 3]。
- 长期产能预测仅给出定底流压(1.5 MPa)结果，未讨论变生产制度或井间干扰的影响。
- 未从索引片段中确认模型是否包含页岩气吸附/解吸等关键机理。

## Assumptions / Conditions
- **裂缝建模**：天然裂缝为离散的矩形片状（由圆盘模型修正），长度服从幂律分布，空间分布由分形维数和成对校正函数决定；二维多重信息叠加算法通常迭代7–9次，且各子区域分布概率之和不必为1 [Wei 2021, pp. 2-4]。
- **流动模拟**：气‑水两相黑油模型，忽略组分传质；考虑气体滑脱、应力敏感（渗透率随有效应力指数衰减）、毛管力与重力；正交网格下采用EDFM处理方法，虚拟裂缝网格孔隙度满足体积守恒 [Wei 2021, pp. 5-6]。
- **历史拟合**：使用神经网络代理加速MCMC，对每个匹配参数分别设定独立误差阈值来筛选解，而非总目标函数 [Wei 2021, pp. 7-8]。待拟合参数的范围由工程限制事先给定（表6）[Wei 2021, pp. 9]。

## Key Variables / Parameters
- **三维分形参数**：Dc3D (案例2.6)、Dl3D (案例3.5)、三维裂缝密度常数α (案例0.9)、最小与最大缝长 [Wei 2021, pp. 3, 7-8]。
- **裂缝属性**：天然裂缝组数(2)、中位方位角(0°/180°)、中位倾角(80°)、长度/高度比(2:1)、开度；人工裂缝有效缝高、半长、导流能力、簇效率(79.5%)、天然缝导流能力 [Wei 2021, pp. 7-8, 表4]。
- **储层与岩石物性**：基质渗透率(0.45×10⁻⁷ μm² P50)、孔隙度(6.3% P50)、岩石压缩系数(5.12×10⁻⁴ MPa⁻¹)、应力敏感系数(渗透率衰减系数0.028 MPa⁻¹)、相对渗透率曲线端点与指数 [Wei 2021, pp. 8-9, 表7]。
- **EDFM核心参数**：非相邻连接对传导率TNNC，虚拟裂缝网格孔隙度 [Wei 2021, pp. 5-6]。
- **历史拟合参数界限**：13个变量的最小/最大限制（表6）[Wei 2021, pp. 9]。

## Reusable Claims
1. **基于乘法级联过程的三维分形离散裂缝网络生成方法**：能生成具有自相似和标度不变性的天然裂缝系统，只需通过Dc、Dl、α少个分形参数即可控制裂缝的总体分布与等效流动能力。适用于压裂后页岩等非常规储层天然裂缝的简捷建模 [Wei 2021, pp. 2-4]。
   - **证据**：3D生成示例图1，2D验证中反算参数与输入一致（表1）；同一组分形参数得到的裂缝网络等效渗透率等价 [Wei 2021, pp. 2, 4-5]。
   - **限制**：需预设研究区域尺寸、最小缝长等信息；圆盘到矩形的等效修正可能造成局部几何偏差。

2. **EDFM对复杂裂缝网络的高效模拟**：通过NNC传导率代替局部网格加密，可在正交网格下用更少的裂缝网格模拟裂缝‑基质和裂缝间的流动，极大降低计算开销，且对极低基质渗透率情况无需加密网格 [Wei 2021, pp. 5-7]。
   - **证据**：与LGR和PEBI方法的基准对比，EDFM网格数少、计算时间短，日产气/累产气曲线一致性良好（表3，图7） [Wei 2021, pp. 6-7]。
   - **限制**：依赖正交网格，复杂形态时网格生成难度增加。

3. **NN-MCMC智能历史拟合可获得参数的不确定性集合**：利用神经网络代理模型搭配MCMC采样，能为每个关键参数生成一系列可接受解，避免陷于单组最优解，进而提供P50及概率产能预测 [Wei 2021, pp. 7-8, 9]。
   - **证据**：昭通井获得75个历史拟合解，P50参数列于表7，并给出20年产量预测曲线 [Wei 2021, pp. 9-10]。
   - **限制**：代理模型精度和阈值设定影响解的质量，采样次数需求可能较高。

## Candidate Concepts
- [[fractal discrete fracture network (FDFN)]]
- [[multiplicative cascade process]]
- [[embedded discrete fracture model (EDFM)]]
- [[non-neighboring connection (NNC)]]
- [[assisted history matching (AHM)]]
- [[Markov chain Monte Carlo (MCMC)]]
- [[shale gas productivity evaluation]]
- [[stress sensitivity of permeability]]
- [[power-law fracture length distribution]]

## Candidate Methods
- [[multiplicative cascade process for 3D fractal fractures]]
- [[equivalent area method for disk-to-rectangle fracture correction]]
- [[EDFM with orthogonal grids]]
- [[neural network proxy-based MCMC (NN-MCMC)]]
- [[multiple information superposition algorithm for 2D fracture distribution]]
- [[reservoir numerical simulation with black oil model]]

## Connections To Other Work
- 利用并修正了Kim等人[9]的三维分形模型（将圆盘裂缝等效为矩形） [Wei 2021, pp. 2-3]。
- 天然裂缝的自相似和标度不变性及其分形参数化控制的思想继承自[8-11]等研究 [Wei 2021, pp. 2]。
- EDFM的技术优势及NNC处理方法建立在前人工作[17-20]基础上 [Wei 2021, pp. 2, 5-6]。
- 智能历史拟合模块NN-MCMC参考了文献[25]的代理辅助MCMC框架 [Wei 2021, pp. 7]。
- 从主题上，本方法可连接到 [[fracture characterization in unconventional reservoirs]]、[[proxy-based history matching]]、[[stochastic fracture network generation]] 等领域。
- 未从索引片段中确认与其他已发表页岩气井产能评价方法的具体量化比较。

## Open Questions
- 如何从微地震、成像测井等实际数据稳定反演分形参数（Dc, Dl, α）？未从索引片段中确认。
- NN-MCMC方法对超过20个强相关拟合参数的可扩展性如何？代理模型泛化能力是否足够？
- 模型未包含吸附气解吸、多组分扩散等页岩气关键机理，引入后对历史拟合和产能预测的影响未从索引片段中确认。
- 长期产能预测中生产制度变化（变流压或变产量）以及井间干扰的影响未被讨论。
- 该方法在多口井、不同区块的应用验证情况缺失。

## Source Coverage
本页基于10条索引片段编写，覆盖了原文的摘要、3D分形裂缝生成原理、2D验证、流动模拟模型与假设、EDFM效率对比、智能历史拟合工作流以及昭通实例的应用结果。整体上覆盖了方法提出到单井验证的主要环节，但对神经网络代理的具体结构、MCMC的详细实现算法、部分数学推导以及更多性能对比细节未能从片段中获取，可能需要查阅全文。此外，关于方法在其他井或地区的推广验证信息缺失。
