'''
This class interacts with the user, providing messages
The class takes an instance of FileHandler and UrlRequester classes
The class methods either a) interract with user, or b) open urls, retrieve info and add to files
'''
class UserInteraction:
    def __init__(self, file_handler, url_requester):
        self.file_handler = file_handler
        self.url_requester = url_requester
        
    def start(self):
        self.ask_user_for_topic()
        self.create_topic_file_name()
        self.ask_user_for_directory()
        self.create_directory_and_file()
        self.inform_user_results_location()
        self.ask_user_for_urls()
        self.visit_urls_save_paragraphs()

    '''
    Checks topic name entered is not blank
    Saves topic name input to self.topic_name
    '''
    def ask_user_for_topic(self):
        no_topic_name = True
        while no_topic_name:
            print("Hello. What is the name of the topic you would like to research?")
            topic = input()
            if topic == "":
                print("Topic name must not be blank")
                continue
            self.topic_name = topic
            no_topic_name = False

    def create_topic_file_name(self):
        topic_file_name = str(self.topic_name.replace(" ","_")) + ".txt"
        self.topic_file_name = topic_file_name

    '''
    Asks user for a directory to save results in  
    '''
    def ask_user_for_directory(self):
        no_results_directory = True
        while no_results_directory:
            print("What is the name of the directory you would like to save your results?")
            directory_name = input()
            if directory_name == "":
                print("Directory name must not be blank")
                continue
            self.directory_name = directory_name
            no_results_directory = False

    def create_directory_and_file(self):
        directory = self.file_handler.make_directory(self.directory_name)
        file = self.file_handler.create_file(self.topic_file_name, self.directory_name)
        if directory and file:
            pass
        else:
            print("Sorry, there was an error creating the directory and/ or file.  Please try again.")
            quit()

    def inform_user_results_location(self):
        print("Saved paragraphs from the urls you enter below will be saved to:")
        print("DIRECTORY: " + self.directory_name)
        print("FILE NAME: " + self.topic_file_name)

    '''
    Keep asking for urls until user says 'N'
    Store urls in self.urls as a list
    '''
    def ask_user_for_urls(self):
        self.urls = []
        print("Now we will ask you for some urls to search")
        still_entering_urls = True
        while still_entering_urls:
            print("Enter a valid url")
            url = input()
            if url == "":
                print("Sorry, url can't be blank.")
                continue
            self.urls.append(url)
            print("Enter another url? Enter 'Y' or 'N':")
            enter_another = input()
            if enter_another == 'N' or enter_another == 'n':
                still_entering_urls = False

    '''
    FileHandler creates a temporary (append binary) file and opens topic file
    FOR each URl, UrlRequester opens and saves text to temp file
    UrlRequester uses Beautiful Soup to retrieve paragraphs from temp file ....
    .... and appends paragraphs to topic_file
    Finally, open up temp file in write mode to leave 'textfile.txt' blank for the next time program runs
    '''
    def visit_urls_save_paragraphs(self):
        temp_file = self.file_handler.create_temporary_file_append_binary() # 'textfile.txt' created
        topic_file = self.file_handler.open_file_append(self.topic_file_name)
        for url in self.urls:
            self.url_requester.get_store_url_content(url, temp_file)
        temp_file = self.file_handler.open_file_read("tempfile.txt")
        self.url_requester.append_paragraphs(temp_file, topic_file)
        temp_file = self.file_handler.open_file_write("tempfile.txt") # re-open 'textfile.txt' in 'w' mode - leaves blank file
        






