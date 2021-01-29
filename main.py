from classes import filehandler
from classes import userinteraction
from classes import urlrequester


#### Class with methods to create directories, open files, write to files
file_handler = filehandler.FileHandler()

#### Class that utilizes 'requests' and 'Beautiful Soup' libraries
url_requester = urlrequester.UrlRequester()

#### Class that gets input from user - uses FileHandler and UrlRequester classes
user_interaction = userinteraction.UserInteraction(file_handler, url_requester)

### RUN THE PROGRAM ###
user_interaction.start()

quit()

