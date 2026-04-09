import unittest
import os

class TestFileGeneration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        import testing  # runs all generate functions

    def test_valid_file_exists(self):
        self.assertTrue(os.path.isfile("test_ftp_data/MED_DATA_20230603140104.csv"))

    def test_empty_file_exists(self):
        self.assertTrue(os.path.isfile("test_ftp_data/MED_DATA_20230603140200.csv"))

    def test_empty_file_is_empty(self):
        size = os.path.getsize("test_ftp_data/MED_DATA_20230603140200.csv")
        self.assertEqual(size, 0)

    def test_bad_filename_exists(self):
        self.assertTrue(os.path.isfile("test_ftp_data/med_data_20230603.csv"))

    def test_duplicate_batch_file_exists(self):
        self.assertTrue(os.path.isfile("test_ftp_data/MED_DATA_20230603140400.csv"))

    def test_invalid_readings_file_exists(self):
        self.assertTrue(os.path.isfile("test_ftp_data/MED_DATA_20230603140500.csv"))

    def test_missing_columns_file_exists(self):
        self.assertTrue(os.path.isfile("test_ftp_data/MED_DATA_20230603140600.csv"))

if __name__ == "__main__":
    unittest.main()