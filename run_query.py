from src.graph.query_engine import GraphQueryEngine
from src.rag.generator import OllamaGenerator


def main():
    engine = GraphQueryEngine("data/graph.json")
    llm = OllamaGenerator(model="phi3:mini")

    print("\n Welcome to GraphRAG Marine Mind")
    print("Type 'exit' to quit\n")

    while True:
        query = input("Ask a question: ")

        if query.lower() == "exit":
            break

        # 1. Retrieve graph knowledge
        results = engine.query(query)

        print("\n Retrieved Knowledge:")
        for r in results:
            print(f"- {r}")

        # 2. Generate grounded answer using Phi
        answer = llm.generate_answer(query, results)

        print("\n Final Answer:")
        print(answer)
        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    main()