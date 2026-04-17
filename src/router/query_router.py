class QueryRouter:
    def __init__(self):
        # keywords that usually require LLM reasoning
        self.reasoning_keywords = [
            "compare", "why", "how", "explain", "difference", "which"
        ]

    def route(self, query: str, graph_results: list):
        q = query.lower()

        # -----------------------------
        # CASE 1: No graph results
        # -----------------------------
        if not graph_results:
            return "llm_only"

        # -----------------------------
        # CASE 2: Simple factual query
        # -----------------------------
        simple_keywords = ["what is", "define", "list", "name"]

        if any(k in q for k in simple_keywords) and len(graph_results) <= 2:
            return "graph_only"

        # -----------------------------
        # CASE 3: Reasoning required
        # -----------------------------
        if any(k in q for k in self.reasoning_keywords):
            return "graph_plus_llm"

        # -----------------------------
        # DEFAULT: hybrid
        # -----------------------------
        return "graph_plus_llm"