"""
Ship Relight Guardian
Module: Relight Permission Gate

Purpose:
Authorize or deny relight based on vehicle state, propellant state,
and selected engine health.

Stage:
7 — Run Relight Permission Gate
"""


class RelightPermissionGate:
    def evaluate(
        self,
        vehicle_state: str,
        propellant_state: str,
        selected_engine: str | None,
        engine_health_score: int | None,
    ) -> dict:

        if vehicle_state != "GREEN":
            return {"relight_allowed": False, "decision": "HOLD", "reason": "VEHICLE_STATE_NOT_GREEN"}

        if propellant_state != "GREEN":
            return {"relight_allowed": False, "decision": "HOLD", "reason": "PROPELLANT_STATE_NOT_GREEN"}

        if selected_engine is None:
            return {"relight_allowed": False, "decision": "SKIP_RELIGHT", "reason": "NO_SELECTED_ENGINE"}

        if engine_health_score is None or engine_health_score < 85:
            return {"relight_allowed": False, "decision": "SKIP_RELIGHT", "reason": "ENGINE_HEALTH_BELOW_THRESHOLD"}

        return {
            "relight_allowed": True,
            "decision": "RELIGHT",
            "reason": "ALL_GATES_GREEN",
            "selected_engine": selected_engine,
        }