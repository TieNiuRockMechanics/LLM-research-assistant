---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2005-auradou-permeability-anisotropy-induced-by-the-shear-displacement-of-rough-fracture-walls"
title: "Permeability Anisotropy Induced by the Shear Displacement of Rough Fracture Walls."
status: "draft"
source_pdf: "data/papers/2005 - Permeability anisotropy induced by the shear displacement of rough fracture walls.pdf"
collections:
citation: "Auradou, H., et al. “Permeability Anisotropy Induced by the Shear Displacement of Rough Fracture Walls.” *Water Resources Research*, vol. 41, 2005, pp. W09423, doi:10.1029/2005WR003938."
indexed_texts: "13"
indexed_chars: "60819"
nonempty_source_blocks: "13"
compiled_source_blocks: "13"
compiled_source_chars: "61119"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004933"
coverage_status: "full-index"
source_signature: "e6170a0ff44f43a356815ab47e469469d8fb023f"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T12:45:09"
---

# Permeability Anisotropy Induced by the Shear Displacement of Rough Fracture Walls.

## One-line Summary
剪切位移使粗糙裂隙壁面的互补自仿射表面产生渗透率各向异性，平行于位移方向的渗透率随归一化孔径方差 \(S^2\) 线性下降，垂直方向的渗透率线性上升或保持稳定，\(S^2\) 是控制该过程的关键参数 [Auradou 2005, pp. 1-1, 8-9]。

## Research Question
粗糙裂隙两壁具有互补的自仿射形貌，当施加平行于平均平面的剪切位移 \(\vec{u}\) 后，裂隙渗透率如何产生各向异性？渗透率各向异性与孔径场统计特征（尤其是归一化孔径方差 \(S^2\)）之间存在何种定量关系？ [Auradou 2005, pp. 1-1, 1-2]。

## Study Area / Data
- **物理实验**：透明环氧树脂和硅橡胶复制的花岗岩拉伸裂隙模型，源自法国布列塔尼 Lanhelin 采石场。原始岩块尺寸 25×25×40 cm³ [Auradou 2005, pp. 1-2, 2-3]。
- **表面形貌**：机械轮廓仪（770×60 网格，250 μm 间距，10 μm 垂直分辨率）获取表面高度图；自仿射 Hurst 指数 \(\zeta=0.75\pm0.05\)，功率谱密度符合 \(P(f)\propto f^{-1-2\zeta}\)，在约 0.75 mm 至 50 mm 尺度范围内成立 [Auradou 2005, pp. 2-3]。
- **数值模拟**：傅里叶合成法生成自仿射表面，Hurst 指数设为 0.8，平均粗糙度 1 mm 距离内高度波动约为 0.25 mm，平均隙宽 \(a_0\approx 1\text{ mm}\)，模拟域典型尺寸 25.6×25.6 mm，最大剪切位移至表面首次接触 [Auradou 2005, pp. 6-7]。
- **流体**：水–甘油溶液（10% 甘油，20 ℃ 黏度 1.288 cP），染色液含 0.2–0.3 g/L 苯胺黑，密度匹配，雷诺数 < 1，流量 < 5 mL/min [Auradou 2005, pp. 2-3]。

## Methods
1. **实验装置**：顶部固定透明环氧树脂壁面，底部硅橡胶壁面可垂直（\(a_0\)）和水平（\(\vec{u}\)）平移，裂隙内充满透明流体，从中心孔径向注入染色流体，通过 CCD 相机记录透射光强 [Auradou 2005, pp. 2-3]。
2. **浓度场重构**：基于比尔–朗伯定律 \(I(x,y)=I_0(x,y)\exp[-m\,c(x,y)\,a(x,y)]\)，利用已知消光系数 \(m=2.9\pm0.4\text{ m}^2/\text{g}\) 和最终稳态浓度 \(c_f\)，计算每一像素的瞬时浓度 \(c(x,y,t)/c_f = \ln[I/I_0] / \ln[I_0/I_f]\) [Auradou 2005, pp. 3-4]。
3. **各向异性定量**：计算浓度场惯性张量 \(\mathbf{M}(t)\)，其特征值 \(\lambda_+^2\)、\(\lambda_-^2\) 给出快慢流动方向，特征值比 \((\lambda_+/ \lambda_-)^2\) 通过弱各向异性 Hele-Shaw 流近似等于渗透率比 \(k_\perp/k_\parallel\) [Auradou 2005, pp. 3-5]。
4. **数值模拟**：采用格子 Boltzmann 方法求解完整三维流场，周期性边界条件，分别沿平行和垂直于 \(\vec{u}\) 的方向施加压力梯度，计算流量得到渗透率 \(k_\parallel/k_0\) 和 \(k_\perp/k_0\) [Auradou 2005, pp. 6-7]。
5. **解析模型**：将裂隙视为平行“脊”通道，平行位移方向为串联电阻，垂直方向为并联电阻，得到有效水力隙宽的上下界：\(\langle a^3 \rangle / a_0^3 = 1+3S^2\) 和 \(\langle a^{-3}\rangle^{-1}/a_0^3 = 1-6S^2 + O(S^4)\) [Auradou 2005, pp. 5-6]。

