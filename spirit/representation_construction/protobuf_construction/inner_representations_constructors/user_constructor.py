import datetime

from spirit.representations_server.representation_user import \
    RepresentationUser


def construct_user(protobuf_user, _):
    gender = protobuf_user.gender
    user_id = protobuf_user.user_id
    username = protobuf_user.username
    birth_date = datetime.datetime.fromtimestamp(protobuf_user.birthday)
    user = RepresentationUser(gender, user_id, username, birth_date)
    return user


construct_user.field = "UserInner"
