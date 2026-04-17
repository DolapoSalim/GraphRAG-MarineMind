import json


class Evaluator:
    def __init__(self, graph_engine, stats_engine):
        self.graph_engine = graph_engine
        self.stats_engine = stats_engine

    def evaluate(self, eval_file: str):
        with open(eval_file, "r") as f:
            tests = json.load(f)

        results = []

        for test in tests:
            query = test["query"]
            expected = test["expected_concepts"]

            graph_results = self.graph_engine.query(query)
            stats_results = self.stats_engine.query(query)

            retrieved_text = " ".join(graph_results + stats_results).lower()

            score = sum(1 for e in expected if e.lower() in retrieved_text)

            accuracy = score / len(expected)

            results.append({
                "query": query,
                "score": accuracy
            })

        return results