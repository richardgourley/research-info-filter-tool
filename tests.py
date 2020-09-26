import unittest
import main

class UnitTests(unittest.TestCase):
    def test_enter_urls_exists(self):
        actual = main.enterUrls
        expected = True
        self.assertEqual(actual, expected, 'Expected True.')

if __name__ == "__main__":
    unittest.main()