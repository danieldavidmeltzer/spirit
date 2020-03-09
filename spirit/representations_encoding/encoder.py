from ..utils.parsing_utils import general_parse
from ..utils.parsing_utils.parsing_configurations import ParsingConfigurations


def encode_item(repr_item, encoders, item_mark=None, **kwargs):
    """
    encode an item represented in one of representations
    item_mark is used when needed to mark item to know it's encoder
    kwargs are additional items to pass to the encoders
    """

    def inner_encode_item(item, item_mark_inner=None, **kwargs_inner):
        return encode_item(item, encoders, item_mark_inner, **kwargs_inner)

    def class_encode_method(cls, item, **encode_kwargs):
        return cls(item).encode(inner_encode_item, **encode_kwargs)

    def function_encode_method(func, item, **encode_kwargs):
        return func(item, inner_encode_item, **encode_kwargs)

    parsing_configurations = ParsingConfigurations.basic_configuration()
    if item_mark is not None:
        def comparator(_, compared_item_mark, candidate, encode_attr):
            field = getattr(candidate, encode_attr)
            return field.lower() == compared_item_mark.lower()

        parsing_configurations.item_mark = item_mark
        parsing_configurations.parser_comparator = comparator

    return general_parse.parse_item(repr_item,
                                    encoders,
                                    class_encode_method,
                                    function_encode_method,
                                    parsing_configurations,
                                    **kwargs)
