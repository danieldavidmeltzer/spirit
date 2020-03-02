from flask import Flask
from flask import request

from spirit.communication_protobuf.connection_protocol_pb2 import\
    SnapshotPacketCommunicated
from spirit.representation_construction.protobuf_construction.protobuf_parsers\
    .communication_protobuf_parser import parse_communication_protobuf
from spirit.representations_encoding.helper_encoders import inner_encoder
from spirit.utils.context import Context

app = Flask(__name__)


class Server:
    def __init__(self, host, port, publish):
        self.host = host
        self.port = port
        self.publish = publish

    def run_server(self):
        app.config["publish"] = self.publish
        app.run(host=self.host, port=self.port)


@app.route("/upload_snapshot", methods=['POST'])
def handle_snapshot():
    snapshot = request.get_data()
    protobuf_snapshot_packet = SnapshotPacketCommunicated()
    protobuf_snapshot_packet.ParseFromString(snapshot)
    snapshot_packet_represented = \
        parse_communication_protobuf(protobuf_snapshot_packet)
    encoded_packet = inner_encoder.encode_item(snapshot_packet_represented)
    serialized_encoded_packet = encoded_packet.SerializeToString()
    context = Context.build_context(app.config["publish"])
    context.publish(serialized_encoded_packet)
    return "handled"
