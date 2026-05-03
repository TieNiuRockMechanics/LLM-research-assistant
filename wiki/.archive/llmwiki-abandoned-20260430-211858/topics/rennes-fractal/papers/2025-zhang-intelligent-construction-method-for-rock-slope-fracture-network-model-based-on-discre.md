---
type: "paper"
paper_id: "2025-zhang-intelligent-construction-method-for-rock-slope-fracture-network-model-based-on-discre"
title: "Intelligent Construction Method for Rock Slope Fracture Network Model Based on Discrete Element and Neural Network."
status: "draft"
source_pdf: "data/papers/2025 - Intelligent construction method for rock slope fracture network model based on discrete element and neural network.pdf"
citation: "Zhang, Zhe, et al. \"Intelligent Construction Method for Rock Slope Fracture Network Model Based on Discrete Element and Neural Network.\" *Scientific Reports*, vol. 15, 2025, article 41577, doi:10.1038/s41598-025-25409-2."
indexed_texts: "14"
indexed_chars: "69979"
compiled_at: "2026-04-27T19:49:32"
---

# Intelligent Construction Method for Rock Slope Fracture Network Model Based on Discrete Element and Neural Network.

## One-line Summary
本研究提出一种结合现场勘探平硐数据、离散元数值模拟（3DEC）与BP/CC神经网络的智能离散裂隙网络（DFN）构建方法，并在大渡河成都岸岩质边坡案例中实现高精度裂隙网络反演。

## Research Question
如何利用有限二维勘探平硐数据，通过智能算法实现高陡岩质边坡内部复杂裂隙网络的高精度三维表征与参数反演？[Zhang 2025, pp. 1-2]

## Study Area / Data
- **研究区域**：大渡河成都岸特大桥（位于四川省甘孜藏族自治州泸定县北侧）岩质边坡 [Zhang 2025, pp. 6-8]。
- **数据来源**：通过钻爆法开挖的勘探平硐（高程1724 m，断面2 m × 2 m，长度100 m）获取现场裂隙分布特征 [Zhang 2025, pp. 6-8]。
- **岩性单元**：闪长岩、碎裂岩、花岗岩三种岩性单元，采用分层建模策略 [Zhang 2025, pp. 2-3]。
- **数值模拟样本库**：基于Monte Carlo原理和3DEC软件，按625组参数组合（每组参数含k、α、lmin、lmax、Hbottom、Htop，每个参数5个水平）生成DFN模型，提取平硐全裂隙与贯穿裂隙统计图谱 [Zhang 2025, pp. 8-10]。

## Methods
1. **DFN生成框架**：采用Monte Carlo随机原理建立三维DFN生成模型框架，基于Davy [28] 提出的公式描述裂隙长度分布 n(l)=αl⁻α；裂隙中心位置采用齐次泊松过程生成 [Zhang 2025, pp. 3-6]。
2. **数值模拟实验**：使用3DEC软件进行多组数值模拟（每组625次），提取二维裂隙迹线照片（全裂隙与贯穿裂隙），并通过PCAS程序进行图像特征提取与优化 [Zhang 2025, pp. 8-10]。
3. **数据样本构建**：定义23个输入参数（包括裂隙产状、尺寸、质心坐标的统计量：均值、标准差、集中区间上限、浓度内数量、正态拟合R²、分形维数及拟合优度等），输出参数为6个待校准DFN参数（k、α、lmin、lmax、Hbottom、Htop）[Zhang 2025, pp. 10-12]。
4. **神经网络建模**：
   - 采用反向传播（BP）神经网络（三层单隐层或四层双隐层结构，隐层神经元数6~29）和级联相关（CC）神经网络（动态生长，最大20隐层神经元）。
   - 激活函数为双曲正切（tanh），损失函数为均方误差（MSE）。
   - 数据归一化至[-1,1]，按60%训练、20%验证、20%测试分割；通过推广预测算法和网格搜索优化学习率等超参数 [Zhang 2025, pp. 12-15]。
5. **分层建模策略**：对不同岩性单元（闪长岩、碎裂岩、花岗岩）分别构建差异化神经网络模型 [Zhang 2025, pp. 2-3]。

## Key Findings
- 勘探平硐裂隙图像最优格式为：分辨率600×9000像素、绿色迹线、透明度70% [Zhang 2025, pp. 1-2]。
- 分层建模策略下各岩性单元最优预测误差：
  - 闪长岩区：四层BP网络误差18.4%
  - 碎裂岩区：三层BP网络误差8.0%
  - 花岗岩区：CC网络误差10.3% [Zhang 2025, pp. 1-2]
