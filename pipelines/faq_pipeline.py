from typing import Any

from models.generation import openai_generate
from retrieval.faq_retriever import search_faq_hybrid
from retrieval.reranker import rerank
from pipelines.utils import PipelineUtils
from prompts.faq_generate_prompts import faq_generate_prompt


class FaqPipeline(PipelineUtils):
    def __init__(
        self,
        retrieval_top_k: int = 5,
        rerank_top_k: int = 3,
        alpha: float = 0.5,
    ) -> None:
        self.retrieval_top_k = retrieval_top_k
        self.rerank_top_k = rerank_top_k
        self.alpha = alpha

    def _make_prompt(self, query: str, context: str, chat_history: str) -> str:
        return faq_generate_prompt.render(
            query=query,
            context=context,
            chat_history=chat_history or "No previous messages.",
        )

    def run(self, query: str, chat_history: str = "") -> dict[str, Any]:
        retrieval_query = query
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
            "route": "faq",
            "query": query,
            "chat_history": chat_history,
            "rewritten_query": query,
            "retrieval_query": retrieval_query,
            "nodes": reranked_nodes,
            "context": context,
            "prompt": prompt,
            "answer": answer,
        }
