from spirit.inner_protobuf.inner_protocol_pb2 import \
    SnapshotPacketInner


class SnapshotPacketEncoder:
    def __init__(self, snapshot_packet):
        self.snapshot_packet = snapshot_packet

    def encode(self, encoder):
        encoded_snapshot_packet = SnapshotPacketInner()
        encoder(self.snapshot_packet.snapshot,
                encoded_snapshot=encoded_snapshot_packet.snapshot)
        encoder(self.snapshot_packet.user,
                encoded_user=encoded_snapshot_packet.user)
        return encoded_snapshot_packet


SnapshotPacketEncoder.field = "RepresentationSnapshotPacket"
