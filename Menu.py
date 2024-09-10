# Класс створення меню
class Menu:
    current_menu = 'MINE MENU'
    def __init__(self, menu_title, menu_list: list):
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
            print(" " * 47, index + 1, menu['item'])

        print()
        choice =  self.get_user_choice()
        self.go_to_menu(self.__menu_list[choice - 1])
        return self.current_menu

    def get_user_choice(self):
        while True:
            try:
                # Чекаємо ввод користувача
                choice = input(f'\n{" " * 40}Select menu item:\t')
                choice = int(choice)
                # Перевіряємо, що число знаходиться в допустимому діапазоні
                if 1 <= choice <= len(self.__menu_list):
                    return choice
                else:
                    print(f"Please enter a number between 1 and {len(self.__menu_list)}.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    def go_to_menu(self, choice_menu):
        # Перехід до іншого меню
        self.current_menu = choice_menu['menu_title']
        print(self.current_menu)
        print(f"Go to menu {self.current_menu}")


    @property
    def menu_list(self):
        return self.__menu_list

    @menu_list.setter
    def menu_list(self, menu_item):
        self.__menu_list.append(menu_item)

class SubMenu(Menu):
    def __init__(self, menu_title, menu_list: list):
        super().__init__(menu_title, menu_list)

