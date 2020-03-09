from spirit.utils import fetcher
from spirit.utils.list_utils import get_single_item
from .parsing_configurations import ParsingConfigurations


def parse_using_parsers(item,
                        potential_parsers,
                        parse_method,
                        parsing_configurations,
                        **kwargs):
    """
    parse general item using potential_parsers
    according to parsing_configurations
    """
    parse_attr_name = parsing_configurations.parse_attr_name
    parser_comparator = parsing_configurations.parser_comparator

    item_mark = parsing_configurations.item_mark
    all_parsers = [item
                   for item
                   in potential_parsers
                   if hasattr(item, parse_attr_name)]
    # TODO: check if hasattr needed if we have parser_comparator
    parsers_for_item = [candidate for candidate in all_parsers
                        if parser_comparator(item,
                                             item_mark,
                                             candidate,
                                             parse_attr_name)
                        ]
    if parsing_configurations.enforce_one_parser:
        single_parser = get_single_item(parsers_for_item)
        if single_parser:
            return parse_method(single_parser, item, **kwargs)
    else:
        results = []
        for parser in parsers_for_item:
            results.append(parse_method(parser, item, **kwargs))
        return results


def parse_item(item,
               parsers_module,
               cls_parse_method,
               func_parse_method,
               parsing_configurations=
               # TODO: change this to None and inside method, handle None
               ParsingConfigurations.basic_configuration(),
               **kwargs):
    """
    parse an item if parser exist for it,
    if no parser found and one parser is enforced, we return the item itself
    returns multiple parsing results in array if single parser isn't enforced
    uses parsing_configurations
    """
    parsed_with_classes = \
        parse_using_parsers(item,
                            fetcher.get_all_classes(parsers_module),
                            cls_parse_method,
                            parsing_configurations,
                            **kwargs)
    if parsing_configurations.enforce_one_parser:
        if parsed_with_classes is not None:  # we don't care for __bool__
            return parsed_with_classes
    parsed_with_funcs = \
        parse_using_parsers(item,
                            fetcher.get_all_funcs(parsers_module),
                            func_parse_method,
                            parsing_configurations,
                            **kwargs)
    if parsing_configurations.enforce_one_parser:
        if parsed_with_funcs is not None:  # we don't care for __bool__
            return parsed_with_funcs
    else:
        return parsed_with_classes + parsed_with_funcs
    return item
