---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2022-waqas-investigation-of-strength-behavior-of-thermally-deteriorated-sedimentary-rocks-subjec"
title: "Investigation of Strength Behavior of Thermally Deteriorated Sedimentary Rocks Subjected to Dynamic Cyclic Loading."
status: "draft"
source_pdf: "data/papers/2022 - Investigation of strength behavior of thermally deteriorated sedimentary rocks subjected to dynamic cyclic loading.pdf"
collections:
  - "论文"
citation: "Waqas, Umer, and Muhammad Farooq Ahmed. “Investigation of Strength Behavior of Thermally Deteriorated Sedimentary Rocks Subjected to Dynamic Cyclic Loading.” *International Journal of Rock Mechanics & Mining Sciences*, vol. 158, 2022, 105201. doi:10.1016/j.ijrmms.2022.105201."
indexed_texts: "15"
indexed_chars: "74613"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T10:56:54"
---

# Investigation of Strength Behavior of Thermally Deteriorated Sedimentary Rocks Subjected to Dynamic Cyclic Loading.

## One-line Summary
This study investigates the strength behavior of thermally deteriorated sedimentary rocks under high-frequency dynamic cyclic loading, using experiments and machine learning to model and classify the strength improvement caused by crack closure at resonance.

## Research Question
How does dynamic cyclic loading at resonance frequencies affect the stiffness and strength of thermally damaged sedimentary rocks, and can data-driven models predict and classify the resulting strength improvement? [Waqas 2022, pp. 2-2]

## Study Area / Data
Rock samples were collected from the Khewra Gorge, Punjab, Pakistan. The studied rock types included calcite-rich marl, dolomite, limestone, and five different sandstone formations, categorized broadly as carbonate and silicate groups. [Waqas 2022, pp. 2-3, 7-7]

## Methods
- **Sample Preparation and Thermal Treatment**: NX-size rock core samples (length-to-diameter ratio of 2.5–3) were prepared per ASTM C215. Samples were heated in a cyclic manner from 50°C to 200°C in 50°C increments, with gradual cooling in a desiccator between each stage to induce thermal tension cracks. [Waqas 2022, pp. 2-3]
- **Dynamic Testing**: Thermally treated samples were tested under dynamic cyclic loading at resonance frequencies of 5–15 kHz, in accordance with ASTM C215, using an Erudite Resonance Frequency Meter in both longitudinal and torsional modes. [Waqas 2022, pp. 1-2, 3-6]
- **Unconfined Compressive Strength (UCS) Test**: UCS tests were performed to validate the creation of thermal damage. [Waqas 2022, pp. 2-3]
- **Strength Improvement Factor (SIF) Calculation**: SIF was calculated using the change in Poisson's ratio before and after dynamic loading: `SIF = (1 - v_i^2 / v_f^2) × 100`. [Waqas 2022, pp. 3-6]
- **Predictive Modeling**: Two techniques were used to relate SIF to dynamic properties:
    - **Cascade-Forward Neural Network (CFNN)** [Waqas 2022, pp. 6-6]
    - **Adaptive Neuro-Fuzzy Inference System (ANFIS)** [Waqas 2022, pp. 6-6]
- **Classification**: A hybrid meta-classifier (MC) was developed by stacking six supervised learning algorithms to classify rocks into SIF groups. The base classifiers were: Naïve Bayes (NB), Logistic Regression (LR), K-Nearest Neighbor (K-NN), Multilayer Perceptron (ANN-MLP), Support Vector Machine (SVM), and Random Forest (RF). [Waqas 2022, pp. 1-2, 7-7]
- **Model Validation**: Model performance was evaluated using metrics including the confusion matrix, precision, recall, F-measure, Receiver Operator Characteristic (ROC) curve, Matthew’s correlation coefficient (MCC), and percentage error rate. [Waqas 2022, pp. 6-7]

## Key Findings
- Under resonance, all measured dynamic parameters of thermally damaged rocks showed an increase. [Waqas 2022, pp. 1-2]
- Specific increments at the resonance state ranged from:
    - Longitudinal quality factor: 16–30
    - Torsional quality factor: 9–20
    - Longitudinal resonance frequency: 1.5–2.2 kHz
    - Torsional resonance frequency: 1.0–1.8 kHz
    - Young’s modulus: 34–162 GPa
    - Shear modulus: 17–69 GPa
    - Strength Improvement Factor (SIF): 0–39% [Waqas 2022, pp. 1-2]
