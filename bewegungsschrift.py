import argparse
import yaml
from microservices import video_input, pose_estimation, human_selection, labanotation_generation

def main():
    parser = argparse.ArgumentParser(description="Labanotation Generator from Video")
    parser.add_argument("--input", type=str, required=True, help="Path to the input video file")
    parser.add_argument("--output", type=str, required=True, help="Path to save the generated Labanotation")
    parser.add_argument("--select-human", action="store_true", help="Enable human selection by drawing a border")
    args = parser.parse_args()

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

if __name__ == "__main__":
    main()
