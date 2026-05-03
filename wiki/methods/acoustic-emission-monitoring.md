---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "声发射监测 (Acoustic Emission Monitoring)"
aliases:
  - "AE monitoring"
  - "Acoustic Emission technique"
sources:
  - "2017-kumari-mechanical-behaviour-of-australian-strathbogie-granite-under-in-situ-stress-and-temp"
  - "2018-xu-acoustic-emission-and-damage-characteristics-of-granite-subjected-to-high-temperature"
  - "2023-cui-experimental-investigation-on-the-influence-on-mechanical-properties-and-acoustic-emiss"
  - "2023-ge-thermal-damage-of-high-temperature-sandstone-subjected-to-cooling-shock-and-its-effect-o"
  - "2025-zhu-physico-mechanical-properties-of-granite-after-thermal-treatments-using-different-cooli"
---

# 声发射监测 (Acoustic Emission Monitoring)

## Purpose

在岩石变形和破裂过程中实时监测微破裂产生的弹性波，用于分析损伤演化、破裂模式和破坏前兆。
## Aliases

- AE monitoring
- Acoustic Emission technique
## Workflow

在试件表面（或现场井孔）安装压电传感器；加载或注入过程中连续采集 AE 波形/参数（振铃计数、能量、幅值、RA-AF 值等）；可进行震源定位和 b 值分析。
## Inputs

- AE 传感器及采集系统
- 加载系统或注入系统
## Outputs

- AE 事件数、累积计数
- 能量率
- b 值
- 定位事件分布
- 破裂机制分类（拉伸/剪切）
## Assumptions

- 信号传播速度恒定（用于定位）
- AE 信号仅来源于试样或储层变形破裂
## Strengths

- 无损、实时、灵敏度高
- 揭示多阶段破裂过程
## Limitations

- 信号易受试验机噪音影响
- 严重损伤时高衰减影响捕捉
- 定位精度受传感器数量和速度模型影响
## Related Concepts

- acoustic-emission
- mesoscopic-damage
- induced-seismicity
## Source Papers

- [2017-kumari-mechanical-behaviour-of-australian-strathbogie-granite-under-in-situ-stress-and-temp](../papers/2017-kumari-mechanical-behaviour-of-australian-strathbogie-granite-under-in-situ-stress-and-temp.md)
- [2018-xu-acoustic-emission-and-damage-characteristics-of-granite-subjected-to-high-temperature](../papers/2018-xu-acoustic-emission-and-damage-characteristics-of-granite-subjected-to-high-temperature.md)
- [2023-cui-experimental-investigation-on-the-influence-on-mechanical-properties-and-acoustic-emiss](../papers/2023-cui-experimental-investigation-on-the-influence-on-mechanical-properties-and-acoustic-emiss.md)
- [2023-ge-thermal-damage-of-high-temperature-sandstone-subjected-to-cooling-shock-and-its-effect-o](../papers/2023-ge-thermal-damage-of-high-temperature-sandstone-subjected-to-cooling-shock-and-its-effect-o.md)
- [2025-zhu-physico-mechanical-properties-of-granite-after-thermal-treatments-using-different-cooli](../papers/2025-zhu-physico-mechanical-properties-of-granite-after-thermal-treatments-using-different-cooli.md)
