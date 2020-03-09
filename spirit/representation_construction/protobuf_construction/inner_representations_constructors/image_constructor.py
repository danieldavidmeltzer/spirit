from spirit.representations_server.representation_image import\
    RepresentationImage


def construct_image(protobuf_image, _):
    blob_id = protobuf_image.blob_id
    width = protobuf_image.width
    height = protobuf_image.height
    return RepresentationImage(width, height, blob_id)


construct_image.field = "ImageInner"
