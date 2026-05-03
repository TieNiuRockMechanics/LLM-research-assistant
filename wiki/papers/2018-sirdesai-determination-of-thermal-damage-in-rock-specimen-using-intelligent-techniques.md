---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2018-sirdesai-determination-of-thermal-damage-in-rock-specimen-using-intelligent-techniques"
title: "Determination of Thermal Damage in Rock Specimen Using Intelligent Techniques."
status: "draft"
source_pdf: "data/papers/2018 - Determination of thermal damage in rock specimen using intelligent techniques.pdf"
collections:
  - "论文"
citation: "Sirdesai, Nikhil Ninad, et al. \"Determination of Thermal Damage in Rock Specimen Using Intelligent Techniques.\" *Engineering Geology*, vol. 239, 2018, pp. 179-94. doi:10.1016/j.enggeo.2018.03.027."
indexed_texts: "13"
indexed_chars: "64164"
nonempty_source_blocks: "13"
compiled_source_blocks: "13"
compiled_source_chars: "64495"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.005159"
coverage_status: "full-index"
source_signature: "675e9e99c41df7a36f355767a4106697ad0b7b40"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T20:24:35"
---

# Determination of Thermal Damage in Rock Specimen Using Intelligent Techniques.

## One-line Summary
针对细粒 Dholpur 砂岩，利用多变量回归分析（MVRA）、人工神经网络（ANN）及自适应神经模糊推理系统（ ANFIS）由热处理后的物理性质预测热损伤程度 D(T)，结果表明 ANFIS 具有最高的预测精度。

## Research Question
能否仅凭易于获取的热处理后物理性质（孔隙度、密度、热膨胀系数、超声波波速及温度），借助统计与软计算工具准确估测岩石试样的热损伤程度 D(T)，从而避免依赖耗时且需专用设备的弹性模量测试？

## Study Area / Data
- **研究区/材料**：印度拉贾斯坦邦 Dholpur 地区的细粒砂岩（Dholpur sandstone），属 Vindhyan 超群上 Bhander 组。该砂岩实际未受化学淋滤，无双重孔隙，历史上用于 Rashtrapati Bhavan、印度国会、德里红堡等重要建筑 [Sirdesai 2018, pp. 1-3]。
- **矿物组成**：XRD 分析显示主要为石英（约 91–93.5%）和长石（约 6.5–8.8%），含少量云母和辉石的硅质胶结，呈单矿物性，化学性质稳定，热致力学性质变化主要与微裂纹演化有关 [Sirdesai 2018, pp. 3-5, 5-6]。
- **数据集**：共 63 个圆柱试样（长度/直径＝2:1），垂直于层理取芯，经 50 ℃ 间隔热处理至最高 1000 ℃（升温速率 5 ℃/min，保温 120 h，室温下冷却 120 h）。每个温度点至少 3–4 个试样 [Sirdesai 2018, pp. 3-5]。训练用 45 个数据集，其余用于检验；Table 2 详细列出各温度下孔隙度（P）、线/体热膨胀系数（E_L, E_V）、密度（D）、纵/横波波速（V_P, V_S）及热损伤 D(T) 的统计值 [Sirdesai 2018, pp. 5-6]。

## Methods
- **热损伤定义**：基于 Hueckel 等（1994）的方法，\( D(T)=1 - E_T/E_0 \)，其中 E_T 为温度 T 时的弹性模量，E_0 为室温弹性模量。弹性模量在应力-应变曲线裂纹闭合与裂纹起始阈值间的线弹性段读取，分析窗口为 5–20 MPa [Sirdesai 2018, pp. 1-2, 6-7]。
- **输入参数测定**：有效孔隙度采用浮力与饱和法（ISRM 建议）；密度和热膨胀系数通过热处理前后的尺寸与质量计算；波速用 Proceq PUNDIT Lab+ 仪器测量；热分析（TG/DTA）在相同升温条件下进行，XRD 用于矿物表征 [Sirdesai 2018, pp. 3-7]。
- **预测模型**：
  - **MVRA**：建立 D(T) 与 P, D, E_L, E_V, V_P, V_S 的线性回归方程（Eq. 15） [Sirdesai 2018, pp. 11]。
  - **ANN**：前馈反向传播网络，7 个输入节点，1 个含 10 个神经元的隐含层（log‑sigmoid / tan‑sigmoid 传递函数），输出 D(T)。采用 LM、SCG、OSS 三种训练算法（最大 500 个世代），数据预先归一化 [Sirdesai 2018, pp. 7-9, 11-12]。
  - **ANFIS**：基于 Sugeno 模糊推理的五层结构，通过减法聚类生成模糊推理系统，输入使用高斯隶属度函数，输出为线性函数，共 13 条模糊规则。训练采用混合学习算法（正向最小二乘确定后件参数，反向梯度下降更新前件参数），共训练 50 个世代 [Sirdesai 2018, pp. 9-11, 12-14]。
