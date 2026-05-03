---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2014-jin-analytical-expressions-for-the-size-distribution-function-of-elliptical-joints"
title: "Analytical Expressions for the Size Distribution Function of Elliptical Joints."
status: "draft"
source_pdf: "data/papers/2014 - Analytical expressions for the size distribution function of elliptical joints.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Jin, Wencheng, et al. \"Analytical Expressions for the Size Distribution Function of Elliptical Joints.\" *International Journal of Rock Mechanics & Mining Sciences*, vol. 70, 2014, pp. 201-211. DOI:10.1016/j.ijrmms.2014.04.017."
indexed_texts: "11"
indexed_chars: "53521"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "53735"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.003998"
coverage_status: "full-index"
source_signature: "221213972bb7fdf527a61cf01e38df049dbf2f7d"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T15:13:30"
---

# Analytical Expressions for the Size Distribution Function of Elliptical Joints.

## One-line Summary
本文推导了非平行椭圆节理的迹长与尺寸分布之间的体视学关系，并针对均匀、分形、指数及多项式迹长分布，给出了节理长轴尺寸概率密度函数的解析解；通过蒙特卡洛模拟验证了方法的有效性。

## Research Question
如何从可观测的迹长分布（trace length distribution）精确推断三维空间中椭圆节理的尺寸分布（major axis PDF），尤其是当节理为非平行且形状为椭圆时，现有体视学关系存在奇异性和解析解缺失的问题。[Jin 2014, pp. 1-2]

## Study Area / Data
本文未涉及具体野外研究区域。数值验证通过蒙特卡洛模拟生成两组节理网络：
- 模拟1：节理方位确定（倾向0°∠60°，旋转角45°），长宽比k=2；长轴尺寸服从均匀分布，均值8，标准差1；体积密度P30=0.25；采样窗尺寸50×36，方位45°∠90°。
- 模拟2：节理方位确定（45°∠60°，旋转角30°），k=1.5；长轴服从正态分布，均值8，标准差1；P30=0.2；采样窗70×36，方位90°∠90°。
模拟中分别采集到1848和1174条迹线。[Jin 2014, pp. 7-9, Table 1]

## Methods
1. **体视学关系推导**：假设节理为扁平椭圆盘，同一组节理长宽比k恒定、旋转角φ恒定；中心服从泊松分布，取向服从分布f(θ,φ)。通过几何关系建立迹长l与长轴a的积分方程（式15），该方程耦合了节理取向，但证明了迹长分布与采样窗及节理倾角/倾向的独立性。[Jin 2014, pp. 2-4]
2. **Abel积分逆变换**：将积分方程转化为Abel型积分，借鉴Santalò理论导出逆关系（式19），从而可由中间函数h(t) = f(Mt)解析求出g(a)，其中M为与k和特征角β相关的常数。[Jin 2014, pp. 4]
3. **特定分布解析解**：针对四种迹长分布直接给出g(a)的闭式解或半解析解：
   - 均匀分布（式24）[Jin 2014, pp. 4-5]
   - 分形分布（幂律，式31），证明节理尺寸也服从分形分布且分维数比迹长分维数大1。[Jin 2014, pp. 5-6]
   - 指数分布（式42），解中包含修正贝塞尔函数。[Jin 2014, pp. 6-7]
   - 任意多项式分布：用多项式拟合迹长PDF，再利用分部积分和递归关系得到g(a)的半解析表达式（式52-57），并通过迭代数值确定最小长轴ξ₀和平均长度μa。[Jin 2014, pp. 7]
4. **迹长校正**：采用Song和Lee（2001）的方法，利用包含、截断、跨越迹线的计数关系从有限窗口采样统计中恢复无限平面上的真实迹长分布f(l)。[Jin 2014, pp. 7-9]
5. **蒙特卡洛验证**：使用自编Matlab工具箱RJNS3D生成离散裂隙网络，采样获得迹长，按上述流程反推尺寸分布，与理论分布比较。[Jin 2014, pp. 8-10]

