from src.core.classes import Prompt


faq_rewrite_prompt = Prompt(
    model_type="foundation",
    model_name="gpt-4.1",
    version="1",
    variables={"query": "", "chat_history": ""},
    prompt_text="""
You rewrite the latest user question for FAQ retrieval.

Your task:
- If the latest user question depends on the chat history, rewrite it into a standalone question.
- If the latest user question is already self-contained, return it unchanged.
- Keep the same language as the latest user question.
- Return only the rewritten question, with no explanation.

Chat history:
{chat_history}

Latest user question:
{query}
"""
)
