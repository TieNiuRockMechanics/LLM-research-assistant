---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "全球渗透率预测回归模型"
aliases:
  - "global permeability regression model for crystalline rocks"
sources:
  - "2017-achtziger-zupan-a-new-global-database-to-improve-predictions-of-permeability-distribution-i"
---

# 全球渗透率预测回归模型

## Purpose

基于全球约 29,000 个现场渗透率数据建立的回归模型，可依据深度、地质构造省和地震构造活动性（PGA）来预测场地尺度下结晶岩渗透率随深度的变化趋势。
## Aliases

- global permeability regression model for crystalline rocks
## Workflow

确定目标场地位于何种地质构造省和 PGA 等级（高、中、低、极低）；根据表格或回归公式选取相应的斜率 A 和截距 B；用公式 log(k)=A×log(z)+B 计算特定深度 z 的预测渗透率 (m²)。
## Inputs

- 目标位置的深度 (km)
- 该地的地质构造省分类
- 该地的峰值地面加速度 (PGA) 等级
## Outputs

- 在特定深度和不确定性范围内预测的结晶岩渗透率 (log(m²))
## Assumptions

- 深度是渗透率对数的主要趋势控制变量
- 同等地质省和地震活动水平地区，渗透率随深度减小的规律是可迁移的
- 测量尺度、方法、方向性等带来的偏差已通过归一化忽略
## Strengths

- 仅需极少的地质和地球物理背景知识，适用于预可行性研究阶段
## Limitations

- 预测结果不确定性很大（RMSE 约 1-2 个数量级），不能代替场地专项调查
- 数据偏向欧美和浅层，对亚洲和深度 >1000 m 的环境预测偏差可能较大
- 未考虑 THMC 耦合作用导致的动态渗透率演化
## Related Concepts

- permeability-upscaling
## Source Papers

- [2017-achtziger-zupan-a-new-global-database-to-improve-predictions-of-permeability-distribution-i](../papers/2017-achtziger-zupan-a-new-global-database-to-improve-predictions-of-permeability-distribution-i.md)
