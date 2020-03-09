class RepresentationPose:
    def __init__(self, rotation, translation):
        """
        rotation is (x, y, z, w)
        translation is (x, y, z)
        """
        self.rotation = rotation
        self.translation = translation
