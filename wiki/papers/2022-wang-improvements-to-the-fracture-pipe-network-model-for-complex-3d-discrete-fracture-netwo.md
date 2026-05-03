---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-wang-improvements-to-the-fracture-pipe-network-model-for-complex-3d-discrete-fracture-netwo"
title: "Improvements to the Fracture Pipe Network Model for Complex 3D Discrete Fracture Networks."
status: "draft"
source_pdf: "data/papers/2022 - Improvements to the Fracture Pipe Network Model for Complex 3D Discrete Fracture Networks.pdf"
collections:
citation: "Wang, Chenhui, et al. \"Improvements to the Fracture Pipe Network Model for Complex 3D Discrete Fracture Networks.\" 2022."
indexed_texts: "12"
indexed_chars: "58030"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "57826"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.996485"
coverage_status: "full-index"
source_signature: "17cb29dc7e3dbea44f909b41b58e9c46d4d9f745"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T05:32:45"
---

# Improvements to the Fracture Pipe Network Model for Complex 3D Discrete Fracture Networks.

## One-line Summary
本研究针对复杂三维离散裂缝网络（DFN），提出四项改进以提升裂缝管道网络模型（FPNM）的渗透率预测精度，并通过合成与真实裂缝样本验证了改进效果。[Wang 2022, pp. 1-1]

## Research Question
现有的基于质心和交线方法（CIM）的裂缝管道网络模型在应用于复杂互连的离散裂缝网络时，所计算的流体流动特性（如渗透率）会出现较大偏差，如何改进FPNM的管道传导率分配及网络拓扑构建，以提高其在复杂三维DFN中的精度与适用性？[Wang 2022, pp. 1-1, 1-2, 5-7]

## Study Area / Data
- 合成DFN测试案例：
  - 两个用于验证传统Guo模型的三维DFN：Model 1（5条规则裂缝）和Model 2（8条定向裂缝），模型大小为100³体素，分辨率1 μm/体素。[Wang 2022, pp. 5-7]
  - 六个复杂度递增的“子DFN”场景（sub1至sub6），从Model 2分离而来，用于量化不同复杂度下模型的性能。[Wang 2022, pp. 7-8]
  - 两个由ADFNE开源代码生成的基准DFN：S1（74条裂缝）和S2（157条裂缝），采用正方形裂缝，边长服从指数分布，孔径分别为5 μm和7 μm。[Wang 2022, pp. 10-12]
- 实际裂缝样本：两个碳酸盐岩储层的微CT图像提取的等效DFN——R1（两条相交裂缝，图像300³体素）和R2（四条裂缝，图像600³体素），分辨率均为13 μm/体素。[Wang 2022, pp. 12-13]
- 参考数值模拟：采用格子玻尔兹曼方法（LBM），D3Q19离散速度方案，多松弛时间模型，恒定压力边界，收敛于10000个迭代步内。[Wang 2022, pp. 4-5]

## Methods
- **传统FPNM构建（Guo模型）**：采用质心和交线方法（CIM），每条裂缝由质心到交线中点构建管道，并利用等效矩形和立方定律计算管道传导率。质心节点长度计算为 \( l_c = \frac{2D}{N_i} \cdot \frac{l_i}{\overline{l_i}} \)，其中 \( D \) 为直径，\( N_i \) 为交线条数。[Wang 2022, pp. 2-4]
- **复杂性量化指标**：提出两个指标——平均交线数 (\( N_{il} \)) 和平均交点数 (\( N_{ip} \))，用于衡量DFN结构的复杂程度。[Wang 2022, pp. 5-7]
- **四项改进**：
    1. **质心节点长度修正**：从式(4)分母中移除交线条数 \( N_i \)，改为 \( l_c = \sqrt{4A/\pi} \cdot (l_i / \overline{l_i}) \)，以避免因交线过多而过度减小节点长度和等效宽度。[Wang 2022, pp. 7-8]
    2. **边界节点长度修正**：将边界节点所连接的键长度减去边界节点半径，以消除将半球节点作为整球处理带来的额外压降。[Wang 2022, pp. 7-9]
    3. **节点截面积修正**：利用相交裂缝间的二面角 \( \theta \) 计算节点面积，将传导率缩放为 \( g \sim 1/(\sin\theta)^2 \)，以反映交会区扩大的过流面积。[Wang 2022, pp. 8-9]
    4. **节点与键的合并**：后处理合并重叠或共位的节点和键，删除冗余连接，确保网络拓扑正确。[Wang 2022, pp. 9-10]
