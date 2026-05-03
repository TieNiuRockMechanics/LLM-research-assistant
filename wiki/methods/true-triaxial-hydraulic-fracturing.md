---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "真三轴水力压裂试验"
aliases:
  - "true triaxial fracturing test"
  - "3D stress fracturing"
sources:
  - "2020-zhou-investigation-on-fracture-creation-in-hot-dry-rock-geothermal-formations-of-china-duri"
---

# 真三轴水力压裂试验

## Purpose

在独立三向应力下进行水力压裂，研究地应力差、天然裂缝和泵注参数对裂缝起裂与扩展的影响。
## Aliases

- true triaxial fracturing test
- 3D stress fracturing
## Workflow

立方体试样中心钻孔，施加三向独立应力（σH, σh, σv），注入压裂液，记录压力-时间曲线，试验后剖分观察裂缝几何。
## Inputs

- 地应力 σH, σh, σv
- 注入排量
- 压裂液粘度
## Outputs

- 起裂压力
- 裂缝形态
- 扩展轨迹
## Assumptions

- 试样均质
- 钻孔缩尺相似准则成立
## Strengths

- 再现真实应力差下的裂缝行为
## Limitations

- 试样尺寸有限
- 无法完全复制井筒大规模流动
## Related Concepts

- hydraulic-fracturing
- in-situ-stress
- fracture-initiation
## Source Papers

- [2020-zhou-investigation-on-fracture-creation-in-hot-dry-rock-geothermal-formations-of-china-duri](../papers/2020-zhou-investigation-on-fracture-creation-in-hot-dry-rock-geothermal-formations-of-china-duri.md)
