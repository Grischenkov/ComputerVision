import os
import cv2
import matplotlib.pyplot as plt

class Solution():
    def __init__(self):
        self.__result_image = None
        self.__source_image = None
        self.__source_image_path = ''
        self.__source_template = None
        self.__source_template_path = ''

    @property
    def result_image(self):
        return self.__result_image
    @result_image.setter
    def result_image(self, file):
        self.__result_image = file

    @property
    def source_image_path(self):
        return self.__source_image_path
    @source_image_path.setter
    def source_image_path(self, path):
        self.__source_image_path = path
    @property
    def source_image(self):
        return self.__source_image
    @source_image.setter
    def source_image(self, file):
        self.__source_image = file

    @property
    def source_template_path(self):
        return self.__source_template_path
    @source_template_path.setter
    def source_template_path(self, path):
        self.__source_template_path = path
    @property
    def source_template(self):
        return self.__source_template
    @source_template.setter
    def source_template(self, file):
        self.__source_template = file

    def load_source_files(self):
        while True:
            try:
                self.source_image_path = input(f"Путь к исходному изображению: ")
                if os.path.isfile(self.source_image_path):
                    self.source_image = cv2.imread(self.source_image_path)
                    self.source_template_path = input(f"Путь к шаблону: ")
                    if os.path.isfile(self.source_template_path):
                        self.source_template = cv2.imread(self.source_template_path)
                        return
                    else:
                        print(f"Некорректный путь!")    
                else:
                    print(f"Некорректный путь!")
            except:
                print(f"Некорректный путь!")

    def show_result(self, algorithm):
        f, ax = plt.subplots()
        ax.imshow(self.result_image)
        ax.set_title(f"{algorithm}"); plt.grid(None)
        ax.set_xticks([]); ax.set_yticks([])
        f.show()

    def process(self):
        pass