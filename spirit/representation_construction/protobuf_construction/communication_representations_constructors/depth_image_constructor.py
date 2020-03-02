from spirit.blob_store.blob_store import BlobStore
from spirit.representations_server.representation_image import \
    RepresentationImage
from numpy import array


def construct_depth_image(protobuf_depth_image, _, blob_url):
    width = protobuf_depth_image.width
    height = protobuf_depth_image.depth_image.height
    binary_data = array(protobuf_depth_image.depth_image.data).tobytes()
    blob_id = BlobStore(blob_url).save_binary(binary_data)
    depth_image = RepresentationImage(width, height, blob_id)
    return depth_image


construct_depth_image.field = "DepthImageCommunicated"
