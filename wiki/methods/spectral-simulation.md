---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "谱型模拟 (FFT 法)"
aliases:
  - "FFT-based simulation"
  - "frequency-domain simulation"
sources:
  - "1985-miller-spectral-type-simulation-of-spatially-correlated-fracture-set-properties"
---

# 谱型模拟 (FFT 法)

## Purpose

生成具有给定变异函数或协方差函数的空间相关随机场，用于模拟裂隙属性。
## Aliases

- FFT-based simulation
- frequency-domain simulation
## Workflow

由变异函数导出协方差，经 FFT 获得谱密度，分配随机傅里叶系数后逆变换，得到空间相关序列。
## Inputs

- 变异函数
- 分布类型（正态或指数）
## Outputs

- 具有空间相关性的裂隙属性（如产状、间距）
## Assumptions

- 协方差平稳
- 属性分布已知
## Strengths

- 计算高效
## Limitations

- 隐含周期性假设，可能不适用于非平稳数据
- 未考虑互相关
## Related Concepts

- spatial-correlation
- variogram
## Source Papers

- [1985-miller-spectral-type-simulation-of-spatially-correlated-fracture-set-properties](../papers/1985-miller-spectral-type-simulation-of-spatially-correlated-fracture-set-properties.md)
