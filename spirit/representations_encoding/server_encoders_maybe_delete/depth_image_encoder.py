def encode_depth_image(depth_image, _, **kwargs):
    """
    depth_image: array to encode
    """
    snapshot = kwargs["snapshot"]
    snapshot.depth_image.width = depth_image.shape[1]
    snapshot.depth_image.height = depth_image.shape[0]
    #  TODO: change to tobytes if needed
    snapshot.depth_image.data.extend(depth_image.flatten().tolist())


encode_depth_image.field = "DepthImageCommunicated"
