# Класс створення меню
class Menu:
    def __init__(self, menu_title: str, menu_list: list):
        self.__menu_title = menu_title
        self.__menu_list = menu_list

    # функція виводу Меню
    def display_menu(self):
        print()
        border = "*" * 40
        print(border.rjust(80, " "))

        print('*'.rjust(41, ' '), end="")
        print(self.__menu_title.center(37, ' '), '*')

        print(border.rjust(80, " "))
        print()

        for index, menu in enumerate(self.__menu_list):
            print(" " * 47, index + 1, menu)

        print()
        choice =  self.get_user_choice()
        self.change_menu(choice - 1)
        return self.__menu_list[choice - 1]
    def get_user_choice(self):
        while True:
            try:
                # Запрашиваем ввод пользователя
                choice = input(f'\n{" " * 40}Select menu item:\t')
                # Преобразуем ввод в целое число
                choice = int(choice)
                # Проверяем, что число находится в допустимом диапазоне
                if 1 <= choice <= len(self.__menu_list):
                    return choice
                else:
                    print(f"Please enter a number between 1 and {len(self.__menu_list)}.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    def change_menu(self, choice_menu):
        pass


    @property
    def menu_list(self):
        return self.__menu_list

    @menu_list.setter
    def menu_list(self, menu_item):
        self.__menu_list.append(menu_item)
