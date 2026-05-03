---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-li-rock-crack-recognition-technology-based-on-deep-learning"
title: "Rock Crack Recognition Technology Based on Deep Learning."
status: "draft"
source_pdf: "data/papers/2023 - Rock Crack Recognition Technology Based on Deep Learning.pdf"
collections:
  - "part1"
citation: "Li, Jinbei, et al. \"Rock Crack Recognition Technology Based on Deep Learning.\" *Sensors*, vol. 23, no. 12, 2023, article 5421, doi:10.3390/s23125421."
indexed_texts: "12"
indexed_chars: "59537"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "59530"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.999882"
coverage_status: "full-index"
source_signature: "5e425fece1765d4cc077e136330e2d3565b3602d"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T07:04:47"
---

# Rock Crack Recognition Technology Based on Deep Learning.

## One-line Summary
该研究提出基于深度学习的岩石裂隙识别技术，使用YOLOv7模型结合SimAM注意力机制，在无人机图像上实现高精度检测（精确率100%，AP 96.89%，每100张图片处理时间10秒），为地质灾害早期识别提供新方向。 [Li 2023, pp. 1-2, 10-12]

## Research Question
如何利用深度学习技术快速、精确地获取岩石表面裂缝信息，以提高地质灾害（滑坡、崩塌、泥石流）早期预警的效率？具体包括：YOLOv7模型如何改进以提升裂缝检测性能？哪种注意力机制与YOLOv7结合后能实现速度与精度的最佳平衡？ [Li 2023, pp. 1-3]

## Study Area / Data
研究区域为粤港澳大湾区（111°59′E~115°28′E, 21°56′N~24°51′N），地形以台地、丘陵、平原为主，年均温22℃，年降雨量2300mm，属地质灾害多发区。 [Li 2023, pp. 3-4]

数据源为无人机（UAV）实地拍摄的岩石表面裂缝图像。从大量图像中选取200张不同形态和复杂背景的图片，通过灰度处理、角度变化等数据增强方法扩展至714张，统一裁剪为640×640像素。使用Labelimg标注生成VOC格式数据集，按2:8比例划分测试集与训练集。 [Li 2023, pp. 3-4]

## Methods
以YOLOv7为基线模型，在主干网络（backbone）与颈部网络（neck）之间插入注意力机制，构建改进目标检测器。比较五种注意力机制：CBAM、SE、ECA、CA、SimAM，并以YOLOv5为基准对照。YOLOv7网络包含输入模块（Mosaic、Mixup增强）、主干模块（ELAN、MP结构）和颈部模块（SPPCPC、REP参数化），实现速度与精度平衡。SimAM是基于神经科学理论的无参数3D注意力机制，通过能量函数度量神经元重要性，不增加模型参数；其他注意力机制则引入额外参数。训练50个epoch，采用精确率（Precision）、召回率（Recall）、平均精度（AP）、F1分数和处理100张图片的时间（Time100）评估性能。 [Li 2023, pp. 2-3, 4-8, 8-9, 10]

## Key Findings
1. SimAM注意力机制插入YOLOv7后，模型参数量与计算量未增加，性能提升最显著：精确率100%、召回率75%、AP 96.89%，较基线YOLOv7（98.33%, 73.75%, 95.44%）分别提高1.67%、1.25%和1.45%，且处理速度不变（10 s/100张）。 [Li 2023, pp. 10-12]
2. CBAM与SE机制虽精确率亦达100%，但召回率或速度下降严重（CBAM Time100=34 s，SE召回率68.75%）；ECA与CA机制则导致精确率降低（<97%）。 [Li 2023, pp. 10-12]
3. 训练损失曲线显示，SimAM收敛较快，最终验证损失最低（0.0163），训练稳定性优于其他变体。 [Li 2023, pp. 9-10]
4. YOLOv5基准精确率95.7%、召回率55.16%、AP 88%、Time100为12 s，全面落后于YOLOv7系列模型。 [Li 2023, pp. 10-12]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| SimAM+YOLOv7 精确率100%，召回率75%，AP 96.89%，Time100=10s | [Li 2023, pp. 10-12] | 训练50 epoch，VOC裂缝数据集（714张640×640图像），测试集评估 | 无参数增加，综合性能最优 |
| 基线YOLOv7 精确率98.33%，召回率73.75%，AP 95.44%，Time100=10s | [Li 2023, pp. 10-12] | 相同数据集与训练设置 | 作为改进对照 |
| CBAM+YOLOv7 精确率100%，召回率73.75%，AP 95.68%，Time100=34s | [Li 2023, pp. 10-12] | 相同条件 | 参数增加，速度显著下降 |
| SE+YOLOv7 精确率100%，召回率68.75%，AP 96.21%，Time100=31s | [Li 2023, pp. 10-12] | 相同条件 | 召回率下降明显 |
| ECA+YOLOv7 精确率96.83%，召回率76.25%，AP 94.60%，Time100=16s | [Li 2023, pp. 10-12] | 相同条件 | 精确率下降 |
| CA+YOLOv7 精确率96.61%，召回率71.25%，AP 95.68%，Time100=11s | [Li 2023, pp. 10-12] | 相同条件 | 精确率下降 |
| YOLOv5基准 精确率95.7%，召回率55.16%，AP 88%，Time100=12s | [Li 2023, pp. 10-12] | 相同数据集 | 性能最差 |
| SimAM未增加参数量（37.620M params, 106.472G FLOPs），其他机制均有增加 | [Li 2023, pp. 8-9, Table 1] | 模型输入尺寸640 | 无参数注意力机制优势 |

