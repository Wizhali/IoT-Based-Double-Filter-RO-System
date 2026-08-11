
# 💧 IoT-Based Double-Filter RO System

### Smart Water Quality Monitoring and RNN-Based Predictive Analysis

An IoT-enabled water-quality monitoring system that combines a double-filter RO setup, ESP32, water-quality sensors, Flask backend, web dashboard, and an RNN-based machine-learning model for water-quality classification.

---

## 📌 Project Overview

The **IoT-Based Double-Filter RO System** is a final-year academic project designed to monitor important water-quality parameters and provide intelligent water-quality classification.

The system uses an **ESP32** to collect readings from water-quality sensors. The collected sensor values are transmitted through Wi-Fi to a **Flask backend**, where the data is processed and passed to a trained **Recurrent Neural Network (RNN)** model.

The web-based dashboard provides a centralized interface for displaying sensor readings and the predicted water-quality status.

The project integrates **IoT, embedded systems, web technologies, and machine learning** into a single water-quality monitoring solution.

> **Note:** The machine-learning implementation in this repository was reconstructed using the available water-quality dataset and documented project information. The reported ML metrics apply to the reconstructed implementation.

---

## 🎯 Objectives

* Monitor important water-quality parameters.
* Integrate water-quality sensors with an ESP32.
* Transmit sensor readings through Wi-Fi.
* Develop a Flask-based backend API.
* Develop a web-based monitoring dashboard.
* Apply machine learning for water-quality classification.
* Implement an RNN-based prediction model.
* Provide a modular and reproducible project structure.
* Support real-time water-quality monitoring and analysis.

---

## ✨ Key Features

### 🔹 IoT-Based Monitoring

The ESP32 acts as the central IoT controller and collects water-quality readings from connected sensors.

### 🔹 Water-Quality Parameters

The machine-learning pipeline uses four primary input parameters:

* **pH**
* **TDS (ppm)**
* **Turbidity (NTU)**
* **Temperature (°C)**

The hardware design can also incorporate conductivity monitoring.

### 🔹 Wi-Fi Communication

The ESP32 transmits sensor readings to the Flask backend through Wi-Fi.

### 🔹 Flask Backend

The backend provides APIs for:

* Backend health checking
* Receiving water-quality data
* Processing sensor values
* Performing RNN-based prediction
* Returning prediction results

### 🔹 Web Dashboard

The frontend displays:

* pH
* TDS
* Turbidity
* Temperature
* Water-quality prediction
* Unsafe probability
* Backend connection status

### 🔹 Machine Learning

An RNN-based binary-classification model classifies water quality into:

```text
Safe
Unsafe
```

---

# 🏗️ System Architecture

```text
                         WATER INPUT
                             │
                             ▼
                      ┌─────────────┐
                      │   Filter 1  │
                      └──────┬──────┘
                             │
                             ▼
                      ┌─────────────┐
                      │   Filter 2  │
                      └──────┬──────┘
                             │
                             ▼
                       ┌───────────┐
                       │ RO System │
                       └─────┬─────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Water Quality       │
                  │ Sensors             │
                  └──────────┬──────────┘
                             │
                             ▼
                        ┌─────────┐
                        │  ESP32  │
                        └────┬────┘
                             │
                            Wi-Fi
                             │
                             ▼
                    ┌────────────────┐
                    │ Flask Backend  │
                    └───────┬────────┘
                            │
                  ┌─────────┴─────────┐
                  │                   │
                  ▼                   ▼
          ┌──────────────┐     ┌─────────────┐
          │ RNN Model    │     │ Web         │
          │ Prediction   │     │ Dashboard   │
          └──────────────┘     └─────────────┘
```

---

# 🔄 System Workflow

```text
Water
  ↓
Double Filtration
  ↓
RO Purification
  ↓
Sensor Measurement
  ↓
ESP32
  ↓
Wi-Fi Communication
  ↓
Flask API
  ↓
Data Preprocessing
  ↓
Feature Scaling
  ↓
RNN Model
  ↓
Safe / Unsafe Prediction
  ↓
Web Dashboard
```

