import time
from src.engine.engine_model import EngineModel
from src.scoring.health_scoring import HealthScorer
from src.decision.relight_gate import RelightGate

def run(iterations=6):

    print("\n🚀 SHIP RELIGHT GUARDIAN — MISSION CONTROL SIMULATION\n")

    engine = EngineModel()
    scorer = HealthScorer()
    gate = RelightGate()

    for step in range(iterations):

        print(f"\n================ STEP {step+1} ================\n")

        # simulate engine drift + random failure
        engine.drift_health()

        if step % 2 == 0:
            failed = engine.inject_failure()
            print(f"⚠️ FAILURE EVENT: {failed}")

        # get engine data
        health = engine.get_health()

        print("\n📊 ENGINE HEALTH STATUS")
        for k, v in health.items():
            print(f" - {k}: {v}")

        # score engines
        scored = scorer.score_engines(health)

        print("\n📈 ENGINE CLASSIFICATION")
        for k, v in scored.items():
            print(f" - {k}: {v['health']} | {v['grade']}")

        # decision gate
        result = gate.evaluate(scored)

        print("\n🧠 RELIGHT DECISION")
        print(f" Decision: {result['decision']}")
        print(f" State: {result['state']}")
        print(f" Selected Engine: {result['selected_engine']}")
        print(f" Health: {result['health']}")

        time.sleep(1)

    print("\n✅ MISSION COMPLETE — SYSTEM STABLE\n")


if __name__ == "__main__":
    run()