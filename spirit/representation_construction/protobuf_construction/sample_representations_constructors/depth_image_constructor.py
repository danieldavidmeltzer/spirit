import numpy


def construct_depth_image(protobuf_depth_image, _):
    size = protobuf_depth_image.width, protobuf_depth_image.height
    return numpy.array(protobuf_depth_image.data).reshape(size)


construct_depth_image.field = "DepthImage"
