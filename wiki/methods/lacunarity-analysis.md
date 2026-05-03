---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "缺项性分析 (Lacunarity Analysis)"
aliases:
sources:
  - "2010-roy-lacunarity-analysis-of-fracture-networks-evidence-for-scale-dependent-clustering"
---

# 缺项性分析 (Lacunarity Analysis)

## Purpose

量化裂隙网络在不同观测尺度下的空间聚集（间隙分布）程度，弥补分形维数无法区分相同维数但不同空间结构的模式的缺陷。
## Aliases

- not-confirmed-from-current-pages
## Workflow

将裂隙图转为二值像素图；以步长滑动边长为 r 的方形窗，统计窗内目标像素数 s(r)；计算均值 Z1 和方差 Z2，得到缺项性 L(r)=Z2/Z1²+1；计算标准化缺项性 L*(r)=(L(r)-1)/(1/f-1)，绘制 L*(r)-r 曲线。
## Inputs

- 裂隙网络二值图像
## Outputs

- 标准化缺项性曲线 L*(r)
## Assumptions

- 裂隙网络可用二维像素图近似
- Lmin（全图窗口）=1，Lmax（单像素窗口）=1/f
## Strengths

- 消除裂隙丰度（密度）对聚类结果的影响
- 捕捉尺度依赖的聚类变化
## Limitations

- 仅适用于二维表征
- 大盒尺寸下区分能力下降
## Related Concepts

- lacunarity
- fractal-dimension
## Source Papers

- [2010-roy-lacunarity-analysis-of-fracture-networks-evidence-for-scale-dependent-clustering](../papers/2010-roy-lacunarity-analysis-of-fracture-networks-evidence-for-scale-dependent-clustering.md)