- The ANFIS model (R = 0.97) demonstrated superior predictive performance for SIF compared to the CFNN model (R = 0.93). [Waqas 2022, pp. 1-2]
- For SIF-based classification, the developed hybrid meta-classifier (MC) outperformed all individual base classifiers on both training and validation datasets, showing higher values for all performance indicators. [Waqas 2022, pp. 1-2]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| SIF values increased by 0–39% under resonance. | [Waqas 2022, pp. 1-2] | NX-size sedimentary rock cores subjected to cyclic heating up to 200°C and tested at 5–15 kHz. | SIF is calculated from the before and after Poisson's ratio. |
| ANFIS predicted SIF with R = 0.97, outperforming CFNN (R = 0.93). | [Waqas 2022, pp. 1-2] | Dependent variable: SIF. Independent variables: resonance frequency ratio and quality factor ratio. | Performance measured by correlation coefficient R. |
| The hybrid meta-classifier (MC) performed better than NB, LR, K-NN, ANN-MLP, SVM, and RF individually. | [Waqas 2022, pp. 1-2] | Classification into 5 SIF groups. Validation using metrics like MCC and error rate. | MC is a stacking ensemble of the six listed classifiers. |
| Measured dynamic properties for Salt Range Marl: E=47.43 GPa, G=20.17 GPa, v=0.17. | [Waqas 2022, pp. 3-6] | Samples tested according to ASTM C215. | Data represents Pre-Cambrian rocks from the study area. |

## Limitations
未从索引片段中确认作者明确指出的研究局限性。但从方法描述来看，研究结果特定于所采集的岩石类型（Khewra Gorge的沉积岩）和特定的热处理方案（最高200°C的循环加热）。

## Assumptions / Conditions
- The cyclic heating and cooling procedure effectively induced thermal tension cracks in the rock samples, validated by UCS tests. [Waqas 2022, pp. 2-3]
- The crack closure phenomenon under elastic deformation is the primary mechanism for stiffness and strength improvement under the wave resonance effect. [Waqas 2022, pp. 3-6]
- Dynamic testing was performed only in the linear-nonlinear strain regimes up to resonance. [Waqas 2022, pp. 2-2]
- `SIF` calculation `SIF = (1 - v_i^2 / v_f^2) × 100` is an appropriate metric for quantifying strength improvement due to dynamic loading. [Waqas 2022, pp. 3-6]
- The independent variables for prediction modeling (resonance frequency ratio `(F_r)_L / (F_r)_T` and quality factor ratio `Q_L / Q_T`) are sufficient to predict `SIF`. [Waqas 2022, pp. 6-6]
- The machine learning classifiers assume that the 5-group classification of SIF is meaningful and the labeled data is representative. [Waqas 2022, pp. 6-7]

## Key Variables / Parameters
- **Measured Dynamic Properties**: Young's modulus (E), Shear modulus (G), Poisson's ratio (v), Longitudinal resonance frequency `(F_r)_L`, Torsional resonance frequency `(F_r)_T`, Longitudinal quality factor `Q_L`, Torsional quality factor `Q_T`. [Waqas 2022, pp. 1-2, 3-6]
- **Derived Metric**: Strength Improvement Factor (SIF) [Waqas 2022, pp. 3-6]
- **Prediction Model Inputs (Independent Variables)**: Resonance frequency ratio `(F_r)_L / (F_r)_T`, Quality factor ratio `Q_L / Q_T`. [Waqas 2022, pp. 6-6]
- **Thermal Treatment Parameters**: Maximum temperature (200°C), heating increment (50°C), heating rate (1–5 °C/min). [Waqas 2022, pp. 1-2, 2-3]
- **Dynamic Loading Parameters**: Frequency range (5–15 kHz). [Waqas 2022, pp. 1-2]

