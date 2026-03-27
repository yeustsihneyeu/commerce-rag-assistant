from pydantic import BaseModel, Field, ConfigDict

from typing import Optional


class TestQuestion(BaseModel):

    model_config = ConfigDict(extra="ignore")

    question: str = Field(description="User question used for RAG evaluation")
    relevant_docs: list = Field(
        description="List of relevant document ids for the question"
    )
    reference_answer: Optional[str] = None
    contexts: Optional[list] = None
    metadata: Optional[dict] = None
    type_question: Optional[str] = None


class ContextRelevanceWrapper(BaseModel):

    question: str = Field(description="User question used to judge context relevance")
    contexts: list = Field(
        description="Retrieved document texts evaluated for relevance to the question"
    )


class ResponseGroundednessWrapper(BaseModel):

    contexts: list = Field(
        description="Retrieved document texts used to verify answer grounding"
    )
    answer: str = Field(
        description="Generated or candidate answer evaluated against the contexts"
    )


class AnswerRelevanceWrapper(BaseModel):

    question: str = Field(description="User question used to judge answer relevance")
    answer: str = Field(
        description="Generated or candidate answer evaluated for relevance to the question"
    )
