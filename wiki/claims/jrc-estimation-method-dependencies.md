---
type: "claim"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
claim: "JRC 估算依赖所用的粗糙度参数和计算方法：Z₂ 与 JRC 的幂律关系在采样间隔为 0.5 mm 时 R²=0.972，但对采样间隔极度敏感；分形维数 D 与 JRC 的相关性因分形算法不同而差异巨大（分规法优于盒计数法）；视觉对比法系统性低估 JRC 约 2.9 个单位；许多经验公式未强制施加光滑节理 JRC=0 的边界条件。"
confidence: "high"
claim_status: "supported"
sources:
  -
    paper_id: "2014-jang-determination-of-joint-roughness-coefficients-using-roughness-parameters"
    locator: "pp. 3-5, 10-12"
  -
    paper_id: "2015-li-relationship-between-joint-roughness-coefficient-and-fractal-dimension-of-rock-fracture"
    locator: "pp. 6-8"
  -
    paper_id: "2017-li-uncertainties-in-estimating-the-roughness-coefficient-of-rock-fracture-surfaces"
    locator: "pp. 8-10"
---

# Claim: JRC 估算依赖所用的粗糙度参数和计算方法：Z₂ 与 JRC 的幂律关系在采样间隔为 0.5 mm 时 R²=0.972，但对采样间隔极度敏感；分形维数 D 与 JRC 的相关性因分形算法不同而差异巨大（分规法优于盒计数法）；视觉对比法系统性低估 JRC 约 2.9 个单位；许多经验公式未强制施加光滑节理 JRC=0 的边界条件。

## Status

supported

## Confidence

high

## Evidence

Batch 2 研究表明 JRC-Z₂ 关系对采样间隔敏感，误差可达数个单位；Batch 3 统计 223 条剖面显示视觉对比平均偏差 -2.9；Batch 2 和 3 指出分形维数计算方法影响与 JRC 相关性；Batch 2 揭示第 4 条 Barton 标准剖面偏差持续 >±5%；Batch 2 指出许多公式在 D=1 时预测非零 JRC。
## Condition

适用于与 Barton 标准剖面统计特征相似的岩石节理；应用经验公式时必须匹配原始采样间隔（如 0.5 mm）和分形计算方法。
## Limitation

不同经验关系不可混用；视觉对比偏差依赖于操作者经验；第 4 条剖面异常原因尚不明确；光滑节理边界条件常被忽视。
## Supports

- not-confirmed-from-current-pages
## Contradicts

- not-confirmed-from-current-pages
## Source Papers

- [2014-jang-determination-of-joint-roughness-coefficients-using-roughness-parameters](../papers/2014-jang-determination-of-joint-roughness-coefficients-using-roughness-parameters.md) (pp. 3-5, 10-12)
- [2015-li-relationship-between-joint-roughness-coefficient-and-fractal-dimension-of-rock-fracture](../papers/2015-li-relationship-between-joint-roughness-coefficient-and-fractal-dimension-of-rock-fracture.md) (pp. 6-8)
- [2017-li-uncertainties-in-estimating-the-roughness-coefficient-of-rock-fracture-surfaces](../papers/2017-li-uncertainties-in-estimating-the-roughness-coefficient-of-rock-fracture-surfaces.md) (pp. 8-10)
