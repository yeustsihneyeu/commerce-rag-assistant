import sys
from pathlib import Path
from typing import Any

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from llama_index.core import Settings, VectorStoreIndex
from llama_index.core.vector_stores.types import VectorStoreQueryMode, MetadataFilters
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.vector_stores.weaviate import WeaviateVectorStore

from vectorstore.weaviate import client


def get_collections(collection_name: str):
    weaviate_client = client.connect()
    return weaviate_client.collections.get(collection_name)


def build_index(
    collection_name: str,
):
    weaviate_client = client.connect()
    vector_store = WeaviateVectorStore(
        weaviate_client=weaviate_client,
        index_name=collection_name,
    )
    return weaviate_client, VectorStoreIndex.from_vector_store(vector_store)


def build_retriever(
    collection_name: str,
    embedding_model_name: str,
    top_k: int,
    filters: MetadataFilters | None = None,
    query_mode: VectorStoreQueryMode = VectorStoreQueryMode.DEFAULT,
    alpha: float | None = None,
):
    Settings.embed_model = OpenAIEmbedding(model=embedding_model_name)

    weaviate_client, index = build_index(collection_name)

    return weaviate_client, index.as_retriever(
        similarity_top_k=top_k,
        vector_store_query_mode=query_mode,
        filters=filters,
        alpha=alpha,
    )


def semantic_search(
    query: str,
    collection_name: str,
    embedding_model_name: str,
    top_k: int = 3,
    filters: MetadataFilters | None = None,
) -> list[Any]:
    return retriever_search(
        query=query,
        collection_name=collection_name,
        embedding_model_name=embedding_model_name,
        query_mode=VectorStoreQueryMode.DEFAULT,
        filters=filters,
        top_k=top_k,
    )


def retriever_search(
    query: str,
    collection_name: str,
    embedding_model_name: str,
    query_mode: VectorStoreQueryMode,
    filters: MetadataFilters | None = None,
    top_k: int = 3,
    alpha: float | None = None,
) -> list[Any]:
    weaviate_client, retriever = build_retriever(
        collection_name=collection_name,
        embedding_model_name=embedding_model_name,
        top_k=top_k,
        query_mode=query_mode,
        alpha=alpha,
        filters=filters,
    )

    try:
        return retriever.retrieve(query)
    finally:
        weaviate_client.close()


def service_search(
    query: str,
    collection_name: str,
    embedding_model_name: str,
    method_name: str,
    filters: MetadataFilters | None = None,
    top_k: int = 3,
    alpha: float = 0.5,
):
    query_mode_by_method = {
        "semantic_search": VectorStoreQueryMode.DEFAULT,
        "keyword_search": VectorStoreQueryMode.TEXT_SEARCH,
        "hybrid_search": VectorStoreQueryMode.HYBRID,
    }

    query_mode = query_mode_by_method.get(method_name)
    if query_mode is None:
        raise ValueError(f"Unsupported search method: {method_name}")

    return retriever_search(
        query=query,
        collection_name=collection_name,
        embedding_model_name=embedding_model_name,
        query_mode=query_mode,
        filters=filters,
        top_k=top_k,
        alpha=alpha if query_mode == VectorStoreQueryMode.HYBRID else None,
    )
