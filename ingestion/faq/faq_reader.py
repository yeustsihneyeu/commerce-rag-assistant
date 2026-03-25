from llama_index.core.readers.base import BaseReader

from ingestion.faq.faq_doc_builder import build_llama_documents
from ingestion.faq.faq_chunker import parse_faq_docx


class FaqDocxReader(BaseReader):
    def load_data(self, file: str, extra_info: dict | None = None):
        sections = parse_faq_docx(path=file)
        documents = build_llama_documents(sections)

        if extra_info:
            for document in documents:
                document.metadata.update(extra_info)

        return documents
