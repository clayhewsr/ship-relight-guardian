"""
Ship Relight Guardian
Module: Propellant State Checker

Purpose:
Evaluate whether propellant conditions are safe enough to permit relight.

Stage:
4 — Check Propellant State

Public Repository Notice:
This is a conceptual simulation module.
It is not flight software.
"""


class PropellantStateChecker:
    """
    Checks simulated propellant readiness before relight permission.
    """

    def evaluate(
        self,
        tank_pressure_stable: bool,
        liquid_settled_at_pickup: bool,
        gas_ingestion_risk: bool,
        header_tank_margin_ok: bool,
    ) -> dict:
        """
        Return propellant state as GREEN or RED.
        """

        all_green = (
            tank_pressure_stable
            and liquid_settled_at_pickup
            and not gas_ingestion_risk
            and header_tank_margin_ok
        )

        return {
            "tank_pressure_stable": tank_pressure_stable,
            "liquid_settled_at_pickup": liquid_settled_at_pickup,
            "gas_ingestion_risk": gas_ingestion_risk,
            "header_tank_margin_ok": header_tank_margin_ok,
            "propellant_state": "GREEN" if all_green else "RED",
        }