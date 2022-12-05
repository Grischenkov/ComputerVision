import cv2
import time

from solution.solution import Solution

class OpenCVSolution(Solution):
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
                self.time += end_time
            else:
                retval, frame = cv2.threshold(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
            if cv2.waitKey(119) == ord('w'):
                key = not key
            cv2.imshow(f"Result file (OpenCV)", frame)
            ret, frame = self.source_file.read()
        self.source_file.release()
        cv2.destroyAllWindows()
        self.time /= n_frames

def solution(frame, kernel):
    frame = cv2.dilate(frame, kernel)
    return frame