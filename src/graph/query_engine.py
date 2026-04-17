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
    # Tokenization
    # -------------------------
    def _tokenize(self, text: str) -> List[str]:
        return self._normalize(text).replace("_", " ").split()

    # -------------------------
    # Intent Detection
    # -------------------------
    def _detect_intent(self, query: str) -> str:
        q = query.lower()

        if any(word in q for word in ["method", "estimate", "measure", "map"]):
            return "method"

        if any(word in q for word in ["cause", "affect", "driver", "impact"]):
            return "driver"

        if any(word in q for word in ["indicate", "indicator", "signal"]):
            return "indicator"

        return "general"

    # -------------------------
    # Core Search Logic
    # -------------------------
    def search(self, query: str) -> List[Dict[str, Any]]:
        query_words = self._tokenize(query)
        intent = self._detect_intent(query)

        scored_results = []

        for entry in self.graph:
            subject = entry.get("subject", "")
            predicate = entry.get("predicate", "")
            obj = entry.get("object", "")
            context = entry.get("context", "")

            subject_tokens = self._tokenize(subject)
            predicate_tokens = self._tokenize(predicate)
            object_tokens = self._tokenize(obj)
            context_tokens = self._tokenize(context)

            # -------------------------
            # Intent-based filtering
            # -------------------------
            if intent == "method":
                if predicate not in ["estimates", "detects", "maps"]:
                    continue

            elif intent == "driver":
                if predicate not in ["causes", "impacts"]:
                    continue

            elif intent == "indicator":
                if predicate not in ["indicates"]:
                    continue

            # -------------------------
            # Weighted scoring
            # -------------------------
            score = 0

            for word in query_words:
                if word in object_tokens:
                    score += 3
                elif word in subject_tokens:
                    score += 2
                elif word in predicate_tokens:
                    score += 1
                elif word in context_tokens:
                    score += 1

            # -------------------------
            # Phrase boost
            # -------------------------
            full_text = " ".join(subject_tokens + predicate_tokens + object_tokens)
            if " ".join(query_words) in full_text:
                score += 3

            # -------------------------
            # Threshold filter
            # -------------------------
            if score >= 2:
                scored_results.append((score, entry))

        # -------------------------
        # Sort results
        # -------------------------
        scored_results.sort(key=lambda x: x[0], reverse=True)

        # -------------------------
        # Return top-k
        # -------------------------
        top_k = 3
        return [entry for _, entry in scored_results[:top_k]]

    # -------------------------
    # Formatting
    # -------------------------
    def format_result(self, entry: Dict[str, Any]) -> str:
        subject = entry.get("subject", "")
        predicate = entry.get("predicate", "")
        obj = entry.get("object", "")
        source = entry.get("source", "")

        if source:
            return f"{subject} → {predicate} → {obj} [source: {source}]"
        return f"{subject} → {predicate} → {obj}"

    # -------------------------
    # Full Query Pipeline
    # -------------------------
    def query(self, user_query: str) -> List[str]:
        results = self.search(user_query)

        if not results:
            return ["No relevant information found in graph."]

        return [self.format_result(r) for r in results]