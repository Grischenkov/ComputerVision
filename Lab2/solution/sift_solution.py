import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

from solution.solution import Solution

class SiftSolution(Solution):
    def __init__(self):
        super().__init__()
    def process(self):
        image = np.copy(self.source_image)
        template = np.copy(self.source_template)

        sift = cv2.SIFT_create()

        kp1, des1 = sift.detectAndCompute(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), None)
        kp2, des2 = sift.detectAndCompute(cv2.cvtColor(template, cv2.COLOR_BGR2GRAY), None)

        des1 = np.uint8(des1 * 255)
        des2 = np.uint8(des2 * 255)

        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        matches = bf.match(des1, des2)
        matches = sorted(matches, key=lambda x: x.distance)

        point_list = []
        for m in matches[:10]:
            point_list.append(m.queryIdx)
        c_list = cv2.KeyPoint_convert(kp1)
        needed_c_list = []
        for p in point_list:
            needed_c_list.append(c_list[p])

        df = pd.DataFrame(needed_c_list, columns=['x', 'y'])
        y_max, y_min = int(df.y.max()), int(df.y.min())
        x_max, x_min = int(df.x.max()), int(df.x.min())

        image = cv2.rectangle(image, (x_max, y_max), (x_min, y_min), color=(255, 55, 0), thickness=15)
        image = cv2.drawMatches(image, kp1, template, kp2, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

        f, ax = plt.subplots(1, 3, figsize=(50, 25))
        ax[0].imshow(cv2.cvtColor(self.source_image, cv2.COLOR_BGR2RGB))
        ax[0].set_title("Source"); plt.grid(None)
        ax[0].set_xticks([]); ax[0].set_yticks([])
        ax[1].imshow(cv2.cvtColor(self.source_template, cv2.COLOR_BGR2RGB))
        ax[1].set_title("Template"); plt.grid(None)
        ax[1].set_xticks([]); ax[1].set_yticks([])
        ax[2].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        ax[2].set_title(f"Result"); plt.grid(None)
        ax[2].set_xticks([]); ax[2].set_yticks([])

        canvas = FigureCanvas(f)
        canvas.draw()
        
        width, height = f.get_size_inches() * f.get_dpi()
        image = np.frombuffer(canvas.tostring_rgb(), dtype='uint8').reshape((int(height), int(width), 3))
        
        self.result_image = image