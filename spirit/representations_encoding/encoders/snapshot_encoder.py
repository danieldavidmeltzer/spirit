from datetime import datetime

from spirit.protobuf_reprsentations.spirit_sample_reps_pb2 import Snapshot


class SnapshotEncoder:
    def __init__(self, snapshot):
        self.snapshot = snapshot

    def encode(self, encoder):
        encoded_snapshot = Snapshot()
        milliseconds_from_epoch = \
            int(datetime.timestamp(self.snapshot.date_time) * 1000)
        encoded_snapshot.datetime = milliseconds_from_epoch
        encoder(self.snapshot.pose,
                snapshot=encoded_snapshot)
        encoder(self.snapshot.color_image,
                "ColorImage",
                snapshot=encoded_snapshot)
        encoder(self.snapshot.depth_image,
                "DepthImage",
                snapshot=encoded_snapshot)
        encoder(self.snapshot.feelings,
                snapshot=encoded_snapshot)
        return encoded_snapshot


SnapshotEncoder.field = "RepresentationSnapshot"
