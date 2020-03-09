def save_simple_result(result, saver, mongo_db):
    collection = mongo_db.fields
    insertion_result = collection.insert_one({'value': result.field_value})
    return insertion_result.inserted_id


save_simple_result.field = "RepresentationFieldSimple"
