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
    mp_drawing = mp.solutions.drawing_utils
    mp_holistic = mp.solutions.holistic
    mp_face_mesh = mp.solutions.face_mesh

    cap = cv2.VideoCapture(0)
    with mp_holistic.Holistic(static_image_mode=False) as holistic:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Convert the BGR image to RGB for processing
            results = holistic.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            # Draw pose landmarks
            if results.pose_landmarks:
                mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

            # Draw left hand landmarks
            if results.left_hand_landmarks:
                mp_drawing.draw_landmarks(frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

            # Draw right hand landmarks
            if results.right_hand_landmarks:
                mp_drawing.draw_landmarks(frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

            # Draw face landmarks using FACEMESH_CONTOURS or FACEMESH_TESSELATION
            if results.face_landmarks:
                mp_drawing.draw_landmarks(frame, results.face_landmarks, mp_face_mesh.FACEMESH_CONTOURS)

            # Show the frame
            cv2.imshow('Webcam Test', frame)

            # Exit if 'Esc' key is pressed
            if cv2.waitKey(5) & 0xFF == 27:
                break

    cap.release()
    cv2.destroyAllWindows()

def launch_webcam_cube_test():
    mp_drawing = mp.solutions.drawing_utils
    mp_holistic = mp.solutions.holistic
    mp_face_mesh = mp.solutions.face_mesh

    cap = cv2.VideoCapture(0)
    with mp_holistic.Holistic(static_image_mode=False) as holistic:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Convert the BGR image to RGB for processing
            results = holistic.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            # Draw pose landmarks
            if results.pose_landmarks:
                mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

            # Draw left hand landmarks
            if results.left_hand_landmarks:
                mp_drawing.draw_landmarks(frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

            # Draw right hand landmarks
            if results.right_hand_landmarks:
                mp_drawing.draw_landmarks(frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

            # Draw face landmarks using FACEMESH_CONTOURS or FACEMESH_TESSELATION
            if results.face_landmarks:
                mp_drawing.draw_landmarks(frame, results.face_landmarks, mp_face_mesh.FACEMESH_CONTOURS)

            # Draw a cube around the detected pose
            if results.pose_landmarks:
                for landmark in results.pose_landmarks.landmark:
                    x = int(landmark.x * frame.shape[1])
                    y = int(landmark.y * frame.shape[0])
                    cv2.rectangle(frame, (x - 10, y - 10), (x + 10, y + 10), (0, 255, 0), 2)

            # Show the frame
            cv2.imshow('Webcam Cube Test', frame)

            # Exit if 'Esc' key is pressed
            if cv2.waitKey(5) & 0xFF == 27:
                break

    cap.release()
    cv2.destroyAllWindows()
