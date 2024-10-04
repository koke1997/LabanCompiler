import cv2
import requests

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()
    return frames

def extract_frames(video_path):
    frames = read_video(video_path)
    return frames

def send_frames_to_pose_estimation(frames, pose_estimation_url):
    for frame in frames:
        _, img_encoded = cv2.imencode('.jpg', frame)
        response = requests.post(pose_estimation_url, data=img_encoded.tostring(), headers={'Content-Type': 'application/octet-stream'})
        if response.status_code != 200:
            print(f"Failed to send frame to pose estimation service: {response.status_code}")
