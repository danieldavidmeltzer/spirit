from . import snapshot_parsers
from spirit.utils.list_utils import lower_list
from spirit.utils.parsing_utils import general_parse
from spirit.utils.parsing_utils.parsing_configurations import \
    ParsingConfigurations
from spirit.utils.string_utils import non_key_sensitive_match


def parse_snapshot(snapshot, parser_field, context):
    """
    parse a snapshot with context
    """

    def class_parse_method(cls, item, inner_context):
        return cls(item, inner_context).parse()

    def function_parse_method(parse, item, inner_context):
        return parse(item, inner_context)

    def comparator(item, _, candidate, parse_attr):
        field = getattr(candidate, parse_attr)
        snapshot_has_field = field.lower() in lower_list(vars(item))
        fields_match = non_key_sensitive_match(field, parser_field)
        return snapshot_has_field and fields_match

    parsing_config = ParsingConfigurations.basic_configuration()
    parsing_config.parser_comparator = comparator
    parsing_config.enforce_one_parser = False
    return general_parse.parse_item(snapshot,
                                    snapshot_parsers,
                                    class_parse_method,
                                    function_parse_method,
                                    parsing_config,
                                    context=context)
