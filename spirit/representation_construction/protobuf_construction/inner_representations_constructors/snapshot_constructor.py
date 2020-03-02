import datetime as dt

from spirit.representations_server.representation_snapshot import \
    RepresentationSnapshot


class SnapshotConstructor:
    field = "SnapshotCommunicated"

    def __init__(self, protobuf_snapshot):
        self.protobuf_snapshot = protobuf_snapshot

    def construct(self, parse_protobuf_item):
        date_time = dt.datetime.fromtimestamp(self.protobuf_snapshot.datetime
                                              / 1000.0)
        pose = parse_protobuf_item(self.protobuf_snapshot.pose)
        color_image = parse_protobuf_item(self.protobuf_snapshot.color_image)
        depth_image = parse_protobuf_item(self.protobuf_snapshot.depth_image)
        feelings = parse_protobuf_item(self.protobuf_snapshot.feelings)
        return RepresentationSnapshot(date_time,
                                      pose,
                                      color_image,
                                      depth_image,
                                      feelings)
