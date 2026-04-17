import json
from typing import List, Dict


class GraphQueryEngine:
    def __init__(self, graph_path: str):
        self.graph = self._load_graph(graph_path)

    def _load_graph(self, file_path: str) -> List[Dict]:
        """Load graph data from a JSON file."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data
        except Exception as e:
            raise RuntimeError(f"Failed to load graph: {e}")

    def _normalize(self, text: str) -> str:
        """Normalize text for comparison."""
        return text.lower().strip()

    def _match_entry(self, query_words: List[str], entry: Dict) -> bool:
        """Check if any query word matches subject, predicate, or object."""
        subject = self._normalize(entry.get("subject", ""))
        predicate = self._normalize(entry.get("predicate", ""))
        obj = self._normalize(entry.get("object", ""))

        for word in query_words:
            if word in subject or word in predicate or word in obj:
                return True
        return False

    def search(self, query: str) -> List[Dict]:
        """Search the graph for relevant entries."""
        query_words = self._normalize(query).split()

        results = []
        for entry in self.graph:
            if self._match_entry(query_words, entry):
                results.append(entry)

        return results

    def format_result(self, entry: Dict) -> str:
        """Format a graph entry into a readable string."""
        subject = entry.get("subject", "")
        predicate = entry.get("predicate", "")
        obj = entry.get("object", "")
        context = entry.get("context", "")

        if context:
            return f"{subject} → {predicate} → {obj} ({context})"
        return f"{subject} → {predicate} → {obj}"

    def query(self, user_query: str) -> List[str]:
        """Full query pipeline: search + format."""
        results = self.search(user_query)

        if not results:
            return ["No relevant information found."]

        return [self.format_result(r) for r in results]