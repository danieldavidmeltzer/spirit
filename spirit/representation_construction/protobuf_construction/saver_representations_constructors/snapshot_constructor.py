import datetime as dt

from spirit.representations_saver.representation_snapshot \
    import RepresentationSnapshot


def construct_snapshot(snapshot_protobuf, _):
    date_time = dt.datetime.fromtimestamp(snapshot_protobuf.datetime
                                          / 1000.0)

    return RepresentationSnapshot(date_time,
                                  snapshot_protobuf.snapshot_id)


construct_snapshot.field = "SnapshotSaver"
