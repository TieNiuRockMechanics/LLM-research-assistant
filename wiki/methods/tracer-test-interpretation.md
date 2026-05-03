---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "示踪试验技术与解析 (Tracer Test Interpretation)"
aliases:
  - "tracer test"
  - "示踪测试"
  - "dipole tracer test"
  - "强制梯度示踪试验"
  - "conservative tracer analysis"
sources:
  - "2017-shook-use-of-tracers-and-temperature-to-estimate-fracture-surface-area-for-egs-reservoirs"
  - "2018-liao-a-dna-tracer-system-for-hydrological-environment-investigations"
  - "2025-zhang-in-situ-interference-and-tracer-tests-in-granite-rock-with-fractures-at-beishan-explo"
  - "2023-ren-a-comprehensive-review-of-tracer-tests-in-enhanced-geothermal-systems"
---

# 示踪试验技术与解析 (Tracer Test Interpretation)

## Purpose

通过注入保守或吸附型示踪剂，监测产出浓度突破曲线 (BTC)，反演储层扫掠体积、流动通道参数和传热表面积。
## Aliases

- tracer test
- 示踪测试
- dipole tracer test
- 强制梯度示踪试验
- conservative tracer analysis
## Workflow

注入示踪剂段塞（可脉冲注入于注水-抽水双井间），在产出口连续采样记录浓度变化；绘制归一化质量通量曲线；通过矩分析法（如平均停留时间）或解析反演（如一维移流-弥散模型、等效通道模型）提取达西速度、弥散度、等效通道长度、回收率等参数。
## Inputs

- 注入示踪剂浓度和质量
- 注/抽速率
- 采出流体浓度时间序列
## Outputs

- 质量回收率
- 平均停留时间
- 扫掠孔隙体积
- 传热表面积
- 达西速度 u，纵向弥散度 α_L
## Assumptions

- 示踪剂保守（无吸附/降解/化学反应）
- 稳流条件
- 忽略基质扩散（短时试验）
## Strengths

- 成本低，信息丰富
- 直接反映井间连通性和交换面积
## Limitations

- 解释结果非唯一
- 测试周期长
- 对于极低渗基质解析解假设可能失效
## Related Concepts

- equivalent-flow-channel-model
- dna-tracer
## Source Papers

- [2017-shook-use-of-tracers-and-temperature-to-estimate-fracture-surface-area-for-egs-reservoirs](../papers/2017-shook-use-of-tracers-and-temperature-to-estimate-fracture-surface-area-for-egs-reservoirs.md)
- [2018-liao-a-dna-tracer-system-for-hydrological-environment-investigations](../papers/2018-liao-a-dna-tracer-system-for-hydrological-environment-investigations.md)
- [2025-zhang-in-situ-interference-and-tracer-tests-in-granite-rock-with-fractures-at-beishan-explo](../papers/2025-zhang-in-situ-interference-and-tracer-tests-in-granite-rock-with-fractures-at-beishan-explo.md)
- [2023-ren-a-comprehensive-review-of-tracer-tests-in-enhanced-geothermal-systems](../papers/2023-ren-a-comprehensive-review-of-tracer-tests-in-enhanced-geothermal-systems.md)
