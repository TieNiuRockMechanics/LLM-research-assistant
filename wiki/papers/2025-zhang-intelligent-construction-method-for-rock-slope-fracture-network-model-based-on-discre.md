---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2025-zhang-intelligent-construction-method-for-rock-slope-fracture-network-model-based-on-discre"
title: "Intelligent Construction Method for Rock Slope Fracture Network Model Based on Discrete Element and Neural Network."
status: "draft"
source_pdf: "data/papers/2025 - Intelligent construction method for rock slope fracture network model based on discrete element and neural network.pdf"
collections:
citation: "Zhang, Zhe, et al. \"Intelligent Construction Method for Rock Slope Fracture Network Model Based on Discrete Element and Neural Network.\" *Scientific Reports*, vol. 15, 2025, article 41577, doi:10.1038/s41598-025-25409-2."
indexed_texts: "14"
indexed_chars: "69979"
nonempty_source_blocks: "14"
compiled_source_blocks: "14"
compiled_source_chars: "69457"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.992541"
coverage_status: "full-index"
source_signature: "986c09ba30e0941dbe8feed8b160ea01dc8be23d"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T08:35:23"
---

# Intelligent Construction Method for Rock Slope Fracture Network Model Based on Discrete Element and Neural Network.

## One-line Summary
This study develops an intelligent Discrete Fracture Network (DFN) construction method that fuses field adit data, Monte Carlo stochastic simulation in 3DEC, and Back Propagation (BP) and Cascade Correlation (CC) neural networks to invert 3D fracture parameters from 2D adit observations; applied to the Dadu River Chengdu Bank rock slope using a stratified modeling strategy over three lithological units, the optimal models yield parameter inversion errors of 18.4 % (four-layer BP for diorite), 8.0 % (three-layer BP for cataclastic rock), and 10.3 % (CC for granite), and the complete DFN closely matches field fracture distributions[Zhang 2025, pp. 1-2][Zhang 2025, pp. 22-24].

## Research Question
How can limited 2D adit fracture observations be transformed into a high-fidelity 3D discrete fracture network model for complex high‑steep rock slopes, overcoming cross‑scale mapping errors, spatial heterogeneity, and the small‑sample limitations of traditional statistical and machine learning approaches?[Zhang 2025, pp. 1-2]

## Study Area / Data
- **Site:** Dadu River Chengdu Bank rock slope (Dadu River Grand Bridge slope project), Lu Ding, Ganzi Tibetan Autonomous Prefecture, Sichuan Province, China[Zhang 2025, pp. 6-8].
- **Exploration adit:** elevation 1724 m, cross‑section 2 m × 2 m, length 100 m, excavated by drilling and blasting; highly weathered, blocky, fractured rock mass with three dominant fracture sets[Zhang 2025, pp. 6-8].
- **Lithological units (stratified):** diorite (0–30 m), cataclastic rock (30–60 m), granite (60–90 m); the field fractures were simplified to 121, 123, and 90 discrete fractures, respectively[Zhang 2025, pp. 6-8].
- **Synthetic data library:** 625 numerical simulations per lithological unit using 3DEC; each simulation produced “whole fracture trace” and “penetrating fracture trace” statistical maps; from these, 23 geometric input parameters (dip, size, centroid coordinates, etc., Table 7) and 6 output parameters (k, α, lmin, lmax, Hbottom, Htop) were extracted, yielding 625 data samples per zone[Zhang 2025, pp. 10-12].
- **Optimal image format for PCAS feature extraction:** resolution 600 × 9000 pixels, fracture trace colour green, transparency 70 %[Zhang 2025, pp. 8-10].

## Methods
1. **DFN modelling framework:**  
   - Fracture orientation via Fisher distribution (density index k, Eq. 4), size via power‑law model (Davy, length index α, Eq. 6‑7), spatial position by homogeneous Poisson process, and geometry abstracted as discs[Zhang 2025, pp. 2-3][Zhang 2025, pp. 3-6].  
   - Monte Carlo stochastic generation in 3DEC, controlled by six calibrated parameters (k, α, lmin, lmax, Hbottom, Htop) and three fixed parameters (mean dip θ0, mean dip‑direction φ0, actual fracture count per zone)[Zhang 2025, pp. 6-8][Zhang 2025, pp. 10-12].

2. **Stratified numerical experiments:**  
   - Three lithological units, each with system‑determined parameter ranges (Table 4); 5×5×5×5 = 625 simulations per unit using 3DEC, extracting whole‑ and penetrating‑fracture trace maps[Zhang 2025, pp. 6-8][Zhang 2025, pp. 10-12].

