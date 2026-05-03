---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "投影法评估裂缝连通性"
aliases:
  - "projection connectivity"
  - "一维连通性 χ"
sources:
  - "2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi"
---

# 投影法评估裂缝连通性

## Purpose

将二维孔壁图像向量化投影到一维，通过连通段占比评估裂缝连通性。
## Aliases

- projection connectivity
- 一维连通性 χ
## Workflow

孔壁图像二值化，沿钻孔方向投影为一维数组，计算裂缝连通段总长/钻孔长度得到 χ。
## Inputs

- 孔壁二值图像
## Outputs

- χ
## Assumptions

- 投影方向与钻孔一致
## Strengths

- 快速
## Limitations

- 仅一维方向连通性
## Related Concepts

- not-confirmed-from-current-pages
## Source Papers

- [2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi](../papers/2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi.md)
