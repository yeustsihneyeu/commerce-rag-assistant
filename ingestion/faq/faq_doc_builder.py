import uuid

from llama_index.core import Document


def build_llama_documents(sections: list[dict]) -> list[Document]:
    documents = []

    for section in sections:
        header = section["header"]
        content = section["content"]
        section_id = section["section_id"]

        text = f"{header}\n{content}"

        documents.append(
            Document(
                text=text,
                doc_id=str(uuid.uuid4()),
                metadata={
                    "section_title": header,
                    "source_type": "faq",
                    "source_file": "faq.docx",
                    "section_id": section_id
                },
            )
        )

    return documents
