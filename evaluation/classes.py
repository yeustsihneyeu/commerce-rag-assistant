from pydantic import BaseModel, Field


class TestQuestion(BaseModel):
    
    question: str = Field(description="The question to ask the RAG system")
    reference_answer: str = Field(description="The reference answer for this question")
    relevant_docs: list = Field(description="The relevant docs for the question")
