---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-wu-characterization-of-flow-and-transport-in-a-fracture-network-at-the-egs-collab-field-exp"
title: "Characterization of Flow and Transport in a Fracture Network at the EGS Collab Field Experiment through Stochastic Modeling of Tracer Recovery."
status: "draft"
source_pdf: "data/papers/2021 - Characterization of flow and transport in a fracture network at the EGS Collab field experiment through stochastic modeling of tracer recovery.pdf"
collections:
  - "part4-1"
citation: "Wu, Hui, et al. “Characterization of Flow and Transport in a Fracture Network at the EGS Collab Field Experiment through Stochastic Modeling of Tracer Recovery.” *eScholarship*, 1 Feb. 2021, doi:10.1016/j.jhydrol.2020.125888. Accessed 2026."
indexed_texts: "18"
indexed_chars: "85259"
nonempty_source_blocks: "18"
compiled_source_blocks: "18"
compiled_source_chars: "85330"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.000833"
coverage_status: "full-index"
source_signature: "570db95243a3d831e034cfb8c9a8517045ce2b85"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T04:00:22"
---

# Characterization of Flow and Transport in a Fracture Network at the EGS Collab Field Experiment through Stochastic Modeling of Tracer Recovery.

## One-line Summary
本研究在数据丰富的增强型地热系统（EGS）试验台中，通过基于高保真裂隙网络模型的大规模随机示踪剂模拟，成功重现了六个保守示踪剂测试的现场回收数据，证明了利用随机建模表征裂隙流动与传输特征的可行性和有效性，并揭示了试验期间裂隙流动系统的演变过程。

## Research Question
能否在数据丰富的地下裂隙储层中，利用高保真裂隙网络模型与高性能计算，通过同时匹配多个观测点的示踪剂突破曲线，约束流动与传输的关键参数，并推断其动态演变？ [Wu 2021, pp. 1-5, abstract]

## Study Area / Data
- **地点**：美国南达科他州桑福德地下研究设施（SURF）4850 层西通道旁的 EGS Collab 实验 1 号测试床，深度约 1478 m，围岩以千枚岩为主 [Wu 2021, pp. 7-11]。
- **井网**：一口注入井 E1‑I，一口生产井 E1‑P，六口监测井（E1‑PDT，E1‑PDB，E1‑PST，E1‑PSB，E1‑OT，E1‑OB）[Wu 2021, pp. 7-11]。
- **地质/地球物理数据**：岩心录井、井壁成像、微震事件、分布式温度传感（DTS）、电阻率层析成像（ERT）、连续主动源地震监测（CASSM）、井下摄像等，用于刻画天然裂缝和水力裂缝 [Wu 2021, pp. 7-11, pp. 11-13]。
- **示踪剂测试**：2018 年 10 月 26 日至 11 月 14 日的 6 次 C‑Dots 保守示踪剂测试，注入时长 5.0‑7.6 min，注入浓度 160‑623 ppm，在 E1‑PHF、E1‑PNF 和 E1‑OT 获得了穿透曲线（BTCs），各井流出流量见表 1 [Wu 2021, pp. 13-16]。

## Methods
- **裂隙网络模型构建**：基于多种地质/地球物理观测，将流动系统简化为一条水力裂缝（由微震云和 DTS 异常约束）和一条天然裂缝（OT‑P 连接体，由五处自然流动的天然裂缝痕迹约束），裂缝平面分别用椭圆表示，周边设置汇项（sink）以参数化未显式建模的天然裂隙泄漏；两条裂缝通过交线上的泄漏界面序贯耦合 [Wu 2021, pp. 16-18]。
- **随机模拟框架**：对每条裂缝的参数空间（裂缝半轴长、孔径分布、弥散度、汇位置/尺寸、泄漏界面位置/长度/流量）采用拉丁超立方抽样，每个参数在给定范围内服从均匀或对数均匀分布（表 2），生成大量随机实现；用 GEOS 多物理场模拟平台求解稳态流场和瞬态示踪剂运移（有限体积法，上风差分）[Wu 2021, pp. 18-21, pp. 21-23]。
- **拟合与拒绝采样**：定义基于峰值浓度、峰现时间及半峰宽的误差函数（式 2），采用拒绝采样法获得后验参数集及其 90% 置信区间，同时惩罚多峰实现 [Wu 2021, pp. 23-26]。
- **序贯耦合**：先对水力裂缝进行随机模拟，取最优实现得到泄漏界面处的流量和浓度边界条件，再对天然裂缝进行随机模拟 [Wu 2021, pp. 23-26]。

