class ChatPipeline:
    def __init__(
        self,
        domain_router,
        faq_pipeline,
        product_pipeline,
    ):
        self.domain_router = domain_router
        self.faq_pipeline = faq_pipeline
        self.product_pipeline = product_pipeline

    def run(self, user_query: str):
        route = self.domain_router.route(user_query)
        pass