"""
Ship Relight Guardian
Module: Post-Ignition Monitor

Purpose:
Monitor engine behavior after a relight attempt and determine whether
the relight remains stable or should be aborted.

Stage:
8 — After Ignition Monitoring

Public Repository Notice:
This is a conceptual simulation module.
It is not flight software.
"""


class PostIgnitionMonitor:
    """
    Monitors simulated post-ignition engine behavior.
    """

    def evaluate(
        self,
        thrust_buildup_ok: bool,
        chamber_pressure_stable: bool,
        turbopump_stable: bool,
        vibration_safe: bool,
        temperature_safe: bool,
    ) -> dict:
        """
        Return post-ignition stability state.
        """

        stable = (
            thrust_buildup_ok
            and chamber_pressure_stable
            and turbopump_stable
            and vibration_safe
            and temperature_safe
        )

        if stable:
            return {
                "post_ignition_state": "STABLE",
                "abort_required": False,
                "reason": "RELIGHT_STABLE",
            }

        return {
            "post_ignition_state": "UNSTABLE",
            "abort_required": True,
            "reason": "POST_IGNITION_LIMIT_EXCEEDED",
        }