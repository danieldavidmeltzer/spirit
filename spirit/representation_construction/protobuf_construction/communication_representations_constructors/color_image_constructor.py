from spirit.blob_store.blob_store import BlobStore
from spirit.representations_server.representation_image import \
    RepresentationImage


def construct_color_image(protobuf_color_image, _, blob_url, keys):
    width = protobuf_color_image.width
    height = protobuf_color_image.height
    binary_data = protobuf_color_image.data
    blob_id = BlobStore(blob_url, keys).save_binary(binary_data)
    color_image = RepresentationImage(width, height, blob_id)
    return color_image


construct_color_image.field = "ColorImageCommunicated"
