import argparse
import yaml
import cv2
from microservices import video_input, pose_estimation, human_selection, labanotation_generation
from microservices.pose_estimation.perform_pose_estimation import launch_webcam_test
from microservices.pose_estimation.launch_webcam_cube_test import launch_webcam_cube_test

def main():
    parser = argparse.ArgumentParser(description="Labanotation Generator from Video")
    parser.add_argument("--input", type=str, help="Path to the input video file")
    parser.add_argument("--output", type=str, help="Path to save the generated Labanotation")
    parser.add_argument("--select-human", action="store_true", help="Enable human selection by drawing a border")
    parser.add_argument("--webcam-test", action="store_true", help="Launch test from webcam")
    parser.add_argument("--webcam-cube", action="store_true", help="Launch cube test from webcam")
    args = parser.parse_args()

    if args.webcam_test:
        launch_webcam_test()
        return

    if args.webcam_cube:
        launch_webcam_cube_test()
        return

    video_path = args.input
    output_path = args.output
    select_human = args.select_human

    frames = video_input.extract_frames(video_path)
    if select_human:
        frames = human_selection.receive_video_frames(frames)
    pose_estimations = pose_estimation.receive_frames_from_video_input(frames)
    labanotation_generation.receive_pose_data(pose_estimations)

    labanotation = labanotation_generation.generate_labanotation(pose_estimations)
    labanotation_generation.save_labanotation(labanotation, output_path)

    # Draw a 3D cube around the human
    for frame in frames:
        for pose in pose_estimations:
            for landmark in pose.landmark:
                x = int(landmark.x * frame.shape[1])
                y = int(landmark.y * frame.shape[0])
                cv2.rectangle(frame, (x - 10, y - 10), (x + 10, y + 10), (0, 255, 0), 2)

    # Log the position of the human in the 3D cube
    for pose in pose_estimations:
        human_position = {
            'x': pose.landmark[0].x,
            'y': pose.landmark[0].y,
            'z': pose.landmark[0].z
        }
        print(f"Human position in 3D cube: {human_position}")

if __name__ == "__main__":
    main()