- 六个DFN输出参数在测试集上的预测误差均低于30% [Zhang 2025, pp. 12-15]。
- 与传统方法相比，参数反演误差降低18.4%–55.6% [Zhang 2025, pp. 2-3]。
- 方法已成功应用于大渡河成都岸特大桥边坡工程 [Zhang 2025, pp. 1-2]。

## Limitations
- 片段中指出传统方法仍存在局限性：二维平硐数据与三维DFN参数之间的跨维度映射关系尚不明确，传统特征工程难以捕捉多尺度裂隙相关性 [Zhang 2025, pp. 2-3]。
- 现有模型缺乏分层策略来处理多期构造活动引起的空间异质性 [Zhang 2025, pp. 2-3]。
- 机器学习模型在小样本条件下泛化能力受限 [Zhang 2025, pp. 2-3]。
- （本文提出的方法虽改进了上述问题，但片段未明确讨论该方法自身的局限性，因此未从片段中确认更多限制条件。）

## Reusable Claims
- 勘探平硐裂隙图像以“600×9000像素、绿色迹线、70%透明度”为最优，可确保PCAS程序分析精度 [Zhang 2025, pp. 1-2]。
- 基于Davy模型，裂隙长度指数α的增大导致长裂隙比例系统性降低，DFN系统向短裂隙主导网络转变 [Zhang 2025, pp. 3-6]。
- 采用齐次泊松过程生成裂隙中心空间位置，虽为简化假设，但与3DEC内置算法兼容 [Zhang 2025, pp. 3-6]。
- BP神经网络（四层）在闪长岩区预测误差18.4%，三层BP在碎裂岩区8.0%，CC网络在花岗岩区10.3% [Zhang 2025, pp. 1-2]。
- 基于23个输入特征（包括全裂隙与贯穿裂隙的产状、尺寸、位置统计量）可有效反演6个DFN关键参数（k、α、lmin、lmax、Hbottom、Htop）[Zhang 2025, pp. 10-12]。

## Candidate Concepts
- [[离散裂隙网络 (DFN)]]
- [[Monte Carlo随机原理]]
- [[BP神经网络]]
- [[Cascade Correlation神经网络]]
- [[3DEC数值模拟]]
- [[PCAS图像特征提取]]
- [[齐次泊松过程]]
- [[分形维数]]
- [[Fisher分布]]
- [[裂隙产状]]
- [[裂隙迹长]]
- [[分层建模策略]]

## Candidate Methods
- [[勘探平硐图像优化法]]（600×9000像素、绿色迹线、70%透明度）
- [[Davy裂隙长度分布模型]] [28]
- [[数值模拟样本生成方案]]（5因素5水平全组合，共625组）
- [[BP网络结构优化]]（三层/四层，隐层神经元6~29）
- [[CC网络动态生长训练]]
- [[网格搜索与推广预测算法超参数优化]]
- [[全裂隙与贯穿裂隙双统计图谱法]]

## Open Questions
- 如何进一步提高小样本条件下机器学习模型的泛化能力？[Zhang 2025, pp. 2-3]
- 二维平硐数据到三维DFN参数之间的跨维度映射误差如何进一步降低？[Zhang 2025, pp. 2-3]
- 本文提出的分层建模策略是否适用于其他构造活动更复杂或岩性变化更频繁的边坡？未从索引片段中确认。
- 该方法对于非贯通裂隙（即片段中提到的“非穿透性裂隙”）的处理是否对最终预测精度有量化影响？未从索引片段中确认。
- 如何将本方法推广至其他地质背景（如隧道、矿山边坡）？未从索引片段中确认。

## Source Coverage
- [Zhang 2025, pp. 1-2]：研究动机、方法概述、最优图像格式、分层预测误差、工程应用。
- [Zhang 2025, pp. 2-3]：现有局限性（2D→3D映射、小样本、空间异质性），分层策略，误差降低幅度。
- [Zhang 2025, pp. 3-6]：DFN建模框架，Davy模型（公式6,7），长度指数α的影响，齐次泊松过程。
- [Zhang 2025, pp. 6-8]：研究区域（大渡河成都岸、泸定）、勘探平硐施工参数、现场裂隙特征。
- [Zhang 2025, pp. 8-10]：数值模拟设计方案（表4，625组参数），提取裂隙迹线照片，PCAS图像分析。
- [Zhang 2025, pp. 10-12]：23个输入参数定义（表7），输出参数（k,α,lmin,lmax,Hbottom,Htop）。
- [Zhang 2025, pp. 12-15]：神经网络结构（BP三层/四层、CC动态生长），超参数优化，数据分割（60/20/20），预测误差均<30%，稳定性验证。
