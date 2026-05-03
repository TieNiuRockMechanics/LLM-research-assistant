---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-gottron-upscaling-of-fractured-rock-mass-properties-an-example-comparing-discrete-fracture"
title: "Upscaling of Fractured Rock Mass Properties – An Example Comparing Discrete Fracture Network (DFN) Modeling and Empirical Relations Based on Engineering Rock Mass Classifications."
status: "draft"
source_pdf: "data/papers/2021 - Upscaling of fractured rock mass properties – An example comparing Discrete Fracture Network (DFN) modeling and empirical relations based on engineering rock ma.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Gottron, D., and A. Henk. \"Upscaling of Fractured Rock Mass Properties – An Example Comparing Discrete Fracture Network (DFN) Modeling and Empirical Relations Based on Engineering Rock Mass Classifications.\" *Engineering Geology*, vol. 294, 2021, 106382, doi:10.1016/j.enggeo.2021.106382."
indexed_texts: "19"
indexed_chars: "91396"
nonempty_source_blocks: "19"
compiled_source_blocks: "19"
compiled_source_chars: "86757"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.949243"
coverage_status: "full-index"
source_signature: "42a1e1e35de930e2b18bb605a545b7ebcceaf1be"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T04:55:16"
---

# Upscaling of Fractured Rock Mass Properties – An Example Comparing Discrete Fracture Network (DFN) Modeling and Empirical Relations Based on Engineering Rock Mass Classifications.

## One-line Summary
通过离散裂隙网络（DFN）建模与基于工程岩体分类的经验关系进行对比，评估裂隙岩体弹性参数（变形模量、泊松比），并采用蒙特卡罗模拟考虑不确定性，揭示DFN模型能给出与含完整岩石参数的经验公式一致的较低变形模量，且能捕捉各向异性与空间变异性 [Gottron 2021, pp. 1-2]。

## Research Question
如何比较基于离散裂隙网络（DFN）模型与基于传统岩体分类（RMR、GSI、Q系统、RQD）的经验关系推算的裂隙岩体力学性质（变形模量、泊松比），并评估两类方法在不确定性处理、各向异性描述和空间变异性方面的能力？ [Gottron 2021, pp. 1-2]。

## Study Area / Data
研究选用两个德国砂岩采石场（Remlingen 与 Flechtingen）作为案例 [Gottron 2021, pp. 5-6]：
- Remlingen 砂岩属上 Buntsandstein（下三叠统），发育两组近垂直裂隙（R1：168/90°，R2：073/88°）和一组近水平层理/裂隙（R3：175/05°）；岩体构造较均一，水平层含黏土/粉砂岩软弱夹层 [Gottron 2021, pp. 5-6]。
- Flechtingen 砂岩属上 Rotliegend（下二叠统），发育三组垂直裂隙（F1：119/89°，F2：018/89°，F3：175/84°），具有大型交错层理和颗粒变化 [Gottron 2021, pp. 5-6]。
- 采用地面激光扫描（TLS）获取点云数据，半自动提取裂隙产状、等效半径和强度（P10、P32），基于概率密度函数（如对数正态、正态分布）描述各裂隙组几何参数（表1） [Gottron 2021, pp. 5-6]。
- 实验室测试获得完整岩石力学参数（单轴抗压强度、弹性模量、泊松比）和裂隙面力学参数（黏聚力、摩擦角、法向/切向刚度），其中Remlingen水平层理组未取得试样，参数引用自Ernst et al. (2016)，采用残余黏聚力0.025 MPa、残余摩擦角25°、切向刚度0.015 MPa/mm、法向刚度1 MPa/mm [Gottron 2021, pp. 7-8]。

## Methods
**DFN建模与升尺度**：
- 使用 FracMan 7.9 软件，建立50 m边长的立方体模型域，基于各裂隙组的产状、尺寸、强度概率分布生成随机裂隙网络，并通过与TLS数据的对比（产状、强度、尺寸）验证模型（最大偏差12.5%）[Gottron 2021, pp. 10-11]。
- 对裂隙组赋予实验室获得的力学参数，采用 Oda Geomechanics 方法假设各向同性或垂直横向各向同性（VTI），计算网格单元（1×1×1 或 10×10×10）的变形模量与泊松比张量；同时进行参数敏感性分析（弹性模量、刚度、裂隙强度等18个额外模型）[Gottron 2021, pp. 8-9]。

