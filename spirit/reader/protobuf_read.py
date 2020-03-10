import struct
from contextlib import suppress

from spirit.representation_construction. \
    protobuf_construction.protobuf_parsers.sample_protobuf_parser import \
    parse_sample_protobuf

_MSG_SIZE_SIZE = 4
_SIZE_FORMAT = "<I"


def _read_formatted(file_interactor, n_bytes, struct_format):
    read_bytes = file_interactor.read(n_bytes)
    if len(read_bytes) == 0:
        return None
    with suppress(IndexError):
        result = struct.unpack(struct_format, read_bytes)[0]
    return result


def _read_protobuf_item(file_interactor, protobuf_class):
    size = _read_formatted(file_interactor, _MSG_SIZE_SIZE, _SIZE_FORMAT)
    if size is None:
        return None
    item = protobuf_class()
    item.ParseFromString(file_interactor.read(size))
    return item


def read_item(file_interactor, protobuf_class):
    protobuf_item = _read_protobuf_item(file_interactor, protobuf_class)
    if protobuf_item is None:
        return None
    return parse_sample_protobuf(protobuf_item)
