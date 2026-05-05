---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-chaipornkaew-predicting-off-fault-deformation-from-experimental-strike-slip-fault-images-us"
title: "Predicting Off-Fault Deformation From Experimental Strike-Slip Fault Images Using Convolutional Neural Networks."
status: "draft"
source_pdf: "data/papers/Predicting Off-Fault Deformation From Experimental Strike-Slip Fault Images Using Convolutional Neural Networks.pdf"
collections:
citation: "Chaipornkaew, L., et al. “Predicting Off-Fault Deformation From Experimental Strike-Slip Fault Images Using Convolutional Neural Networks.” *Geophysical Research Letters*, vol. 49, no. 12, 2022."
indexed_texts: "9"
indexed_chars: "40657"
nonempty_source_blocks: "9"
compiled_source_blocks: "9"
compiled_source_chars: "40561"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.997639"
coverage_status: "full-index"
source_signature: "6512df7c8e963b5168211b9d3a06e7f23fca8d55"
compiled_model: "mimo/mimo-v2.5-pro"
compiled_at: "2026-05-05T10:23:47"
---

# Predicting Off-Fault Deformation From Experimental Strike-Slip Fault Images Using Convolutional Neural Networks.

## One-line Summary

A 2D convolutional neural network trained on binary fault maps from scaled wet-kaolin strike-slip experiments predicts kinematic efficiency (off-fault deformation) with 91% accuracy on unseen experimental data and shows promise for crustal fault applications.

## Research Question

Can a convolutional neural network trained on laboratory-generated strike-slip fault maps predict kinematic efficiency (KE)—the ratio of fault slip to total regional deformation—directly from fault trace geometry, and can such a model generalize to crustal-scale faults? [Chaipornkaew 2022, pp. 1-2]

## Study Area / Data

The study uses analog (scaled physical) experiments rather than a natural geographic study area. Experiments were conducted using wet kaolin clay in a table-top deformation apparatus designed to simulate crustal faulting, where 1 cm of clay equates to 1–2 km of crust [Chaipornkaew 2022, pp. 1-2]. Sixteen experiments were conducted with two basal shear conditions (distributed shear via a 2.5 cm wide elastic band, and localized shear over juxtaposed basal plates) and four loading velocities (0.25, 0.5, 1.0, or 1.5 mm/min), each repeated at least twice [Chaipornkaew 2022, pp. 1-2]. Approximately 200 fault maps per experiment were collected at ~0.3 mm displacement intervals, yielding ~13,400 unique binary fault map inputs after filtering and windowing (64 × 128 pixel windows with ~20% overlap) [Chaipornkaew 2022, pp. 2-3]. For crustal validation, fault traces from three geologic studies were used: the 2016 M7 Kumamoto earthquake Futagawa fault (Scott et al., 2019), Holocene drainages adjacent to the San Andreas fault at Mecca Hills (Gray et al., 2018), and Mesozoic faults/dikes adjacent to the northern Calico fault (Shelef & Oskin, 2010) [Chaipornkaew 2022, pp. 5-6].

## Methods

**Data generation:** Digital image correlation (DIC) techniques and adaptive thresholding were applied to surface images to generate active fault maps and incremental displacement/shear strain maps [Chaipornkaew 2022, pp. 2-3]. Kinematic efficiency labels and their standard deviations were calculated directly from the strain maps [Chaipornkaew 2022, pp. 2-3].

**Data splitting:** For each experiment configuration, all five windows of one experiment were allocated to training; windows from repeated configurations were randomly split into training (2 windows), validation (2 windows), and testing (1 window), yielding a 64%/24%/12% split ratio. Entire time series from each window were kept together to avoid data leakage [Chaipornkaew 2022, pp. 2-3].

**CNN architecture:** The CNN follows a convolutional architecture inspired by LeNet-5 and AlexNet, with stacking convolutional layers (appropriate kernel sizes and dilation parameters), batch normalization, ReLU activation, max-pooling, fully connected layers, and dropout regularization [Chaipornkaew 2022, pp. 3-5]. The Adam optimizer was used [Chaipornkaew 2022, pp. 3-5].

