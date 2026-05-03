---
type: "claim"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
claim: "与等效泊松（随机）DFN 相比，采用运动学生长模型（KFM）生成的 DFN 具有更高的逾渗阈值（约高 50%）和更低的整体等效渗透率（约低 1.5–10 倍），且流动的通道化现象更显著。"
confidence: "high"
claim_status: "supported"
sources:
  -
    paper_id: "2016-maillot-connectivity-permeability-and-channeling-in-randomly-distributed-and-kinematically"
    locator: "pp. 9-11, 17-18"
---

# Claim: 与等效泊松（随机）DFN 相比，采用运动学生长模型（KFM）生成的 DFN 具有更高的逾渗阈值（约高 50%）和更低的整体等效渗透率（约低 1.5–10 倍），且流动的通道化现象更显著。

## Status

supported

## Confidence

high

## Evidence

上千次蒙特卡洛实现对比 KFM 和等效泊松模型的 3D DFN 模拟，发现其渗透率更低；逾渗阈值在 KFM 中更高。
## Condition

适用于三维各向同性裂隙网络，长度分布幂律指数 a=4；差异在低密度和活动构造区更明显。
## Limitation

结论基于特定 KFM 生成器和中等密度网络回归外推；泊松模型简化可能高估连通性。
## Supports

- not-confirmed-from-current-pages
## Contradicts

- not-confirmed-from-current-pages
## Source Papers

- [2016-maillot-connectivity-permeability-and-channeling-in-randomly-distributed-and-kinematically](../papers/2016-maillot-connectivity-permeability-and-channeling-in-randomly-distributed-and-kinematically.md) (pp. 9-11, 17-18)
