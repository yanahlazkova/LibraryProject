from librarian import Librarian
from library import Library
from book import Book

title_menu = 'MAIN MENU'
current_librarian = ''

def display_menu():
    # Display MAINE MENU
    border = "*" * 40
    menu_title = title_menu
    menu_items = [
        'EXIT',
        'Select librarians',
        'List books',
        'Add book',
        'Delete book',
        'Find book',
    ]
    print(border.rjust(80, " "))

    print('*'.rjust(41, ' '), end="")
    print(menu_title.center(37, ' '), '*')

    print(border.rjust(80, " "))
    print()

    for index, menu in enumerate(menu_items):
        print(" " * 47, index + 1, menu)
    print()
    print('Select menu item: '.rjust(60, ' '), end='')
    choice = int(input())
    return choice


def select_librarians(list_librarians):
    display_list_librarians(list_librarians)
    while True:
        try:
            print()
            print(' ' * 45, end="")
            choice = input('Select the librarians: ')
            choice = int(choice)
            if 1 <= choice <= len(list_librarians):
                print(list_librarians[choice - 1])
                return choice - 1
            elif choice == len(list_librarians) + 1:
                break
            else:
                print()
                print(' ' * 45, end="")
                print(f"Please enter a number between 1 and {len(list_librarians) + 1}")
        except ValueError:
            print("Invalid input. Please enter a number.")


def display_list_librarians(list_libr):
    # Display list librarians
    print('\n\n', ' ' * 45, 'LIST LIBRARIANS:\n')

    for index, librarian in enumerate(list_libr):
        print(' ' * 45, index + 1, librarian.librarian)
    print(' ' * 45, len(list_libr) + 1, 'EXIT')
    print('\n', ' ' * 45, end="")




book1 = Book("Book1", "Author1", 101, 2001)
book2 = Book("Book2", "Author2", 102, 2002)
book3 = Book("Book3", "Author3", 103, 2003)

book_list1 = [book1, book2]
book_list2 = [book1, book3]
library1 = Library("Library children", book_list1)
library2 = Library("Library adult", book_list2)

librarian1 = Librarian('Deny-1', library1)
librarian2 = Librarian('Meny-2', library2)
list_librarians = [librarian1, librarian2]


while True:
    choice_item = display_menu()
    match choice_item:
        case 1: break
        case 2:
            choice = select_librarians(list_librarians)
            current_librarian = list_librarians[choice]
            title_menu = f'{current_librarian.librarian}, library "{current_librarian.library.library_name}"'

        case 3:
            print('current_librarian = ', current_librarian)
            if not current_librarian:
                print()
                print(' ' * 45, end="")
                print('Librarian not selected\n')
                input('Press any key')
            else:
                print('current_librarian', current_librarian.librarian)
                print(current_librarian.library)


