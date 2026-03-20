import sys
sys.path.append("../")

from pydantic import BaseModel, Field
from typing import Literal

from llama_index.llms.ollama import Ollama
from llama_index.llms.openai import OpenAI


class RouteDecision(BaseModel):
    route: Literal["faq", "product"] | None
    confidence: float = Field(ge=0.0, le=1.0)


router_model_ollama = Ollama(
    model="qwen2.5:7b",
    temperature=0.1,
    
)

router_model_openai = OpenAI(model="gpt-4o-mini")

router = router_model_ollama.as_structured_llm(RouteDecision)
