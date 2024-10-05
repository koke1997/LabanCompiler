import yaml

def receive_pose_data(pose_data):
    labanotation = generate_labanotation(pose_data)
    save_labanotation(labanotation, "output.yaml")

def generate_labanotation(pose_data):
    labanotation = []
    for pose in pose_data:
        notation = convert_pose_to_labanotation(pose)
        labanotation.append(notation)
    return labanotation

def convert_pose_to_labanotation(pose):
    # Convert 3D pose data to Labanotation
    notation = {}
    for landmark in pose:
        notation[landmark['name']] = {
            'x': landmark['x'],
            'y': landmark['y'],
            'z': landmark['z'],
            'visibility': landmark['visibility']
        }
    return notation

def save_labanotation(labanotation, output_path):
    with open(output_path, 'w') as f:
        yaml.dump(labanotation, f)
