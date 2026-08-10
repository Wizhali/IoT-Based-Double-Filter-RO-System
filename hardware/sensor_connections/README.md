
# Sensor Connections

## Overview

The ESP32 is used as the main microcontroller for collecting water-quality data from the connected sensors.

The project monitors:

* pH
* TDS
* Turbidity
* Temperature
* Conductivity

---

# Sensor-to-ESP32 Connection

| Sensor              | Parameter    | ESP32 GPIO        | Power      | Output            |
| ------------------- | ------------ | ----------------- | ---------- | ----------------- |
| pH Sensor           | pH           | **To be updated** | 3.3V / 5V* | Analog            |
| TDS Sensor          | TDS          | **To be updated** | 3.3V / 5V* | Analog            |
| Turbidity Sensor    | Turbidity    | **To be updated** | 3.3V / 5V* | Analog            |
| Temperature Sensor  | Temperature  | **To be updated** | 3.3V / 5V* | Digital / Analog* |
| Conductivity Sensor | Conductivity | **To be updated** | 3.3V / 5V* | Analog            |

> **Important:** Replace the GPIO and power values with the actual connections used in the physical prototype.

---

## ESP32 Responsibilities

The ESP32 performs the following tasks:

1. Initializes the connected sensors.
2. Reads sensor values.
3. Processes the collected readings.
4. Connects to the Wi-Fi network.
5. Transmits the collected data to the backend.
6. Supports real-time water-quality monitoring.

---

## Data Flow

```text
pH Sensor ───────────┐
TDS Sensor ──────────┤
Turbidity Sensor ────┤
Temperature Sensor ──┤──→ ESP32 ──→ Wi-Fi ──→ Backend
Conductivity Sensor ─┘
```

---

## Calibration

Each sensor should be calibrated according to its specific model and the calibration procedure used during the project implementation.

The final repository should contain the actual calibration values and formulas used in the prototype.

---

## Hardware Photos

Add actual sensor and wiring photographs here when available.

Example:

```text
images/
├── sensor_setup.jpg
├── esp32_connections.jpg
└── prototype.jpg
```

---

## Safety Note

Verify sensor operating voltage and ESP32 input-voltage limits before making physical connections. Do not connect a sensor output to an ESP32 GPIO if its voltage exceeds the GPIO's permitted input range.
