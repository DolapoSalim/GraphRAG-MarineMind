from src.graph.query_engine import GraphQueryEngine
from src.rag.generator import OllamaGenerator
from src.router.query_router import QueryRouter
from src.stats.stats_engine import StatsEngine


def main():
    graph_engine = GraphQueryEngine("data/graph.json")
    stats_engine = StatsEngine("data/stats.json")
    llm = OllamaGenerator(model="phi3:mini")
    router = QueryRouter()

    print("\n Welcome to GraphRAG MarineMind")
    print("Type 'exit' to quit\n")

    while True:
        query = input("Ask a question: ")

        if query.lower() == "exit":
            break

        # -------------------
        # Tier 1: Graph
        # -------------------
        graph_results = graph_engine.query(query)

        # -------------------
        # Tier 2: Stats
        # -------------------
        stats_results = stats_engine.query(query)

        print("\n Tier 1 (Graph):")
        for r in graph_results:
            print(f"- {r}")

        print("\n Tier 2 (Stats):")
        for r in stats_results:
            print(f"- {r}")

        # -------------------
        # Router decision
        # -------------------
        decision = router.route(query, graph_results)

        print(f"\n Router decision: {decision}")

        # -------------------
        # LLM reasoning
        # -------------------
        if decision == "graph_only":
            print("\n Answer (Graph Only):")
            print("\n".join(graph_results))

        else:
            answer = llm.generate_answer(
                query,
                graph_results + stats_results
            )
            print("\n Final Answer:")
            print(answer)

        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    main()