import unittest
import main

class UnitTests(unittest.TestCase):
    def testDisplayWebsiteList(self):
        researchTool = researchtool.ResearchTool(['1234', '4567'], 'flowers')
        actual = researchTool.displayWebsiteList()
        expected = "1234\n4567\n"
        self.assertEqual(actual, expected, "Expected '1234\n4567\n' returned as a string.")
    
if __name__ == "__main__":
    unittest.main()