---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "地质力学约束的裂缝网络升尺度方法"
aliases:
  - "geomechanically-constrained upscaling"
sources:
  - "2015-lei-a-new-approach-to-upscaling-fracture-network-models-while-preserving-geostatistical-and"
---

# 地质力学约束的裂缝网络升尺度方法

## Purpose

将露头尺度获取的二维裂隙网络生长至更大尺度（如储层尺度）的上尺度方法，既保持裂缝网络的统计几何特征，又融入由有限元-离散元 (FEMDEM) 模拟导出的、与应力和位移相关的裂隙孔径和剪切位移分布。
## Aliases

- geomechanically-constrained upscaling
## Workflow

从源头（露头）模式提取裂隙的统计属性，如分形维数、幂律指数和空间排列规则；对源头模式施加代表现场条件的应力进行 FEMDEM 模拟，获取每条裂隙的剪切位移、法向位移和相应的孔径；建立位移-长度或孔径-长度的经验缩放关系；以源头模式为“生长细胞”，在自我复制和随机游走中放大到目标大尺度，同时保持几何拓扑不变和地应力标度关系；计算升尺度后网络的等效渗透率。
## Inputs

- 小尺度（如露头）的裂隙掩膜
- 模型的材料力学参数和应力边界条件
- 目标生长尺度
## Outputs

- 大尺度的、带有地质力学约束孔径和位移的三维 DFN 模型
- 升尺度后的等效渗透率
## Assumptions

- 所研究的裂隙模式统计上平稳（如具非分形的空间组织，D≈2）
- 裂隙内初始孔径满足线性断裂力学的次线性平方根缩放律
- 生长在更高的尺度复制相同的母分布统计特征
## Strengths

- 能将力学约束（应力相关的孔径）注入统计生成的大尺度 DFN 中，比纯几何放大更物理
## Limitations

- 二维分析与真实三维裂隙网络有本质差异（不连续的层、层跨切未捕捉）
- 要求起始裂隙源的网格是统计平稳的，这在很多地点不成立
- 许多重要的破裂抑制/导向机制（如地质力学停止）被忽略
## Related Concepts

- permeability-upscaling
- discrete-fracture-network
## Source Papers

- [2015-lei-a-new-approach-to-upscaling-fracture-network-models-while-preserving-geostatistical-and](../papers/2015-lei-a-new-approach-to-upscaling-fracture-network-models-while-preserving-geostatistical-and.md)
