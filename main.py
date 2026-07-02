import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.append(str(ROOT / "src"))

from ship_relight_guardian.detection.engine_out_detector import EngineOutDetector
from ship_relight_guardian.isolation.failed_engine_isolator import FailedEngineIsolator
from ship_relight_guardian.vehicle.vehicle_state_checker import VehicleStateChecker
from ship_relight_guardian.propellant.propellant_state_checker import PropellantStateChecker
from ship_relight_guardian.scoring.engine_health_scorer import EngineHealthScorer
from ship_relight_guardian.decision.healthiest_engine_selector import HealthiestEngineSelector
from ship_relight_guardian.decision.relight_permission_gate import RelightPermissionGate
from ship_relight_guardian.monitoring.post_ignition_monitor import PostIgnitionMonitor
from ship_relight_guardian.guidance.reduced_engine_guidance_trim import ReducedEngineGuidanceTrim


def main():
    print("SHIP RELIGHT GUARDIAN")
    print("=" * 40)

    detector = EngineOutDetector()
    engine_out = detector.evaluate(True, True, False, False, False)
    print("1. Engine Out:", engine_out)

    isolator = FailedEngineIsolator()
    isolation = isolator.isolate("Raptor-12")
    print("2. Isolation:", isolation)

    vehicle = VehicleStateChecker()
    vehicle_state = vehicle.evaluate(True, True, True, True)
    print("3. Vehicle:", vehicle_state)

    propellant = PropellantStateChecker()
    propellant_state = propellant.evaluate(True, True, False, True)
    print("4. Propellant:", propellant_state)

    scorer = EngineHealthScorer()
    engine_score = scorer.score(True, True, True, True, True, 0)
    print("5. Engine Score:", engine_score)

    selector = HealthiestEngineSelector()
    selected = selector.select([
        {"engine_id": "Raptor-03", "available": True, **engine_score}
    ])
    print("6. Selected Engine:", selected)

    gate = RelightPermissionGate()
    permission = gate.evaluate(
        vehicle_state["vehicle_state"],
        propellant_state["propellant_state"],
        selected["selected_engine"],
        selected["health_score"],
    )
    print("7. Permission:", permission)

    monitor = PostIgnitionMonitor()
    post = monitor.evaluate(True, True, True, True, True)
    print("8. Post Ignition:", post)

    guidance = ReducedEngineGuidanceTrim()
    trim = guidance.calculate(33, 32)
    print("9. Guidance Trim:", trim)

    print("=" * 40)
    print("Simulation complete.")


if __name__ == "__main__":
    main()