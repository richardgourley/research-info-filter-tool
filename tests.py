import unittest
from classes import filehandler
from classes import urlrequester
from classes import userinteraction
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
    def test_retrieve_and_store_url_content_valid_url(self):
        valid_url = "https://www.linuxmint.com/"
        # Must be 'write binary' for writing url request results
        temp_file = open("tempfile.txt", "wb")
        can_open_urls = self.url_requester.retrieve_and_store_url_content(valid_url, temp_file)
        expected = True
        temp_file.close()
        os.unlink('tempfile.txt')
        self.assertEqual(can_open_urls, expected, "Expecting 'True' for opening and storing content from a url.")

    def test_retrieve_and_store_url_content_invalid_url(self):
        invalid_url = "Hello, World!"
        # Must be 'write binary' for writing url request results
        temp_file = open("tempfile.txt", "wb")
        can_open_urls = self.url_requester.retrieve_and_store_url_content(invalid_url, temp_file)
        expected = False
        temp_file.close()
        os.unlink("tempfile.txt")
        self.assertEqual(can_open_urls, expected, "Expecting 'False' for opening an invalid url.")
    
        '''
    UserInteraction Tests
    '''
    def test_class_methods_in_user_interaction(self):
        class_methods = dir(self.user_interaction)
        list_expected_methods = [
            'ask_user_for_directory',
            'ask_user_for_topic',
            'ask_user_for_urls',
            'create_directory_and_file',
            'create_topic_file_name',
            'inform_user_results_location',
            'start',
            'visit_urls_save_paragraphs'
        ]
        for method in list_expected_methods:
            self.assertEqual((method in class_methods), True, "Expecting " + method + " to be in class methods.")

    '''
    Tear Down at the end of the tests
    '''

    def tearDown(self):
        path = os.path.join(os.getcwd(), self.directory_name)

        # remove 'self.directory_name' dir at the end of tests
        if os.path.exists(path):
            shutil.rmtree(path)

if __name__ == "__main__":
    unittest.main()