# Commerce RAG Assistant

Hybrid RAG project for an e-commerce assistant with FAQ retrieval, query rewriting, reranking, and route classification between FAQ and product intents.

## What This Project Does

- indexes FAQ and product data for retrieval
- routes user queries by domain (`faq`, `product`, or `none`)
- runs a hybrid FAQ retrieval pipeline with reranking
- generates answers with an LLM using retrieved context
- provides a local Gradio chat UI for FAQ experiments
- includes notebooks and evaluation reports for retrieval, answer quality, and routing quality

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
3. Evaluate retrieval, answer quality, and routing quality through notebooks and generated reports
4. Run `app.py` to validate the end-to-end FAQ experience

## Evaluation

The repository contains simple notebook-based evaluation flows for the FAQ pipeline.

Implemented evaluations:

- `notebooks/08_faq_retrieve_evaluating.ipynb`
  - retrieval metrics: `precision@k`, `recall@k`, `mrr`, `ndcg@k`
  - context quality metric: `context_relevance`
  - exported report: `reports/faq_retrieving_evaluation.md`
- `notebooks/09_faq_reranking_evaluating.ipynb`
  - compares retrieval metrics before and after reranking
  - exported report: `reports/faq_reranking_evaluation.md`
- `notebooks/12_faq_groundedness_evaluating.ipynb`
  - generation quality metric: `groundedness`
  - exported report: `reports/faq_groundedness_evaluation.md`
- `notebooks/13_faq_answer_relevance_evaluating.ipynb`
  - generation quality metric: `answer_relevance`
  - exported report: `reports/faq_answer_relevance_evaluation.md`
- `notebooks/06_class_routing.ipynb`
  - class/domain routing evaluation
  - exported report: `reports/class_routing_evaluation.md`

Notes:

- Retrieval notebooks show `score` from the hybrid retriever.
- Groundedness and answer relevance notebooks show `rerank_score`, which is the internal reranker score for a chunk. It is not normalized and should not be interpreted like a quality metric.
- `context_relevance`, `groundedness`, and `answer_relevance` are evaluated with `ragas`.

See `notebooks/` for experiments and `reports/` for exported results.

## Notes

- The repo currently looks research-oriented: notebooks and evaluation artifacts are a major part of the workflow.
- `ProductPipeline` and `ChatPipeline` are not fully implemented yet, so the main usable entry point is the FAQ assistant.
- If you plan to publish the repo, consider adding:
  - `.env.example`
  - explicit ingestion commands or scripts
  - architecture diagram
  - tests
