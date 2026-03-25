import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from ragas.embeddings import OpenAIEmbeddings
from ragas.llms import llm_factory

load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")


client = AsyncOpenAI()

openai_llm = llm_factory(
    model="gpt-4.1",
    client=client,
)

openai_embeddings = OpenAIEmbeddings(
    client=client,
    model="text-embedding-3-small",
)
