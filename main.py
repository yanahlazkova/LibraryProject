from book import Book
from menu import Menu
from helpers import *

# Display list librarians

# Create MINE MENU
menu_mine_items = [
    {'item': 'Books', 'menu_title': 'MENU BOOKS'},
    {'item': 'Library (children)', 'menu_title': 'MENU LIBRARY'},
    {'item': 'Library (adult)', 'menu_title': 'MENU LIBRARY'},
    {'item': 'Librarians', 'menu_title': 'MENU LIBRARIAN'},
    {'item': 'EXIT', 'menu_title': 'EXIT'}
]
mine_menu = Menu('MINE MENU', menu_mine_items)

# Create MENU BOOKS
menu_books_items = [
    'Add',
    'Delete',
    'Find a book (title)',
    'Fine a book (author)',
    'List books',
    'Back to MAIN MENU'
]
menu_books = Menu('MENU BOOKS', menu_books_items)

# Create MENU LIBRARIES
menu_libraries_items = [
    'Add book',
    'Delete book',
    'Find library',
    'List libraries',
    'List book in library',
    'Back to MAIN MENU'
]

menu_libraries = Menu('MENU LIBRARY', menu_libraries_items)

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

menu_librarians = Menu('MENU LIBRARIANS', menu_librarians_items)

def main_menu():
    while True:
        choice_menu = mine_menu.display_menu()
        match choice_menu:
            case 'MENU BOOKS':
                print(f'Choice {choice_menu}')
                # choice_menu = menu_books.display_sub_menu()
                sub_menu_books()
            case 'MENU LIBRARY':
                print(choice_menu)

                print(f'Choice {choice_menu}')
                choice_menu = menu_libraries.display_sub_menu()
            case 'EXIT': break


def sub_menu_books():
    while True:
        choice_item = menu_books.display_sub_menu()
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

# Display Mine Menu
main_menu()
