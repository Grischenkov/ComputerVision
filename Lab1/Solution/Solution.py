import os
import cv2

class Solution():
    def __init__(self):
        self.__time = 0
        self.__path = ''
        self.__source_image = None
        self.__result_image = None

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
    def source_image(self):
        return self.__source_image
    @source_image.setter
    def source_image(self, image):
        self.__source_image = image

    @property
    def result_image(self):
        return self.__result_image
    @result_image.setter
    def result_image(self, image):
        self.__result_image = image

    def load_source_image(self):
        while True:
            try:
                self.path = input(f"Путь к файлу: ")
                if os.path.isfile(self.path):
                    self.source_image = cv2.imread(self.path)
                    return
                else:
                    print(f"Некорректный путь!")    
            except:
                print(f"Некорректный путь!")

    def show_source_image(self):
        cv2.imshow(f"Source image", self.source_image)
        cv2.waitKey(0)

    def show_result_image(self, algorithm, realisation):
        cv2.imshow(f"Result image ({algorithm}, {realisation})", self.result_image)
        cv2.waitKey(0)

    def save_result_image(self, algorithm, realisation):
        cv2.imwrite(f"{os.path.splitext(self.path)[0]}_{algorithm}_{realisation}{os.path.splitext(self.path)[1]}", self.result_image)

    def dilation(self, kernel):
        pass

    def binarization(self):
        pass