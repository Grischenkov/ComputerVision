import cv2
import time

from Solution.Solution import Solution

class OpenCVSolution(Solution):
    def __init__(self):
        super().__init__()
    def dilation(self, kernel):
        start_time = time.time()
        self.result_image = cv2.dilate(self.source_image, kernel)
        self.time = time.time() - start_time
    def binarization(self):
        start_time = time.time()
        retval, self.result_image = cv2.threshold(cv2.cvtColor(self.source_image, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
        self.time = time.time() - start_time