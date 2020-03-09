def encode_color_image(color_image, _, snapshot):
    """
    color_image: array to encode
    """
    snapshot.color_image.width = color_image.width
    snapshot.color_image.height = color_image.height
    snapshot.color_image.blob_id = color_image.blob_id


encode_color_image.field = "ColorImageInner"
