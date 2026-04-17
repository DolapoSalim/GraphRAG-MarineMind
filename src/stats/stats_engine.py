import json
from typing import List, Dict, Any


class StatsEngine:
    def __init__(self, stats_path: str):
        self.stats = self._load_stats(stats_path)

    def _load_stats(self, path: str) -> List[Dict[str, Any]]:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def query(self, user_query: str) -> List[str]:
        query = user_query.lower()
        results = []

        for entry in self.stats:
            variable = entry["variable"]

            if variable in query:
                trend = entry["trend"]
                drivers = ", ".join(entry["drivers"])
                confidence = entry["confidence"]

                results.append(
                    f"{variable} → trend: {trend}, drivers: {drivers}, confidence: {confidence}"
                )

        return results