---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2018-lang-relationship-between-the-orientation-of-maximum-permeability-and-intermediate-principa"
title: "Relationship Between the Orientation of Maximum Permeability and Intermediate Principal Stress in Fractured Rocks."
status: "draft"
source_pdf: "data/papers/2018 - Relationship Between the Orientation of Maximum Permeability and Intermediate Principal Stress in Fractured Rocks.pdf"
collections:
citation: "Lang, Philipp S., et al. \"Relationship Between the Orientation of Maximum Permeability and Intermediate Principal Stress in Fractured Rocks.\" *Water Resources Research*, vol. 54, 2018, pp. 8734-8755. doi:10.1029/2018WR023189. Accessed 2026."
indexed_texts: "21"
indexed_chars: "100524"
nonempty_source_blocks: "21"
compiled_source_blocks: "21"
compiled_source_chars: "100962"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004357"
coverage_status: "full-index"
source_signature: "019adf7bc92c1fa0b267185b2a6ff6dfed9024f9"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T21:10:15"
---

# Relationship Between the Orientation of Maximum Permeability and Intermediate Principal Stress in Fractured Rocks.

## One-line Summary

通过三维多尺度数值模型证明，在各向同性裂隙网络中，最大渗透率方向倾向于与中间主应力方向对齐，其机理是裂隙在最大 – 最小主应力平面内发生最强滑动，而单裂隙的透水率在垂直于滑移方向具有显著各向异性的优势通道。

## Research Question

研究在三轴压缩应力作用下，裂隙岩体的渗透率主方向如何受单裂隙剪切诱导的各向异性透水率控制，并澄清最大渗透率方向与远端主应力（特别是中间主应力）之间的物理关系。

## Study Area / Data

该方法通过三组已发表的室内实验进行验证：
- Bandis (1980) 板岩裂隙闭合及剪切实验
- Watanabe et al. (2008) 饭馆花岗岩诱导裂隙的围压–渗流实验
- Nemoto et al. (2009) 相同条件下接触面积直接测量数据  
所有实验均使用新鲜诱导且无载荷下剪切的裂隙，以保留原始表面粗糙度。  
在系统研究中，构建了单裂隙、共轭裂隙对以及 265 个统计等价的离散裂隙网络模型（每个模型含 8 条圆盘形裂隙，粒径分布服从指数为 −2.0 的幂律，半径截断 6.66–20.0 m），模型域边长 10 m（单、共轭裂隙）和 40 m（网络），内部设置渗透性子采样域 Ω 以消除边界效应。

## Methods

1. **双尺度耦合框架**  
   - **网络尺度**：裂隙视为平面不连续面，基于线性弹性均质模型和摩擦库仑定律（μ = 0.6），采用非结构化二次四面体网格及基于间隙的增广拉格朗日方法求解摩擦接触问题，获得每条裂隙的平均法向接触压力 (圧) 和平均剪切位移 (𝛿̄T)。  
   - **裂隙尺度**：为每条裂隙生成两片自仿射粗糙表面（H = 0.8，包含失配波长 λm），根据 (圧) 和 (𝛿̄T) 偏移后，在方形网格上通过 FFT 加速的共轭梯度法求解无摩擦弹性接触，得到机械隙宽场。  
2. **单裂隙流动模拟**  
   在裂隙平面上求解雷诺润滑方程，获得平行和垂直于剪切方向的透水率分量 (K∥, K⟂)，构成对角透水率张量。  
3. **等效渗透率计算**  
   将各裂隙的透水率张量反馈到网络尺度，采用有限元法求解基质–裂隙系统的单相不可压缩稳态流动，并在子采样域中进行压力梯度和流量的体积加权最小二乘平均，得出等效渗透率张量 (k)，基质渗透率取 1 mD。  
4. **假设的开启–闭合过程**  
   先施加初始流体压力 pf = 0.9 S3 使裂隙张开，然后卸除流体压力并施加三轴压缩 (S1 > S2 > S3)，模拟裂隙从张开到接触的力学历程。

## Key Findings

