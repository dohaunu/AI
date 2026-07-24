# Face Recognition Using PCA and SVM

## Project Overview

This project implements a face classification system using Principal Component Analysis (PCA) and a Support Vector Machine (SVM).

PCA is used to reduce the dimensionality of facial images, while the SVM model is trained to classify faces.

The project uses the Labeled Faces in the Wild (LFW) dataset available through Scikit-learn.

## Features

- Loads the LFW face dataset
- Splits the data into training and testing sets
- Applies PCA for dimensionality reduction
- Reconstructs compressed facial images
- Trains an SVM classifier
- Predicts face identities
- Calculates model accuracy
- Displays a classification report
- Generates a confusion matrix
- Compares original, reconstructed, and predicted images

## Technologies Used

- Python
- NumPy
- Matplotlib
- Scikit-learn
- Seaborn

## Machine Learning Workflow

1. Load the LFW Faces dataset
2. Split the dataset into training and testing data
3. Apply PCA using 150 principal components
4. Transform the training and testing images
5. Train an SVM model with an RBF kernel
6. Predict the identities of the test images
7. Evaluate the model using accuracy and a confusion matrix
8. Visualize the classification results

## Installation

```bash
pip install numpy matplotlib scikit-learn seaborn