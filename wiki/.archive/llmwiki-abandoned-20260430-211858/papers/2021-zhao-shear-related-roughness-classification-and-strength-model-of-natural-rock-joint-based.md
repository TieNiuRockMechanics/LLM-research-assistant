---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2021-zhao-shear-related-roughness-classification-and-strength-model-of-natural-rock-joint-based"
title: "Shear-Related Roughness Classification and Strength Model of Natural Rock Joint Based on Fuzzy Comprehensive Evaluation."
status: "draft"
source_pdf: "data/papers/2021 - Shear-related roughness classification and strength model of natural rock joint based on fuzzy comprehensive evaluation.pdf"
collections:
  - "zotero new"
citation: "Zhao, Yanlin, et al. \"Shear-Related Roughness Classification and Strength Model of Natural Rock Joint Based on Fuzzy Comprehensive Evaluation.\" *International Journal of Rock Mechanics & Mining Sciences*, vol. 137, 2021, article no. 104550. Accessed 2026."
indexed_texts: "16"
indexed_chars: "77376"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T03:17:10"
---

# Shear-Related Roughness Classification and Strength Model of Natural Rock Joint Based on Fuzzy Comprehensive Evaluation.

## One-line Summary
本文基于模糊综合评价提出了一种新的岩石节理剪切相关粗糙度系数FRC，并建立了FRC‑JCS剪切强度模型，该模型比传统JRC‑JCS模型更全面地反映多形态参数对节理剪切强度的影响 [Zhao 2021, pp. 1‑1]。

## Research Question
如何建立一种能够综合考虑节理表面多形态参数（幅度、角度、曲率等）的粗糙度量化方法，并将其嵌入剪切强度模型，以解决JRC‑JCS模型因仅依赖单一参数而倾向于低估天然岩石节理剪切强度的问题 [Zhao 2021, pp. 1‑2]。

## Study Area / Data
未从索引片段中确认。片段仅指出试验采用了三种天然岩石节理：大理石（marble）、二辉橄榄岩（lherzolite）和角闪岩（amphibolite），并对每种岩石各制备三个含天然节理的试样 [Zhao 2021, pp. 2‑3]。标准节理剖面选用Barton和Choubey提出的十条标准剖面，并以0.5 mm采样间隔数字化 [Zhao 2021, pp. 2‑3]。

## Methods
- **节理表面形貌测量**：利用Talysurf CLI形态仪扫描天然节理表面，提取二维剖面数据。计算高度统计参数（算术平均高度Sₘ、均方根高度S_q、峰度S_k、偏度S_s）和纹理统计参数（面向剪切方向的粗糙体均方根角S_i、剖面均方根梯度Z₂、曲率类参数S_c）。基于Sₘ与S_q、Z₂与S_i之间的强正相关，最终选取S_i、S_q、S_c、S_k四个参数作为与剪切行为相关的主要影响因子 [Zhao 2021, pp. 1‑1, 4‑5]。
- **模糊综合评价（FCE）**：
  - 建立评价因子集U = {S_i, S_q, S_c, S_k} [Zhao 2021, pp. 8‑9]。
  - 设定评价等级集V = {1, 2, …, 10}，将粗糙度从极光滑至极端粗糙分为十级 [Zhao 2021, pp. 8‑9]。
  - 采用高斯型隶属函数构建单因素评价矩阵R，将各因子的模糊性量化为对十个等级的隶属度 [Zhao 2021, pp. 9‑10]。
  - 通过多因子综合评判得到断裂粗糙度系数FRC [Zhao 2021, pp. 1‑1]。
- **剪切强度模型**：将FRC替代JRC嵌入Barton型剪切强度公式，形成FRC‑JCS模型 [Zhao 2021, pp. 1‑1]。
- **试验验证**：对三种岩石的天然节理试样进行多阶段直剪试验。每块试样在0.4、0.8、1.2、1.6 MPa四级常法向载荷（CNL）下剪切，剪切位移速率0.5 mm/min，直至位移达约10 mm。每次剪切前将节理重新对准至初始天然匹配位置。试验遵循ISRM建议方法 [Zhao 2021, pp. 4‑5]。基本摩擦角通过锯切平面节理的直剪试验确定（具体数值未从索引片段中确认）[Zhao 2021, pp. 2‑3]。单轴抗压和抗拉强度试验遵循ASTM D2938和ASTM D3967 [Zhao 2021, pp. 4‑5]。

