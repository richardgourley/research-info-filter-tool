import unittest
import main

class UnitTests(unittest.TestCase):
    def test_enter_urls_exists(self):
        actual = main.enterUrls
        expected = True
        self.assertEqual(actual, expected, 'Expected True.')

    def test_file_opened(self):
    	actual = main.tempFile
    	expected = True
    	self.assertEqual(actual, expected, 'Expected a tempfile.txt file to have been created')

if __name__ == "__main__":
    unittest.main()