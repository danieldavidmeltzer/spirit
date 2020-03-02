from spirit.representations_server.representation_pose import RepresentationPose


def construct_pose(protobuf_item, _):
    p_rotation = protobuf_item.rotation
    rotation = (p_rotation.x, p_rotation.y, p_rotation.z, p_rotation.w)
    p_translation = protobuf_item.translation
    translation = (p_translation.x, p_translation.y, p_translation.z)
    return RepresentationPose(rotation, translation)


construct_pose.field = "PoseCommunicated"
