import random
import string

import matplotlib.pyplot as plotter


def parse_depth_image(snapshot, context):
    image_name = ''.join(random.choices(string.ascii_uppercase, k=32))
    path = context.path(image_name) + ".jpg"
    plotter.imsave(path, snapshot.depth_image, cmap="hot")


parse_depth_image.field = "depth_image"
