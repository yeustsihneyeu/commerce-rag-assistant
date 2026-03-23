from typing import Any

from models.generation import openai_generate
from pipelines.utils import PipelineUtils
from prompts.base_generated_prompts import base_generated_prompt


class BasePipeline(PipelineUtils):

    def _make_prompt(self, query, chat_history):
        return base_generated_prompt.render(
            query=query, chat_history=chat_history or "No previous messages."
        )

    def run(self, query: str, chat_history: str = "") -> dict[str, Any]:
        prompt = self._make_prompt(query=query, chat_history=chat_history)
        answer = openai_generate(prompt)

        return {
            "route": "base",
            "query": query,
            "chat_history": chat_history,
            "rewritten_query": query,
            "retrieval_query": query,
            "context": "",
            "prompt": prompt,
            "answer": answer,
        }
