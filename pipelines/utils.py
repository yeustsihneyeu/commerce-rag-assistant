from typing import Any

from models.generation import openai_generate
from prompts.faq_rewrite_prompts import faq_rewrite_prompt
from numbers import Real


class PipelineUtils:
    def _extract_text(self, node: Any) -> str:
        text = getattr(node, "text", None)
        if text:
            return text

        inner_node = getattr(node, "node", None)
        if inner_node is None:
            return ""

        if hasattr(inner_node, "get_content"):
            return inner_node.get_content().strip()

        return getattr(inner_node, "text", "").strip()

    def _rewrite_query(self, query: str, chat_history: str) -> str:
        if not chat_history:
            return query

        rewrite_prompt = faq_rewrite_prompt.render(
            query=query,
            chat_history=chat_history,
        )
        rewritten_query = openai_generate(rewrite_prompt).strip()
        return rewritten_query or query

    def _get_node_score(self, node: Any) -> float | None:
        score = getattr(node, "score", None)
        if isinstance(score, bool) or not isinstance(score, Real):
            return None
        return round(float(score), 4)
