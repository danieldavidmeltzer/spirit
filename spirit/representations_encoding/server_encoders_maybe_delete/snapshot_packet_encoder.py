from spirit.communication_protobuf.connection_protocol_pb2 import \
    SnapshotPacketCommunicated


class SnapshotPacketEncoder:
    def __init__(self, snapshot_packet):
        self.snapshot_packet = snapshot_packet

    def encode(self, encoder):
        encoded_snapshot_packet = SnapshotPacketCommunicated()
        encoder(self.snapshot_packet.snapshot,
                encoded_snapshot=encoded_snapshot_packet.snapshot)
        encoder(self.snapshot_packet.user,
                encoded_user=encoded_snapshot_packet.user)
        return encoded_snapshot_packet


SnapshotPacketEncoder.field = "RepresentationSnapshotPacket"
