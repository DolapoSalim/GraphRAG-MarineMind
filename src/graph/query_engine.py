import json
from typing import List, Dict, Any


class GraphQueryEngine:
    def __init__(self, graph_path: str):
        self.graph = self._load_graph(graph_path)

    # -------------------------
    # Load Graph
    # -------------------------
    def _load_graph(self, file_path: str) -> List[Dict[str, Any]]:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            raise RuntimeError(f"Failed to load graph: {e}")

    # -------------------------
    # Normalization
    # -------------------------
    def _normalize(self, text: str) -> str:
        return text.lower().strip()

    # -------------------------
    # Core Search Logic (Ranked Retrieval)
    # -------------------------
    def search(self, query: str) -> List[Dict[str, Any]]:
        query_words = self._normalize(query).split()

        scored_results = []

        for entry in self.graph:
            subject = self._normalize(entry.get("subject", ""))
            predicate = self._normalize(entry.get("predicate", ""))
            obj = self._normalize(entry.get("object", ""))
            context = self._normalize(entry.get("context", ""))

            # combine all fields into searchable text
            full_text = f"{subject} {predicate} {obj} {context}"

            # simple relevance scoring
            score = sum(1 for word in query_words if word in full_text)

            if score > 0:
                scored_results.append((score, entry))

        # sort by relevance (highest score first)
        scored_results.sort(key=lambda x: x[0], reverse=True)

        # return top-k results (important for LLM quality)
        top_results = [entry for _, entry in scored_results[:3]]

        return top_results

    # -------------------------
    # Formatting
    # -------------------------
    def format_result(self, entry: Dict[str, Any]) -> str:
        subject = entry.get("subject", "")
        predicate = entry.get("predicate", "")
        obj = entry.get("object", "")
        context = entry.get("context", "")
        source = entry.get("source", "")

        if context:
            return f"{subject} → {predicate} → {obj} ({context})"
        return f"{subject} → {predicate} → {obj}"

    # -------------------------
    # Full Query Pipeline
    # -------------------------
    def query(self, user_query: str) -> List[str]:
        results = self.search(user_query)

        if not results:
            return ["No relevant information found in graph."]

        return [self.format_result(r) for r in results]