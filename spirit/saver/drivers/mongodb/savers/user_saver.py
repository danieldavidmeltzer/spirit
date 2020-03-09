def save_user(user, saver, snapshot_object_id, mongo_db):
    collection = mongo_db.users
    update_dict = {'$set': {'gender': user.gender,
                            'username': user.username,
                            'birth_date': user.birth_date}}
    if snapshot_object_id != 'default':  # new snapshot
        update_dict['$push'] = {'snapshots': snapshot_object_id}

    collection.update({'user_id': user.user_id}, update_dict, True)


save_user.field = "RepresentationUser"