## Key Findings
- 导出的体视学关系（式15）表明，即使考虑节理取向，迹长分布仍独立于采样窗和节理的倾角/倾向；该结论与平行节理假设下的结果一致，验证了推导的正确性。[Jin 2014, pp. 4]
- 分形迹长分布导出的节理尺寸分布也是分形，且分维数关系为D_joint = D_trace + 1；前人（La Pointe 2002）基于圆形节理的推测得到证实。[Jin 2014, pp. 5-6]
- 针对均匀、指数、多项式迹长分布，给出了可工程应用的g(a)解析式或半解析递推公式（汇总于Table 3）。[Jin 2014, pp. 10, Table 3]
- 蒙特卡洛模拟显示，反演的尺寸分布理论值（均值、上下界）与模拟输入吻合良好（如均匀分布案例均值理论8.000 vs 模拟7.935，正态案例均值理论8.000 vs 8.005），验证了所提方法的有效性。[Jin 2014, pp. 9-10, Table 2]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 体视学关系式(15)：f(l,θ,φ) = (l cosα f(θ,φ))/(M λ μ_a) ∫_{l/M}^{∞} g(a)/√((Ma)² - l²) da | [Jin 2014, pp. 3-4] | 椭圆节理，同组k、φ恒定，中心泊松分布 | 耦合取向但最终迹长分布与取向无关 |
| 均匀迹长对应g(a)式(24)：g(a) = (√(1/a² - 1/ξ²)) / (√(ξ²-ξ₀²)/ξ - ln((ξ-√(ξ²-ξ₀²))/ξ₀))⁻¹ | [Jin 2014, pp. 4-5] | ξ=B₂/M，ξ₀为最小长轴，由数值确定 | μ_a由归一化条件反算（式23） |
| 分形迹长(幂律指数D)对应g(a)式(31)：g(a) = (D+1) ξ₀^{D+1} a^{-(D+2)} | [Jin 2014, pp. 5-6] | 迹长CCDF: G(l) = η₀^D l^{-D} | 分维数关系：D_joint = D + 1 |
| 指数迹长f(l)=Ae^{-Al}对应g(a)式(42)：g(a) = AM BesselK[1, MAa] / BesselK[0, MAξ₀] | [Jin 2014, pp. 6-7] | μ_a = π/(2A M BesselK[0, MAξ₀]) | 需数值确定ξ₀ |
| 多项式迹长f(l)=Σ b_k l^k对应g(a)递归公式(52)-(57) | [Jin 2014, pp. 7] | 用多项式拟合任意连续分布 | 需迭代确定ξ₀与μ_a |
| 蒙特卡洛验证均值和上下界对比（Table 2） | [Jin 2014, pp. 9-10] | 两组定向节理，均匀/正态尺寸分布 | 理论值与模拟值相对误差<1% |

## Limitations
- 所有结果基于假设：节理形状为扁平椭圆盘；同一组节理具有相同长宽比k和固定旋转角φ；中心服从泊松分布。[Jin 2014, pp. 2-3]
- 推导假设迹长分布已知且为无限平面上的真实分布，实际中需要从有限窗口采样校正，可能引入额外误差。[Jin 2014, pp. 7-8]
- 解析解要求迹长分布形式简单（均匀、指数、分形、多项式），对于其他复杂分布需用多项式近似。[Jin 2014, pp. 7]
- 用于推断长宽比k和旋转角φ的方法需要至少两个不同方位的采样窗，且窗口足够大以包含最大迹长，实际应用受限。[Jin 2014, pp. 10]

## Assumptions / Conditions
- 节理为扁平椭圆板，同组内长宽比k（长轴/短轴）恒定，旋转角φ恒定。[Jin 2014, pp. 2]
- 节理中心位置服从三维泊松过程，均值密度P₃₀。[Jin 2014, pp. 2]
- 节理取向的联合PDF f(θ,φ)存在，但最终迹长分布与取向无关。[Jin 2014, pp. 4]
- 用于解析解推导时，假定迹长分布函数在无限区间内“行为良好”（well behaved），且长轴尺寸有有限上界ξ = η/M。[Jin 2014, pp. 4]
- 蒙特卡洛验证中，节理取向设为确定值以简化处理，且采样窗足够大以避免删截偏差。[Jin 2014, pp. 8-9]

## Key Variables / Parameters
- a：椭圆长轴长度，作为节理特征尺寸（characteristic dimension）
- k：椭圆长宽比（长轴/短轴）
- β：特征角，长轴与迹线垂线的夹角（由节理旋转角和采样面决定）
- M：最大迹长与长轴之比，M = √(cot²β+1) / √(k²cot²β+1) (式10)
- g(a)：长轴尺寸的概率密度函数（PDF）
- f(l)：无限采样面上的迹长PDF
- f(l,θ,φ)：考虑节理取向的三维迹长概率函数（式15）
- P₃₀：节理体积密度
- λ, μ_a：中间变量，λ = ∫∫ cosα f(θ,φ) dθ dφ，μ_a = ∫ a g(a) da  [Jin 2014, pp. 2-3]
- ξ₀, ξ：长轴的最小和最大界限（ξ = 最大迹长η / M）
- D：分形分布的幂指数（分维数）

