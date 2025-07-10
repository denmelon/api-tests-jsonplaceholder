post_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["userId", "id", "title", "body"]
}

post_creation_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "body": {"type": "string"},
        "userId": {"type": "integer"},
        "id": {"type": "integer"}
    },
    "required": ["title", "body", "userId", "id"]
}