---

# 🛠️ Technology Stack

## Hardware

* ESP32
* pH sensor
* TDS sensor
* Turbidity sensor
* Temperature sensor
* Conductivity sensor
* RO system
* Double-filter arrangement

## Software

* Arduino IDE
* Embedded C/C++
* Python
* Flask
* HTML5
* CSS3
* JavaScript
* TensorFlow
* Keras
* Scikit-learn
* NumPy

## Machine Learning

* Recurrent Neural Network (RNN)
* Binary Classification
* StandardScaler
* Train/Test Split
* Precision
* Recall
* F1-Score
* ROC-AUC
* Confusion Matrix

---

# 📊 Dataset

The reconstructed machine-learning implementation uses a water-quality dataset containing:

| Property       |         Value |
| -------------- | ------------: |
| Total samples  |       100,800 |
| Input features |             4 |
| Target         |         Label |
| Classes        | Safe / Unsafe |
| Missing values |             0 |
| Duplicate rows |             0 |
| Safe samples   |        30,240 |
| Unsafe samples |        70,560 |

### Input Features

```text
pH
TDS_ppm
Turbidity_NTU
Temperature_C
```

### Target

```text
Safe   → 0
Unsafe → 1
```

### Class Distribution

```text
Safe   → 30%
Unsafe → 70%
```

Because the dataset is imbalanced, model performance is evaluated using multiple metrics rather than accuracy alone.

---

# 🧠 Machine Learning Pipeline

```text
Water Quality Dataset
          ↓
Data Loading
          ↓
Data Validation
          ↓
Label Encoding
          ↓
Train/Test Split
          ↓
Feature Scaling
          ↓
RNN Sequence Preparation
          ↓
RNN Model
          ↓
Model Training
          ↓
Model Evaluation
          ↓
Prediction
```

---

# 🤖 RNN Model Architecture

The implemented model uses a **SimpleRNN-based neural network**.

```text
Input
  │
  ▼
SimpleRNN
64 Units
  │
  ▼
Dropout
  │
  ▼
SimpleRNN
32 Units
  │
  ▼
Dropout
  │
  ▼
Dense
16 Units
  │
  ▼
Dense
1 Unit
  │
  ▼
Safe / Unsafe
```

### Model Summary

| Layer     | Output Shape    | Parameters |
| --------- | --------------- | ---------: |
| SimpleRNN | `(None, 4, 64)` |      4,224 |
| Dropout   | `(None, 4, 64)` |          0 |
| SimpleRNN | `(None, 32)`    |      3,104 |
| Dropout   | `(None, 32)`    |          0 |
| Dense     | `(None, 16)`    |        528 |
| Dense     | `(None, 1)`     |         17 |

### Total Parameters

```text
7,873
```

---

# 📈 Model Training

The dataset was divided using a stratified train/test split.

```text
Training samples → 80,640
Testing samples  → 20,160
```

The RNN was trained with validation monitoring.

The training process achieved very high validation performance, with validation accuracy reaching approximately **99.99%** during training.

---

# 📊 Model Evaluation

The trained RNN model was evaluated on **20,160 test samples**.

| Metric    |  Result |
| --------- | ------: |
| Accuracy  | 100.00% |
| Precision | 100.00% |
| Recall    |  99.99% |
| F1-Score  | 100.00% |
| ROC-AUC   |  1.0000 |

### Classification Report

```text
              precision    recall  f1-score   support

Safe             1.00       1.00      1.00       6048
Unsafe           1.00       1.00      1.00      14112

accuracy                              1.00      20160
macro avg         1.00       1.00      1.00      20160
weighted avg      1.00       1.00      1.00      20160
```

### Confusion Matrix

```text
[[6048,    0],
 [   1, 14111]]
```

The model correctly classified **20,159 out of 20,160** test samples.

> **Important:** These results describe the reconstructed dataset/model implementation in this repository. They should not be presented as measurements from the original final-year project if the original training dataset and model are unavailable.

