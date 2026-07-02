import random

ENGINES = ["Engine_A", "Engine_B", "Engine_C", "Engine_D", "Engine_E", "Engine_F"]

def generate_health():
    return {engine: random.randint(50, 100) for engine in ENGINES}

def detect_failure(health):
    failed = [e for e, h in health.items() if h < 60]
    return failed

def isolate_engines(health, failed):
    for e in failed:
        health[e] = 0
    return health

def score_engines(health):
    return sorted(health.items(), key=lambda x: x[1], reverse=True)

def relight_gate(best_engine, best_score):
    if best_score < 70:
        return "RELIGHT DENIED"
    return f"RELIGHT AUTHORIZED → {best_engine}"

def run_simulation():
    print("\n--- SHIP RELIGHT SIMULATION START ---\n")

    health = generate_health()
    print("ENGINE HEALTH:", health)

    failed = detect_failure(health)
    print("FAILED ENGINES:", failed)

    health = isolate_engines(health, failed)
    ranked = score_engines(health)

    best_engine, best_score = ranked[0]

    print("BEST ENGINE:", best_engine, "SCORE:", best_score)
    print(relight_gate(best_engine, best_score))

    print("\n--- SIMULATION COMPLETE ---\n")

if __name__ == "__main__":
    run_simulation()
