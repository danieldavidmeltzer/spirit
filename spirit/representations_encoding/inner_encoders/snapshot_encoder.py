from datetime import datetime


class SnapshotEncoder:
    def __init__(self, snapshot):
        self.snapshot = snapshot

    def encode(self, encoder, encoded_snapshot):
        milliseconds_from_epoch = \
            int(datetime.timestamp(self.snapshot.date_time) * 1000)
        encoded_snapshot.datetime = milliseconds_from_epoch
        encoded_snapshot.snapshot_id = self.snapshot.snapshot_id
        encoder(self.snapshot.pose,
                snapshot=encoded_snapshot)
        encoder(self.snapshot.color_image,
                "ColorImageInner",
                snapshot=encoded_snapshot)
        encoder(self.snapshot.depth_image,
                "DepthImageInner",
                snapshot=encoded_snapshot)
        encoder(self.snapshot.feelings,
                snapshot=encoded_snapshot)


SnapshotEncoder.field = "RepresentationSnapshot"
