import Menu
from book import Book
from library import Library
from librarian import Librarian
from Menu import *


book1 = Book("Book1", "Author1", 101, 2001)
print(book1)

print('\nЗміна назви книги')
book1.book_title = "NewBook1"
# print(book1)

book2 = Book("Book2", "Author2", 102, 2002)
book3 = Book("Book3", "Author3", 103, 2003)

book_list1 = [book1, book2]
library1 = Library("Library1", book_list1)

print(library1)

print('\nВидалення не існуючої книги book3\n')
library1.delete_book(book3.book_title)

print('\nДодавання книги book3\n')
library1.add_book(book3)

print()
print(library1)

print('\nДодавання вже існуючої книги book3\n')
library1.add_book(book3)

print(library1)

print('\nЗнайти книгу з назвою Book3\n')
print(library1.find_book_title('Book3'))

print('\nСтворюємо біблиотекаря')
new_libraryan = Librarian('Den-1', library1)
print(new_libraryan.show_books_list())

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
    {'1': 'Add'},
    {'2': 'Delete'},
    {'3': 'Find a book (title)'},
    {'4': 'Fine a book (author)'},
    {'5': 'List books'}
]
menu_books = Menu('MENU BOOKS', menu_books_items)

# Create MENU LIBRARIES
menu_libraries_items = [
    '1. Add book',
    '2. Delete book',
    '3. Find library',
    '4. List libraries'
]

menu_libraries = Menu('MENU BOOKS', menu_libraries_items)

# Create MENU LIBRARIES
menu_libraries_items = [
    '1. Add book',
    '2. Delete book',
    '3. Find book (title)',
    '4. Fine book (author)'
]

menu_libraries = Menu('MENU BOOKS', menu_libraries_items)

# Display Mine Menu
choice_mine_menu = mine_menu.display_menu()
print(choice_mine_menu)

# while True:

