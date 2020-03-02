def encode_pose(pose, _, snapshot):
    snapshot.pose.translation.x = pose.translation[0]
    snapshot.pose.translation.y = pose.translation[1]
    snapshot.pose.translation.z = pose.translation[2]
    snapshot.pose.rotation.x = pose.rotation[0]
    snapshot.pose.rotation.y = pose.rotation[1]
    snapshot.pose.rotation.z = pose.rotation[2]
    snapshot.pose.rotation.w = pose.rotation[3]


encode_pose.field = "RepresentationPose"
