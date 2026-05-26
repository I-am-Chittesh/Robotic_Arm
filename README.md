#  Robotic Arm Digital Twin (IoT & MQTT)

![Hardware](https://img.shields.io/badge/Hardware-ESP32--S3-orange)
![Language](https://img.shields.io/badge/Language-C++_%7C_Python-blue)
![Protocol](https://img.shields.io/badge/Protocol-MQTT_(HiveMQ)-green)
![Status](https://img.shields.io/badge/Status-Active_Development-brightgreen)

## Project Overview
This project implements a fully bidirectional **Digital Twin** for a 3-axis robotic arm (Base, Shoulder, and Elbow). By leveraging an ESP32-S3 microcontroller and a cloud-based MQTT broker (HiveMQ), this system allows for real-time, low-latency synchronization between the physical hardware and a digital environment.

Commands sent from the local Python dashboard are instantly packaged into JSON payloads, routed securely through the cloud broker, and executed by the physical servos.

## Core Features
* **Bidirectional Synchronization:** Control the physical arm via a digital interface, or stream telemetry from the arm back to the digital twin.
* **Low-Latency Cloud Routing:** Utilizes HiveMQ Cloud with TLS/SSL encryption for secure, real-time message brokering over Port 8883.
* **JSON Payload Parsing:** Efficiently handles multi-axis commands (e.g., `{"base": 90, "shoulder": 45, "elbow": 135}`) directly on the edge device.
* **Hardware-Agnostic Dashboard:** The Python command layer can easily be expanded into a Unity 3D visualization or machine learning pipeline.

---

## Hardware Architecture

### Components Used
* **Microcontroller:** ESP32-S3 WROOM
* **Actuators:** 3x Standard RC Servo Motors
* **Power:** External 5V supply (Recommended for physical deployment)

### Pin Configuration (ESP32-S3)
| Component | ESP32-S3 Pin | Purpose |
| :--- | :--- | :--- |
| **Base Servo** | `GPIO 4` | Controls horizontal rotation |
| **Shoulder Servo**| `GPIO 5` | Controls primary vertical lift |
| **Elbow Servo** | `GPIO 6` | Controls secondary vertical reach |
| **Power (Red)** | `3V3` / `VIN`| Standard 3.3V/5V logic |
| **Ground (Black)**| `GND` | Common ground |

---

## Software Stack & Dependencies

### 1. The Edge Device (ESP32-S3)
The physical firmware is written in C++ using the Arduino IDE.
**Required Libraries:**
* `WiFiClientSecure.h` (For encrypted TLS connections)
* `PubSubClient` by Nick O'Leary (MQTT Engine)
* `ESP32Servo` by Kevin Harrington (Hardware-specific PWM control)

### 2. The Digital Twin (Python)
The digital dashboard and control script runs locally.
**Required Libraries:**
```bash
pip install paho-mqtt