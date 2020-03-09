from spirit.representations_saver.representation_parsing_result\
    import RepresentationParsingResult


class SnapshotPacketConstructor:
    field = "ParsingResult"

    def __init__(self, parsing_result_protobuf):
        self.parsing_result_protobuf = parsing_result_protobuf

    def construct(self, parse_protobuf_item):
        snapshot = parse_protobuf_item(self.parsing_result_protobuf.snapshot)
        user = parse_protobuf_item(self.parsing_result_protobuf.user)
        result = parse_protobuf_item(self.parsing_result_protobuf.result)
        return RepresentationParsingResult(snapshot, user, result)
