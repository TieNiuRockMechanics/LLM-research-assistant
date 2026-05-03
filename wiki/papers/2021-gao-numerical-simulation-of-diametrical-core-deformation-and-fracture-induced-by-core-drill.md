---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-gao-numerical-simulation-of-diametrical-core-deformation-and-fracture-induced-by-core-drill"
title: "Numerical Simulation of Diametrical Core Deformation and Fracture Induced by Core Drilling."
status: "draft"
source_pdf: "data/papers/2021 - Numerical simulation of diametrical core deformation and fracture induced by core drilling.pdf"
collections:
  - "zotero new"
citation: "Gao, Guiyun, et al. \"Numerical Simulation of Diametrical Core Deformation and Fracture Induced by Core Drilling.\" *Arabian Journal of Geosciences*, vol. 15, no. 1, 2021, article 59. doi:10.1007/s12517-021-09378-0. Accessed 2026."
indexed_texts: "9"
indexed_chars: "40291"
nonempty_source_blocks: "9"
compiled_source_blocks: "9"
compiled_source_chars: "39918"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.990742"
coverage_status: "full-index"
source_signature: "3855c85309573da1595959c1cb3bf0e49dec076f"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T04:32:58"
---

# Numerical Simulation of Diametrical Core Deformation and Fracture Induced by Core Drilling.

## One-line Summary
本研究利用数值模拟方法分析钻探导致的岩心直径方向变形与破裂，发现弹性均质岩心的变形与DCDA理论完全吻合；矿物组分引起的非均质性会产生残余应力并显著影响变形和开裂行为。

## Research Question
当岩心存在弹性各向异性或微裂纹时，钻探引起的岩心直径变形与破裂机制尚未明确。岩心由不同矿物组成，这些矿物组分如何主导钻探过程中的直径变形和破裂行为，是本研究要回答的核心问题。[Gao 2021, pp. 1-2]

## Study Area / Data
本研究为数值模拟研究，未涉及特定地理区域。模拟对象为花岗岩岩心，其矿物组分（石英、斜长石、钾长石、黑云母、绿泥石）的力学参数取自已发表文献 [Gao 2021, pp. 6, Table 1]，参数涵盖密度、弹性模量、泊松比、拉伸强度、断裂能等。模拟中采用的体积组分比例通过七组不同组合来表征矿物含量的变化 [Gao 2021, pp. 8-9]。此外，已验证有限元模型的网格与载荷对称性，并采用1/4模型以提高计算效率 [Gao 2021, pp. 6-7]。

## Methods
**核心变形数值模拟框架**
- 使用ABAQUS建立1/4对称模型，通过“移除”代码模拟钻探过程：先施加原岩应力，消除初始位移和应变，再移除围岩实现应力卸除，记录岩心直径变形 [Gao 2021, pp. 6-7]。
- 弹性均质模拟时，采用线弹性理论计算理论值，并与模拟结果对比 [Gao 2021, pp. 2-3, 6-7]。
- **非均质模拟**：采用两种方法。球形夹杂物法（用圆形代表矿物颗粒）和基于ABAQUS二次开发的随机单元属性法，后者通过随机簇生成不同属性的单元，可精确设计各矿物体积比但难以控制粒径 [Gao 2021, pp. 3-4]。
- **脆性开裂模拟**：基于ABAQUS/Explicit中的脆性开裂模型，采用Rankine准则（最大主应力超过材料拉伸强度时开裂），独立控制I型和II型开裂后行为，以最大位移或断裂能描述后破坏响应 [Gao 2021, pp. 3-4]。
- **粘性单元断裂模拟**：建立零厚度粘性单元（COH2D4），采用牵引-分离定律和指数软化损伤演化（见公式8-11），使用能量或位移基损伤演化准则，断裂能量根据纯I型、II型、III型定义 [Gao 2021, pp. 4-6]。混合模式损伤起始采用二次失效准则（公式12）。

