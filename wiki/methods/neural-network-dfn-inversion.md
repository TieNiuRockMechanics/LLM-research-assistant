---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "基于神经网络的 DFN 参数反演"
aliases:
  - "BP neural network"
  - "CC neural network"
  - "GA-BP neural network"
  - "智能反演"
sources:
  - "2025-zhang-intelligent-construction-method-for-rock-slope-fracture-network-model-based-on-discre"
  - "2025-song-a-back-propagation-neural-network-optimized-by-genetic-algorithm-for-rock-joint-roughn"
---

# 基于神经网络的 DFN 参数反演

## Purpose

使用人工神经网络（BP, CC, GA-BP 等）从二维裂缝图像统计参数（如 PCAS 提取的 23 个特征）反演出三维 DFN 模型的关键参数（Fisher 方向 k, 长度幂律指数 α 等）。
## Aliases

- BP neural network
- CC neural network
- GA-BP neural network
- 智能反演
## Workflow

准备大量合成 DFN 图像与对应已知参数的训练数据；构建神经网络（如 3 层 BP、级联相关 CC），使用网格搜索或遗传算法优化超参数和初始权重；输入从图像提取的特征向量，输出 DFN 参数；可在不同岩性单元分别训练以考虑空间非均质性（分层建模策略）。
## Inputs

- 裂缝图像特征参数（如 PCAS 输出）
- 对应的 DFN 参数标签
## Outputs

- Fisher k
- 长度幂律指数 α
- lmin, lmax
- 模型域高度等
## Assumptions

- 训练数据分布覆盖目标分布
- 输入特征与输出参数存在一一映射
## Strengths

- 泛化能力强，预测误差可 <30%
- 可自动化处理大量图像
## Limitations

- 训练需大量合成数据
- 可能过拟合小样本
- 二维特征到三维参数映射非唯一
## Related Concepts

- pcas-image-processing
- stratified-modeling-strategy
- grid-search-hyperparameter
## Source Papers

- [2025-zhang-intelligent-construction-method-for-rock-slope-fracture-network-model-based-on-discre](../papers/2025-zhang-intelligent-construction-method-for-rock-slope-fracture-network-model-based-on-discre.md)
- [2025-song-a-back-propagation-neural-network-optimized-by-genetic-algorithm-for-rock-joint-roughn](../papers/2025-song-a-back-propagation-neural-network-optimized-by-genetic-algorithm-for-rock-joint-roughn.md)
