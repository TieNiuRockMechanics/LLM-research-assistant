---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-okoroafor-machine-learning-in-subsurface-geothermal-energy-two-decades-in-review"
title: "Machine Learning in Subsurface Geothermal Energy: Two Decades in Review."
status: "draft"
source_pdf: "data/papers/2022 - Machine learning in subsurface geothermal energy Two decades in review.pdf"
collections:
  - "zotero new"
citation: "Okoroafor, Esuru Rita, et al. \"Machine Learning in Subsurface Geothermal Energy: Two Decades in Review.\" *Geothermics*, vol. 102, 2022, 102401. doi:10.1016/j.geothermics.2022.102401. Accessed 2026."
indexed_texts: "21"
indexed_chars: "100409"
nonempty_source_blocks: "21"
compiled_source_blocks: "21"
compiled_source_chars: "95803"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.954128"
coverage_status: "full-index"
source_signature: "1e73c94d18e90ee93e41517fe7f412be0d0687fa"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T05:47:07"
---

# Machine Learning in Subsurface Geothermal Energy: Two Decades in Review.

## One-line Summary
This 20-year review (2002‑2021) of 98 subsurface geothermal papers shows exponential growth in machine‑learning adoption after 2018, with reservoir characterization as the leading application area and a clear shift toward deep‑learning methods in reservoir engineering and seismicity after 2020.

## Research Question
The study investigates: (1) which machine learning algorithms are being used in subsurface geothermal resource development, (2) what types of subsurface problems are being addressed with machine learning, and (3) how machine learning is aiding decision‑making and problem‑solving in the geothermal industry. [Okoroafor 2022, pp. 1-2]

## Study Area / Data
The data corpus was built from two sources:
1. The International Geothermal Association (IGA) database accessed through the Stanford University geothermal search engine (21,388 articles as of 4 January 2022).  
2. The Google Scholar search engine and database, queried with the same AI‑related keywords plus the word “geothermal” (2,278 articles).  

Articles were programmatically filtered using Python based on the presence of keywords: “artificial intelligence”, “machine learning”, “deep learning”, “statistical learning”, “supervised learning”, “unsupervised learning”, and “neural network”. After manual curation to ensure actual application of a machine learning algorithm to a subsurface geothermal problem, 98 papers were retained for analysis. The review covers global geothermal developments, with examples from the USA, Turkey, Iceland, Japan, Mexico, the Philippines, and other countries. [Okoroafor 2022, pp. 5]

## Methods
Data were collected programmatically and then manually filtered. Research areas were categorized into seven subsurface domains: exploration, seismicity, drilling, petrophysics, reservoir characterization, reservoir engineering, and production/injection engineering. Within each domain, subcategories were defined (e.g., for reservoir characterization: seismic interpretation, fracture characterization, geochemistry, tracer testing, reservoir‑temperature estimation). A statistical analysis of publication counts and algorithm usage over time was performed. Machine learning techniques were separated into two broad groups: traditional machine learning (dimensionality reduction, clustering, classification, regression, shallow neural networks) and deep learning (deep neural networks, convolutional neural networks, recurrent neural networks, generative models). The review also mapped each paper to the specific problem addressed and the algorithm(s) used. [Okoroafor 2022, pp. 5-8]

