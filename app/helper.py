from jsonschema import ValidationError, validate

from error import UnsupportedRequestError

VALIDTION_SCHEMA = {
    "song": {
        "type": "object",
        "properties": {
            "duration": {"type": "integer",
                         "minimum": 0},
            "name": {"type": "string",
                     "maxLength": 100},
            "updated_on": {
                "type": "string",
            }
        },
        "required": ["name", "duration", "updated_on"],
        "additionalProperties": False
    },
    "podcast": {
        "type": "object",
        "properties": {
            "duration": {"type": "integer",
                         "minimum": 0},
            "name": {"type": "string",
                     "maxLength": 100},
            "host": {"type": "string",
                     "maxLength": 100},
            "updated_on": {
                "type": "string",
            },
            "participants": {
                "type": "array",
                "items": {
                    "type": "string",
                    "maxLength": 100
                },
                "maxItems": 100
            }
        },
        "required": ["name", "duration", "host", "updated_on"],
        "additionalProperties": False
    },
    "audio_book": {
        "type": "object",
        "properties": {
            "duration": {"type": "integer",
                         "minimum": 0},
            "title": {"type": "string",
                      "maxLength": 100},
            "author": {"type": "string",
                       "maxLength": 100},
            "narrator": {"type": "string",
                         "maxLength": 100},
            "updated_on": {
                "type": "string",
            }
        },
        "required": ["title", "duration", "author", "narrator", "updated_on"],
        "additionalProperties": False
    }
}


def validate_request_body(audio_type, body):
    if not body:
        raise UnsupportedRequestError("Request body cannot be empty")
    valid_schema = VALIDTION_SCHEMA[audio_type]
    try:
        validate(instance=body, schema=valid_schema)
    except ValidationError as exc:
        raise UnsupportedRequestError(exc.message)
