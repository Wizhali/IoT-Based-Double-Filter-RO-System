# Hardware Documentation

## Project

**IoT-Based Double-Filter RO System**

### Smart RO Water Quality Monitoring and Disease Prediction System

This folder contains the hardware-related documentation, sensor information, circuit connections, and implementation details of the IoT-based RO water monitoring system.

---

## Hardware Components

| Component           | Purpose                          |
| ------------------- | -------------------------------- |
| ESP32               | Main IoT microcontroller         |
| pH Sensor           | Measures water pH                |
| TDS Sensor          | Measures total dissolved solids  |
| Turbidity Sensor    | Measures water clarity           |
| Temperature Sensor  | Measures water temperature       |
| Conductivity Sensor | Measures electrical conductivity |
| RO System           | Water purification               |
| Double Filter Unit  | Additional filtration stage      |
| Connecting Wires    | Electrical connections           |
| Power Supply        | Provides power to the system     |

---

## Hardware Architecture

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
              ┌─────────────┐
              │ RO System   │
              └──────┬──────┘
                     │
                     ▼
          ┌──────────────────────┐
          │ Water Quality Sensors│
          │ pH                   │
          │ TDS                  │
          │ Turbidity            │
          │ Temperature          │
          │ Conductivity         │
          └──────────┬───────────┘
                     │
                     ▼
                ┌────────┐
                │ ESP32  │
                └────┬───┘
                     │
                  Wi-Fi
                     │
                     ▼
              Backend / Dashboard
```

---

## Sensor Monitoring

The ESP32 collects water-quality parameters from the connected sensors.

The monitored parameters include:

* pH
* TDS
* Turbidity
* Temperature
* Conductivity

The collected readings are transmitted for real-time monitoring and further analysis.

---

## Hardware Implementation

The physical prototype consists of the RO purification system, double-filter arrangement, water-quality sensors, and ESP32-based IoT monitoring unit.

Actual circuit diagrams, sensor photographs, and prototype images are maintained in the corresponding folders of this repository.

---

## Important Note

Sensor pin numbers, electrical connections, calibration formulas, and operating ranges should be documented according to the actual hardware components used in the project.

