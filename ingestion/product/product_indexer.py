import os
import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from llama_index.core import Document, StorageContext, VectorStoreIndex
from dotenv import load_dotenv
from ingestion.product.product_doc_builder import build_product_llama_documents
from ingestion.product.product_json_chunker import build_product_rag_records
from src.core.transformers import ConditionalFixedChunker
from src.core.utils import ingest_pipeline
from llama_index.embeddings.openai import OpenAIEmbedding
from vectorstore.weaviate import client
from llama_index.vector_stores.weaviate import WeaviateVectorStore


# load data
# load_documents
# create chunks
# embedding
# persisit chunks in to vector store

load_dotenv(override=True)
data_path = os.getenv("PRODUCT_DATA_PATH")
data_path_output = os.getenv("PRODUCT_DATA_PATH_OUTPUT")
embedding_model = os.getenv("PRODUCT_EMBEDDING_MODEL_NAME")
collection_name = os.getenv("PRODUCT_COLLECTION_NAME")



def load_documents(path: str, output_path) -> list[dict[str, object]]:
    return build_product_rag_records(path, output_path)


def create_chunks(list: list[dict[str, object]]) -> list[Document]:
    return build_product_llama_documents(list)


def embeddings(list: list[Document]):
    transformers = [
        ConditionalFixedChunker(),
        OpenAIEmbedding(model=embedding_model),
    ]

    return ingest_pipeline(list, transformations=transformers)


def persist(nodes):
    weaviate_client = client.connect()

    try:
        if weaviate_client.collections.exists(collection_name):
            weaviate_client.collections.delete(collection_name)

        vector_store = WeaviateVectorStore(
            weaviate_client=weaviate_client,
            index_name=collection_name,
        )
        storage_context = StorageContext.from_defaults(vector_store=vector_store)

        VectorStoreIndex(
            nodes=nodes,
            storage_context=storage_context,
        )
    finally:
        weaviate_client.close()


def main():
    documents = load_documents(data_path, data_path_output)
    chunks = create_chunks(documents)
    nodes = embeddings(chunks)
    persist(nodes)


if __name__ == "__main__":
    print("=============== Start PRODUCT ingestion ===============")
    main()
    print("============= Complited PRODUCT ingestion =============")
