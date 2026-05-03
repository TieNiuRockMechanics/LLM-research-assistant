---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2022-jiang-fracture-activation-and-induced-seismicity-during-long-term-heat-production-in-fractu"
title: "Fracture Activation and Induced Seismicity During Long-Term Heat Production in Fractured Geothermal Reservoirs."
status: "draft"
source_pdf: "data/papers/2022 - Fracture Activation and Induced Seismicity During Long-Term Heat Production in Fractured Geothermal Reservoirs.pdf"
collections:
  - "part5-3"
citation: "Jiang, Chuanyin, et al. \"Fracture Activation and Induced Seismicity During Long-Term Heat Production in Fractured Geothermal Reservoirs.\" *Rock Mechanics and Rock Engineering*, vol. 55, 2022, pp. 5235-5258. https://doi.org/10.1007/s00603-022-02882-z."
indexed_texts: "19"
indexed_chars: "91144"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T10:41:46"
---

# Fracture Activation and Induced Seismicity During Long-Term Heat Production in Fractured Geothermal Reservoirs.

## One-line Summary
本研究通过全耦合热‑水‑力学模型，系统揭示了长期热采过程中原位应力状态、注入压力与温度如何通过竞争机制控制二维离散裂缝网络中的裂缝激活和诱发地震的时空演化 [Jiang 2022, pp. 1‑2]。

## Research Question
长期（数年尺度）热生产期间，注入流体的加压和冷却如何与原位应力场耦合，驱动裂缝型地热储层中的裂缝剪切滑移与地震活动？不同应力背景下，加压与热效应对地震事件的触发时间、数量、震级及空间分布的相对贡献如何？[Jiang 2022, pp. 1‑2, 6‑7, 9‑10]

## Study Area / Data
本研究为概念性数值模拟研究，非特定场地案例。模型参数取文献典型值：目标储层埋深3000 m，覆岩应力S_v = 79.4 MPa（岩石密度2700 kg/m³），初始储层温度T₀ = 220 °C，初始孔隙压力p₀ = ρ_w g H = 29.4 MPa。考察三种差应力状态：最小水平应力固定为S_y = 0.8 S_v，最大水平应力分别取S_x = S_v、1.3 S_v、1.6 S_v。模拟了三个宏观水力梯度（注入‑产出井压差）和两种注入温度（分别对应ΔT = 100 °C和200 °C的温度下降）[Jiang 2022, pp. 5‑6]。

## Methods
- **数值框架**：基于有限元方法（COMSOL Multiphysics®）构建全耦合热‑水‑力学（THM）模型 [Jiang 2022, pp. 5]。
- **储层描述**：采用离散裂缝网络（DFN）方法表示天然裂缝系统，基质渗透率远低于裂缝，流动受裂缝网络控制；裂缝开度遵从应力依赖的立方定律 [Jiang 2022, pp. 3‑5]。
- **控制方程**：岩石基质变形为小应变热‑孔弹性；单相达西流描述基质与裂缝中的流体运动；基于局部热平衡假设实现裂缝‑基质换热；详细方程见原文 [Jiang 2022, pp. 3‑5]。
- **地震模拟**：持续监测所有裂缝段的滑移和潜在能量释放，据此计算地震活性与震级（矩震级M_w）[Jiang 2022, pp. 5]。
- **模拟阶段**：先进行原位应力初始化，再施加注入井与生产井之间的压力差及温度差，模拟长期热采过程中的流动‑传热‑变形耦合 [Jiang 2022, pp. 5‑6]。

