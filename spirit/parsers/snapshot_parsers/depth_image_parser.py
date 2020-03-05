import io
import matplotlib.pyplot as plotter
from spirit.blob_store.blob_store import BlobStore
import numpy


def parse_depth_image(snapshot, context):
    blob_store = BlobStore(context.blob_url, context.keys)
    image_array = fetch_raw_image(blob_store, snapshot)
    image_output = io.BytesIO()
    plotter.imsave(image_output, image_array, cmap='hot', format='jpg')
    image_url = blob_store.save_binary(image_output.read())
    return image_url


def fetch_raw_image(blob_store, snapshot):
    color_image_binary = blob_store.get_binary(snapshot.depth_image.blob_url)
    size = snapshot.depth_image.height, snapshot.depth_image.width
    image_array = numpy.frombuffer(color_image_binary).reshape_size(size)
    return image_array


parse_depth_image.field = "depth_image"