**Data augmentation:** Mini-batch processing (256 samples) with geometric transformations—flip, zoom (±5%), and shift (±10%)—to diversify the dataset [Chaipornkaew 2022, pp. 3-5].

**Custom loss function:** A normalized mean square error (MSE) scaled by the squared standard deviation of KE labels, allowing the model to learn more precisely where confidence is highest and relax where uncertainties are high [Chaipornkaew 2022, pp. 3-5].

**Custom accuracy metric:** A prediction was considered correct if the absolute difference between predicted KE and the KE label was within two standard deviations of the labeling calculation uncertainty [Chaipornkaew 2022, pp. 3-5].

**Crustal application:** Crustal fault maps were windowed to 64 × 128 pixels (scaling 6.4 cm experimental width to 6.4 km crustal width using 1 cm = 1 km scaling), oriented so maximum shear strain direction parallels the short edge, and tested with fault trace thicknesses of 2, 3, and 4 pixels [Chaipornkaew 2022, pp. 5-6].

## Key Findings

- The best CNN model achieved 96.7% accuracy on training data, 96.1% on validation data, and 90.9% on an unseen test dataset [Chaipornkaew 2022, pp. 5-6].
- The CNN successfully predicted KE from experimental fault maps across all stages of fault evolution, from echelon crack initiation to through-going slip surfaces [Chaipornkaew 2022, pp. 5-6].
- When applied to crustal fault maps, the CNN predicted KEs that overlap all available geologic estimates from three independent studies [Chaipornkaew 2022, pp. 5-6].
- The CNN predicted the greatest off-fault deformation (lowest KE) for the Calico fault (most segmented trace) and the least off-fault deformation for the San Andreas fault (most straight and continuous) [Chaipornkaew 2022, pp. 5-6].
- Incorrect predictions appeared as clusters of outliers correlating to specific stages of specific experiments rather than being randomly distributed [Chaipornkaew 2022, pp. 6-7].
- KE varies significantly over relatively short distances along faults, with standard deviation within a single 6.4 cm window up to 20% [Chaipornkaew 2022, pp. 6-7].

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| Geologic investigations suggest ~10%–30% of regional strain occurs off mapped faults | [Chaipornkaew 2022, pp. 1-1] | Strike-slip faults in nature | Cites Goren et al., 2015; Gray et al., 2018; Shelef & Oskin, 2010; Titus et al., 2011 |
| Smoother strike-slip faults accommodate slip more efficiently with lesser off-fault deformation | [Chaipornkaew 2022, pp. 1-1] | Both natural and experimental faults | Hypothesis supported by scaled physical experiments |
| As faults mature and become smoother, kinematic efficiency (KE) increases | [Chaipornkaew 2022, pp. 1-1] | Scaled physical experiments | Directly documented in experiments (Hatem et al., 2017) |
| ~13,400 unique binary fault map inputs generated from 16 experiments | [Chaipornkaew 2022, pp. 2-3] | Wet kaolin, various loading rates and basal conditions | After filtering early maps prior to fault initiation |
| Best CNN model achieves 90.9% custom accuracy on unseen test data | [Chaipornkaew 2022, pp. 5-6] | 64×128 pixel binary fault maps | Custom metric: prediction correct if within 2SD of label uncertainty |
| CNN predicts KEs overlapping all three geologic estimates for crustal faults | [Chaipornkaew 2022, pp. 5-6] | Crustal fault maps from Futagawa, San Andreas, Calico faults | Tested with fault thicknesses of 2, 3, and 4 pixels |
| KE within a single 6.4 cm window has standard deviation up to 20% | [Chaipornkaew 2022, pp. 6-7] | Experimental fault maps | Demonstrates significant along-strike variability |
| Fractal dimension cannot reliably capture roughness of segmented faults | [Chaipornkaew 2022, pp. 1-2] | Segmented/immature strike-slip faults | Motivates use of CNN over traditional metrics |

