class Write2File:
    def __init__(self, log_file_name: str = 'log.txt'):
        self.__log_file_name = log_file_name
        self.__clean_log_file()

    def write(self, new_data: str):
        with open(self.__log_file_name, 'a') as log_file:
            log_file.write(new_data)

    def __clean_log_file(self):
        with open(self.__log_file_name, 'w') as log_file:
            log_file.write(str())
