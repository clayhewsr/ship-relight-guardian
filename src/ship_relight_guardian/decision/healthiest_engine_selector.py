"""
Ship Relight Guardian
Module: Healthiest Engine Selector

Purpose:
Select the healthiest available engine from scored engine candidates.

Stage:
6 — Select Healthiest Engine
"""


class HealthiestEngineSelector:
    def __init__(self, minimum_score: int = 85):
        self.minimum_score = minimum_score

    def select(self, engine_scores: list[dict]) -> dict:
        eligible_engines = [
            engine for engine in engine_scores
            if engine.get("available", True)
            and engine.get("health_score", 0) >= self.minimum_score
        ]

        if not eligible_engines:
            return {
                "selected_engine": None,
                "selection_state": "NO_ELIGIBLE_ENGINE",
                "relight_candidate_available": False,
            }

        selected = max(eligible_engines, key=lambda engine: engine["health_score"])

        return {
            "selected_engine": selected.get("engine_id"),
            "health_score": selected.get("health_score"),
            "selection_state": "ENGINE_SELECTED",
            "relight_candidate_available": True,
        }