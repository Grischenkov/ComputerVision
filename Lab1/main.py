import cv2

from Menu import Menu

from Solution.NumbaSolution import NumbaSolution
from Solution.OpenCVSolution import OpenCVSolution
from Solution.PythonSolution import PythonSolution

end_menu = None
start_menu = None
algorithm_menu = None
realisation_menu = None

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

def main():
    while start_menu.selection != "Выйти":
        solution = None
        end_menu.selection = None
        start_menu.selection = None
        algorithm_menu.selection = None
        realisation_menu.selection = None
        start_menu.show()
        if start_menu.selection == "Начало работы":
            algorithm_menu.show()
            if algorithm_menu.selection == "Dilation":
                realisation_menu.show()
                if realisation_menu.selection == "OpenCV":
                    solution = OpenCVSolution()
                elif realisation_menu.selection == "Python":
                    solution = PythonSolution()
                elif realisation_menu.selection == "Numba":
                    solution = NumbaSolution()
                solution.load_source_image()
                solution.dilation(kernel)
            elif algorithm_menu.selection == "Binarization":
                realisation_menu.selection = "OpenCV"
                solution = OpenCVSolution()
                solution.load_source_image()
                solution.binarization()
            print(f"Для алгоритма: {algorithm_menu.selection}\n Реализованного с помощью: {realisation_menu.selection}\n Время выполнения составило {solution.time} с.")
            while end_menu.selection != "Перезапустить":
                end_menu.show()
                if end_menu.selection == "Посмотреть исходный файл":
                    solution.show_source_image()
                elif end_menu.selection == "Посмотреть результат":
                    solution.show_result_image(algorithm_menu.selection, realisation_menu.selection)
                elif end_menu.selection == "Сохранить результат":
                    solution.save_result_image(algorithm_menu.selection, realisation_menu.selection)
                elif end_menu.selection == "Перезапустить":
                    pass
                elif end_menu.selection == "Выйти":
                    return
        elif start_menu.selection == "Выйти":
            return

if __name__ == "__main__":
    end_menu = Menu(
        name="Конец", 
        items=["Посмотреть исходный файл", 
                "Посмотреть результат", 
                "Сохранить результат", 
                "Перезапустить", 
                "Выйти"])
    start_menu = Menu(
        name="Начало", 
        items=["Начало работы", 
                "Выйти"])
    algorithm_menu = Menu(
        name="Алгоритм", 
        items=["Dilation", 
                "Binarization"])
    realisation_menu = Menu(
        name="Реализация", 
        items=["OpenCV", 
                "Python", 
                "Numba"])
    main()