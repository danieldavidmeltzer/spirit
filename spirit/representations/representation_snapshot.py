class RepresentationSnapshot:
    def __init__(self, date_time, pose, color_image, depth_image, feelings):
        self.date_time = date_time
        self.pose = pose
        self.color_image = color_image
        self.depth_image = depth_image
        self.feelings = feelings


