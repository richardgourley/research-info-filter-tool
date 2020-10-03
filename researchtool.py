import re
import os

class ResearchTool():
    def __init__(self, topicName):
        self.topicName = topicName

    def checkUrl(self, url):
        testUrlRegex = re.compile(r'(https|http)://(www\.)?(\w+\.[a-z]{2,}/*.*)')
        mo = testUrlRegex.search(url)

        if not mo is None:
            return True

        return False

    def createTopicTextFileName(self):
        # replaces space with underscores for saving a file with topic name
        topicTextFileName = str(self.topicName.replace(" ", "_")) + ".txt"
        return topicTextFileName

    def createFile(self):
        try:
            topicTextFileName = self.createTopicTextFileName()
            topicFile = open(topicTextFileName, "w")
            topicFile.close()
            return "We have created a file called '{}' to store your paragraphs in.".format(topicTextFileName) 
        except:
            return "Sorry there was a problem."

    def openFile(self):
        return open(self.createTopicTextFileName(), "a")

    # Clear the screen for the user before the next quesiton
    def screen_clear(self):
        if os.name == "posix":
            _ = os.system('clear')
        else:
            _ = os.system('cls')
            
