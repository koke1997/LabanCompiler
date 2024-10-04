import argparse
import cv2
import numpy as np
import mediapipe as mp
import yaml

def main():
    parser = argparse.ArgumentParser(description="Labanotation Generator from Video")
    parser.add_argument("--input", type=str, required=True, help="Path to the input video file")
    parser.add_argument("--output", type=str, required=True, help="Path to save the generated Labanotation")
    parser.add_argument("--select-human", action="store_true", help="Enable human selection by drawing a border")
    args = parser.parse_args()

    video_path = args.input
    output_path = args.output
    select_human = args.select_human

    frames = process_video_input(video_path, select_human)
    pose_estimations = perform_pose_estimation(frames)
    labanotation = generate_labanotation(pose_estimations)

    with open(output_path, 'w') as f:
        yaml.dump(labanotation, f)

def process_video_input(video_path, select_human=False):
    cap = cv2.VideoCapture(video_path)
    frames = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if select_human:
            frame = select_human_in_video(frame)
        frames.append(frame)

    cap.release()
    return frames

def select_human_in_video(frame):
    r = cv2.selectROI("Select Human", frame, fromCenter=False, showCrosshair=True)
    if r != (0, 0, 0, 0):
        x, y, w, h = r
        frame = frame[y:y+h, x:x+w]
    cv2.destroyWindow("Select Human")
    return frame

def perform_pose_estimation(frames):
    mp_pose = mp.solutions.pose
    pose_estimations = []

    with mp_pose.Pose(static_image_mode=True) as pose:
        for frame in frames:
            results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            if results.pose_landmarks:
                pose_estimations.append(results.pose_landmarks)
    return pose_estimations

def generate_labanotation(pose_estimations):
    labanotation = []
    for pose in pose_estimations:
        notation = convert_pose_to_labanotation(pose)
        labanotation.append(notation)
    return labanotation

def convert_pose_to_labanotation(pose):
    # Placeholder function to convert pose to Labanotation
    return {"pose": pose}

if __name__ == "__main__":
    main()
