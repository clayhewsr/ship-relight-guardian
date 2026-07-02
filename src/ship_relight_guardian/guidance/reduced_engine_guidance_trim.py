"""
Ship Relight Guardian
Module: Reduced Engine Guidance Trim

Purpose:
Adjust simulated guidance state after relight when the vehicle is operating
with fewer engines than nominal.

Stage:
8 Extension — Guidance Trim for Reduced Engine Count

Public Repository Notice:
This is a conceptual simulation module.
It is not flight software.
"""


class ReducedEngineGuidanceTrim:
    """
    Simulates guidance compensation after engine loss.
    """

    def calculate(
        self,
        nominal_engine_count: int,
        active_engine_count: int,
    ) -> dict:
        """
        Calculate reduced-engine guidance trim state.
        """

        if nominal_engine_count <= 0:
            return {
                "trim_state": "INVALID",
                "reason": "NOMINAL_ENGINE_COUNT_INVALID",
            }

        if active_engine_count <= 0:
            return {
                "trim_state": "SAFE_TRAJECTORY",
                "reason": "NO_ACTIVE_ENGINES",
            }

        thrust_fraction = active_engine_count / nominal_engine_count

        return {
            "trim_state": "REDUCED_ENGINE_TRIM",
            "nominal_engine_count": nominal_engine_count,
            "active_engine_count": active_engine_count,
            "thrust_fraction": round(thrust_fraction, 3),
        }