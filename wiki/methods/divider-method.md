---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "分规法 (Divider Method)"
aliases:
  - "compass-walking method"
sources:
  - "2011-bae-characterization-of-joint-roughness-in-granite-by-applying-the-scan-circle-technique-to"
  - "2015-li-relationship-between-joint-roughness-coefficient-and-fractal-dimension-of-rock-fracture"
---

# 分规法 (Divider Method)

## Purpose

通过不同跨距的分规测量节理剖面长度，估算分形维数。
## Aliases

- compass-walking method
## Workflow

设定一系列分规跨距 r，用每个 r 沿着剖面线分步测量，记录总步数 N(r) 和残余长度 f(r)；在对数坐标中绘制 log(N+f/r) vs. log(r)，斜率即为负分形维数。
## Inputs

- 节理剖面的二维数字化坐标
## Outputs

- 分形维数 D_compass
## Assumptions

- 节理剖面符合自仿射分形模型
## Strengths

- 比盒计数法对走向和填充更敏感
- 与 JRC 相关性高
## Limitations

- 分规尺级数选择影响结果
- 非自仿射特征可能无稳定解
## Related Concepts

- fractal-dimension
- joint-roughness-coefficient
## Source Papers

- [2011-bae-characterization-of-joint-roughness-in-granite-by-applying-the-scan-circle-technique-to](../papers/2011-bae-characterization-of-joint-roughness-in-granite-by-applying-the-scan-circle-technique-to.md)
- [2015-li-relationship-between-joint-roughness-coefficient-and-fractal-dimension-of-rock-fracture](../papers/2015-li-relationship-between-joint-roughness-coefficient-and-fractal-dimension-of-rock-fracture.md)