3. **Image‑based feature extraction:**  
   - PCAS program used to analyse trace maps; pixel resolution, colour, and transparency optimised; selected configuration: 600 × 9000 px, green colour, 70 % transparency (mean relative error ~5.1‑5.3 %)[Zhang 2025, pp. 8-10].  
   - From each map, 23 geometric parameters were extracted: orientation, size, and location descriptors for whole fractures and penetrating fractures (Table 7)[Zhang 2025, pp. 10-12].

4. **Neural network inversion:**  
   - Two network types: Back Propagation (BP, three‑layer and four‑layer) and Cascade Correlation (CC); activation function tanh, loss function MSE, data split 60 % training / 20 % validation / 20 % testing[Zhang 2025, pp. 12-15].  
   - Hyperparameter ranges: hidden neurons hBP∈[6,29], hmax CC = 20; learning step ε∈(0,0.5]; grid search used to find optimal structures (Table 9) and learning parameters (Table 10)[Zhang 2025, pp. 15-17].  
   - For each lithological zone, 625 samples were used to train and validate the networks; test‑set mean relative errors for all six output parameters were below 30 % (Table 11)[Zhang 2025, pp. 17-19].

5. **Intelligent model selection and DFN assembly:**  
   - Field adit fracture images were processed with PCAS to obtain the 23 input parameters (Table 8); these were fed into the trained networks to predict DFN parameters (Table 12).  
   - For each zone, the model that minimised the average relative error δ* between simulated and field fracture statistics was chosen (Table 13): first group (diorite) → four‑layer BP (δ*=18.4 %); second group (cataclastic rock) → three‑layer BP (δ*=8.0 %); third group (granite) → CC (δ*=10.3 %)[Zhang 2025, pp. 22-24].  
   - The three optimal DFN sub‑models were combined into one complete 3D DFN, which showed high agreement with the original adit fracture pattern[Zhang 2025, pp. 22-24].

## Key Findings
1. The Fisher distribution parameter k controls orientation concentration: larger k concentrates fractures around the mean orientation. The power‑law length index α governs size distribution; increasing α reduces the proportion of long fractures, shifting the network toward short‑length dominance. Fracture positions follow a homogeneous Poisson process, and fracture shape is modelled as a disc[Zhang 2025, pp. 22-24].  
2. For PCAS‑based feature extraction from DFN trace maps, the optimal image format is 600 × 9000 pixels, green fracture traces, and 70 % transparency; this yields relative errors around 5.1 % for transparency and 5.3 % for colour, balancing accuracy and processing time[Zhang 2025, pp. 8-10].  
3. A total of 23 input parameters were derived from adit fracture statistics (dip, size, centroid coordinates for whole and penetrating fractures); together with 625 numerical simulations per lithological zone, they formed the training corpus for the neural network models[Zhang 2025, pp. 10-12].  
4. Optimal neural network configurations per zone: four‑layer BP network for diorite (δ*=18.4 %), three‑layer BP for cataclastic rock (δ*=8.0 %), and CC network for granite (δ*=10.3 %). Test‑set errors for all six output parameters were consistently below 30 %, with elevation bounds Hbottom and Htop showing errors under 1.2 %[Zhang 2025, pp. 17-19][Zhang 2025, pp. 22-24].  
5. The complete DFN model assembled from the three optimal sub‑models reproduces the field fracture distribution with high fidelity, confirming the reliability of the intelligent inversion method[Zhang 2025, pp. 22-24].  
6. Compared with traditional methods, the stratified neural network approach reduces parameter inversion errors by 18.4–55.6 %[Zhang 2025, pp. 1-2].

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Optimal image configuration for PCAS: 600×9000 px, green colour, 70 % transparency → mean relative errors 5.27 % (colour), 5.13 % (transparency). | [Zhang 2025, pp. 8-10] | PCAS used on whole‑fracture trace maps from 3DEC; all colours except black gave similar errors. | Selected over 700×10500 px for processing speed (18.2 s vs 30.7 s). |
| Stratified neural network predictions yield average relative errors δ* of 18.4 % (four‑layer BP, diorite), 8.0 % (three‑layer BP, cataclastic rock), 10.3 % (CC, granite) for the 23 geometric features. | [Zhang 2025, pp. 1-2] (abstract), [Zhang 2025, pp. 22-24] (Table 13) | Field adit data input, optimal network per unit. | Compared to 28.8 %, 21.5 %, 55.6 % for sub‑optimal networks. |
| Test‑set mean relative errors for all six output parameters (k, α, lmin, lmax, Hbottom, Htop) are <30 %; Hbottom and Htop errors are ≤1.23 % across all groups. | [Zhang 2025, pp. 17-19] (Table 11) | 60/20/20 split, optimal structures/hyperparameters; 125 test samples per group. | Confirms strong generalisation capability. |
| Increasing Fisher density index k transforms fracture orientation from quasi‑uniform to strongly clustered around the mean direction (θ0, φ0). | [Zhang 2025, pp. 2-3] | Fisher distribution model; numerical simulation. | k = (Nt−2)/(Nt−|τn|). |
| Larger length index α causes a progressive reduction in the proportion of elongated fractures, driving the system toward predominantly short fractures. | [Zhang 2025, pp. 3-6] | Power‑law (Davy) model with bounds lmin, lmax. | Parametric analysis Fig. 3. |
| Homogeneous Poisson process assumption for fracture centre locations does not capture tectonic‑induced clustering, which may affect seepage and block stability analyses. | [Zhang 2025, pp. 24-25] | Limitation of current model. | Suggested for future improvement. |
| The proposed method achieves 18.4–55.6 % reduction in parameter inversion errors relative to traditional methods. | [Zhang 2025, pp. 1-2] | Comparison with single‑model approaches (not explicitly detailed). | Reflects benefit of stratified modelling and neural networks. |