- **渗透率计算**：基于单相不可压缩层流假设，通过节点压力求解线性方程组，利用达西定律计算渗透率。[Wang 2022, pp. 4-5]
- **参考方法**：LBM用于生成渗透率真值以评估FPNM的偏差（\( \text{deviation} = \frac{k_{\text{FPNM}} - k_{\text{LBM}}}{k_{\text{LBM}}} \times 100\% \)）。[Wang 2022, pp. 5-7]

## Key Findings
- 传统Guo模型仅在简单DFN中预测准确；对于复杂DFN（Model 2），渗透率偏差高达−40%至−49%，且偏差随复杂度指标增加而增大。[Wang 2022, pp. 5-7]
- 四项改进逐步降低平均偏差：改进1后偏差从−35%降至−18%（改善~17%）；改进2后降至−7%（改善~11%）；改进3后降至−5.6%（改善~1.4%）；改进4后降至−4.5%（改善~1.1%）。[Wang 2022, pp. 7-10]
- 在S1和S2两个基准DFN上，改进后的FPNM与LBM的偏差分别为−9.31%至−11.24%和−5.03%至−8.38%，远优于Guo模型的−60%至−67%。计算时间（数秒）仅为LBM（~500秒）的极小部分。[Wang 2022, pp. 12]
- 实际样本R1和R2的改进FPNM偏差在−15.50%~20.31%和−18.08%~13.48%之间，优于Guo模型，但偏差大于基准案例，可能源于立方定律假设和LBM分辨率限制。[Wang 2022, pp. 12-13]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| Guo模型在Model 1上的渗透率偏差：kx −3.42%, ky −5.12%, kz 0.02% | [Wang 2022, pp. 5-7] Table 1 | 简单DFN，5条矩形裂缝，100³体素，1 μm/voxel | 规则网络，交线少 |
| Guo模型在Model 2上的渗透率偏差：−40.89% ~ −49.23% | [Wang 2022, pp. 5-7] Table 1 | 复杂DFN，8条定向裂缝，100³体素，1 μm/voxel | 高交线数，复杂拓扑 |
| 六个子DFN的Guo模型k与LBM偏差，平均偏差随复杂度增加，最高−49.61% | [Wang 2022, pp. 7-9] Table 3, Figure 4 | sub1~sub6，Nil=5.0~6.0，Nip=0~6.13 | 偏差与Nil/Nip正相关 |
| 改进1后六个子DFN平均偏差从−35%降至−18% | [Wang 2022, pp. 7-8] Figure 4, Table S1 | 去除 Ni 的质心长度公式 | 主要提升源于等效宽度校正 |
| 改进1+2后平均偏差降至−7% | [Wang 2022, pp. 8-9] Figure 4 | 边界节点键长减去半径 | 边界处理贡献~11%改善 |
| 改进1+2+3后平均偏差降至−5.6% | [Wang 2022, pp. 9-10] Figure 4 | 二面角缩放传导率 | 改善幅度较小，仅应用于节点 |
| 全部四项改进后平均偏差降至−4.5% | [Wang 2022, pp. 10] Figure 4 | 后处理合并节点/键 | 拓扑校正为主，偏差降低1.1% |
| 基准案例S1改进FPNM偏差：kx −9.31%, ky −8.71%, kz −11.24% | [Wang 2022, pp. 12] Table 4 | 74条裂缝，孔径5 μm，正方形，指数边长分布 | Guo模型偏差约−60% |
| 基准案例S2改进FPNM偏差：kx −5.03%, ky −7.51%, kz −8.38% | [Wang 2022, pp. 12] Table 4 | 157条裂缝，孔径7 μm | 复杂互联，偏差远小于Guo模型 |
| 实际样本R1改进FPNM偏差：kx +13.27%, ky +20.31%, kz −15.50% | [Wang 2022, pp. 13] Table 5 | 碳酸盐岩微CT, 300³ voxels, 13 μm/voxel | 低交线，两个裂缝相交 |
| 实际样本R2改进FPNM偏差：kx +13.48%, kz −18.08% (Y方向不连通) | [Wang 2022, pp. 13] Table 5 | 600³ voxels, 4 fractures, min aperture 4 voxels | LBM分辨率可能引入误差 |
| 计算效率对比：FPNM数秒，LBM平均~500秒 | [Wang 2022, pp. 12] | 个人笔记本（i7 CPU, 32 GB RAM） | FPNM大幅节省计算资源 |

