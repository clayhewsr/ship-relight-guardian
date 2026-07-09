import random

ENGINES = ["Engine_A", "Engine_B", "Engine_C", "Engine_D", "Engine_E", "Engine_F"]

class EngineModel:

    def __init__(self):
        self.health = {e: random.randint(70, 100) for e in ENGINES}

    def inject_failure(self):
        failed = random.choice(ENGINES)
        self.health[failed] = random.randint(0, 40)
        return failed

    def drift_health(self):
        for e in self.health:
            change = random.randint(-6, 3)
            self.health[e] = max(0, min(100, self.health[e] + change))

    def get_health(self):
        return self.health