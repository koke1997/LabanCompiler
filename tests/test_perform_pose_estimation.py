import unittest
from unittest.mock import patch, MagicMock
import microservices.pose_estimation.perform_pose_estimation as perform_pose_estimation

class TestPerformPoseEstimation(unittest.TestCase):

    @patch('microservices.pose_estimation.perform_pose_estimation.mp.solutions.holistic.Holistic.process')
    def test_perform_pose_estimation(self, mock_process):
        mock_results = MagicMock()
        mock_results.pose_landmarks = 'pose_landmarks'
        mock_results.left_hand_landmarks = 'left_hand_landmarks'
        mock_results.right_hand_landmarks = 'right_hand_landmarks'
        mock_results.face_landmarks = 'face_landmarks'
        mock_process.return_value = mock_results

        frames = ['frame1', 'frame2']
        expected_pose_estimations = ['pose_landmarks', 'left_hand_landmarks', 'right_hand_landmarks', 'face_landmarks',
                                     'pose_landmarks', 'left_hand_landmarks', 'right_hand_landmarks', 'face_landmarks']

        pose_estimations = perform_pose_estimation.perform_pose_estimation(frames)
        self.assertEqual(pose_estimations, expected_pose_estimations)

    @patch('microservices.pose_estimation.launch_webcam_cube_test.cv2.VideoCapture')
    @patch('microservices.pose_estimation.launch_webcam_cube_test.mp.solutions.holistic.Holistic.process')
    @patch('microservices.pose_estimation.launch_webcam_cube_test.cv2.imshow')
    @patch('microservices.pose_estimation.launch_webcam_cube_test.cv2.waitKey', return_value=27)
    @patch('microservices.pose_estimation.launch_webcam_cube_test.cv2.destroyAllWindows')
    def test_launch_webcam_cube_test(self, mock_destroyAllWindows, mock_waitKey, mock_imshow, mock_process, mock_VideoCapture):
        mock_cap = MagicMock()
        mock_VideoCapture.return_value = mock_cap
        mock_cap.isOpened.side_effect = [True, False]
        mock_cap.read.return_value = (True, 'frame')

        mock_results = MagicMock()
        mock_results.pose_landmarks = MagicMock()
        mock_results.pose_landmarks.landmark = [MagicMock(x=0.5, y=0.5, z=0.0)]
        mock_process.return_value = mock_results

        perform_pose_estimation.launch_webcam_cube_test()

        mock_VideoCapture.assert_called_once_with(0)
        mock_cap.read.assert_called_once()
        mock_process.assert_called_once()
        mock_imshow.assert_called_once_with('Webcam Cube Test', 'frame')
        mock_waitKey.assert_called_once_with(5)
        mock_destroyAllWindows.assert_called_once()

if __name__ == '__main__':
    unittest.main()
