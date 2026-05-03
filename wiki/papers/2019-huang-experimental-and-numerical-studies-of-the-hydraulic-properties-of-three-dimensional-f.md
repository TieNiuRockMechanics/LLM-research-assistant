---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-huang-experimental-and-numerical-studies-of-the-hydraulic-properties-of-three-dimensional-f"
title: "Experimental and Numerical Studies of the Hydraulic Properties of Three-Dimensional Fracture Networks with Spatially Distributed Apertures."
status: "draft"
source_pdf: "data/papers/2019 - Experimental and Numerical Studies of the Hydraulic Properties of Three-Dimensional Fracture Networks with Spatially Distributed Apertures.pdf"
collections:
citation: "Huang, Na, et al. \"Experimental and Numerical Studies of the Hydraulic Properties of Three-Dimensional Fracture Networks with Spatially Distributed Apertures.\" *Rock Mechanics and Rock Engineering*, vol. 52, 2019, pp. 4731-4746. doi:10.1007/s00603-019-01869-7."
indexed_texts: "13"
indexed_chars: "64881"
nonempty_source_blocks: "13"
compiled_source_blocks: "13"
compiled_source_chars: "64284"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.990799"
coverage_status: "full-index"
source_signature: "ee7d3f51559e3edccb8449590f3d0694554fb43a"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T00:26:22"
---

# Experimental and Numerical Studies of the Hydraulic Properties of Three-Dimensional Fracture Networks with Spatially Distributed Apertures.

## One-line Summary
通过透明树脂三维裂隙网络模型的流动实验与数值模拟，揭示了裂隙开度空间非均质性（正态与对数正态分布）诱发的优势通道流对渗透率的影响，并提出了对数正态分布截断阈值的临界表达式，该表达式可推广到复杂密集离散裂隙网络。

## Research Question
裂隙开度的空间非均质性如何影响三维（3D）裂隙网络中的流动通道化及等效渗透特性？如何确定对数正态开度分布在实际裂隙岩体模拟中合理的截断阈值？

## Study Area / Data
- **物理模型**：利用五轴数控机床（VC‑X350，分辨率0.05 mm，公差0.006 mm）加工透明树脂，构建一个尺寸为200 × 100 × 100 mm的稀疏三维裂隙网络样品，包含5个裂隙段（segment 1‑5），其表面粗糙度用节理粗糙度系数（JRC）量化，各段平均JRC依次为4.16、3.15、2.91、6.48、4.97[Huang 2019, pp. 3-5]。裂隙开度服从截断正态分布（均值为0.804 mm，偏差为0.317），并在场中分布少数接触点（零开度）[Huang 2019, pp. 3-4]。
- **数值参数研究模型**：
  - 稀疏裂隙网络：开度服从正态分布，均值eₘ = 0.5, 1.0, 2.0 mm，偏差σ = 0.5, 1.0, 1.5, 2.0[Huang 2019, pp. 9-10]。
  - 稀疏/密集离散裂隙网络（DFN）：开度服从对数正态分布，对数均值u = 0.5, 1.0, 2.0 mm，对数标准差σf = 0.1, 0.5, 1.0[Huang 2019, pp. 10-12]；DFN模型生成时，裂隙位置和产状服从均匀分布，裂隙长度服从幂律分布（幂指数a = 2.0, 10 ≤ l ≤ 15 m），裂隙数量n从5至30，开度服从对数正态分布（0 < u ≤ 3.0，0 < σf ≤ 1.0）[Huang 2019, pp. 12-13, Table 3]。
- **流动实验数据**：9种不同进出口组合（如inlet_1&2‑outlet_1&2等）下的水力梯度i与流量Q关系，实测流量范围0.39×10⁻⁵–5.60×10⁻⁵ m³/s，采用蒸馏水（密度998.2 kg/m³，黏度0.001 Pa·s，20 ℃）[Huang 2019, pp. 5-6, Table 1]。

