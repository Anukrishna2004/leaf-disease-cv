# Plant Leaf Disease Detector

## Project Structure

leaf-disease-cv/
│
├── data/
│   ├── train/
│   │   ├── Tomato___healthy/
│   │   ├── Tomato___Early_blight/
│   │   ├── Tomato___Late_blight/
│   │   └── Tomato___Leaf_Mold/
│   │
│   └── val/
│       ├── Tomato___healthy/
│       ├── Tomato___Early_blight/
│       ├── Tomato___Late_blight/
│       └── Tomato___Leaf_Mold/
│
├── src/
│   ├── dataset_loader.py
│   ├── visualize_batch.py
│   └── split_dataset.py
│
├── models/
│
├── notebooks/
│
├── README.md
├── requirements.txt
├── verify_gpu.py
└── .gitignore

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

## Training results
Training Results
CNN trained for 10 epochs.
Training loss reduced from ~0.85 to ~0.17.
Validation loss reduced from ~0.48 to ~0.17.
No significant overfitting observed.
