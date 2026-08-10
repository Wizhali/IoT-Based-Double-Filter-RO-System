
# 💧 IoT-Based Double-Filter RO System

### Smart Water Quality Monitoring and Predictive Analysis

An IoT-enabled water-quality monitoring system that integrates an ESP32, water-quality sensors, Flask backend, web dashboard, and RNN-based machine-learning analysis.

---

## 📌 Project Overview

The **IoT-Based Double-Filter RO System** is a smart water-monitoring solution developed as a final-year academic project.

The system combines a double-filter RO setup with IoT-based sensing to monitor important water-quality parameters. Sensor readings are collected using an ESP32 and transmitted through Wi-Fi to a Flask backend.

A web dashboard provides a centralized interface for viewing the collected water-quality information.

The project also includes an **RNN-based machine-learning module** for predictive analysis.

> **Note:** The original project dataset and RNN implementation were lost. The machine-learning section of this repository is being reconstructed using a documented public replacement dataset. It should not be interpreted as the exact original training setup.

---

## 🎯 Objectives

* Monitor water-quality parameters in real time.
* Integrate water-quality sensors with an ESP32.
* Transmit sensor readings using Wi-Fi.
* Provide a web-based monitoring dashboard.
* Analyze collected water-quality data.
* Integrate an RNN-based predictive-analysis module.
* Create a modular and reproducible project structure.

---

## ✨ Key Features

### 🔹 IoT Monitoring

The ESP32 collects water-quality readings from connected sensors.

### 🔹 Water Quality Parameters

The system is designed to monitor:

* pH
* TDS
* Turbidity
* Temperature
* Conductivity

### 🔹 Real-Time Communication

Sensor data can be transmitted from the ESP32 to the Flask backend through Wi-Fi.

### 🔹 Web Dashboard

The frontend provides a simple interface for displaying:

* Current pH
* TDS
* Turbidity
* Temperature
* Conductivity
* Water-quality status
* Alerts
* Last updated time

### 🔹 Machine Learning

An RNN-based module is included for predictive analysis using water-quality data.

---

## 🏗️ System Architecture

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
              ┌───────────────────┐
              │ Water Quality     │
              │ Sensors           │
              └─────────┬─────────┘
                        │
                        ▼
                   ┌─────────┐
                   │  ESP32  │
                   └────┬────┘
                        │
                      Wi-Fi
                        │
                        ▼
                ┌──────────────┐
                │ Flask Backend│
                └──────┬───────┘
                       │
              ┌────────┴────────┐
              │                 │
              ▼                 ▼
       ┌────────────┐    ┌─────────────┐
       │ ML / RNN   │    │ Web         │
       │ Prediction │    │ Dashboard   │
       └────────────┘    └─────────────┘
```

---

## 🔄 System Workflow

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
Wi-Fi
  ↓
Flask API
  ↓
Data Processing
  ↓
RNN Analysis
  ↓
Dashboard
```

---

## 🛠️ Technology Stack

### Hardware

* ESP32
* pH sensor
* TDS sensor
* Turbidity sensor
* Temperature sensor
* Conductivity sensor
* RO system
* Double-filter arrangement

### Software

* Arduino IDE
* Embedded C/C++
* Python
* Flask
* HTML5
* CSS3
* JavaScript
* TensorFlow/Keras
* Recurrent Neural Network (RNN)

---

## 📁 Repository Structure

```text
IoT-Based-Double-Filter-RO-System/
│
├── README.md
│
├── firmware/
│   └── esp32_water_monitoring.ino
│
├── hardware/
│   ├── README.md
│   └── sensor_connections/
│       └── README.md
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
│   └── README.md
│
├── dataset/
│   └── README.md
│
└── docs/
    └── README.md
```

---

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd IoT-Based-Double-Filter-RO-System
```

### 2. Create a Python virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install backend dependencies

```bash
pip install -r backend/requirements.txt
```

### 4. Start Flask

```bash
python backend/app.py
```

The backend runs on:

```text
http://localhost:5000
```

### 5. Configure ESP32

Open:

```text
firmware/esp32_water_monitoring.ino
```

Update the Wi-Fi credentials and backend server address according to your local network.

---

## 📊 API

### GET latest water-quality data

```text
GET /api/water-data
```

### POST water-quality data

```text
POST /api/water-data
```

Example JSON:

```json
{
    "ph": 7.2,
    "tds": 320,
    "turbidity": 2.1,
    "temperature": 27.5,
    "conductivity": 410
}
```

---

## 🤖 Machine Learning

The project contains an RNN-based machine-learning module.

### Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Preprocessing
   ↓
Feature Scaling
   ↓
Sequence Preparation
   ↓
RNN
   ↓
Training
   ↓
Evaluation
   ↓
Prediction
```

The original project dataset was unavailable during reconstruction. Therefore, the repository will document the replacement public dataset separately.

**Actual model metrics will be reported only after training the reconstructed model.**

---

## 👥 Team

**Team Size:** 3

This was developed as a final-year academic project.

---

## 📚 Documentation

Detailed documentation is available in:

* [`hardware/`](hardware/)
* [`firmware/`](firmware/)
* [`backend/`](backend/)
* [`frontend/`](frontend/)
* [`machine-learning/`](machine-learning/)
* [`dataset/`](dataset/)
* [`docs/`](docs/)

---

## ⚠️ Disclaimer

This project is intended for academic and research purposes.

Machine-learning predictions should not be interpreted as medical diagnosis or professional medical advice.

---

## 📌 Project Status

| Component                | Status            |
| ------------------------ | ----------------- |
| Repository structure     | ✅                 |
| Hardware documentation   | ✅                 |
| ESP32 firmware structure | ✅                 |
| Flask backend            | ✅                 |
| Web dashboard            | ✅                 |
| ML documentation         | ✅                 |
| Dataset                  | 🔄 Reconstruction |
| RNN implementation       | 🔄 Reconstruction |
| Model evaluation         | 🔄 Pending        |
| Final integration        | 🔄 Pending        |

---

## 👩‍💻 Author

**Vishali Raja**

Final Year Academic Project

**IoT-Based Double-Filter RO System**
