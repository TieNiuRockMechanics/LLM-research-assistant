---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "超声波波速测量 (Ultrasonic Pulse Velocity)"
aliases:
  - "P-wave velocity"
  - "ultrasonic pulse velocity"
  - "UPV"
sources:
  - "2019-wu-on-the-tensile-mechanical-characteristics-of-fine-grained-granite-after-heating-cooling"
  - "2021-li-thermal-damage-effect-on-the-thermal-conductivity-inhomogeneity-of-granite"
  - "2017-l-the-effect-of-high-temperature-on-tensile-strength-of-sandstone"
---

# 超声波波速测量 (Ultrasonic Pulse Velocity)

## Purpose

通过测量纵波（可扩展至横波）在岩石中的传播速度，评估岩石完整性、孔隙/裂隙发育程度和热损伤。
## Aliases

- P-wave velocity
- ultrasonic pulse velocity
- UPV
## Workflow

使用已知频率的探头与耦合剂，测量脉冲穿过试样的走时，计算波速；常基于波速下降定义损伤因子 D=1-(Vp/Vp0)²。
## Inputs

- 试样长度
- 走时 t
- 探头频率
## Outputs

- P 波速度 Vp
- 损伤因子 D
## Assumptions

- 材料均质弹性
- 波沿直线传播
## Strengths

- 无损、快速、可重复
## Limitations

- 仅反映平均特性，不区分裂纹方向
## Related Concepts

- thermal-damage
- microcrack-density
- elastic-modulus
## Source Papers

- [2019-wu-on-the-tensile-mechanical-characteristics-of-fine-grained-granite-after-heating-cooling](../papers/2019-wu-on-the-tensile-mechanical-characteristics-of-fine-grained-granite-after-heating-cooling.md)
- [2021-li-thermal-damage-effect-on-the-thermal-conductivity-inhomogeneity-of-granite](../papers/2021-li-thermal-damage-effect-on-the-thermal-conductivity-inhomogeneity-of-granite.md)
- [2017-l-the-effect-of-high-temperature-on-tensile-strength-of-sandstone](../papers/2017-l-the-effect-of-high-temperature-on-tensile-strength-of-sandstone.md)
