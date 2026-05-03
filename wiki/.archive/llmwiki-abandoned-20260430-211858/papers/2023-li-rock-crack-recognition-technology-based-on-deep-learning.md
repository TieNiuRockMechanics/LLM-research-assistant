---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-li-rock-crack-recognition-technology-based-on-deep-learning"
title: "Rock Crack Recognition Technology Based on Deep Learning."
status: "draft"
source_pdf: "data/papers/2023 - Rock Crack Recognition Technology Based on Deep Learning.pdf"
collections:
  - "part1"
citation: "Li, Jinbei, et al. \"Rock Crack Recognition Technology Based on Deep Learning.\" *Sensors*, vol. 23, no. 12, 2023, article 5421, doi:10.3390/s23125421."
indexed_texts: "12"
indexed_chars: "59537"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T13:09:35"
---

# Rock Crack Recognition Technology Based on Deep Learning.

## One-line Summary

本研究提出了基于深度学习的岩石裂缝识别技术，首次将YOLOv7与注意力机制相结合，用于处理无人机采集的岩石表面图像，以实现对地质灾害前兆裂缝的快速、精确检测 [Li 2023, pp. 1-2]。

## Research Question

如何利用深度学习技术，特别是通过改进YOLOv7模型并引入注意力机制，从无人机拍摄的岩石表面图像中快速、准确地识别裂缝信息，以克服传统人工处理效率低下及实地调查受限的问题 [Li 2023, pp. 2-3]？

## Study Area / Data

- **研究区域**：粤港澳大湾区城市群，位于南岭南侧和南海北部，经纬度范围为111°59′ E ~ 115°28′ E，21°56′ N ~ 24°51′ N。该区域以台地、丘陵和平原地貌为主，海洋-陆地-大气相互作用强，气候复杂多变，年平均气温22°C，年降雨量2300毫米，属地质灾害易发区 [Li 2023, pp. 3-4]。
- **数据采集**：数据通过无人机（UAV）在野外拍摄获取，为增加数据集特征并防止模型过拟合，对同一岩体裂缝进行了多姿态、多角度拍摄。从大量图片中选取了200张具有不同形态和复杂背景的图像以提高样本代表性 [Li 2023, pp. 3-4]。
- **数据预处理**：将无人机拍摄的图像统一裁剪为640 × 640大小的小图片。利用数据增强技术（如角度变化、灰度化处理）将数据集从200张扩充至714张。之后，使用Labelimg工具进行标注，制作成用于裂缝目标检测的VOC数据集，并按2:8的比例划分为测试集和训练集 [Li 2023, pp. 1-2, 3-4]。

## Methods

- **基准模型**：以YOLOv5作为基准进行比较 [Li 2023, pp. 8]。
- **核心方法**：提出一种基于改进YOLOv7的岩石裂缝识别技术。其网络结构包含输入模块、骨干网络模块和颈部模块 [Li 2023, pp. 4-5]。
    - **输入模块**：采用Mosaic数据增强、Mixup数据增强、自适应锚框计算等技术 [Li 2023, pp. 4-5]。
    - **骨干网络**：包含ELAN结构和MP-1结构，用于高效的特征提取与聚合 [Li 2023, pp. 5-6]。
    - **颈部模块**：包含SPPCSPC结构、ELAN-1结构和REP结构。REP结构（结构重参数化）在保证精度的同时提升了运行速度 [Li 2023, pp. 5-6]。
- **创新点**：首次将YOLOv7与注意力机制结合，用于岩石裂缝检测 [Li 2023, pp. 1-2]。在YOLOv7的骨干网络之间插入了多种注意力机制进行对比研究 [Li 2023, pp. 3-4]，具体包括：CBAM（通道与空间注意力机制）、SE（通道注意力机制）、ECA、CA和SimAM（无参数注意力机制）。SimAM基于神经科学理论设计，考虑了空间抑制效应，通过定义能量函数来衡量神经元的重要性 [Li 2023, pp. 7-8]。

## Key Findings

