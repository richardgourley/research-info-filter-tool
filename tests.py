import unittest
import researchtool

class UnitTests(unittest.TestCase):
    def testCheckUrlHttp(self):
        researchTool = researchtool.ResearchTool([], 'flowers')
        actual = researchTool.checkUrl('http://www.testsite.com')
        expected = True
        self.assertEqual(actual, expected, "Expected 'http://www.testsite.com' to return True.")

    def testCheckUrlHttps(self):
        researchTool = researchtool.ResearchTool([], 'flowers')
        actual = researchTool.checkUrl('https://www.testsite.com')
        expected = True
        self.assertEqual(actual, expected, "Expected 'https://www.testsite.com' to return True.")

    def testCheckUrlShort(self):
        researchTool = researchtool.ResearchTool([], 'flowers')
        actual = researchTool.checkUrl('https://testsite.com')
        expected = True
        self.assertEqual(actual, expected, "Expected 'https://testsite.com' to return True.")

    def testCheckUrlInvalid(self):
        researchTool = researchtool.ResearchTool([], 'flowers')
        actual = researchTool.checkUrl('https://testsite.c.om')
        expected = False
        self.assertEqual(actual, expected, "Expected 'https://wwww.testsite.c.om' to return False.")

    def testCheckUrlPage(self):
        researchTool = researchtool.ResearchTool([], 'flowers')
        actual = researchTool.checkUrl('https://testsite.com/new_book')
        expected = True
        self.assertEqual(actual, expected, "Expected 'https://testsite.com/new_book' to return True.")


if __name__ == "__main__":
    unittest.main()