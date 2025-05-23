# scripts_v2/my_script/tests/test_run_data_process.py
import unittest
import os
from unittest.mock import patch, mock_open
from scripts_v2.my_script.run_data_process import process_data

class TestRunDataProcess(unittest.TestCase):

    def test_process_data_basic(self):
        mock_file_content = "hello world"
        expected_output = "hello world"
        with patch("builtins.open", mock_open(read_data=mock_file_content)) as mock_file:
            process_data("input.txt", "output.txt", False)
            mock_file.assert_any_call("input.txt", 'r')
            mock_file.assert_any_call("output.txt", 'w')
            mock_file().write.assert_called_once_with(expected_output)

    def test_process_data_upper_case(self):
        mock_file_content = "hello world"
        expected_output = "HELLO WORLD"
        with patch("builtins.open", mock_open(read_data=mock_file_content)) as mock_file:
            process_data("input.txt", "output.txt", True)
            mock_file.assert_any_call("input.txt", 'r')
            mock_file.assert_any_call("output.txt", 'w')
            mock_file().write.assert_called_once_with(expected_output)

    def test_process_data_input_not_found(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            with patch('builtins.print') as mock_print:
                process_data("non_existent.txt", "output.txt", False)
                mock_print.assert_called_once_with("Error: Input file 'non_existent.txt' not found.")