## Limitations

- The CNN was trained exclusively on wet kaolin experiments; kaolin produces highly localized faults, whereas other analog materials (e.g., sand) produce wider fault zones and may yield different off-fault deformation degrees [Chaipornkaew 2022, pp. 6-7].
- The active morphology of crustal strike-slip faults may depend on processes not captured in the wet kaolin experiments, so the CNN may not accurately predict off-fault deformation for all strike-slip faults [Chaipornkaew 2022, pp. 6-7].
- The 6.4 cm wide window may not fully capture fault segmentation; if the window spans only a single segment rather than adjacent segments, KE will be artificially high [Chaipornkaew 2022, pp. 6-7].
- The CNN predicted KE for crustal fault maps did not vary systematically with fault trace thickness, suggesting potential sensitivity to geometric augmentation scale [Chaipornkaew 2022, pp. 6-7].
- Incorrect predictions clustered as outliers correlated to specific stages of specific experiments, indicating the model may struggle with certain fault configurations [Chaipornkaew 2022, pp. 6-7].
- Very few geologic estimates of off-fault deformation exist for crustal faults, limiting validation [Chaipornkaew 2022, pp. 5-6].

## Assumptions / Conditions

- Wet kaolin clay is a valid analog for crustal materials, with 1 cm of clay scaling to 1–2 km of crust [Chaipornkaew 2022, pp. 1-2].
- Binary fault maps oriented to regional loading contain sufficient geometric information to predict KE [Chaipornkaew 2022, pp. 1-2].
- The viscoelastic behavior of wet kaolin simulates off-fault stress relaxation within the crust [Chaipornkaew 2022, pp. 1-2].
- The custom accuracy metric (prediction within 2 standard deviations of label uncertainty) is an appropriate performance measure [Chaipornkaew 2022, pp. 3-5].
- The minimum scaling ratio (1 cm = 1 km) is used for crustal window sizing, providing 2–4 windows per crustal study [Chaipornkaew 2022, pp. 5-6].
- The range of loading rates in experiments incorporates some degree of off-fault deformation variability due to the viscoelastic material behavior [Chaipornkaew 2022, pp. 6-7].

## Key Variables / Parameters

- **Kinematic Efficiency (KE):** The ratio of incremental strike-slip accommodated along faults to total incremental displacement; ranges from 0 (all off-fault deformation) to 1 (all on-fault slip) [Chaipornkaew 2022, pp. 1-1].
- **Off-fault deformation:** The portion of total applied loading not expressed as fault slip (1−KE) [Chaipornkaew 2022, pp. 1-1].
- **Basal shear conditions:** Distributed shear (elastic band) vs. localized shear (juxtaposed basal plates) [Chaipornkaew 2022, pp. 1-2].
- **Loading velocities:** 0.25, 0.5, 1.0, 1.5 mm/min [Chaipornkaew 2022, pp. 1-2].
- **Input window size:** 64 × 128 pixels, short side parallel to applied shear [Chaipornkaew 2022, pp. 2-3].
- **Custom loss function:** L = MSE / (SD² + ε), where ε = 1e-5 [Chaipornkaew 2022, pp. 3-5].
- **Augmentation ranges:** Zoom ±5%, Shift ±10% [Chaipornkaew 2022, pp. 3-5].
- **Mini-batch size:** 256 samples [Chaipornkaew 2022, pp. 3-5].
- **Training epochs:** 50 (with early stopping to prevent overfitting) [Chaipornkaew 2022, pp. 5-6].

## Reusable Claims

