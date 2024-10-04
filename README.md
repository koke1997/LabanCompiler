# Bewegungsschrift - Labanotation Generator from Video

**Bewegungsschrift** is a tool for generating Labanotation from video inputs, designed exclusively for analyzing human movement. This tool takes a video file as input, uses advanced computer vision to detect human body movements, and converts these movements into Labanotation symbols, creating a precise representation of human motion.

## Table of Contents
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Examples](#examples)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Video Input Analysis**: Accepts video files containing human subjects and analyzes the movement.
- **Human Pose Estimation**: Utilizes cutting-edge pose estimation models to detect and track the joints of human figures.
- **Labanotation Output**: Converts the extracted motion into Labanotation symbols, providing a detailed and standard representation of movement.
- **Optimized for Human Models**: Exclusively designed to detect and represent human movements, ensuring high accuracy.
- **Geometry and Programming Integration**: Combines elements of geometry for movement analysis and programming for automatic conversion to Labanotation.
- **Human Selection**: Allows selecting a human in the video by drawing a border around it.

## Technology Stack
- **Python**: Core language used for scripting and processing.
- **OpenCV**: For video processing, frame extraction, and human motion detection.
- **OpenPose**: A machine learning framework used for pose estimation and detecting human body joints.
- **NumPy**: For handling mathematical computations related to geometry.
- **Matplotlib**: Used to visualize the detected movements and their corresponding Labanotation.
- **LabanWriter Integration**: The generated Labanotation is compatible with LabanWriter for further editing.

## Installation
To get started with **Bewegungsschrift**, you need to install the required tools and dependencies.

### Prerequisites
- Python 3.8 or above
- Git
- Virtual environment (optional, but recommended)

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/username/Bewegungsschrift.git
    cd Bewegungsschrift
    ```
2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
After installing the necessary dependencies, you can start using **Bewegungsschrift** to convert videos into Labanotation.

### Command-Line Interface
1. **Basic Usage**:
    ```sh
    python bewegungsschrift.py --input path/to/your/video.mp4 --output path/to/output.yaml
    ```
    - `--input`: Path to the video file.
    - `--output`: Path to save the generated Labanotation.

2. **Optional Parameters**:
    - `--visualize`: Display a visualization of the movement analysis.
    - `--frame-rate`: Set the frame rate for processing the video (default: 10 fps).
    - `--select-human`: Enable human selection by drawing a border around the human in the video.

### Example
To analyze a video of a dance routine and generate the corresponding Labanotation:
```sh
python bewegungsschrift.py --input videos/dance.mp4 --output notations/dance_notation.yaml --visualize
```

To analyze a video and select a human by drawing a border around it:
```sh
python bewegungsschrift.py --input videos/dance.mp4 --output notations/dance_notation.yaml --select-human
```

## Configuration
You can modify the settings of the tool by editing the configuration file `config.yaml`. Key configuration options include:
- **Frame Rate**: Set the rate at which frames are sampled for analysis.
- **Pose Estimation Model**: Choose between different pose estimation models (e.g., OpenPose, BlazePose).
- **Output Format**: Specify the format for Labanotation output (e.g., JSON, XML).

## Examples
### Input Video
The tool accepts a video of a human performing movements, such as a dance or exercise routine. The video should clearly show the human subject without obstructions.

### Labanotation Output
The output is a Labanotation file that can be visualized or edited with software like LabanWriter.

Example output (YAML format):
```yaml
movements:
  - frame: 1
    body_part: left_arm
    direction: upward
    angle: 45
  - frame: 1
    body_part: right_leg
    direction: forward
    angle: 30
```

## Limitations
- **Human Only**: The tool is designed to work exclusively with human models. It may not accurately detect animals or non-human objects.
- **Video Quality**: The accuracy of Labanotation generation is dependent on the quality of the input video. High-resolution videos with minimal background noise are recommended.
- **Complex Movements**: Very fast or complex movements may result in reduced accuracy in pose estimation.

## Contributing
Contributions are welcome! If you have ideas for new features or find bugs, please open an issue or submit a pull request.

### Steps to Contribute
1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature-name
    ```
3. Make your changes and commit them:
    ```sh
    git commit -m "Description of changes"
    ```
4. Push to your fork and submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