## Key Findings
- **参数敏感性**（水力裂缝均匀孔径场景）：Sobol’ 总灵敏度分析表明，孔径（w）、汇位置（θ）是对总失配度影响最大的两个参数，而裂缝半长（A1, A2）和泄漏界面长度（LL）等参数影响甚微 [Wu 2021, pp. 26-31, Fig. 6]。
- **水力裂缝的均匀孔径模型**：能够同时匹配 E1‑PHF 和 E1‑OT 的实测 BTCs，获得关键参数的 90% 置信区间，其中孔径在 10 月 26 日（0.648 mm）远大于后期测试（0.124‑0.305 mm），汇位置稳定在 229°‑260°，泄漏界面中心位置在 3.6‑6.2 m 之间 [Wu 2021, pp. 25-26, Table 3]。
- **天然裂缝需要非均质孔径**：均匀孔径假设下无法合理重现 E1‑PNF 的 BTC；采用空间自相关非均质孔径（对数正态分布）后，可获得令人满意的匹配，推断的平均孔径约 1‑3 mm，与岩心观察一致，但孔径参数本身未能唯一约束 [Wu 2021, pp. 31-35, pp. 35-38]。
- **流场演变**：模拟结果揭示了两次主要变化——① 10 月 26 日至 31 日间水力裂缝孔径显著减小，可能因裂缝扩展加强了与天然裂隙系统的连通，无需再靠大孔径容纳注入量；② 11 月 1 日至 7 日间 E1‑OT 密封破坏导致流出再分配，使示踪剂更快到达 E1‑OT [Wu 2021, pp. 38-42]。
- **数据质量与观测点数量至关重要**：仅匹配 E1‑PHF 或 E1‑OT 单一 BTC 时，关键参数无法收敛；缺失 BTC 上升段或尾部会增加解释不确定性 [Wu 2021, pp. 42-45]。
- **独立验证**：模型推断的水力裂缝泄流位于其西边界，后期 12 月的注水刺激中微震事件向北扩展并与之相交，证实了该推断 [Wu 2021, pp. 38-42]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 在水力裂缝均匀孔径场景下，孔径（w）和汇位置（θ）的 Sobol’ 总灵敏度指数最高，是控制示踪剂运移的主导参数 | [Wu 2021, pp. 26-31] | 6 次测试，均匀孔径，9 参数 | 裂缝半长 (A1, A2) 和泄漏界面长度 (LL) 灵敏度极低 |
| 10 月 26 日拟合孔径 (0.648 mm) 显著大于后期测试 (0.124‑0.305 mm)，与 10 月 29‑30 日的水力裂缝扩展时间吻合 | [Wu 2021, pp. 38-42, Table 3] | 均匀孔径最佳估计值 | 表明裂缝扩展后不需要大孔径来容纳注入量 |
| 非均质孔径场景下可实现天然裂缝 E1‑PNF BTC 的良好匹配，推断的平均孔径 (1‑3 mm) 与岩心观察一致 | [Wu 2021, pp. 35-38, Fig. 10] | 天然裂缝，非均质孔径，约 5 万实现 | 孔径参数无法唯一约束，存在过拟合风险 |
| 仅用单点（E1‑PHF 或 E1‑OT）BTC 进行反演时，关键参数（w, θ, αL, PL）的分布很宽，无法有效约束 | [Wu 2021, pp. 42-45, Fig. 12] | 10 月 31 日测试，均匀孔径场景 | 多观测点同时匹配是参数可行约束的前提 |
| 随机模拟推断的水力裂缝泄漏位于其西边界，后被 12 月微震事件证实 | [Wu 2021, pp. 38-42] | 独立野外观察 | 增强了对模型结果的信心 |

