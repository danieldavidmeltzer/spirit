import datetime as dt
from uuid import uuid4

from spirit.representations_server.representation_snapshot import \
    RepresentationSnapshot


class SnapshotConstructor:
    field = "SnapshotCommunicated"

    def __init__(self, protobuf_snapshot):
        self.protobuf_snapshot = protobuf_snapshot

    def construct(self, parse_protobuf_item, blob_url, keys):
        date_time = dt.datetime.fromtimestamp(self.protobuf_snapshot.datetime
                                              / 1000.0)
        pose = parse_protobuf_item(self.protobuf_snapshot.pose)
        color_image = parse_protobuf_item(self.protobuf_snapshot.color_image,
                                          blob_url=blob_url,
                                          keys=keys)
        depth_image = parse_protobuf_item(self.protobuf_snapshot.depth_image,
                                          blob_url=blob_url,
                                          keys=keys)

        feelings = parse_protobuf_item(self.protobuf_snapshot.feelings)
        return RepresentationSnapshot(date_time,
                                      pose,
                                      color_image,
                                      depth_image,
                                      feelings,
                                      str(uuid4()))