## Key Findings
1. **原位应力背景控制**：差应力状态决定了裂缝系统的初始临界性。低差应力（S_x = S_v）下，裂缝远离临界状态；高差应力（S_x = 1.6 S_v）下，大量裂缝已处于临界滑动状态 [Jiang 2022, pp. 7, 9‑10]。
2. **加压与热效应的竞争**：注入诱导的流体加压在早期起主导作用，而低温流体注入引起的热收缩在后期驱动裂缝激活；低差应力时激活由后期热抽采主导，高差应力时早期加压已引发大量滑移 [Jiang 2022, pp. 6‑7, 9]。
3. **温度对地震时序与震级的影响**：低差应力条件下，只有当温差ΔT达到200 °C时才触发显著地震，且注入温度控制事件的时间、震级与数量；高差应力条件下，ΔT = 100 °C即可产生明显热效应，但热效应一般不改变早期加压触发事件的时间，主要影响震级分布 [Jiang 2022, pp. 9‑10]。
4. **裂缝激活对压力梯度敏感**：裂缝激活对注入压力梯度的变化敏感，而注入温度则主要影响热抽采引起的二次地震事件的震级，通常不改变其时间和数量 [Jiang 2022, pp. 1, 9]。
5. **流动结构与通道化**：随应力比增大，裂缝开度差异加剧，导致更强烈的流动局部化（流量通道化密度d_Q减小），并形成更尖锐的热锋。后期剪切扩容进一步改变主流通道分布 [Jiang 2022, pp. 7‑9]。
6. **空间分布**：大震级事件主要集中在注入井近场及主要流动通道沿线 [Jiang 2022, pp. 9‑10]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 低差应力 (S_x=S_v) 下，早期 (t≤10⁶ s) 仅约0.2%裂缝激活；至 t=10⁷ ‑ 10⁸ s 热锋推进时激活区域显著扩大，热应力是关键驱动力。 | [Jiang 2022, pp. 6‑7] | p_in=34.6 MPa, T_in=120 °C; 2D DFN模型，含30°和110°两组裂缝 | 加压与热效应的竞争在此条件下由热效应主导。 |
| 高差应力 (S_x=1.6S_v) 下，相同水力条件，早期 (t≤10⁶ s) 已有约15%裂缝激活，主要由流体加压触发。 | [Jiang 2022, pp. 7] | 同上压力和温度条件 | 表明临界应力状态对加压高度敏感。 |
| 在 S_x=1.6S_v 时，ΔT=0 °C 等温情形下频率‑震级分布尾部下降平缓；ΔT≥100 °C 时出现急剧下降，热效应改变了地震统计特征。 | [Jiang 2022, pp. 9‑10] | 高差应力，不同注入温度对比 | 热应力影响主要反映在震级分布上。 |
| 流量通道化密度 d_Q 随应力比 S_x/S_y 增大而减小，如从 S_x=1.3S_v 到 1.6S_v 时流动局部化加强。 | [Jiang 2022, pp. 8‑9] | 非等温注入，热采进行至10⁷‑10⁸ s | d_Q 越小表示主通道间距越大，流动越集中。 |
| 当 S_x=S_v 时，ΔT=100 °C 仅使频率‑震级曲线小幅右移；ΔT=200 °C 则大幅提高事件数量和震级。 | [Jiang 2022, pp. 9‑10] | 低差应力，不同注入温度 | 低温差下热效应阈值为~200 °C。 |

## Limitations
索引片段未明确讨论研究局限。根据文中给出的方法假设（见 Assumptions / Conditions），模型限定于单相饱和流、二维离散裂缝网络、小应变热弹性和局部热平衡，且基质渗透率极低；这些条件可能使结果不适用于存在非均质基质渗流或三维流路径的场合。实际储层的非均质性、多相流、化学作用等均未被纳入，对长期地震风险的预测能力尚待验证。

## Assumptions / Conditions
- 储层由多孔基质和离散裂缝组成，基质渗透率远低于裂缝，流动由裂缝网络控制 [Jiang 2022, pp. 3]。
- 初始完全饱和单相水，流体与工作介质相同，满足单相达西流 [Jiang 2022, pp. 3]。
- 基质与裂缝中的水之间基于局部热平衡进行热交换 [Jiang 2022, pp. 3]。
- 岩石基质视为弹性，遵循小应变热‑孔弹性本构 [Jiang 2022, pp. 3‑4]。
- 裂缝力学行为采用线弹性本构，开度随有效正应力变化，渗透率依立方定律更新 [Jiang 2022, pp. 4‑5]。
- 模拟深度3000 m，参考应力、温度、孔隙压力基于静水柱和密度假设 [Jiang 2022, pp. 5]。
- 仅考虑长期热采阶段，忽略短期水力压裂增产过程，因此注入‑产出井压差维持在较低水平 [Jiang 2022, pp. 6]。
- 研究为通用参数化研究，未针对特定场地校准 [Jiang 2022, pp. 5]。

## Key Variables / Parameters
- **原位应力**：S_v（垂向），S_x、S_y（最大、最小水平应力），应力比 S_x/S_y 或差应力水平 [Jiang 2022, pp. 5]。
- **注入参数**：注入压力 p_in，压力差 Δp = p_in ‑ p_out，注入温度 T_in，温度降 ΔT = T₀ − T_in [Jiang 2022, pp. 5‑6]。
- **裂缝几何与力学**：初始开度 b₀，法向刚度 K_n，剪切刚度，摩擦角，裂缝组产状（30°与110°）[Jiang 2022, pp. 5‑6]。
- **输送属性**：裂缝渗透率 κ_f（与开度立方相关），流体压缩系数 χ_w，基质导热系数等 [Jiang 2022, pp. 4‑5]。
- **地震指标**：单个裂缝段滑移距离，矩震级 M_w，事件数量，频率‑震级分布 [Jiang 2022, pp. 5, 9‑10]。
- **流动结构指标**：流量通道化密度 d_Q [Jiang 2022, pp. 8]。
- **热力学参数**：热膨胀系数 α_T，比热容，导热系数 [Jiang 2022, pp. 4‑5]。
- **弹性参数**：杨氏模量 E，泊松比 ν，Biot 系数 α_B [Jiang 2022, pp. 4]。

