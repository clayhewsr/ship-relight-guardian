"""
Ship Relight Guardian
Module: Engine-Out Detector

Purpose:
Detect when an engine has experienced a shutdown or abnormal operating condition.

This module is part of Stage 1 of the Ship Relight Guardian architecture.

Public Repository Notice:
This implementation is a conceptual engineering simulation.
It is not flight software.
"""


class EngineOutDetector:
    """
    Detects a possible engine-out event using simulated telemetry.
    """

    def __init__(self):
        self.engine_out = False

    def evaluate(
        self,
        thrust_loss: bool,
        chamber_pressure_drop: bool,
        shutdown_signal: bool,
        excessive_vibration: bool,
        excessive_temperature: bool,
    ) -> bool:
        """
        Determine whether an engine-out event has occurred.
        """

        if (
            thrust_loss
            or chamber_pressure_drop
            or shutdown_signal
            or excessive_vibration
            or excessive_temperature
        ):
            self.engine_out = True
        else:
            self.engine_out = False

        return self.engine_out