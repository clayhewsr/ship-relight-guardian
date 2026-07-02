"""
Ship Relight Guardian
Module: Engine Health Scorer

Purpose:
Evaluate the health of a remaining engine using simulated telemetry.

Stage:
5 — Score Remaining Engines

Public Repository Notice:
This is a conceptual engineering simulation.
It is not flight software.
"""


class EngineHealthScorer:
    """
    Calculates a normalized health score for an engine.
    """

    def score(
        self,
        chamber_pressure_ok: bool,
        turbopump_speed_ok: bool,
        inlet_pressure_ok: bool,
        temperature_ok: bool,
        vibration_ok: bool,
        previous_anomalies: int,
    ) -> dict:
        """
        Calculate a simple engine health score.
        """

        score = 0

        if chamber_pressure_ok:
            score += 20

        if turbopump_speed_ok:
            score += 20

        if inlet_pressure_ok:
            score += 20

        if temperature_ok:
            score += 20

        if vibration_ok:
            score += 20

        # Deduct points for previous anomalies
        score -= previous_anomalies * 5

        score = max(0, min(score, 100))

        return {
            "health_score": score,
            "health_state": (
                "GREEN"
                if score >= 85
                else "YELLOW"
                if score >= 60
                else "RED"
            ),
        }