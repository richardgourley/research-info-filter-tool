import unittest
from classes import filehandler
import os

class UnitTests(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.directory_name = 'test'
        self.file_handler = filehandler.FileHandler()
    '''
    File handler tests
    '''
    def test_make_directory_returns_true(self):
        can_open_file = self.file_handler.make_directory(self.directory_name)
        expected = True
        self.assertEqual(can_open_file, expected, "Expected a successful opening of a file to return true.")

    def test_create_file_returns_true(self):
        # Expecting 'test' dir to exist
        can_create_file = self.file_handler.create_file('linux', self.directory_name)
        expected = True
        self.assertEqual(can_create_file, expected, "Expected a successful creation of a file.")

    def test_open_file_append_returns_file_mode_a(self):
        file = self.file_handler.open_file_append('test/linux')
        mode = file.mode
        expected = "a"
        file.close()
        self.assertEqual(mode, expected, "Expected file to open successfully with mode 'a'.")

if __name__ == "__main__":
    unittest.main()