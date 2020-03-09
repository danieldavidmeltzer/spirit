import io
import matplotlib.pyplot as plotter
from spirit.blob_store.blob_store import BlobStore
import numpy


def parse_depth_image(snapshot, context):
    blob_store = BlobStore(context.blob_url, context.keys)
    image_array = fetch_raw_image(blob_store, snapshot)
    image_output = io.BytesIO()
    plotter.imsave(image_output, image_array, cmap='hot', format='jpg')
    image_output.seek(0)
    img_binary = image_output.read()
    image_url = blob_store.save_binary(img_binary)
    return image_url


def fetch_raw_image(blob_store, snapshot):
    color_image_binary = blob_store.get_binary(snapshot.depth_image.blob_id)
    size = snapshot.depth_image.width, snapshot.depth_image.height
    image_array = numpy.frombuffer(color_image_binary).reshape(size)
    return image_array


parse_depth_image.field = "depth_image"
