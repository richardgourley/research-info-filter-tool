import researchtool
import requests
import bs4

# ask user for a topic
topic = input("Hello. What is the name of the topic you would like to research?\n")

# create instance of ResearchTool
rt = researchtool.ResearchTool(topic)

# get file name, create file and then tell user where they can find results.
topicFileName = rt.createTopicTextFileName()
rt.createFile()
print("\nGreat! You can see your saved paragraphs in this file in the current folder when you have finished:\n", topicFileName, "\n")

# Open the topicFile where the user can save useful paragraphs.
topicFile = rt.openFile()

# Temp File that stores page content after each URL is entered, the user will save useful
# ...paragraphs to the topicFile above
tempFile = open("tempfile.txt", "wb")

enterUrls = True
# Keep asking user if they want to add another URL until they say 'N'
while enterUrls is True:
    print("===========================")
    url = input("\nEnter a valid url to search\n")

    if rt.checkUrl(url):        
        # If url is valid, save content to tempfile.txt
        try:
            res = requests.get(url)
            res.raise_for_status()
            for chunk in res.iter_content(100000):
                tempFile.write(chunk)
            tempFile.close()
        except:
            print("=====Sorry not a valid url, please try another====\n")
            continue
        
    else:
        print("=====Sorry not a valid url, please try another====\n")
        continue

    # Show the user all paragraphs from tempfile.txt
    tempFile = open("tempfile.txt")
    soup = bs4.BeautifulSoup(tempFile.read(), "html.parser")
    paras = soup.select('p')
    
    print("\n================================")
    print("HERE WE WILL SHOW YOU THE TEXT FROM EACH PARAGRAPH FROM THE URL")
    print("YOU CAN DECIDE IF YOU WANT TO SAVE IT FOR YOUR RESEARCH")
    print("================================")

    for para in paras:
        print("\n===================")
        print(para.getText())
        # Ask the user if this paragraph is useful- they can save it in topicFile
        useful = input("\nSave this paragraph to your research file? Y or N \n")
        if useful == "n" or useful == "N":
            continue
        else:
            print("==========================")
            paraText = para.getText()
            topicFile.write(paraText + "\n\n")

    # Delete content from tempFile.txt

    
    # Ask user if they have finished entering URLS
    print("\n==============================================================")
    print("============WE'VE REACHED THE END OF THAT URL================")
    print("==============================================================")
    
    another = input("\nEnter another url? Enter any key for YES or 'n' for NO\n")
    if another == 'N' or another == 'n':
        print("\n=======FINSIHED=========")
        print("\n===Thank you!======")
        print("\nYou can see all of your saved paragraphs for your research saved into the file:", topicFileName)
        break





