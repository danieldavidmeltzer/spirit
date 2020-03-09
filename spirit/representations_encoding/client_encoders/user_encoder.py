from datetime import datetime


def encode_user(user, _, encoded_user):
    encoded_user.user_id = user.user_id
    encoded_user.username = user.username
    secs_since_epoch = int(datetime.timestamp(user.birth_date))
    encoded_user.birthday = secs_since_epoch
    encoded_user.gender = user.gender


encode_user.field = "RepresentationUser"
