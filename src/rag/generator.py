import requests
from typing import List


class OllamaGenerator:
    def __init__(self, model: str = "phi3:mini", host: str = "http://localhost:11434"):
        self.model = model
        self.url = f"{host}/api/generate"

    def generate_answer(self, query: str, context: str) -> str:
        prompt = f"""
    You are a marine ecology research assistant.

    You MUST follow these rules:
    1. Use ONLY the provided context
    2. Do NOT add external knowledge
    3. Be concise and scientific
    4. No repetition
    5. No storytelling

    FORMAT YOUR ANSWER LIKE THIS:

    - Direct Answer:
    Provide a concise list of methods or concepts.

    - Evidence from Graph:
    List the relevant graph relationships exactly as given.

    - Ecological Interpretation:
    Brief scientific explanation (2–3 sentences max).

    ----------------------

    CONTEXT:
    {context}

    QUESTION:
    {query}

    ANSWER:
    """

        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": 180
                }
            }
        )

        if response.status_code != 200:
            raise RuntimeError(response.text)

        return response.json()["response"].strip()