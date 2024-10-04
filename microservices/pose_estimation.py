import cv2
import numpy as np
import mediapipe as mp
import requests

def receive_frames_from_video_input(frames):
    pose_estimations = perform_pose_estimation(frames)
    send_pose_data_to_labanotation_generation(pose_estimations)

def perform_pose_estimation(frames):
    pose_estimations = []
    mp_pose = mp.solutions.pose
    with mp_pose.Pose(static_image_mode=True) as pose:
        for frame in frames:
            results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            if results.pose_landmarks:
                pose_estimations.append(results.pose_landmarks)
    return pose_estimations

def send_pose_data_to_labanotation_generation(pose_estimations):
    labanotation_generation_url = "http://localhost:5002/labanotation"
    for pose in pose_estimations:
        response = requests.post(labanotation_generation_url, json=pose)
        if response.status_code != 200:
            print(f"Failed to send pose data to Labanotation generation service: {response.status_code}")
