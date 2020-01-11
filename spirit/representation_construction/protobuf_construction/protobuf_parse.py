from spirit.utils.parsing_utils import general_parse
from . import protobuf_representations_constructors


def parse_protobuf_item(protobuf_item):
    """
    represent protobuf_item with one of the reader's representations,
     if exist
     otherwise return the item itself

     Exception: if multiple representations exist for item,
      throwing an exception

    """

    def class_construct_method(cls, item):
        return cls(item).construct(parse_protobuf_item)

    def function_parse_method(func, item):
        return func(item, parse_protobuf_item)

    return general_parse.parse_item(protobuf_item,
                                    protobuf_representations_constructors,
                                    class_construct_method,
                                    function_parse_method)
