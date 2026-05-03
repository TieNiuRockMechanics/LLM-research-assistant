---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2009-kim-estimation-of-fracture-porosity-of-naturally-fractured-reservoirs-with-no-matrix-porosi"
title: "Estimation of Fracture Porosity of Naturally Fractured Reservoirs With No Matrix Porosity Using Fractal Discrete Fracture Networks."
status: "draft"
source_pdf: "data/papers/2009 - Estimation of Fracture Porosity of Naturally Fractured Reservoirs With No Matrix Porosity Using Fractal Discrete Fracture Networks.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Kim, Tae H., and David S. Schechter. \"Estimation of Fracture Porosity of Naturally Fractured Reservoirs With No Matrix Porosity Using Fractal Discrete Fracture Networks.\""
indexed_texts: "10"
indexed_chars: "46461"
nonempty_source_blocks: "10"
compiled_source_blocks: "10"
compiled_source_chars: "46738"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.005962"
coverage_status: "full-index"
source_signature: "525268d5f9814159c2668edb1b7f66a457c849e4"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T13:38:18"
---

# Estimation of Fracture Porosity of Naturally Fractured Reservoirs With No Matrix Porosity Using Fractal Discrete Fracture Networks.

## One-line Summary
本文开发了基于分形离散裂缝网络（FDFN）的生成算法，用于估算基质孔隙度可忽略的I型天然裂缝性储层的裂缝孔隙度。通过乘法级联裂缝中心生成与自仿射开度分布模拟，使网络更接近真实裂缝系统，并利用2D与3D代码结合高效获取孔隙度分形维数与绝对量。

## Research Question
如何在无基质孔隙度的天然裂缝性储层中，利用考虑尺度相关分形几何和粗糙开度分布的离散裂缝网络可靠地估算裂缝孔隙度？

## Study Area / Data
- **类比露头**：美国怀俄明州Bridger Gap露头图（Harstad 1995），调查域约40 m×40 m [Kim unknown-year, pp. 9-9]。
- **开度数据参考**：Spraberry Trend Area岩心人工裂缝的CT扫描结果（Kim and Schechter 2006）[Kim unknown-year, pp. 5-6 footnote]；以及实验室测量（Pyrak‑Nolte et al. 1987; Keller 1996; Bertel et al. 2001; Muralidharan et al. 2004）与成像测井数据（Luthi and Souhaite 1990）[Kim unknown-year, pp. 1-1]。

## Methods
1. **FDFN生成理论基础**  
   - 采用一阶分形模型：裂缝中心分布分形维数 **Dc**，长度分布分形维数 **Dl**，密度项 **a** 不随尺度变化（Davy et al. 1990; Bour et al. 2002）[Kim unknown-year, pp. 1-2]。  
   - 裂缝中心生成：**乘法级联过程**（multiplicative cascade），复制自然裂缝的聚集特性（Darcel et al. 2003; Dreuzy et al. 2004）[Kim unknown-year, pp. 2-2]。  
   - 裂缝方位：服从 **Fisher分布**，由平均方向和Fisher常数K控制（Priest 1993）[Kim unknown-year, pp. 2-2]。  
   - 裂缝开度：每条裂缝用自仿射分形（fBm）描述，通过**修正连续随机加法**（corrected SRA）生成，参数为Hurst指数H和振幅A（Saupe 1988; Liu et al. 2004）[Kim unknown-year, pp. 2-3]。  

2. **代码验证**  
   - 自我一致性：生成网络的Dc、Dl、a与输入一致；方位Fisher常数匹配 [Kim unknown-year, pp. 3-3]。  
   - 理论模型对比：  
     * 中心间距‑长度幂律关系 \(d(l)\propto l^{D_l/D_c}\)（Bour et al. 2002）：33个2D FDFN最大误差<14% [Kim unknown-year, pp. 3-4]。  
     * 裂缝孔隙度标度律 \(\phi_f(L)=\phi_{f0}\left(\frac{L}{L_0}\right)^{D_{fp}-E}\)（Chang and Yortsos 1990）：2D和3D生成均吻合 [Kim unknown-year, pp. 4-4, 6-7]。  

3. **高效孔隙度估算两步法**  
   - 第一步：用 **2D FDFN** 估算分形维数 \(D_{fp}\)（2D与3D结果几乎一致）[Kim unknown-year, pp. 7-8]。  
   - 第二步：用 **3D FDFN** 估算参考域孔隙度 \(\phi_{f0}\)，再利用标度律扩展到任意域尺寸 [Kim unknown-year, pp. 8-8]。  

