import json
import uuid

from llama_index.core import Document


EMBED_METADATA_KEYS = [
    "product_id",
    "brand",
    "color",
    "category",
    "top_type",
    "bottom_type",
    "dupatta",
    "pattern",
    "shape",
    "neck",
    "sleeves",
    "length",
    "hemline",
    "top_fabric",
    "bottom_fabric",
    "dupatta_fabric",
    "occasion",
    "wash_care",
]

EXCLUDED_EMBED_METADATA_KEYS = [
    "source_type",
    "price",
    "rating_count",
    "avg_rating",
    "image_url",
    "raw_attributes",
]

EXCLUDED_LLM_METADATA_KEYS = [
    "image_url",
    "raw_attributes",
]


def build_product_uuid(product_id: str) -> str:
    """Generate a stable UUID acceptable to Weaviate for a product record."""
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"fashion_catalog:{product_id}"))


def build_product_llama_documents(records: list[dict[str, object]]) -> list[Document]:
    documents = []

    for record in records:
        product_id = record.get("product_id")
        text = record.get("text")

        if not product_id or not text:
            continue

        product_id = str(product_id)
        metadata = {
            "source_type": "fashion_catalog",
            "product_id": product_id,
        }

        for key in EMBED_METADATA_KEYS:
            value = record.get(key)
            if value is not None:
                metadata[key] = value

        for key in ("price", "rating_count", "avg_rating", "image_url"):
            value = record.get(key)
            if value is not None:
                metadata[key] = value

        raw_attributes = record.get("attributes")
        if raw_attributes:
            metadata["raw_attributes"] = json.dumps(raw_attributes, ensure_ascii=False, sort_keys=True)

        documents.append(
            Document(
                text=str(text),
                doc_id=build_product_uuid(product_id),
                metadata=metadata,
                excluded_embed_metadata_keys=EXCLUDED_EMBED_METADATA_KEYS,
                excluded_llm_metadata_keys=EXCLUDED_LLM_METADATA_KEYS,
            )
        )

    return documents
