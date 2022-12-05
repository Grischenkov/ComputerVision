import cv2

from menu import Menu

from solution.numba_solution import NumbaSolution
from solution.open_cv_solution import OpenCVSolution
from solution.python_solution import PythonSolution

end_menu = None
start_menu = None
realisation_menu = None

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

def main():
    while start_menu.selection != "Выйти":
        solution = None
        end_menu.selection = None
        start_menu.selection = None
        realisation_menu.selection = None
        start_menu.show()
        if start_menu.selection == "Начало работы":
            realisation_menu.show()
            if realisation_menu.selection == "OpenCV":
                solution = OpenCVSolution()
            elif realisation_menu.selection == "Python":
                solution = PythonSolution()
            elif realisation_menu.selection == "Numba":
                solution = NumbaSolution()
            solution.load_source_file()
            solution.process(kernel)
            print(f"Для алгоритма, реализованного с помощью: {realisation_menu.selection}\n Среднее время обработки кадра составило {solution.time} с.")
            while end_menu.selection != "Перезапустить":
                end_menu.show()
                if end_menu.selection == "Перезапустить":
                    pass
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
        items=["OpenCV", 
                "Python", 
                "Numba"])
    main()