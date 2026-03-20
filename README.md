# Commerce RAG Assistant

Hybrid RAG project for an e-commerce assistant with FAQ retrieval, query rewriting, reranking, and route classification between FAQ and product intents.

## What This Project Does

- indexes FAQ and product data for retrieval
- routes user queries by domain (`faq`, `product`, or `none`)
- runs a hybrid FAQ retrieval pipeline with reranking
- generates answers with an LLM using retrieved context
- provides a local Gradio chat UI for FAQ experiments
- includes notebooks and evaluation reports for retrieval and routing quality

## Current Status

The FAQ flow is the most complete part of the repository.

- `app.py` runs a local Gradio interface backed by `FaqPipeline`
- `pipelines/faq_pipeline.py` rewrites follow-up questions, retrieves FAQ chunks, reranks them, and generates an answer
- product and unified chat pipelines exist, but are still scaffolds in the current codebase

## Tech Stack

- Python
- LlamaIndex
- Weaviate
- OpenAI and Ollama integrations
- Gradio
- pandas
- sentence-transformers

## Project Structure

- `app.py` - local Gradio app
- `pipelines/` - FAQ, product, and chat pipelines
- `retrieval/` - retrievers and reranker
- `routing/` - intent/domain routing
- `ingestion/` - FAQ and product parsing, chunking, and indexing
- `prompts/` - prompt templates for routing, rewriting, and answer generation
- `models/` - model integration for generation and routing
- `evaluation/` - evaluation helpers
- `reports/` - generated evaluation reports
- `notebooks/` - experiments and pipeline prototyping
- `data/` - raw, processed, and eval data
- `vectorstore/` - vector database integration

## Requirements

- Python 3.11+ recommended
- Docker, if you want to run Weaviate locally
- API credentials in `.env` for the providers you use

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a local `.env` file for secrets and runtime configuration.

Minimal example:

```env
OPENAI_API_KEY=your_key_here
```

Add any Ollama or local model settings you use in your environment.

## Run Weaviate

The repository includes a minimal local Weaviate setup:

```bash
docker compose up -d
```

This exposes Weaviate on `http://localhost:8080`.

## Run The App

Start the local FAQ assistant UI:

```bash
python app.py
```

The app opens a Gradio interface for testing the FAQ pipeline.

## Development Workflow

Typical flow in this repository:

1. Prepare or update source documents in `data/raw/`
2. Use ingestion modules or notebooks to parse, chunk, and index data
3. Evaluate retrieval/routing quality through notebooks and generated reports
4. Run `app.py` to validate the end-to-end FAQ experience

## Evaluation

The repository contains notebooks and generated reports for:

- FAQ retrieval evaluation
- FAQ reranking evaluation
- class/domain routing evaluation

See `notebooks/` for experiments and `reports/` for exported results.

## Notes

- The repo currently looks research-oriented: notebooks and evaluation artifacts are a major part of the workflow.
- `ProductPipeline` and `ChatPipeline` are not fully implemented yet, so the main usable entry point is the FAQ assistant.
- If you plan to publish the repo, consider adding:
  - `.env.example`
  - explicit ingestion commands or scripts
  - architecture diagram
  - tests

