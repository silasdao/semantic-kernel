# Copyright (c) Microsoft. All rights reserved.

from datetime import datetime

# These responses are modeled after the OpenAI REST API


def create_completion_response(
    completion_text, model, num_prompt_tokens, num_completion_tokens
):
    return [{"generated_text": completion_text}]


def create_embedding_indices(embeddings):
    index = 0
    data_entries = []
    for embedding in embeddings:
        data_entries.append(
            {"object": "embedding", "index": index, "embedding": embedding.tolist()}
        )
        index = index + 1
    return data_entries


def create_embedding_response(embeddings, num_prompt_tokens):
    data_entries = create_embedding_indices(embeddings)
    return {
        "object": "list",
        "data": data_entries,
        "usage": {
            "prompt_tokens": num_prompt_tokens,
            "total_tokens": num_prompt_tokens,
        },
    }


def create_image_gen_response(image_data):
    return {"created": datetime.now(), "data": image_data}
