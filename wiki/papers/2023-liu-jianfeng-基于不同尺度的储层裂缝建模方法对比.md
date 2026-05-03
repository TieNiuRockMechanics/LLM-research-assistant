---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-liu-jianfeng-基于不同尺度的储层裂缝建模方法对比"
title: "基于不同尺度的储层裂缝建模方法对比."
status: "draft"
source_pdf: "data/papers/2023 - 基于不同尺度的储层裂缝建模方法对比.pdf"
collections:
  - "大论文-离散裂缝网络"
citation: "Liu Jianfeng, et al. \"基于不同尺度的储层裂缝建模方法对比.\" 地球物理学进展, vol. 38, no. 5, 2023, pp. 2071-2079. doi:10.6038/pg2023GG0552. Accessed 2026."
indexed_texts: "7"
indexed_chars: "30852"
nonempty_source_blocks: "7"
compiled_source_blocks: "7"
compiled_source_chars: "30991"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004505"
coverage_status: "full-index"
source_signature: "7a9036c8c93ded0cd135f31aa1c2baa5a2f94fc1"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T07:17:20"
---

# 基于不同尺度的储层裂缝建模方法对比.

## One-line Summary

本文对比了基于裂缝尺度划分的三类储层裂缝建模方法——叠前地震属性预测大尺度裂缝、基于微地震事件的DFN随机建模表征中尺度裂缝、计算机断层扫描获取小尺度裂缝模型，并指出单一建模方法存在尺度局限，多尺度裂缝信息整合是新的研究方向。

## Research Question

如何根据不同裂缝尺度选择有效的建模方法，并整合不同尺度裂缝信息以提高低孔低渗透储层裂缝三维地质建模的全面性和精确性。

## Study Area / Data

本文为方法对比综述，未指定具体研究区或案例数据。文中引用的数据来源及方法包括：地震数据（叠前/叠后属性、OVT道集）、微地震事件数据、成像测井（FMI）数据、岩芯CT扫描切片等。

## Methods

依据裂缝尺度，将裂缝建模方法归纳为三类：

1. **大尺度裂缝建模**：基于叠前地震属性的预测方法，包括椭圆拟合方位各向异性分析、结合OVT域五维地震属性的裂缝预测（印兴耀等，2018；周路等，2023）。  
2. **中尺度裂缝建模**：基于微地震事件的DFN（离散裂缝网络）随机建模，通过模拟退火算法优化目标函数，并利用拓扑结构（CC、IC、II节点分类）剔除孤立区域（许德友等，2016；Ardakani等，2018）；结合FMI成像测井获取裂缝产状校正地震预测结果（王蓓等，2019；Babasafari等，2022）。  
3. **小尺度裂缝建模**：计算机断层扫描（CT）定量表征微米级裂缝（Lai等，2017），并结合计算机视觉技术（轮廓检测、空间矩/中心距分析）在X、Y、Z三个方向上独立识别裂缝后合成三维模型（Singh等，2021）。  
4. **多尺度耦合**：采用分布函数匹配法恢复多尺度裂缝规模分布函数，实现不同尺度模型整合（董少群等，2020）。

## Key Findings

