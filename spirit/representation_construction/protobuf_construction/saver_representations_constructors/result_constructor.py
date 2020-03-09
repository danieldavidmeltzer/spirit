from spirit.representations_saver.representation_result\
    import RepresentationResult


class SnapshotPacketConstructor:
    field = "Result"

    def __init__(self, result_protobuf):
        self.result_protobuf = result_protobuf

    def construct(self, parse_protobuf_item):
        parser_name = self.result_protobuf.parser_name
        parser_fields = []
        for item in self.result_protobuf.parser_fields:
            parser_fields.append(parse_protobuf_item(item))
        return RepresentationResult(parser_name, parser_fields)
