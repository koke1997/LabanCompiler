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

def launch_webcam_test():
    mp_holistic = mp.solutions.holistic
    cap = cv2.VideoCapture(0)
    with mp_holistic.Holistic(static_image_mode=False) as holistic:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            results = holistic.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            if results.pose_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
            if results.left_hand_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
            if results.right_hand_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
            if results.face_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(frame, results.face_landmarks, mp_holistic.FACE_CONNECTIONS)
            cv2.imshow('Webcam Test', frame)
            if cv2.waitKey(5) & 0xFF == 27:
                break
    cap.release()
    cv2.destroyAllWindows()
