import time
import copy

from Solution.Solution import Solution

class PythonSolution(Solution):
    def __init__(self):
        super().__init__()
    def dilation(self, kernel):
        start_time = time.time()
        self.result_image = solution(self.source_image, kernel)
        self.time = time.time() - start_time
    def binariztion(image):
        print("Метод не реализован!")
    
def solution(source_image, kernel):
    y = kernel.shape[0] // 2
    x = kernel.shape[1] // 2
    processed_image = copy.deepcopy(source_image)
    for chanel in range (source_image.shape[2]):
        for i in range(y, source_image.shape[0] - y):
            for j in range(x, source_image.shape[1] - x):
                local_window = source_image[i-y:i+y+1, j-x:j+x+1, chanel]
                max = 0
                for z in range(local_window.shape[0]):
                    for c in range(local_window.shape[1]):
                        if kernel[z][c] == 1:
                            if local_window[z][c] > max:
                                max = local_window[z][c]
                processed_image[i][j][chanel] = max
    return processed_image