# CAME Projects  
## Complete AI & Model Engineering Portfolio

CAME (**Complete AI & Model Engineering**) is a collection of end-to-end Artificial Intelligence and software engineering projects demonstrating modern approaches to building intelligent systems.

This repository acts as the parent workspace for multiple independent AI applications maintained as Git submodules. Each project focuses on different areas of AI engineering, including **Computer Vision, Responsible AI, Multi-Agent Systems, Generative AI, and Intelligent Web Applications**.

---

# 📂 Repository Structure

```text
CAME Projects/
│
├── FairFace Detector/
│   └── FairVision - CNN Age Classification Bias Analysis
│
└── Travelling Agent for plan your tour/
    └── AeroTrip AI - Multi-Agent Travel Planner
```

## 🚀 Projects
#### 🧠 FairVision
Detecting and Mitigating Bias in CNN Age Classification

FairVision is an end-to-end Deep Learning and Computer Vision project focused on analyzing and reducing demographic bias in facial age classification models.

The system uses a custom Convolutional Neural Network trained with the FairFace dataset to investigate model behavior across different demographic groups and provide transparency through fairness evaluation.

##### Key Features
Custom CNN architecture built from scratch using PyTorch
FairFace dataset integration
Age group classification across 9 categories
Demographic bias analysis
Fairness metric evaluation
Bias mitigation techniques:
Class weighting
Oversampling
Balanced training strategies
Interactive Streamlit evaluation dashboard
Technology Stack
Python
PyTorch
Hugging Face Datasets
Streamlit
NumPy
Pandas
Scikit-learn
Matplotlib

##### 📁 Project Location:

FairFace Detector/


For complete implementation details, setup instructions, architecture, and evaluation results, refer to:

FairFace Detector/README.md

#### ✈️ AeroTrip AI
Multi-Agent Travel Planner & Logistics Suite

AeroTrip AI is an intelligent travel planning platform powered by Google Agent Development Kit (ADK 2.0).

The system uses a multi-agent architecture where specialized AI agents collaborate to generate travel plans, verify requirements, analyze logistics, and provide an interactive travel assistant experience.

##### Key Features

Flight Planning Agent

Flight route discovery
Airline comparison
Schedule analysis
Travel prerequisite verification

Places Explorer Agent

Tourist attraction discovery
Cultural recommendations
Restaurant and activity suggestions

Travel Guardrails Engine

Destination validation
Budget feasibility checks
Trip duration verification
Travel advisory handling

##### Prerequisite Verification System

Passport checks
Visa requirements
Health requirements
Insurance verification

Modern AI Dashboard

Glassmorphism interface
Agent activity monitoring
Interactive itinerary visualization
Budget analysis
Technology Stack
Python
Google Agent Development Kit (ADK)
Google Gemini API
FastAPI
HTML / CSS / JavaScript
Pytest

📁 Project Location:

Travelling Agent for plan your tour/


For complete architecture, installation, and usage instructions, refer to:

Travelling Agent for plan your tour/README.md

##### 🎯 Project Goals

CAME demonstrates the complete lifecycle of modern AI system development:

Research
   ↓
Data Processing
   ↓
Model / Agent Development
   ↓
Evaluation
   ↓
Optimization
   ↓
Deployment
   ↓
User Interaction


##### The projects emphasize:

✅ Scalable AI architecture
✅ Responsible AI development
✅ Modular engineering practices
✅ Real-world deployment workflows
✅ Explainability and transparency
🛠️ Common Technologies

##### The CAME portfolio uses a combination of:

Category	Technologies
Programming	Python
Deep Learning	PyTorch
Generative AI	Google Gemini
Agent Frameworks	Google ADK
Computer Vision	CNN, FairFace Dataset
Web Applications	Streamlit, FastAPI
Data Processing	NumPy, Pandas
Machine Learning	Scikit-learn
Testing	Pytest
Version Control	Git Submodules
📦 Clone Repository

Clone the repository including all project submodules:
```bash
git clone --recurse-submodules <repository-url>
```

If the repository was cloned without submodules:
```bash
git submodule update --init --recursive
```
🔄 Updating Projects

Update all submodules:
```bash
git submodule update --remote --merge
```

Update an individual project:
```bash
cd "FairFace Detector"
git pull origin main
```

or
```bash
cd "Travelling Agent for plan your tour"
git pull origin main
```
📚 Documentation

Each project maintains independent documentation covering:

Installation instructions
Dependencies
Architecture
Usage guides
Project workflow
Technical implementation
Results and evaluation

Navigate into each project folder for detailed information.

👨‍💻 Author

Samiru Nuwanaka

University of Moratuwa
Biomedical / Electronic Engineering

GitHub:
https://github.com/samirunuwanaka

⭐ About CAME

CAME represents a practical exploration of modern AI engineering — combining machine learning research, responsible AI principles, intelligent agents, and software development practices into complete working systems.

The objective is to build AI solutions that are not only accurate, but also transparent, scalable, maintainable, and useful in real-world applications.
