---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "Slug 干扰试验与水文连通性分析"
aliases:
  - "slug interference test"
  - "HCC matrix"
sources:
  - "2025-zhang-in-situ-interference-and-tracer-tests-in-granite-rock-with-fractures-at-beishan-explo"
---

# Slug 干扰试验与水文连通性分析

## Purpose

通过多孔瞬时抽水-观测试验，利用 KGS 模型反演水力传导系数，并构建 HCC 矩阵量化井间连通性。
## Aliases

- slug interference test
- HCC matrix
## Workflow

在源孔快速抽水，在观测孔监测压力变化；用 KGS 模型拟合求取水力传导系数 K；计算最大水位降深比 HCC，构建非对称连接矩阵，分析连通方向性。
## Inputs

- 抽水量或抽水速率
- 孔压/水位观测序列
- 井结构参数
## Outputs

- 水力传导系数 K
- HCC 矩阵
- 连通方向性
## Assumptions

- 无压含水层
- 侧向无限延伸
- 部分贯穿井
## Strengths

- 可揭示非均质各向异性连通性
## Limitations

- 未分段封隔，可能混合响应
- 需要多个观测孔
## Related Concepts

- hydraulic-connectivity-coefficient
## Source Papers

- [2025-zhang-in-situ-interference-and-tracer-tests-in-granite-rock-with-fractures-at-beishan-explo](../papers/2025-zhang-in-situ-interference-and-tracer-tests-in-granite-rock-with-fractures-at-beishan-explo.md)
