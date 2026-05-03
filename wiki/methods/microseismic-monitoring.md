---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "微震监测与分析 (Induced Seismicity Monitoring for EGS)"
aliases:
  - "seismicity monitoring"
  - "induced seismicity monitoring"
sources:
  - "2014-zang-analysis-of-induced-seismicity-in-geothermal-reservoirs-an-overview"
  - "2010-genter-contribution-of-the-exploration-of-deep-crystalline-fractured-reservoir-of-soultz-to"
---

# 微震监测与分析 (Induced Seismicity Monitoring for EGS)

## Purpose

通过布设地面和/或井下的地震检波器网络，实时监测并事后处理 EGS 水力增产和长期注采循环过程中引发的微震事件，评估储层改造体积和发震风险。
## Aliases

- seismicity monitoring
- induced seismicity monitoring
## Workflow

布设高灵敏度井下三分量地震台网；记录连续波形，利用长短时窗比或相关算法进行事件扫描；拾取 P/S 波震相，用 1D/3D 速度模型定位事件；分析时空分布、震级-频率分布（b 值）、矩张量反演获取破裂机制；评估动态和静态发震概率。
## Inputs

- 井下和/或地面高灵敏度三分量地震记录
- 高精度速度结构
## Outputs

- 微震事件目录（时间、位置、震级）
- 地震矩张量和破裂机制
- Gutenberg-Richter b 值
- 储层改造体积 SRV
## Assumptions

- 诱发事件的时空分布反映流体压力和应力扰动的波及范围
- 震级-频率关系满足 Gutenberg-Richter 统计
## Strengths

- 是监测地下无法直接观测的储层增产动态的唯一有效技术
- 提供 4D 应力-破裂信息
## Limitations

- 定位精度和检测灵敏度取决于台网几何
- 最大震级常在停注后发生，实时预警有滞后
- 无法从短时观测中约束‘最大可能震级’
## Related Concepts

- induced-seismicity
- enhanced-geothermal-system
## Source Papers

- [2014-zang-analysis-of-induced-seismicity-in-geothermal-reservoirs-an-overview](../papers/2014-zang-analysis-of-induced-seismicity-in-geothermal-reservoirs-an-overview.md)
- [2010-genter-contribution-of-the-exploration-of-deep-crystalline-fractured-reservoir-of-soultz-to](../papers/2010-genter-contribution-of-the-exploration-of-deep-crystalline-fractured-reservoir-of-soultz-to.md)