## Key Findings
- 剪切位移导致孔径场中出现垂直于 \(\vec{u}\) 的拉长通道（脊），抑制平行流，增强垂直流 [Auradou 2005, pp. 3-4]。
- 实验侵入斑长轴方向始终垂直于剪切位移方向，与位移振幅无关；无位移时形状近似圆形 [Auradou 2005, pp. 4-5]。
- 归一化孔径方差 \(S^2 = \sigma_a^2(u)/a_0^2\) 与位移幅值 \(u\) 成幂律关系：\(\sigma_a(u) \propto u^\zeta\)（\(\zeta=0.75\)），与表面自仿射指数一致 [Auradou 2005, pp. 5-6]。
- 数值模拟显示：\(k_\parallel/k_0\) 随 \(S^2\) 线性下降，\(k_\perp/k_0\) 随 \(S^2\) 线性上升，不同剪切方向结果相似，证实各向异性仅由剪切位移引起 [Auradou 2005, pp. 7-8]。
- 简单串联/并联模型给出的上下界与模拟趋势定性一致，方向正确，数量级相当 [Auradou 2005, pp. 7-8]。
- 实验渗透率比 \(k_\perp/k_\parallel\) 随 \(S^2\) 近似线性增大，斜率因剪切方向而异（y 方向约为 5.4，x 方向约为 2.3），且始终位于数值模拟最强与最弱各向异性之间 [Auradou 2005, pp. 8-9]。
- 对所有数值实现进行平均，得到拟合式：\(\langle k_\perp/k_0 \rangle = 0.995 + 1.09 S^2\)，\(\langle k_\parallel/k_0 \rangle = 0.955 - 3.05 S^2\) [Auradou 2005, pp. 7-8]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 侵入斑长轴方向始终垂直于 \(\vec{u}\)，角度波动约 ±5° | [Auradou 2005, pp. 4-5] | 不同振幅（0.25–1 mm）和方向（沿x、y、45°） | 无位移时方向分散，证实各向异性由剪切位移产生。 |
| 孔径方差 \(\sigma_a\) 与位移 \(u\) 关系：\(\sigma_a=0.265–0.285\,u^{0.75}\) | [Auradou 2005, pp. 5-6] | 不同剪切方向（±x, ±y） | 幂指数 0.75 与表面自仿射指数一致，验证自仿射相关性。 |
| 数值模拟中 \(k_\parallel/k_0\) 和 \(k_\perp/k_0\) 均随 \(S^2\) 线性变化，方向相反 | [Auradou 2005, pp. 7-8] | \(a_0=1.0\text{ mm}\)，变位移 (0–1.6 mm) 或固定位移变隙宽 (0.75–2.0 mm) | 两个实现及不同剪切方向均呈现相同趋势，证实 \(S^2\) 是控制参数。 |
| 实验 \(k_\perp/k_\parallel\) 随 \(S^2\) 线性增大，斜率为 2.3 ± 0.15 (x方向) 和 5.4 ± 0.3 (y方向) | [Auradou 2005, pp. 8-9] | 恒隙宽 \(a_0=1\text{ mm}\) 变位移，或恒位移 \(u_x=2.0\text{ mm}\) 变隙宽 | 斜率差异反映统计涨落，但总体趋势一致。 |
| 串联/并联模型预测 \(k_\perp\) 上限为 \(1+3S^2\)，\(k_\parallel\) 下限为 \(1-6S^2+...\) | [Auradou 2005, pp. 5-6] | 假设孔径呈高斯分布，\(S\ll1\) | 预测方向与幅度与模拟吻合，但绝对值存在分散。 |

