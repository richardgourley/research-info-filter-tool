import unittest
import researchtool

class UnitTests(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.directory_name = 'test'
    
    '''
    File handler tests
    '''
    def test_make_directory_returns_true(self):
        file_handler = filehandler.FileHandler()
        can_open_file = file_handler.make_directory('test')
        expected = True
        self.assertEqual(can_open_file, expected, "Expected a successful opening of a file to return true.")

    def test_create_file_returns_true(self):
        file_handler = filehandler.FileHandler()
        # Expecting 'test' dir to exist
        can_create_file = file_handler.create_file('linux', self.directory_name)
        expected = True
        self.assertEqual(can_create_file, expected, "Expected a successful creation of a file.")

if __name__ == "__main__":
    unittest.main()