## Limitations
- 模型假设裂缝为规则形状（矩形或椭圆）且孔径恒定，未引入粗糙度或孔径变化。[Wang 2022, pp. 13-14]
- 仅考虑完全张开的裂缝，未包括矿物沉淀导致的闭合或部分充填裂缝。[Wang 2022, pp. 13-14]
- 当前FPNM仅适用于无基质孔隙的裂缝网络，尚未耦合基质孔隙流。[Wang 2022, pp. 14]
- 基准验证中LBM作为参考存在固有数值误差，其精度受制于空间分辨率和松弛参数，尤其当裂缝孔径仅几个格点（如实测R2的4体素）时可能引入较大误差。[Wang 2022, pp. 12-13]
- 实际案例渗透率偏差较大，部分可能源于立方定律对真实裂缝流动描述的不足。[Wang 2022, pp. 12-13]

## Assumptions / Conditions
- 流体为单相、不可压缩层流，满足Stokes方程和立方定律。[Wang 2022, pp. 4, 13]
- 裂缝壁面为无滑移边界。[Wang 2022, pp. 3]
- 边界条件：模型入口和出口为恒定压力，其余面为无流动边界。[Wang 2022, pp. 4]
- 管道网络的节点压力定义在节点中心，压降仅发生在连接的键上。[Wang 2022, pp. 4]
- 裂缝由等效矩形子域表示，其传导率基于立方定律和Darcy定律推导。[Wang 2022, pp. 3-4]
- LBM模拟采用D3Q19 MRT格式，初始速度为零，恒定压力梯度，固体壁面使用反弹边界。[Wang 2022, pp. 5]
- 实际裂缝网络提取时通过连通性分析移除孤立裂缝，确保网络完全渗透。[Wang 2022, pp. 10-12]

## Key Variables / Parameters
- \( l_c \): 质心节点长度。[Wang 2022, pp. 3, 7]
- \( w_{eq} \): 等效矩形宽度。[Wang 2022, pp. 3]
- \( g_f \): 裂缝管道水力传导率。[Wang 2022, pp. 3]
- \( N_{il} \): 平均交线数（复杂度指标）。[Wang 2022, pp. 5-6]
- \( N_{ip} \): 平均交点数（复杂度指标）。[Wang 2022, pp. 6]
- \( D \) 或 \( A \): 裂缝直径或面积。[Wang 2022, pp. 3, 5]
- \( b \): 裂缝孔径。[Wang 2022, pp. 3]
- \( \theta \): 二面角，用于相交节点面积修正。[Wang 2022, pp. 8]
- \( r_n \): 边界节点半径，用于键长修正。[Wang 2022, pp. 8]
- \( k \): 绝对渗透率。[Wang 2022, pp. 4]