4. **现场应用**：Bridger Gap露头  
   - 提取裂缝中心坐标、方位组数及Fisher常数、长度分布和密度项a [Kim unknown-year, pp. 9-9]。  
   - 生成FDFN几何后，结合实测H和A为每条裂缝赋予分形开度分布 [Kim unknown-year, pp. 9-10]。

## Key Findings
1. FDFN生成码产生的网络与未参与生成的理论模型（中心距‑长度幂律、孔隙度标度律）高度吻合，验证了算法的可靠性 [Kim unknown-year, pp. 3-4, 6-7]。  
2. 裂缝孔隙度具有分形特征：**Dfp随Dc增加而减小**（密度增大，大尺度孔隙度相对提升），**随Dl增加而减小**（短裂缝增多导致孔隙度降低）[Kim unknown-year, pp. 4-4, 6-7]。  
3. **2D和3D FDFN估计的Dfp基本相同**，2D代码运行速度更快，因此更适合估算分形维数 [Kim unknown-year, pp. 7-8]。  
4. 绝对孔隙度对比：低Dc时2D估计偏高（假设裂缝在z向不变），高Dc时3D可能反超（3D裂缝数量增速更快）；因此**3D更适合绝对孔隙度估算**[Kim unknown-year, pp. 8-8]。  
5. 两步法（2D定Dfp，3D定φf0）实现任意尺度裂缝孔隙度估算，且效率较高 [Kim unknown-year, pp. 8-8, 10-10]。  
6. Bridger Gap应用：成功生成几何、方位与原始露头一致的FDFN，为附加开度分布后估算孔隙度奠定基础 [Kim unknown-year, pp. 9-10]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 裂缝孔隙度遵循分形标度律，2D和3D生成均验证（R²良好） | [Kim unknown-year, pp. 4-4, 6-7]；Chang & Yortsos (1990) | 多域尺寸，每种尺寸多次实现取平均 | Dfp受Dc和Dl影响 |
| 2D与3D所得Dfp几乎一致，围绕45°线分布 | [Kim unknown-year, pp. 7-8] Fig.15 | 12组案例（6组2D，6组3D） | 支持2D用于Dfp估计 |
| 当Dc较小时2D孔隙度 > 3D；高Dc时3D可反超 | [Kim unknown-year, pp. 8-8] Fig.16 | Case1‑6对比 | 2D假设z向恒等 |
| Bridger Gap实测：Dc=1.691, Dl=1.266, a=0.965，两组方位Fisher常数103和62 | [Kim unknown-year, pp. 9-9] Figs.19,21,23 | Harstad (1995)露头 | 直接用作输入参数 |
| 生成网络的中心距‑长度幂律与理论值吻合，最大误差13.6% | [Kim unknown-year, pp. 6-6, 7-7] Fig.13 | 24个3D‑FDFN的2D截面分析 | 几何合理性验证 |

## Limitations
- 3D裂缝形状假定为圆盘，实际形状可能更复杂 [Kim unknown-year, pp. 4-6]。  
- 开度参数（H、A）获取依赖特定实验或成像测井，通用性待验证 [Kim unknown-year, pp. 10-10]。  
- 3D生成耗时长、内存需求大，限制了验证域尺寸和实现次数 [Kim unknown-year, pp. 6-7]。  
- 未与动态流动模拟耦合，对生产动态的预测能力未知。  
- 假设基质孔隙度为零且裂缝网络完全符合分形模型；非分形或混合特征储层的适用性待评估。

## Assumptions / Conditions
- 储层属Nelson (2001) Type I：基岩无储存能力与渗透率 [Kim unknown-year, pp. 1-1]。  
- 裂缝中心分布可用一阶分形模型描述，密度项 **a** 不依赖观察尺度 [Kim unknown-year, pp. 1-2]。  
- 裂缝长度服从幂律分布，分形维数Dl为常数。  
- 裂缝开度为自仿射分形，各裂缝独立生成 [Kim unknown-year, pp. 2-3]。  
- 裂缝方位符合Fisher分布 [Kim unknown-year, pp. 2-2]。  
- 3D裂缝形状为圆盘，其直径与2D迹长转换采用Piggott (1997)关系式 [Kim unknown-year, pp. 4-6, 式11]。  
- 裂缝孔隙度标度律采用Chang & Yortsos (1990)模型，嵌入欧式维数E在2D为2，3D为3 [Kim unknown-year, pp. 4-4]。