## Limitations
- 惯性张量法估算渗透率比严格仅适用于弱各向异性（\(|k_x-k_y|\ll k_x+k_y\)），当 \(S\) 接近 0.1 时出现偏离线性的非线性效应 [Auradou 2005, pp. 4-5, 8-9]。
- 数值模拟和解析模型假设壁面无接触，未考虑随深度增加可能出现的接触面积效应 [Auradou 2005, pp. 1-2, 9-9]。
- 解析模型建立在栅格状“脊”通道假设上，未考虑孔径场的连通性、曲折度等其他几何因素，导致不同实现间常数有较大分散 [Auradou 2005, pp. 8-9]。
- 模拟域尺寸（约 25.6 mm）有限，可能存在有限尺寸效应；实验裂隙尺寸为 20 cm，但统计涨落仍显著 [Auradou 2005, pp. 2-3, 9-9]。
- 实验仅能测定渗透率比 \(k_\perp/k_\parallel\)，无法获得绝对渗透率；用于验证的数值模拟则提供绝对比值 [Auradou 2005, pp. 1-2, 6-7]。

## Assumptions / Conditions
- 裂隙壁面为各向同性、互补的自仿射表面，Hurst 指数 \(\zeta\approx0.75–0.8\)；各向异性仅由剪切位移引入 [Auradou 2005, pp. 1-1, 1-2, 2-3]。
- 剪切位移足够小，两壁在任何位置均不接触，隙宽完全由垂直分离 \(a_0\) 和局部高度差决定，避免剪胀效应 [Auradou 2005, pp. 1-2]。
- 径向注入为二维 Hele-Shaw 型流动，忽略惯性（Re < 1），满足达西定律 [Auradou 2005, pp. 2-3]。
- 局部浓度与光强的指数关系（比尔–朗伯定律）成立，且吸光度与 \(a\,c\) 呈线性（适用于 \(a\,c_0 < 0.15\text{ g/m}^2\)）[Auradou 2005, pp. 3-4]。
- 对于解析模型，孔径分布近似为高斯分布，且 \(S\ll 1\)，可展开至 \(O(S^2)\) [Auradou 2005, pp. 5-6]。
- 渗透率各向异性可用侵入斑惯性张量特征值比表征，且该比值在 \(R_g>30\text{ mm}\) 后趋于稳定，侵入过程自相似 [Auradou 2005, pp. 4-5]。

## Key Variables / Parameters
- 剪切位移矢量 \(\vec{u}\)（幅值 \(u\)、方向）
- 平均垂直分离隙宽 \(a_0\)
- 归一化孔径方差 \(S^2 = \langle (a-a_0)^2 \rangle / a_0^2 = \sigma_a^2(u)/a_0^2\)，其中 \(\sigma_a(u)\propto u^\zeta\)
- 平行渗透率 \(k_\parallel\)、垂直渗透率 \(k_\perp\)、各向同性渗透率 \(k_0\)（\(u=0\)）
- 惯性张量特征值比 \((\lambda_+/\lambda_-)^2\)，用作 \(k_\perp/k_\parallel\) 的估计
- 自仿射 Hurst 指数 \(\zeta\)（实验 0.75，模拟 0.8）

## Reusable Claims
1. **剪切位移方向与渗透率各向异性方向固定**：对互补自仿射裂隙壁，剪切位移 \(\vec{u}\) 会导致垂直于 \(\vec{u}\) 的方向成为优先流动通道，平行于 \(\vec{u}\) 的渗透率下降。该结论在实验（多种位移方向和大小）和数值模拟（不同表面实现）中均成立，条件是壁面无接触、初始表面各向同性 [Auradou 2005, pp. 4-5, 7-8]。
2. **归一化孔径方差 \(S^2\) 是控制渗透率各向异性的关键参数**：\(k_\parallel/k_0\) 和 \(k_\perp/k_0\) 均随 \(S^2\) 近似线性变化，且该关系在固定隙宽变位移和固定位移变隙宽两种工况下保持一致，表明只要裂隙保持张开，行为对绝对隙宽不敏感 [Auradou 2005, pp. 7-8]。
3. **简单串联/并联模型可定性预测渗透率变化方向**：将孔径结构简化为平行“脊”后，串联模型给出 \(k_\parallel\) 下限（随 \(S^2\) 下降），并联模型给出 \(k_\perp\) 上限（随 \(S^2\) 上升），可用于初步估计，但具体系数需考虑具体表面几何 [Auradou 2005, pp. 5-6, 7-8]。
4. **孔径方差与剪切位移的标度律**：对于自仿射表面，\(\sigma_a(u) = C u^\zeta\)，其中 \(\zeta\) 与表面 Hurst 指数相同；因此，若能从有限测量获得 \(C\) 和 \(\zeta\)，可在不完整形貌扫描的情况下估算 \(S^2\) [Auradou 2005, pp. 5-6]。
5. **径向注入实验可用于快速获取渗透率各向异性比值**：通过分析染色液侵入斑的惯性张量，可估算 \(k_\perp/k_\parallel\)，但该方法要求各向异性较弱且边界各向同性 [Auradou 2005, pp. 3-5]。