1. 叠前地震属性比叠后属性包含更丰富的地质信息，可预测大尺度裂缝的发育方向、强度和密度；OVT域五维地震属性通过高精度方位各向异性分析进一步提高了大尺度裂缝预测精度。  
2. 基于微地震事件的DFN随机建模能检测更多中小尺度裂缝，通过拓扑优化剔除孤立节点区域，使模型更贴近实际油气生产。  
3. 计算机断层扫描技术可定量表征微米级小尺度裂缝，结合计算机视觉从三维切片中准确区分裂缝与基质，提升小尺度裂缝信息的精确度。  
4. 单一尺度建模方法无法全面反映储层裂缝的多尺度特性，基于裂缝特征细分尺度并整合多源信息进行建模已成为新的研究方向。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 大尺度裂缝可通过地震属性识别，延伸长度>68 m，宽度>10 mm | Liu 2023, pp. 1-2 | 低孔低渗透储层裂缝分类标准 | 定义源于李阳等（2016） |
| 叠前地震属性利用椭圆拟合方法预测裂缝方向、密度和强度 | Liu 2023, pp. 2-3 | 地震波衰减与裂缝走向垂直时快，平行时慢 | 拟合椭圆长轴为裂缝方向，长短轴比为密度，离心率为强度 |
| 结合OVT域五维地震属性进行方位各向异性分析可提高裂缝识别精度 | Liu 2023, pp. 3-4 | OVT道集包含X、Y、time、偏移距、方位角五维信息 | 詹仕凡等（2015）说明AVO梯度与方位角余弦变化关系 |
| DFN随机建模可通过微地震事件点调节裂缝模型，目标是最小化事件点到裂缝面的距离并最大化事件点覆盖率 | Liu 2023, pp. 4-5 | 假设位置相近且共面的微震事件属于同一裂缝 | 采用模拟退火算法求解，许德友等（2016）改进方法 |
| 拓扑结构优化DFN模型，将裂缝连接节点分为孤立（I）、相邻（X/Y）和交叉，保留高度连接和部分连接区域 | Liu 2023, pp. 5 | 裂缝模型分为CC、IC、II三类连接形式 | 孤立及死角裂缝网络对整体渗流贡献小，可剔除 |
| FMI成像测井可获取裂缝倾角和方位角，校正地震预测的裂缝走向和密度 | Liu 2023, pp. 5 | 标准裂缝在FMI图像中呈正弦曲线特征 | 马燕和陈小东（2018）说明测量原理 |
| CT扫描通过X射线衰减系数差异区分岩芯与裂缝，CT值公式：CT_number = (μc - μω)/μω × 1000 | Liu 2023, pp. 6 | 体素为基本单元，二维切片堆叠成三维模型 | 物质密度越高CT值越大，可有效区分裂缝 |
| 计算机视觉结合切片分析，在两个及以上方向上被识别为裂缝的体素才标记为裂缝 | Liu 2023, pp. 6-7 | 使用OpenCV FindContours函数提取轮廓属性，计算空间矩和中心距 | 裂缝具有细长结构、发育方向和长度远大于宽度的特征 |
| 多尺度裂缝建模需整合不同尺度模型，利用分布函数匹配法恢复整体规模分布 | Liu 2023, pp. 7 | 不同尺度裂缝规模分布函数具有相似性 | 董少群等（2020）提出 |

## Limitations

1. 叠前属性预测大尺度裂缝虽优于叠后，但精度仍受限于地震分辨率，难以精确解释中尺度裂缝。  
2. 基于微震事件的DFN随机建模依赖微震检测精度和先验统计信息，裂缝常被过度模拟，需拓扑优化修正。  
3. 小尺度裂缝CT建模受限于扫描分辨率，难以有效识别孔隙和微裂缝网络；计算机视觉方法需要体素在多方向上确认，可能漏识部分单方向裂缝。  
4. 多尺度耦合方法（分布函数匹配法）的适用条件和普适性未在文中深入讨论。  
5. 本文为综述性对比，未提供实际工区应用效果的定量对比数据。

## Assumptions / Conditions

- 裂缝分类按尺度标准：大尺度（延伸长度>68 m，宽度>10 mm），中尺度（17~68 m，宽度>10 mm），小尺度（<17 m，宽度0.1~10.0 mm）（李阳等，2016）。  
- 地震波衰减各向异性与裂缝走向相关，可据此预测裂缝方向。  
- 微震事件点空间位置可代表水力压裂产生的中尺度裂缝几何形状。  
- 岩芯CT扫描中，裂缝与基质的X射线衰减系数存在显著差异。  
- 裂缝具有细长几何特征，可在二维切片中通过轮廓检测识别。  
- 多尺度建模时，不同尺度裂缝的规模分布函数具有相似性。

## Key Variables / Parameters

- **大尺度裂缝**：椭圆拟合长轴（方向）、长短轴比（密度）、离心率（强度）；OVT域AVO梯度方位角余弦参数。  
- **中尺度裂缝**：DFN模型中微震事件到裂缝面的正交平方距离、裂缝椭圆面面积；模拟退火温度T、Metropolis准则系数Ap；拓扑节点类型I、X、Y。  
- **小尺度裂缝**：CT值（亨氏单位HU）、X射线线性衰减系数μ、体素空间矩m_ji和中心距mu_ji。  
- **多尺度耦合**：裂缝规模分布函数。