## Key Findings
1. 在弹性均质岩心中，模拟的直径变形与DCDA理论值完全一致（不同应力比SHmax/Shmin=1.0~3.0下，U1和U2与理论计算吻合，dmax−dmin理论值与模拟值匹配）[Gao 2021, pp. 7, Table 2]。
2. 考虑矿物组分时，变形场呈非均质特征，最大直径变形U1和U2因矿物分布不同而变化。例如，U1随斜长石含量增加而减小，随石英含量增加而增大（除试样2、3外），而U2变化趋势相反，且U1与黑云母体积比正相关 [Gao 2021, pp. 8-9, Fig. 10]。
3. 非均质岩心卸荷后出现残余应力，局部残余应力甚至接近施加应力，导致DCDA弹性理论可能失效 [Gao 2021, pp. 9-10]。
4. 脆性开裂模拟显示，裂纹沿最大水平应力SHmax方向开启，主裂纹方位沿最小水平应力Shmin方向，靠近中心略有偏移。裂纹密度在SHmax方向大于Shmin方向。裂纹参数（如破坏应变）影响裂纹长度和密度 [Gao 2021, pp. 10, Fig. 11-12]。
5. 粘性单元模拟表明，应力释放过程中矿物颗粒周围（如黑云母）出现较大应力差，产生局部张应力，促使裂纹张开。微裂纹先在黑云母周围萌生，随后沿Shmin方向在斜长石或钾长石中扩展。粘性单元完全损伤后删除（白色区域）[Gao 2021, pp. 10-11, Fig. 14-15]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 弹性均质岩心直径变形与DCDA理论计算值一致 | [Gao 2021, pp. 7, Table 2] | SHmax/Shmin=1.0~3.0，E=71.6 GPa，ν=0.25；1/4对称模型 | 模拟释放围岩后U1、U2与理论值吻合 |
| 球形夹杂物与随机单元属性法均能模拟非均质变形，后者更均匀，残余应力较低 | [Gao 2021, pp. 4, 7-9] | 试样No.6矿物体积比石英48.2%、斜长石39.8%等 | 变形场不均匀，残余应力出现 |
| 矿物体积比影响直径变形：U1随斜长石比减小、石英比增加而增大（除个别样）；U2反向变化 | [Gao 2021, pp. 9, Fig. 10] | 7组不同体积比试样，随机单元属性法 | 变形与黑云母体积比同步变化 |
| 脆性开裂模型产生SHmax方向开启裂纹，主方位沿Shmin | [Gao 2021, pp. 10, Fig. 11] | 随机单元属性法，脆性开裂参数见表1；破坏应变0.001或2e-5 | 裂纹密度在SHmax方向更高 |
| 粘性单元显示微裂纹萌生于黑云母等高刚度差矿物周围，继而沿Shmin方向扩展 | [Gao 2021, pp. 11, Fig. 14-15] | ZT粘性单元，能量基指数软化；SHmax=60 MPa，Shmin=30 MPa | 单元完全损伤后删除，SDEG从0增至1 |
| 卸荷残余应变可达10⁻⁴量级，局部拉伸应力促进开裂 | [Gao 2021, pp. 9,11] | 非均质模型（随机属性法） | 残余应力接近施加应力值时DCDA不适用 |

## Limitations
- 模拟所用矿物力学参数取自文献，可能与实际岩石不完全一致，准确性待验证 [Gao 2021, pp. 12]。
- 主要依赖数值模拟，缺乏相应的室内实验或现场数据直接验证 [Gao 2021, pp. 12]。
- DCDA理论基于线弹性各向同性，模拟结果揭示了非均质时的偏差，但未提出修正方法 [Gao 2021, pp. 12]。
- 脆性开裂与粘性单元模型受限于设定的破坏准则和参数，未涵盖更复杂的微裂纹相互作用 [Gao 2021, pp. 10-11]。

## Assumptions / Conditions
- DCDA理论假设：岩石为均质各向同性、小变形线弹性，钻孔轴方向应力Sv与水平应力无关 [Gao 2021, pp. 2-3, 公式1-2]。
- 钻探时岩心初始为理想圆形，钻头处的截面与围岩约束一致，离开切削面的截面自由膨胀 [Gao 2021, pp. 2-3, Fig.1]。
- 模拟中岩心未考虑孔隙压力、温度效应，仅施加地应力载荷（SHmax和Shmin） [Gao 2021, pp. 6-7]。
- 脆性开裂模型假定材料受压时线弹性，开裂后行为由最大位移或断裂能控制；多裂纹可在正交方向独立产生 [Gao 2021, pp. 3-4]。
- 粘性单元方法假设破坏前为线弹性牵引‑分离，损伤起始遵循二次名义应力准则，损伤演化采用指数软化 [Gao 2021, pp. 4-6, 公式8-12]。