## Reusable Claims
- “传统的质心与交线方法（CIM）构建的FPNM在复杂互连的离散裂缝网络中会产生显著的渗透率偏差，偏差随网络复杂度的增加而增大。” Source: [Wang 2022, pp. 1-1, 5-7]，条件：采用Guo et al. (2018)的公式，矩形或椭圆裂缝，使用立方定律。
- “从质心节点长度公式(4)中去除交线条数\( N_i \)可将复杂DFN的平均渗透率偏差降低约17个百分点（从−35%至−18%）。” Source: [Wang 2022, pp. 7-8] Fig. 4, 适用于交线较多的DFN。
- “将边界节点连接的键长度减去节点半径可进一步将平均偏差降低约11个百分点（−18%至−7%）。” Source: [Wang 2022, pp. 8-9] Fig. 4, 假设边界节点原按整球处理。
- “使用裂缝二面角θ对节点截面积和传导率进行缩放（\( g \sim 1/(\sin\theta)^2 \)）仅带来~1.4%的偏差改善，因为其影响仅限于节点区。” Source: [Wang 2022, pp. 8-9], 适用于交叉角度较小的裂缝交点时效果可能更明显。
- “对管道网络进行节点与键的合并后处理是确保复杂DFN拓扑正确性的必要步骤，可避免因重叠产生的冗余连接，并使偏差进一步降低约1.1%。” Source: [Wang 2022, pp. 9-10], 适用于存在质心重叠、交线中点重叠或重复键的DFN。
- “改进后的FPNM能够以极少的计算成本（数秒）获得与LBM模拟（~500秒）可比的渗透率，特别适合复杂三维DFN的快速评估。” Source: [Wang 2022, pp. 12] Table 4, 基于两个合成基准案例（74和157条裂缝）。
- “对于真实裂缝样本，改进FPNM的渗透率偏差（±13%~21%）显著优于传统Guo模型（偏差可达38%），但仍高于理想DFN案例，表明有必要进一步考虑孔径变化和粗糙度。” Source: [Wang 2022, pp. 13] Table 5, 样本R1和R2，碳酸盐岩微CT。

## Candidate Concepts
- [[fracture pipe network model (FPNM)]]
- [[discrete fracture network (DFN)]]
- [[centroid and intersection line method (CIM)]]
- [[Guo model]]
- [[cubic law]]
- [[equivalent rectangular domain]]
- [[seepage subdomain]]
- [[pore-scale laminar flow]]
- [[complexity indicators]] (average intersection line number, average intersection point number)
- [[dihedral angle]]
- [[node and bond merging]]

## Candidate Methods
- [[fracture pipe network model (FPNM)]]
- [[lattice Boltzmann method (LBM)]]
- [[centroid and intersection line method]]
- [[boundary element method (BEM)]] (used in prior work to derive pipe conductances)
- [[finite element method (FEM)]] (mentioned as computationally expensive alternative)
- [[non-conforming mesh method]]
- [[cubic law]]
- [[ADFNE open source code]]
- [[Palabos LBM solver]]
- [[ImageJ (Fiji)]] for fracture extraction from micro-CT

## Connections To Other Work
- 传统FPNM通常采用Guo et al. (2018)等提出的CIM方法[Wang 2022, pp. 1-2, 3]。
- Elsworth (1986) 提出混合边界元-有限元法分析DFN流动[Wang 2022, pp. 1-2]。
- Dershowitz and Fidelibus (1999) 使用边界元计算等效管道传导率，再结合FPNM[Wang 2022, pp. 1-2]。
- Sarkar et al. (2004) 表明裂缝内流体流向主要沿裂缝方向，不受全局压力梯度方向影响，这一发现支撑了仅将节点截面积修正局限于节点区的决定[Wang 2022, pp. 3, 9]。
- 当前改进FPNM的基准参考为LBM，基于Palabos平台，LBM与Navier-Stokes方程等价[Wang 2022, pp. 4-5]。
- 未来扩展计划包括与孔隙网络模型耦合，解决裂缝-基质流，并参考Scott et al. (2019)和Wang et al. (2020)的多尺度孔网建模工作[Wang 2022, pp. 14]。

## Open Questions
- 如何将改进FPNM与孔隙网络模型耦合，以同时描述裂缝和基质中的流动？[Wang 2022, pp. 14]
- 如何在FPNM中纳入裂缝粗糙度模型，以更好地表征真实裂缝的非立方律流动行为？[Wang 2022, pp. 14]
- 对于部分充填或非完全张开的裂缝，如何修正管道传导率的计算？[Wang 2022, pp. 13-14]
- 在实际应用中，如何自动、准确地从微CT图像中提取DFN并将其转化为FPNM，同时降低因人工提取引入的偏差？[Wang 2022, pp. 12-13, 13]

## Source Coverage
所有12个非空索引片段均被处理。区块覆盖率为100%（12/12），字符覆盖率为99.65%（57,826/58,030）。编译采用单阶段直通，未使用二次加工或外部知识。