## Reusable Claims
- **Claim 1**：在低差应力状态（S_x ≤ S_v）下，裂缝型地热储层的长期地震活动主要由热抽采阶段的温度下降驱动，而非注入流体加压。只有当注入流体与储层的温差足够大（如ΔT≥200 °C）时，才会触发数量可观且震级偏大的地震事件 [Jiang 2022, pp. 6‑7, 9‑10]。  
  *适用条件*：临界应力状态远离破坏包络线，水力梯度适中，裂缝网络具有特定优势方位。  
  *限制*：基于二维DFN‑THM概念模型，基质渗透率极低，假设单相流和局部热平衡；未考虑真实储层非均质性与三维效应。

- **Claim 2**：在高差应力状态（如S_x = 1.6S_v）下，早期流体加压即足以激活大量临界应力裂缝，地震事件在注入早期集中发生一次或两次；后续热收缩对震级分布有显著影响，但一般不改变加压触发的初始事件时间 [Jiang 2022, pp. 7, 9]。  
  *适用条件*：裂缝系统处于或接近临界滑动状态，裂缝方位有利于剪切活化，压力梯度与注入压力水平相似。  
  *限制*：同上。另外，忽略水力压裂增产阶段可能改变裂缝网络连通性的影响。

- **Claim 3**：裂缝激活对注入压力梯度的变化比对注入温度的变化更敏感。在热抽采阶段，注入温度主要影响二次热诱发地震的震级，而对这些事件的发生时间和次数影响有限 [Jiang 2022, pp. 1, 9]。  
  *适用条件*：热采阶段已经在稳定流动状态下进行，裂缝渗透率主要受力学和热应力共同作用。  
  *限制*：以上结论源于有限组参数对比，且压力梯度和温度范围受限于通用参数设定，推广到实际工程需谨慎。

- **Claim 4**：应力状态通过影响裂缝开度差异控制流动通道化程度：应力比越高，开度各向异性越强，导致更集中的流动通道和更尖锐的热锋，进而影响地震事件的空间聚类 [Jiang 2022, pp. 7‑9]。  
  *适用条件*：两组相交裂缝网络，且优势方向与主应力方位匹配。  
  *限制*：裂缝网络几何固定，未考虑裂缝延伸或新裂缝生成过程。

## Candidate Concepts
[[fracture activation]], [[induced seismicity]], [[discrete fracture network (DFN)]], [[thermal-hydro-mechanical coupling]], [[Mohr-Coulomb failure criterion]], [[heat production]], [[critical stress state]], [[flow channeling]], [[shear dilation]], [[enhanced geothermal system (EGS)]], [[thermo-poro-elasticity]], [[cubic law fracture permeability]]

## Candidate Methods
[[fully coupled THM model]], [[finite element method (COMSOL)]], [[DFN-based flow and deformation modeling]], [[single-phase Darcy flow]], [[local thermal equilibrium assumption]], [[stress-dependent fracture aperture]], [[moment magnitude estimation]], [[Mohr’s circle analysis]]

## Connections To Other Work
- 本文在引言中明确指出，之前大量物理实验（Giorgetti et al. 2019; Guglielmi et al. 2015）和数值模拟（Cappa et al. 2018; Deng et al. 2016, 2020; Rutqvist et al. 2013, 2015; Ucar et al. 2017）揭示了耦合HM过程对注入诱发断层滑移和地震的控制，经典莫尔‑库仑理论可用于解释 [Jiang 2022, pp. 2‑3]。
- 文章还提及热应力的作用，引用 Blöcher et al. 2018、Gan and Lei 2020 等研究，指出热效应对有效正应力的削弱可加速断层激活并提高震级 [Jiang 2022, pp. 2‑3]。
- 从主题上，本文可连接到 [[hydro-mechanical coupling in geothermal reservoirs]]、[[poroelastic stress changes]]、[[rate-and-state fault friction]]（虽未在片段中直接采用，但属于研究地震统计的延伸方向）以及由[[cold water injection]]引起的热弹性收缩等概念。

## Open Questions
未从索引片段中确认。片段未列出文章明确提出的开放性问题或后续研究方向。

## Source Coverage
本页依据19个索引片段，覆盖了论文摘要、引言（部分背景与动机）、方法框架（控制方程、假设、数值实现）、模型设置（应力条件、温度、压力梯度）、以及结果与讨论中的核心发现（不同应力比下裂缝激活时序、地震频率‑震级分布变化、流动通道化表征）。片段缺失内容可能包括：完整的参数敏感性分析、模型验证的详细结果（附录部分）、对长期热能产出的定量分析、深入的机理讨论和图表（如Mohr圆分析细节）、以及结论部分。受限于片段采样，部分量化关系（如精确的压力‑温度组合下的累计地震矩）与全文结论可能未被完全捕捉。