- **单裂隙各向异性**：剪切位移导致透水率在垂直剪切方向显著增大，各向异性比 (ah,⟂/ah,∥) 随相对剪切位移 (δ′T = δT/L) 和围压的增加而增大（最高约 1.625）。归一化剪切位移是比绝对位移更重要的控制参数。  
- **裂隙刚度与透水率不唯一对应**：两条尺寸不同但绝对剪移相同的裂隙具有相同的法向刚度，但其透水率及其各向异性比并不相同，说明刚度不能作为透水率的唯一指标。  
- **单裂隙取向效应**：嵌入基质中的单裂隙，当倾角 β ≈ 60° 时（对应临界取向附近）水力隙宽达到最大，证实了“临界取向裂隙最可能形成高导水通道”的已有认识。  
- **共轭裂隙对行为**：固定夹角 60° 的两条共轭裂隙，其中间主渗透率方向会偏向具有更大剪切位移和更低压缩的分支，当对称轴倾角 β ≈ 60° 时，岩体渗透率比无滑移状态高约 3 个数量级。  
- **裂隙网络结果**：265 个随机各向同性裂隙网络统计显示，**整体最大渗透率方向 (kmax) 明显倾向与中间主应力 S2 对齐**；仅有少数被个别裂隙主导的案例中 kmax 会偏离 S2，且这些案例对应的渗透率往往更低。该结果与 Sibson (1996) 的现场观测一致。

## Core Evidence Table

| 证据 | 出处 | 条件 | 备注 |
|------|------|------|------|
| kmax 取向与 S2 对齐 | 265 个网络模型 | 各向同性裂隙网络，SV > SH > Sh，μ = 0.6，应力比 S1/S3 = 3.1 | 当个别裂隙主导时，kmax 可能偏向 S3，渗透率降低约 1/3 |
| 单裂隙各向异性比 ah,⟂/ah,∥ 最高约 1.625（δT = 3 mm，压力至 50 MPa） | δT = 3 mm 模型，Watanabe et al. 参数 | 花岗岩，E = 29.4 GPa，ν = 0.15 | 渗透率比值为 (1.625)² |
| 水力隙宽最大值出现在 β ≈ 60–67° | 单裂隙旋转模型 | L = 5 m，S1/S3 = 3.1 | 最大剪移出现在 52–60°，受压缩减小影响，水力隙宽峰值稍向后移 |
| 共轭裂隙对在 β = 60° 时整体渗透率较无剪移高约 3 个数量级 | 共轭裂隙对模型 | 裂隙夹角 60°，L = 5 m，域 10 m | kmed 在 x − z 平面内旋转 |
| 裂隙法向刚度呈线性增长，反映接触面积随压力线性变化 | δT = 3 mm 模型 | 粗糙表面弹性接触理论预期 | 线性关系延续至 50 MPa |
| 相同 δT 但不同裂隙尺寸（L = 250 和 500 mm）的刚度相等，透水率及各项异性比不等 | L = 250，500 mm 模型 | hrms = 0.01 LH，δT ≈ 4 mm | 证明刚度不能唯一映射为透水率 |
| 归一化水力隙宽 a′h 在 S1–S3 平面内取极大值 | 265 个网络统计 | 幂律裂隙尺寸，指数 −2.0 | 与临界取向裂隙的导水优势一致 |
| 裂隙接触斑尺寸分布呈幂律，斜率与实验（Nemoto et al.）一致 | 数值模型 vs 压力敏感胶片 | 花岗岩，δT = 3 mm，p = 10 MPa | 良好定性吻合 |

## Limitations

- 假设裂隙在剪切过程中表面不发生损伤；天然裂隙大位移可能改变粗糙度频谱及各向异性。  
- 摩擦系数固定为 0.6，基质为线弹性各向同性，未考虑塑性、非均质或孔隙弹性效应。  
- 网络规模较小（8 条裂隙），应力比单一，结论的普适性有待更大规模参数化研究。  
- 未考虑化学溶解、沉淀、胶结等过程，仅适用于“应力主控”的裂隙渗透率系统。  
- 渗透率计算采用等效渗透率而非有效渗透率，单次实现的离散度较大（跨 3 个数量级）。

## Assumptions / Conditions

- 裂隙为平面圆盘，网络尺度接触基于摩擦库仑定律（μ = 0.6）。  
- 单裂隙尺度假设无摩擦弹性接触，采用刚性复合表面与等效弹性半空间的简化模型。  
- 裂隙表面为自仿射（H = 0.8），复合表面包含失配波长 λm，以复现无剪切时的残余渗透性。  
- 基质为各向同性线弹性多孔介质，渗透率 k_matrix = 1 mD。  
- 应力条件为三轴压缩，主应力方向与模型边界一致，SV > SH > Sh。  
- 假设裂隙经历“初始流体张开→卸除流体压力→三轴压缩接触”的加载路径。  
- 用于验证的所有实验均属于新鲜裂隙、无载荷下剪切的情形，以保证粗糙度不被严重改变。

## Key Variables / Parameters

