import unittest
from archives import Archive
import os

class TestArchiveTasks(unittest.TestCase):

    def setUp(self):
        self.test_directory_path = os.path.join(os.getcwd(), 'archives_test')
        assert type(self.test_directory_path) == str
        self.default_directory_archive = Archive()
        self.custom_directory_archive = Archive(path=self.test_directory_path)
        self.zip_archive = Archive(path='archive_test_zip.zip')


    def test_set_format(self):
        self.default_directory_archive.set_format('zip')
        self.assertEqual(self.default_directory_archive.format, 'zip')

    def test_load_directory_default(self):
        self.assertEqual(self.default_directory_archive.input_type, 'directory')
    
    def test_load_directory_custom(self):
        self.assertEqual(self.custom_directory_archive.path, self.test_directory_path)
    
    def test_load_zipfile(self):
        self.assertEqual(self.zip_archive.input_type, 'zip')

    def test_scan_directory(self):
        self.assertIsNotNone(self.custom_directory_archive.scan())

    def test_scan_zipfile(self):
        self.assertIsNotNone(self.zip_archive.scan())

    def make_zip_from_directory(self):
        pass

if __name__ == "__main__":
    unittest.main()