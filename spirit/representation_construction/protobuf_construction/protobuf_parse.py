from spirit.utils.parsing_utils import general_parse


def parse_protobuf_item(protobuf_item, constructors, **kwargs):
    """
    represent protobuf_item with one of the reader's representations,
     if exist
     otherwise return the item itself

     Exception: if multiple representations exist for item,
      throwing an exception

    """

    def parse_protobuf_with_existing_constructors(item, **inner_kwargs):
        return parse_protobuf_item(item, constructors, **inner_kwargs)

    def class_construct_method(cls, item, **parse_kwargs):
        return cls(item).construct(parse_protobuf_with_existing_constructors,
                                   **parse_kwargs)

    def function_parse_method(func, item, **parse_kwargs):
        return func(item,
                    parse_protobuf_with_existing_constructors,
                    **parse_kwargs)

    return general_parse.parse_item(protobuf_item,
                                    constructors,
                                    class_construct_method,
                                    function_parse_method,
                                    **kwargs)


