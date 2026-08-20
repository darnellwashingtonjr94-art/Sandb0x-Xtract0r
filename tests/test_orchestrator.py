import unittest
import os
from src.orchestrator.router import FileRouter

class TestFileRouter(unittest.TestCase):
    def setUp(self):
        self.router = FileRouter()

    def test_missing_file_raises_exception(self):
        with self.assertRaises(FileNotFoundError):
            self.router.detect_platform("non_existent_file.exe")

    def test_extension_fallback(self):
        test_file = "test_sample.apk"
        with open(test_file, "w") as f:
            f.write("mock apk payload content")
        
        try:
            platform = self.router.detect_platform(test_file)
            self.assertEqual(platform, "android")
        finally:
            if os.path.exists(test_file):
                os.remove(test_file)

if __name__ == "__main__":
    unittest.main()

