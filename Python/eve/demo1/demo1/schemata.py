people = {
    "firstname": {
        "type": "string",
        "minlength": 1,
        "maxlength": 10
    },
    "lastname": {
        "type": "string",
        "minlength": 1,
        "maxlength": 15,
        "required": True,
        "unique": True
    },
    "role": {
        "type": "list",
        "allowed": ["author", "contributor"]
    }
}