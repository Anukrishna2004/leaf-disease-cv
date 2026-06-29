# Leaf Disease Detection using Deep Learning

## 1. Dataset & Agritech Problem

Tomato leaf diseases significantly reduce crop yield and quality when not detected early. Manual disease identification is time-consuming and requires expert knowledge. This project develops a deep learning-based system to automatically classify tomato leaf images into four categories: Healthy, Early Blight, Late Blight, and Leaf Mold.

The dataset consists of labeled tomato leaf images organized into training, validation, and test sets. Images were resized to 224 × 224 pixels and normalized using ImageNet mean and standard deviation. Data augmentation techniques such as random horizontal flip, random rotation, random resized crop, and color jitter were applied during training to improve model generalization.

---

## 2. Architecture & Training Choices

A custom CNN model and a transfer learning approach using ResNet18 were explored. The final model uses a pretrained ResNet18 architecture with the final fully connected layer replaced to classify four disease categories.

Training configuration:

* Optimizer: Adam
* Loss Function: CrossEntropyLoss
* Learning Rate: 0.001
* Batch Size: 32
* Epochs: 10
* Early Stopping with patience of 3 epochs
* Best model saved based on validation loss

Data augmentation was enabled to reduce overfitting and improve robustness.

---

## 3. Metrics & Error Analysis

The trained model was evaluated using validation and test datasets.

Evaluation methods included:

* Accuracy
* Classification Report (Precision, Recall, F1-score)
* Confusion Matrix
* Misclassified Image Review

Most prediction errors occurred between visually similar disease classes such as Early Blight and Late Blight. These diseases exhibit overlapping symptoms, making classification more challenging. Data augmentation helped reduce overfitting and improved validation performance.

---

## 4. API Deployment

The trained model was exported for inference and deployed using FastAPI.

Available API endpoints:

* GET `/health`
* POST `/predict`

The `/predict` endpoint accepts an uploaded tomato leaf image and returns:

* Predicted class
* Confidence score
* Inference time (milliseconds)

The application was containerized using Docker.

Deployment files include:

* Dockerfile
* .dockerignore
* DEPLOY.md

The API was successfully tested using Swagger UI at:

`http://localhost:8000/docs`

---

## 5. Ethics and Privacy for Field Imagery

Although plant leaf images generally do not contain personal information, care should be taken when collecting images in agricultural fields to avoid capturing identifiable individuals or private property.

The model should be used as a decision-support tool rather than a replacement for agricultural experts. Predictions should be verified before applying pesticides or taking crop management decisions.

Future improvements include:

* Support for additional crop diseases
* Mobile application deployment
* Larger and more diverse datasets
* Real-time field inference using edge devices

---

# Conclusion

This project demonstrates an end-to-end deep learning pipeline for automated tomato leaf disease detection. The workflow includes dataset preparation, preprocessing, CNN and ResNet18 model training, evaluation, prediction, FastAPI deployment, and Docker containerization. The developed system provides a scalable and efficient solution for assisting farmers in early disease detection and crop health monitoring.
