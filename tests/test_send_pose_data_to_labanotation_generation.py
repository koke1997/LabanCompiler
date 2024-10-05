import unittest
from unittest.mock import patch, MagicMock
import microservices.pose_estimation.send_pose_data_to_labanotation_generation as send_pose_data_to_labanotation_generation

class TestSendPoseDataToLabanotationGeneration(unittest.TestCase):

    @patch('microservices.pose_estimation.send_pose_data_to_labanotation_generation.requests.post')
    @patch('microservices.pose_estimation.send_pose_data_to_labanotation_generation.logger.info')
    @patch('microservices.pose_estimation.send_pose_data_to_labanotation_generation.logger.error')
    def test_send_pose_data_to_labanotation_generation(self, mock_logger_error, mock_logger_info, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = "Success"
        mock_post.return_value = mock_response

        pose_estimations = [MagicMock()]
        pose_estimations[0].landmark = [MagicMock(x=0.1, y=0.2, z=0.3, visibility=0.9)]

        send_pose_data_to_labanotation_generation.send_pose_data_to_labanotation_generation(pose_estimations)

        mock_post.assert_called_once()
        mock_logger_info.assert_any_call("Sending POST request to http://localhost:5002/labanotation")
        mock_logger_info.assert_any_call("Payload: [{'x': 0.1, 'y': 0.2, 'z': 0.3, 'visibility': 0.9}]")
        mock_logger_info.assert_any_call("Response status code: 200")
        mock_logger_info.assert_any_call("Response content: Success")
        mock_logger_error.assert_not_called()

    @patch('microservices.pose_estimation.send_pose_data_to_labanotation_generation.requests.post')
    @patch('microservices.pose_estimation.send_pose_data_to_labanotation_generation.logger.error')
    def test_send_pose_data_to_labanotation_generation_failure(self, mock_logger_error, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.content = "Internal Server Error"
        mock_post.return_value = mock_response

        pose_estimations = [MagicMock()]
        pose_estimations[0].landmark = [MagicMock(x=0.1, y=0.2, z=0.3, visibility=0.9)]

        send_pose_data_to_labanotation_generation.send_pose_data_to_labanotation_generation(pose_estimations)

        mock_post.assert_called_once()
        mock_logger_error.assert_any_call("Failed to send pose data to Labanotation generation service: 500")

    @patch('microservices.pose_estimation.send_pose_data_to_labanotation_generation.requests.post')
    @patch('microservices.pose_estimation.send_pose_data_to_labanotation_generation.logger.error')
    def test_send_pose_data_to_labanotation_generation_exception(self, mock_logger_error, mock_post):
        mock_post.side_effect = requests.exceptions.RequestException("Request failed")

        pose_estimations = [MagicMock()]
        pose_estimations[0].landmark = [MagicMock(x=0.1, y=0.2, z=0.3, visibility=0.9)]

        send_pose_data_to_labanotation_generation.send_pose_data_to_labanotation_generation(pose_estimations)

        mock_post.assert_called_once()
        mock_logger_error.assert_any_call("Request failed: Request failed")

if __name__ == '__main__':
    unittest.main()
