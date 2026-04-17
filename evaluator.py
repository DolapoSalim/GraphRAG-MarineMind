import sys
from src.graph.query_engine import GraphQueryEngine
from src.stats.stats_engine import StatsEngine


EVAL_SET = [
    {
        "query": "What methods estimate seagrass extent?",
        "expected": ["sentinel", "satellite", "seagrass"]
    },
    {
        "query": "What affects seagrass health?",
        "expected": ["temperature", "eutrophication", "human"]
    },
    {
        "query": "What indicates ecosystem health?",
        "expected": ["biodiversity", "seagrass"]
    }
]


def evaluate():
    print("\n Starting GraphRAG-MarineMind Evaluation...\n")

    try:
        graph = GraphQueryEngine("data/graph.json")
        stats = StatsEngine("data/stats.json")
    except Exception as e:
        print(f" Failed to initialize engines: {e}")
        sys.exit(1)

    total_score = 0

    for i, test in enumerate(EVAL_SET, 1):
        query = test["query"]
        expected = test["expected"]

        print(f"\n Test {i}")
        print(f"Query: {query}")

        try:
            graph_results = graph.query(query)
            stats_results = stats.query(query)
        except Exception as e:
            print(f" Error during query: {e}")
            continue

        combined = " ".join(graph_results + stats_results).lower()

        # Debug: show what system retrieved
        print("\nRetrieved:")
        for r in graph_results:
            print(f"- [Graph] {r}")
        for r in stats_results:
            print(f"- [Stats] {r}")

        # Scoring
        matches = [e for e in expected if e in combined]
        score = len(matches) / len(expected)

        total_score += score

        print(f"\nExpected keywords: {expected}")
        print(f"Matched: {matches}")
        print(f"Score: {score:.2f}")

        print("-" * 50)

    avg_score = total_score / len(EVAL_SET)

    print("\n FINAL RESULTS")
    print(f"Average Accuracy: {avg_score:.2f}")
    print("\n Evaluation complete.\n")


if __name__ == "__main__":
    evaluate()