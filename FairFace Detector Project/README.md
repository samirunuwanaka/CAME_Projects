# FairVision - Detecting and Mitigating Bias in CNN Age Classification

![Streamlit Application Dashboard Dynamic Preview](streamlit%20app.png)

An end-to-end Deep Learning and computer vision project focused on analyzing, detecting, and mitigating demographic bias (gender, race, ethnicity) within a Convolutional Neural Network (CNN) trained for age group classification. Built using **PyTorch**, **Hugging Face Datasets (FairFace)**, and **Streamlit** for interactive model evaluation and demographic transparency.

---

## 📌 Repository Overview

CAME (Complete AI & Model Engineering) is an end-to-end machine learning repository that demonstrates the full lifecycle of an AI system — from data preprocessing to model deployment and fairness evaluation.

This project focuses on building **robust, modular, and responsible AI systems**, combining model performance with critical ethical considerations such as bias detection and algorithmic mitigation.

### 🎯 Key Objectives
- Develop a complete, production-ready **AI/ML pipeline**.
- Build customized **CNN architectures from scratch** without relying on pre-trained transfer learning weights.
- Evaluate model classification thresholds comprehensively across **different demographic groups**.
- Detect, isolate, and structurally **reduce systemic bias in predictions**.
- Maintain a **clean, scalable project workspace**.

### 🧠 Core Features
- Complete ML workflow loop (data ingestion → structural preprocessing → model tuning → local deployment).
- Deep Convolutional Neural Network custom blueprint tailored for multi-class facial image frames.
- Algorithmic bias mitigation modules (dynamic class weighting, statistical data balancing).
- High-reusability modular codebase separating runtime interfaces from underlying tensor layers.

---

## 📂 Project Architecture

The directory structure organizes model definition assets, training configurations, cached model checkpoints, and datasets across local directories:

```text
├── .devcontainer/
│   └── devcontainer.json            # Visual Studio Code development container configurations
├── dataset/
│   └── HuggingFaceM4___fair_face/   # FairFace dataset storage (Hugging Face format)
│       └── 0.25/0.0.0/54d573cdb8b5af490ba8da9da2799628f6e5c496/
│           ├── cache-*.arrow         # Arrow format execution cache files
│           ├── dataset_info.json     # Metadata structure describing dataset splits
│           ├── fair_face-train-*.arrow # Localized high-fidelity training shards
│           └── fair_face-validation.arrow # Standalone validation tracking matrix
├── fairface_sample/
│   ├── labels.csv                   # Structured CSV file pairing images with annotations
│   └── images/                      # Directory of local sample images for verification
│       ├── img_0.jpg
│       └── ... (img_1.jpg to img_9.jpg)
├── .gitignore                       # File ignoring local caches, state trackers, and binaries
├── best_fairface_model.pt           # Final serialized PyTorch model weight parameters
├── CAME_ Individual Assignment Brief_ FairVision ... .pdf # Assignment specification guidelines
├── FairVision.ipynb                 # Interactive Jupyter Notebook for exploratory analysis and training
├── MLModel.py                       # PyTorch source script containing the custom CNN blueprint
├── README.md                        # Documentation entry point
├── requirements.txt                 # Exact external package dependencies
├── streamlit_app append.py          # Modified backend extension adjustments
└── streamlit_app.py                 # Core production-ready user interface deployment file
```

### Module Breakdown
* **`MLModel.py`**: Defines the Convolutional Neural Network architecture in PyTorch. Implements customized forward execution paths to predict age groups while providing hooks to extract latent features for demographic parity tracking.
* **`FairVision.ipynb`**: Contains structural research routines including data balancing operations, bias metric evaluation loops (e.g., disparate impact ratio, equalized odds), model training, and optimization.
* **`streamlit_app.py`**: Operates as a dashboard interface that processes uploaded user images or sample files, outputs CNN classification metrics, and displays live bias telemetry charts across different intersectional demographic slices.

---
## 📊 Dataset Specifications

**Dataset Used:** FairFace (Hugging Face Configuration: 0.25)
🔗 https://huggingface.co/datasets/HuggingFaceM4/FairFace

### Data Breakdown & Splits
- **Total Ingested Samples:** ~97,698 images
- **Training Set Split:** 86,744 images
- **Validation Set Split:** 10,954 images
- **Physical Shape:** 224 × 224 pixels (RGB color space)

### Labels & Target Variables
* **Age Groups (9 Target Classes):** `0–2`, `3–9`, `10–19`, `20–29`, `30–39`, `40–49`, `50–59`, `60–69`, `70+`
* **Demographic Attributes (Fairness Analysis):**
  - **Race:** 7 categorized groups (White, Black, Latino, East Asian, Southeast Asian, Indian, Middle Eastern)
  - **Gender:** Binary tracking vectors (`Male`, `Female`)

---

## 🛠️ Installation & Virtual Environment Setup

This workflow is optimized to execute deterministically within a dedicated environment using **PowerShell** on **Windows**.

