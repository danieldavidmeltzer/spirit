from numpy import array

from spirit.blob_store.blob_store import BlobStore
from spirit.representations_server.representation_image import \
    RepresentationImage


def construct_depth_image(protobuf_depth_image, _, blob_url, keys):
    width = protobuf_depth_image.width
    height = protobuf_depth_image.height
    binary_data = array(protobuf_depth_image.data).tobytes()
    blob_id = BlobStore(blob_url, keys=keys).save_binary(binary_data)
    depth_image = RepresentationImage(width, height, blob_id)
    return depth_image


construct_depth_image.field = "DepthImageCommunicated"
