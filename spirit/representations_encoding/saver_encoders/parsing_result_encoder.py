

class ParsingResultEncoder:
    field = "ParsingResult"

    def __init__(self, result):
        self.snapshot = result[0]
        self.user = result[1]
        self.parser_result = result[2]

    def encode(self, encoder):
        pass
