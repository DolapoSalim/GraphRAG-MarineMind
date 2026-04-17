from src.graph.query_engine import GraphQueryEngine
from src.rag.generator import OllamaGenerator
from src.router.query_router import QueryRouter


def main():
    engine = GraphQueryEngine("data/graph.json")
    llm = OllamaGenerator(model="phi3:mini")
    router = QueryRouter()

    print("\n Welcome to GraphRAG Marine Mind!")
    print("Type 'exit' to quit\n")

    while True:
        query = input("Ask a question: ")

        if query.lower() == "exit":
            break

        # 1. Retrieve graph data
        results = engine.query(query)

        print("\n Retrieved Knowledge:")
        for r in results:
            print(f"- {r}")

        # 2. Decide routing
        decision = router.route(query, results)

        print(f"\n Router decision: {decision}")

        # 3. Execute based on decision
        if decision == "graph_only":
            print("\n Answer (Graph Only):")
            print("\n".join(results))

        else:
            answer = llm.generate_answer(query, results)
            print("\n Final Answer:")
            print(answer)

        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    main()