## Limitations
- **Single adit reliance:** The model is built and validated on data from one exploration adit; generalisability to other slopes or larger regions requires additional borehole or adit data[Zhang 2025, pp. 24-25].
- **Inherent 2D‑to‑3D ambiguity:** Different 3D fracture configurations can produce identical 2D traces; the neural network mapping reduces but does not eliminate this uncertainty[Zhang 2025, pp. 24-25].
- **Lack of mechanical calibration:** Only geometric accuracy is assessed; the DFN has not been validated against rock mass mechanical responses (deformation, failure) or field monitoring data[Zhang 2025, pp. 24-25].
- **Spatial homogeneity assumption:** Fracture centres are generated by a homogeneous Poisson process, potentially ignoring real clustering effects that influence seepage and stability[Zhang 2025, pp. 24-25].

## Assumptions / Conditions
- Fracture geometry is abstracted as a disc (disk‑shaped model)[Zhang 2025, pp. 3-6].
- Fracture orientations follow a Fisher distribution with density index k[Zhang 2025, pp. 2-3].
- Fracture sizes obey a power‑law distribution (Davy model) with length index α and bounded by lmin, lmax[Zhang 2025, pp. 3-6].
- Fracture centroids are distributed according to a homogeneous Poisson process (spatially uniform)[Zhang 2025, pp. 3-6][Zhang 2025, pp. 24-25].
- The adit data adequately represents the fracture population within each lithological unit; stratification captures the dominant spatial heterogeneity[Zhang 2025, pp. 6-8].
- Neural networks trained on 625 synthetic samples can generalise to the field fracture statistics; the mapping between 23 input features and 6 output parameters is one‑to‑one[Zhang 2025, pp. 17-19].
- The PCAS program and the optimised image format (600×9000 px, green, 70 % transparency) accurately extract relevant geometric features from trace maps[Zhang 2025, pp. 8-10].

## Key Variables / Parameters
- **Fixed parameters (per lithological unit):** mean dip angle θ0, mean dip direction φ0, actual number of adit fractures n (Table 3)[Zhang 2025, pp. 6-8].
- **Calibrated output parameters (6):** Fisher density coefficient k, length index α, minimum fracture size lmin, maximum fracture size lmax, bottom elevation Hbottom, top elevation Htop (ranges in Table 4)[Zhang 2025, pp. 6-8][Zhang 2025, pp. 10-12].
- **Input parameters (23):** descriptors of whole‑fracture dip (mean, std, concentration interval, number in concentration, normality fit), size (total length, std, min/max, fractal dimension, fractal fit), centroid coordinates (mean, std, concentration interval, number in concentration, fractal dimension, fractal fit); and penetrative‑fracture mean dip, mean length, mean/min/max centroid coordinates, total number of penetrating fractures (Table 7)[Zhang 2025, pp. 10-12].
- **Neural network hyperparameters:** number of hidden neurons hBP (6–29), maximum hidden neurons for CC (20), learning steps εBP, εCC (0.01 to 0.5), output transformation coefficient σ0, weight coefficient η, data split 60/20/20[Zhang 2025, pp. 12-15][Zhang 2025, pp. 15-17].

