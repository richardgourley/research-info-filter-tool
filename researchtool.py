import re

class ResearchTool():
    def __init__(self, topicName):
        self.topicName = topicName

    def checkUrl(self, url):
        testUrlRegex = re.compile(r'(https|http)://(www\.)?\w+\.[a-z]{2,}/*.*')
        mo = testUrlRegex.search(url)

        if not mo is None:
            return True

        return False

    def createTopicTextFileName(self):
        # replaces space with underscores for saving a file with topic name
        topicTextFileName = str(self.topicName.replace(" ", "_")) + ".txt"
        return topicTextFileName

    def createFile(self):
        topicFile = open(self.createTopicTextFileName())