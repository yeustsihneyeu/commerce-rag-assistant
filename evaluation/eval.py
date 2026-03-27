import sys

sys.path.append("../")

import json
import math
from typing import Any

from ragas.metrics.collections import (
    ContextRelevance,
    ResponseGroundedness,
    AnswerRelevancy,
)

from evaluation.classes import (
    TestQuestion,
    ContextRelevanceWrapper,
    ResponseGroundednessWrapper,
    AnswerRelevanceWrapper,
)
from evaluation.reporting import get_node_id
from models.evaluation import openai_llm, openai_embeddings

TEST_FILE = "../../data/eval/faq_evaluation_dataset.jsonl"
PRODUCT_TEST_FILE = "../../data/eval/product_eval_dataset.jsonl"


def _has_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _has_any_text(values: list[Any]) -> bool:
    return any(_has_text(value) for value in values)


def _unique_by_node_id(nodes: list[Any], k: int) -> list[Any]:
    unique_nodes = []
    seen_node_ids = set()

    for item in nodes:
        node_id = get_node_id(item)
        if node_id in seen_node_ids:
            continue
        seen_node_ids.add(node_id)
        unique_nodes.append(item)
        if len(unique_nodes) >= k:
            break

    return unique_nodes


def evaluate_retrieval(test: TestQuestion, nodes: list, k: int = 5):
    # precision@k, recall@k, mrr, nDCG@k are computed on unique retrieved ids.
    retrieved = _unique_by_node_id(list(nodes), k=k)
    relevant_docs = set(test.relevant_docs)

    hits = []
    retrieved_ids = []

    for item in retrieved:
        node_id = get_node_id(item)
        retrieved_ids.append(node_id)
        hits.append(1 if node_id in relevant_docs else 0)

    hit_count = sum(hits)
    retrieved_count = len(retrieved)
    relevant_count = len(relevant_docs)

    precision_at_k = hit_count / retrieved_count if retrieved_count else 0.0
    recall_at_k = hit_count / relevant_count if relevant_count else 0.0

    mrr = 0.0
    for rank, hit in enumerate(hits, start=1):
        if hit:
            mrr = 1.0 / rank
            break

    dcg = sum(hit / math.log2(rank + 1) for rank, hit in enumerate(hits, start=1))
    ideal_hits = [1] * min(relevant_count, retrieved_count)
    idcg = sum(
        hit / math.log2(rank + 1) for rank, hit in enumerate(ideal_hits, start=1)
    )
    ndcg_at_k = dcg / idcg if idcg else 0.0

    return {
        "question": test.question,
        "relevant_docs": test.relevant_docs,
        "retrieved_docs": retrieved_ids,
        f"precision": precision_at_k,
        f"recall": recall_at_k,
        "mrr": mrr,
        f"ndcg": ndcg_at_k,
    }


async def context_relevance(test: ContextRelevanceWrapper):
    if not _has_text(test.question) or not _has_any_text(test.contexts):
        return 0.0
    metric = ContextRelevance(llm=openai_llm)
    result = await metric.ascore(
        user_input=test.question,
        retrieved_contexts=test.contexts,
    )
    return result.value


async def groundedness(test: ResponseGroundednessWrapper):
    if not _has_text(test.answer) or not _has_any_text(test.contexts):
        return 0.0
    metric = ResponseGroundedness(llm=openai_llm)
    result = await metric.ascore(
        response=test.answer,
        retrieved_contexts=test.contexts,
    )
    return result.value


async def answer_relevance(test: AnswerRelevanceWrapper):
    if not _has_text(test.question) or not _has_text(test.answer):
        return 0.0
    metric = AnswerRelevancy(llm=openai_llm, embeddings=openai_embeddings)
    result = await metric.ascore(user_input=test.question, response=test.answer)
    return result.value


def load_tests() -> list[TestQuestion]:
    tests = []
    with open(TEST_FILE, "r", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line.strip())
            tests.append(TestQuestion(**data))
    return tests


def product_load_tests() -> list[TestQuestion]:
    tests = []
    with open(PRODUCT_TEST_FILE, "r", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line.strip())
            tests.append(TestQuestion(**data))
    return tests
