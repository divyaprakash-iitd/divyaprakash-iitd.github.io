---
title: "Machine Learning-Based Estimation of Superdroplet Growth Rates"
excerpt: "A Python-based machine learning framework for parameterizing superdroplet growth in cloud microphysics models, leveraging high-fidelity Direct Numerical Simulation (DNS) data.<br/><img src='/images/cloud_py.webp' alt='Superdroplet growth: machine learning model compared with DNS data' loading='lazy'>"
collection: portfolio
date: 2024-10-12
---

## Project Overview
Droplet growth and size spectra play a crucial role in the microphysics of atmospheric clouds. However, it is challenging to represent droplet growth rate accurately in cloud-resolving models such as Large Eddy Simulations (LESs). To overcome the limitations of the "well-mixed" assumption in traditional LES solvers, this project proposes a parameterization for superdroplet growth using high-fidelity Direct Numerical Simulation (DNS) data. A novel clustering algorithm maps droplets in DNS fields to superdroplets, and a machine learning model is developed to relate the effective growth rate of these superdroplets to filtered DNS flow variables.

## Key Features
- **Advanced Data Processing**: Ingests and transforms raw Lagrangian and Eulerian data from DNS simulations into a structured format for machine learning.
- **Feature Engineering**: Implements multiple scaling methods to extract and prepare features and labels for model training.
- **Machine Learning Model**: Trains and validates a model to predict the effective supersaturation for superdroplets, achieving a promising R² value of nearly 0.9.
- **A Posteriori Analysis**: Includes scripts for evaluating the model's performance and generalization on unseen data.
- **Modular Workflow**: The project is organized into distinct stages: post-processing, training, and a posteriori analysis.

## Technical Details
- **Language**: Python
- **Core Modules**:
  - `post-processing`: Scripts for data ingestion and transformation.
  - `training`: Scripts for feature extraction, model training, and validation.
  - `aposteriori`: Scripts for a posteriori analysis and performance evaluation.

## Publication
The findings and methodologies of this project are detailed in a preprint available on arXiv:
[https://arxiv.org/abs/2410.13890](https://arxiv.org/abs/2410.13890)

## Technical Documentation
[GitHub Repository](https://github.com/divyaprakash-iitd/cloud_py/tree/main)
