

class RepresentationSnapshot:
    def __init__(self, date_time, pose, color_image, depth_image, feelings,
                 snapshot_id):
        """
        date_time is datetime.datetime
        pose is Representation Pose
        color_image is numpy array in format of
         (width, height, rgb) array
        depth_image is numpy array in format of
        (width, height) array of float values
        feelings is RepresentationFeelings
        """
        self.date_time = date_time
        self.pose = pose
        self.color_image = color_image
        self.depth_image = depth_image
        self.feelings = feelings
        self.snapshot_id = snapshot_id
