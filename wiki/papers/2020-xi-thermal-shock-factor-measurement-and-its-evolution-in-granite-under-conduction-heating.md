---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-xi-thermal-shock-factor-measurement-and-its-evolution-in-granite-under-conduction-heating"
title: "Thermal Shock Factor Measurement and Its Evolution in Granite under Conduction Heating."
status: "draft"
source_pdf: "data/papers/2020 - 传导加热下花岗岩中热冲击因子试验测定与演变规律分析.pdf"
collections:
  - "part2"
  - "郤"
citation: "Xi, Baoping, et al. \"Thermal Shock Factor Measurement and Its Evolution in Granite under Conduction Heating.\" *Chinese Journal of Rock Mechanics and Engineering*, vol. 39, no. 7, 2020, pp. 1356-68. doi:10.13722/j.cnki.jrme.2020.0101."
indexed_texts: "4"
indexed_chars: "16420"
nonempty_source_blocks: "4"
compiled_source_blocks: "4"
compiled_source_chars: "14894"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.907065"
coverage_status: "full-index"
source_signature: "fc2a0999b94ed64bbbfcdcb3307e9d589823b2c8"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T03:48:33"
---

# Thermal Shock Factor Measurement and Its Evolution in Granite under Conduction Heating.

## One-line Summary
实验测定了恒定热源（60 ∼ 100 ℃）传导加热下花岗岩的温度场、温度梯度和热冲击因子，发现加热过程分为快速升温、缓慢升温和相对稳定三个阶段，热冲击因子分布非均质、对岩体结构敏感且峰值动态迁移，为岩石热损伤理论提供基础。

## Research Question
花岗岩在传导加热过程中热冲击因子如何随时间演变？其空间分布规律与温度梯度、岩体结构（矿物颗粒、微裂隙）之间存在怎样的关系？

## Study Area / Data
实验样品为花岗岩，化学成分（XRF）以 SiO₂（64.578%）、Al₂O₃（12.294%）、Fe₂O₃（4.120%）为主；矿物组成（XRD）包括石英、碱性长石、斜长石、云母等[Xi 2020, pp. 1-4]。试件尺寸 200 mm × 200 mm × 100 mm，表面钻有 Φ8 mm、深 30 mm 的孔，孔心距 25 mm，每面布置 36 个测点，共 64 个温度测点[Xi 2020, pp. 4-10]。加热热源温度设定为 60 ℃、70 ℃、80 ℃、90 ℃和 100 ℃，每次加热持续 10 h[Xi 2020, pp. 1-4]。

## Methods
- **温度测量**：采用 TORPRE TP9000 多路数据采集仪配合 ARM 微处理器，实现 64 通道同步测温，精度 ±1 ℃，分辨率 ±0.5 ℃。温度传感器按图 4(a) 阵列埋入岩体 30 mm 深处[Xi 2020, pp. 1-4, 4‑10]。  
- **热冲击因子计算**：由实测温度场计算温度梯度 d*T*/d*x*，再根据式 ω = (d*T*/d*x*) / τ （式中 τ 为特征时间）获得热冲击因子 ω[Xi 2020, pp. 1-4]。  
- **动态热应力与热损伤判据**：利用 Lidman 和 Bobrowsky 热应力公式 p = αE·(d*T*/d*x*) 和 σ*_T* = αE ω，结合判据 σ*_T* ≥ σ*_cri* 判断热损伤是否发生[Xi 2020, pp. 1-4]。  
- 实验与测量方法的专利号为 CN201811439431.2[Xi 2020, pp. 13-13]。

