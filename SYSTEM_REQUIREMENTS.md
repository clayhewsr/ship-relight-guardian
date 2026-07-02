\# Ship Relight Guardian System Requirements



\## Purpose



This document defines the functional requirements for the Ship Relight Guardian architecture.



The requirements describe \*\*what the system must do\*\*, not \*\*how it is implemented\*\*.



\---



\# Functional Requirement 1 — Engine-Out Detection



The system shall continuously monitor propulsion telemetry.



The system shall detect:



\- loss of thrust

\- abnormal chamber pressure

\- shutdown events

\- turbopump instability

\- abnormal vibration

\- abnormal temperature



Output:



```

ENGINE\_OUT = TRUE | FALSE

```



\---



\# Functional Requirement 2 — Failed Engine Isolation



When an engine-out event is detected, the failed engine shall be isolated.



Isolation actions include:



\- prevent restart attempts

\- remove engine from candidate pool

\- mark engine unavailable

\- protect neighboring engines



Output:



```

ENGINE\_ISOLATED = TRUE

```



\---



\# Functional Requirement 3 — Vehicle State Evaluation



The system shall evaluate vehicle stability before authorizing recovery.



Minimum checks include:



\- attitude stability

\- angular rate

\- structural vibration

\- thermal operating region



Output:



```

VEHICLE\_STATE = GREEN | YELLOW | RED

```



\---



\# Functional Requirement 4 — Propellant Assessment



The system shall verify propellant readiness.



Minimum checks:



\- tank pressure

\- liquid settling

\- gas ingestion risk

\- header tank margin



Output:



```

PROPELLANT\_STATE = GREEN | YELLOW | RED

```



\---



\# Functional Requirement 5 — Engine Health Evaluation



Each available engine shall receive a health score.



Suggested evaluation factors:



\- chamber pressure

\- turbopump speed

\- inlet pressure

\- temperature

\- vibration

\- previous anomalies



Output:



```

ENGINE\_HEALTH = 0.00 – 1.00

```



\---



\# Functional Requirement 6 — Engine Selection



The healthiest available engine shall be selected.



Selection shall ignore:



\- isolated engines

\- failed engines

\- engines below minimum health threshold



Output:



```

SELECTED\_ENGINE

```



\---



\# Functional Requirement 7 — Relight Permission Gate



A relight shall only be authorized if:



✓ Vehicle State = GREEN



✓ Propellant State = GREEN



✓ Selected Engine Health ≥ Minimum Threshold



✓ Recovery Path Available



Otherwise:



```

RELIGHT = DENIED

```



\---



\# Functional Requirement 8 — Post-Ignition Monitoring



Following relight, the system shall continue monitoring:



\- thrust buildup

\- chamber pressure

\- vibration

\- thermal response

\- guidance response



If instability exceeds limits:



```

ABORT RELIGHT

```



or



```

SAFE TRAJECTORY MODE

```



\---



\# Non-Functional Requirements



The architecture shall be:



\- Modular

\- Explainable

\- Testable

\- Expandable

\- Deterministic

\- Simulation-first



\---



\# Core Decision Rule



A relight decision shall never be based solely on mission timing.



Authorization requires successful completion of all required safety gates.

