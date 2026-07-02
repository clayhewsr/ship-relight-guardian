# Ship Relight Guardian

A modular Python simulation system for engine-out detection, fault isolation, engine health scoring, and autonomous relight decision-making.

This project models a redundant propulsion decision pipeline that evaluates multiple engines and selects the safest recovery path after a failure event.

---

## System Overview

The Ship Relight Guardian simulates a structured decision system used to handle engine failure scenarios in a multi-engine environment. It evaluates system health, isolates failures, and determines whether a safe relight is possible.

---

## System Flow

1. Detect engine anomaly (pressure, vibration, thrust deviation)
2. Isolate failed engine to prevent system contamination
3. Evaluate vehicle and propellant state
4. Score remaining engines based on health metrics
5. Select healthiest engine candidate
6. Evaluate relight permission gate conditions
7. Execute relight decision or hold if unsafe
8. Monitor post-ignition stability and adjust guidance

---

## System Diagram

![Relight Health Gate Logic](31eb5075-62f0-4e03-8479-2d35e8085394.png)

---

## How to Run

```bash
python main.py
