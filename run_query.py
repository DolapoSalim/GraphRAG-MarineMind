from src.graph.query_engine import GraphQueryEngine


def main():
    engine = GraphQueryEngine("data/graph.json")

    print("\nWelcome to GraphRAG Query Engine")
    print("Type 'exit' to quit\n")

    while True:
        query = input("Ask a question: ")

        if query.lower() == "exit":
            break

        results = engine.query(query)

        print("\nResults:")
        for res in results:
            print(f"- {res}")
        print()


if __name__ == "__main__":
    main()