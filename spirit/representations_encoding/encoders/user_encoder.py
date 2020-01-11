from datetime import datetime

from spirit.protobuf_reprsentations.spirit_sample_reps_pb2 import User


def encode_user(user, _):
    encoded_user = User()
    encoded_user.user_id = user.user_id
    encoded_user.username = user.username
    secs_since_epoch = int(datetime.timestamp(user.birt_date))
    encoded_user.birthday = secs_since_epoch
    encoded_user.gender = user.gender
    return encoded_user


encode_user.encoded_representation = "RepresentationUser"
