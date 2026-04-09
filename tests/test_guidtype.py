import unittest
import os
import csv
from unittest.mock import patch

class TestLogError(unittest.TestCase):

    def setUp(self):
        os.makedirs("logs", exist_ok=True)

    @patch("guidtype.get_guid", return_value="test-guid-1234")
    def test_log_error_creates_log_file(self, mock_guid):
        from guidtype import log_error
        log_error("test_file.csv", "Test reason")
        from datetime import datetime
        date_today = datetime.now().strftime("%Y%m%d")
        log_file = os.path.join("logs", f"error_log_{date_today}.csv")
        self.assertTrue(os.path.isfile(log_file))

    @patch("guidtype.get_guid", return_value="test-guid-5678")
    def test_log_error_writes_correct_columns(self, mock_guid):
        from guidtype import log_error
        log_error("bad_file.csv", "Empty file")
        from datetime import datetime
        date_today = datetime.now().strftime("%Y%m%d")
        log_file = os.path.join("logs", f"error_log_{date_today}.csv")
        with open(log_file, "r") as f:
            reader = csv.reader(f)
            rows = list(reader)
        headers = rows[0]
        self.assertIn("guid", headers)
        self.assertIn("filename", headers)
        self.assertIn("reason", headers)

if __name__ == "__main__":
    unittest.main()