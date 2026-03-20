from llama_index.core.schema import NodeWithScore
from llama_index.core.postprocessor import SentenceTransformerRerank
from src.core.utils import get_required_env


def rerank(query: str, nodes: list, top_k: int = 3) -> list[NodeWithScore]:
    reranker = SentenceTransformerRerank(top_n=top_k, model=get_required_env("RERANK_MODEL_NAME"), keep_retrieval_score=True)
    reranked_nodes = reranker.postprocess_nodes(nodes=nodes, query_str=query)
    return reranked_nodes
