---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "从钻孔数据推断裂隙尺寸分布"
aliases:
  - "fracture size from boreholes"
  - "Zhang et al. stereological method"
  - "椭圆节理体视学法"
sources:
  - "2016-gao-fracture-size-estimation-using-data-from-multiple-boreholes"
  - "2010-zhang-the-planar-shape-of-rock-joints"
  - "2014-jin-analytical-expressions-for-the-size-distribution-function-of-elliptical-joints"
---

# 从钻孔数据推断裂隙尺寸分布

## Purpose

基于椭圆面裂隙假设，通过统计多个平行钻孔壁上的正弦迹线或部分迹线的计数信息，反推裂隙长轴的平均尺寸或尺寸的概率密度分布。
## Aliases

- fracture size from boreholes
- Zhang et al. stereological method
- 椭圆节理体视学法
## Workflow

方法一（多孔交切法）：将椭圆裂隙沿钻孔方向投影到垂直于钻孔的平面上，建立投影尺寸期望与被交切钻数量之间的解析关系；通过单孔内全交切与部分交切的差值估算均值 μ_a 和标准差 σ_a；再利用多孔中交切不同数量钻孔的裂隙数来反推最优的假设分布（如分形、指数或对数正态分布）。方法二（椭圆节理体视学）：从岩体多个非平行采样窗收集迹长数据；应用 Priest-Hudson 或 Song-Lee 方法校正采样偏差得到真实迹长分布；假设节理为椭圆、具有恒定长宽比 k 和指定旋转角 φ；通过体视学关系式计算出对应迹长的理论期望值，追溯使不同采样窗数据能自洽得出相同长轴分布 g(a) 的 k 和 φ。
## Inputs

- 每个钻孔段内全交切和部分交切的裂隙数量统计
- 钻孔孔径、深度、平行布置间距
- 已知或假设的裂隙纵横比 κ 和旋转角 γ
- 多个不平行采样窗的校正后迹长分布
## Outputs

- 裂隙长轴均值 μ_a 及标准差 σ_a
- 尺寸分布类型倾向（分形、指数、对数正态）
- 长宽比 k 和旋转角 φ 的估算值
## Assumptions

- 裂隙为无厚度的椭圆平面
- 同组裂隙的纵横比相同且恒定
- 裂隙中心服从泊松过程（空间均匀）
## Strengths

- 解决了孔径远小于裂隙尺寸时的尺寸反演难题
- 突破了“等维圆盘”假设的局限性
## Limitations

- 多孔法在裂隙密度 P30 < 0.01 时不成立
- 只能拟合成分数、指数或对数正态三类
- 要求节理组内产状严格平行，与天然产状离散度不符
## Related Concepts

- fracture-size-distribution
## Source Papers

- [2016-gao-fracture-size-estimation-using-data-from-multiple-boreholes](../papers/2016-gao-fracture-size-estimation-using-data-from-multiple-boreholes.md)
- [2010-zhang-the-planar-shape-of-rock-joints](../papers/2010-zhang-the-planar-shape-of-rock-joints.md)
- [2014-jin-analytical-expressions-for-the-size-distribution-function-of-elliptical-joints](../papers/2014-jin-analytical-expressions-for-the-size-distribution-function-of-elliptical-joints.md)
