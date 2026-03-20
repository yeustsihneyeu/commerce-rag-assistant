import sys
sys.path.append("../")
from prompts.routing_prompts import routing_prompt
from models.routing import RouteDecision, router


def generate(query: str) -> RouteDecision:

    try:
        return router.complete(query).raw

    except Exception as e:
        
        print(f"Routing failed: {e}")

        return RouteDecision(
            route=None,
            confidence=0.0,
        )
    

def apply_confidence_threshold(response: RouteDecision, threshold):
    if response.confidence < threshold:
        return None, response.confidence

    return response.route, response.confidence


def make_prompt(query) -> str:
    return routing_prompt.render(query=query)


def get_class_query(query, threshold = 0.65) -> str:
    prompt = make_prompt(query)
    response = generate(prompt)
    route, confidence = apply_confidence_threshold(response, threshold)
    return route, confidence
