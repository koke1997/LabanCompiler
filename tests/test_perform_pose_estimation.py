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

if __name__ == '__main__':
    unittest.main()