- **性能指标**：以决定系数（R²）、平均绝对百分误差（MAPE）、均方根误差（RMSE）和方差占比（VAF）评估各模型 [Sirdesai 2018, pp. 14-15]。

## Key Findings
1. **温度驱动特性演变**：Dholpur 砂岩在 300–500 ℃ 区间存在临界温度区（CTZ），初期微裂纹闭合使密度和波速上升、孔隙度下降，D(T) 出现负值（“愈合”效应）；超过 CTZ 后，因各向异性膨胀和石英 α→β 转变（~579 ℃），微裂纹急剧萌生、扩展，导致孔隙度增大、波速和密度降低，弹性模量下降，D(T) 转为正值并持续增大 [Sirdesai 2018, pp. 9-11]。
2. **模型预测精度对比**：
   - ANN 训练算法中，Levenberg‑Marquardt (LM) 效果最佳（R²=0.725）；SCG 次之（R²≈0.710），OSS 最差（R²≈0.694） [Sirdesai 2018, pp. 14-15]。
   - 三类模型最终比较：ANFIS 远优于 ANN 和 MVRA，其 R² = 0.999、RMSE = 0.39、VAF = 97.34%、MAPE = 0.89%；MVRA 的 R² 仅 0.687 [Sirdesai 2018, pp. 14-15]。
3. **可行性**：利用 P, D, E_L, E_V, V_P, V_S 及温度 T 等常规物理指标，即可通过 ANFIS 模型快速、低成本、高精度地评估热损伤程度，无需进行弹性模量等破坏性或复杂的实验室测试 [Sirdesai 2018, pp. 15-16]。

## Core Evidence Table
| 证据 | 来源 | 条件/数据 | 注释 |
|------|------|-----------|------|
| D(T)=1 − E_T/E_0，据弹性模量变化量化热损伤 | [Sirdesai 2018, pp. 1-2] | 弹性模量 E_T 取自 5–20 MPa 应力窗口 | 损伤值在 CTZ 以下为负（弹性模量升高），高温时为正值 |
| 矿物成分主要为石英（91.2–93.5%）和长石（6.5–8.8%），粘土矿物极微量 | [Sirdesai 2018, pp. 3-5] (Table 1, Fig. 3) | Dholpur 砂岩，25–1000 ℃ 分析 | TGA 质量损失极小，DTA 在 579.19 ℃ 出现石英反转吸热峰 |
| CTZ 位于 300–500 ℃，其下微裂纹闭合、愈合；其上微裂纹萌生与扩展 | [Sirdesai 2018, pp. 9-11] (Fig. 7) | 升温速率 5 ℃/min，保温 120 h | 密度、波速、孔隙度的转折与此一致 |
| MVRA 方程 D(T)=0.24−0.03(P)−0.01(D)−0.04(EL)−0.06(EV)−0.02(VP)−0.07(VS)−0.33(T) | [Sirdesai 2018, pp. 11] (Eq. 15) | 归一化变量 | 解释力有限（R²=0.687） |
| ANN (LM) 预测结果：R²=0.725，残差 6.88 | [Sirdesai 2018, pp. 14-15] (Table 5, 6) | 单隐层（10 神经元），LM 训练 | 优于 SCG、OSS |
| ANFIS 最终性能：R²=0.999，RMSE=0.39，VAF=97.34%，MAPE=0.89% | [Sirdesai 2018, pp. 14-15] (Table 6, Fig. 15, 16) | 减法聚类，高斯隶属函数，13 规则，50 epochs | 对所有 63 个数据集拟合最优 |

## Limitations
- 模型仅针对 Dholpur 细粒石英砂岩建立，对其他岩性（含碳酸盐、粘土矿物较高等）的适用性未经检验 [Sirdesai 2018, pp. 15-16]。
- 热处理条件固定（升温 5 ℃/min，保温 120 h，慢速室温冷却），不同加热速率或冷却方式可能改变损伤路径 [Sirdesai 2018, pp. 3-5]。
- 训练和测试样本量为 63，且最高温度 1000 ℃；极端高温或更宽温度范围的预测精度未验证。
- 有效孔隙度测量采用浸水法，仅适用于非膨胀性岩石 [Sirdesai 2018, pp. 6-7]。
- 损伤量 D(T) 仅基于准静态弹性模量，未考虑动态加载或蠕变等损伤形式。