**岩体分类与经验关系**：
- 基于现场填图和TLS数据，结合 Priest 和 Hudson (1976) 的 RQD 公式（因裂隙间距较大，RQD=100 独立于概率分布），确定 RMR、GSI、Q 系统评分，其中 RMR 和 GSI 考虑 ±5，Q 考虑 ±4 的变异范围 [Gottron 2021, pp. 4-5, 6-7]。
- 采用蒙特卡罗模拟（Python 脚本）将分类输入参数视为正态分布随机变量，生成变形模量的概率分布，涵盖表4所列的18条经验方程（含仅基于分类评分的、分类评分+完整岩石参数的）[Gottron 2021, pp. 9-10]。

## Key Findings
- **DFN模型升尺度结果**：对Remlingen，VTI横向变形模量均值5.6 GPa，纵向4.1 GPa，各向同性4.6 GPa；Flechtingen横向4.8 GPa，纵向13.6 GPa（因无水平裂隙，纵向上几乎未弱化），各向同性6.1 GPa；变形模量仅为完整岩石弹性模量的26%~35% [Gottron 2021, pp. 10-13]。泊松比显示显著各向异性，Remlingen水平向0.56，垂向0.10；Flechtingen水平向0.56，垂向0.39 [Gottron 2021, pp. 10-11]。
- **岩体分类经验关系结果**：单纯基于分类评分的方程（如 Bieniawski 1978、Read et al. 1999、Gokceoglu et al. 2003）普遍高估变形模量，甚至超过完整岩石弹性模量；包含完整岩石参数的方程则给出与DFN模型一致的显著弱化结果，尤其是 Ajalloeian 和 Mohammadi (2014)、Carvalho (2004)、Galera et al. (2007)、Nicholson 和 Bieniawski (1990)、Shen et al. (2012)、Sonmez et al. (2006) 的公式 [Gottron 2021, pp. 11-13]。
- **DFN与经验关系的比较**：DFN模型计算值落在经验方程结果的较低区间，且离散度更小；岩体分类无法反映各向异性（如Flechtingen纵向模量接近完整岩石，横向显著降低），而DFN能提供各向异性张量和空间变异性[Gottron 2021, pp. 12-13]。
- **高分辨率DFN模型**（Remlingen，10×10×10网格）显示变形模量空间变化剧烈（纵向1.1~15.8 GPa，横向2.9~15.8 GPa），泊松比在软弱水平层附近显著升高（水平向可达0.70）[Gottron 2021, pp. 11-12]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| DFN模型计算的变形模量约为完整岩石弹性模量的25-35% | [Gottron 2021, pp. 12-13] | 模型域50 m立方，基于TLS实测几何参数与实验室力学参数；Remlingen 完整岩 E=15.8 GPa，Flechtingen E=17.7 GPa | 各向同性均值4.6~6.1 GPa；不含水平裂隙的Flechtingen纵向仍达13.6 GPa |
| 仅基于RMR的公式（如Bieniawski 1978、Read et al. 1999）高估变形模量，其结果可超过完整岩石弹性模量 | [Gottron 2021, pp. 11-13] | 蒙特卡罗模拟输入RMR均值73~76，完整岩石E 15~18 GPa | 部分公式给出>40 GPa的变形模量 |
| 包含完整岩石参数的RMR/GSI经验公式（如Galera et al. 2007, Nicholson & Bieniawski 1990, Sonmez et al. 2006, Carvalho 2004）与DFN模型结果吻合 | [Gottron 2021, pp. 11-13] | M.C.模拟考虑参数不确定性 | 变形模量分布在10 GPa以下，与DFN值一致 |
| VTI假设下，无水平裂隙的Flechtingen纵向变形模量（13.6 GPa）远大于横向（4.8 GPa），显示各向异性；Remlingen因水平软弱层存在，纵向亦有明显弱化（4.1 GPa） | [Gottron 2021, pp. 12-13] | 横向模量主要受垂直裂隙控制；纵向模量对水平裂隙敏感 | 证明DFN能够捕捉裂隙产状导致的方向性力学性质差异 |
| TLS半自动提取的裂隙几何参数验证表明DFN模型与实测产状、强度（P10）和尺寸吻合良好（偏差<12.5%） | [Gottron 2021, pp. 10-11] | 对比了27条虚拟钻孔的P10和RANSAC算法提取的裂隙尺寸 | 验证确保了模型的代表性 |
| 高分辨率DFN（5 m单元）揭示了强烈空间变异性：部分单元变形模量与完整岩石相同，部分仅1~3 GPa | [Gottron 2021, pp. 11-12] | Remlingen模型50 m域内划分10×10×10网格 | 说明岩体力学性质可能在工程尺度上非均匀，岩体分类无法反映 |

