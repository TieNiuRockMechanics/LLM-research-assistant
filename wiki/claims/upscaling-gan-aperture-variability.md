---
type: "claim"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
claim: "Upscaling-GAN 可直接从灰度图像生成任意尺寸裂缝网络，保留裂缝开度空间变异性（CV≈0.32-0.37），优于常数开度假设。"
confidence: "medium"
claim_status: "provisional"
sources:
  -
    paper_id: "2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai"
    locator: "pp. 6-11"
---

# Claim: Upscaling-GAN 可直接从灰度图像生成任意尺寸裂缝网络，保留裂缝开度空间变异性（CV≈0.32-0.37），优于常数开度假设。

## Status

provisional

## Confidence

medium

## Evidence

生成图像开度 CV 为 0.32–0.37（原图 0.42），长度幂律 α≈3.45–3.57，强度 1.48–1.92 m⁻¹，与训练图一致。
## Condition

单张 500×500 图像训练，二维灰度图。
## Limitation

模型在其它裂缝模式上的泛化能力未知，三维未扩展。
## Supports

- not-confirmed-from-current-pages
## Contradicts

- not-confirmed-from-current-pages
## Source Papers

- [2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai](../papers/2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai.md) (pp. 6-11)
