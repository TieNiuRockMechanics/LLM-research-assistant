---
type: "paper"
paper_id: "2024-zhang-fracture-network-characterization-and-thermal-performance-prediction-in-enhanced-geot"
title: "Fracture Network Characterization and Thermal Performance Prediction in Enhanced Geothermal Reservoirs Using Covariance Matrix Adaptation and Embedded Discrete Fracture Model."
status: "draft"
source_pdf: "data/papers/2025 - Fracture Network Characterization and Thermal Performance Prediction in Enhanced Geothermal Reservoirs Using Covariance Matrix Adaptation and Embedded Discrete.pdf"
citation: "Zhang, Kun, and Hui Wu. \"Fracture Network Characterization and Thermal Performance Prediction in Enhanced Geothermal Reservoirs Using Covariance Matrix Adaptation and Embedded Discrete Fracture Model.\" *Water Resources Research*, 2024. doi:10.1029/2024WR039452. Accessed 2026."
indexed_texts: "20"
indexed_chars: "98108"
compiled_at: "2026-04-27T19:48:29"
---

# Fracture Network Characterization and Thermal Performance Prediction in Enhanced Geothermal Reservoirs Using Covariance Matrix Adaptation and Embedded Discrete Fracture Model.

## One-line Summary

该研究提出了一种集成逆推框架，结合新型[[裂缝网络参数化]]方法、[[协方差矩阵自适应进化策略]]（CMA-ES）和[[嵌入式离散裂缝模型]]（EDFM），用于表征EGS中的裂缝网络并预测长期热性能，并通过三个合成案例验证了其有效性 [Zhang 2024, pp. 1-1]。

## Research Question

如何解决[[增强型地热系统]]（EGS）中裂缝网络表征的难题（包括高维度和高度非线性的参数空间），并利用推断出的模型准确预测储层的长期热性能 [Zhang 2024, pp. 1-1, 1-2]？

## Study Area / Data

本研究使用三个复杂度不同的**合成EGS案例研究**来验证框架的有效性 [Zhang 2024, pp. 1-1]。数值实验基于合成的参照裂缝网络 [Zhang 2024, pp. 8-8]。逆推过程利用示踪剂（包括保守型和吸附型示踪剂）测量数据作为观测数据 [Zhang 2024, pp. 1-1, 4-4]。

## Methods

1.  **裂缝网络参数化方法**：提出了一种新颖的参数化策略。该方法假设一个具有**固定几何形状**的背景裂缝网络模型，并为每条裂缝设计**非均匀的裂缝开度分布**，用三个参数（中心位置 xc、有效长度 xl、开度 xa）定义，从而可以生成多种有效的裂缝网络几何形状 [Zhang 2024, pp. 3-4]。
2.  **参数反演算法**：采用[[协方差矩阵自适应进化策略]]（CMA-ES）作为随机逆推方法来推断裂缝参数 [Zhang 2024, pp. 1-1, 2-3]。通过匹配示踪剂测量数据和正向模拟数据来定义适应度函数 [Zhang 2024, pp. 4-6]。执行**多次独立的 CMA-ES 运行**以获取一组低误差的解决方案，用于不确定性评估 [Zhang 2024, pp. 1-1, 7-7]。
3.  **正向流与输运模拟**：采用[[嵌入式离散裂缝模型]]（EDFM）进行稳健的正向模拟 [Zhang 2024, pp. 1-1]。EDFM 允许裂缝网格独立于基质网格，便于在裂缝几何形状变化时更新裂缝网格而无需对整个系统重新划分网格，这使其在裂缝逆推中具有优势 [Zhang 2024, pp. 2-3]。该正向模型在开源多物理场耦合平台“GEOS”中实现 [Zhang 2024, pp. 7-7]。
4.  **整体工作流程**：集成框架包括在每次CMA-ES迭代中根据更新后的参数构建裂缝网络、将其嵌入基质网格、运行EDFM示踪剂模型获取突破数据、与测量数据比较并计算适应度值，然后由CMA-ES更新参数，如此迭代直至获得可行解。得到的多个低误差解用于后续长期热性能预测 [Zhang 2024, pp. 7-8]。

## Key Findings

