import cv2
import numpy as np
import openpose
import requests

def receive_frames_from_video_input(frames):
    pose_estimations = perform_pose_estimation(frames)
    send_pose_data_to_labanotation_generation(pose_estimations)

def perform_pose_estimation(frames):
    pose_estimations = []
    for frame in frames:
        pose = openpose.detect_pose(frame)
        pose_estimations.append(pose)
    return pose_estimations

def send_pose_data_to_labanotation_generation(pose_estimations):
    labanotation_generation_url = "http://localhost:5002/labanotation"
    for pose in pose_estimations:
        response = requests.post(labanotation_generation_url, json=pose)
        if response.status_code != 200:
            print(f"Failed to send pose data to Labanotation generation service: {response.status_code}")
