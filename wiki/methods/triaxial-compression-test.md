---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "三轴压缩试验 (Triaxial Compression Test)"
aliases:
  - "conventional triaxial compression test"
  - "三轴试验"
sources:
  - "2017-yang-experimental-investigation-on-triaxial-mechanical-and-permeability-behavior-of-sandsto"
  - "2015-yu-experimental-investigation-on-mechanical-properties-and-permeability-evolution-of-red-sa"
  - "2015-siratovich-saturated-heating-and-quenching-of-three-crustal-rocks-and-implications-for-ther"
  - "2016-yin-comparison-of-mechanical-properties-in-high-temperature-and-thermal-treatment-granite"
  - "2016-shao-effect-of-temperature-on-permeability-and-mechanical-characteristics-of-lignite"
---

# 三轴压缩试验 (Triaxial Compression Test)

## Purpose

测量不同围压和温度下的岩石强度、变形特性及同时测量渗透率，获取强度包络线（粘聚力 c、内摩擦角 φ）。
## Aliases

- conventional triaxial compression test
- 三轴试验
## Workflow

对圆柱试样施加围压 σ3，然后增加轴压 σ1 至破坏；可同步进行稳态或瞬态渗透率测量；也可在高温下进行（如 1000°C 高温三轴系统）。
## Inputs

- 围压 σ3
- 温度
- 加载速率
- 可选：渗流介质与孔隙压力
## Outputs

- 峰值偏应力 (σ1-σ3)max
- 粘聚力 c，内摩擦角 φ
- 应力-应变曲线
- 渗透率演化曲线
## Assumptions

- σ2 = σ3
- 刚性固体介质
- 有效应力原理（当有孔压时）
## Strengths

- 可模拟原位应力状态
- 可同时获取力学和水力性质
## Limitations

- 不反映真三轴路径（σ2≠σ3）
- 实验时间短，难以捕捉长期蠕变效应
## Related Concepts

- permeability-evolution
- strength-envelope
## Source Papers

- [2017-yang-experimental-investigation-on-triaxial-mechanical-and-permeability-behavior-of-sandsto](../papers/2017-yang-experimental-investigation-on-triaxial-mechanical-and-permeability-behavior-of-sandsto.md)
- [2015-yu-experimental-investigation-on-mechanical-properties-and-permeability-evolution-of-red-sa](../papers/2015-yu-experimental-investigation-on-mechanical-properties-and-permeability-evolution-of-red-sa.md)
- [2015-siratovich-saturated-heating-and-quenching-of-three-crustal-rocks-and-implications-for-ther](../papers/2015-siratovich-saturated-heating-and-quenching-of-three-crustal-rocks-and-implications-for-ther.md)
- [2016-yin-comparison-of-mechanical-properties-in-high-temperature-and-thermal-treatment-granite](../papers/2016-yin-comparison-of-mechanical-properties-in-high-temperature-and-thermal-treatment-granite.md)
- [2016-shao-effect-of-temperature-on-permeability-and-mechanical-characteristics-of-lignite](../papers/2016-shao-effect-of-temperature-on-permeability-and-mechanical-characteristics-of-lignite.md)