## Candidate Concepts
- [[自仿射裂隙 (self-affine fracture)]]
- [[剪切诱导渗透率各向异性 (shear-induced permeability anisotropy)]]
- [[孔径方差 (aperture variance)]]
- [[串联–并联通道模型 (series-parallel channels model)]]
- [[惯性张量分析 (inertia tensor analysis)]]
- [[径向注入实验 (radial injection experiment)]]
- [[格子 Boltzmann 方法 (lattice Boltzmann method)]]
- [[互补表面剪切位移 (complementary surface shear displacement)]]
- [[归一化孔径方差 S²]]
- [[渗透率各向异性比值 k⊥/k∥]]

## Candidate Methods
- [[径向染色液注入结合比尔–朗伯定律反演浓度场]]
- [[基于惯性张量的侵入斑各向异性量化]]
- [[机械轮廓仪获取自仿射表面高度图]]
- [[透明环氧/硅橡胶裂隙复模制造技术]]
- [[格子 Boltzmann 法模拟粗糙裂隙三维流动]]
- [[傅里叶合成法生成自仿射表面]]
- [[基于功率谱密度的自仿射指数测定]]
- [[通过变隙宽/变位移实验分离孔径方差效应]]

## Connections To Other Work
- 前期研究已观测到剪切后垂直方向渗透率高于平行方向的现象 [Gentier et al., 1997; Yeo et al., 1998]，以及自仿射裂隙中的渗透率各向异性迹象 [Drazer and Koplik, 2002]。本工作首次系统结合实验、数值和解析论证了这一效应。
- Thompson and Brown [1991] 使用各向异性表面发现渗透率受相关长度方向影响，本研究的各向异性并非表面本身各向异性，而是由剪切位移引起，机理不同但现象类似。
- 自仿射断层和裂隙表面的普遍性由 Bouchaud [2003] 等总结，花岗岩类 Hurst 指数约 0.8；本工作使用的表面拟合指数 0.75 与文献一致 [Boffa et al., 1998; Méheust and Schmittbuhl, 2000]。
- 串联/并联电阻类比思路源于 Zimmerman et al. [1991] 对正弦和锯齿隙宽的分析，本工作将其推广至自仿射裂隙并引入孔径方差 \(S^2\) 作为控制参数。
- Plouraboué et al. [1995] 研究了自仿射裂隙孔径场的标度性质，指出剪切位移引入的失相关长度，本工作在此基础上将孔径方差与渗透率联系起来。
- 格子 Boltzmann 方法在粗糙裂隙流动中的应用可见于 Drazer and Koplik [2000, 2001, 2002] 等，本工作沿用其数值框架。

## Open Questions
- 渗透率变化量在不同表面实现间存在显著分散，除 \(S^2\) 外，还有哪些几何参数（例如脊的连通性、脊间距、曲折度）控制该分散？有限尺寸效应在模拟和实验中影响如何？ [Auradou 2005, pp. 8-9]。
- 能否仅通过有限测点（如沿剪切方向的少数轮廓线）估计孔径方差，从而免去全表面扫描？此简化对预测渗透率各向异性的精度如何？ [Auradou 2005, pp. 9-9]。
- 当裂隙承受较大正应力、接触面积显著增加时，剪切诱导的各向异性规律是否仍然以 \(S^2\) 为主导？哪些新参数需引入？ [Auradou 2005, pp. 9-9]。
- 当 \(S\) 不再远小于 1 时，非线性项如何影响渗透率比？更高阶的孔径分布矩是否必需？ [Auradou 2005, pp. 8-9]。
- 本研究的渗透率各向异性分析基于稳态单相流，其对溶质输运（如弥散张量各向异性）的影响是否可类比？ [Auradou 2005, pp. 10-10，参考文献涉及弥散]。

## Source Coverage
本文档编译自论文全部索引片段。共处理 **13** 个非空源块，总字符数约 61,119。片段覆盖率为 100%（按块）和 100.5%（按字符，因编译后可能包含少量格式化字符）。索引策略为单次编译（single-pass-markdown），无遗漏或幻觉内容。所有引用均源自索引片段内原文标注。
