\# Ship Relight Guardian Roadmap



\## Vision



Ship Relight Guardian is a modular safety architecture that evaluates whether an engine relight should occur following an engine-out event.



The system is built around health validation instead of timeline execution.



\---



\# Development Phases



\## Phase 1 — Foundation



\- \[x] README

\- \[x] Architecture

\- \[ ] Roadmap

\- \[ ] Repository Structure

\- \[ ] License

\- \[ ] Contributing Guide



\---



\## Phase 2 — Detection Layer



Modules



\- Engine-Out Detector

\- Telemetry Monitor

\- Sensor Validation

\- Failure Classification



Deliverable



Detect engine failures with simulated telemetry.



\---



\## Phase 3 — Isolation Layer



Modules



\- Failed Engine Isolation

\- Valve Isolation

\- Restart Lockout

\- Neighbor Protection



Deliverable



Safely isolate the failed propulsion unit.



\---



\## Phase 4 — Vehicle Assessment



Modules



\- Attitude Monitor

\- Rotation Monitor

\- Thermal Monitor

\- Structural Vibration Monitor



Deliverable



Determine if the vehicle is stable enough for relight.



\---



\## Phase 5 — Propellant Assessment



Modules



\- Tank Pressure

\- Liquid Settling

\- Header Tank Margin

\- Gas Ingestion Detection



Deliverable



Determine if propellant conditions support a safe relight.



\---



\## Phase 6 — Engine Health



Modules



\- Chamber Pressure Analysis

\- Turbopump Analysis

\- Temperature Analysis

\- Vibration Analysis

\- Historical Reliability



Deliverable



Produce a health score for every remaining engine.



\---



\## Phase 7 — Decision Layer



Modules



\- Engine Selection

\- Relight Permission Gate

\- Safety Validation

\- Mission Logic



Deliverable



Authorize or reject relight.



\---



\## Phase 8 — Recovery Layer



Modules



\- Post-Ignition Monitoring

\- Guidance Trim

\- Reduced Engine Compensation

\- Continuous Health Monitoring



Deliverable



Safely recover vehicle performance after relight.



\---



\# Design Philosophy



Observe



↓



Understand



↓



Validate



↓



Score



↓



Decide



↓



Act



↓



Monitor



↓



Repeat



\---



\# Long-Term Goals



\- Modular simulation framework

\- Expandable architecture

\- Independent subsystem testing

\- Public educational reference

\- GitHub open-source collaboration

