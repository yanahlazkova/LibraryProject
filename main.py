from book import Book
from menu import *

# Create MENU BOOKS
menu_books_items = [
    'Add',
    'Delete',
    'Find a book (title)',
    'Fine a book (author)',
    'List books',
    'Back to MAIN MENU'
]
menu_books = SubMenu('MENU BOOKS', menu_books_items)

# Create MENU LIBRARIES
menu_libraries_items = [
    'List libraries',
    'Add library',
    'Delete library',
    'Find library',
    'Back to MAIN MENU'
]

menu_libraries = SubMenu('MENU LIBRARY', menu_libraries_items)

# Create MENU LIBRARIES
# В меню бібліотекарів можна додати бібліотекаря, видалити, знайти, обрати бібліотекаря,
# та при виборі бібліотекаря додати книгу в бібліотеку, видалити, знайти, вивести список книг
menu_librarians_items = [
    'Add librarians',
    'Delete librarians',
    'List librarians',
    'Add book in library',
    'Delete book in library',
    'List books in library',
    'Find book',
    'List books'
]

menu_librarians = SubMenu('MENU LIBRARIANS', menu_librarians_items)

# Create MINE MENU
menu_mine_items = [
    {'item': 'Books', 'menu': menu_books},
    {'item': 'Libraries', 'menu': menu_libraries},
    # {'item': 'Library (adult)', 'menu': menu_},
    {'item': 'Librarians', 'menu': menu_librarians},
    {'item': 'EXIT', 'menu': 'EXIT'}
]
mine_menu = Menu('MINE MENU', menu_mine_items)


def main_menu():
    while True:
        mine_menu.display_menu()
        choice_menu = mine_menu.get_user_choice()
        if 1 <= choice_menu <= len(menu_mine_items) - 1:
            print(f'Your choice: {menu_mine_items[choice_menu - 1]['item']}')
            input('Press any key to continue ')
            return menu_mine_items[choice_menu - 1]['menu']

        elif choice_menu == len(menu_mine_items):
            print('EXIT')
            exit()


def submenu_books():
    while True:
        choice_item = menu_books.display_menu()
        match choice_item:
            case 'Add':
                add_book()
            case 'Delete':
                delete_book()
            case 'Find a book (title)':
                print('Choice item ', choice_item)
            case 'Fine a book (author)':
                print('Choice item ', choice_item)
            case 'List books':
                print('Choice item ', choice_item)
            case 'Back to MAIN MENU': break


# Вивести головне меню
choice_menu = main_menu()

print(choice_menu.menu_title)

# Вивести підменю
choice_menu.display_menu()

