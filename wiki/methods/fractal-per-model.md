---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "渗透率增强率分形模型 (Fractal PER Model)"
aliases:
  - "fractal permeability enhancement ratio model"
sources:
  - "2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi"
---

# 渗透率增强率分形模型 (Fractal PER Model)

## Purpose

将裂缝迹长分形维数、迂曲分形维数和体积应变等参数代入公式，计算各向异性渗透率增强率 (PER)。
## Aliases

- fractal permeability enhancement ratio model
## Workflow

提取三维网络各截面裂缝迹线，计算各自的分形维数（Df, DT, Dl）；结合体积应变 εv 代入模型公式，得到不同方向 PER。
## Inputs

- 裂缝迹长分形维数 Df
- 迂曲维数 DT, Dl
- 体积应变 εv
## Outputs

- PER_x, PER_y, PER_z
## Assumptions

- 各维数代表对应方向的有效值
- 裂缝宽度与长度成比例
## Strengths

- 从分形统计直接外推渗透增强
## Limitations

- 未完全耦合多分形维数
- 基于等效二维截面
## Related Concepts

- not-confirmed-from-current-pages
## Source Papers

- [2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi](../papers/2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi.md)
