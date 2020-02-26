from flask import Flask
from flask import jsonify
from flask import request

from spirit.protobuf_reprsentations import Snapshot
from spirit.representation_construction.protobuf_construction.protobuf_parse \
    import parse_protobuf_item
from spirit.snapshot_parser_utils.parser import parse_snapshot
from . import parsers
from .utils import fetcher
from .utils.context import Context

app = Flask(__name__)


class Server:
    def __init__(self, host, port, data_dir):
        self.host = host
        self.port = port
        self.data_dir = data_dir

    def run_server(self):
        app.config["data_dir"] = self.data_dir
        app.run(host=self.host, port=self.port)


@app.route("/get_parsers")
def available_parsers_names():
    """
    get list of all available parsers
    """

    def protocol_field_for_parser(parser):
        return \
            convert_representation_field_to_protocol_field(parser.field)

    return jsonify([protocol_field_for_parser(parser)
                    for parser in get_all_parsers()])


def convert_representation_field_to_protocol_field(field):
    """
    this function should take snapshot representation field name
    and convert it to the matching name in protocol
    """
    mapping = {"date_time": "datetime"}
    return mapping.get(field, field)  # name from map, default is name itself


@app.route("/upload_snapshot", methods=['POST'])
def handle_snapshot():
    snapshot = request.get_data()
    protobuf_snapshot = Snapshot()
    protobuf_snapshot.ParseFromString(snapshot)
    # we can use parse_protobuf_item() only because the format and the
    # representation in both the client and the server are the same
    # but if the client was written in other language or in other formats
    # and wouldn't use this format we would have had to use our own
    # code, i don't  want to have code multiplication within the project so
    # it's ok, carefully use this code until it diverges
    snapshot_represented = parse_protobuf_item(protobuf_snapshot)
    context = Context.build_context(app.config["data_dir"])
    parse_snapshot(snapshot_represented, context)
    return "handled"


def get_all_parsers():
    return get_all_class_parsers() + get_all_func_parsers()


def get_all_class_parsers():
    available_parsers = [cls
                         for cls in
                         fetcher.get_all_classes(parsers)
                         if "parse" in cls.__name__.lower()]
    return available_parsers


def get_all_func_parsers():
    available_parsers = [f
                         for f in fetcher.get_all_funcs(parsers)
                         if "parse" in f.__name__.lower()]
    return available_parsers
