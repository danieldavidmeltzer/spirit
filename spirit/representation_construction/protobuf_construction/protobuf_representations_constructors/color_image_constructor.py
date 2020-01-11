import numpy


def construct_color_image(protobuf_color_image, _):
    size = protobuf_color_image.width, protobuf_color_image.height, 3
    byte_array = bytearray(protobuf_color_image.data)
    numpy_repr = numpy.array(byte_array).reshape(size)
    return numpy_repr


construct_color_image.field = "ColorImage"
