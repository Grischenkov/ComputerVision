class Menu():
    def __init__(self, name, items):
        self.name = name
        self.items = items
        self.selection = None
    def show(self):
        print(f"{self.name}:")
        for item in enumerate(self.items):
            print(f"    {item[0] + 1}. {item[1]}")
        self.__get_selection()
    def __get_selection(self):
        self.selection = self.items[self.__get_input() - 1]
    def __get_input(self):
        while True:
            try:
                return int(input(f"Выбор: "))
            except:
                print(f"Некорректный ввод!")