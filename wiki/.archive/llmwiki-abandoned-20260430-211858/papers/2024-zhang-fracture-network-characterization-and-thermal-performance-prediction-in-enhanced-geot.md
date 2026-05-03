---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2024-zhang-fracture-network-characterization-and-thermal-performance-prediction-in-enhanced-geot"
title: "Fracture Network Characterization and Thermal Performance Prediction in Enhanced Geothermal Reservoirs Using Covariance Matrix Adaptation and Embedded Discrete Fracture Model."
status: "draft"
source_pdf: "data/papers/2025 - Fracture Network Characterization and Thermal Performance Prediction in Enhanced Geothermal Reservoirs Using Covariance Matrix Adaptation and Embedded Discrete.pdf"
collections:
citation: "Zhang, Kun, and Hui Wu. \"Fracture Network Characterization and Thermal Performance Prediction in Enhanced Geothermal Reservoirs Using Covariance Matrix Adaptation and Embedded Discrete Fracture Model.\" *Water Resources Research*, 2024, doi:10.1029/2024WR039452. Accessed 2026."
indexed_texts: "20"
indexed_chars: "98108"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T15:17:11"
---

# Fracture Network Characterization and Thermal Performance Prediction in Enhanced Geothermal Reservoirs Using Covariance Matrix Adaptation and Embedded Discrete Fracture Model.

## One-line Summary

本研究提出一种集成反演框架，将基于背景断裂网络与非均匀孔径的参数化方法、协方差矩阵自适应进化策略（CMA-ES）以及嵌入式离散断裂模型（EDFM）相结合，用于增强型地热系统（EGS）中的人工断裂网络表征与长期热性能预测 [Zhang 2024, pp. 1-1]。

## Research Question

如何有效表征增强型地热系统（EGS）中高度不确定的人工断裂网络，并基于此表征准确预测储层的长期热性能？ [Zhang 2024, pp. 1-1, 3-4]

## Study Area / Data

本研究采用三个具有不同复杂度的合成数值案例（3个合成EGS案例），以验证所提反演框架的有效性。案例涵盖二维和三维情况，储层参数（如温度、压力、注入速率等）分别进行了设定。所有案例中，岩石基质均为低渗透性，储层饱和水。三维案例还考虑了垂向地温梯度（50°C/km）和静水压力平衡假设 [Zhang 2024, pp. 8-9]。

## Methods

### 断裂网络参数化方法
提出一种新的参数化策略：使用一个拥有固定几何形状和密集断裂分布的**背景断裂网络模型**作为反演模型，以逼近真实的断裂网络。每个背景断裂采用精心设计的**非均匀孔径分布**，由中心位置（x_c）、有效断裂长度（x_l）和断裂孔径（x_a）三个参数定义，将断裂划分为有效段和无效段，从而可生成多种有效断裂网络几何形态 [Zhang 2024, pp. 1-1, 3-4]。

### 反演算法
采用**协方差矩阵自适应进化策略（CMA-ES）**作为随机反演方法，通过匹配保守性和吸附性示踪剂测量数据进行断裂参数反演。多次并行运行CMA-ES以获得一组模型实现，从而进行**不确定性评估**。反演的适应度函数定义为观测示踪剂/井压力数据与模拟数据之间的不匹配度 [Zhang 2024, pp. 1-1, 4-6]。

### 正演模拟
采用**嵌入式离散断裂模型（EDFM）**进行裂隙储层中流动和传输的正演模拟。EDFM允许断裂网格独立于基质网格，在反演过程中仅需更新断裂网格，无需重划整个系统网格。流体遵循达西定律，断裂渗透率基于立方定律由孔径值确定。示踪剂传输仅考虑在断裂内进行。所有正演模型在开源多物理场耦合平台“GEOS”上实现 [Zhang 2024, pp. 2-3, 6-8]。

## Key Findings

