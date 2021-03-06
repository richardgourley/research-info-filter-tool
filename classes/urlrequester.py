import requests
import bs4

class UrlRequester():
    def __init__(self):
        pass

    '''
    Tries to open given url
    Retrieves content and saves to file given (append binary file)
    '''
    def retrieve_and_store_url_content(self, url, file):
        try:
            res = requests.get(url)
            res.raise_for_status()
            for chunk in res.iter_content(100000):
                file.write(chunk)
        except:
            print("NOTE! COULD NOT OPEN URL: " + url)

    def append_paragraphs(self, temp_file, topic_file):
        soup = bs4.BeautifulSoup(temp_file.read(), "html.parser")
        paragraphs = soup.select('p')
        for para in paragraphs:
            para_text = para.getText()
            topic_file.write(para_text + "\n\n")
        topic_file.write("=======END OF URL========\n")



   