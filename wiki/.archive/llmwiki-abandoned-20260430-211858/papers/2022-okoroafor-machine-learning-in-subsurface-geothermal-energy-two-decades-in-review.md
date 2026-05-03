---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2022-okoroafor-machine-learning-in-subsurface-geothermal-energy-two-decades-in-review"
title: "Machine Learning in Subsurface Geothermal Energy: Two Decades in Review."
status: "draft"
source_pdf: "data/papers/2022 - Machine learning in subsurface geothermal energy Two decades in review.pdf"
collections:
  - "zotero new"
citation: "Okoroafor, Esuru Rita, et al. \"Machine Learning in Subsurface Geothermal Energy: Two Decades in Review.\" *Geothermics*, vol. 102, 2022, 102401. doi:10.1016/j.geothermics.2022.102401. Accessed 2026."
indexed_texts: "21"
indexed_chars: "100409"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T11:04:18"
---

# Machine Learning in Subsurface Geothermal Energy: Two Decades in Review.

## One-line Summary
This paper reviews the trends, algorithms, and applications of machine learning (ML) in subsurface geothermal resource development over two decades (2002–2021), finding an exponential increase in usage since 2018, with reservoir characterization being the most active area [Okoroafor 2022, pp. 1-2].

## Research Question
The review investigates which ML algorithms are being used in subsurface geothermal development, what types of problems are being addressed, and how ML aids decision-making, while also identifying gaps and opportunities for expanded adoption [Okoroafor 2022, pp. 1-2].

## Study Area / Data
The study is a literature review. Data were gathered from the International Geothermal Association (IGA) database (21,388 articles) and Google Scholar (2,278 articles), then filtered programmatically using AI-related keywords. After manual curation to ensure articles involved the application of a machine learning algorithm to a subsurface geothermal problem, 98 peer-reviewed journal articles, World Geothermal Congress, Geothermal Rising, and Stanford Geothermal Workshop papers published between 2002 and 2021 were retained for detailed analysis [Okoroafor 2022, pp. 5-5, 5-8].

## Methods
A Python routine was developed to programmatically retrieve and filter articles from the IGA and Google Scholar databases using keywords: "artificial intelligence", "machine learning", "deep learning", "statistical learning", "supervised learning", "unsupervised learning", and "neural network." Google Scholar searches combined these keywords with "geothermal." The collected articles were then manually curated to ensure relevance. The retained 98 papers were categorized into specific research areas (exploration, drilling, reservoir characterization, seismicity, petrophysics, reservoir engineering, production/injection engineering) for statistical and detailed literature analysis [Okoroafor 2022, pp. 5-5, 5-8].

