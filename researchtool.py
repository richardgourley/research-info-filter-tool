import re
import requests
import os

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
        try:
            topicTextFileName = self.createTopicTextFileName()
            topicFile = open(topicTextFileName, "w")
            topicFile.close()
            return "We have created a file called '{}' to store your paragraphs in.".format(topicTextFileName) 
        except:
            return "Sorry there was a problem."
            






# get information from the user
# create an instance of the class - with user information


'''
researchTopic = input("Hello. Enter the name of your research topic:\n")
print("TOPIC NAME: ", researchTopic)

urls = []
enterUrls = True
tempFile = open("tempfile.txt" ,"wb")


while enterUrls is True:
    url = input("Enter a valid url to search\n")

    try:
        res = requests.get(url)
            res.raise_for_status()
        for chunk in res.iter_content(100000):
            tempFile.write(chunk)
        urls.append(url)
    except:
        print("=====Sorry not a valid url, please try another====\n")
        continue

    another = input("Enter another url? Enter Y or N\n")
    if another == 'N':
        break

print("\nHere are the urls you have decided to search:")
for u in urls:
    print(u)'''
