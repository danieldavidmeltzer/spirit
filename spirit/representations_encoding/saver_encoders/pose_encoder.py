def encode_pose(pose_result, encoder, result):
    pose = pose_result[1]
    parser_name = pose_result[0]  # this should be 'pose'
    result.parser_name = parser_name
    rotation = encoder(pose.rotation, "rotation")
    translation = encoder(pose.translation, "translation")
    result.parser_fields.append(rotation)
    result.parser_fields.append(translation)


encode_pose.field = "pose"
