from retrieval.base_retriever import semantic_search, service_search
from src.core.utils import get_required_env


def search_faq(query: str, top_k: int = 3):
    return semantic_search(
        query=query,
        collection_name=get_required_env("FAQ_COLLECTION_NAME"),
        embedding_model_name=get_required_env("FAQ_EMBEDDING_MODEL_NAME"),
        top_k=top_k,
    )


def search_faq_keyword(query: str, top_k: int = 3):
    return service_search(
        query=query,
        collection_name=get_required_env("FAQ_COLLECTION_NAME"),
        embedding_model_name=get_required_env("FAQ_EMBEDDING_MODEL_NAME"),
        method_name="keyword_search",
        top_k=top_k,
    )


def search_faq_hybrid(query: str, top_k: int = 3, alpha: float = 0.5):
    return service_search(
        query=query,
        collection_name=get_required_env("FAQ_COLLECTION_NAME"),
        embedding_model_name=get_required_env("FAQ_EMBEDDING_MODEL_NAME"),
        method_name="hybrid_search",
        top_k=top_k,
        alpha=alpha,
    )

