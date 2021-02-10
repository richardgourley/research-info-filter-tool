import os

class FileHandler():
    def __init__(self):
        pass

    def make_directory(self, directory_name):
        if not os.path.exists(directory_name):
            try:
                os.mkdir(directory_name)
                return True
            except:
                return None
        return True

    def create_file_in_directory(self, topic_file_name, directory_name):
        try:
            os.chdir(directory_name)
            results_file = open(topic_file_name, "w")
            results_file.close()
            return True
        except:
            return None

            