- **模型参数与计算效率**：与基准YOLOv7（Baseline）相比，插入SimAM注意力机制后，模型的参数量（#Param.）和计算量（FLOPs）没有增加，均为37.620 M和106.472 G。而其他注意力机制（如CBAM、SE、ECA等）均不同程度地增加了模型参数 [Li 2023, pp. 8-10]。
- **性能比较**：研究通过比较分析，确定了最优的裂缝识别方案。但具体的精度、召回率、平均精度等性能指标的详细数值比较结果未从索引片段中确认。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| SimAM注意力机制在插入YOLOv7后未增加模型参数量和计算量，其#Param.为37.620 M，FLOPs为106.472 G，与Baseline相同。 | [Li 2023, pp. 8-10], Table 1 | 输入图像尺寸为640×640；模型为改进的YOLOv7 Baseline。 | 相比之下，CBAM、SE、ECA、CA等其他注意力机制均增加了参数量，可能降低模型效率。 |
| 模型基于神经科学理论中的空间抑制效应设计，通过最小化能量函数来评估神经元重要性。 | [Li 2023, pp. 7-8] | 这是SimAM注意力机制的理论基础，涉及公式 `et(wt, bt, y, xi) = ( yt− ∧ t )2 + ...` 。 | 该理论认为信息含量最高的神经元对周围神经元具有更强的抑制作用。 |

## Limitations

- 数据集可能具有局限性：虽然进行了数据增强，但初始选取的图像仅为200张，样本量相对有限，可能未能完全代表所有形态和地质环境下的岩石裂缝 [Li 2023, pp. 3-4]。
- 研究区域集中在粤港澳大湾区，模型的泛化能力未在其他气候和地质条件下的区域得到验证 [Li 2023, pp. 3-4]。
- 缺乏与传统或其它两阶段检测方法（如Faster-RCNN）在裂缝识别任务上的详细性能对比数据，文内仅与YOLOv5基准进行了比较 [Li 2023, pp. 8]。
- 模型性能（如精度、召回率）的关键实验结果未从索引片段中确认，无法评估其综合检测效果。

## Assumptions / Conditions

- **对象假设**：岩石表面的裂缝是滑坡、崩塌、泥石流等地质灾害的早期可识别前兆，通过视觉信息可以被捕获和识别 [Li 2023, pp. 1-2]。
- **数据条件**：假设通过无人机多角度拍摄、裁剪和数据增强（如灰度化）后的640×640图像，能够为深度学习模型提供充足且有效的特征，避免过拟合 [Li 2023, pp. 3-4]。
- **模型适用性**：假设单阶段目标检测模型（YOLOv7）在速度上的优势，结合注意力机制在特征聚焦上的能力，适用于处理大量无人机拍摄图像以提升效率 [Li 2023, pp. 2-3]。
- **实验对比前提**：将YOLOv5作为基准进行对比，隐含假设YOLOv5是该任务下当前较为先进的单阶段检测方法 [Li 2023, pp. 8]。

## Key Variables / Parameters

- **#Param. (参数量)**：衡量模型大小的指标，影响训练和推理效率。基准Baseline为37.620 M [Li 2023, pp. 8-10]。
- **FLOPs (计算量)**：衡量模型计算复杂度的指标。基准Baseline为106.472 G [Li 2023, pp. 8-10]。
- **注意力机制类型**：作为一个关键控制因素，包括SimAM, CBAM, SE, ECA, CA等 [Li 2023, pp. 7-8]。
- **性能评价指标**：包括精确度（Precision）、召回率（Recall）、平均精度（AP）和Time100（处理100张图片所需时间） [Li 2023, pp. 8-10]。具体公式为 Precision = TP / (TP + FP)，Recall = TP / (TP + FN) [Li 2023, pp. 8]。
- **图像输入尺寸**：640 × 640 [Li 2023, pp. 1-2, 8-10]。

## Reusable Claims

