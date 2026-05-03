---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2025-tian-assessment-method-of-surface-morphology-based-on-100-shear-tests-and-pso-rbf-neural-ne"
title: "Assessment Method of Surface Morphology Based on 100 Shear Tests and PSO-RBF Neural Network."
status: "draft"
source_pdf: "data/papers/2025 - Assessment Method of Surface Morphology Based on 100 Shear Tests and PSO-RBF Neural Network.pdf"
collections:
  - "zotero new"
citation: "Tian, Yongchao, et al. \"Assessment Method of Surface Morphology Based on 100 Shear Tests and PSO-RBF Neural Network.\" *Rock Mechanics and Rock Engineering*, vol. 58, 2025, pp. 9089–9125. doi:10.1007/s00603-025-04566-w."
indexed_texts: "26"
indexed_chars: "128191"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T14:57:05"
---

# Assessment Method of Surface Morphology Based on 100 Shear Tests and PSO-RBF Neural Network.

## One-line Summary
本研究针对现有结构面粗糙度系数（JRC）数据集和定量方法的缺陷，从数百个形态参数中筛选出8个代表性参数，利用85个砂岩试件剖面经熵权‑TOPSIS排序后等间隔选取100个剖面，通过CNC雕刻制作试件并进行直剪试验，在此基础上提出基于粒子群优化‑径向基函数（PSO‑RBF）神经网络的表面形态评估方法 [Tian 2025, pp. 1‑2]。

## Research Question
如何克服现有JRC反算和视觉比对方法的主观性，建立一套可靠的profile‑JRC数据集，并构建能够综合多个形态参数信息、准确量化结构面表面形态的机器学习模型？现有数据集中有哪些系统性缺陷需被修正？ [Tian 2025, pp. 1‑3]

## Study Area / Data
- 原始剖面数据来源于85个砂岩试件，通过熵权‑TOPSIS方法对提取的大量剖面进行粗糙度排序，等间隔选出100个剖面 [Tian 2025, pp. 1‑2]。
- 利用CNC雕刻技术将这100个剖面加工成结构面试件，进行直接剪切试验，并利用JRC‑JCS模型反算每个剖面的JRC值 [Tian 2025, pp. 1‑2]。
- 模型训练与验证所依据的profile‑JRC数据集包含上述100组直剪试验结果；文中系统梳理了Barton (1976)、Bandis (1980)、Bandis et al. (1983)、Grasselli (2001) 等历史数据集及其局限性 [Tian 2025, pp. 10‑12]。
- 试件岩性、具体产地与取样工程背景未从索引片段中确认。

## Methods
1. **代表性形态参数筛选**：从数百个形态参数中，考察物理意义、文献使用频率及与JRC的相关性，选定8个最具代表性的参数：Z₂, Rp, CLA, RMS, Rz, Sp, θ\*ₘₐₓ/(C+1), θₐᵥₑ [Tian 2025, pp. 1, 3‑5]。
2. **剖面选取与试件制备**：采用熵权‑TOPSIS法对85个砂岩试件提取的剖面进行粗糙度水平排序，等间隔选取100个剖面；采用CNC雕刻工艺制备含目标剖面的结构面试件 [Tian 2025, pp. 1‑2]。
3. **直剪试验与JRC反算**：对100个试件开展直接剪切试验，通过JRC‑JCS模型（式9：τₚ = σₙ tan(JRC·log₁₀(JCS/σₙ)+φ_b)）反算每个剖面对应的JRC值 [Tian 2025, pp. 1‑2, 7‑8]。
4. **PSO‑RBF神经网络建模**：基于上述数据集，构建粒子群优化‑径向基函数神经网络模型，以综合评价结构面形态特征 [Tian 2025, pp. 2‑3]。