### 1. Initialize Project Environment
Open your PowerShell console, change directory to your core execution workspace path, and build your isolated virtual environment:

```powershell
# Navigate into the project folder
cd "D:\"

# Build an isolated Python virtual runtime workspace
python -m venv .venv

# Adjust system execution permissions for the local process terminal instance
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Activate the local virtual path script
.\.venv\Scripts\Activate.ps1
```

### 2. Install Package Dependencies
Execute batch installation parameters to ingest computer vision modules, web-rendering architectures, data optimization layers, and PyTorch components:

```powershell
pip install -r requirements.txt
```

*Note: If requirements.txt is empty or missing specific targets, fallback manually to the foundational pipeline tools:*
```powershell
pip install torch torchvision torchaudio streamlit pandas numpy matplotlib datasets pyarrow scikit-learn seaborn
```

---

## ⚙️ Technical Blueprint & Pipeline Workflow

### 🔄 The System Pipeline Flow
``text
Data Collection (FairFace Dataset)
       ⬇️
Data Preprocessing (Face Alignment, Multi-Class Binning, Augmentations)
       ⬇️
Model Design (Custom CNN Architecture via PyTorch from Scratch)
       ⬇️
System Training (Adam Optimizer, CrossEntropyLoss, Bias-Adjusted Loops)
       ⬇️
Rigorous Evaluation (Intersectional Group Performance Checks & Auditing)
       ⬇️
Local Deployment (Interactive Streamlit Web App Interface)
```

### 🧠 Model Architecture Blueprint
A custom deep convolutional neural network built natively from scratch in PyTorch without pre-trained model transfer-learning dependencies:

```text
Input Image (224x224x3 Matrix)
       ⬇️
Convolutional Layer (Feature Mapping) + ReLU Activation
       ⬇️
Max Pooling Layer (Spatial Downsampling)
       ⬇️
Convolutional Layer (Deep Feature Abstraction) + ReLU Activation
       ⬇️
Max Pooling Layer (Spatial Downsampling)
       ⬇️
Fully Connected Dense Layers (Classification Flattening Layer)
       ⬇️
Softmax Activation Layer Output (Produces Probabilities across 9 Age Classes)
```

---

### 📊 Comprehensive Evaluation Engine
The system measures classification accuracy alongside absolute fairness parameters through automated routines processing:
- Overall Accuracy metrics.
- Intersectional Precision, Recall, and F1-Scores.
- Segmented Confusion Matrices.
- Group-wise classification parity across distinct demographic buckets.

### ⚖️ Fairness & Bias Mitigation System
To counteract real-world data collection imbalances, the script incorporates active algorithmic mitigation methods:
- **Demographic-based Evaluation**: Explicit performance metrics tracked per protected attribute subset.
- **Bias Detection**: Mathematical scoring of Disparate Impact and Equalized Odds variance.
- **Active Structural Mitigation**:
  - *Class Weighting*: Penalty scaling inside loss functions based on demographic sample frequencies.
  - *Oversampling*: Enhancing low-density group visibility across training iterations.
  - *Balanced Batch Training*: Enforcing demographic equilibrium inside forward steps.

---

## 💻 Running the Interactive Dashboard

Once your environment variables and dependency weights are established, execute the local Streamlit dashboard application to audit the CNN age prediction models.

```powershell
# Run the core dashboard utility script
streamlit run streamlit_app.py
```

*Application Verification Features:*
* **Image Evaluation Hook**: Upload raw images or pick from the localized sample path (`fairface_sample/images/`).
* **CNN Classification Analysis**: Decodes age brackets (e.g., 0-2, 3-9, 10-19, 20-29, etc.) alongside evaluation prediction confidence intervals.
* **Bias Profiling Summary**: Compares confusion matrices across available protected variables to confirm equalized odds compliance.

---

## 📈 System Metrics & Practical Guardrails

### Project Results
- Delivers robust baseline classification capability across targeted image validation frames.
- Exposes clear, quantifiable trade-offs between optimization targets and demographic fairness thresholds.

### 📌 Targeted Use Cases
- High-fidelity computer vision validation systems.
- Responsible, transparent AI engineering research.
- Biomedical and electronic framework implementations.

### ⚠️ Known Operational Limitations
- Overall validation performance depends closely on the clean ingestion of initial input datasets.
- Minor residual bias variances may still manifest when processing completely unseen out-of-distribution faces.
- Configured for local evaluation architectures (not intended for production commercial cloud systems).

### 🧭 Ethical Compliance Framework
- Actively seeks to enforce and improve predictive fairness across all protected attributes.
- Inhibits structural misuse within sensitive or facial-tracking diagnostic settings.
- Maintains deep internal transparency by printing verifiable prediction probabilities.

---

## 👨‍💻 Author Profile

**Nuwanaka WAS** University of Moratuwa  
Biomedical / Electronic Engineering  

---

## ⭐ Final Note
CAME is designed to demonstrate how modern AI systems should be built — prioritizing not only mathematical performance accuracy, but also architectural fairness, clean modular scaling, and responsible real-world development impact.