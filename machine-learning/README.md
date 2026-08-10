# Machine Learning — Water Quality Classification

## Overview

This module contains the machine-learning component of the IoT-Based Double-Filter RO System.

The model uses water-quality parameters collected from the dataset to classify water as:

* **Safe**
* **Unsafe**

A Recurrent Neural Network (RNN) using Keras/TensorFlow was developed for binary classification.

---

## Dataset

The dataset contains:

* **100,800 samples**
* **4 input features**
* **1 binary target**

### Input Features

| Feature         | Description                 |
| --------------- | --------------------------- |
| `pH`            | Acidity/alkalinity of water |
| `TDS_ppm`       | Total Dissolved Solids      |
| `Turbidity_NTU` | Water turbidity             |
| `Temperature_C` | Water temperature           |

### Target

| Label  | Encoding |
| ------ | -------: |
| Safe   |        0 |
| Unsafe |        1 |

### Dataset Distribution

| Class     |     Samples | Percentage |
| --------- | ----------: | ---------: |
| Safe      |      30,240 |        30% |
| Unsafe    |      70,560 |        70% |
| **Total** | **100,800** |   **100%** |

The dataset contains no missing values or duplicate rows according to the dataset analysis.

---

## Data Preprocessing

The following preprocessing steps were applied:

1. Load the dataset using Pandas.
2. Remove unnecessary whitespace from column names and labels.
3. Encode `Safe` as `0`.
4. Encode `Unsafe` as `1`.
5. Separate input features and target.
6. Perform an 80/20 stratified train-test split.
7. Apply `StandardScaler`.
8. Reshape the scaled data for RNN input.

### Dataset Split

```text
Total samples:       100,800
Training samples:     80,640
Testing samples:      20,160
```

### RNN Input Shape

```text
(80640, 4, 1)
```

The four water-quality features are represented as the sequence dimension for the RNN implementation.

---

## RNN Architecture

The implemented model contains:

```text
Input
  ↓
SimpleRNN (64 units)
  ↓
Dropout (20%)
  ↓
SimpleRNN (32 units)
  ↓
Dropout (20%)
  ↓
Dense (16 units, ReLU)
  ↓
Dense (1 unit, Sigmoid)
```

### Model Parameters

**Total parameters:** 7,873

**Trainable parameters:** 7,873

### Configuration

| Parameter         | Value               |
| ----------------- | ------------------- |
| Optimizer         | Adam                |
| Loss              | Binary Crossentropy |
| Output activation | Sigmoid             |
| Batch size        | 64                  |
| Maximum epochs    | 30                  |
| Early stopping    | Enabled             |
| Random state      | 42                  |

---

## Model Training

The model was trained using:

* 80% training data
* 20% held-out test data
* 20% of the training data used for validation
* Early stopping based on validation loss

Training stopped after the validation performance stopped improving.

---

## Evaluation Results

The final model was evaluated on the **20,160-sample held-out test set**.

| Metric    |      Result |
| --------- | ----------: |
| Accuracy  | **100.00%** |
| Precision | **100.00%** |
| Recall    |  **99.99%** |
| F1-Score  | **100.00%** |
| ROC-AUC   |  **1.0000** |

### Confusion Matrix

```text
                Predicted
              Safe   Unsafe

Actual Safe    6048      0
Actual Unsafe     1  14111
```

The model correctly classified **20,159 of 20,160 test samples**, with one Unsafe sample classified as Safe.

---

## Model Files

The trained model and preprocessing scaler are stored in:

```text
model/
├── rnn_water_quality.keras
└── water_quality_scaler.pkl
```

### Model

`rnn_water_quality.keras`

Contains the trained TensorFlow/Keras RNN model.

### Scaler

`water_quality_scaler.pkl`

Contains the `StandardScaler` fitted during training.

The same scaler must be used when preprocessing new sensor readings before prediction.

---

## Prediction

The `predict.py` script loads the trained model and scaler.

Example input:

```python
ph = 7.38
tds = 138.7
turbidity = 0.25
temperature = 20.25
```

The prediction pipeline is:

```text
New Sensor Values
       ↓
StandardScaler
       ↓
RNN Input Reshaping
       ↓
Trained RNN
       ↓
Probability
       ↓
Safe / Unsafe
```

---

## Files

```text
machine-learning/
│
├── README.md
├── preprocessing.py
├── train_model.py
├── predict.py
├── requirements.txt
│
└── model/
    ├── README.md
    ├── rnn_water_quality.keras
    └── water_quality_scaler.pkl
```

---

## Important Note About Results

The reported metrics are results obtained from the held-out test set of the reconstructed public dataset.

The **100% test accuracy should not be interpreted as guaranteed real-world accuracy** for every water source or sensor environment. The dataset has strong class separation, and further validation using independent real-world sensor measurements would be appropriate before deployment.

---

## Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* TensorFlow
* Keras
* Joblib

---

## Next Integration

The trained model can be integrated with the Flask backend so that live ESP32 sensor readings can be passed through the same preprocessing pipeline and classified as Safe or Unsafe.