## Methods
- **物理模型制造**：采用改进的逐次随机添加（SRA）算法生成裂隙表面的粗糙形貌，通过三维CAD建模软件生成裂隙网络实体并分割为四个块体，利用五轴数控铣削加工透明树脂块体，最后组装并以玻璃夹套固定密封[Huang 2019, pp. 3-4]。
- **流动可视化与测量**：配备CCD相机（30帧/秒）实时捕捉染色水流（红色食用色素，浓度5 g/L）在裂隙中的流动图像；用注射泵（精度±0.001 mL/min）控制恒定流量，电子天平（精度±0.01 g）测量流出量，差压计（精度±10 Pa）记录水头损失[Huang 2019, pp. 5-6]。
- **数值模拟**：基于Reynolds方程（局部立方定律）模拟单个裂隙内的稳定流，在裂隙交线处施加连续性条件（水头相等与流量守恒）；采用Galerkin法求解，利用Huang et al.（2018）开发的代码离散裂隙网络模型；根据Forchheimer定律（i = AQ + BQ²）反算线性流阶段的等效渗透率K = μ/(AρgAₛ)[Huang 2019, pp. 6-7]。
- **参数分析**：对于正态分布开度，对比平行板模型与空间变开度模型的渗透率比K/K₀；对于对数正态分布，定义η = Kₜ/Kc（Kₜ为截断分布下的渗透率，Kc为完全对数正态分布下的渗透率），考察η随截断阈值eₜ的变化，回归给出临界阈值e_c（η = 0.9处的eₜ）的数学表达式[Huang 2019, pp. 9-12]。

## Key Findings
1. **五轴加工制造的有效性**：五轴数控铣削可以精确制造具有空间分布开度的三维裂隙网络透明样品，CCD直接可视化观察到明显的优势流通道[Huang 2019, pp. 7, 13]。
2. **流动非线性与渗透率一致性**：实测i‑Q关系呈二次非线性，符合Forchheimer方程；9组不同进出口条件下的数值模拟等效渗透率与实验结果的相对偏差r₁全部小于10%（例：inlet_2‑outlet_1时Kₑ=1.51×10⁻¹⁰ m²，Kₛ=1.53×10⁻¹⁰ m²，r₁=1.32%），验证了数值方法的可靠性[Huang 2019, pp. 7-9, Table 1]。
3. **正态分布开度下的流动通道化**：
   - 随均值eₘ减小和/或标准差σ增大，接触比增大，流体局部化增强；优势流通道仅占裂隙平面面积的26% – 67%，但输送了90%以上的流量[Huang 2019, pp. 9-10]。
   - 空间变开度模型的等效渗透率低于相同均值的平行板模型（K/K₀ < 1），差异随eₘ减小而增大；当σ增大时，K/K₀可能增大或减小，取决于大通道和小阻力区域的相对宏观流向方位[Huang 2019, pp. 10, 图9b]。
4. **对数正态开度分布的截断效应**：
   - η = Kₜ/Kc随截断阈值eₜ先显著上升，随后趋于1.0；临界截断阈值e_c（η = 0.9）受u和σf控制，其回归表达式为：«ec = 0.77u^{1.34} 3.95 / σ_f»（未考虑量纲，因属回归函数；R² = 0.989）[Huang 2019, pp. 10-12, Table 2, Fig. 12]。
   - 将该表达式应用于裂隙数n=5–30的密集DFN模型，η‑eₜ演化趋势与稀疏网络相似，模拟的e_c与预测值吻合良好（R² = 0.977），证明表达式可准确评价复杂三维裂隙网络的合理截断阈值[Huang 2019, pp. 12-13, Fig. 15]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 相对误差r₁<10%（9种进出口组合） | Huang 2019, pp. 7-9, Table 1 | Q范围0.39×10⁻⁵–5.60×10⁻⁵ m³/s，树脂裂隙网样品 | 验证数值代码的有效性 |
