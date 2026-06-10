# Plant Leaf Disease Detector

## Project Structure

leaf-disease-cv/
├── data/
├── src/
├── models/
├── notebooks/
├── requirements.txt
└── verify_gpu.py

## Environment

Python Virtual Environment (venv)

Installed Packages:
- torch
- torchvision
- Pillow
- matplotlib

## PyTorch Environment Verification

PyTorch: 2.12.0+cpu
torchvision: 0.27.0+cpu

CUDA available: False
Tensor device: cpu

## Class Imbalance Summary

Healthy: 1272 training images
Early Blight: 800 training images
Late Blight: 1527 training images
Leaf Mold: 761 training images

Observation:
The dataset is moderately imbalanced. Late Blight has the highest
number of samples (1527), while Leaf Mold has the lowest (761).