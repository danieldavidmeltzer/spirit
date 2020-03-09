from spirit.representations_server.representation_feelings import \
    RepresentationFeelings


def construct_feelings(protobuf_feeling, _):
    return RepresentationFeelings(protobuf_feeling.hunger,
                                  protobuf_feeling.thirst,
                                  protobuf_feeling.exhaustion,
                                  protobuf_feeling.happiness)


construct_feelings.field = "FeelingsInner"
