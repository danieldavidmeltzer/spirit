def save_snapshot(snapshot, saver, result_object_id, parser_name, mongo_db):
    collection = mongo_db.snapshots
    result = collection.update({'snapshot_id': snapshot.snapshot_id},
                               {'$push': {
                                   'results': {parser_name: result_object_id}},
                                '$set': {'date_time': snapshot.date_time}},
                               True)
    return result.get('upserted', 'default')


save_snapshot.field = "RepresentationSnapshot"
