from spirit.saver_protobuf.saver_proto_pb2 import ParsingResult


class ParsingResultEncoder:
    field = "ParsingResult"

    def __init__(self, result):
        self.snapshot = result[0]
        self.user = result[1]
        self.parser_result = result[2]  # tuple of (parser_name, parser_result)

    def encode(self, encoder):
        result = ParsingResult()
        encoder(self.snapshot, encoded_snapshot=result.snapshot)
        encoder(self.user, encoded_user=result.user)
        parser_name = self.parser_result[0]
        if parser_name.lower() in ["color_image", "depth_image"]:
            encoder(self.parser_result, "ImageUrl", result=result.result)
        else:
            encoder(self.parser_result, parser_name, result=result.result)
        return result
