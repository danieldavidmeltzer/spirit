from purl import URL

import requests
from spirit.representations_client.representation_snapshot_packet \
    import RepresentationSnapshotPacket
from spirit.representations_encoding.helper_encoders import client_encoder
from spirit.reader import reader
from spirit.utils.exception_utils import retry_on_exception


class Client:
    def __init__(self, path, host, port):
        self.path = path
        self.host = host
        self.port = port
        self.url = URL(scheme="http", host=host, port=port)

    def upload_snapshots(self):
        rd = reader.Reader(self.path)
        user = rd.user
        for snapshot in rd:
            self.upload_packet(snapshot, user)

    @retry_on_exception(requests.exceptions.RequestException, 3)
    def upload_packet(self, snapshot, user):
        snapshot_packet = RepresentationSnapshotPacket(user, snapshot)
        upload_snapshot_packet(snapshot_packet,
                               f"http://{self.host}:{self.port}")


def upload_snapshot_packet(snapshot_packet, server_url):
    snapshot_packet_in_protobuf = client_encoder.encode_item(snapshot_packet)
    serialized_snapshot_packet = snapshot_packet_in_protobuf.SerializeToString()
    response = requests.post(server_url + "/upload_snapshot",
                             data=serialized_snapshot_packet)
    return response.text
