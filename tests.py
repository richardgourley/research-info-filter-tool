import unittest
from classes import filehandler
from classes import urlrequester
import shutil
import os

class UnitTests(unittest.TestCase):
    @classmethod
    def setUp(self):
        # Start directory - used in methods to return to start directory after each test 
        self.start_directory = os.getcwd()
        self.directory_name = 'test'
        self.file_handler = filehandler.FileHandler()
        self.url_requester = urlrequester.UrlRequester()

    '''
    File handler tests
    '''
    def test_make_directory_returns_true(self):
        can_open_file = self.file_handler.make_directory(self.directory_name)
        expected = True
        os.chdir(self.start_directory)
        self.assertEqual(can_open_file, expected, "Expected a successful opening of a file to return true.")

    def test_create_file_returns_true(self):
        self.file_handler.make_directory(self.directory_name)
        can_create_file = self.file_handler.create_file_in_directory('linux', self.directory_name)
        expected = True
        os.chdir(self.start_directory)
        self.assertEqual(can_create_file, expected, "Expected a successful creation of a file.")

    '''
    UrlRequester Tests
    '''
    def test_retrieve_and_store_url_content(self):
        valid_url = "linuxmint.com"
        temp_file = open("tempfile.txt", "wb")
        can_open_urls = self.url_requester.retrieve_and_store_url_content(valid_url, temp_file)
        expected = True
        os.unlink('tempfile.txt')
        self.assertEqual(can_open_urls, expected, "Expecting 'True' for opening and storing content from a url.")
    
    '''
    Tear Down at the end of the tests
    '''

    def tearDown(self):
        path = os.path.join(os.getcwd(), self.directory_name)

        # remove 'self.directory_name' dir at the end of tests
        if os.path.exists(path):
            shutil.rmtree(path)

if __name__ == "__main__":
    unittest.main()import unittest