## Limitations
- 仅使用粤港澳大湾区无人机影像数据集，模型泛化性未在其他地质环境验证。 [Li 2023, pp. 12-13]
- 注意力机制固定插入在主干网络与颈部网络之间，未探索其他位置或组合效果。 [Li 2023, pp. 12-13]
- 裂缝识别限于目标检测框，未能实现裂缝宽度、长度、面积等几何参数的精细量化。 [Li 2023, pp. 13]
- 未讨论复杂光照、遮挡等野外条件对检测性能的影响（文中未直接提及，但结论中指出需进一步研究）。 [Li 2023, pp. 12-13]

## Assumptions / Conditions
- 模型训练与测试基于VOC格式标注数据，输入图像尺寸固定为640×640。 [Li 2023, pp. 3-4]
- 所有模型在相同超参数下训练50个epoch，训练集与测试集按8:2划分。 [Li 2023, pp. 9-10]
- 性能指标计算采用目标检测标准定义（TP、FP、FN、TN）。 [Li 2023, pp. 8-9]
- 注意力机制插入方式均为在主干网络输出的三个特征层后接注意力模块。 [Li 2023, pp. 8]

## Key Variables / Parameters
- 检测性能：精确率（Precision）、召回率（Recall）、平均精度（AP）、F1分数、Time100（s）
- 模型复杂度：参数量（Param.）、计算量（FLOPs）
- 注意力机制类型：CBAM、SE、ECA、CA、SimAM
- 训练指标：总损失（Total Loss）、验证损失（Val Loss）
- 数据集规模：714张，训练集80%，测试集20%

## Reusable Claims
- YOLOv7在岩石裂缝检测任务中优于YOLOv5，精度和速度均更高。 [Li 2023, pp. 10-12]
- 在YOLOv7 backbone与neck之间插入SimAM注意力机制，可以在不增加任何参数的前提下，将AP从95.44%提升至96.89%，精确率提升至100%，召回率提升至75%，且推理速度不变。 [Li 2023, pp. 10-12, 12-13]
- CBAM和SE注意力机制虽能提升精确率，但会大幅增加参数量和推理时间（Time100增至34s和31s），不适合实时检测场景。 [Li 2023, pp. 10-12]
- 无参数注意力机制（如SimAM）适合资源受限的边缘端部署，能保持高精度同时不增加计算负担。 [Li 2023, pp. 8-9, 12-13]

## Candidate Concepts
- [[岩石裂隙识别]]
- [[YOLOv7]]
- [[SimAM注意力机制]]
- [[目标检测]]
- [[地质灾害早期识别]]
- [[无人机图像处理]]
- [[深度学习]]
- [[粤港澳大湾区]]

## Candidate Methods
- [[YOLOv7改进模型]]
- [[注意力机制集成]]
- [[数据增强（角度变换、灰度化）]]
- [[VOC数据集标注]]
- [[模型性能评估（Precision, Recall, AP, Time100）]]

## Connections To Other Work
- 首次将YOLOv7与注意力机制结合用于岩石裂缝检测，填补了该领域空白。 [Li 2023, pp. 2-3]
- 与Huang Xiaohong等人基于改进Faster-RCNN的岩石裂缝追踪方法相比，YOLOv7系列在速度与精度平衡上更具优势。 [Li 2023, pp. 2-3]
- 在注意力机制应用上，CBAM、SE在其他任务（如绝缘子缺陷检测、柿子识别）中的改进幅度与本研究相近，而SimAM的无参数特性使其在工程部署中更具潜力。 [Li 2023, pp. 12-13]
- 与YOLOv5的直接对比证实，YOLOv7作为新一代检测器在裂缝场景表现更佳。 [Li 2023, pp. 10-12]

## Open Questions
- 注意力机制的最佳插入位置及不同机制的组合是否还能进一步提升性能？ [Li 2023, pp. 12-13]
- 模型在多种岩性、气候和光照条件下的泛化能力如何？ [Li 2023, pp. 12-13]
- 如何结合图像分割技术实现裂缝几何参数（宽度、长度、面积）的自动提取，以支持灾害定量风险评估？ [Li 2023, pp. 13]
- 能否采用更先进的检测架构（如Transformer）进一步突破现有性能上限？ [未在本研究范围，但为自然延伸]

## Source Coverage
所有非空索引片段均已处理。共12个文本块，59,537字符，实际使用59,530字符，覆盖率按块计100%，按字符计99.99%。 [参考coverage audit数据]
