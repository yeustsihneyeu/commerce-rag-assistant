import os

import weaviate


def connect():
    mode = os.getenv("WEAVIATE_CONNECTION_MODE", "local").lower()

    if mode == "local":
        return weaviate.connect_to_local()

    raise ValueError(
        "Unsupported WEAVIATE_CONNECTION_MODE. Expected one of: local, cloud, custom."
    )


def local():
    return connect()