| 优势通道面积占比Rf=26%–67%（正态开度模型） | Huang 2019, pp. 9-10, Fig. 9a | eₘ=0.5–2.0 mm, σ=0.5–2.0 | 通道判定标准：单元局部流量占比>0.005 |
| K/K₀<1，且随eₘ增大而增大 | Huang 2019, pp. 10, Fig. 9b | 正态分布开度，平行板参考模型 | 平行板模型高估渗透率 |
| η=Kₜ/Kc随eₜ先陡增后稳定趋近1 | Huang 2019, pp. 10-12, Fig. 11 | u=0.5,1.0,2.0 mm; σf=0.1,0.5,1.0 | 通用行为，与参数无关 |
| ec = 0.77 u^{1.34} 3.95 / σ_f，R²=0.989 | Huang 2019, pp. 12, Table 2, Fig. 12 | 稀疏裂隙网，对数正态开度 | 临界阈值定义η=0.9 |
| 密集DFN模型（n=5–30）中ec预测R²=0.977 | Huang 2019, pp. 12-13, Fig. 15 | 裂隙长度幂律分布a=2.0，开度对数正态 | 证明表达式的可扩展性 |

## Limitations
- 实验仅制作了一个稀疏裂隙网络样品，因此参数研究主要依赖经实验验证的数值模型[Huang 2019, pp. 9]。
- 实验中未直接测试线性流动阶段，因为极低水压下测量精度的限制，i‑Q关系均在非线性流动区域拟合获得A、B系数[Huang 2019, pp. 7]。
- 示踪实验仅用于可视化流道，未系统分析溶质突破时间和润湿表面积[Huang 2019, pp. 14]。
- 数值模拟中Reynolds方程适用于低Re数流动，虽实验中出现非线性流动，但建模仍以局部立方定律为基础，未直接求解Navier–Stokes方程[Huang 2019, pp. 6]。

## Assumptions / Conditions
- 裂隙内流体为不可压缩、均质（蒸馏水）且等温（20 °C）[Huang 2019, pp. 5]。
- 裂隙壁面接触点处理为光滑平行面，接触区开度设为零[Huang 2019, pp. 3-4, 9]。
- 对于正态分布开度，所有负开度被设置为零以表示接触；对于对数正态分布，采用截断分布时eₜ以下的部分保留原分布，零接触另外设定[Huang 2019, pp. 9-10]。
- 数值流模拟基于Reynolds方程（局部立方定律），并在裂隙交线施加水头连续和流量守恒条件，忽略惯性项对裂隙交汇处的影响[Huang 2019, pp. 6-7]。
- 密集DFN模型生成时，裂隙位置和产状为均匀分布，长度服从幂律分布a=2.0，忽略基质渗透性[Huang 2019, pp. 12-13, Table 3]。
- 等效渗透率K依据Forchheimer关系中的黏性项系数A反算，适用于线性流动占优的低Re数区域[Huang 2019, pp. 6]。

## Key Variables / Parameters
- **裂隙开度分布**：正态分布参数eₘ (均值)、σ (标准差)；对数正态分布参数u (对数均值)、σf (对数标准差)；截断阈值eₜ及临界阈值ec[Huang 2019, pp. 3-4, 9‑12]。
- **几何参数**：模型尺寸、裂隙段表面JRC、接触比（接触面积/裂隙总面积）[Huang 2019, pp. 3-4, Fig. 7d]。
- **水力参数**：流量Q、水力梯度i、Forchheimer系数A和B、等效渗透率K（KE、KS）、渗透率比K/K₀、η=Kₜ/Kc[Huang 2019, pp. 6-7, Table 1, Figs. 9b, 11]。
- **优势流描述**：优势通道面积占比Rf（单元局部流量占比>0.005的区域面积/总裂隙面积）[Huang 2019, pp. 9-10]。