## Key Findings
1. 在天然岩石节理中，Sₘ与S_q、Z₂与S_i之间存在强线性正相关关系（例如Z₂ = 0.0182 S_i，R² = 0.992），表明部分高度和纹理参数存在冗余 [Zhao 2021, pp. 5‑7]。
2. JRC‑JCS模型倾向于低估天然节理的剪切强度，主要原因在于未能综合考虑多种形态特性 [Zhao 2021, pp. 1‑2]。
3. 基于FCE融合S_i、S_q、S_c、S_k四个参数得到的断裂粗糙度系数FRC，其数值通常高于传统JRC值 [Zhao 2021, pp. 1‑1]。
4. 所提出的FRC‑JCS剪切强度模型比以往发表的模型能更全面地体现节理表面形态参数对剪切强度的影响（具体增幅或对比数据未从索引片段中确认）[Zhao 2021, pp. 1‑1]。
5. 多级CNL直剪试验表明，峰值强度和残余强度均随法向应力增加而升高，大部分曲线呈现明显的峰值和残余段 [Zhao 2021, pp. 7‑8]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| FRC通常高于JRC | [Zhao 2021, pp. 1‑1] | 基于大理石、二辉橄榄岩、角闪岩天然节理的FCE分析；评价因子为S_i、S_q、S_c、S_k；标准节理剖面数字化间隔0.5 mm | 未给出具体高出数值；结论源于摘要陈述 |
| JRC-JCS模型低估天然节理剪切强度 | [Zhao 2021, pp. 1‑2] | 引用文献42‑55的实验结果；对比对象为天然岩石节理 | 片段仅提及“许多实验结果”表明该趋势，未列出具体对比数据 |
| Z₂与S_i呈强线性关系：Z₂ = 0.0182 S_i (R² = 0.992) | [Zhao 2021, pp. 5‑7] | 数据来源：天然岩石节理（三种岩石共9个表面）的二维剖面 | 强相关说明这两个纹理参数传递的信息高度重叠 |
| FRC-JCS模型能更全面反映多形态参数对剪切强度的影响 | [Zhao 2021, pp. 1‑1] | 基于FCE综合S_i、S_q、S_c、S_k | 具体比较对象为“previously published shear strength models”，片段未命名 |
| 直剪试验下峰值和残余强度随法向应力增加而上升 | [Zhao 2021, pp. 7‑8] | CNL条件，法向应力0.4~1.6 MPa，天然节理试样 | 未提供具体强度数值 |

## Limitations
- 索引片段未提供FRC的具体计算公式或隶属函数参数化细节，无法评估模型的可复现性 [Zhao 2021, 整体]。
- 片段中未报告FRC‑JCS模型与其他模型的定量比较结果（如预测误差、平均偏差等），难以判断改进的实际幅度 [Zhao 2021, pp. 1‑1]。
- 试验仅涵盖三种岩石类型（大理石、二辉橄榄岩、角闪岩）和四级低法向应力（0.4~1.6 MPa），模型外推至其他岩性或高应力条件的适用性未从索引片段中确认。
- 数据仅来自二维剖面参数的统计，三维表面综合形貌的利用程度在片段中未说明。

## Assumptions / Conditions
- 节理粗糙度的评判可用四个参数（S_i、S_q、S_c、S_k）通过模糊综合评判充分表达，且评价等级可线性划分为十级 [Zhao 2021, pp. 8‑9]。
- 采样间隔0.5 mm适用于所研究尺度的节理剖面形貌量化，这一间隔与Tse和Cruden建立Z₂‑JRC关系式的采样条件一致 [Zhao 2021, pp. 2‑3, 5‑7]。
- 直剪试验在常法向载荷（CNL）条件下进行，剪切过程中法向载荷保持不变 [Zhao 2021, pp. 4‑5]。
- 每次多阶段剪切前试样可准确复位至初始天然匹配位置；多次试验取平均值以减小结果离散性 [Zhao 2021, pp. 4‑5]。
- 基本摩擦角通过锯切平面节理的直剪试验确定，并假设该值可代表完整岩石节理的残余摩擦分量（此类假设为Barton模型常用前提） [Zhao 2021, pp. 2‑3]。

## Key Variables / Parameters
- **形态参数**：Sₘ（算术平均高度）、S_q（均方根高度）、S_k（峰度）、S_s（偏度）、Z₂（剖面均方根梯度）、S_i（面向剪切方向的粗糙体均方根角）、S_c（未展开全称，与曲率相关） [Zhao 2021, pp. 1‑1, 3‑4]。
- **粗糙度系数**：JRC（节理粗糙度系数）、FRC（断裂粗糙度系数，基于FCE的新指标） [Zhao 2021, pp. 1‑1]。
- **强度模型参数**：JCS（节理壁面抗压强度），模型形式为FRC‑JCS剪切强度模型 [Zhao 2021, pp. 1‑1]。
- **试验控制参数**：法向应力（0.4, 0.8, 1.2, 1.6 MPa）、剪切位移速率（0.5 mm/min）、剪切位移量（约10 mm） [Zhao 2021, pp. 4‑5]。
- **评价集**：V = {1, 2, …, 10}十级粗糙度 [Zhao 2021, pp. 8‑9]。
- **经验关系**：JRC = 32.2 + 32.47 log Z₂（Tse & Cruden公式，采样间隔0.5 mm）[Zhao 2021, pp. 5‑7]。

