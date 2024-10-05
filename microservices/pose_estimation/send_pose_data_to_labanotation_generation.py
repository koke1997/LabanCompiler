import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_pose_data_to_labanotation_generation(pose_estimations):
    labanotation_generation_url = "http://localhost:5002/labanotation"
    for pose in pose_estimations:
        try:
            # Convert NormalizedLandmarkList to a serializable format
            pose_data = [{'x': lm.x, 'y': lm.y, 'z': lm.z, 'visibility': lm.visibility} for lm in pose.landmark]
            
            # Log request details
            logger.info(f"Sending POST request to {labanotation_generation_url}")
            logger.info(f"Payload: {pose_data}")
            
            response = requests.post(labanotation_generation_url, json=pose_data)
            
            # Log response details
            logger.info(f"Response status code: {response.status_code}")
            logger.info(f"Response content: {response.content}")
            
            if response.status_code != 200:
                logger.error(f"Failed to send pose data to Labanotation generation service: {response.status_code}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