## Assumptions / Conditions
- 岩石为均质、无非均质性扰动的细粒砂岩，无化学淋滤 [Sirdesai 2018, pp. 1-3]。
- 热损伤可完全由热处理后样品的整体物理性质（P, D, EL, EV, VP, VS）及温度 T 表征 [Sirdesai 2018, pp. 1-7]。
- 热处理过程中升温速率恒定（5 ℃/min），达到目标温度后保温 120 h，然后自然冷却 120 h [Sirdesai 2018, pp. 3-5]。
- 弹性模量在 5–20 MPa 应力窗口内获取，且该窗口位于线弹性段 [Sirdesai 2018, pp. 6-7]。
- 输入参数之间不存在完全共线性，但可能存在一定相关性（如 V_P 与密度），软计算模型可隐式处理。

## Key Variables / Parameters
- **输出变量**：热损伤 D(T) (无量纲，负值表示弹性模量增加) [Sirdesai 2018, pp. 1-2]
- **输入变量**：
  - 温度 T (℃)
  - 有效孔隙度 P (%)
  - 线热膨胀系数 E_L (°C⁻¹)
  - 体积热膨胀系数 E_V (°C⁻¹)
  - 密度 D (g·cm⁻³)
  - 纵波波速 V_P (m·s⁻¹)
  - 横波波速 V_S (m·s⁻¹)
- **中间测定量**：弹性模量 E (GPa) [Sirdesai 2018, pp. 6-7]
- **性能指标**：R², MAPE, RMSE, VAF [Sirdesai 2018, pp. 14-15]

## Reusable Claims
1. 对于以石英为主、粘土矿物含量极低的细粒砂岩，可通过热处理后的 P, D, E_L, E_V, V_P, V_S 及 T 利用 ANFIS 模型高精度预测热损伤 D(T)（R²=0.999, MAPE<1%）。**条件**：升温速率 5 ℃/min，保温 120 h，缓慢室温冷却；输入参数按 ISRM 建议方法测得 [Sirdesai 2018, pp. 14-15]。
2. 在此类岩石中，CTZ 约为 300–500 ℃；低于 CTZ 时 D(T) 可为负，表明热“愈合”效应；高于 CTZ 后 D(T) 随温度单调增加，标志着累积损伤 [Sirdesai 2018, pp. 9-11]。该结论适用于经历了相同热处理历程的细粒石英砂岩。
3. ANFIS 在预测地质材料热损伤时相比传统 MVRA 和 ANN（LM）具有更高的泛化能力，其残差极小（RMSE=0.39），可用于快速现场评估 [Sirdesai 2018, pp. 14-16]。**局限**：需要足够数量的训练样本覆盖温度区间。

## Candidate Concepts
- [[thermal damage]]
- [[critical temperature zone]]
- [[ultrasonic wave velocity]]
- [[porosity]]
- [[thermal expansion coefficient]]
- [[elastic modulus]]
- [[stress-strain behavior]]

## Candidate Methods
- [[multivariate regression analysis]]
- [[artificial neural network]]
- [[Levenberg-Marquardt algorithm]]
- [[ANFIS]]
- [[X-ray diffraction]]
- [[thermogravimetric/differential thermal analysis]]
- [[ultrasonic pulse velocity measurement]]
- [[ISRM suggested methods]]

## Connections To Other Work
- 热损伤的定义 D(T)=1−E_T/E_0 直接采用 Hueckel 等 (1994) 的框架 [Sirdesai 2018, pp. 1-2]。
- 前人研究已用超声波波速和声发射评估热损伤（Chaki et al. 2008; Eberhardt et al. 1999; 等），但需要合规的试样和设备，本研究提出由常规物理性质替代的路径 [Sirdesai 2018, pp. 1-3]。
- 与先前用 ANN、ANFIS 预测岩石强度（Yilmaz and Yuksek 2009; Singh et al. 2012）的思路一致，但将此扩展到热损伤这种派生变量 [Sirdesai 2018, pp. 3]。
- 论文中 Dholpur 砂岩的 CTZ 行为与 Liu and Xu (2015)、Tian et al. (2015) 等报道的其他砂岩类似，临界温度与石英反转温度相关 [Sirdesai 2018, pp. 9-11, 5-6]。

## Open Questions
- ANFIS 模型能否迁移至含较多粘土或碳酸盐矿物的砂岩，预测精度如何？[未在文中验证]
- 在更快的升温速率或不同冷却路径（如水冷）下，本预测模型的可靠性尚待研究。[仅研究了缓慢冷却]
- 若加入声发射特征或微观 CT 参数作为输入，能否进一步提升预测精度？
- 模型在超过 1000 ℃ 或极长热暴露时间（如核废料处置）场景下的适用性未探索。
- 如何将单块试样尺度的损伤预测扩展到岩体尺度的等效热损伤评估？

## Source Coverage
所有非空索引片段（共 13 个，覆盖 64164 字符）均已处理并纳入本页面。编译后源字符数为 64495，覆盖率（基于区块数）为 1.0，基于字符比为 1.005，源指纹为 `675e9e99c41df7a36f355767a4106697ad0b7b40`，达到完全索引状态。
