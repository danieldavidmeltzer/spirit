import matplotlib.pyplot as plotter
import string
import random


def parse_depth_image(context, snapshot):
    image_name = ''.join(random.choices(string.ascii_uppercase, k=32))
    path = context.path(image_name)+".jpg"
    plotter.imsave(path, snapshot.depth_image, cmap="hot")


parse_depth_image.field = "depth_image"
