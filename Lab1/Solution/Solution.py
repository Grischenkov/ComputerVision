import os
import cv2

class Solution():
    def __init__(self):
        self.time = 0
        self.path = ''
        self.result_image = None
        self.source_image = self._load_image()
    def _load_image(self):
        while True:
            try:
                file_path = input(f"Путь к файлу: ")
                self.source_image = cv2.imread(file_path)
                self.path = file_path
                return
            except:
                print(f"Некорректный путь!")
    def show_source(self):
        cv2.imshow(f"Source image", self.source_image)
        cv2.waitKey(0)
    def show_result(self, algorithm, realisation):
        cv2.imshow(f"Result image ({algorithm}, {realisation})", self.result_image)
        cv2.waitKey(0)
    def save_result(self, algorithm, realisation):
        cv2.imwrite(f"{os.path.splitext(self.path)[0]}_{algorithm}_{realisation}{os.path.splitext(self.path)[1]}", self.result_image)
    def dilatation(self, kernel):
        pass
    def binarization(self):
        pass