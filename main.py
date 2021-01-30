from classes.filehandler import FileHandler
from classes.userinteraction import UserInteraction
from classes.urlrequester import UrlRequester

#### Class with methods to create directories, open files, write to files
file_handler = FileHandler()

#### Class that utilizes 'requests' and 'Beautiful Soup' libraries
url_requester = UrlRequester()

#### Class that gets input from user - uses FileHandler and UrlRequester classes
user_interaction = UserInteraction(file_handler, url_requester)

### RUN THE PROGRAM ###
user_interaction.start()

quit()

