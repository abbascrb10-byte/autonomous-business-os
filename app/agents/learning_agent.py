from typing import Dict

class LearningAgent:
    def __init__(self):
        self.source_weights: Dict[str, float] = {
            "requests": 1.2,
            "forums": 1.0,
            "search": 1.1,
            "owned": 1.5,
            "agentic": 1.3
        }

    def adjust_weights(self, source: str, converted: bool):
        if source in self.source_weights:
            if converted:
                self.source_weights[source] += 0.05
            else:
                self.source_weights[source] = max(0.1, self.source_weights[source] - 0.01)
