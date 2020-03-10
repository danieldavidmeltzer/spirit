from purl import URL

from spirit.representation_construction.protobuf_construction.protobuf_parsers \
    import saver_protobuf_parser
from spirit.saver_protobuf.saver_proto_pb2 import ParsingResult
from spirit.utils.fetcher import find_driver
from . import drivers


class Saver:
    def __init__(self, database_url):
        self.driver = find_driver(database_url, drivers)

    def save(self, packet):
        result = ParsingResult()
        result.ParseFromString(packet)
        represented_result = saver_protobuf_parser.parse_saver_protobuf(result)
        self.driver.save_parsing_result(represented_result)