- **Claim 1**：在将注意力机制整合到YOLOv7骨干网络时，SimAM注意力机制可以在不增加任何参数量和计算量的前提下维持原模型的这些特性，这是其相对于CBAM、SE、ECA等其他主流机制的一个工程优势 [Li 2023, pp. 8-10]。
    - **适用条件**：应用于YOLOv7模型的特定位置（骨干网络之间），输入尺寸为640×640。
    - **证据**：Table 1显示，Baseline与Baseline + SimAM的#Param.和FLOPs数值完全一致，而其他机制的加入都导致参数量上升。
    - **限制**：此结论仅基于参数量和计算量数据，未涉及该机制对最终检测精度的影响。

- **Claim 2**：基于神经科学的能量最小化函数是设计SimAM注意力机制的理论核心，该函数用于量化目标神经元与其他神经元的线性可分性，以评估其重要性 [Li 2023, pp. 7-8]。
    - **适用条件**：将视觉注意力过程类比为生物视觉系统中的神经元竞争与抑制过程。
    - **证据**：片段中明确了SimAM的设计考虑了“空间抑制”属性，即活跃神经元抑制周围神经元，并提供了能量函数的具体定义。
    - **限制**：未从索引片段中确认该理论优势在实际裂缝检测任务中对精度提升的直接贡献程度。

## Candidate Concepts

- [[geological disaster early signs]]
- [[crack detection]]
- [[deep learning in geoscience]]
- [[object detection]]
- [[YOLOv7]]
- [[attention mechanism]]
- [[SimAM]]
- [[convolutional neural network]]
- [[UAV-based survey]]
- [[fatigue cracking]]

## Candidate Methods

- [[YOLOv7]]
- [[YOLOv5]]
- [[SimAM attention mechanism]]
- [[CBAM attention mechanism]]
- [[SE attention mechanism]]
- [[ECA attention mechanism]]
- [[CA attention mechanism]]
- [[Mosaic data augmentation]]
- [[Mixup data augmentation]]
- [[structural reparameterization (REP)]]

## Connections To Other Work

- **与目标检测方法的关系**：本文对比了单阶段检测方法（如YOLOv5, YOLOv7）和两阶段检测方法（如Faster-RCNN系列）的优缺点，指出YOLOv7在速度和精度上进行了优化，但未引用具体论文于此片段 [Li 2023, pp. 2-3, 8]。
- **与注意力机制研究的关系**：广泛引用了多种注意力机制的现有工作，包括通道注意力机制SENet (2018)、ECANet，空间注意力机制DCN, PSAnet, SASA，以及结合两者的CBAM (2018)、CA, SimAM等。具体引用关系未从索引片段中逐一确认 [Li 2023, pp. 7]。
- **与地质灾害识别方法的关系**：提及了基于微博数据的实时识别方法、SBAS-InSAR和SA-MFNet等多源数据融合分析方法，指出这些方法在时间敏感性和应用局限性上的问题 [Li 2023, pp. 2-3]。本文提出的方法旨在作为这些传统方法的一种补充，解决快速高效获取现场裂缝信息的问题。

## Open Questions

- 引入SimAM注意力机制的YOLOv7模型，在测试集上的精确度、召回率和平均精度等核心性能指标具体达到了多少？相较于其他注意力机制及YOLOv5基准的优势如何？
- 该模型在识别密集排列或微小裂缝时的具体表现如何？是否解决了传统单阶段检测器在此类场景下检测效果差的问题 [Li 2023, pp. 2-3]？
- 所使用的714张图片的VOC数据集具体如何划分？是否涵盖了独立的验证集以防止过拟合和进行超参数调优？

## Source Coverage

本页依据了论文的12个索引片段，内容覆盖了摘要、引言（包括相关方法概述）、研究区与数据描述、核心方法（YOLOv7模型结构和各类注意力机制原理）以及部分结果与分析（模型参数与计算量表格）。然而，片段未能覆盖详细的实验结果章节，包括模型的精度、召回率、平均精度变化曲线、检测效果的可视化对比图等关键证据。因此，无法评估该方法在实际裂缝识别效果上的最终性能。此外，讨论（Discussion）和结论（Conclusions）章节也缺失，限制了对其研究不足和未来展望的理解。