## Reusable Claims
- **Image optimisation for PCAS:** For 2D trace maps generated by 3DEC, a resolution of 600×9000 px, green fracture traces, and 70 % transparency provides a balanced trade‑off between extraction accuracy (mean relative error ~5.1–5.3 %) and processing time. *Condition:* similar fracture density and image quality as in this study[Zhang 2025, pp. 8-10].
- **Stratified DFN inversion:** Constructing separate neural‑network models for distinct lithological units can reduce parameter inversion error by up to 55.6 % compared to a single homogeneous model. *Condition:* lithological units exhibit significantly different fracture geometric characteristics[Zhang 2025, pp. 1-2][Zhang 2025, pp. 22-24].
- **Neural network generalisation:** BP and CC networks trained on 625 synthetic DFN simulations can invert six 3D DFN parameters from 23 2D fracture statistics with test‑set mean relative errors <30 % (elevation errors <1.2 %). *Condition:* training data generated under the same Monte Carlo framework and feature extraction pipeline; validation limited to a single adit[Zhang 2025, pp. 17-19].
- **Orientation concentration control:** Increasing Fisher density index k monotonically concentrates fracture orientations around the mean direction. *Condition:* Fisher distribution is an adequate model for the fracture set[Zhang 2025, pp. 2-3].
- **Size distribution scaling:** Increasing length index α systematically reduces the proportion of long fractures, driving the network toward a short‑fracture‑dominated population. *Condition:* fracture size follows a truncated power law with fixed lmin, lmax[Zhang 2025, pp. 3-6].
- **Poisson position limitation:** Assuming a homogeneous Poisson process for fracture centre locations may fail to reproduce clustering, potentially degrading predictions for seepage and rock‑block stability. *Condition:* tectonically influenced zones where clustering is present[Zhang 2025, pp. 24-25].

## Candidate Concepts
- [[Discrete Fracture Network (DFN)]]
- [[Fisher distribution]]
- [[Monte Carlo stochastic simulation]]
- [[Back Propagation (BP) neural network]]
- [[Cascade Correlation (CC) neural network]]
- [[Poisson process]]
- [[power-law distribution]]
- [[stratified modeling]]
- [[density index k]]
- [[length index α]]
- [[disc-shaped fracture model]]
- [[fracture orientation]]
- [[fracture size distribution]]
- [[fracture spatial distribution]]
- [[3DEC software]]
- [[PCAS program]]
- [[image-based feature extraction]]
- [[geometric distribution characteristics]]
- [[2D-to-3D mapping]]
- [[hyperparameter optimization]]
- [[mean relative error δ*]]

## Candidate Methods
- [[3DEC discrete element modeling]]
- [[Monte Carlo simulation]]
- [[Fisher distribution for orientation]]
- [[power-law (Davy) model for fracture size]]
- [[Poisson process for spatial location]]
- [[image processing with PCAS]]
- [[pixel resolution optimization]]
- [[color and transparency optimization]]
- [[Back Propagation neural network]]
- [[Cascade Correlation neural network]]
- [[tanh activation function]]
- [[MSE loss function]]
- [[grid search for hyperparameters]]
- [[promotion prediction algorithm]]
- [[stratified modeling strategy]]
- [[numerical simulation experimental design]]
- [[data split (60/20/20)]]

## Connections To Other Work
- Builds on foundational DFN concepts: Robertson’s disk‑shaped fracture model[Zhang 2025, pp. 1-2]; Fisher distribution for orientation clustering[Zhang 2025, pp. 2-3]; Davy’s power‑law size model[Zhang 2025, pp. 3-6]; and Poisson process for spatial positions[Zhang 2025, pp. 3-6].
- Extends earlier 3DEC‑based Monte Carlo DFN simulations (e.g., Singh et al. 2022, Vyazmensky et al. 2010) by coupling them with intelligent parameter inversion[Zhang 2025, pp. 1-2].
- Contrasts with traditional statistical methods that rely on isotropic assumptions and struggle with tectonic zoning[Zhang 2025, pp. 1-2].
- Relates to machine learning applications in fracture modelling: SVM for orientation‑mechanical correlation[Zhang 2025, pp. 1-2]; deep learning (GAN‑based FracGen, U‑Net, convolutional networks) for fracture detection and reconstruction[Zhang 2025, pp. 1-2].
- Addresses limitations identified in small‑sample machine learning models by using a structured synthetic data library and stratified modeling[Zhang 2025, pp. 1-2].

## Open Questions
- How transferable are the trained neural network models to slopes with different lithologies, tectonic histories, or adit geometries?[Zhang 2025, pp. 24-25]
- Can the geometric DFN be validated against mechanical response (e.g., deformation, failure modes) through coupled DEM simulations and field monitoring?[Zhang 2025, pp. 24-25]
- How can the 2D‑to‑3D ambiguity be further reduced, perhaps by incorporating additional constraints such as multiple viewing angles or in‑situ stress data?
- What is the impact of the homogeneous Poisson location assumption on fracture connectivity, permeability, and rock mass strength, and how can clustering be integrated while maintaining computational tractability?[Zhang 2025, pp. 24-25]
- Is it feasible to extend the methodology to multiple adits or boreholes to improve representativeness and capture large‑scale spatial trends?[Zhang 2025, pp. 24-25]
- How would the method perform with a larger or more diverse training dataset, and what is the minimum number of simulations required for reliable network performance?

## Source Coverage
All 14 non‑empty indexed fragments were processed. Coverage ratio by blocks: 1.0; coverage ratio by characters: 0.992541. Total compiled source characters: 69,457. Source signature: 986c09ba30e0941dbe8feed8b160ea01dc8be23d.
