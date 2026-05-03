---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "巴西劈裂试验 (Brazilian Test)"
aliases:
  - "Brazilian disc test"
  - "splitting tensile test"
  - "indirect tensile test"
  - "巴西圆盘法"
sources:
  - "2019-wu-on-the-tensile-mechanical-characteristics-of-fine-grained-granite-after-heating-cooling"
  - "2020-sha-experimental-evaluation-of-physical-and-mechanical-properties-of-geothermal-reservoir-r"
  - "2017-l-the-effect-of-high-temperature-on-tensile-strength-of-sandstone"
---

# 巴西劈裂试验 (Brazilian Test)

## Purpose

间接测定岩石抗拉强度。
## Aliases

- Brazilian disc test
- splitting tensile test
- indirect tensile test
- 巴西圆盘法
## Workflow

将圆盘试样径向对径压缩，记录最大载荷，按公式 σt = 2P/(πDt) 计算抗拉强度。
## Inputs

- 圆盘试件直径 D、厚度 t
- 最大载荷 P
## Outputs

- 抗拉强度 σt
## Assumptions

- 中心裂纹起裂
- 线弹性荷载
- 端部摩擦忽略
## Strengths

- 操作简单
- 试件制备容易
## Limitations

- 间接测量，应力状态非纯拉
- 可能出现无效破坏
## Related Concepts

- tensile-strength
- brittle-failure
## Source Papers

- [2019-wu-on-the-tensile-mechanical-characteristics-of-fine-grained-granite-after-heating-cooling](../papers/2019-wu-on-the-tensile-mechanical-characteristics-of-fine-grained-granite-after-heating-cooling.md)
- [2020-sha-experimental-evaluation-of-physical-and-mechanical-properties-of-geothermal-reservoir-r](../papers/2020-sha-experimental-evaluation-of-physical-and-mechanical-properties-of-geothermal-reservoir-r.md)
- [2017-l-the-effect-of-high-temperature-on-tensile-strength-of-sandstone](../papers/2017-l-the-effect-of-high-temperature-on-tensile-strength-of-sandstone.md)
