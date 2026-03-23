from pydantic import BaseModel, Field


class TestQuestion(BaseModel):

    question: str = Field(description="The question to ask the RAG system")
    reference_answer: str = Field(description="The reference answer for this question")
    relevant_docs: list = Field(description="The relevant docs for the question")


class ContextRelevanceWrapper(BaseModel):

    question: str = Field(description="The question to ask the RAG system")
    contexts: list = Field(description="The retrieved docs for the question")


class ResponseGroundednessWrapper(BaseModel):

    contexts: list = Field(description="The retrieved docs for the question")
    answer: str = Field(description="The final answer for the question")


class AnswerRelevanceWrapper(BaseModel):

    question: str = Field(description="The question to ask the RAG system")
    answer: str = Field(description="The final answer for the question")
