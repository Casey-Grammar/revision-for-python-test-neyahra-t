import unittest
from unittest.mock import patch
import io
import sys
import Task3

class TestTask3(unittest.TestCase):
    
    @patch('builtins.input', return_value='1')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one_dog_year(self, mock_stdout, mock_input):
        """Test conversion of 1 dog year to human years"""
        Task3.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Human years = 7")
    
    @patch('builtins.input', return_value='5')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_five_dog_years(self, mock_stdout, mock_input):
        """Test conversion of 5 dog years to human years"""
        Task3.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Human years = 35")
    
    @patch('builtins.input', return_value='0')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_zero_dog_years(self, mock_stdout, mock_input):
        """Test conversion of 0 dog years to human years"""
        Task3.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Human years = 0")
    
    @patch('builtins.input', return_value='10')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ten_dog_years(self, mock_stdout, mock_input):
        """Test conversion of 10 dog years to human years"""
        Task3.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Human years = 70")
    
    @patch('builtins.input', side_effect=['abc', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_input_handling(self, mock_stdout, mock_input):
        """Test handling of invalid input (should raise ValueError)"""
        with self.assertRaises(ValueError):
            Task3.main()

if __name__ == '__main__':
    unittest.main()