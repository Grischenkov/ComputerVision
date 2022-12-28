import cv2
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

from solution.solution import Solution

class MatchTemplateSolution(Solution):
    def __init__(self):
        super().__init__()
    def process(self):
        image = np.copy(self.source_image)
        template = np.copy(self.source_template)

        h, w, ch = template.shape

        result = cv2.matchTemplate(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), cv2.cvtColor(template, cv2.COLOR_BGR2GRAY), cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        bottom_right = (max_loc[0] + w, max_loc[1] + h)
        
        cv2.rectangle(image, max_loc, bottom_right, 255, 2)

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