from .. import client_encoders
from .. import encoder


def encode_item(item, item_mark=None, **kwargs):
    return encoder.encode_item(item, client_encoders, item_mark, **kwargs)
