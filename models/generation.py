import os
import time
from dotenv import load_dotenv
from openai import OpenAI, RateLimitError
from llama_index.llms.ollama import Ollama

load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")

openai = OpenAI()


def openai_generate(prompt: str, model: str = "gpt-4.1"):
    retries = 5
    base_delay = 2.0

    for attempt in range(retries):
        try:
            response = openai.responses.create(model=model, input=prompt)
            return response.output_text
        except RateLimitError:
            if attempt == retries - 1:
                raise
            time.sleep(base_delay * (attempt + 1))


def ollama_generate(prompt: str, model: str = "qwen2.5:7b"):
    ollama = Ollama(
        model=model,
        temperature=0.1,
    )
    response = ollama.complete(prompt)
    return response.text
