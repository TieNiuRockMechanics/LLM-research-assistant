---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "Dips 软件裂缝产状分组"
aliases:
  - "Dips"
  - "下半球投影"
sources:
  - "2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi"
---

# Dips 软件裂缝产状分组

## Purpose

利用下半球施密特投影和聚类分析对裂缝方位进行分组，识别优势组。
## Aliases

- Dips
- 下半球投影
## Workflow

导入裂缝倾向/倾角数据，生成极点图；自动或手动聚类，每个组拟合 Fisher 分布。
## Inputs

- 倾向/倾角数据
## Outputs

- 优势组数
- 平均方向
- Fisher k
## Assumptions

- 每组服从 Fisher 分布
## Strengths

- 可视化清晰
## Limitations

- 三组以上复杂分布可能重叠
## Related Concepts

- not-confirmed-from-current-pages
## Source Papers

- [2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi](../papers/2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi.md)
