---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "PFC-FDEM 跨尺度热力断裂模拟"
aliases:
  - "PFC-FDEM multi-scale thermal-mechanical simulation"
  - "跨尺度裂纹网络映射与优化"
sources:
  - "2025-zhai-pfc-fdem-multi-scale-cross-platform-numerical-simulation-of-thermal-crack-network-evol"
---

# PFC-FDEM 跨尺度热力断裂模拟

## Purpose

在微观颗粒流 (PFC) 中模拟热裂纹萌生，再将裂纹网络映射到宏观有限元-离散元 (FDEM) 模型中进行动态断裂分析，实现热-力顺序耦合的跨尺度模拟。
## Aliases

- PFC-FDEM multi-scale thermal-mechanical simulation
- 跨尺度裂纹网络映射与优化
## Workflow

在 PFC 中建立颗粒模型，施加温度边界通过顺序耦合计算热应力和裂纹；对生成的热裂纹网络进行拓扑优化（如 Weibull 调制长度、方向余弦退火优化）以降低计算量；通过能量一致性校正将裂纹映射到 FDEM 中；在 FDEM 中施加动态载荷（如 SHTB）并采用解耦 DIF 模型近似应变率效应。
## Inputs

- PFC 矿物颗粒参数
- 加热曲线
- FDEM 材料参数
- 动态载荷
## Outputs

- 多温度下热裂纹网络
- 动态断裂响应（应力-应变、扩展路径）
## Assumptions

- 顺序热力耦合，力场对温度场反作用忽略
- 二维平面应力
- 应变率效应可解耦处理
## Strengths

- 直接追踪热裂纹萌生到宏观断裂的全过程
- 跨尺度映射保证能量一致性
## Limitations

- 二维模型，高密度裂纹交互误差增大
- 参数标定复杂（需 PSO 等多目标优化）
## Related Concepts

- thermal-damage
- cohesive-zone-model
- crack-length-optimization
## Source Papers

- [2025-zhai-pfc-fdem-multi-scale-cross-platform-numerical-simulation-of-thermal-crack-network-evol](../papers/2025-zhai-pfc-fdem-multi-scale-cross-platform-numerical-simulation-of-thermal-crack-network-evol.md)
