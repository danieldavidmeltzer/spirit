def encode_color_image(color_image, _, snapshot):
    """
    color_image: array to encode
    """
    snapshot.color_image.width = color_image.shape[1]
    snapshot.color_image.height = color_image.shape[0]
    snapshot.color_image.data = color_image.tobytes()


encode_color_image.field = "ColorImageCommunicated"