## Key Findings
- 恒定热源传导加热下花岗岩温度变化经历三个阶段：（1）快速升温阶段（~1 h，升温速率 30 ~ 45 ℃/h）；（2）缓慢升温阶段（~3 h，速率 1 ~ 3 ℃/h）；（3）相对稳定阶段。近热源点升温快，远热源点滞后[Xi 2020, pp. 1-4, 4‑10]。  
- 温度梯度在加热阶段变化剧烈，80 ℃ 加热初期梯度极值可达 532 ℃/m，最小值仅 12 ℃/m；4 h 后峰值降至 292 ℃/m，稳定阶段梯度集中在 68 ~ 292 ℃/m[Xi 2020, pp. 4-10]。  
- 热冲击因子在岩体内呈非均质、不规则分布，对矿物颗粒、微裂隙等岩体结构敏感；其峰值在传导加热过程中动态移动[Xi 2020, pp. 1-4, 10‑13]。  
- 不同热源温度下，热冲击因子峰值大小和出现时刻各异，且沿传热方向（从近热源至远热源）逐渐降低[Xi 2020, pp. 10-13]。  
- 循环加热导致花岗岩损伤的本质是矿物颗粒在动态热应力作用下分离，裂纹逐渐萌生、扩展并贯通岩体[Xi 2020, pp. 1-4]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 80 ℃恒温热源加热10 h，温度场在0~4 h内剧烈变化，4 h后趋于稳定 | Xi 2020, pp. 4-10, 图5 | 200 mm × 200 mm × 100 mm花岗岩，单面传导加热 | 温度分布见图5(a)~(f) |
| 测点温度曲线显示三阶段：1 h内快速升温30~45 ℃/h；随后约3 h缓慢升温1~3 ℃/h；之后基本稳定 | Xi 2020, pp. 4-10, 图6 | 60~100 ℃热源，监测点4#~34# | 所有工况均符合该规律 |
| 80 ℃加热初期（90 s）温度梯度高达532 ℃/m，最小12 ℃/m；4 h后峰值292 ℃/m，稳定阶段68~292 ℃/m | Xi 2020, pp. 4-10, 图8 | 同一试件，80 ℃传导加热 | 梯度非均匀，加热前期梯度变化率大 |
| 80 ℃加热时热冲击因子在前4 h数值较大，尤其加热第1 h内突出，随后减小 | Xi 2020, pp. 10-13, 图12 | 80 ℃恒温热源 | 热冲击因子分布受矿物结构影响 |
| 热冲击因子峰值随时间动态迁移，近热源点（4#）峰值高且出现早，远热源点（28#）峰值低且滞后 | Xi 2020, pp. 10-13, 图13、图14 | 60~100 ℃，不同测量点 | 图13、14 |
| 循环加热下矿物颗粒分离、裂纹萌生—扩展—贯通，可作为热损伤本质描述 | Xi 2020, pp. 1-4 | 实验观察与理论分析 | 未直接量化裂纹密度 |

## Limitations
- 仅使用一种花岗岩，矿物成分和结构代表性有限，结论外推需谨慎。  
- 实验为恒定热源单面传导加热，未涉及对流、辐射及冷却过程，与实际工程热环境有差异。  
- 热冲击因子计算基于一维温度梯度假设，三维效应可能引起误差。  
- 未同步进行力学参数测试，热损伤程度仅通过温度梯度和热冲击因子间接推断，缺乏直接的强度或裂纹量化数据。  
- 加热时长限于10 h，可能未完全达到热稳态；循环次数有限，热疲劳效应未充分考察。

## Assumptions / Conditions
- 花岗岩在计算中被视为均质热弹性材料，但实测表明非均质性影响显著。  
- 热冲击因子定义式 ω = (d*T*/d*x*) / τ 中的 τ 取自温度曲线特征时间，具经验性。  
- 动态热应力按线弹性公式计算，忽略塑性变形和微裂纹导致的非线性。  
- 实验假设试件与热源接触良好、侧面绝热（主要为传导传热），未考虑空气对流散热。  
- 温度传感器埋深30 mm，假设该深度处温度代表局部平均值，不讨论传感器本身热扰动。

## Key Variables / Parameters
- **热源温度** Tₛ：60, 70, 80, 90, 100 ℃  
- **加热时间** t：0 ~ 10 h，重点观察前4 h  
- **温度梯度** d*T*/d*x*（℃/m）：空间分布与随时间演变  
- **热冲击因子** ω（℃/(m·s)）：由温度梯度和特征时间计算  
- **热膨胀系数** α、**弹性模量** E：文中作为常量符号，未给具体数值  
- **临界应力** σ*_cri*：未标定具体值，仅作为判据引用  
- **矿物组成与含量**（表1）：影响热物性参数空间非均质性

