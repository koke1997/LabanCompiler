import unittest
from unittest.mock import patch, MagicMock
import microservices.human_selection as human_selection

class TestHumanSelection(unittest.TestCase):

    @patch('microservices.human_selection.cv2.selectROI')
    @patch('microservices.human_selection.cv2.destroyWindow')
    def test_select_human(self, mock_destroyWindow, mock_selectROI):
        mock_selectROI.return_value = (10, 10, 100, 100)
        frame = MagicMock()
        selected_frame = human_selection.select_human(frame)
        mock_selectROI.assert_called_once_with("Select Human", frame, fromCenter=False, showCrosshair=True)
        mock_destroyWindow.assert_called_once_with("Select Human")
        self.assertEqual(selected_frame, frame[10:110, 10:110])

    @patch('microservices.human_selection.select_human')
    def test_receive_video_frames(self, mock_select_human):
        mock_select_human.side_effect = lambda frame: f"selected_{frame}"
        frames = ['frame1', 'frame2', 'frame3']
        selected_frames = human_selection.receive_video_frames(frames)
        self.assertEqual(selected_frames, ['selected_frame1', 'selected_frame2', 'selected_frame3'])
        self.assertEqual(mock_select_human.call_count, 3)

if __name__ == '__main__':
    unittest.main()
