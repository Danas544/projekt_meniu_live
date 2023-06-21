
def table_insert_rule():

    validation_rules = {
        "validator": {
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["name", "surname", "time", "Table"],
                "properties": {
                    "name": {"bsonType": "string"},
                    'surname': {"bsonType": "string"},
                    "time": {"bsonType": "double"},
                    "Table": {"bsonType": "string"}
                },
            }
        }
    }
    return validation_rules


def order_insert_rule():
    pass