---

# 🔌 ESP32 Firmware

The ESP32 firmware is located at:

```text
firmware/esp32_water_monitoring.ino
```

The firmware is responsible for:

1. Connecting to Wi-Fi.
2. Reading sensor values.
3. Preparing sensor readings.
4. Sending readings to the Flask backend.
5. Displaying communication information through the Serial Monitor.

Example data:

```json
{
    "ph": 7.38,
    "tds": 138.7,
    "turbidity": 0.25,
    "temperature": 20.25
}
```

Sensor conversion formulas should be calibrated according to the specific sensors used in the physical implementation.

---

# 🌐 Flask Backend

The Flask backend is located at:

```text
backend/app.py
```

## Backend Responsibilities

```text
Receive Input
     ↓
Validate Data
     ↓
Scale Features
     ↓
Load RNN Model
     ↓
Generate Prediction
     ↓
Return JSON Response
```

---

# 📡 API Endpoints

## Health Check

```text
GET /api/health
```

Used to verify that the backend is running.

---

## Water Quality Prediction

```text
POST /api/predict
```

### Example Request

```json
{
    "ph": 7.38,
    "tds": 138.7,
    "turbidity": 0.25,
    "temperature": 20.25
}
```

### Example Response

```json
{
    "status": "success",
    "water_quality": "Safe",
    "unsafe_probability": 0.0001,
    "sensor_data": {
        "pH": 7.38,
        "TDS_ppm": 138.7,
        "Turbidity_NTU": 0.25,
        "Temperature_C": 20.25
    }
}
```

The probability shown above is an example response format. Actual prediction probabilities depend on the trained model and input values.

---

# 🖥️ Web Dashboard

The frontend is located in:

```text
frontend/
├── index.html
├── style.css
└── script.js
```

The dashboard displays:

```text
┌─────────────────────────────────────────┐
│       IoT WATER QUALITY MONITORING      │
├─────────────────────────────────────────┤
│                                         │
│     pH       TDS     Turbidity   Temp   │
│     7.38     138.7      0.25     20.25  │
│                                         │
├─────────────────────────────────────────┤
│                                         │
│          WATER QUALITY                  │
│               SAFE                      │
│                                         │
│        Unsafe Probability               │
│                                         │
└─────────────────────────────────────────┘
```

---

# 📁 Repository Structure

```text
IoT-Based-Double-Filter-RO-System/
│
├── README.md
│
├── firmware/
│   └── esp32_water_monitoring.ino
│
├── backend/
│   ├── app.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── machine-learning/
│   ├── README.md
│   ├── preprocessing.py
│   ├── train_model.py
│   ├── predict.py
│   ├── requirements.txt
│   │
│   └── model/
│       ├── README.md
│       ├── rnn_water_quality.keras
│       └── water_quality_scaler.pkl
│
├── dataset/
│   ├── README.md
│   └── water_quality_dataset.csv
│
├── hardware/
│   ├── README.md
│   └── sensor_connections/
│       └── README.md
│
└── docs/
    └── README.md
```

---

# 🚀 Installation and Setup

## 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>

cd IoT-Based-Double-Filter-RO-System
```

---

## 2. Create Python Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3. Install Backend Dependencies

```bash
pip install -r backend/requirements.txt
```

---

## 4. Start Flask Backend

```bash
python backend/app.py
```

The backend should be available at:

```text
http://127.0.0.1:5000
```

---

## 5. Test Backend Health

Open:

```text
http://127.0.0.1:5000/api/health
```

A successful backend should return a health/status response.

---

## 6. Configure ESP32

Open:

```text
firmware/esp32_water_monitoring.ino
```

Update:

```cpp
const char* WIFI_SSID = "YOUR_WIFI_NAME";
const char* WIFI_PASSWORD = "YOUR_WIFI_PASSWORD";
```

Also configure the Flask server address:

```cpp
const char* SERVER_URL =
    "http://YOUR_COMPUTER_IP:5000/api/predict";
