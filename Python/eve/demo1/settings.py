import schemata

people = {
    "item_title": "person",
    "schema": schemata.people,
    "additional_lookup": {"url": 'regex("[\w]+")', "field": "lastname"},
}
DOMAIN = {"people": people}

MONGO_HOST = "localhost"
MONGO_PORT = 27017

MONGO_USERNAME = ""
MONGO_PASSWORD = ""

MONGO_DBNAME = "demo1"

RESOURCE_METHODS = ["GET", "POST", "DELETE"]
ITEM_METHODS = ["GET", "PATCH", "PUT", "DELETE"]
