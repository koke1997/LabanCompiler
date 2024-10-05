import unittest
from unittest.mock import patch, MagicMock
import bewegungsschrift

class TestBewegungsschrift(unittest.TestCase):

    @patch('bewegungsschrift.argparse.ArgumentParser.parse_args')
    def test_main_with_webcam_test(self, mock_parse_args):
        mock_parse_args.return_value = MagicMock(webcam_test=True, input=None, output=None, select_human=False)
        with patch('bewegungsschrift.pose_estimation.launch_webcam_test') as mock_launch_webcam_test:
            bewegungsschrift.main()
            mock_launch_webcam_test.assert_called_once()

    @patch('bewegungsschrift.argparse.ArgumentParser.parse_args')
    def test_main_with_webcam_cube(self, mock_parse_args):
        mock_parse_args.return_value = MagicMock(webcam_cube=True, input=None, output=None, select_human=False)
        with patch('bewegungsschrift.pose_estimation.launch_webcam_cube_test') as mock_launch_webcam_cube_test:
            bewegungsschrift.main()
            mock_launch_webcam_cube_test.assert_called_once()

    @patch('bewegungsschrift.argparse.ArgumentParser.parse_args')
    def test_main_with_video_input(self, mock_parse_args):
        mock_parse_args.return_value = MagicMock(webcam_test=False, input='input.mp4', output='output.yaml', select_human=False)
        with patch('bewegungsschrift.video_input.extract_frames', return_value=['frame1', 'frame2']) as mock_extract_frames, \
             patch('bewegungsschrift.pose_estimation.receive_frames_from_video_input', return_value=['pose1', 'pose2']) as mock_receive_frames, \
             patch('bewegungsschrift.labanotation_generation.generate_labanotation', return_value='labanotation') as mock_generate_labanotation, \
             patch('bewegungsschrift.labanotation_generation.save_labanotation') as mock_save_labanotation:
            bewegungsschrift.main()
            mock_extract_frames.assert_called_once_with('input.mp4')
            mock_receive_frames.assert_called_once_with(['frame1', 'frame2'])
            mock_generate_labanotation.assert_called_once_with(['pose1', 'pose2'])
            mock_save_labanotation.assert_called_once_with('labanotation', 'output.yaml')

    @patch('bewegungsschrift.argparse.ArgumentParser.parse_args')
    def test_main_with_human_selection(self, mock_parse_args):
        mock_parse_args.return_value = MagicMock(webcam_test=False, input='input.mp4', output='output.yaml', select_human=True)
        with patch('bewegungsschrift.video_input.extract_frames', return_value=['frame1', 'frame2']) as mock_extract_frames, \
             patch('bewegungsschrift.human_selection.receive_video_frames', return_value=['selected_frame1', 'selected_frame2']) as mock_receive_video_frames, \
             patch('bewegungsschrift.pose_estimation.receive_frames_from_video_input', return_value=['pose1', 'pose2']) as mock_receive_frames, \
             patch('bewegungsschrift.labanotation_generation.generate_labanotation', return_value='labanotation') as mock_generate_labanotation, \
             patch('bewegungsschrift.labanotation_generation.save_labanotation') as mock_save_labanotation:
            bewegungsschrift.main()
            mock_extract_frames.assert_called_once_with('input.mp4')
            mock_receive_video_frames.assert_called_once_with(['frame1', 'frame2'])
            mock_receive_frames.assert_called_once_with(['selected_frame1', 'selected_frame2'])
            mock_generate_labanotation.assert_called_once_with(['pose1', 'pose2'])
            mock_save_labanotation.assert_called_once_with('labanotation', 'output.yaml')

    @patch('bewegungsschrift.argparse.ArgumentParser.parse_args')
    def test_main_with_webcam_cube_logging(self, mock_parse_args):
        mock_parse_args.return_value = MagicMock(webcam_cube=True, input=None, output=None, select_human=False)
        with patch('bewegungsschrift.pose_estimation.launch_webcam_cube_test') as mock_launch_webcam_cube_test, \
             patch('builtins.print') as mock_print:
            bewegungsschrift.main()
            mock_launch_webcam_cube_test.assert_called_once()
            mock_print.assert_any_call("Human position in 3D cube: {'x': 0.5, 'y': 0.5, 'z': 0.0}")

if __name__ == '__main__':
    unittest.main()