## Reusable Claims

1. 在低孔低渗储层中，裂缝具有多尺度性，大尺度裂缝控制油气保存，中尺度控制渗流系统，小尺度起储集作用（薛艳梅等，2014）[条件：致密储层裂缝特征分类]。  
2. 叠前地震属性（椭圆拟合、OVT域五维地震属性）可预测大尺度裂缝的方向、强度和密度，较叠后属性信息更丰富[Liu 2023, pp. 2-4][条件：地震数据方位角覆盖充分]。  
3. 基于微地震事件的DFN随机建模能够利用微震事件点位置约束裂缝面，通过模拟退火算法实现裂缝网络优化[Liu 2023, pp. 4-5][条件：微震事件定位精度高，裂缝产状可近似为椭圆面]。  
4. 拓扑结构分析可剔除DFN中孤立及死角裂缝网络，保留连通性高的部分，提升模型对渗流的表征能力[Liu 2023, pp. 5][条件：裂缝网络节点可分为I、X、Y三类]。  
5. 计算机断层扫描结合计算机视觉轮廓检测和空间矩分析，可在体素级别标记裂缝，实现小尺度裂缝三维定量表征[Liu 2023, pp. 6-7][条件：至少两个方向识别为裂缝的体素才被标记]。  
6. 多尺度裂缝建模需根据裂缝尺度选择对应方法并利用分布函数匹配法整合，是低孔低渗储层三维地质建模的重要思路[Liu 2023, pp. 7][条件：不同尺度裂缝规模分布函数相似]。

## Candidate Concepts

- [[Multi-scale fracture characterization]]
- [[Low-porosity low-permeability reservoir]]
- [[Discrete Fracture Network (DFN)]]
- [[Pre-stack seismic attributes]]
- [[Computed Tomography (CT) for rock fractures]]
- [[Topological optimization of fracture networks]]
- [[Ellipse fitting method]]
- [[OVT domain five-dimensional seismic data]]
- [[FMI imaging logging]]
- [[Computer vision for fracture detection]]

## Candidate Methods

- [[Pre-stack fracture prediction using ellipse fitting]]
- [[DFN stochastic modeling based on microseismic events]]
- [[Simulated annealing optimization for DFN]]
- [[Volume scanline sampling with topology analysis]]
- [[FMI-based fracture attribute correction]]
- [[X-ray CT 3D reconstruction of fractures]]
- [[Slice-wise contour detection and moment analysis]]
- [[Multi-scale distribution function matching]]

## Connections To Other Work

- 叠前属性裂缝预测引用印兴耀等（2018）椭圆拟合原理，詹仕凡等（2015）OVT域属性分析，周路等（2023）五维地震属性在栖霞组应用。  
- DFN随机建模基于Baecher等（1977）经典模型，由Seifollahi等（2014）微震驱动方法发展而来，许德友等（2016）、Ardakani等（2018）进一步改进。  
- 小尺度裂缝表征参考Lai等（2017）工业CT定量分析，Singh等（2021）计算机视觉与无监督机器学习方法。  
- 多尺度耦合方法参考董少群等（2020）致密砂岩储层多尺度裂缝三维地质建模方法。  
- 整体研究思路与代瑞雪等（2017）、赵春段等（2022）多尺度裂缝预测建模一致。

## Open Questions

1. 如何进一步融合叠前地震、微震、测井和岩芯信息，建立高精度的全尺度裂缝模型？  
2. 多尺度裂缝耦合的分布函数匹配法在不同储层类型中的适用性如何？  
3. 小尺度裂缝建模中，如何利用神经网络或机器学习自动提取裂缝特征并提高分辨率？  
4. 实际生产开发中，如何定量评估不同尺度裂缝对产能的贡献，并优化模型渗透性调整策略？  
5. 针对裂缝被过度模拟的问题，是否存在更有效的先验约束或后处理方法？

## Source Coverage

所有7个非空索引片段均已处理。覆盖情况：源文本块数覆盖率100%，字符覆盖率100.45%（因片段间存在必要重叠）。
