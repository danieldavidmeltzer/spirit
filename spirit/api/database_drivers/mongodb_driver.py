from pymongo import MongoClient

from spirit.utils.list_utils import get_single_item


def make_dict(db_list):
    """
    change db list that has elements of type [{'key':value},...]
    to dict
    Args:
        db_list:
            the db list
    Returns:
        dict
    """
    result_dict = {}
    for item in db_list:
        key = get_single_item(list(item.keys()))
        result_dict[key] = item[key]
    return result_dict


def user_not_found_response(user_id):
    return {'error': f"no user {user_id}"}


def snapshot_not_found(snapshot_id):
    return {'error': f"snapshot {snapshot_id} not found"}


def result_not_found(result_name):
    return {'error': f'{result_name} result not found'}


def _get_snapshot_date(snapshot):
    snapshot_date = snapshot['date_time']
    snapshot_date_formatted = 'no date, error on our side'
    if snapshot_date:
        snapshot_date_formatted = \
            snapshot_date.strftime("%d/%m/%Y, %H:%M:%S")
    return snapshot_date_formatted


class MongoDBDriver:
    scheme = 'mongodb'

    def __init__(self, db_url):
        self.mongo_db = MongoClient(db_url).spirit

    def get_users(self):
        users_query = self.mongo_db.users.find().sort("user_id")
        users = {}
        for user in users_query:
            users[user['user_id']] = {'name': user['username']}
        return users

    def get_user(self, user_id):
        user = self.mongo_db.users.find_one({'user_id': user_id})
        if user is None:
            return user_not_found_response(user_id)
        genders_list = ['male', 'female', 'other']
        return {'user_id': user['user_id'],
                'name': user['username'],
                'birthday': user['birth_date'].strftime("%d/%m/%Y, %H:%M:%S"),
                'gender': genders_list[user['gender']]}

    def get_snapshots(self, user_id):
        user = self.mongo_db.users.find_one({'user_id': user_id})
        if user is None:
            return user_not_found_response(user_id)
        snapshots_ids = user['snapshots']
        snapshot_results = \
            self.mongo_db.snapshots.find({'_id': {'$in': snapshots_ids}})
        snapshots = {}
        for snapshot in snapshot_results:
            snapshot_id = snapshot['snapshot_id']
            snapshot_date =\
                snapshot['date_time'].strftime("%d/%m/%Y, %H:%M:%S")
            snapshots[snapshot_id] = {'date_time': snapshot_date}
        return snapshots

    def get_snapshot(self, snapshot_id):
        snapshot = self.mongo_db.snapshots.find_one(
            {'snapshot_id': snapshot_id})
        if snapshot is None:
            return snapshot_not_found(snapshot_id)
        snapshot_date_formatted = _get_snapshot_date(snapshot)

        def get_res_name(result):
            return get_single_item(list(result.keys()))

        results_name = list(map(get_res_name, snapshot['results']))
        return {'snapshot_id': snapshot_id,
                'snapshot_date': snapshot_date_formatted,
                'results': results_name}

    def get_result(self, snapshot_id, result_name):
        result = {}
        snapshot = self.mongo_db.snapshots.find_one(
            {'snapshot_id': snapshot_id})
        if snapshot is None:
            return snapshot_not_found(snapshot_id)
        results_dict = make_dict(snapshot['results'])
        result_obj_id = results_dict.get(result_name)
        if result_obj_id is None:
            return result_not_found(result_name)
        result_obj = self.mongo_db.results.find_one({'_id': result_obj_id})
        fields = result_obj['fields']
        for field in fields:
            result[field] = self._get_field(fields[field])
        return result

    def _get_field(self, field_id):
        field = self.mongo_db.fields.find_one({'_id': field_id})
        if 'value' in field:
            return field['value']
        else:
            result = {}
            fields = field['fields']
            for sub_field in fields:
                result[sub_field] = self._get_field(fields[sub_field])
            return result

    def get_image_id(self, snapshot_id, result_name):
        result = self.get_result(snapshot_id, result_name)
        return result['image_url']