## Limitations
- 模型未包含基质扩散，但依据基质低孔隙度（0.01）和短示踪注入时间（5‑7.6 min），其影响可能有限 [Wu 2021, pp. 16-18]。
- 非均质孔径场景下，天然裂缝的孔径参数无法唯一确定，可能过度拟合有限的示踪剂数据 [Wu 2021, pp. 31-35]。
- C‑Dots 示踪剂对千枚岩可能存在 Langmuir 型吸附，导致水回收率与示踪剂质量回收率不一致，引入额外不确定性 [Wu 2021, pp. 42-45]。
- 部分 BTC 数据不完整（如 10 月 26 日 E1‑OT 缺失上升段，11 月 14 日 E1‑PNF 缺失尾部），加大了随机模拟结果的模糊性 [Wu 2021, pp. 42-45]。
- 裂隙网络的几何简化（椭圆形状、汇参数）可能忽略真实形态细节，但对主要流动特征的影响在模型假设范围内 [Wu 2021, pp. 16-18]。

## Assumptions / Conditions
- 流动为稳态，示踪剂运移遵循对流‑弥散方程，不考虑温度影响（注入近等温）[Wu 2021, pp. 21-23]。
- 裂缝采用薄层等效多孔介质，等效孔隙度 φ = w/H，等效渗透率 k = w³/(12H)，即服从立方定律 [Wu 2021, pp. 21-23]。
- 横向弥散度 αT = 0.1αL，分子扩散系数固定为 Dm = 3×10⁻⁹ m²/s [Wu 2021, pp. 18-21]。
- 测量误差为独立同分布的高斯随机变量，标准差 σe = 0.3 [Wu 2021, pp. 23-26]。
- 参数空间中各参数服从均匀或对数均匀分布，采用拉丁超立方抽样 [Wu 2021, pp. 21-23]。
- 仅两条主要裂缝参与流动与传输，其他天然裂隙的影响通过周边汇项参数化 [Wu 2021, pp. 16-18]。
- 示踪剂测试期间裂缝几何形态不变（稳态流场）；孔径场在单一实现中固定 [Wu 2021, pp. 21-23]。

## Key Variables / Parameters
- **水力裂缝**：半长轴 A1 (8.0‑17.5 m), A2 (7.5‑13.5 m)；均匀孔径 w (0.01‑1 mm) 或非均质孔径参数 (平均孔径 𝒘 = 0.05‑1 mm, 标准差 σ = 0.05‑1 mm, 相关长度 CL = 4‑15 m)；纵向弥散度 αL (0.001‑4 m)；汇位置 θ (0‑360°) 和长度 L (3‑15 m)；泄漏界面中心位置 PL (0.2‑9.0 m), 长度 LL (0.2‑9.0 m，受 PL 制约), 泄漏流量 qL (各测试日范围不同，见表 2) [Wu 2021, pp. 18-21, Table 2]。
- **天然裂缝**：均匀孔径 w' (0.01‑30 mm) 或 𝒘′ (0.1‑10 mm), σ' (0.1‑10 mm), CL' (4‑25 m)；汇位置 θ' (0‑360°) 和长度 L' (3‑20 m) [Wu 2021, pp. 18-21, Table 2]。
- **示踪剂注入条件**：注入浓度 C₀ (160‑623 ppm), 注入持续时间 5.0‑7.6 min [Wu 2021, pp. 13-16, Table 1]。