## Key Findings
1. **Exponential growth after 2018.** The number of ML publications for subsurface geothermal applications increased exponentially from 2018, with the ratio of ML papers to total IGA papers rising to 3% in 2019 and beyond 12% in 2021. [Okoroafor 2022, pp. 6-8]  
2. **Deep learning gained visibility after 2020.** Traditional machine learning and deep learning were both used sparingly until 2018; deep‑learning applications became more prominent in 2020 and 2021, especially deep neural networks and convolutional neural networks. [Okoroafor 2022, pp. 6-7]  
3. **Reservoir characterization is the dominant application area.** Reservoir characterization had the most publications, followed by reservoir engineering and exploration. Drilling had relatively few ML applications despite its high cost. [Okoroafor 2022, pp. 8]  
4. **Traditional ML dominates early‑stage areas; deep learning dominates later‑stage areas.** Traditional algorithms (especially shallow neural networks) were primarily used in exploration, reservoir characterization, petrophysics, and drilling—areas with high risk, high cost, and sometimes minimal data. Deep learning algorithms were mainly applied in reservoir engineering and production/injection engineering, where more data are available or can be synthetically generated. [Okoroafor 2022, pp. 8]  
5. **Shallow neural networks are the most common technique.** Across all research areas, neural networks (both shallow and deep) are the most frequently applied machine learning method. [Okoroafor 2022, pp. 13-14]  
6. **Challenges remain.** The adoption of ML is limited by data accessibility and curation, the need for large, well‑structured datasets, and a shortage of geothermal professionals trained in artificial intelligence. [Okoroafor 2022, pp. 13]  

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 98 papers were retained for subsurface ML review out of 21,388 IGA articles and 2,278 Google Scholar hits. | [Okoroafor 2022, pp. 5-6] | Manual filtering based on actual ML application to a subsurface problem. | The total number of papers reviewed is explicitly 98. |
| Reservoir characterization has the largest share of ML publications among the seven research areas. | [Okoroafor 2022, pp. 8] | Derived from the distribution of the 98 reviewed papers. | Subcategories with most publications: geochemistry and reservoir‑temperature estimation. |
| Deep learning first appeared in geothermal literature in 2010, but only became frequent in 2020‑2021. | [Okoroafor 2022, pp. 6-7] | Based on the corpus of 98 papers. | The first documented deep‑learning application was in reservoir characterization. |
| Shallow neural networks (SNN) and multi‑layer perceptrons are the most widely used algorithms across all areas. | [Okoroafor 2022, pp. 13-14] | Summary table lists SNN in exploration, drilling, petrophysics, reservoir characterization, reservoir engineering, and production/injection. | Deep learning methods are concentrated in reservoir engineering and seismicity. |
| The ratio of ML papers to total IGA papers jumped from near zero to >12% in 2021. | [Okoroafor 2022, pp. 6-7] | The spike in 2021 coincides with the lowest total number of IGA papers in the observed period. | Quinquennial World Geothermal Congresses cause periodic spikes. |
| Transfer learning from oil‑and‑gas ML models is identified as a low‑hanging opportunity. | [Okoroafor 2022, pp. 14] | Domain similarities are noted (seismic interpretation, fault detection, drill‑string vibration, well‑log interpretation). | No concrete case studies of transfer learning in geothermal are provided; the claim is prospective. |

## Limitations
- The keyword‑based search may have missed earlier studies that performed rudimentary machine learning under older terminology such as “regression”, “kriging”, “Monte‑Carlo”, or “PCA”, without explicitly using modern AI‑related keywords. [Okoroafor 2022, pp. 5]  
- Only journal articles retrieved via Google Scholar were kept, but conference papers from IGA‑affiliated venues (World Geothermal Congress, Geothermal Rising, Stanford Workshop) were included. Non‑peer‑reviewed papers from other sources were excluded. [Okoroafor 2022, pp. 5]  
- The analysis relies on the manual categorization of research areas and subcategories; a different categorization could shift the distribution of papers. [Okoroafor 2022, pp. 5-6]  
- The review does not assess the technical quality or reproducibility of the reported machine learning models; it only documents trends and algorithm usage.  
- Data access limitations may bias the results toward publicly available, English‑language research.  

## Assumptions / Conditions
- Machine learning is defined as a branch of artificial intelligence that uses statistical methods to train computational models from data, with deep learning considered a subset involving neural networks with three or more hidden layers. [Okoroafor 2022, pp. 3-5]  
- The seven research areas (exploration, seismicity, drilling, petrophysics, reservoir characterization, reservoir engineering, production/injection engineering) are defined with explicit, operational definitions provided in the paper. [Okoroafor 2022, pp. 5-6]  
- The counted publications must involve an actual application of a machine learning algorithm to a subsurface geothermal problem; articles that merely mention AI or ML are excluded. [Okoroafor 2022, pp. 5]  
- The trend analysis assumes that the IGA and Google Scholar databases are reasonably representative of global geothermal research output, at least for English‑language work.  

## Key Variables / Parameters
- **Machine learning technique categories:** traditional ML (PCA, k‑means, logistic regression, decision trees, random forest, SVM, shallow neural networks) vs. deep learning (deep NN, CNN, RNN, LSTM, GAN, autoencoders). [Okoroafor 2022, pp. 4-5]  
- **Research areas:** exploration, seismicity, drilling, petrophysics, reservoir characterization, reservoir engineering, production/injection engineering. [Okoroafor 2022, pp. 5-6]  
- **Time window:** 2002 – 2021.  
- **Output metrics:** publication counts, algorithm usage trends, ratio of ML papers to total geothermal papers.  
- **Application problems per area:** e.g., rate‑of‑penetration prediction in drilling, reservoir‑temperature estimation in reservoir characterization, production decline prediction in reservoir engineering. [Okoroafor 2022, pp. 13-14]  

