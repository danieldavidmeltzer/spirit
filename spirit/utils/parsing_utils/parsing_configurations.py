class ParsingConfigurations:
    def __init__(self):
        self.parser_comparator = None
        self.item_mark = None
        self.parse_attr_name = None
        self.enforce_one_parser = False

    @classmethod
    def basic_configuration(cls):
        config = cls()
        config.parse_attr_name = "field"
        config.item_mark = None
        config.enforce_one_parser = True

        def basic_comparator(item, _, candidate, parse_attr_name):
            type_name = type(item).__name__
            parse_attr_value = getattr(candidate, parse_attr_name)
            return type_name.lower() == parse_attr_value.lower()

        config.parser_comparator = basic_comparator
        return config
