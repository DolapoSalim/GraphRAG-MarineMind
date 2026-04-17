import requests
from typing import List


class OllamaGenerator:
    def __init__(self, model: str = "phi3:mini", host: str = "http://localhost:11434"):
        self.model = model
        self.url = f"{host}/api/generate"

    def generate_answer(self, query: str, context: List[str]) -> str:
        """
        Generate grounded ecological answers using Phi via Ollama.
        """

        # Step 1: compress graph output into context
        context_text = "\n".join(context)

        # Step 2: strict grounding prompt (IMPORTANT)
        prompt = f"""
You are an expert ecological AI assistant for marine ecosystem analysis.

You MUST follow these rules:
- Only use the provided context
- Do NOT invent new facts
- If information is missing, say "not available in graph data"

Context:
{context_text}

Question:
{query}

Provide a clear, scientifically accurate explanation.
Focus on ecological interpretation (not general definitions).
"""

        # Step 3: call Ollama API
        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )

        if response.status_code != 200:
            raise RuntimeError(f"Ollama error: {response.text}")

        return response.json()["response"].strip()