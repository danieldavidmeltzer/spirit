import logging

from flask import Flask
from flask import request

from spirit.blob_store.secret_keys import get_minio_keys_from_environment
from spirit.communication_protobuf.connection_protocol_pb2 import \
    SnapshotPacketCommunicated
from spirit.representation_construction.protobuf_construction.protobuf_parsers \
    .communication_protobuf_parser import parse_communication_protobuf
from spirit.representations_encoding.helper_encoders import inner_encoder
from spirit.utils.context import Context

# from gevent.pywsgi import WSGIServer

app = Flask(__name__)


class Server:
    def __init__(self, host, port, blob_store, publish):
        self.host = host
        self.port = port
        self.publish = publish
        self.blob_store = blob_store

    def run_server(self):
        app.config["publish"] = self.publish
        app.config["blob_store"] = self.blob_store
        app.run(host=self.host, port=self.port, debug=True)
        logging.info(f"listening at {self.host}:{self.port}")


@app.route("/upload_snapshot", methods=['POST'])
def handle_snapshot():
    snapshot = request.get_data()
    protobuf_snapshot_packet = SnapshotPacketCommunicated()
    protobuf_snapshot_packet.ParseFromString(snapshot)
    blob_url = app.config["blob_store"]
    snapshot_packet_represented = \
        parse_communication_protobuf(protobuf_snapshot_packet,
                                     blob_url=blob_url,
                                     keys=get_minio_keys_from_environment())
    encoded_packet = inner_encoder.encode_item(snapshot_packet_represented)
    serialized_encoded_packet = encoded_packet.SerializeToString()
    context = Context.build_context(app.config["publish"])
    context.publish(serialized_encoded_packet)
    return "handled"
