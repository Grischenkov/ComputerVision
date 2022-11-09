from Menu import Menu

from Solution.NumbaSolution import NumbaSolution
from Solution.OpenCVSolution import OpenCVSolution
from Solution.PythonSolution import PythonSolution

kernel = None
end_menu = None
start_menu = None
algorithm_menu = None
realisation_menu = None

def main():
    while start_menu.selection != "Выйти":
        solution = None
        start_menu.show()
        if start_menu.selection == "Загрузить изображение":
            algorithm_menu.show()
            if algorithm_menu.selection == "Дилатация":
                realisation_menu.show()
                if realisation_menu.selection == "OpenCV":
                    solution = OpenCVSolution()
                elif realisation_menu.selection == "Python":
                    solution = PythonSolution()
                elif realisation_menu.selection == "Numba":
                    solution = NumbaSolution()
                solution.dilatation(kernel)
            elif algorithm_menu.selection == "Бинаризация":
                realisation_menu.selection = "OpenCV"
                solution = OpenCVSolution()
                solution.binarization()
            print(f"Для алгоритма: {algorithm_menu.selection}\n Реализованного с помощью: {realisation_menu.selection}\n Время выполнения составило {solution.time} с.")
            while end_menu.selection != "Перезапустить":
                end_menu.show()
                if end_menu.selection == "Посмотреть результат":
                    solution.show_result()
                elif end_menu.selection == "Сохранить результат":
                    solution.save_result()
                elif end_menu.selection == "Перезапустить":
                    pass
                elif end_menu.selection == "Выйти":
                    return
        elif start_menu.selection == "Выйти":
            return

if __name__ == "__main__":
    end_menu = Menu(
        name="Конец", 
        items=["Посмотреть результат", 
                "Сохранить результат", 
                "Перезапустить", 
                "Выйти"])
    start_menu = Menu(
        name="Начало", 
        items=["Загрузить изображение", 
                "Выйти"])
    algorithm_menu = Menu(
        name="Алгоритм", 
        items=["Дилатация", 
                "Бинаризация"])
    realisation_menu = Menu(
        name="Реализация", 
        items=["OpenCV", 
                "Python", 
                "Numba"])
    main()