import struct
from contextlib import suppress

from . import protobuf_representations_constructors
from ..utils import fetcher


_MSG_SIZE_SIZE = 4
_SIZE_FORMAT = "<I"


def _read_formatted(file_interactor, n_bytes, struct_format):
    read_bytes = file_interactor.read(n_bytes)
    if len(read_bytes) == 0:
        return None
    result = None
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
    return parse_protobuf_item(protobuf_item)


def parse_using_parsers(protobuf_item, potential_parsers,
                        parse_method=lambda parser, *args: parser(*args)):
    """
    parse protobuf_item using specific parsers
    parse_method is how to parse using the parser
    (default behavior is call the pasrser with protobuf_item,
     parse_protobuf_item)
    """
    all_parsers = [item for item in potential_parsers
                   if "construct" in item.__name__.lower()]
    protobuf_class = type(protobuf_item)
    proto_name = protobuf_class.__name__.lower()
    parsers_for_item = [cls for cls in all_parsers
                        if proto_name == cls.field.lower()]
    if len(parsers_for_item) == 1:
        parser = parsers_for_item[0]
        return parse_method(parser, protobuf_item, parse_protobuf_item)
    elif len(parsers_for_item) > 1:
        raise Exception("Ambigious representations")


def parse_protobuf_item(protobuf_item):
    """
    represent protobuf_item with one of the reader's representations,
     if exist
     otherwise return the item itself

     Exception: if multiple representations exist for item,
      throwing an exception

    """
    def class_parse_method(cls, item, parse_func):
        return cls(item).construct(parse_func)

    parsed_with_classes = \
        parse_using_parsers(protobuf_item,
                            fetcher.get_all_classes(protobuf_representations_constructors),
                            class_parse_method)
    if parsed_with_classes:
        return parsed_with_classes

    parsed_with_funcs = \
        parse_using_parsers(protobuf_item,
                            fetcher.get_all_funcs(protobuf_representations_constructors))
    if parsed_with_funcs:
        return parsed_with_funcs
    return protobuf_item


