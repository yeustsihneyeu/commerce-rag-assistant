from pipelines.faq_pipeline import FaqPipeline
from pipelines.utils import PipelineUtils
from pipelines.base_pipeline import BasePipeline


class ChatPipeline(PipelineUtils):
    def __init__(
        self,
        domain_router,
        faq_pipeline: FaqPipeline,
        # product_pipeline,
        base_pipeline: BasePipeline,
    ):
        self.domain_router = domain_router
        self.faq_pipeline = faq_pipeline
        # self.product_pipeline = product_pipeline
        self.base_pipeline = base_pipeline

    def run(self, query: str, chat_history: str = ""):
        rewritten_query = self._rewrite_query(query, chat_history)
        route_decision = self.domain_router.get_class_query(rewritten_query)
        route, _ = getattr(route_decision, "route", route_decision)

        print(route)
        if route == "faq":
            return self.faq_pipeline.run(
                query=rewritten_query,
                chat_history=chat_history,
            )

        return self.base_pipeline.run(
            query=rewritten_query,
            chat_history=chat_history,
        )