## Reusable Claims
- **Claim**: For thermally damaged sedimentary rocks, dynamic loading at resonance frequency can induce an increase in dynamic moduli and a Strength Improvement Factor (SIF) of up to 39%. This is attributed to the elastic closure of thermal cracks. [Waqas 2022, pp. 1-2, 3-6]
    - **Conditions**: Thermal damage induced by cyclic heating up to 200°C; testing under high-frequency (5–15 kHz) cyclic loading at resonance.
    - **Evidence**: Measured increases in Young's modulus (34–162 GPa), shear modulus (17–69 GPa), and SIF (0–39%).
- **Claim**: The Adaptive Neuro-Fuzzy Inference System (ANFIS) is a superior predictor (R=0.97) compared to a Cascade-Forward Neural Network (R=0.93) for the Strength Improvement Factor of thermally damaged rocks at resonance. [Waqas 2022, pp. 1-2]
    - **Conditions**: Inputs are resonance frequency ratio and quality factor ratio.
- **Claim**: A stacking ensemble meta-classifier can more accurately classify the degree of dynamic strength improvement in thermally damaged rocks than individual classifiers including SVM, Random Forest, and K-NN. [Waqas 2022, pp. 1-2]
    - **Conditions**: Base classifiers: NB, LR, K-NN, ANN-MLP, SVM, RF.

## Candidate Concepts
- [[Thermal Damage]]
- [[Resonance Frequency]]
- [[Wave Resonance Effect]]
- [[Rock Stiffness]]
- [[Strength Improvement Factor (SIF)]]
- [[Dynamic Cyclic Loading]]
- [[Crack Closure]]
- [[Meta-classifier]]
- [[Ensemble Learning]]
- [[Poisson's Ratio]]

## Candidate Methods
- [[ASTM C215]] (Fundamental Transverse, Longitudinal, and Torsional Frequencies of Concrete Specimens)
- [[Erudite Resonance Frequency Meter]]
- [[Adaptive Neuro-Fuzzy Inference System (ANFIS)]]
- [[Cascade-Forward Neural Network (CFNN)]]
- [[Random Forest (RF)]]
- [[Support Vector Machine (SVM)]]
- [[K-Nearest Neighbor (K-NN)]]
- [[Stacking Ensemble Method]]

## Connections To Other Work
- The study explicitly states that past research using resonant bar experiments noticed a shift in resonance frequency from linear (intermediate strain) to nonlinear decline (high strain) at ambient conditions, but no such studies existed for thermally damaged rocks prior to this work. [Waqas 2022, pp. 2-2]
- The work builds upon the ASTM C215 testing procedure, adapting it for rock mechanics. [Waqas 2022, pp. 1-2, 2-3]
- Authors note that previous predictive models for rock properties were based on mechanical, physical, and mineralogical properties, but no meaningful relationship for dynamic parameters of thermally damaged rocks under resonance had been developed. [Waqas 2022, pp. 2-2]
- Potential conceptual connections include [[Empirical Rock Property Estimation]], [[Nonlinear Resonance Spectroscopy]], and [[Microcrack Damage in Geomaterials]].

## Open Questions
- What is the specific nature of the thermal microcracks (density, aspect ratio, distribution) generated by the heating protocol, and how do they quantitatively relate to the closure efficiency?
- How transferable are the developed CFNN, ANFIS, and MC models to other rock types or different thermal damage scenarios (e.g., fire damage, geothermal environments)?
- What is the underlying physical mechanism for the superiority of the ANFIS model over the CFNN model in this specific prediction task?
- The study notes a shift from linear to nonlinear frequency behavior in undamaged rocks; how does this nonlinear behavior manifest in the measured properties of thermally damaged rocks under resonance, and was it captured by the models? [Waqas 2022, pp. 2-2]

## Source Coverage
This Markdown page is based on 15 index fragments from [Waqas 2022]. The coverage is heavily weighted towards the **Introduction**, **Methods**, and summary of **Key Findings** from the Abstract. Specific details on the experimental data table (Table 1) and the mechanics of model architectures are present. However, the **Results and Discussion** and **Conclusion** sections are largely missing, meaning detailed analysis of model performance (beyond the final R values), the specific classification results for each rock type, and discussions on geological or practical implications are not covered in the provided fragments.
