from spirit.representations_server.representation_image import\
    RepresentationImage


def construct_color_image(protobuf_color_image, _):
    blob_id = protobuf_color_image.blob_id
    width = protobuf_color_image.width
    height = protobuf_color_image.height
    return RepresentationImage(width, height, blob_id)


construct_color_image.field = "ColorImageCommunicated"