## Key Findings
- 现有profile‑JRC数据集存在六大类缺陷：试件取样代表性不足；剖面清晰度低、难以与JRC值准确匹配；JRC值分布范围过宽；细节信息捕捉困难；实验反算法中代表性剖面选取主观，且直接将试件JRC赋予剖面不合理；剖面比较法中代表性剖面与标准剖面的选取均基于主观判断，不同学者视觉比对结果离散性大（42%相对误差超过0.2） [Tian 2025, pp. 5‑8]。
- 试件尺寸（长70 ~ 140 mm，宽20.3 ~ 140 mm）存在显著差异，但原始文献未考虑尺寸效应对试验结果的影响 [Tian 2025, pp. 8‑10]。
- 基于100组直剪试验构建的profile‑JRC数据集，避免了传统方法的主观性问题，其具体精度与PSO‑RBF模型的验证性能未从索引片段中确认。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 八个代表性形态参数（Z₂, Rp, CLA, RMS, Rz, Sp, θ\*ₘₐₓ/(C+1), θₐᵥₑ）具有明确的物理意义、高文献频率且与JRC显著相关 | [Tian 2025, pp. 1, 3‑5] | 参数来自数百个候选参数，筛选基于文献调研与相关性分析 | 角度型参数（前四个）的预测性能一般优于高度型参数（后四个） |
| 现有profile‑JRC数据集存在六类主要缺陷（主观选取代表性与标准剖面、反算JRC直接赋予剖面、视觉比对一致性差、尺寸差异显著等） | [Tian 2025, pp. 5‑10] | 综合分析Barton (1976)、Bandis (1980)、Bandis et al. (1983)、Grasselli (2001) 的数据集 | 12位学者对同一剖面视觉比对JRC值，42%的相对误差超过0.2 [Tian 2025, pp. 8] |
| 表1汇总了基于Z₂、Rp、θ\*ₘₐₓ/(C+1)等参数的多个JRC定量模型及其拟合优度（R），来源于多名研究者的成果 | [Tian 2025, pp. 5‑7] | 模型多基于十标准剖面或特定工程剖面，采样间隔δ=0.1~2 mm | 本文仅引用以说明参数代表性，非直接证据 |
| 熵权‑TOPSIS法排序后等间隔选出的100个剖面，经CNC雕刻与直剪试验建立了新的profile‑JRC数据集 | [Tian 2025, pp. 1‑2] | 原始剖面来自85个砂岩试件；直剪试验后采用JRC‑JCS模型反算 | 详细试验参数（法向应力、JCS值等）未从索引片段中确认 |

## Limitations
- 本页依据的索引片段主要覆盖引言、方法设计、数据集缺陷分析，未包含模型的训练集/测试集划分、预测精度、鲁棒性验证等结果 [Source Coverage]。
- 试件剖面均源于砂岩，岩性单一，向其他岩类的推广性未从片段确认。
- 试验采用CNC雕刻仿真节理面，其与天然风化、蚀变节理面的等效性未从片段论证。
- 考虑尺寸效应的控制实验未见描述。

## Assumptions / Conditions
- 直接剪切试验反算JRC依赖JRC‑JCS模型（τₚ = σₙ tan(JRC·log₁₀(JCS/σₙ)+φ_b)）的有效性，假设基本摩擦角φ_b和壁面抗压强度JCS已知且准确 [Tian 2025, pp. 7‑8]。
- 剖面粗糙度排序和代表性参数的选取基于85个砂岩试件的统计数据，隐含了该样本集能充分代表砂岩结构面形态多样性的假设。
- PSO‑RBF网络能有效融合8个形态参数并消除信息冗余，隐含输入参数间存在非线性互补关系的前提 [Tian 2025, pp. 2‑3]。

## Key Variables / Parameters
- **形态参数**：Z₂（一阶导数均方根），Rp（粗糙度轮廓指数），CLA（中心线平均高度），RMS（均方根高度），Rz（最大峰谷高度），Sp（最大峰高），θ\*ₘₐₓ/(C+1)（基于3D点云的有效倾角参数），θₐᵥₑ（平均绝对倾角） [Tian 2025, pp. 3‑5]。
- **直剪试验参数**：峰值强度τₚ、法向应力σₙ、基本摩擦角φ_b、壁面抗压强度JCS [Tian 2025, pp. 7‑8]。
- **模型参数**：PSO‑RBF网络的具体结构（隐含层神经元数、径向基函数宽度、粒子群参数等）未从索引片段中确认。

