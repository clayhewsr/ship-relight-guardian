# Ship Relight Guardian

## Overview

# Ship Relight Guardian

Ship Relight Guardian is a fault-tolerant engine-out detection and autonomous relight decision system for multi-engine propulsion architectures.

The project simulates how a vehicle can detect an engine failure, isolate the failed engine, evaluate remaining engine health, score available recovery options, and authorize the safest relight candidate.

## Core Capabilities

- Engine-out detection
- Failed-engine isolation
- Vehicle health evaluation
- Propellant and system readiness checks
- Engine health scoring
- Best-engine selection
- Relight permission logic
- Post-relight monitoring
- Reduced-engine guidance support

## System Diagram

![Ship Relight Health Gate Logic](ship_relight_health_gate_logic.png)

## How It Works

1. Detect engine anomaly
2. Isolate failed engine
3. Evaluate remaining engine health
4. Score each engine
5. Select safest recovery candidate
6. Run relight permission gate
7. Authorize, wait, or abort
8. Continue mission with updated guidance

## Mission Goal

The goal is to demonstrate a modular safety-assist system that supports fault-tolerant propulsion recovery decisions.

This project is intended as a simulation and software architecture prototype for engine health monitoring, relight decision logic, and mission stability evaluation.

## Current Status

- Engine failure simulation working
- Health scoring module added
- Relight decision gate added
- Multi-step mission loop running
- GitHub repository updated with core simulation modules
- 
Ship Relight Guardian is a fault-tolerant propulsion decision system that models engine-out detection, engine isolation, vehicle health evaluation, and autonomous relight authorization logic for multi-engine aerospace architectures.

The system simulates redundancy-based decision-making used in high-reliability propulsion systems, where continued operation depends on real-time engine health assessment and controlled recovery logic.

---

## System Architecture

The system is structured as a sequential decision pipeline:

1. Engine-out detection
2. Engine isolation
3. Vehicle health evaluation
4. Propellant state validation
5. Engine health scoring
6. Optimal engine selection
7. Relight permission gating
8. Post-ignition monitoring
9. Reduced-engine guidance computation

---

## System Diagram

![Relight Health Gate Logic](31eb5075-62f0-4e03-8479-2d35e8085394.png)

---

## System Inputs

- Chamber pressure
- Turbopump performance metrics
- Inlet pressure readings
- Thermal telemetry
- Vibration signatures
- Valve state positions
- IMU attitude and rate data
- Propellant tank levels

---

## System Outputs

- Engine health score (0–100)
- Engine isolation command
- Relight authorization decision
- Selected restart engine
- Post-relight stability status
- Guidance adjustment signals

---

## System States

- NOMINAL
- MONITORING
- DEGRADED
- ENGINE_ISOLATED
- RELIGHT_PENDING
- RELIGHT_AUTHORIZED
- RELIGHT_ABORTED
- STABILIZED

---

## Failure Modes

- Engine shutdown event detection failure
- False-positive isolation triggers
- Sensor degradation or drift
- Propellant imbalance conditions
- Thermal instability during relight
- Vibration threshold exceedance

---

## Relight Permission Logic

Relight authorization is granted only when:

- All critical system parameters are within safe thresholds
- Vehicle stability constraints are satisfied
- Propellant conditions are nominal
- At least one engine meets minimum health threshold
- Guidance system remains stable under reduced thrust conditions

---

## How to Run

```bash
python main.py
