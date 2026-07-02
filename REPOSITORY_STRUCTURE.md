\# Ship Relight Guardian Repository Structure



\## Purpose



This document defines the complete repository layout before implementation begins.



Each directory has a single responsibility.



\---



\# Repository Layout



```text

ship-relight-guardian/

│

├── README.md

├── ARCHITECTURE.md

├── PROJECT\_ROADMAP.md

├── REPOSITORY\_STRUCTURE.md

├── LICENSE

├── CHANGELOG.md

├── CONTRIBUTING.md

│

├── docs/

│

├── src/

│   ├── detection/

│   ├── isolation/

│   ├── vehicle/

│   ├── propellant/

│   ├── scoring/

│   ├── decision/

│   ├── monitoring/

│   ├── guidance/

│   └── common/

│

├── simulation/

│

├── tests/

│

├── examples/

│

└── assets/

```



\---



\# Documentation



README.md



Project overview.



ARCHITECTURE.md



System architecture.



PROJECT\_ROADMAP.md



Development phases.



REPOSITORY\_STRUCTURE.md



Repository organization.



CHANGELOG.md



Version history.



CONTRIBUTING.md



Contribution guide.



LICENSE



Repository license.



\---



\# Source Modules



\## detection/



Detect propulsion anomalies.



Modules:



\- engine\_out\_detector

\- telemetry\_monitor

\- sensor\_validation

\- failure\_classifier



\---



\## isolation/



Protect the propulsion system.



Modules:



\- failed\_engine\_isolation

\- valve\_manager

\- restart\_lockout

\- neighbor\_engine\_protection



\---



\## vehicle/



Determine if the vehicle is stable.



Modules:



\- attitude\_monitor

\- angular\_rate\_monitor

\- vibration\_monitor

\- thermal\_monitor



\---



\## propellant/



Determine if propellant conditions are safe.



Modules:



\- tank\_pressure

\- liquid\_settling

\- gas\_ingestion

\- header\_margin



\---



\## scoring/



Evaluate engine health.



Modules:



\- chamber\_pressure

\- turbopump

\- temperature

\- vibration

\- anomaly\_history

\- engine\_health\_score



\---



\## decision/



Final authorization layer.



Modules:



\- healthiest\_engine\_selector

\- relight\_permission\_gate

\- mission\_decision



\---



\## monitoring/



Observe the relight.



Modules:



\- thrust\_monitor

\- chamber\_pressure\_monitor

\- ignition\_validation

\- abort\_monitor



\---



\## guidance/



Trajectory recovery.



Modules:



\- reduced\_engine\_trim

\- trajectory\_adjustment

\- engine\_compensation



\---



\## common/



Shared utilities.



Modules:



\- constants

\- logging

\- configuration

\- health\_states



\---



\# Engineering Philosophy



Every folder should have one responsibility.



Every module should perform one job.



Every decision should be explainable.



Every action should be validated before execution.

