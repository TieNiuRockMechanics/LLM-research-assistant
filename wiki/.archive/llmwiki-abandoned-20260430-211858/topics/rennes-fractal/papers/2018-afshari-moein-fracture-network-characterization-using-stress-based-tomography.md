---
type: "paper"
paper_id: "2018-afshari-moein-fracture-network-characterization-using-stress-based-tomography"
title: "Fracture Network Characterization Using Stress-Based Tomography."
status: "draft"
source_pdf: "data/papers/2018 - Fracture Network Characterization Using Stress-Based Tomography.pdf"
citation: "Afshari Moein, Mohammad Javad, et al. “Fracture Network Characterization Using Stress-Based Tomography.” *Journal of Geophysical Research: Solid Earth*, vol. 123, no. 10, 2018, pp. 9324-. DOI:10.1029/2018JB016438. Accessed 15 Jun. 2026."
indexed_texts: "18"
indexed_chars: "86036"
compiled_at: "2026-04-27T19:38:30"
---

# Fracture Network Characterization Using Stress-Based Tomography.

## One-line Summary
本文提出了一种名为“应力断层扫描”（stress-based tomography）的新方法，在贝叶斯框架内利用钻孔尺度的应力异质性来校准离散裂缝网络（DFN），从而表征深部增强型地热系统（EGS）储层中的裂缝网络及其非均质性 [Afshari 2018, pp. 1-1]。

## Research Question
在EGS开发初期，有关裂缝网络结构的信息主要来自钻孔图像和露头数据，但用这些数据成像深部储层的非连续面十分困难。井壁破坏数据只能提供地应力状态的部分分量及其非均质性信息。本文的工作假设是天然裂缝的滑动主要控制这些应力非均质性 [Afshari 2018, pp. 1-1]。因此，核心研究问题为：如何利用钻孔尺度的应力变化来反演深部地热储层中的裂缝网络几何及其非均质性？ [Afshari 2018, pp. 1-2]

## Study Area / Data
该方法通过两个测试案例进行验证：(1) 一个由少量裂缝组成的简单合成DFN（域大小100×100 m²，含四个正交大裂缝，最小间距10 m，最小长度40 m，总长度250 m）; (2) 一个基于野外露头数据映射的更复杂、更现实的裂缝网络 [Afshari 2018, pp. 8-9]。作为方法论背景，文中还引用了法国Soultz-sous-Forêts EGS站点GPK4钻孔的成像测井数据，以及瑞士Basel EGS井的应力剖面（包括S_hmin、S_hmax、S_v及最大水平主应力方位）来展示应力测量与钻孔破坏特征 [Afshari 2018, pp. 3-4]。反演所需的观测数据为沿钻孔的至少一个主应力分量的大小和方向 [Afshari 2018, pp. 6-7]。

## Methods
文中提出了一种称为“应力断层扫描”的贝叶斯反演方法 [Afshari 2018, pp. 1-1]。具体步骤包括：

1. **正向模拟**：采用二维平面应变假设（垂直平面），使用位移不连续法（DDM）模拟裂缝域内的应力变化。裂缝力学行为由Barton-Bandis模型描述，峰值剪应力通过Mohr-Coulomb准则估算，超出峰值后剪切刚度设为零（滑动裂缝） [Afshari 2018, pp. 4-6]。应力波动从域中心的虚拟钻孔中提取 [Afshari 2018, pp. 4-6]。
2. **先验信息**：基于裂缝属性（长度、方位、密度）的统计知识生成初始随机DFN实现 [Afshari 2018, pp. 1-1],[Afshari 2018, pp. 7-8]。
3. **贝叶斯反演**：采用马尔可夫链蒙特卡洛（MCMC）方法，具体为随机游走Metropolis-Hastings算法 [Afshari 2018, pp. 8-9]。每次迭代通过平移域内的某一裂缝来更新DFN，比较模拟应力剖面与观测应力剖面，计算似然函数（假设正态分布，基于均方根误差），并按Metropolis-Hastings接受准则决定是否接受新实现 [Afshari 2018, pp. 7-9]。反演过程中裂缝数量保持固定 [Afshari 2018, pp. 6-7]。
4. **结果输出**：存储所有可接受的DFN实现形成集合，舍去前一半以消除初始模型偏差，最终用该集合生成概率图，显示裂缝可能的位置和长度 [Afshari 2018, pp. 1-1],[Afshari 2018, pp. 8-9]。