## Reusable Claims
1. 恒定热源传导加热下花岗岩温度上升过程可分三阶段：快速升温（~1 h，30 ~ 45 ℃/h）、缓慢升温（~3 h，1 ~ 3 ℃/h）和相对稳定阶段，该规律在60 ~ 100 ℃范围内成立。  
2. 温度梯度在加热初期有极大值（如80 ℃时最高532 ℃/m），随后迅速衰减并趋于稳定；温度梯度的时空变化幅度与热源温度正相关。  
3. 花岗岩内热冲击因子分布非均质、不规则，对岩体结构（矿物颗粒、微裂隙）敏感，其峰值随加热进程动态迁移，近热源处峰值高且出现早，远热源处则低且晚。  
4. 循环加热下花岗岩损伤的细观机制是矿物颗粒在动态热应力下分离，裂纹逐步萌生、扩展并贯通；热冲击因子可作为定量表征热损伤强弱的物理量。  
5. 基于热冲击因子计算的动态热应力及岩石热损伤判据（σ*_T* ≥ σ*_cri*）可为岩石热破坏理论发展提供支撑。

## Candidate Concepts
- [[热冲击因子]] (Thermal shock factor)  
- [[温度梯度]] (Temperature gradient)  
- [[岩石热损伤]] (Rock thermal damage)  
- [[动态热应力]] (Dynamic thermal stress)  
- [[传导加热]] (Conduction heating)  
- [[非均质性]] (Heterogeneity)  
- [[矿物颗粒分离]] (Mineral grain separation)  
- [[裂纹萌生与扩展]] (Crack initiation and propagation)  
- [[热破坏判据]] (Thermal failure criterion)

## Candidate Methods
- [[多通道温度同步采集方法]] (Multi-channel synchronous temperature acquisition)  
- [[埋入式温度传感器阵列]] (Embedded temperature sensor array)  
- [[热冲击因子试验测定法]] (Experimental measurement of thermal shock factor, Patent CN201811439431.2)  
- [[基于温度梯度的动态热应力反演]] (Dynamic thermal stress inversion from temperature gradient)  
- [[温度梯度-时间特征曲线分析]] (Temperature gradient‑time characteristic curve analysis)

## Connections To Other Work
- 本文直接引用 Lidman & Bobrowsky (1949) 的热应力公式，将动态热应力与温度梯度、热冲击因子关联，延续了热冲击因子在陶瓷材料评价中的思路[Xi 2020, pp. 1-4]。  
- 与作者团队前期关于热冲击速度与花岗岩宏观力学参数关系的研究（Xi et al., 2019, 2020）一脉相承，进一步将热冲击因子用于热损伤能力定量表征[Xi 2020, pp. 13-13]。  
- 参考了林睦曾 (1991) 的岩石热物理学和赵阳升等 (2004) 的干热岩地热开发理论，将热冲击因子纳入岩石热破坏理论框架[Xi 2020, pp. 1-4]。  
- 其他学者如 Tang et al.（2016, 2018）关于热破裂的理论和数值研究，以及 Winkelman & Schott (1894)、Norton (1926) 的早期工作，为本实验的物理背景提供了参考[Xi 2020, pp. 13-13]。

## Open Questions
- 热冲击因子与花岗岩矿物组成、颗粒尺寸、微裂隙密度的定量关系尚未建立。  
- 不同冷却方式（如水中淬冷、空气自然冷却）对热冲击因子演变的影响未在本文探讨。  
- 三维非均质岩体中热冲击因子的分布规律及其与宏观力学强度（抗压、抗拉）的直接关联缺乏实验验证。  
- 多次循环加热后热冲击因子的累积变化特征及热疲劳退化规律未知。  
- 热冲击因子临界值与岩石固有强度参数（抗拉强度、断裂韧度）的映射关系需结合力学试验进一步标定。

## Source Coverage
所有非空索引片段（共 4 段，总计 16 420 字符）均已处理并用于构建本页。编译时实际使用字符数 14 894，按区块覆盖率 100%，按字符覆盖率约 90.7%。无额外虚构内容。
