from spirit.representations_server.representation_image import\
    RepresentationImage


def construct_depth_image(protobuf_depth_image, _):
    blob_id = protobuf_depth_image.blob_id
    width = protobuf_depth_image.width
    height = protobuf_depth_image.height
    return RepresentationImage(width, height, blob_id)


construct_depth_image.field = "DepthImageCommunicated"
