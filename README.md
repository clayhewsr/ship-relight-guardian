# Ship Relight Guardian

![Ship Relight Health Gate Logic](ship_relight_health_gate_logic.png)

## Overview

Ship Relight Guardian is a modular fault-tolerant engine health monitoring and autonomous relight decision system designed to simulate engine-out recovery for multi-engine propulsion systems.

The project demonstrates how software can detect propulsion failures, evaluate remaining engine health, select the safest recovery option, and assist operators through a structured decision process.

---

# Features

- Engine failure detection
- Engine health monitoring
- Health scoring algorithms
- Intelligent engine selection
- Autonomous relight authorization
- Mission stability verification
- Multi-step simulation engine
- Modular architecture
- Expandable AI-assisted decision framework

---

# Current Architecture

```
ship-relight-guardian/
│
├── README.md
├── LICENSE
├── requirements.txt
├── main.py
│
├── src/
│   ├── core/
│   ├── decision/
│   ├── engine/
│   ├── scoring/
│   ├── simulation/
│   ├── utils/
│   └── ship_relight_guardian/
│
├── assets/
└── docs/
```

---
---

# How to Run
---

# Project Status

**Current Version:** Prototype v1

## Completed

- ✅ Modular project architecture
- ✅ Engine simulation framework
- ✅ Engine health scoring
- ✅ Autonomous relight decision logic
- ✅ Multi-step simulation loop
- ✅ GitHub project structure
- ✅ Initial documentation

## In Progress

- 🚧 Interactive mission dashboard
- 🚧 Live engine status indicators
- 🚧 Mission event logging
- 🚧 Simulation visualization
- 🚧 Expanded failure scenarios

## Planned

- Predictive engine health monitoring
- AI-assisted diagnostics
- Historical mission replay
- Multi-vehicle simulation
- Operator control panel
- Digital twin integration
- Plugin architecture for future expansion

---

# Contributing

This repository is under active development.

Suggestions, improvements, and engineering discussions are welcome as the project continues to evolve.

---

# License

This project is currently intended for research, educational, and demonstration purposes.
Future licensing may be updated as the platform matures.
## Requirements

- Python 3.10 or newer
- Git
- pip

## Clone the Repository

```bash
git clone https://github.com/clayhewsr/ship-relight-guardian.git
cd ship-relight-guardian
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Simulation

```bash
python main.py
```

or, if using the modular simulation:

```bash
python -m src.simulation.run_simulation
```

---

# Example Simulation Output

```text
STEP 1

Engine A : FAILURE
Engine B : FAILURE
Engine C : GOOD
Engine D : WARNING
Engine E : GOOD
Engine F : GOOD

Decision: PASS

Selected Engine:
Engine E

MISSION COMPLETE

SYSTEM STABLE
```

---

# Repository Goals

The Ship Relight Guardian project is focused on demonstrating a modular engineering approach to propulsion recovery simulations.

Current areas of development include:

- Engine health monitoring
- Failure detection
- Intelligent scoring
- Relight authorization
- Mission-state management
- Expandable simulation framework
- Future visualization dashboard

---

# Technologies

- Python
- GitHub
- Modular Software Architecture
- Simulation Modeling
- Fault-Tolerant Design
- Engineering Decision Logic

---

# Current Project Status

🟢 Active Development

The project is under continuous development with new simulation capabilities, visualization tools, and engineering modules being added as the architecture evolves.

# Module Responsibilities

## Core

Maintains overall system state and mission status.

## Engine

Models engine performance, degradation, and failures.

## Decision

Determines whether engine relight should be authorized.

## Scoring

Evaluates engine health and assigns recovery scores.

## Simulation

Runs complete mission simulations including failures, recovery decisions, and mission completion.

## Utils

Reserved for future shared helper functions and utilities.

---

# Simulation Workflow

1. Detect engine anomaly
2. Identify failed engine
3. Evaluate remaining engines
4. Score engine health
5. Select best recovery candidate
6. Execute relight decision logic
7. Continue simulation
8. Verify mission stability

---

# Example Output

```
ENGINE CLASSIFICATION

Engine A - FAILURE
Engine B - FAILURE
Engine C - GOOD
Engine D - WARNING
Engine E - GOOD
Engine F - GOOD

Decision:
PASS

