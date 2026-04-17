from src.graph.query_engine import GraphQueryEngine
from src.stats.stats_engine import StatsEngine
from src.rag.generator import OllamaGenerator
from src.rag.context_builder import ContextBuilder
from src.router.query_router import QueryRouter


def main():
    graph_engine = GraphQueryEngine("data/graph.json")
    stats_engine = StatsEngine("data/stats.json")
    llm = OllamaGenerator(model="phi3:mini")
    router = QueryRouter()
    builder = ContextBuilder()

    print("\nWelcome to GraphRAG MarineMind (Unified System)")
    print("Type 'exit' to quit\n")

    while True:
        query = input("Ask a question: ")

        if query.lower() == "exit":
            break

        # -------------------
        # Tier 1
        # -------------------
        graph_results = graph_engine.query(query)

        # -------------------
        # Tier 2
        # -------------------
        stats_results = stats_engine.query(query)

        # -------------------
        # Build unified context
        # -------------------
        context = builder.build(graph_results, stats_results)

        print("\n Unified Context:")
        print(context)

        # -------------------
        # Routing decision
        # -------------------
        decision = router.route(query, graph_results)

        print(f"\nRouter decision: {decision}")

        # -------------------
        # LLM reasoning
        # -------------------
        if decision == "graph_only":
            print("\nAnswer (Graph Only):")
            print("\n".join(graph_results))

        else:
            answer = llm.generate_answer(query, context)
            print("\nFinal Answer:")
            print(answer)

        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    main()