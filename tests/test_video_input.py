import unittest
from unittest.mock import patch, MagicMock
import microservices.video_input as video_input

class TestVideoInput(unittest.TestCase):

    @patch('microservices.video_input.cv2.VideoCapture')
    def test_read_video(self, mock_VideoCapture):
        mock_cap = MagicMock()
        mock_VideoCapture.return_value = mock_cap
        mock_cap.isOpened.side_effect = [True, True, False]
        mock_cap.read.side_effect = [(True, 'frame1'), (True, 'frame2')]

        frames = video_input.read_video('video_path')

        mock_VideoCapture.assert_called_once_with('video_path')
        self.assertEqual(frames, ['frame1', 'frame2'])
        mock_cap.release.assert_called_once()

    @patch('microservices.video_input.read_video')
    def test_extract_frames(self, mock_read_video):
        mock_read_video.return_value = ['frame1', 'frame2']

        frames = video_input.extract_frames('video_path')

        mock_read_video.assert_called_once_with('video_path')
        self.assertEqual(frames, ['frame1', 'frame2'])

    @patch('microservices.video_input.requests.post')
    @patch('microservices.video_input.cv2.imencode')
    def test_send_frames_to_pose_estimation(self, mock_imencode, mock_post):
        mock_imencode.return_value = (True, 'encoded_frame')
        mock_post.return_value.status_code = 200

        frames = ['frame1', 'frame2']
        video_input.send_frames_to_pose_estimation(frames, 'pose_estimation_url')

        self.assertEqual(mock_imencode.call_count, 2)
        self.assertEqual(mock_post.call_count, 2)
        mock_post.assert_any_call('pose_estimation_url', data='encoded_frame'.tostring(), headers={'Content-Type': 'application/octet-stream'})

if __name__ == '__main__':
    unittest.main()
