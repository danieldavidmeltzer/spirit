def parse_pose(snapshot, _):
    print(snapshot.pose.rotation)


parse_pose.field = "pose"