- Approximately 10%–30% of regional strain may occur off mapped strike-slip faults, based on geologic investigations [Chaipornkaew 2022, pp. 1-1].
- Strike-slip faults with smoother traces accommodate slip more efficiently and produce less off-fault deformation than faults with rough or complex traces in the slip direction [Chaipornkaew 2022, pp. 1-1].
- Fractal dimension cannot reliably quantify the roughness of segmented fault maps where connectivity controls fault slip, limiting its utility for immature fault stages [Chaipornkaew 2022, pp. 1-2].
- A 2D CNN trained on binary fault maps from scaled experiments can predict kinematic efficiency with ~91% custom accuracy on unseen experimental data, where accuracy is defined as predictions within two standard deviations of the label uncertainty [Chaipornkaew 2022, pp. 5-6].
- When applied to crustal fault maps, the experimentally trained CNN predicts KE values that overlap available geologic estimates from independent studies using different methods (coseismic DIC, geomorphic analysis, geologic mapping) [Chaipornkaew 2022, pp. 5-6].
- KE varies significantly over short distances along faults, with standard deviations up to 20% within a single 6.4 cm experimental window [Chaipornkaew 2022, pp. 6-7].
- The degree of off-fault deformation in viscoelastic analog materials depends on applied loading rate [Chaipornkaew 2022, pp. 6-7].

## Candidate Concepts

- [[kinematic efficiency]]
- [[off-fault deformation]]
- [[strike-slip fault evolution]]
- [[fault maturity]]
- [[fault segmentation]]
- [[distributed deformation]]
- [[analog modeling]]
- [[wet kaolin clay]]
- [[fractal dimension]]
- [[fault complexity]]
- [[seismic hazard analysis]]

## Candidate Methods

- [[convolutional neural network (CNN)]]
- [[digital image correlation (DIC)]]
- [[adaptive thresholding]]
- [[custom loss function]]
- [[data augmentation]]
- [[Adam optimizer]]
- [[batch normalization]]
- [[dropout regularization]]
- [[max-pooling]]
- [[scaled physical experiments]]

## Connections To Other Work

- The study builds on scaled physical experiments of strike-slip fault evolution using wet kaolin (Hatem et al., 2015, 2017; Cooke et al., 2013; Tchalenko, 1970) [Chaipornkaew 2022, pp. 1-2].
- Geologic estimates of off-fault deformation from Goren et al. (2015), Gray et al. (2018), Shelef & Oskin (2010), and Titus et al. (2011) provide the basis for the ~10%–30% range [Chaipornkaew 2022, pp. 1-1].
- The CNN architecture is inspired by LeNet-5 (Lecun et al., 1998) and AlexNet (Krizhevsky et al., 2012) [Chaipornkaew 2022, pp. 3-5].
- Crustal validation uses fault maps from Scott et al. (2019) for the Futagawa fault, Gray et al. (2018) for the San Andreas fault at Mecca Hills, and Shelef & Oskin (2010) for the Calico fault [Chaipornkaew 2022, pp. 5-6].
- The hypothesis that smoother faults produce greater slip is supported by studies on fault roughness and stress (Chester & Chester, 2000; Fang & Dunham, 2013; Newman & Griffith, 2014; Saucier et al., 1992) [Chaipornkaew 2022, pp. 1-1].
- The relationship between fault maturity and surface slip vs. off-fault deformation connects to Dolan & Haravitch (2014) and Milliner et al. (2016) [Chaipornkaew 2022, pp. 1-1].

## Open Questions

- Can the CNN be retrained on additional datasets (e.g., using different analog materials like sand) to produce more robust predictive tools for crustal faults? [Chaipornkaew 2022, pp. 6-7]
- How does the choice of window width affect KE prediction for highly segmented faults, and what is the optimal window size? [Chaipornkaew 2022, pp. 6-7]
- How well does the model generalize to strike-slip faults with different rheological properties or tectonic settings not represented in the training data? [Chaipornkaew 2022, pp. 6-7]
- Could the approach be extended to predict off-fault deformation for other fault types (normal, reverse)? [Not confirmed in fragments]
- What is the sensitivity of the CNN predictions to the fault trace thickness representation in crustal maps? [Chaipornkaew 2022, pp. 6-7]

## Source Coverage

All 9 non-empty indexed fragments were processed. The compiled source blocks total 9 of 9, covering 40,561 of 40,657 indexed characters (coverage ratio: 0.998 by characters, 1.0 by blocks). The coverage status is full-index with a single-pass compile strategy.
