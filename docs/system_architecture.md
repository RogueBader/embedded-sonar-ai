# System Architecture

The project aims to develop an embedded AI system for acoustic echo detection and classification.

## Processing Pipeline

External Echosounder
        ↓
Binary Echo Data
        ↓
Python Data Processing
        ↓
Signal Visualization
        ↓
Feature Extraction
        ↓
Dataset Creation
        ↓
PyTorch Model Training
        ↓
Model Deployment
        ↓
Real-Time Classification

## Hardware

- Arduino UNO Q 4GB
- Qualcomm Dragonwing QRB2210
- STM32U585
- External Echosounder

## Software

- Python
- NumPy
- SciPy
- Matplotlib
- PyTorch

## Current Status

Completed:
- Repository setup
- Binary data pipeline
- Signal visualization
- Basic feature extraction

In Progress:
- Dataset acquisition
- Feature engineering

Future Work:
- Model training
- Deployment
- Real-time classification