## Limitations
- 裂隙几何参数来源于地面激光扫描，受限于扫描位置、点云遮挡和岩壁湿度等；虽然目前有低成本摄影测量替代方案，但仍需专业设备与处理经验 [Gottron 2021, pp. 12-13].
- 岩体分类评分本身具有主观性和不确定性，文中采用±5（RMR/GSI）和±4（Q）的区间，但实际变异性可能更大 [Gottron 2021, pp. 9-10].
- DFN模型假设所有裂隙均为随机分布，没有考虑确定性大裂隙或断层（研究区无此类构造），故模型仅基于随机参数 [Gottron 2021, pp. 12].
- Remlingen水平裂隙组的力学参数因无法取样而借用文献值，可能引入额外误差 [Gottron 2021, pp. 7-8].
- 部分经验方程（如Hoek & Brown 1997）对输入评分高度敏感，GSI值变化10即可导致变形模量从48 GPa降至27 GPa，实际应用需谨慎 [Gottron 2021, pp. 12-13].

## Assumptions / Conditions
- 岩体变形模量的升尺度采用Oda岩体力学方法，假设各向同性或VTI（垂直横向各向同性）对称性；VTI允许泊松比大于0.5，上限可达1 [Gottron 2021, pp. 10].
- 裂隙网络为随机生成，其统计特性（产状、尺寸、强度）由实测概率密度函数表征，单个裂隙无现实对应物 [Gottron 2021, pp. 2-3].
- Monte Carlo模拟假设各输入参数服从正态分布，范围依据现场和实验室数据确定 [Gottron 2021, pp. 9-10].
- RQD计算基于 Priest & Hudson (1976) 的负指数公式，且因本研究裂隙间距大，结果与分布函数选择无关 [Gottron 2021, pp. 6-7].
- 实验室测试的力学参数（表3）代表完整岩石和裂隙面性质，并假设所有裂隙组的同类参数除Remlingen水平层外均相同 [Gottron 2021, pp. 7-8].

## Key Variables / Parameters
- 裂隙几何参数：产状（倾角/倾向）、等效半径（对数正态或正态分布）、P10、P32（面积密度） [Gottron 2021, pp. 5-6].
- 完整岩石力学参数：单轴抗压强度（Rem 98.9±8.0 MPa, Fle 103.3±8.4 MPa）、弹性模量（Rem 15.8±0.8 GPa, Fle 17.7±4.4 GPa）、泊松比（Rem 0.30±0.07, Fle 0.38±0.05） [Gottron 2021, pp. 7-8].
- 裂隙面强度参数：黏聚力（0.4 MPa）、摩擦角（Rem 37.9°, Fle 39.0°）、法向刚度（Rem 7.1±2.3 MPa/mm, Fle 7.5±2.8 MPa）、切向刚度（Rem 0.7±0.2 MPa/mm, Fle 0.8±0.3 MPa），Rem水平层采用残余值 [Gottron 2021, pp. 7-8].
- 岩体分类评分：RQD=100，RMR均值73~76，GSI 77，Q均值4~5，考虑变异区间 [Gottron 2021, pp. 10-11].
- DFN模型设置：模型域边长50 m，网格单元1×1×1（或10×10×10） [Gottron 2021, pp. 8-9].