Selected Engine:
Engine E

MISSION COMPLETE

SYSTEM STABLE
```

---

# Development Progress

### Completed

- Modular project architecture
- Engine simulation framework
- Health scoring module
- Decision engine
- Relight authorization logic
- Multi-step simulation loop
- GitHub project organization

### In Progress

- Dashboard visualization
- Live engine status indicators
- Interactive mission display
- Event logging
- Improved simulation realism

### Planned

- AI-assisted decision support
- Predictive engine health
- Historical replay
- Mission recording
- Web dashboard
- Multi-vehicle simulation
- Operator control panel

---

# Design Philosophy

Ship Relight Guardian is designed around modular engineering principles.

Each subsystem performs a single responsibility, allowing the project to grow while remaining easy to understand, test, and maintain.

The long-term objective is to demonstrate reliable propulsion recovery decision support through simulation, visualization, and intelligent software architecture.

---

# Status

Current Version

**Prototype v1**

Current Capabilities

- Engine health evaluation
- Fault detection
- Relight decision logic
- Simulation engine
- GitHub hosted development

---
---

# Development Roadmap

## Phase 1 — Foundation ✅

- [x] Create GitHub repository
- [x] Professional project documentation
- [x] Modular project architecture
- [x] Core simulation framework
- [x] Engine health scoring
- [x] Autonomous relight decision logic
- [x] Mission simulation loop

---
---

# Project Objectives

Ship Relight Guardian is being developed as a modular simulation platform for propulsion fault detection, recovery planning, and autonomous relight decision support.

The project is designed to demonstrate engineering best practices by separating each major function into independent, reusable modules that can evolve over time.

## Primary Objectives

- Develop a reliable engine health monitoring framework.
- Simulate propulsion system failures.
- Evaluate engine recovery options using health scoring.
- Assist operators with structured relight decisions.
- Provide a foundation for future AI-assisted diagnostics.
- Create a reusable architecture for simulation and visualization.

---

# Engineering Principles

The project follows several core engineering principles:

- **Modularity** – Each subsystem has a clearly defined responsibility.
- **Scalability** – New simulation modules can be added without redesigning the system.
- **Transparency** – Decision logic is understandable and traceable.
- **Maintainability** – Code is organized for long-term development.
- **Safety** – Decisions are based on system state rather than assumptions.

---

# Long-Term Vision

The long-term vision is to evolve Ship Relight Guardian into a comprehensive propulsion systems simulation environment featuring:

- Interactive dashboards
- Digital twin concepts
- Predictive health monitoring
- AI-assisted recommendations
- Scenario playback and mission replay
- Expandable plugin architecture
- Support for additional vehicle and propulsion configurations

---

# Repository Status

**Status:** Active Development

The repository is continuously evolving as new simulation capabilities, visualization tools, and software architecture improvements are added.

## Phase 2 — Visualization 🚧

- [ ] Live engine status dashboard
- [ ] Green / Yellow / Red engine indicators
- [ ] Mission timeline
- [ ] Interactive control panel
- [ ] Engine health gauges
- [ ] Mission event log

---

## Phase 3 — Advanced Simulation

- [ ] Multiple engine-out scenarios
- [ ] Weather effects
- [ ] Fuel system failures
- [ ] Sensor failures
- [ ] Electrical failures
- [ ] Hydraulic failures
- [ ] Recovery scenarios

---

## Phase 4 — Intelligent Decision Support

- [ ] AI-assisted diagnostics
- [ ] Failure prediction
- [ ] Maintenance recommendations
- [ ] Risk assessment
- [ ] Mission success probability
- [ ] Recovery optimization

---

## Phase 5 — Future Expansion

- [ ] Web dashboard
- [ ] Mobile monitoring
- [ ] Fleet management
- [ ] Historical mission replay
- [ ] Data analytics
- [ ] API integration
- [ ] Digital twin support

---

# Current Development Status

**Project Status:** Active Development

### Completed

- Professional GitHub repository
- Modular Python architecture
- Engine simulation framework
- Health scoring system
- Decision engine
- Relight authorization logic
- Mission simulation

### Current Focus

Building a professional simulation platform capable of demonstrating autonomous propulsion recovery through modular software architecture and visualization.

# License

This project is released for research and educational purposes.

Future licensing may change as development progresses.
