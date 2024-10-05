import unittest
from unittest.mock import patch, mock_open
import microservices.labanotation_generation as labanotation_generation

class TestLabanotationGeneration(unittest.TestCase):

    def test_generate_labanotation(self):
        pose_data = [
            [{'name': 'nose', 'x': 0.5, 'y': 0.5, 'z': 0.0, 'visibility': 0.9}],
            [{'name': 'left_eye', 'x': 0.4, 'y': 0.4, 'z': 0.0, 'visibility': 0.8}]
        ]
        expected_labanotation = [
            {'nose': {'x': 0.5, 'y': 0.5, 'z': 0.0, 'visibility': 0.9}},
            {'left_eye': {'x': 0.4, 'y': 0.4, 'z': 0.0, 'visibility': 0.8}}
        ]
        labanotation = labanotation_generation.generate_labanotation(pose_data)
        self.assertEqual(labanotation, expected_labanotation)

    def test_convert_pose_to_labanotation(self):
        pose = [{'name': 'nose', 'x': 0.5, 'y': 0.5, 'z': 0.0, 'visibility': 0.9}]
        expected_notation = {'nose': {'x': 0.5, 'y': 0.5, 'z': 0.0, 'visibility': 0.9}}
        notation = labanotation_generation.convert_pose_to_labanotation(pose)
        self.assertEqual(notation, expected_notation)

    @patch('builtins.open', new_callable=mock_open)
    @patch('microservices.labanotation_generation.yaml.dump')
    def test_save_labanotation(self, mock_yaml_dump, mock_open):
        labanotation = [{'nose': {'x': 0.5, 'y': 0.5, 'z': 0.0, 'visibility': 0.9}}]
        output_path = 'output.yaml'
        labanotation_generation.save_labanotation(labanotation, output_path)
        mock_open.assert_called_once_with(output_path, 'w')
        mock_yaml_dump.assert_called_once_with(labanotation, mock_open())

if __name__ == '__main__':
    unittest.main()
