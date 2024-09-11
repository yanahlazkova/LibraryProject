from book import Book
from library import Library
from librarian import Librarian

book1 = Book("Book1", "Author1", 101, 2001)
print(book1)

print('\nЗміна назви книги')
book1.book_title = "NewBook1"
# print(book1)

book2 = Book("Book2", "Author2", 102, 2002)
book3 = Book("Book3", "Author3", 103, 2003)

book_list1 = [book1, book2]
library1 = Library("Library children", book_list1)
library2 = Library("Library adult", book_list1)

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
libraryan1 = Librarian('Deny-1', library1)
print(libraryan1.show_books_list())

libraryan2 = Librarian('Meny-2', library2)


list_librarians = [libraryan1, libraryan2]

# methods MENU BOOKS
def display_list_librarians():
    border = "*" * 40
    menu_title = 'List librarians:'
    print(border.rjust(80, " "))

    print('*'.rjust(41, ' '), end="")
    print(menu_title.center(37, ' '), '*')

    print(border.rjust(80, " "))
    print()
    for index, item in enumerate(list_librarians):
        print(" " * 47, index + 1, item.librarian)

    print()
    choice = choice_librarian()
    return choice
def choice_librarian():
    while True:
        try:
            choice_librarian = input('Enter number of choice librarian: ')
            choice_librarian = int(choice_librarian)
            if 1 <= choice_librarian <= len(list_librarians):
                return list_librarians[choice_librarian-1]
            else:
                print(f"Please enter a number between 1 and {len(list_librarians)}")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Add book
def add_book():
    book_title = input('Enter book title: ')
    author = input('Enter author: ')
    page_count = int(input('Enter page count: '))
    publication_year = int(input("Enter year of publication: "))
    new_book = Book(book_title, author, page_count, publication_year)
    choice_librarian = display_list_librarians()
    choice_librarian.add_book(new_book)
    print(f'Added book: \n{new_book}')
    print(f'List books of librarian {choice_librarian.librarian}')

    input("Press any key: ")

# Delete book
def delete_book():
    pass