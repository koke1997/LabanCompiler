import unittest
from unittest.mock import patch, MagicMock
import microservices.pose_estimation.receive_frames_from_video_input as receive_frames_from_video_input

class TestReceiveFramesFromVideoInput(unittest.TestCase):

    @patch('microservices.pose_estimation.receive_frames_from_video_input.perform_pose_estimation')
    @patch('microservices.pose_estimation.receive_frames_from_video_input.log_body_part_positions')
    def test_receive_frames_from_video_input(self, mock_log_body_part_positions, mock_perform_pose_estimation):
        frames = ['frame1', 'frame2']
        mock_pose_estimations = ['pose1', 'pose2']
        mock_perform_pose_estimation.return_value = mock_pose_estimations

        receive_frames_from_video_input.receive_frames_from_video_input(frames)

        mock_perform_pose_estimation.assert_called_once_with(frames)
        mock_log_body_part_positions.assert_called_once_with(mock_pose_estimations)

    @patch('microservices.pose_estimation.receive_frames_from_video_input.logger.info')
    @patch('time.sleep', return_value=None)
    def test_log_body_part_positions(self, mock_sleep, mock_logger_info):
        mock_pose_estimations = [MagicMock(), MagicMock()]
        mock_pose_estimations[0].landmark = [MagicMock(name='landmark1', x=0.1, y=0.2, z=0.3)]
        mock_pose_estimations[1].landmark = [MagicMock(name='landmark2', x=0.4, y=0.5, z=0.6)]

        with patch('microservices.pose_estimation.receive_frames_from_video_input.time.sleep', side_effect=KeyboardInterrupt):
            receive_frames_from_video_input.log_body_part_positions(mock_pose_estimations)

        mock_logger_info.assert_any_call("Body part: landmark1, Position: x=0.1, y=0.2, z=0.3")
        mock_logger_info.assert_any_call("Body part: landmark2, Position: x=0.4, y=0.5, z=0.6")

if __name__ == '__main__':
    unittest.main()
