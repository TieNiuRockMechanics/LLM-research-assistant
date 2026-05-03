---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "波形矩张量反演 (Moment Tensor Inversion)"
aliases:
  - "Full Waveform Moment Tensor Inversion"
sources:
  - "2014-zang-analysis-of-induced-seismicity-in-geothermal-reservoirs-an-overview"
---

# 波形矩张量反演 (Moment Tensor Inversion)

## Purpose

通过拟合观测到的井下或地面地震波形，求解事件的完整地震矩张量，区分微地震的剪切、张裂和压缩体积分量。
## Aliases

- Full Waveform Moment Tensor Inversion
## Workflow

挑选高信噪比的多分量宽频波形记录；计算理论格林函数；利用全局或梯度下降法寻找最优矩张量元素使合成波形与实测波形最佳拟合；将矩张量分解为各向同性 (ISO)、补偿线性矢量偶极 (CLVD) 和双力偶 (DC) 分量。
## Inputs

- 高质量三分量宽频地震波形
- 精确速度模型
## Outputs

- 地震矩张量
- 矩震级 Mw
- 破裂机制的剪切、张裂和 CLVD 百分比
## Assumptions

- 震源破裂过程可近似为同步点源
- 格林函数能有效模拟复杂波路径
## Strengths

- 能区分注入导致的是水力拉张微破裂还是远场剪切滑动
- 可用于反演局部应力场
## Limitations

- 对低频微震信噪比不足时可靠性降低
- 反演对速度模型不准较敏感
- 低震级事件解的非唯一性强
## Related Concepts

- induced-seismicity
## Source Papers

- [2014-zang-analysis-of-induced-seismicity-in-geothermal-reservoirs-an-overview](../papers/2014-zang-analysis-of-induced-seismicity-in-geothermal-reservoirs-an-overview.md)
