import gc
import tensorflow as tf

from menu import Menu

from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.applications.vgg19 import VGG19
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.efficientnet import EfficientNetB0

from solution.solution import Solution

end_menu = None
start_menu = None
realisation_menu = None

def main():
    while start_menu.selection != "Выйти":
        gc.collect()
        tf.keras.backend.clear_session()
        
        solution = None
        end_menu.selection = None
        start_menu.selection = None
        realisation_menu.selection = None
        start_menu.show()
        if start_menu.selection == "Начало работы":
            realisation_menu.show()
            if realisation_menu.selection == "VGG16":
                solution = Solution(224, 224, VGG16(weights='imagenet'))
            elif realisation_menu.selection == "VGG19":
                solution = Solution(224, 224, VGG19(weights='imagenet'))
            elif realisation_menu.selection == "ResNet-50":
                solution = Solution(224, 224, ResNet50(weights='imagenet'))
            elif realisation_menu.selection == "EfficientNet_B0":
                solution = Solution(224, 224, EfficientNetB0(weights='imagenet'))
            solution.load_source_files()
            solution.process()
            print(f"Для модели {realisation_menu.selection}: \n{solution.describe()}")
            while end_menu.selection != "Перезапустить":
                end_menu.show()
                if end_menu.selection == "Перезапустить":
                    del solution
                elif end_menu.selection == "Выйти":
                    return
        elif start_menu.selection == "Выйти":
            return

if __name__ == "__main__":
    end_menu = Menu(
        name="Конец", 
        items=["Перезапустить", 
                "Выйти"])
    start_menu = Menu(
        name="Начало", 
        items=["Начало работы", 
                "Выйти"])
    realisation_menu = Menu(
        name="Реализация", 
        items=["VGG16", 
                "VGG19",
                "ResNet-50",
                "EfficientNet_B0"])
    main()