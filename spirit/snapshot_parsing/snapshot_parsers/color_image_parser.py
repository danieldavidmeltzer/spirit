import random
import string

from PIL import Image


def parse_color_image(context, snapshot):
    image_name = ''.join(random.choices(string.ascii_uppercase, k=32))
    path = context.path(image_name)
    Image.fromarray(snapshot.color_image).save(path)
    print(path)


parse_color_image.field = "color_image"
