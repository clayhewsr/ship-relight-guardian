class HealthScorer:
    def score_engines(self, engine_health):

        scores = {}

        for engine, health in engine_health.items():

            if health >= 85:
                grade = "🟢 EXCELLENT"
            elif health >= 70:
                grade = "🟡 GOOD"
            elif health >= 50:
                grade = "🟠 WARNING"
            elif health >= 30:
                grade = "🔴 CRITICAL"
            else:
                grade = "⚫ FAILURE"

            scores[engine] = {
                "health": health,
                "grade": grade
            }

        return scores
