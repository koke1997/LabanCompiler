import cv2
import mediapipe as mp

def perform_pose_estimation(frames):
    pose_estimations = []
    mp_holistic = mp.solutions.holistic
    with mp_holistic.Holistic(static_image_mode=True) as holistic:
        for frame in frames:
            results = holistic.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            if results.pose_landmarks:
                pose_estimations.append(results.pose_landmarks)
            if results.left_hand_landmarks:
                pose_estimations.append(results.left_hand_landmarks)
            if results.right_hand_landmarks:
                pose_estimations.append(results.right_hand_landmarks)
            if results.face_landmarks:
                pose_estimations.append(results.face_landmarks)
    return pose_estimations