```

Do **not** upload real Wi-Fi credentials to a public GitHub repository.

---

## 7. Upload ESP32 Firmware

Open the firmware using **Arduino IDE**.

Select:

```text
Board → ESP32
Port → Your ESP32 COM Port
```

Compile and upload the firmware.

Open the Serial Monitor at:

```text
115200 baud
```

---

# 🔬 Example Sensor Data

Example input:

```json
{
    "ph": 7.38,
    "tds": 138.7,
    "turbidity": 0.25,
    "temperature": 20.25
}
```

Data flow:

```text
Sensor Values
      ↓
ESP32
      ↓
Wi-Fi
      ↓
Flask API
      ↓
Feature Scaling
      ↓
RNN Model
      ↓
Prediction
      ↓
Dashboard
```

---

# 👥 Team

**Team Size:** 3

This project was developed as a **final-year academic project**.

The project involved work across:

* IoT and ESP32 integration
* Sensor data acquisition
* Backend/API development
* Web dashboard development
* Machine-learning model development
* Testing
* Documentation

---

# 📌 Project Outcome

The project demonstrates the integration of:

```text
IoT
 +
Embedded Systems
 +
Water Quality Monitoring
 +
Machine Learning
 +
Web Technologies
```

The system provides an end-to-end architecture for collecting water-quality parameters, processing the data, performing RNN-based classification, and presenting the prediction through a web dashboard.

---

# 🔮 Future Enhancements

* Add real-time graphical sensor monitoring.
* Add historical water-quality data storage.
* Add database integration.
* Add automatic alerts for unsafe water.
* Improve sensor calibration.
* Add mobile application support.
* Add cloud deployment.
* Add additional water-quality parameters.
* Compare RNN performance with Random Forest, XGBoost, and other classification models.
* Implement continuous real-time prediction from ESP32 sensor readings.
* Add authentication and secure API communication.

---

# ⚠️ Limitations

* Sensor conversion formulas depend on the actual hardware and calibration.
* The reconstructed ML dataset may differ from the original final-year project dataset.
* The reported RNN metrics apply to the reconstructed model and dataset.
* The system is intended for academic and research demonstration.
* The prediction should not be treated as a certified laboratory water-quality test.

---

# 📚 Documentation

Additional project information is organized in:

```text
hardware/
firmware/
backend/
frontend/
machine-learning/
dataset/
docs/
```

Each module can be developed, tested, and maintained independently.

---

# 📜 Project Status

| Component                 | Status        |
| ------------------------- | ------------- |
| Repository structure      | ✅ Complete    |
| Dataset                   | ✅ Available   |
| Dataset preprocessing     | ✅ Complete    |
| RNN model                 | ✅ Trained     |
| Model evaluation          | ✅ Complete    |
| ESP32 firmware            | ✅ Implemented |
| Flask backend             | ✅ Implemented |
| Frontend                  | ✅ Implemented |
| API testing               | ✅ Completed   |
| Hardware calibration      | ✅ Implemented |
| Full hardware integration | ✅ Integrated  |

---

# 🏆 Key Result

The reconstructed RNN model achieved:

```text
Accuracy  : 100.00%
Precision : 100.00%
Recall    : 99.99%
F1 Score  : 100.00%
ROC-AUC   : 1.0000
```

on the held-out test dataset.

Because the reconstructed dataset is highly separable, these metrics should be interpreted cautiously and should not be generalized to real-world water-quality performance without testing on independently collected sensor data.

---

# 🎓 Academic Project

**Project Type:** Final-Year Academic Project

**Team Size:** 3

**Project Title:** IoT-Based Double-Filter RO System

**Domain:** IoT | Embedded Systems | Machine Learning | Water Quality Monitoring

---

# 👩‍💻 Author

**Vishali Raja**

Final-Year Student

**IoT-Based Double-Filter RO System**

---

## ⭐ Acknowledgement

This project was developed as part of a final-year academic project exploring the integration of IoT, embedded systems, machine learning, and web technologies for water-quality monitoring.
