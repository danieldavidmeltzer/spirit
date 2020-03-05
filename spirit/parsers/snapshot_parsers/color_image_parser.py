import io
from numpy import array
from PIL import Image
from spirit.blob_store.blob_store import BlobStore


def parse_color_image(snapshot, context):
    blob_store = BlobStore(context.blob_url, context.keys)
    image_array = fetch_image(blob_store, snapshot)
    image = Image.fromarray(image_array)
    image_output = io.BytesIO()
    image.save(image_output, format='JPEG')
    image_url = blob_store.save_binary(image_output.read())
    return image_url


def fetch_image(blob_store, snapshot):
    color_image_binary = blob_store.get_binary(snapshot.color_image.blob_url)
    size = snapshot.color_image.height, snapshot.color_image.width, 3
    image_array = array(bytearray(color_image_binary)).reshape(size)
    return image_array


parse_color_image.field = "color_image"