## Reusable Claims
1. 在天然岩石节理中，Z₂与S_i之间存在极强的线性正相关（Z₂ = 0.0182 S_i, R² = 0.992），因此两者在表征局部倾斜度时高度重叠，可以择一使用或进行降维 [Zhao 2021, pp. 5‑7]。（条件：采样间隔0.5 mm，剖面协方差符合文中定义；限制：仅基于三种岩石的有限剖面验证。）
2. FRC通过模糊综合评价将多形态参数（S_i, S_q, S_c, S_k）融合为单一指标，其值通常大于对应的JRC值 [Zhao 2021, pp. 1‑1]。（条件：评价因子需先归一化或使用高斯隶属函数，等级设定为1‑10级；限制：具体计算流程在片段中未完整揭露。）
3. 当采用CNL直剪时，随着法向应力从0.4 MPa升至1.6 MPa，天然节理的峰值强度和残余强度均单调升高 [Zhao 2021, pp. 7‑8]。（条件：天然粗糙节理，剪切位移速率0.5 mm/min，试样在各级法向应力下重新匹配；限制：仅适用于试验涵盖的三种岩石和应力范围。）
4. 传统JRC‑JCS模型因仅依赖单一粗糙度指标而无法捕获幅度、曲率等形态的独立影响，从而系统性低估天然节理剪切强度 [Zhao 2021, pp. 1‑2]。（条件：对比建立在多篇文献的实验证据上；限制：片段未给出具体低估幅度。）

## Candidate Concepts
- [[Rock Joint Shear Strength]]
- [[JRC-JCS Model]]
- [[Joint Roughness Coefficient]]
- [[Fuzzy Comprehensive Evaluation]]
- [[Morphological Parameters of Rock Joints]]
- [[Direct Shear Test under CNL]]
- [[Natural Rock Joint]]

## Candidate Methods
- [[Fuzzy Set Theory]]
- [[Gaussian Membership Function]]
- [[Talysurf CLI Morphology Instrument]]
- [[3D Laser Scanning of Rock Joints]]
- [[Multi-stage Direct Shear Test]]
- [[Statistical Roughness Parameters (Sm, Sq, Ss, Sk, Z2, Si, Sc)]]
- [[Barton Standard Joint Profiles Digitization]]

## Connections To Other Work
- 与 [[Barton and Choubey (1977) JRC-JCS model]] 直接关联：本文指出该模型低估天然节理强度，原因在于未考虑多形态参数，提出的FRC‑JCS模型旨在修正此缺陷 [Zhao 2021, pp. 1‑2]。标准剖面和JRC计算方法均直接引自该文献。
- 引用 [[Tse and Cruden (1979)]] 提出的Z₂与JRC的经验关系式（JRC = 32.2 + 32.47 log Z₂）来计算基准JRC值 [Zhao 2021, pp. 5‑7]。
- 模糊综合评价方法沿用 [[Zadeh (1965) Fuzzy Set Theory]] 的基础框架，并在岩石力学中已有前例应用于稳定性分类和岩体分级等领域（片段中列举了多项应用但未展开具体文献细节）[Zhao 2021, pp. 1‑2]。
- 索引片段未提及其他直接对比的强度模型，但根据主题可连接到 [[Grasselli roughness metric]]、[[fractal roughness description]] 等候选方法，均试图解决多尺度粗糙度捕捉问题。

## Open Questions
- FRC‑JCS模型在不同岩性、高法向应力及常刚度（CNS）条件下的适用性未从索引片段中确认。
- 模糊隶属函数（如高斯函数参数）的选择对FRC数值的灵敏度尚不清楚，片段未提供相关分析。
- FRC与传统JRC及三维粗糙度指标（如Grasselli提出的θ*max/(C+1)）的定量比较数据缺失。
- 模型预测效果相对于实际试验结果的定量误差统计未在片段中报告。

## Source Coverage
本页基于论文《Shear-Related Roughness Classification and Strength Model of Natural Rock Joint Based on Fuzzy Comprehensive Evaluation》（Zhao et al., 2021）的16个索引片段编写，片段总跨度从第1页至第10页（全文页码据片段显示至18页左右）。覆盖内容集中在摘要、部分引言、试验材料与方法（试样制备、形态参数测量）、部分试验结果（基本力学性质、JRC计算、剪切曲线特征）以及模糊综合评价的初始步骤。缺少的关键信息包括：FRC的具体计算流程、隶属度矩阵的构建细节、FRC‑JCS模型的数学表达式、模型与试验结果及与其它模型的定量对比、讨论部分以及全文结论。因此本页关于模型能力和精度方面的描述可能存在缺失，部分结论仅为摘要级陈述。
