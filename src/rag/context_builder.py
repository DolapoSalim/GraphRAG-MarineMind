from typing import List


class ContextBuilder:
    def build(self, graph_results: List[str], stats_results: List[str]) -> str:
        """
        Merge Tier 1 (Graph) + Tier 2 (Stats)
        into a single structured context for the LLM.
        """

        context = []

        # -------------------------
        # Tier 1: Graph knowledge
        # -------------------------
        if graph_results:
            context.append("=== GRAPH KNOWLEDGE (Tier 1) ===")
            context.extend(graph_results)

        # -------------------------
        # Tier 2: Statistical knowledge
        # -------------------------
        if stats_results:
            context.append("\n=== ECOLOGICAL TRENDS (Tier 2) ===")
            context.extend(stats_results)

        return "\n".join(context)