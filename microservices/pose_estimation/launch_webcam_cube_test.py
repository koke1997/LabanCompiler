import cv2
import mediapipe as mp

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

                # Log the position of the human in the 3D cube
                human_position = {
                    'x': results.pose_landmarks.landmark[0].x,
                    'y': results.pose_landmarks.landmark[0].y,
                    'z': results.pose_landmarks.landmark[0].z
                }
                print(f"Human position in 3D cube: {human_position}")

                # Create a Labanotation language dictionary for the human position
                labanotation_dict = {
                    'head': {
                        'x': results.pose_landmarks.landmark[0].x,
                        'y': results.pose_landmarks.landmark[0].y,
                        'z': results.pose_landmarks.landmark[0].z
                    },
                    'left_hand': {
                        'x': results.pose_landmarks.landmark[15].x,
                        'y': results.pose_landmarks.landmark[15].y,
                        'z': results.pose_landmarks.landmark[15].z
                    },
                    'right_hand': {
                        'x': results.pose_landmarks.landmark[16].x,
                        'y': results.pose_landmarks.landmark[16].y,
                        'z': results.pose_landmarks.landmark[16].z
                    },
                    'torso': {
                        'x': results.pose_landmarks.landmark[11].x,
                        'y': results.pose_landmarks.landmark[11].y,
                        'z': results.pose_landmarks.landmark[11].z
                    }
                }
                print(f"Labanotation dictionary: {labanotation_dict}")

            # Show the frame
            cv2.imshow('Webcam Cube Test', frame)

            # Exit if 'Esc' key is pressed
            if cv2.waitKey(5) & 0xFF == 27:
                break

    cap.release()
    cv2.destroyAllWindows()