## Key Variables / Parameters
- **几何/载荷**：岩心初始半径23.5 mm；水平主应力SHmax、Shmin（如20 MPa/10 MPa、60 MPa/30 MPa）；应力比SHmax/Shmin [Gao 2021, pp. 7, Table 2]。
- **矿物组分**：石英(s)、斜长石、钾长石、黑云母、绿泥石的体积比；各矿物弹性模量E（19.9~86.1 GPa）、泊松比ν（0.14~0.35）、拉伸强度Ts（3~9 MPa）、I型断裂能GIC（0.3~0.9 MPa·mm）等 [Gao 2021, pp. 6, Table 1]。
- **脆性开裂参数**：破坏应变/位移（0.0005~0.001）、直接裂纹破坏应变 [Gao 2021, pp. 6, Table 1]。
- **粘性单元参数**：纯正型刚度kno、临界应力tno（1 MPa）、剪切强度ts0,tt0（2 MPa）、断裂能GI/GII（0.1 N/m, 10 N/m）、指数软化系数 [Gao 2021, pp. 10-11]。
- **损伤变量**：SDEG（0~1，0无损，1完全损伤）、有效位移δm [Gao 2021, pp. 5-6,10]。

## Reusable Claims
- 在弹性均质各向同性岩石中，基于DCDA理论的数值模拟能精确重现钻孔引起的直径变形，可用于验证计算模型 [Condition: 线弹性、小变形、无裂纹；据Table 2]。[Gao 2021, pp. 7, 11-12]
- 岩心矿物组分的非均质分布会导致释放应力后产生残余应力和非均质直径变形，可能使DCDA计算的地应力差远高于水力压裂实测值 [Condition: 存在弹性模量和泊松比差异显著的矿物；据pp. 9-10, 12]。[Gao 2021, pp. 9-10, 12]
- 钻探应力释放会在最大水平应力方向引起张开裂纹，且微裂纹密度在该方向更高；主裂纹方位与最小水平应力平行 [Condition: 脆性开裂模型成立；据Fig.11,12]。[Gao 2021, pp. 10]
- 矿物颗粒间刚度差异（如黑云母）导致局部张应力集中，是微裂纹萌生的关键机制 [Condition: 粘性单元法，矿物接触面具有确定的牵引‑分离参数；据Fig.14-15]。[Gao 2021, pp. 11]

## Candidate Concepts
- [[Diametrical core deformation analysis (DCDA)]]
- [[In situ stress measurement]]
- [[Stress release induced by drilling]]
- [[Elastic heterogeneity]]
- [[Mineral component volume ratio]]
- [[Residual stress after coring]]
- [[Brittle cracking model]]
- [[Cohesive element method]]
- [[Traction–separation law]]
- [[Damage evolution (SDEG)]]
- [[Core-induced microcracks]]
- [[Random elemental properties method]]

## Candidate Methods
- [[ABAQUS secondary development for random material assignment]]
- [[Spherical inclusion method for mineral representation]]
- [[Brittle cracking model in ABAQUS/Explicit]]
- [[Zero-thickness cohesive element embedding]]
- [[Energy-based exponential softening damage evolution]]
- [[Mixed-mode quadratic nominal stress initiation criterion]]
- [[Quarter symmetry model for diametrical core deformation]]

## Connections To Other Work
- DCDA理论基础源于Funato和Chen (2005)，并由Funato等 (2012)、Ito等 (2020)通过实验验证；本研究在弹性均质条件下复现了理论结果，证实了模型的有效性 [Gao 2021, pp. 1-2, 7]。
- 模拟得出的开裂方向与Liu等 (2011) 关于环向速度各向异性与应力方向关系的认识一致，即微裂纹平行于最小应力方向，与实验观察吻合 [Gao 2021, pp. 10, 12]。
- 现场DCDA测得应力差偏高的现象（Chen等 2007）可通过本研究中矿物组分引起的残余应力和裂纹效应得到解释 [Gao 2021, pp. 12]。
- 采用的脆性开裂和粘性单元方法与多篇岩石断裂模拟文献（如Jiang和Meng 2018、Su等 2010）的技术路线一致 [Gao 2021, pp. 4-6, 10,13]。

## Open Questions
- 如何修正或扩展DCDA方法，使其适用于非均质或含微裂纹的岩心应力测量 [Gao 2021, pp. 12]。
- 矿物组分的精确本构参数（尤其是断裂能和强度）如何通过实验标定 [Gao 2021, pp. 12]。
- 三维条件下岩心卸荷变形和裂纹演化是否与二维模拟结果一致。
- 动态钻探过程（如钻头振动、流体冷却）对直径变形的影响机制未涉及。
- 多矿物集合体的残余应力释放能否通过原位波速变化量化。

## Source Coverage
本页面已处理所有非空索引片段。共索引文本块9个，索引字符40291个；编译使用的源块9个，编译字符39918个。按块覆盖率为1.0，按字符覆盖率为0.990742。已实现全量索引覆盖，无遗漏。数据签名：3855c85309573da1595959c1cb3bf0e49dec076f。全部陈述仅基于所提供的索引片段。
