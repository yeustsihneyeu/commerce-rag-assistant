import os
from llama_index.core.ingestion import IngestionPipeline
from dotenv import load_dotenv


load_dotenv(override=True)

def ingest_pipeline(documents, transformations):
    pipeline = IngestionPipeline(
        transformations=transformations,
    )

    nodes = pipeline.run(documents=documents)
    return nodes


def get_required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")
    return value


def generate_params_dict(
    prompt: str,
    model: str,
    temperature: float = 1.0,
    role: str = 'user',
    top_p: float = 1.0,
    max_tokens: int = 500,
) -> dict:
    # Create the dictionary with the necessary parameters
    kwargs = {
        "prompt": prompt,
        "role": role,
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": max_tokens,
        "model": model
    }
    return kwargs