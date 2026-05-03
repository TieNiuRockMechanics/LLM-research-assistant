---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "嵌入式离散裂缝模型 (EDFM)"
aliases:
  - "EDFM"
  - "嵌入式裂缝模型"
sources:
  - "2024-zhang-fracture-network-characterization-and-thermal-performance-prediction-in-enhanced-geot"
---

# 嵌入式离散裂缝模型 (EDFM)

## Purpose

将离散裂缝嵌入结构化基质网格中，通过传导率计算裂缝-基质交换，避免网格重构，适用于复杂裂缝网络的流动模拟。
## Aliases

- EDFM
- 嵌入式裂缝模型
## Workflow

生成背景网格，将裂缝与网格相交计算连接对，分配传导率，组装矩阵求解。
## Inputs

- 基质网格
- 裂缝几何及属性
## Outputs

- 压力、温度分布
- 产量/注入量
## Assumptions

- 裂缝可嵌入而不改变网格
- 基质与裂缝间的流动由传导率描述
## Strengths

- 计算高效
- 适合裂缝网络反演
## Limitations

- 不能解析裂缝尖端细节
- 大裂缝与基质间需适当加密
## Related Concepts

- discrete-fracture-network
## Source Papers

- [2024-zhang-fracture-network-characterization-and-thermal-performance-prediction-in-enhanced-geot](../papers/2024-zhang-fracture-network-characterization-and-thermal-performance-prediction-in-enhanced-geot.md)
