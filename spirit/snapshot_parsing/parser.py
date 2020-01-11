from spirit.utils.list_utils import lower_list
from . import snapshot_parsers
from ..utils.parsing_utils import general_parse
from ..utils.parsing_utils.parsing_configurations import ParsingConfigurations


def parse_snapshot(snapshot, snapshot_context):
    """
    parse a snapshot with context
    """

    def class_parse_method(cls, item, context):
        return cls(context, item).parse()

    def function_parse_method(parse, item, context):
        return parse(context, item)

    def comparator(item, _, candidate, parse_attr):
        field = getattr(candidate, parse_attr)
        return field.lower() in lower_list(vars(item))

    parsing_config = ParsingConfigurations.basic_configuration()
    parsing_config.parser_comparator = comparator
    parsing_config.enforce_one_parser = False
    return general_parse.parse_item(snapshot,
                                    snapshot_parsers,
                                    class_parse_method,
                                    function_parse_method,
                                    parsing_config,
                                    context=snapshot_context)