- 该逆推框架能够有效捕捉裂缝网络中的主要流动和运移特征 [Zhang 2024, pp. 1-1]。
- 通过推断出的裂缝网络模型，能够很好地预测EGS储层的**长期热性能** [Zhang 2024, pp. 1-1, 1-2]。
- CMA-ES 已被用于通过匹配保守型和吸附型示踪剂测量值来推断裂缝参数 [Zhang 2024, pp. 1-1]。
- 该综合框架为EGS中的裂缝网络表征和热性能预测提供了可行的解决方案，并有可能应用于非常规天然气/油藏勘探 [Zhang 2024, pp. 1-1]。
- 所提出的参数化方法的关键创新在于使用具有精心设计的非均匀开度分布的较密集裂缝网络 [Zhang 2024, pp. 3-4]。
- 通过多条独立CMA-ES运行获得的解决方案集合，可用于进行不确定性评估 [Zhang 2024, pp. 7-7]。
- 数值实验展示了该框架在不同复杂度等级（Case 1, 2, 3）下的表现 [Zhang 2024, pp. 8-8]。
- 在进行示踪剂逆推阶段，由于示踪剂测试时间较短（几天到几周），地下温度场几乎不变，因此忽略了水和密度的温度/压力变化 [Zhang 2024, pp. 8-9]。

## Limitations

- 该研究是基于**合成案例**进行的，其在实际现场条件下的应用效果未从索引片段中确认。
- 对于更复杂的地质情况（例如具有更复杂的裂缝拓扑结构或非达西流）的泛化能力，片段未提供明确信息。
- 该框架的计算成本是一个实际限制因素，文中提及计算网格的细化是在“保持足够精度”和“计算需求”之间做出的实际折衷 [Zhang 2024, pp. 8-9]。
- CMA-ES 运行通过连续迭代之间 RMSE 低于预设阈值来终止，但该方法的局限性未从索引片段中得到确认 [Zhang 2024, pp. 6-7]。
- 文中提到逆推后得到的解 S_c 被用于后续预测和不确定性分析，但解的全局最优性未从索引片段中确认 [Zhang 2024, pp. 6-7]。
- 论文提到的10页之后的内容未从索引片段中提供。

## Reusable Claims

- EDFM 允许裂缝网格独立于基质网格，在裂缝几何形状变化时只需更新裂缝网格，无需对整个系统重新划分网格，这使其在裂缝逆推中具有显著优势 [Zhang 2024, pp. 2-3]。
- 裂缝网络表征问题本质上具有高维度性和高度非线性，亟需有效的反演方法 [Zhang 2024, pp. 1-2]。
- 通过匹配保守型和吸附型示踪剂测量值，可以借助CMA-ES算法推断裂缝参数 [Zhang 2024, pp. 1-1]。
- 对具有固定几何形状和精心设计的非均匀开度分布的背景裂缝网络进行参数化，可以更好地逼近真实裂缝网络 [Zhang 2024, pp. 3-4]。
- 即使在裂缝逆推阶段忽略了温度效应，由此推断出的模型仍能用于准确预测长期热性能 [Zhang 2024, pp. 1-1, 8-9]。

## Candidate Concepts

- [[增强型地热系统 (EGS)]]
- [[裂缝网络表征]]
- [[热性能预测]]
- [[裂缝参数化]]
- [[非均匀裂缝开度]]
- [[背景裂缝网络]]
- [[保守型示踪剂]]
- [[吸附型示踪剂]]
- [[不确定性评估]]
- [[热储工程]]

## Candidate Methods

- [[协方差矩阵自适应进化策略 (CMA-ES)]]
- [[嵌入式离散裂缝模型 (EDFM)]]
- [[裂缝网络参数化方法]]（固定几何 + 非均匀开度）
- [[GEOS 多物理场耦合平台]]

## Open Questions

- 该框架在真实现场数据（而非合成数据）上的表现如何？其鲁棒性和准确性能否得到验证？
- 将该框架扩展到三维、更复杂的裂缝网络（例如考虑多个裂缝组、裂缝弯曲或交叉）时，计算复杂度和性能会受到多大影响？
- CMA-ES 的结果对算法参数（如初始协方差矩阵、种群大小）的敏感性如何？
- 如何在逆推过程中更有效地整合除示踪剂之外的其他现场数据（如微震监测、温度数据）？
- 该框架能否从 EGS 成功迁移至非常规油气藏勘探？[Zhang 2024, pp. 1-1]

## Source Coverage

本页面完全基于论文的第3页至第9页的索引片段构建。论文标题、作者、摘要以及引言和方法的详细内容均源自提供的片段。论文第10页及后续（包括第3个案例的详细结果和结论）的内容未从索引片段中提供。
