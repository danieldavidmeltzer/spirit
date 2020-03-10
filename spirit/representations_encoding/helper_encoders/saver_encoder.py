from .. import encoder
from .. import saver_encoders


def encode_item(item, item_mark=None, **kwargs):
    return encoder.encode_item(item, saver_encoders, item_mark, **kwargs)
