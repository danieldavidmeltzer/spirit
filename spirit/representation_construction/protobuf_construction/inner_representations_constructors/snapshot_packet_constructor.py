from spirit.representations_server.representation_snapshot_packet import \
    RepresentationSnapshotPacket


class SnapshotPacketConstructor:
    field = "SnapshotPacketCommunicated"

    def __init__(self, protobuf_snapshot_packet):
        self.protobuf_snapshot_packet = protobuf_snapshot_packet

    def construct(self, parse_protobuf_item, blob_url):
        snapshot = parse_protobuf_item(self.protobuf_snapshot_packet.snapshot,
                                       blob_url=blob_url)
        user = parse_protobuf_item(self.protobuf_snapshot_packet.user)
        return RepresentationSnapshotPacket(user, snapshot)
