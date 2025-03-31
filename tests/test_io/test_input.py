import unittest
import os
import pandas as pd
from app.io.input import read_file_builtin
from app.io.input import read_file_pandas


class TestReadFileBuiltin(unittest.TestCase):
    def setUp(self):
        """Test data preparing"""
        self.test_file = "test_data.txt"
        self.test_content = "It is test data"
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write(self.test_content)

    def test_read_existing_file(self):
        """Test of reading existing file"""
        content = read_file_builtin(self.test_file)
        self.assertEqual(content, self.test_content)

    def test_file_not_found(self):
        """Test incase file is not exist"""
        with self.assertRaises(FileNotFoundError):
            read_file_builtin("nonexistent_file.txt")

    def test_empty_file(self):
        """Trying to read empty file"""
        empty_file = "empty.txt"
        with open(empty_file, 'w', encoding='utf-8') as f:
            pass

        self.assertEqual(read_file_builtin(empty_file), "")

    def tearDown(self):
        """Clearing"""
        try:
            os.remove(self.test_file)
            os.remove("empty.txt")
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    unittest.main()