## Reusable Claims
- 在具有丰富地质/地球物理约束的环境中，基于高保真裂隙网络的随机示踪剂模拟能够同时匹配多个监测点的 BTCs，从而有效约束主导流动与传输的关键参数（如孔径和汇位置）[Wu 2021, pp. 1-5, pp. 25-26]。
- 水力裂缝在均匀孔径假设下即可重现示踪剂响应，而天然裂缝则需要非均质孔径场才能拟合，提示天然裂缝中流动通道化更为显著 [Wu 2021, pp. 31-35, pp. 38-42]。
- 至少需要两个观测点的示踪剂数据才能对参数施加有效约束；单一观测点反演可能导致参数无法收敛 [Wu 2021, pp. 42-45]。
- Sobol’ 总灵敏度指标可定量识别控制示踪剂运移的主导参数，在类似研究中可作为降低参数维度的依据 [Wu 2021, pp. 26-31]。
- 连续多次示踪剂测试与随机模拟相结合，可推断裂隙流动系统的动态演变，例如裂缝扩展引起的孔径减小或密封破坏导致的流径重分配 [Wu 2021, pp. 38-42]。

## Candidate Concepts
- [[stochastic tracer modeling]] [[fracture characterization]] [[EGS Collab Experiment 1]]
- [[fracture network model]] [[leakage interface]] [[sequential coupling]]
- [[rejection sampling]] [[Sobol’ sensitivity analysis]] [[Latin hypercube sampling]]
- [[flow channeling]] [[heterogeneous aperture distribution]] [[peak-based misfit function]]
- [[multi‑peak penalty]] [[pressure‑tracer data integration]]

## Candidate Methods
- [[high‑fidelity fracture model constrained by borehole imaging, microseismicity, DTS, etc.]]
- [[stochastic realizations with uniform/log‑uniform parameter distributions and Latin hypercube sampling]]
- [[finite volume flow and transport simulation in GEOS on equivalent porous fractures]]
- [[rejection sampling for posterior appraisal using four‑point peak misfit function]]
- [[Sobol’ total sensitivity index for dominant parameter identification]]
- [[sequential simulation of coupled hydraulic and natural fractures via leakage interface]]

## Connections To Other Work
- Soultz‑sous‑Forêts 站点采用随机反演时，未能同时匹配两条 BTCs，本研究通过匹配两个观测点实现了有效约束，表明多观测点数据是突破瓶颈的关键 [Wu 2021, pp. 5-7]。
- 与离散裂隙网络随机模拟（Cacas et al., 1990a,b）一脉相承，但利用更密集的地质/地球物理数据和高性能计算提升了模拟保真度 [Wu 2021, pp. 1-5]。
- C‑Dots 此前被视作保守示踪剂（Hawkins et al., 2017b; Mattson et al., 2019b），但本研究指出其可能存在吸附，与后续吸附试验结果一致，提醒谨慎解释回收率 [Wu 2021, pp. 42-45]。
- 天然裂缝非均质孔径下的流动通道化特征，与实验室和理论研究中观察到的单裂隙通道化现象（Moreno et al., 1988; Tsang & Tsang, 1989; Fu et al., 2016）相符 [Wu 2021, pp. 31-35]。

## Open Questions
- 如何利用更长的观测时间、更多监测点的 BTC 数据，来降解非均质孔径反演的过拟合问题，获取唯一可辩识的参数？ [Wu 2021, pp. 35-38, pp. 42-45]
- C‑Dots 的吸附行为对随机模拟结果的定量影响有多大？是否可通过联合拟合多种示踪剂（如保守示踪剂与反应性示踪剂）来降低不确定性？ [Wu 2021, pp. 42-45]
- 能否将裂缝形态的确定性信息（如椭圆假设）与随机几何描述更好地结合，以平衡模型可预测性与灵活性？ [Wu 2021, pp. 16-18]

## Source Coverage
本次编辑处理了所有 18 个非空索引源文本块。已编译的源文本字符总数为 85,330（索引字符数 85,259），按块覆盖率 1.0，按字符覆盖率 1.000833。所有陈述均严格基于提供的索引片段，未添加任何外部或虚构信息，并已通过来源标签 [Wu 2021, pp. …] 标注。