## Reusable Claims
1. **Reservoir characterization is the most machine‑learning‑intensive subsurface area in geothermal energy.** This claim holds for the period 2002‑2021 based on the reviewed 98 papers, with geochemical temperature estimation and fracture characterization as primary sub‑tasks. [Okoroafor 2022, pp. 10-11]  
2. **Shallow neural networks are the dominant algorithm class across all geothermal subsurface research areas.** This conclusion is drawn from the summary table (Table 1) and is conditioned on the 98 reviewed papers; it does not consider techniques used in older, non‑AI‑branded studies. [Okoroafor 2022, pp. 13-14]  
3. **Deep learning adoption in subsurface geothermal research became significant only after 2020**, with deep neural networks and CNNs appearing mainly in reservoir engineering and seismicity. This claim is based on the observed publication trend in the curated corpus. [Okoroafor 2022, pp. 6-7]  
4. **Drilling and exploration—the highest‑risk and highest‑cost phases—show relatively few ML applications**, indicating an opportunity for expanded use of machine learning to reduce financial risk. [Okoroafor 2022, pp. 8, 14]  
5. **Transfer learning from oil‑and‑gas machine‑learning models is a prospective avenue** for tasks such as seismic interpretation, fault detection, and well‑log interpretation in geothermal contexts, though no geothermal‑specific transfer‑learning case studies are yet documented. [Okoroafor 2022, pp. 14]  

## Candidate Concepts
- [[enhanced geothermal system (EGS)]]  
- [[subsurface geothermal resource development]]  
- [[reservoir characterization]]  
- [[fracture characterization]]  
- [[geothermal exploration]]  
- [[induced seismicity]]  
- [[rate of penetration (ROP)]]  
- [[petrophysical properties]]  
- [[geothermal reservoir temperature estimation]]  
- [[tracer test interpretation]]  
- [[proxy modeling]]  
- [[transfer learning]]  
- [[data-driven reservoir management]]  

## Candidate Methods
- [[artificial neural network (ANN)]]  
- [[shallow neural network]]  
- [[deep neural network (DNN)]]  
- [[convolutional neural network (CNN)]]  
- [[recurrent neural network (RNN)]]  
- [[long short‑term memory (LSTM)]]  
- [[multi‑layer perceptron (MLP)]]  
- [[support vector machine (SVM)]]  
- [[random forest (RF)]]  
- [[k‑nearest neighbors (kNN)]]  
- [[decision tree]]  
- [[gradient boosting]]  
- [[XGBoost]]  
- [[principal component analysis (PCA)]]  
- [[k‑means clustering]]  
- [[generative adversarial network (GAN)]]  
- [[autoencoder]]  
- [[alternating conditional expectations (ACE)]]  
- [[non‑negative matrix factorization (NMF)]]  
- [[genetic algorithm (GA)]]  

## Connections To Other Work
- The review explicitly connects geothermal ML challenges to the oil‑and‑gas industry, noting that AI has lowered exploration risks, improved drilling automation, and enhanced reservoir monitoring in oil and gas. These successes motivate similar applications in geothermal energy. [Okoroafor 2022, pp. 2-3]  
- The paper references the AI Index report to contextualize the boom in AI research and notes that investment in AI for the energy sector remains negligible, which may explain the relatively late adoption of ML in geothermal research. [Okoroafor 2022, pp. 3]  
- The concept of transfer learning is introduced as a way to leverage pre‑trained oil‑and‑gas models for analogous geothermal tasks, though concrete interdisciplinary examples are not provided. [Okoroafor 2022, pp. 14]  

## Open Questions
- **How can ML be better integrated into exploration and drilling to reduce the high up‑front risks and costs?** The paper identifies these areas as under‑served despite their critical financial impact. [Okoroafor 2022, pp. 8, 14]  
- **What are the most effective strategies for creating open, curated geothermal datasets** that would enable more widespread and rigorous ML research? [Okoroafor 2022, pp. 13]  
- **How can the geothermal workforce be rapidly upskilled in AI/ML** to close the gap between data availability and model development? [Okoroafor 2022, pp. 13]  
- **To what extent can transfer learning from oil‑and‑gas models accelerate geothermal ML applications** given the differences in data distribution, geological settings, and operational constraints? [Okoroafor 2022, pp. 14]  
- **Will the exponential growth in deep‑learning publications continue**, and will deep‑learning methods eventually dominate all subsurface geothermal research areas, or will traditional ML remain important for data‑scarce problems?  

## Source Coverage
All 21 non‑empty indexed fragments from Okoroafor et al. (2022) were processed in this compilation. The indexed text totals 100,409 characters, of which 95,803 characters (coverage ratio by blocks = 1.0; coverage ratio by characters = 0.954) are represented in the supplied source blocks. No external information was added.
