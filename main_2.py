from librarian import Librarian
from library import Library
from book import Book
import os, json

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
        'Change book name',
        'Find book',
        'Save to file'
    ]
    print()
    print(border.rjust(80, " "))

    print('*'.rjust(41, ' '), end="")
    print(menu_title.center(37, ' '), '*')

    print(border.rjust(80, " "))
    print()

    for index, menu in enumerate(menu_items):
        print(" " * 47, index + 1, menu)
    print()
    print('Select menu item: '.rjust(60, ' '), end='')
    try:
        # Чекаємо ввод користувача
        choice = int(input())
        # Перевіряємо, що число знаходиться в допустимому діапазоні
        if 1 <= choice <= len(menu_items):
            return choice
        else:
            indent()
            print(f"Please enter a number between 1 and {len(menu_items)}.")

    except ValueError:
        indent()
        print("Invalid input. Please enter a number.")


def display_message():
    print()
    print(' ' * 30, end="")
    print('Librarian not selected. Select librarians in menu item - "2"\n')
    print(' ' * 45, end="")
    input('Press any key')

def select_librarians(list_librarians):
    display_list_librarians(list_librarians)
    while True:
        try:
            print()
            print(' ' * 45, end="")
            choice = input('Select the librarians: ')
            choice = int(choice)
            if 1 <= choice <= len(list_librarians):
                global current_librarian
                global title_menu
                current_librarian = list_librarians[choice - 1]
                title_menu = f'{current_librarian.librarian}, library: "{current_librarian.library.library_name}"'
                print()
                print(' ' * 35, 'Your choice:')
                print(list_librarians[choice - 1])
                print(' ' * 35, 'Press any key', end='')
                input()
                return
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

def indent():
    # Робить відступ від краю
    print()
    print(' ' * 45, end='')

def add_book():
    indent()
    book_title = input('Enter book title: ')
    indent()
    author = input('Enter author: ')
    indent()
    page_count = int(input('Enter page count: '))
    indent()
    publication_year = int(input("Enter year of publication: "))
    indent()
    new_book = Book(book_title, author, page_count, publication_year)
    current_librarian.library.add_book(new_book)
    print(f'List books of librarian {current_librarian.librarian} {current_librarian.library}')
    indent()
    input("Press any key")

def delete_book():
    print(current_librarian.library)
    indent()
    book_title = input('Enter book title: ')
    current_librarian.library.delete_book(book_title)
    indent()
    input('Press any key')

def change_book_name():
    print(current_librarian.library)
    change_book = find_book()
    print(change_book)
    indent()
    new_book_title = input('Enter new book title: ')
    change_book.book_title = new_book_title
    indent()
    input('Press any key')

def find_book():
    indent()
    book_title = input('Enter the book title: ')
    change_book = current_librarian.library.find_book_title(book_title)
    return change_book

def create_dict_librarians(librarians):
    data_librarians = []
    dict_librarian = {}
    for libr in librarians:
        dict_librarian = {
            'librarian_name': libr.librarian,
            'library_name': libr.library.library_name,
            'list_books': []
        }

        list_books = libr.library.books_list

        for book in list_books:
            dict_librarian['list_books'].append({
                'book_title': book.book_title,
                'author': book.author,
                'page_count': book.page_count,
                'publication_year': book.publication_year
            })

        data_librarians.append(dict_librarian)
    return data_librarians


def save_data(librarians):
    data_librarians = create_dict_librarians(librarians)
    print(data_librarians)
    with open('data.json', 'w') as file:
        json.dump(data_librarians, file, indent=4)
    input('Press any key ')

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
            # Вибір бібліотекаря
            select_librarians(list_librarians)

        case 3:
            # Відображення списку книг обраного бібліотекаря
            # print('current_librarian = ', current_librarian)
            if not current_librarian:
                display_message()
            else:
                print('Librarian', current_librarian.librarian, '\n')
                print(current_librarian.library)
                print()
                print(' ' * 45, end="")
                input('Press any key')
        case 4:
            # Додавання книги до бібліотеки обранного бібліотекаря
            if not current_librarian:
                display_message()
            else:
                indent()
                print(f'Librarian {current_librarian.librarian}, Library "{current_librarian.library.library_name}"\n')
                add_book()

        case 5:
            # Видалення книги з бібліотеки обранного бібліотекаря
            if not current_librarian:
                display_message()
            else:
                indent()
                print(f'Librarian {current_librarian.librarian}, Library "{current_librarian.library.library_name}"\n')
                delete_book()
        case 6:
            # Спроба змінити назву книги
            if not current_librarian:
                display_message()
            else:
                indent()
                print(f'Librarian {current_librarian.librarian}, Library "{current_librarian.library.library_name}"\n')
                change_book_name()
        case 7:
            # Пошук книги
            if not current_librarian:
                display_message()
            else:
                indent()
                print(f'Librarian {current_librarian.librarian}, Library "{current_librarian.library.library_name}"\n')
                change_book = find_book()
                print(change_book)
                input('Press any key ')
        case 8:
            # Збереження у файл
            indent()
            save_data(list_librarians)
