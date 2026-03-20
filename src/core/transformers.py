from typing import List

from llama_index.core.schema import TransformComponent, BaseNode, Document
from llama_index.core.node_parser import TokenTextSplitter

from pydantic import PrivateAttr


class ConditionalFixedChunker(TransformComponent):
    max_chars: int = 1500
    chunk_size: int = 512
    chunk_overlap: int = 50

    _splitter: TokenTextSplitter = PrivateAttr()

    def __init__(self, **data):
        super().__init__(**data)
        self._splitter = TokenTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
        )

    def __call__(self, nodes: List[BaseNode], **kwargs) -> List[BaseNode]:
        result_nodes = []

        for node in nodes:
            text = node.text or ""

            if len(text) <= self.max_chars:
                result_nodes.append(node)
                continue

            split_nodes = self._splitter.get_nodes_from_documents([
                Document(
                    text=text,
                    metadata=node.metadata,
                    doc_id=node.node_id,
                )
            ])

            for i, split_node in enumerate(split_nodes, start=1):
                split_node.metadata = {
                    **(node.metadata or {}),
                    "parent_node_id": node.node_id,
                    "subchunk_id": i,
                }

            result_nodes.extend(split_nodes)

        return result_nodes