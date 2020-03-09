from spirit.utils.parsing_utils import general_parse
from spirit.utils.parsing_utils.parsing_configurations \
    import ParsingConfigurations
from . import savers


def save_item(repr_item, item_mark=None, **kwargs):
    """
    save an item represented in one of representations
    item_mark is used when needed to mark item to know it's saver
    kwargs are additional items to pass to the savers
    """

    def class_encode_method(cls, item, **encode_kwargs):
        return cls(item).save(save_item, **encode_kwargs)

    def function_save_method(func, item, **encode_kwargs):
        return func(item, save_item, **encode_kwargs)

    parsing_configurations = ParsingConfigurations.basic_configuration()
    # TODO: if not used delete item_mark check if one of savers use it
    # if item_mark is not None:
    #     def comparator(_, compared_item_mark, candidate, encode_attr):
    #         field = getattr(candidate, encode_attr)
    #         return field.lower() == compared_item_mark.lower()
    #
    #     parsing_configurations.item_mark = item_mark
    #     parsing_configurations.parser_comparator = comparator

    return general_parse.parse_item(repr_item,
                                    savers,
                                    class_encode_method,
                                    function_save_method,
                                    parsing_configurations,
                                    **kwargs)