- 所提出的集成反演框架能在三个不同复杂度的合成EGS案例中，有效捕捉断裂网络中的主要流动和传输特征 [Zhang 2024, pp. 1-1]。
- 推断出的断裂网络模型能够适当地预测EGS储层的长期热性能 [Zhang 2024, pp. 1-1]。
- CMA-ES算法被成功用于从高维、高度不确定的参数空间（涉及断裂数量、位置、尺寸、方向和孔径）中推断模型参数 [Zhang 2024, pp. 1-2]。
- 该集成框架为EGS的断裂网络表征和热性能预测提供了一种可行的解决方案，并在非常规油气藏勘探中具有潜在应用 [Zhang 2024, pp. 1-1]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 集成框架能在三个合成案例中捕捉主要流和传输特征 | [Zhang 2024, pp. 1-1] | 三个合成EGS案例，使用保守性和吸附性示踪剂数据 | 结果来自合成实验，非现场数据 |
| 推断出的断裂网络模型可预测ESG储层的长期热性能 | [Zhang 2024, pp. 1-1] | 基于反演得到的断裂网络模型进行热性能预测 | 长期热性能预测的准确度由推断模型支持 |
| EDFM允许断裂网格独立于基质网格，便于反演中更新网格 | [Zhang 2024, pp. 2-3] | 使用EDFM作为正演模拟器 | 这是EDFM相对传统DFM的关键优势 |

## Limitations

- 本研究仅在**合成数值案例**上验证了方法的有效性，未从索引片段中确认是否使用真实现场数据 [Zhang 2024, pp. 1-1, 8-9]。
- 示踪剂反演阶段**忽略了温度和压力引起的水密度变化**，将其近似为空间均匀和时间恒定。这可能影响在真实地热梯度情景下的反演精度 [Zhang 2024, pp. 8-9]。
- 背景断裂网络模型假设断裂几何形状和方向固定（仅考虑两个主方向），这可能限制了其表征具有复杂、多方向断裂网络的储层的能力 [Zhang 2024, pp. 3-4]。

## Assumptions / Conditions

- 使用**合成案例**进行验证，非真实现场数据 [Zhang 2024, pp. 8-9]。
- 真实断裂网络可被一个密集的、具有固定几何形状的**背景断裂网络**模型通过部分激活（调整非均匀孔径）来充分或大部分再现 [Zhang 2024, pp. 3-4]。
- 示踪剂反演阶段，储层温度场在短期示踪测试（几天至几周）内基本不变，水密度可近似为空间均匀且不随时间变化 [Zhang 2024, pp. 8-9]。
- 三维案例中假设**垂向地温梯度为50°C/km**，初始压力场为**静水压力平衡** [Zhang 2024, pp. 8-9]。
- 断裂渗透率由**立方定律**基于孔径值确定，假设光滑平行板几何 [Zhang 2024, pp. 6-7]。
- 基质为低渗透性，示踪剂传输**仅在断裂中**被考虑 [Zhang 2024, pp. 6-8]。

## Key Variables / Parameters

- **断裂参数化变量**：中心位置 (x_c)，有效断裂长度 (x_l)，断裂孔径 (x_a) [Zhang 2024, pp. 3-4]。
- **反演适应度函数** (O(x))：由观测数据 (y_obs) 与模型预测 (y(x)) 的不匹配度及测量误差的自动方差矩阵 (C_D) 定义 [Zhang 2024, pp. 4-6]。
- **CMA-ES 更新参数**：通过加权重组更新均值矩阵 (m^(g+1))，并自适应更新捕获参数方差的协方差矩阵 (C^(g+1)) [Zhang 2024, pp. 4-6]。
- **储层关键参数**：注入速率（0.75, 1.0, 10.0 kg/s）、基质渗透率（设为低渗透）、初始温度与压力（2D案例为200°C, 34 MPa；3D案例不同） [Zhang 2024, pp. 8-9]。
- **终止准则**：基于连续迭代间的均方根误差（RMSE）低于预设阈值 (ˆδ) 来终止单次CMA-ES运行 [Zhang 2024, pp. 6-7]。

## Reusable Claims

