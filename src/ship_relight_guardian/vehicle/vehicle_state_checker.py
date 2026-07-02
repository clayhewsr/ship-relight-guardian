"""
Ship Relight Guardian
Module: Vehicle State Checker

Purpose:
Evaluate whether the vehicle is stable enough to permit a relight decision.

Stage:
3 — Check Vehicle State

Public Repository Notice:
This is a conceptual simulation module.
It is not flight software.
"""


class VehicleStateChecker:
    """
    Checks vehicle stability conditions before relight permission.
    """

    def evaluate(
        self,
        attitude_stable: bool,
        spin_rate_safe: bool,
        vibration_safe: bool,
        thermal_zone_safe: bool,
    ) -> dict:
        """
        Return vehicle state as GREEN or RED.
        """

        all_green = (
            attitude_stable
            and spin_rate_safe
            and vibration_safe
            and thermal_zone_safe
        )

        return {
            "attitude_stable": attitude_stable,
            "spin_rate_safe": spin_rate_safe,
            "vibration_safe": vibration_safe,
            "thermal_zone_safe": thermal_zone_safe,
            "vehicle_state": "GREEN" if all_green else "RED",
        }