反演至少需要两个应力分量作为观测（一个大小和一个方向）；单个应力方向不足以重建简单DFN [Afshari 2018, pp. 6-7]。远场应力需另行约束，不确定度来源于测量尺度等因素 [Afshari 2018, pp. 4-6]。

## Key Findings
*   应力断层扫描方法成功重建了简单合成DFN和更复杂的基于露头的裂缝网络，生成了裂缝概率分布图 [Afshari 2018, pp. 1-1]。
*   钻孔尺度的应力异质性可用于校准DFN，且假设其主要由裂缝滑动引起 [Afshari 2018, pp. 1-1]。
*   MCMC方法能有效拟合模拟与观测的应力剖面，并通过Metropolis-Hastings准则获得稳定的后验集合 [Afshari 2018, pp. 8-9]。
*   两个测试案例均使用了来自两个正交裂缝集的DFN [Afshari 2018, pp. 8-9]。具体的重建精度指标（如识别成功率）未从索引片段中确认。

## Limitations
*   该方法基于二维平面应变假设，限制了应用场景 [Afshari 2018, pp. 3-4]。
*   反演过程中裂缝数量固定，无法改变，这可能无法反映真实的裂缝网络复杂性 [Afshari 2018, pp. 6-7]。
*   需要至少两个应力分量（一个大小和一个方向）作为观测，获取完整的应力张量沿钻孔极其困难 [Afshari 2018, pp. 6-7]。
*   仅通过合成案例和露头数据测试，尚未在真实深部EGS钻孔中验证 [Afshari 2018, pp. 1-1]。
*   远场应力的约束不直接，其不确定性会对结果产生影响 [Afshari 2018, pp. 4-6]。

## Reusable Claims
*   钻孔尺度的应力异质性主要由天然裂缝滑动控制，这一假设是应力断层扫描的理论基础 [Afshari 2018, pp. 1-1]。
*   应力断层扫描至少需要一个主应力分量的大小和一个方向的观测资料才能进行有效反演 [Afshari 2018, pp. 6-7]。
*   MCMC方法可用于校准DFN，通过比较模拟与观测应力剖面，结合Metropolis-Hastings准则接受/拒绝模型 [Afshari 2018, pp. 1-1],[Afshari 2018, pp. 8-9]。
*   对于简单和复杂的裂缝网络，基于应力的断层扫描能成功成像裂缝的可能位置和长度 [Afshari 2018, pp. 1-1]。
*   在MCMC反演期间，裂缝的数量保持固定不变 [Afshari 2018, pp. 6-7]。
*   单独的应力方向观测不足以约束一个简单的DFN（仅含少量裂缝） [Afshari 2018, pp. 6-7]。

## Candidate Concepts
[[stress-based tomography]], [[discrete fracture network (DFN)]], [[Bayesian inference]], [[Markov Chain Monte Carlo (MCMC)]], [[Metropolis-Hastings algorithm]], [[Enhanced Geothermal System (EGS)]], [[in situ stress characterization]], [[Barton-Bandis model]], [[displacement discontinuity method (DDM)]], [[heterogeneous stress field]], [[borehole breakouts]], [[drilling-induced tensile fractures]], [[prior information]]

## Candidate Methods
[[stress-based tomography]], [[Bayesian inversion for DFN]], [[MCMC with Metropolis-Hastings for DFN calibration]], [[2D plane strain DDM simulation]], [[probability map generation from MCMC ensemble]], [[normal likelihood function for stress misfit]]

## Open Questions
*   如何将该二维方法扩展到三维真实地质环境？
*   在反演中允许裂缝数量变化（可逆跳跃MCMC）是否会显著改善结果？
*   不同应力观测分量（例如大小 vs. 方位）对反演灵敏度的相对权重如何最优确定？
*   该方法在实际深部EGS井中的表现如何，面临哪些额外挑战（如数据稀疏性、计算成本）？
*   能否利用其他类型的地球物理观测（如微震事件、温度异常）与应力数据联合反演？

## Source Coverage
索引片段共18个，覆盖论文第1-9页，包括摘要、引言、方法学（正向模拟、贝叶斯反演、MCMC细节）和测试案例。关键部分（如方法论框架、观测要求、2D假设、裂缝数量固定、测试结果）均有明确记录。论文结尾部分（讨论、展望）未包含在索引片段中。
