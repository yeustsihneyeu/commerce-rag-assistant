import sys

sys.path.append("../")

from src.core.classes import Prompt

routing_prompt = Prompt(
    model_type="ollama",
    model_name="qwen2.5:7b",
    version="1",
    variables={"query": ""},
    prompt_text="""
You are a strict classifier for a clothing store assistant.

Classify the user query into exactly one label:
- faq
- product

Definitions:
- faq: general store information, support, service rules, or policies such as returns, refunds, shipping, payment, contact methods, promotions, locations, opening hours, account help, or order support.
- product: requests that need product catalog knowledge, product search, recommendations, styling, availability, attributes, comparisons, or examples of items.

Confidence rules:
- Also estimate your confidence as a float from 0.0 to 1.0.
- Use high confidence only when the query clearly belongs to one class.
- Use low confidence when the query is vague, underspecified, off-topic, or could belong to both classes.
- Do not inflate confidence.

Examples:
- Is there a refund for incorrectly bought clothes? label=faq confidence=0.98
- Where are your stores located? label=faq confidence=0.99
- How can I contact you via phone? label=faq confidence=0.98
- Tell me about the cheapest T-shirts that you have. label=product confidence=0.98
- Do you have blue T-shirts under 100 dollars? label=product confidence=0.99
- Give me ideas for a sunny look. label=product confidence=0.93
- How old are you? label=faq confidence=0.10
- Help me with something for tomorrow. label=product confidence=0.22
- I need help. label=faq confidence=0.20

Return the result using the structured output schema.

Query to classify: {query}
    """
)
