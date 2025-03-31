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


class TestReadFilePandas(unittest.TestCase):
    def setUp(self):
        """Test .csv data preparing"""
        self.test_csv = "test_data.csv"
        self.test_data = pd.DataFrame({
            'Name': ['Anton', 'Masha'],
            'Age': [19, 21]
        })
        self.test_data.to_csv(self.test_csv, index=False)

    def test_read_valid_csv(self):
        """Test of reading correct .csv file"""
        df = read_file_pandas(self.test_csv)
        pd.testing.assert_frame_equal(df, self.test_data)

    def test_file_not_found(self):
        """Test of reading unexisting file"""
        with self.assertRaises(FileNotFoundError):
            read_file_pandas("nonexistent.csv")

    def test_empty_csv(self):
        """Test of reading empty .csv file"""
        empty_csv = "empty.csv"
        pd.DataFrame().to_csv(empty_csv)

        df = read_file_pandas(empty_csv)
        self.assertTrue(df.empty)

    def tearDown(self):
        """Clearing after all tests"""
        try:
            os.remove(self.test_csv)
            os.remove("empty.csv")
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()