- 裂隙特征尺寸 L，粗糙度参数 (hrms, H)，失配波长 λm  
- 归一化剪切位移 δ′T = δT/L  
- 平均接触压力 (圧) 及其归一化 (圧)/S1  
- 裂隙透水率张量 K = diag(K∥, K⟂, 0)  
- 水力隙宽 ah，各向异性比 ah,⟂/ah,∥  
- 接触比 Rc（真实接触面积/名义面积）  
- 裂隙对称轴倾角 β（相对 S2‑S3 平面）  
- 远端主应力大小 S1, S2, S3，应力比 S1/S3  
- 摩擦系数 μ，弹性参数 E, ν，约化模量 E*  
- 等效渗透率张量 k，其最大特征值方向 nkmax

## Reusable Claims

- 当裂隙因剪切位移产生显著各向异性透水率（K⟂ > K∥）时，各向同性裂隙网络的最大渗透率方向倾向于与中间主应力方向对齐。[[Lang et al. 2018]]*  
- 单裂隙透水率的各向异性比随归一化剪切位移 δ′T 的增大而单调增大，同时围压升高会进一步放大各向异性。[[Lang et al. 2018, 3.1]]*  
- 裂隙的法向刚度和透水率之间不存在一一对应的唯一关系，使用刚度推断透水率或其各向异性缺乏物理基础。[[Lang et al. 2018, 3.1]]*  
- 临界取向裂隙（约 β = 52–60°）具有最大的剪切位移和相对较低的压缩，因而具有最高的水力隙宽，构成岩体中的优先导水通道。[[Lang et al. 2018, 3.2.1]]*  
- 共轭裂隙对在 60° 倾角下，岩体渗透率可比无剪切情况高出 3 个数量级，且中间主渗透率方向偏离对称轴、偏向高剪移分支。[[Lang et al. 2018, 3.2.2]]*  
- 二维假设各向同性透水率的模拟得出 kmax ∥ S1，而三维模型纳入了各向异性透水率及中间主应力后，得出 kmax ∥ S2，揭示了降维假设对渗透率方向预测的根本性影响。[[Lang et al. 2018, 讨论部分]]*

## Candidate Concepts

- [[shear-induced transmissivity anisotropy]]
- [[fracture-matrix equivalent permeability tensor]]
- [[intermediate principal stress alignment of kmax]]
- [[multiscale hydromechanical coupling in fractured rock]]
- [[self-affine fracture roughness and asperity contact]]
- [[opening-closure stress path under triaxial compression]]
- [[critical fracture orientation for maximum hydraulic aperture]]
- [[stiffness-transmissivity non-uniqueness]]

## Candidate Methods

- [[FFT-accelerated elastic contact of rough surfaces]]
- [[augmented Lagrangian-Uzawa method for frictional contact]]
- [[downscale-upscale two-scale coupling (DFM-to-single fracture)]]
- [[Reynolds lubrication equation on variable aperture field]]
- [[permeability tensor computation by subsampling and least squares]]
- [[stochastic generation of self-affine composite surfaces with mismatch length]]
- [[power-law contact size distribution from numerical contact models]]

## Connections To Other Work

- 本研究的两尺度耦合方法是在 Lang et al. (2014, 2015, 2016) 及 Nejati et al. (2016) 的验证基础上建立的。  
- 与传统二维模型（Baghbanan & Jing 2008; Min, Rutqvist et al. 2004）的结论（kmax ∥ S1）形成对比，首次在三维模型中引入单裂隙各向异性透水率后，发现 kmax ∥ S2。  
- 结果与 Sibson (1996) 的现场观察一致：在长期演化中，断裂–断层系统的结构渗透率常在中间主应力方向发育。  
- 支持 Barton et al. (1995) 的论断“临界取向裂隙最可能导水”，并为其提供了基于双尺度力学的物理解释。  
- 与 Laubach et al. (2004) 强调的化学胶结控制渗透性的情形互补，适用于当前应力状态决定渗透性主方向的裂隙岩体。

## Open Questions

- 在更大尺寸、更高密度的复杂随机网络中，kmax ∥ S2 的规律是否保持，是否存在尺度依赖性？  
- 当裂隙发生大位移剪切，超出线弹性小变形假设时，透水率各向异性如何演化，是否会进一步增强 S2 对齐的趋势？  
- 考虑剪切过程中表面磨损和碎屑形成后，透水率各向异性的幅度和稳定性如何变化？  
- 其他应力路径（不同 S1/S3 比、孔隙压力变化）下，最大渗透率方向与中间主应力的关系是否仍然稳健？  
- 如何将该双尺度方法有效应用于强非均质岩体、层状地层或包含局部胶结的真实储层裂隙系统？  
- 能否基于地应力方向和裂隙产状统计，建立预测 kmax 方向的简化判据，而无需繁重的数值模拟？

## Source Coverage

本文使用全部 21 个非空索引片段（100% 块覆盖，100% 字符覆盖：已索引 100,524 字符，编译 100,962 字符，覆盖率 1.004）。所有内容均源自这些片段，无外部信息引入。
