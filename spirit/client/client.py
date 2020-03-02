from purl import URL

import requests
from spirit.representations_client.representation_snapshot_packet \
    import RepresentationSnapshotPacket
from spirit.representations_encoding.helper_encoders import client_encoder
from spirit.reader import reader


class Client:
    def __init__(self, path, host, port):
        self.path = path
        self.host = host
        self.port = port
        self.url = URL(scheme="http", host=host, port=port)

    def upload_snapshots(self):
        rd = reader.Reader(self.path)
        for snapshot in rd:
            snapshot_packet = RepresentationSnapshotPacket(rd.user, snapshot)
            upload_snapshot_packet(snapshot_packet,
                                   f"http://{self.host}:{self.port}")
            # TODO: move to self.url.as_string())


def upload_snapshot_packet(snapshot_packet, server_url):
    snapshot_packet_in_protobuf = client_encoder.encode_item(snapshot_packet)
    serialized_snapshot_packet = snapshot_packet_in_protobuf.SerializeToString()
    response = requests.post(server_url + "/upload_snapshot",
                             data=serialized_snapshot_packet)
    return response.text
