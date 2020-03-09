def save_composite_result(composite_result, saver, mongo_db):
    collection = mongo_db.fields
    sub_field_ids = {}
    for field in composite_result.sub_fields:
        object_id = saver(field, mongo_db=mongo_db)
        sub_field_ids[field.field_name] = object_id
    result = collection.insert_one({'fields': sub_field_ids})
    return result.inserted_id


save_composite_result.field = "RepresentationFieldComposite"

