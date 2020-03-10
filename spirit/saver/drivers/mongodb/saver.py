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

    return general_parse.parse_item(repr_item,
                                    savers,
                                    class_encode_method,
                                    function_save_method,
                                    parsing_configurations,
                                    **kwargs)