## Key Findings
- **Exponential Growth in ML Application**: The application of ML in the subsurface geothermal industry saw a steady increase over 20 years, with an exponential rise from 2018 to 2021. This growth may have been facilitated by the inception of frameworks like PyTorch, TensorFlow, and Keras in 2015 [Okoroafor 2022, pp. 1-2, 5-8].
- **Dominance of Reservoir Characterization**: The research area with the most significant application of ML was reservoir characterization [Okoroafor 2022, pp. 1-2].
- **DL Adoption Spikes Late**: Significant use of deep learning algorithms was limited until 2020 and 2021, with only one paper in 2010 and two in 2015 utilizing deep learning [Okoroafor 2022, pp. 5-8].
- **ML vs. DL Use Cases**: Traditional ML algorithms were primarily used in early, high-risk stages with often minimal data (e.g., exploration, early reservoir characterization, drilling). Deep learning algorithms were mainly applied in reservoir engineering and production/injection engineering, where more data are available or can be synthetically generated [Okoroafor 2022, pp. 8-9].
- **Drilling Optimization**: ML methods, including multiple linear regression and shallow neural networks, were used to predict rate of penetration (ROP) from surface controllable drilling parameters to address high drilling costs and risks [Okoroafor 2022, pp. 9-9].
- **Seismic Applications**: CNN models have been trained for the detection/location of microseismic events and for estimating acoustic emission and moment tensor solutions from large laboratory datasets [Okoroafor 2022, pp. 9-9].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 98 papers on ML in subsurface geothermal were identified and analyzed from an initial set of >23,000 articles. | [Okoroafor 2022, pp. 5-8] | Filtering with AI keywords and manual curation on IGA and Google Scholar databases up to Jan 4, 2022. | The final count excludes topics unrelated to subsurface development. |
| The application of ML algorithms became exponential from 2018 to 2021. | [Okoroafor 2022, pp. 1-2, 5-8] | Based on a statistical analysis of the 98 reviewed papers published from 2002 to 2021. | This coincides with the 2015 release of major DL frameworks. |
| Reservoir characterization is the field with the most significant ML applications in the geothermal industry. | [Okoroafor 2022, pp. 1-2] | Conclusion from the review of all 98 papers across identified research areas. | |
| Deep learning was predominantly used from 2020-2021, with very few prior applications. | [Okoroafor 2022, pp. 5-8] | Findings from the timeline analysis of the 98 papers. | Only 1 paper in 2010 and 2 in 2015 used DL. |
| Drilling had relatively fewer machine learning applications compared to other areas like exploration. | [Okoroafor 2022, pp. 8-9] | Observation from the distribution of papers across research areas. | Drilling contributes significantly to high geothermal development costs. |

## Limitations
- The authors acknowledge that the keyword-based search may not capture all relevant studies. Early ML applications might have been published under broader terms like "regression," "kriging," or "stochastic modeling" before modern ML terminology became popular in the last ~10–15 years [Okoroafor 2022, pp. 5-5].
- The review is limited to English-language articles from two specific databases (IGA and Google Scholar) and focuses exclusively on subsurface resource development, excluding topics like above-ground power plant operations [Okoroafor 2022, pp. 5-5, 5-8].
- 未从索引片段中确认是否对论文质量或结果稳健性进行了正式评估。

## Assumptions / Conditions
- Machine learning terminology (e.g., "deep learning," "neural network") is assumed to be a reliable filter for identifying relevant applications, with the awareness that this risks excluding older, rudimentary ML work published under different nomenclature [Okoroafor 2022, pp. 5-5].
- The study categorizes deep neural networks as any neural network with three or more hidden layers, distinguishing them from shallow neural networks (or multi-layer perceptrons with one or two hidden layers) [Okoroafor 2022, pp. 4-5].
- The data collection from Google Scholar assumes that combining AI keywords with the word "geothermal" effectively captures the target literature [Okoroafor 2022, pp. 5-5].

## Key Variables / Parameters
- **Number of publications** (journal vs. conference) over time [Okoroafor 2022, pp. 5-8].
- **Frequency of algorithm type usage** (traditional ML vs. deep learning) [Okoroafor 2022, pp. 5-8].
- **Rate of Penetration (ROP)** : A key drilling performance metric modeled using ML, typically ranging from 2 m/hr to 5 m/hr in hard geothermal rocks [Okoroafor 2022, pp. 9-9].
- **Controllable drilling parameters**: Weight on bit (WOB), bit types, bit speed, and fluid rheological properties, used as inputs for ROP prediction models [Okoroafor 2022, pp. 9-9].
- **Machine learning technique categories**: Traditional ML (regression, classification, clustering), dimensionality reduction (PCA, ICA, t-SNE), shallow neural networks (MLP), and deep learning (CNN, RNN, LSTM, GAN) [Okoroafor 2022, pp. 4-5].

## Reusable Claims
1.  **Claim**: Reviews on ML applications to geothermal subsurface problems are feasible by programmatically filtering large academic databases with a curated set of AI-specific keywords and then manually validating the results for domain relevance. This methodology can be replicated for other niche energy fields. [Okoroafor 2022, pp. 5-5]
    - *Conditions*: Requires access to databases like IGA and Google Scholar, and a set of domain-specific keywords. Acknowledges potential keyword bias by missing older studies using non-standard ML terminology.
