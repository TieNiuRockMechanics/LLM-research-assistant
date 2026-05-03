---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "单轴压缩试验 (Uniaxial Compression Test)"
aliases:
  - "UCS test"
  - "unconfined compression test"
  - "单轴压缩声发射试验"
sources:
  - "2020-qin-physical-and-mechanical-properties-of-granite-after-high-temperature-treatment"
  - "2021-kang-experimental-study-on-the-physical-and-mechanical-variations-of-hot-granite-under-diff"
  - "2025-bu-temperature-dependent-acoustic-emission-characteristics-and-statistical-constitutive-mod"
  - "2024-zheng-physical-and-mechanical-properties-and-damage-mechanism-of-sandstone-at-high-temperat"
  - "2017-yang-an-experimental-investigation-on-thermal-damage-and-failure-mechanical-behavior-of-gra"
  - "2018-zhang-laboratory-investigation-on-physical-and-mechanical-properties-of-granite-after-heati"
---

# 单轴压缩试验 (Uniaxial Compression Test)

## Purpose

测定岩石单轴抗压强度、弹性模量和泊松比，常同步进行声发射监测以分析损伤演化。适用于常温和高温热处理后试样。
## Aliases

- UCS test
- unconfined compression test
- 单轴压缩声发射试验
## Workflow

圆柱试样轴向加载至破坏，记录应力-应变曲线；可同步安装声发射传感器采集 AE 信号（振铃计数、振幅、b 值等）；对热损伤试样，需先进行热处理（慢加热、保温、冷却）。
## Inputs

- 直径与高度标准试件（如 φ50×100 mm）
- 加载速率
- 可选：AE 传感器及采集系统
## Outputs

- 单轴抗压强度 UCS
- 弹性模量 E
- 泊松比 ν
- AE 累积计数、起裂应力 σci、损伤应力 σcd
## Assumptions

- 均质连续
- 小变形
- 端面摩擦已消除
- AE 事件代表微裂纹
## Strengths

- 标准方法，结果可比较
- 可实时获取损伤信息
## Limitations

- 不能反映围压下行为
- 对试样缺陷敏感
## Related Concepts

- compressive-strength
- elastic-modulus
- brittle-ductile-transition
- thermal-damage
## Source Papers

- [2020-qin-physical-and-mechanical-properties-of-granite-after-high-temperature-treatment](../papers/2020-qin-physical-and-mechanical-properties-of-granite-after-high-temperature-treatment.md)
- [2021-kang-experimental-study-on-the-physical-and-mechanical-variations-of-hot-granite-under-diff](../papers/2021-kang-experimental-study-on-the-physical-and-mechanical-variations-of-hot-granite-under-diff.md)
- [2025-bu-temperature-dependent-acoustic-emission-characteristics-and-statistical-constitutive-mod](../papers/2025-bu-temperature-dependent-acoustic-emission-characteristics-and-statistical-constitutive-mod.md)
- [2024-zheng-physical-and-mechanical-properties-and-damage-mechanism-of-sandstone-at-high-temperat](../papers/2024-zheng-physical-and-mechanical-properties-and-damage-mechanism-of-sandstone-at-high-temperat.md)
- [2017-yang-an-experimental-investigation-on-thermal-damage-and-failure-mechanical-behavior-of-gra](../papers/2017-yang-an-experimental-investigation-on-thermal-damage-and-failure-mechanical-behavior-of-gra.md)
- [2018-zhang-laboratory-investigation-on-physical-and-mechanical-properties-of-granite-after-heati](../papers/2018-zhang-laboratory-investigation-on-physical-and-mechanical-properties-of-granite-after-heati.md)
