# app/ollama_client.py

from ollama import chat
from app.config import MODEL_NAME


class OllamaClient:

    def get_response(self, messages):
        try:
            response = chat(
                model=MODEL_NAME,
                messages=messages
            )

            return response["message"]["content"]

        except Exception as e:
            return f"❌ Error: {e}"