## Reusable Claims
- 现有profile‑JRC数据集的缺陷可归纳为取样代表性不足、剖面‑JRC匹配困难、JRC分布范围过宽、细节捕捉能力差、反算法与视觉比对法均存在主观性偏差等类别 [Tian 2025, pp. 5‑8]。适用条件：分析历史文献提供的2D剖面数据集。限制：分类基于作者总结，部分数据集的尺寸信息不完整。
- 角度型形态参数（Z₂, Rp, θ\*ₘₐₓ/(C+1), θₐᵥₑ）在预测JRC时普遍优于高度型参数（CLA, RMS, Rz, Sp），可优先作为粗糙度模型的输入变量 [Tian 2025, pp. 3‑5]。证据来自表1中大量模型的回归统计。限制：该结论仍依赖于采样间隔、剖面长度及岩性背景。
- 采用熵权‑TOPSIS对大量剖面排序后等间隔采样，能够在避免主观挑选的同时保证数据集中粗糙度分级的均匀覆盖 [Tian 2025, pp. 1‑2]。适用条件：需要先提取足够数量的剖面并计算多个形态参数。限制：最终数据集仅包含100个剖面，可能无法完整反映真实分布。

## Candidate Concepts
- [[joint roughness coefficient (JRC)]]
- [[JRC-JCS shear strength model]]
- [[surface morphology quantification]]
- [[representative morphology parameters]]
- [[profile-JRC dataset]]
- [[visual comparison method]]
- [[entropy weight-TOPSIS method]]
- [[PSO-RBF neural network]]
- [[scale effect in rock joints]]

## Candidate Methods
- [[direct shear test]]
- [[experimental result inversion method]]
- [[profile comparison method]]
- [[straight-edge method]]
- [[statistical parameter method]]
- [[fractal geometry method]]
- [[CNC engraving for rock joint replicas]]
- [[3D point cloud morphology analysis]]

## Connections To Other Work
- 本文系统引用了Barton (1976)、Bandis (1980)、Bandis et al. (1983)、Grasselli (2001) 等构建的经典profile‑JRC数据集，并指出这些早期数据集在代表性、主观性与尺寸控制方面的不足 [Tian 2025, pp. 5‑10]。
- 文中与Li and Zhang (2015)、Tatone and Grasselli (2010)、Yu and Vayssade (1991)、Jang et al. (2014) 等研究的JRC定量模型进行对比，验证选定8个参数的代表性及预测能力，但未在片段中展示直接比较结果 [Tian 2025, pp. 3‑7]。
- 可从主题上连接到任何基于[[PSO-RBF]]、[[artificial neural network for rock joint]]、[[shear test database construction]]的研究，但具体模型性能比较未从索引片段中确认。

## Open Questions
- PSO‑RBF神经网络模型的预测精度、训练时间、与现有经验公式及传统BP网络的对比结果未从索引片段中确认。
- 该模型是否适用于三维表面形态（面粗糙度）量化，是否有3D点云数据的直接输入接口？
- 新数据集与历史数据集在共同剖面或共同标准下的验证一致性如何？
- 尺寸效应（剖面长度、试件宽度）对反算JRC的敏感性量化未涉及。
- 其他岩性（如灰岩、花岗岩、页岩）的适用性尚未验证。

## Source Coverage
本页依据论文索引片段中的26个片段撰写，主要覆盖摘要、引言（研究背景与动机）、代表性参数选取（部分）、现有profile‑JRC数据集的详细缺陷分析（Chapter 3.1‑3.2）以及实验设计与方法概述。**缺失的核心内容**包括：PSO‑RBF模型的具体结构、训练与验证过程、模型性能指标（R²、RMSE等）、与其它方法的定量对比、全部100组直剪试验的反算JRC结果、讨论与结论部分。因此，关于模型有效性和新数据集优越性的具体证据尚无法从片段中获得。
