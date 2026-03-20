from typing import Any

from models.generation import openai_generate
from prompts.faq_generate_prompts import faq_generate_prompt
from prompts.faq_rewrite_prompts import faq_rewrite_prompt
from retrieval.faq_retriever import search_faq_hybrid
from retrieval.reranker import rerank


class FaqPipeline:
    def __init__(
        self,
        retrieval_top_k: int = 5,
        rerank_top_k: int = 3,
        alpha: float = 0.5,
    ) -> None:
        self.retrieval_top_k = retrieval_top_k
        self.rerank_top_k = rerank_top_k
        self.alpha = alpha

    @staticmethod
    def _extract_text(node: Any) -> str:
        text = getattr(node, "text", None)
        if text:
            return text

        inner_node = getattr(node, "node", None)
        if inner_node is None:
            return ""

        if hasattr(inner_node, "get_content"):
            return inner_node.get_content().strip()

        return getattr(inner_node, "text", "").strip()

    def _make_prompt(self, query: str, context: str, chat_history: str) -> str:
        return faq_generate_prompt.render(
            query=query,
            context=context,
            chat_history=chat_history or "No previous messages.",
        )

    def _rewrite_query(self, query: str, chat_history: str) -> str:
        if not chat_history:
            return query

        rewrite_prompt = faq_rewrite_prompt.render(
            query=query,
            chat_history=chat_history,
        )
        rewritten_query = openai_generate(rewrite_prompt).strip()
        return rewritten_query or query

    def run(self, query: str, chat_history: str = "") -> dict[str, Any]:
        rewritten_query = self._rewrite_query(query, chat_history)
        retrieval_query = rewritten_query
        nodes = search_faq_hybrid(
            query=retrieval_query,
            top_k=self.retrieval_top_k,
            alpha=self.alpha,
        )
        reranked_nodes = rerank(retrieval_query, nodes, top_k=self.rerank_top_k)
        context_parts = []
        for node in reranked_nodes:
            text = self._extract_text(node)
            if text:
                context_parts.append(text)
        context = "\n\n".join(context_parts)
        prompt = self._make_prompt(
            query=query,
            context=context,
            chat_history=chat_history,
        )
        answer = openai_generate(prompt)

        return {
            "query": query,
            "chat_history": chat_history,
            "rewritten_query": rewritten_query,
            "retrieval_query": retrieval_query,
            "nodes": reranked_nodes,
            "context": context,
            "prompt": prompt,
            "answer": answer,
        }
