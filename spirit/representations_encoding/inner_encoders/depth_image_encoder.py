def encode_depth_image(depth_image, _, snapshot):
    """
    depth_image: array to encode
    """
    snapshot.depth_image.width = depth_image.width
    snapshot.depth_image.height = depth_image.height
    snapshot.depth_image.blob_id = depth_image.blob_id


encode_depth_image.field = "DepthImageInner"
