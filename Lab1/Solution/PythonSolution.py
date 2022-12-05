import cv2
import time
import numpy as np

from Solution.Solution import Solution

class PythonSolution(Solution):
    def __init__(self):
        super().__init__()
    def process(self, kernel):
        key = True
        n_frames = 0
        self.time = 0
        ret, frame = self.source_file.read()
        while(ret):
            if key:
                n_frames += 1
                start_time = time.time()
                frame = solution(frame, kernel)
                end_time = time.time() - start_time
                print(f"Frame: {n_frames}, time: {end_time}")
                self.time += end_time
            else:
                retval, frame = cv2.threshold(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
            if cv2.waitKey(119) == ord('w'):
                key = not key
            cv2.imshow(f"Result file (Python)", frame)
            ret, frame = self.source_file.read()
        self.source_file.release()
        cv2.destroyAllWindows()
        self.time /= n_frames
    
def solution(frame, kernel):
    y = kernel.shape[0] // 2
    x = kernel.shape[1] // 2
    processed_image = np.copy(frame)
    for chanel in range (frame.shape[2]):
        for i in range(y, frame.shape[0] - y):
            for j in range(x, frame.shape[1] - x):
                local_window = frame[i-y:i+y+1, j-x:j+x+1, chanel]
                max = 0
                for z in range(local_window.shape[0]):
                    for c in range(local_window.shape[1]):
                        if kernel[z][c] == 1:
                            if local_window[z][c] > max:
                                max = local_window[z][c]
                processed_image[i][j][chanel] = max
    return processed_image