## Key Variables / Parameters
- **Dc, Dc3D**：裂缝中心分布分形维数（2D/3D）[Kim unknown-year, pp. 1-2, 4-6]  
- **Dl, Dl3D**：裂缝长度分布分形维数 [Kim unknown-year, pp. 1-2]  
- **a, a3D**：裂缝密度项（式1,2,11关联）[Kim unknown-year, pp. 1-2, 4-6]  
- **lmin**：最小裂缝长度 [Kim unknown-year, pp. 1-2]  
- **K**：Fisher常数，控制方位离散度 [Kim unknown-year, pp. 2-2]  
- **H**：Hurst指数，开度粗糙度 [Kim unknown-year, pp. 2-3]  
- **A**：开度振幅 [Kim unknown-year, pp. 3-3]  
- **φf0, L0**：参考域边长及对应初始裂缝孔隙度 [Kim unknown-year, pp. 4-4]  
- **Dfp, Dfp3D**：裂缝孔隙度分形维数 [Kim unknown-year, pp. 4-4]  
- **L**：感兴趣域边长 [Kim unknown-year, pp. 4-4]

## Reusable Claims
- 「利用乘法级联过程生成裂缝中心并结合自仿射开度模型的FDFN，能比平行板假设的DFN产生更真实的孔隙度估计。」依据 [Kim unknown-year, pp. 1-1, 2-3]  
- 「I型天然裂缝性储层的裂缝孔隙度是尺度相关的，遵循幂律标度，其分形维数Dfp可由2D或3D FDFN导出。」依据 [Kim unknown-year, pp. 4-4, 6-7]  
- 「2D FDFN能高效估算Dfp，而3D FDFN提供更准确的绝对孔隙度值；两者结合可估计任意尺度的裂缝孔隙度。」依据 [Kim unknown-year, pp. 7-8, 8-8]  
- 「一阶分形模型中的密度项a不依赖于测量或生成域的尺度，使得不同尺度数据的直接利用成为可能。」依据 [Kim unknown-year, pp. 1-2]  
- 「随着长度分形维数Dl增大，裂缝孔隙度降低；随着中心分形维数Dc增大，裂缝孔隙度（尤其在大尺度）升高。」依据 [Kim unknown-year, pp. 4-4, 6-7]

## Candidate Concepts
- [[天然裂缝性储层]]
- [[分形离散裂缝网络]]
- [[裂缝孔隙度分形维数]]
- [[乘法级联过程]]
- [[自仿射裂缝开度]]
- [[Fisher分布]]
- [[一阶分形断裂模型]]
- [[Chang-Yortsos孔隙度标度律]]
- [[裂缝网络聚类性]]
- [[2D与3D分形密度转换]]

## Candidate Methods
- [[分形离散裂缝网络生成（2D/3D）]]
- [[乘法级联裂缝中心生成]]
- [[修正连续随机加法开度模拟]]
- [[配对关联函数分形分析]]
- [[裂缝网络几何验证（中心距-长度幂律）]]
- [[露头裂缝特征数字化与统计]]
- [[2D-3D分形维数关系利用]]
- [[基于标度律的裂缝孔隙度外推]]

## Connections To Other Work
- 引用Nelson (2001)的裂缝储层分类作为应用背景 [Kim unknown-year, pp. 1-1]。  
- 裂缝网络分形建模直接继承Davy et al. (1990)、Bour & Davy (1999)、Bour et al. (2002)、Darcel et al. (2003)的工作 [Kim unknown-year, pp. 1-2, 3-3]。  
- 开度建模基于分数布朗运动（Voss 1988）及Moltz et al. (1997)、Liu et al. (2004)的算法改进 [Kim unknown-year, pp. 2-3]。  
- 孔隙度标度律源自Chang & Yortsos (1990)的分形油藏模型 [Kim unknown-year, pp. 4-4]。  
- 3D裂缝迹长与直径的转换采用Piggott (1997)的公式 [Kim unknown-year, pp. 4-6]。  
- 实测开度数据引用Pyrak‑Nolte et al. (1987)、Keller (1996)、Bertel et al. (2001)、Muralidharan et al. (2004)及Kim & Schechter (2006)等 [Kim unknown-year, pp. 1-1, 5-6]。

## Open Questions
- 在完全耦合的流动与地质力学模拟中，FDFN估算的孔隙度对生产动态的影响如何？  
- 开度分形参数H和A对最终孔隙度估算的敏感性如何？如何从有限的测井数据中约束这些参数？  
- 方法对非分形或混合成因裂缝网络的适用性及所需修正。  
- 能否通过井间示踪剂测试或生产动态反演来验证估算的裂缝孔隙度？  
- 在多相流条件下，粗糙开度分布对有效裂缝孔隙度的影响是否与静态估算一致？

## Source Coverage
所有非空索引片段均已处理并纳入本页面。索引文本10个，总字符数46 461，非空源块10个，编译源块10个，编译源字符46 738。覆盖率（按块）：1.0，覆盖率（按字符）：1.005962。源签名：525268d5f9814159c2668edb1b7f66a457c849e4。编译策略：单次编译。 [Kim unknown-year, pp. 1-1 ~ 11-11]
