from book import Book
from library import Library

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
