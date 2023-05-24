from typing import Dict
import json
import random


class JSONGenerator:
    def __init__(self, count=1):
        self.count = count

    def generate_json(self) -> str:
        result = [self._generate_dict() for _ in range(self.count)]
        return json.dumps(result)

    def _generate_dict(self) -> Dict:
        return {
            "a": random.randint(0, 100),
            "b": random.randint(0, 100),
            "c": random.randint(0, 100),
        }
