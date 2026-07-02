\# Ship Relight Guardian Architecture



\## System Overview



Ship Relight Guardian is organized as an eight-stage decision pipeline.



The system does not treat relight as a timed event.  

It treats relight as a permission decision.



A relight command is only allowed after the system confirms that:



\- the failed engine has been isolated

\- the vehicle is stable

\- the propellant state is safe

\- at least one remaining engine is healthy

\- the trajectory has enough margin

\- post-ignition monitoring is ready



\---



\## High-Level Flow



```text

Sensor Inputs

&#x20;    ↓

1\. Detect Engine-Out

&#x20;    ↓

2\. Isolate Failed Engine

&#x20;    ↓

3\. Check Vehicle State

&#x20;    ↓

4\. Check Propellant State

&#x20;    ↓

5\. Score Remaining Engines

&#x20;    ↓

6\. Select Healthiest Engine

&#x20;    ↓

7\. Relight Permission Gate

&#x20;    ↓

8\. Post-Ignition Monitoring

