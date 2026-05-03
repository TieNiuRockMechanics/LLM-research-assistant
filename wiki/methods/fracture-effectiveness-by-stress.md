---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "基于地应力方位的裂缝有效性评价"
aliases:
sources:
  - "2012-tong-kaijun-reservoir-evaluation-and-fracture-chracterization-of-the-metamorphic-buried-hil"
---

# 基于地应力方位的裂缝有效性评价

## Purpose

在缺少动态数据时，通过成像测井解释出的裂缝走向与现今最大水平主应力方向的夹角，半定量评价变质岩潜山裂缝的导流能力。
## Aliases

- not-confirmed-from-current-pages
## Workflow

从钻孔成像（如 FMI）拾取裂缝产状和走向；通过区域应力图、钻孔崩落或钻井诱导缝确定现今最大水平主应力方向；计算每条裂缝走向与主应力方向之间的锐角夹角；将裂缝划分为高度有效（<30°）、中等有效（30°–60°）和无效（>60°）等分类。
## Inputs

- 成像测井裂缝产状（走向）
- 现今最大水平主应力方向
## Outputs

- 有效的裂缝密度和定向分布
- 裂缝有效性分级（I 类、II 类、III 类）
## Assumptions

- 现今应力场与古应力场方向一致或控制了后期裂缝的重新激活状态
- 裂缝开启程度高则对应流体流动优势通道
## Strengths

- 方法直接，所需数据为常规测井和局部应力背景资料
- 可将静态裂缝参数转化为动态有效性评价
## Limitations

- 仅根据走向夹角判识，忽略了裂缝多期次和胶结充填的多重影响
- 成像测井无法测定裂纹的径向延伸，可能高估无充填裂缝的有效性
## Related Concepts

- buried-hill-reservoir
## Source Papers

- [2012-tong-kaijun-reservoir-evaluation-and-fracture-chracterization-of-the-metamorphic-buried-hil](../papers/2012-tong-kaijun-reservoir-evaluation-and-fracture-chracterization-of-the-metamorphic-buried-hil.md)