## Reusable Claims
- 离散裂隙网络模型计算的岩体变形模量可仅为完整岩石弹性模量的25%~35%，弱化程度取决于裂隙产状与力学性质 [Gottron 2021, pp. 12-13]。
- 仅使用岩体分类评分（RMR、GSI、Q）而不引入完整岩石力学参数的经验公式会显著高估变形模量，有时超过完整岩石弹性模量 [Gottron 2021, pp. 11-13]。
- 包含完整岩石弹性模量的经验方程（如Galera et al. 2007, Nicholson & Bieniawski 1990, Sonmez et al. 2006, Carvalho 2004, Ajalloeian & Mohammadi 2014）能给出与DFN升尺度结果一致的变形模量估计 [Gottron 2021, pp. 12-13]。
- 无水平裂隙的垂直裂隙组岩体（如Flechtingen）在纵向上（平行于裂隙走向）几乎不弱化，横向（垂直裂隙面）弱化显著，表现出强各向异性 [Gottron 2021, pp. 10-11]。
- DFN方法能提供空间变异的岩体力学参数张量，并可同时用于水力（渗透率张量）升尺度，实现裂隙岩体的水-力耦合表征 [Gottron 2021, pp. 12-13]。
- 蒙特卡罗模拟用于岩体分类输入参数的不确定性传播是一种有效改进，能给出变形模量的概率分布而非单点值 [Gottron 2021, pp. 9-10]。

## Candidate Concepts
- [[离散裂隙网络（DFN）]]
- [[岩体分类]]
- [[岩石质量指标（RQD）]]
- [[岩体评分（RMR）]]
- [[地质强度指数（GSI）]]
- [[Q系统]]
- [[蒙特卡罗模拟]]
- [[Oda岩体力学方法]]
- [[垂直横向各向同性（VTI）]]
- [[Pij系统]]
- [[裂隙强度P32]]
- [[扫描线法P10]]
- [[裂缝柔度张量]]
- [[等效连续体]]
- [[岩体变形模量]]
- [[岩体泊松比]]
- [[水力-力学耦合]]

## Candidate Methods
- [[地面激光扫描（TLS）裂隙测量]]
- [[点云自动裂隙产状提取]]
- [[RANSAC形状检测（裂隙面提取）]]
- [[虚拟钻孔P10计算]]
- [[DFN随机建模（FracMan）]]
- [[Oda Geomechanics升尺度]]
- [[Oda Permeability升尺度]]
- [[直接剪切试验（裂隙强度）]]
- [[三轴压缩试验]]
- [[各向同性对称假设]]
- [[VTI对称假设]]
- [[岩体分类经验关系蒙特卡罗模拟]]
- [[概率密度函数输入DFN]]
- [[裂隙几何验证（产状、强度、尺寸）]]

## Connections To Other Work
- 裂隙岩体变形模量的降低幅度（20~75% 完整岩石）与 Beiki et al. (2010) 及 Pollard 和 Fletcher (2005) 的报道一致 [Gottron 2021, pp. 12-13]。
- 文中用于估算变形模量的经验方程涵盖了众多经典工作，包括 Bieniawski (1978)、Hoek & Diederichs (2006)、Shen et al. (2012)、Sonmez et al. (2004, 2006)、Carvalho (2004) 等，这些方程多数基于RMR、GSI或Q系统 [Gottron 2021, pp. 9-10]。
- Pij 系统源自 Dershowitz 和 Herda (1992)，用于将不同维度下的裂隙强度进行转换；P10 向 P32 的转换使用了 Wang (2005) 的解析解 [Gottron 2021, pp. 3]。
- 裂隙几何参数的自动提取借鉴了 Laux 和 Henk (2015)、Pan et al. (2019)、Xu et al. (2020) 的工作，这些研究亦展示了TLS在DFN建模中的应用 [Gottron 2021, pp. 2-3]。

## Open Questions
- 如何将DFN建模方法扩展到包含断层等确定性大尺度构造的复杂裂隙系统，并评估其对整体岩体力学性质的影响 [Gottron 2021, pp. 2-3]？
- 经验方程对输入评分的高度敏感性提示，如何系统性地量化因主观判断和测量偏差引起的分类结果不确定性，并建立更稳健的工程应用准则 [Gottron 2021, pp. 12-13]？
- 文中仅考虑了两个砂岩采石场，关于不同岩性（如结晶岩、碳酸盐岩）下DFN与经验关系的对比仍需更多案例验证 [Gottron 2021, pp. 1]。
- DFN模型中裂隙的法向和切向刚度取值对升尺度结果影响显著，但现场直接获取原位刚度参数的方法仍待发展，如何利用室内试验与数值模拟联合反演是潜在方向 [Gottron 2021, pp. 12-13]。

## Source Coverage
本文完全基于所提供的19个非空索引片段（共91,396字符）编写。所有索引片段均经过处理，编译源块覆盖率为100%（19/19），编译源块字符覆盖率为94.93%（86,757/91,396个字符）。未添加片段之外的作者、页码、数据或结论。
