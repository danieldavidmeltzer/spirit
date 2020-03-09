def save_result(result, saver, mongo_db):
    collection = mongo_db.results
    object_ids = {}
    for field in result.parser_fields:
        object_id = saver(field, mongo_db=mongo_db)
        object_ids[field.field_name] = object_id
    result = collection.insert_one({'fields': object_ids})
    return result.inserted_id


save_result.field = "RepresentationResult"