## Reusable Claims
- **体视学独立性**：对于非平行椭圆节理，无限平面上迹长分布f(l)与采样窗方向和节理产状（倾向/倾角）无关，仅取决于长宽比k和特征角β，从而验证了工程中忽略取向影响的常用假设。[Jin 2014, pp. 4]
- **分形尺寸关系**：若迹长服从幂律分形分布（CCDF ∝ l^{-D}），则椭圆长轴也服从分形分布，且分维数 D_a = D + 1。此关系独立于k和β，且与La Pointe（2002）针对圆盘的结果一致。[Jin 2014, pp. 5-6]
- **均匀迹长解**：当迹长在[B₁, B₂]内均匀分布时，长轴分布g(a)为闭式（式24），其中ξ=B₂/M，ξ₀由归一化条件数值确定。该解可用于初步估算节理尺寸分布。[Jin 2014, pp. 4-5, Table 3]
- **指数迹长解**：迹长服从负指数分布时，g(a)正比于a·BesselK(1, MAa)，其中μ_a = π/[2A M BesselK(0, MAξ₀)]。该解为指数类分布的精确逆推提供了基础。[Jin 2014, pp. 6-7]
- **多项式近似通用框架**：任意连续迹长分布可拟合为多项式，代入递归公式（52-57）求得g(a)的半解析解。此方法可处理工程中任意形态的迹长直方图，避免了传统矩方法的分布假设限制。[Jin 2014, pp. 7]
- **迹长校正适用性**：Song和Lee（2001）的迹长校正方法（基于包含、截断计数）可扩展用于椭圆节理，因为单节理的迹长仍正比于中心到采样面的距离。[Jin 2014, pp. 7-8]
- **k/β推断策略**：当未知k和φ时，可通过两个以上不同方位采样窗获取迹长分布，假设多组M值反复迭代，直至反算的μ_a一致，从而确定k与β。该思路为工程中椭圆形状参数获取提供了可行路径。[Jin 2014, pp. 10]

## Candidate Concepts
- [[椭圆节理]] (elliptical joints)
- [[体视学关系]] (stereological relationship)
- [[迹长分布]] (trace length distribution)
- [[节理尺寸分布]] (joint size distribution, PDF of major axis)
- [[Abel积分逆变换]] (inverse Abel integral)
- [[分形裂隙网络]] (fractal fracture network)
- [[蒙特卡洛验证]] (Monte Carlo simulation)
- [[离散裂隙网络]] (discrete fracture network, DFN)
- [[Song-Lee迹长校正]] (Song and Lee bias correction)
- [[Crofton定理]] (Crofton theorem)
- [[泊松平板模型]] (Poisson flat plate model)

## Candidate Methods
- [[椭圆节理迹长-尺寸体视学推导]]：基于泊松假设与几何概率导出积分方程（式15），并证明取向独立性。[Jin 2014, pp. 2-4]
- [[Santalò变换求逆]]：将体视学方程转化为Abel方程并求逆，得到g(a)的通用积分表达式（式19）。[Jin 2014, pp. 4]
- [[特定分布解析反演]]：分别对均匀、分形、指数分布迹长直接积分得到g(a)解析式。[Jin 2014, pp. 4-7]
- [[多项式迹长尺寸反演]]：用多项式拟合任意迹长分布，通过分部积分和递归积分得到g(a)的半解析解，并迭代确定参数。[Jin 2014, pp. 7]
- [[基于包含迹线的分布校正]]：利用Song和Lee方法从窗口采样数据恢复无限面迹长分布，应用于椭圆节理。[Jin 2014, pp. 7-9]
- [[双窗口推断形状参数]]：通过两个不同方位采样窗的迹长与平均尺寸一致性约束，推断k和旋转角φ。[Jin 2014, pp. 10]

## Connections To Other Work
- 与Warburton (1980)的圆盘/平行四边形节理体视学工作一脉相承，但将其推广到椭圆形。
- 借鉴Zhang et al. (2002)关于平行椭圆节理的体视学关系，本工作去除了平行假设，并证明所得关系在耦合取向后迹长分布仍与取向无关。[Jin 2014, pp. 2, 4]
- 逆问题求解利用了Santalò针对球体截圆问题的积分变换，与Tonon & Chen (2007)对圆盘直径的一类闭式解方法类似，但本文针对椭圆推导了更复杂的逆变换。[Jin 2014, pp. 4, 10]
- 分形分布的结果印证了La Pointe (2002)的推测：分形迹长对应分形尺寸，且尺寸分维数高1。
- 迹长校正采用Song & Lee (2001)的计数法，并验证其适用于椭圆节理。
- 多项式拟合法避免了Crofton定理依赖矩假设的缺点，与Song (2006)的离散数值解法思路不同，提供了连续解析近似。[Jin 2014, pp. 7]

## Open Questions
- 如何在实际工程中准确获取同一组节理的k和φ仍依赖多个不同方向的采样窗，且对采样窗尺寸有严格要求，操作难度较大。[Jin 2014, pp. 10]
- 当节理长宽比k、旋转角φ不恒定时（例如存在统计分布），体视学关系如何修正？[未明确，基于现有假设]
- 本文方法仅给出长轴分布g(a)，要完整描述椭圆节理尺寸还需知道短轴分布（默认由k固定），当k也随机时如何联合反演？[未涉及]
- 多项式拟合的阶数选择对反演精度的影响规律如何？是否存在过拟合风险？[未讨论]
- 所提方法在严重删截采样（如隧道掌子面有限窗口）时的鲁棒性尚未测试。

## Source Coverage
本页基于论文全文索引片段生成，共处理11个非空源块，覆盖字符53,521（索引）/ 53,735（编译），覆盖率100%（按块数和字符数）。所有非空索引片段均被纳入分析。
