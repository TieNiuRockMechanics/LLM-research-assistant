---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "对数正态分布拟合 (Log‑normal Fitting)"
aliases:
  - "对数正态分布拟合"
sources:
  - "2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers"
---

# 对数正态分布拟合 (Log‑normal Fitting)

## Purpose

用对数正态分布拟合裂缝迹长直方图，获得 μ 和 σ 参数，用于定量比较生成网络与真实网络。
## Aliases

- 对数正态分布拟合
## Workflow

测量所有裂缝长度，绘制直方图，用修正的对数正态分布函数拟合，提取 μ, σ。
## Inputs

- 裂缝长度测量值
## Outputs

- μ, σ
- 拟合优度
## Assumptions

- 迹线长度服从对数正态分布（因低端截断）
## Strengths

- 简单直观
## Limitations

- 三维尺寸分布可能不同
## Related Concepts

- not-confirmed-from-current-pages
## Source Papers

- [2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers](../papers/2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers.md)
