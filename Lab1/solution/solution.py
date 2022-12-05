import os
import cv2

class Solution():
    def __init__(self):
        self.__time = 0
        self.__path = ''
        self.__source_file = None

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time):
        self.__time = time
    
    @property
    def path(self):
        return self.__path
    @path.setter
    def path(self, path):
        self.__path = path

    @property
    def source_file(self):
        return self.__source_file
    @source_file.setter
    def source_file(self, file):
        self.__source_file = file

    def load_source_file(self):
        while True:
            try:
                self.path = input(f"Путь к файлу: ")
                if os.path.isfile(self.path):
                    self.source_file = cv2.VideoCapture(self.path)
                    return
                else:
                    print(f"Некорректный путь!")    
            except:
                print(f"Некорректный путь!")

    def process(self, kernel):
        pass