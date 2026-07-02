"""
Ship Relight Guardian
Module: Failed Engine Isolator

Purpose:
Isolate a failed engine after an engine-out event has been detected.

Stage:
2 — Isolate Failed Engine

Public Repository Notice:
This is a conceptual simulation module.
It is not flight software.
"""


class FailedEngineIsolator:
    """
    Simulates isolation of a failed engine.
    """

    def __init__(self):
        self.engine_isolated = False
        self.failed_engine_id = None

    def isolate(self, engine_id: str) -> dict:
        """
        Isolate the failed engine and prevent restart attempts.
        """

        self.failed_engine_id = engine_id
        self.engine_isolated = True

        return {
            "engine_id": engine_id,
            "isolated": True,
            "restart_allowed": False,
            "neighbor_protection": True,
            "status": "FAILED_ENGINE_ISOLATED",
        }