import unittest
from unittest.mock import patch, mock_open
import sys
import os
import json

# 添加父目录到 Python 路径，以便能够导入 AutoUpdater
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))))

from autoupdater import AutoUpdater

class TestAutoUpdater(unittest.TestCase):
    def setUp(self):
        self.local_directory = "test_local_dir"
        self.remote_base_url = "http://example.com/remote/"
        self.updater = AutoUpdater(self.local_directory, self.remote_base_url)

    @patch('os.walk')
    @patch('builtins.open', new_callable=mock_open)
    def test_get_file_list_with_md5(self, mock_file, mock_walk):
        mock_walk.return_value = [
            ("root", [], ["file1.txt", "file2.txt", "md5.json"])
        ]
        mock_file.return_value.read.return_value = b"test content"
        
        result = self.updater.get_file_list_with_md5(self.local_directory)
        
        self.assertEqual(len(result), 2)
        self.assertIn("file1.txt", result)
        self.assertIn("file2.txt", result)
        self.assertNotIn("md5.json", result)

    @patch('requests.get')
    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    def test_update_files(self, mock_file, mock_makedirs, mock_get):
        mock_get.return_value.json.return_value = {
            "file1.txt": "new_md5",
            "file2.txt": "old_md5"
        }
        self.updater.get_file_list_with_md5 = lambda x: {"file2.txt": "old_md5"}
        
        result = json.loads(self.updater.update_files())
        
        self.assertEqual(result["status"], "success")
        self.assertEqual(len(result["updated_files"]), 1)
        self.assertIn("file1.txt", result["updated_files"])

if __name__ == '__main__':
    unittest.main()