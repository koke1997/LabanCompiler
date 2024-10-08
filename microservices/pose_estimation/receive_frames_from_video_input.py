import logging
import time
from .perform_pose_estimation import perform_pose_estimation

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def receive_frames_from_video_input(frames):
    pose_estimations = perform_pose_estimation(frames)
    log_body_part_positions(pose_estimations)

def log_body_part_positions(pose_estimations):
    while True:
        for pose in pose_estimations:
            for landmark in pose.landmark:
                logger.info(f"Body part: {landmark.name}, Position: x={landmark.x}, y={landmark.y}, z={landmark.z}")
            # Log the position of the human in the 3D cube
            human_position = {
                'x': pose.landmark[0].x,
                'y': pose.landmark[0].y,
                'z': pose.landmark[0].z
            }
            logger.info(f"Human position in 3D cube: {human_position}")
        time.sleep(1)
