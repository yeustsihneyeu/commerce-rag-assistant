import sys
sys.path.append("../")

import json
import math
from typing import Any

from evaluation.classes import TestQuestion

TEST_FILE = "../data/eval/faq_evaluation_dataset.jsonl"


def _get_node_metadata(item: Any) -> dict[str, Any]:
    if hasattr(item, "node"):
        return getattr(item.node, "metadata", {}) or {}
    return getattr(item, "metadata", {}) or {}


def _get_section_id(item: Any) -> Any:
    metadata = _get_node_metadata(item)
    return metadata.get("section_id")


def _unique_by_section_id(nodes: list[Any], k: int) -> list[Any]:
    unique_nodes = []
    seen_section_ids = set()

    for item in nodes:
        section_id = _get_section_id(item)
        if section_id in seen_section_ids:
            continue
        seen_section_ids.add(section_id)
        unique_nodes.append(item)
        if len(unique_nodes) >= k:
            break

    return unique_nodes


def evaluate_retrieval(test: TestQuestion, nodes: list, k: int = 5):
    # precision@k, recall@k, mrr, nDCG@k are computed on unique section ids.
    retrieved = _unique_by_section_id(list(nodes), k=k)
    relevant_docs = set(test.relevant_docs)

    hits = []
    retrieved_ids = []

    for item in retrieved:
        section_id = _get_section_id(item)
        retrieved_ids.append(section_id)
        hits.append(1 if section_id in relevant_docs else 0)

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
    idcg = sum(hit / math.log2(rank + 1) for rank, hit in enumerate(ideal_hits, start=1))
    ndcg_at_k = dcg / idcg if idcg else 0.0

    return {
        "question": test.question,
        "relevant_docs": test.relevant_docs,
        "retrieved_docs": retrieved_ids,
        f"precision@{k}": precision_at_k,
        f"recall@{k}": recall_at_k,
        "mrr": mrr,
        f"ndcg@{k}": ndcg_at_k,
    }


def groundedness(context, response):
    del context, response
    raise NotImplementedError("groundedness is not implemented yet")


def answer_relevance(query, response):
    del query, response
    raise NotImplementedError("answer_relevance is not implemented yet")


def load_tests() -> list[TestQuestion]:
    tests = []
    with open(TEST_FILE, "r", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line.strip())
            tests.append(TestQuestion(**data))
    return tests
