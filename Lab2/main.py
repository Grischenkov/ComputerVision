import cv2

from menu import Menu

from solution.match_template_solution import MatchTemplateSolution
from solution.sift_solution import SiftSolution

end_menu = None
start_menu = None
realisation_menu = None

def main():
    while start_menu.selection != "Выйти":
        solution = None
        end_menu.selection = None
        start_menu.selection = None
        realisation_menu.selection = None
        start_menu.show()
        if start_menu.selection == "Начало работы":
            realisation_menu.show()
            if realisation_menu.selection == "MatchTemplate":
                solution = MatchTemplateSolution()
            elif realisation_menu.selection == "Sift":
                solution = SiftSolution()
            solution.load_source_files()
            solution.process()
            while end_menu.selection != "Перезапустить":
                end_menu.show()
                if end_menu.selection == "Посмотреть результат":
                    solution.show_result(realisation_menu.selection)
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
                "Перезапустить", 
                "Выйти"])
    start_menu = Menu(
        name="Начало", 
        items=["Начало работы", 
                "Выйти"])
    realisation_menu = Menu(
        name="Реализация", 
        items=["MatchTemplate", 
                "Sift"])
    main()