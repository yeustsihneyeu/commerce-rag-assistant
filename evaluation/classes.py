from pydantic import BaseModel, Field
from typing import Literal


class TestQuestion(BaseModel):

    question: str = Field(description="User question used for RAG evaluation")
    reference_answer: str = Field(description="Reference answer derived from the relevant FAQ content")
    relevant_docs: list = Field(description="List of relevant document ids for the question")


class CalibrationTest(BaseModel):
    question: str = Field(description="User question used for answer-level metric calibration")
    reference_answer: str = Field(description="Reference answer derived from the supporting FAQ content")
    relevant_docs: list = Field(description="List of relevant document ids linked to the question")
    candidate_answer: str = Field(description="Candidate answer to be judged for groundedness and relevance")
    answer_type: Literal["good", "bad", "adversarial"] = Field(
        description="Synthetic answer category used in the calibration dataset"
    )
    contexts: list = Field(description="Supporting document texts used as grounding context")
    grounded_label: bool = Field(description="Gold label indicating whether the candidate answer is grounded in the context")
    relevance_label: bool = Field(description="Gold label indicating whether the candidate answer is relevant to the question")


class ContextRelevanceWrapper(BaseModel):

    question: str = Field(description="User question used to judge context relevance")
    contexts: list = Field(description="Retrieved document texts evaluated for relevance to the question")


class ResponseGroundednessWrapper(BaseModel):

    contexts: list = Field(description="Retrieved document texts used to verify answer grounding")
    answer: str = Field(description="Generated or candidate answer evaluated against the contexts")


class AnswerRelevanceWrapper(BaseModel):

    question: str = Field(description="User question used to judge answer relevance")
    answer: str = Field(description="Generated or candidate answer evaluated for relevance to the question")
