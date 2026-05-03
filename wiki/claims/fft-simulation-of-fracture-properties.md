---
type: "claim"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
claim: "裂隙组几何属性（产状、间距、迹长）普遍存在空间自相关，可用变异函数量化并通过 FFT 谱模拟高效生成。"
confidence: "medium"
claim_status: "supported"
sources:
  -
    paper_id: "1985-miller-spectral-type-simulation-of-spatially-correlated-fracture-set-properties"
    locator: "pp. 1-5, 10-11"
---

# Claim: 裂隙组几何属性（产状、间距、迹长）普遍存在空间自相关，可用变异函数量化并通过 FFT 谱模拟高效生成。

## Status

supported

## Confidence

medium

## Evidence

利用 FFT 实现的谱模拟成功复现了正态和指数分布属性的实测变异函数，计算效率极高。
## Condition

协方差平稳过程，属性独立。
## Limitation

未考虑不同属性间的互相关；隐含周期性假设可能不适用于某些边界。
## Supports

- not-confirmed-from-current-pages
## Contradicts

- not-confirmed-from-current-pages
## Source Papers

- [1985-miller-spectral-type-simulation-of-spatially-correlated-fracture-set-properties](../papers/1985-miller-spectral-type-simulation-of-spatially-correlated-fracture-set-properties.md) (pp. 1-5, 10-11)