## Reusable Claims
1. **制造方法**：五轴数控铣削结合透明树脂材料可制备具有精确空间分布开度的三维裂隙网络样品，并实现流场的直接可视化。**条件**：需将裂隙模型分割为可加工块体，且块体间通过接触点对齐粘合；适用于稀疏到中等复杂度的裂隙网络[Huang 2019, pp. 3-4, 13]。
2. **流动沟道化判据**：当裂隙开度场偏离均匀分布较强时（小均值、大标准差），优势流通道仅占裂隙平面的26%–67%，但传递>90%的流量；该比例可用于量化流动非均匀性[Huang 2019, pp. 9-10]。**局限**：该数值基于二维裂隙面网格，且阈值0.005是基于单一样品和特定边界条件。
3. **渗透率低估与平行板高估**：对于正态分布开度，空间变开度模型的等效渗透率总低于相同均值的平行板模型（K/K₀ < 1）；差异随均值减小而增大，而随标准差变化方向取决于通道与障碍的流向配置[Huang 2019, pp. 10]。**适用**：层流、低Re数，裂隙壁接触点光滑处理。
4. **对数正态截断阈值效应**：采用截断对数正态分布时，渗透率比η随eₜ增大先迅速上升后趋于1。以η=0.9定义的临界截断阈值ec可用经验式ec = 0.77 u^{1.34} 3.95 / σ_f（未考虑量纲）描述，该式可应用于具有幂律长度分布的复杂密集DFN模型，决定合理的截断值以避免高估或低估渗透率[Huang 2019, pp. 11-13]。**条件**：裂隙网络的连通性足够好，开度场由给定的u和σf产生。

## Candidate Concepts
- [[fracture network]]  
- [[aperture distribution]]  
- [[channeling flow]]  
- [[critical truncation threshold]]  
- [[normal and lognormal distributions of fracture apertures]]  
- [[preferential flow paths]]  
- [[equivalent permeability]]  
- [[Forchheimer’s law]]  
- [[discrete fracture network (DFN)]]  
- [[five-axis machining transparent fracture model]]  
- [[local cubic law (Reynolds equation)]]  
- [[fracture intersection continuity conditions]]  
- [[contact ratio]]  

## Candidate Methods
- [[modified successive random additions (SRA) for rough fracture surfaces]]  
- [[five-axis CNC machining of transparent resin fracture networks]]  
- [[CCD camera dye-tracing flow visualization]]  
- [[Galerkin finite element discretization of Reynolds equation in fracture networks]]  
- [[truncated normal and lognormal aperture field generation using COVAR code]]  
- [[multivariable regression for critical truncation threshold expression]]  
- [[upscaling from sparse to dense DFN models with power-law length distributions]]  

## Connections To Other Work
- 对单裂隙开度测量的现场方法（核磁共振、CT扫描）表明开度场可用正态或对数正态描述（Brown et al., 1986; Keller, 1998; Lee et al., 2003等），本文在此基础上定量分析了分布参数对网络渗流的影响[Huang 2019, pp. 3, 9‑10]。
- Baghbanan & Jing (2007) 等指出对数正态分布的截断阈值常被任意选取，可能引入不确定性；本研究首次提出基于物理的临界截断阈值关系式，并验证了其在密集DFN中的可扩展性[Huang 2019, pp. 3, 12‑13]。
- 文中提及的流动通道化与前人关于优势通道控制渗流的观点一致（Black et al., 2017; Dessirier et al., 2018），但通过可视化实验直接展示了三维网络中的流径[Huang 2019, pp. 2, 7‑8]。
- 数值代码验证参照了Huang et al. (2016, 2018) 的离散裂隙网络流计算方法[Huang 2019, pp. 6-7]。

## Open Questions
- 未分析非均质开度对溶质突破时间和润湿面积的影响，计划未来系统研究[Huang 2019, pp. 14]。
- 裂隙密度、长度、开度各向异性等多种几何参数的耦合作用尚需实验与数值联合研究[Huang 2019, pp. 14-15]。
- 对数正态截断表达式的普适性是否适用于剪切错动引起的开度演化及应力相关条件下的裂隙网络，未验证。
- 本实验中测试的Re数范围及非线性流动向线性流动的过渡行为未直接测定，未来可改进测量精度以覆盖全流态。

## Source Coverage
所有13个非空索引碎片均已处理，总索引字符数64881，其中非空源块13个、编译源块13个、编译源字符64284。覆盖率（以块计）1.0，覆盖率（以字计）≈0.9908。
