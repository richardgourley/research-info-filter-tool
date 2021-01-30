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

    def create_file(self, topic_file_name, directory_name):
        try:
            os.chdir(directory_name)
            results_file = open(topic_file_name, "w")
            results_file.close()
            return True
        except:
            return None

    '''
    Opens topic file in append mode
    '''
    def open_file_append(self, file_name):
        return open(file_name, "a")

    def open_file_read(self, file_name):
        return open(file_name, "r")

    def open_file_write(self, file_name):
        return open(file_name, "w")

    '''
    Creates 'tempfile.txt' in append binary mode
    '''
    def create_temporary_file_append_binary(self):
        # must be append binary to work with UrlRequester class
        return open("tempfile.txt", "ab")

            
