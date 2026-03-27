import json
from retrieval.base_retriever import semantic_search, service_search
from src.core.utils import get_required_env
from llama_index.core.vector_stores.types import (
    MetadataFilter,
    MetadataFilters,
    FilterOperator,
)
from models.generation import openai_generate
from prompts.metadata_extract_prompt import metadata_extract_prompt


def search_product(query: str, top_k: int = 3):
    return semantic_search(
        query=query,
        collection_name=get_required_env("PRODUCT_COLLECTION_NAME"),
        embedding_model_name=get_required_env("PRODUCT_EMBEDDING_MODEL_NAME"),
        top_k=top_k,
    )


def search_product_keyword(query: str, top_k: int = 3):
    return service_search(
        query=query,
        collection_name=get_required_env("PRODUCT_COLLECTION_NAME"),
        embedding_model_name=get_required_env("PRODUCT_EMBEDDING_MODEL_NAME"),
        method_name="keyword_search",
        top_k=top_k,
    )


def search_product_hybrid(
    query: str,
    top_k: int = 3,
    alpha: float = 0.5,
    filters: MetadataFilters | None = None,
):
    return service_search(
        query=query,
        collection_name=get_required_env("PRODUCT_COLLECTION_NAME"),
        embedding_model_name=get_required_env("PRODUCT_EMBEDDING_MODEL_NAME"),
        method_name="hybrid_search",
        top_k=top_k,
        alpha=alpha,
        filters=filters,
    )


METADATA_FIELDS = [
    "brand",
    "color",
    "occasion",
]


def _metadata_to_llamaindex_filters(metadata: dict) -> MetadataFilters | None:
    filters = []

    for field in METADATA_FIELDS:
        values = metadata.get(field, [])
        if not values:
            continue

        if len(values) == 1:
            filters.append(
                MetadataFilter(
                    key=field,
                    value=values[0],
                    operator=FilterOperator.EQ,
                )
            )
        else:
            filters.append(
                MetadataFilters(
                    filters=[
                        MetadataFilter(
                            key=field,
                            value=value,
                            operator=FilterOperator.EQ,
                        )
                        for value in values
                    ],
                    condition="or",
                )
            )

    price = metadata.get("price", {"min": 0, "max": "inf"})
    min_price = price.get("min", 0)
    max_price = price.get("max", "inf")

    if min_price not in (None, 0):
        filters.append(
            MetadataFilter(
                key="price",
                value=float(min_price),
                operator=FilterOperator.GTE,
            )
        )

    if max_price not in (None, "inf"):
        filters.append(
            MetadataFilter(
                key="price",
                value=float(max_price),
                operator=FilterOperator.LTE,
            )
        )

    if not filters:
        return None

    return MetadataFilters(filters=filters)


def metadata_extractor(query: str) -> MetadataFilters | None:
    prompt = metadata_extract_prompt.render(query=query)
    response = openai_generate(prompt)
    metadata = json.loads(response)
    return _metadata_to_llamaindex_filters(metadata)