1.  EDFM的非一致性网格特性，使其在断裂几何变化时仅需更新断裂网格而不需重划整个计算域网格，因此特别适合集成到自动断裂网络反演方法中 [Zhang 2024, pp. 2-3]。
    - **条件**：断裂几何形状不固定，正演模拟器需处理多种断裂分布。
    - **限制**：与一致性网格的传统DFM相比，EDFM在极高局部各向异性或非常稀疏的大断裂情况下的适用性，未在片段中确认。
2.  通过多次并行运行CMA-ES（每次使用不同起点）来获得一组低不匹配度的模型实现，是实现断裂网络反演不确定性评估的一种有效方法 [Zhang 2024, pp. 1-1, 1-2]。
    - **条件**：CMA-ES被用作随机反演方法。
    - **限制**：此方法依赖于单次运行能收敛到一个有效的局部最优解，片段未提及计算成本或并行运行的次数。
3.  对于深部低渗透基质EGS储层，短期示踪剂测试（几天至几周）期间的温度场可视为几乎不变，因此可忽略由温度和压力变化引起的水密度变化，这对简化示踪反演流体物性参数是可接受的条件 [Zhang 2024, pp. 8-9]。
    - **条件**：测试时间短，基质渗透性低。
    - **证据**：基于合成案例的模型假设和稳态流场前处理。

## Candidate Concepts

[[enhanced geothermal system (EGS)]], [[embedded discrete fracture model (EDFM)]], [[covariance matrix adaptation evolution strategy (CMA-ES)]], [[fracture network characterization]], [[tracer test]], [[fracture reservoir]], [[uncertainty quantification]], [[non-uniform fracture aperture]], [[background fracture network]], [[geothermal reservoir thermal performance]], [[cubic law]]

## Candidate Methods

[[embedded discrete fracture model (EDFM)]], [[covariance matrix adaptation evolution strategy (CMA-ES)]], [[tracer-based fracture inversion]], [[non-conforming discrete fracture model]], [[normal-score transformation]], [[steady-state flow simulation]], [[forward flow and transport simulation (GEOS)]], [[multiple parallel inversion runs]]

## Connections To Other Work

- 本研究将 **EDFM** 的应用从油气藏（如 Jiang et al., 2022; Leines-Artieda et al., 2022 等所报道）拓展至 **EGS 储层**的断裂网络表征中 [Zhang 2024, pp. 2-3]。
- 在反演方法上，与采用 **MCMC 或数据同化**方法进行断裂反演的工作相关，这些方法能产生模型集合并进行不确定性评估，而本研究采用的是**进化算法**中的 CMA-ES [Zhang 2024, pp. 1-2]。
- 其断裂参数化策略区别于许多前人研究中使用**均匀孔径**的假设，而是采用了更精细的**非均匀孔径分布** [Zhang 2024, pp. 3-4]。
- 主题上可与 [[Bayesian inversion for geothermal]]、[[discrete fracture network (DFN) modeling]]、[[fracture network upscaling]] 等概念和方法关联。

## Open Questions

- 该框架在包含**真实现场数据**（如岩心、测井、现场示踪测试数据）的案例中的表现如何？ [Zhang 2024, pp. 1-1]
- 背景断裂网络的**最佳密度和设计原则**是什么，以确保在不显著增加计算成本的前提下，能充分表征未知的真实断裂网络？未从索引片段中确认。
- 除了基于出口浓度/压力的不匹配度，是否可以集成其它类型的地球物理观测数据（如微震、电磁数据）作为反演约束？未从索引片段中确认。
- 对于非矩形的任意储层边界和不规则井网配置，该框架的适用性和调整方法是什么？未从索引片段中确认。

## Source Coverage

本知识页基于论文的20个索引片段构建。这些片段覆盖了摘要、引言/文献综述、方法学（参数化、CMA-ES、EDFM、工作流）以及数值实验设置等部分。**方法学部分覆盖得最为详细**，详细展示了其核心创新点和工作流程。**研究结果和分析部分可能缺失关键细节**，例如三个案例的具体反演精度量化指标（RMSE值等）、不确定性分析的具体结果、长期热性能预测的对比图表等。因此，对框架有效性的定量证据和对局限性的深入讨论可能不完整。