2.  **Claim**: The adoption of deep learning in a specialized geoscience field (subsurface geothermal) lags significantly behind the broader AI boom, with a clear inflection point for publications occurring in 2020-2021, potentially driven by the accessibility of frameworks like TensorFlow and PyTorch released around 2015. [Okoroafor 2022, pp. 5-8]
    - *Conditions*: Based on a corpus of 98 papers up to early 2022. The conclusion about framework influence is suggested but not causally proven.
3.  **Claim**: Deep learning applications in subsurface geothermal are concentrated in data-rich downstream areas (reservoir and production engineering), while traditional machine learning dominates early-stage, high-risk, and data-scarce areas (exploration, drilling). This indicates a strong correlation between data availability and the complexity of ML techniques applicable to a problem. [Okoroafor 2022, pp. 8-9]
    - *Conditions*: Derived from the categorical analysis of 98 papers. It establishes a pattern, not a direct causal link from every paper.
4.  **Claim**: The probability of a greenfield geothermal prospect reaching commercial production is historically low, around 16%, which provides a strong economic motivation for applying data-driven ML techniques to pre-drilling exploration for better site selection and risk reduction. [Okoroafor 2022, pp. 8-9]
    - *Conditions*: Statistic cited from Wall and Dobson, 2016, within the context of motivating ML for exploration. The 16% figure acts as a baseline against which the value of ML can be argued.

## Candidate Concepts
- [[geothermal exploration]]
- [[drilling optimization]]
- [[reservoir characterization]]
- [[seismicity prediction]]
- [[rate of penetration (ROP)]]
- [[geophysical inversion]]
- [[enhanced geothermal systems (EGS)]]

## Candidate Methods
- [[Convolutional Neural Network (CNN)]]
- [[Support Vector Machine (SVM)]]
- [[Principal Component Analysis (PCA)]]
- [[logistic regression]]
- [[kriging]]
- [[shallow neural network / multi-layer perceptron]]
- [[Random Forest]]

## Connections To Other Work
- The review builds upon the concept of technology improvement driving geothermal capacity, citing forecasts like the GeoVision study suggesting U.S. capacity could reach 60 GWe with accelerated development and tech improvements, creating the context for why AI/ML adoption is critical [Okoroafor 2022, pp. 2-3].
- In exploration, the paper connects recent ML applications to a history of data-driven modeling with GIS and statistical methods like weights-of-evidence and logistic regression [Okoroafor 2022, pp. 8-9].
- The rise of ML conferences and preprints (as noted by Zhang et al., 2021a) is contextually linked to the overall AI boom, contrasting with the energy sector's lagging investment [Okoroafor 2022, pp. 3-4].
- 未从索引片段中确认与其他具体综述或AI在能源领域应用论文的直接比较性结论。

## Open Questions
- How can data availability and curation challenges be systematically addressed for exploration, drilling, and seismicity to enable broader and more complex ML adoption? [Okoroafor 2022, pp. 1-2]
- What are the specific barriers to applying deep learning techniques in data-scarce geothermal contexts compared to traditional ML? [Okoroafor 2022, pp. 8-9]
- To what extent did the introduction of TensorFlow, PyTorch, and Keras in 2015 causally accelerate ML adoption in the geothermal industry, or was it a coincidental correlation? [Okoroafor 2022, pp. 5-8]

## Source Coverage
This page is based on 12 indexing fragments covering the abstract, introduction, methods, and results sections of the paper. The fragments provide good coverage of the study's methodology, statistical findings, and high-level topic distributions (exploration, drilling, seismicity). However, detailed findings from the in-depth literature review for each research area (e.g., petrophysics, reservoir engineering, production) beyond the summary statements are likely missing. Information on specific model performances (e.g., accuracy scores), dataset details for the reviewed papers, and the full scope of the "gaps and opportunities" discussion is not present in the provided fragments.
