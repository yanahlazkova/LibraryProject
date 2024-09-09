from book import Book

class Library():
    def __init__(self, library_name, books_list: list):
        self.__library_name = library_name
        self.__books_list = books_list

    def add_book(self, book):
        # Спочатку виконати пошук даної книги в списку
        # Якщо список НЕ пустий, виконати пошук
        # якщо книга НЕ знайдена, додати її у список
        if self.__books_list:
            if self.__find_book(book):
                print(f'The Book "{book.book_title}" already exists in the list')
                return
        print("Adding book...")
        self.__books_list.append(book)

    def delete_book(self, book_title):
        found_book = self.find_book_title(book_title)
        if found_book:
            self.__books_list.remove(found_book)
            print("Deleted")
        else:
            print(f"You can't deleted the book \"{book_title}\".\n It's not in the list.")

    def __find_book(self, book):
    # Пошук книги у списку
        return self.__books_list.count(book)

    def find_book_title(self, book_title):
        # Пошук по назві книги
        found_book = None
        for book in self.__books_list:
            if book.book_title == book_title:
                found_book = book
        if found_book:
            return found_book
        else:
            print(f'The book "{book_title}" not found.')
            return False

    @property
    def library_name(self):
        return self.__library_name

    def __str__(self):
        if self.__books_list:
            i = 0
            return (f'List of books in librery "{self.__library_name}":\n'+
                '\n'.join(f'{i+1}.{book.book_title} {book.author} ({book.page_count} pages, '
                          f'{book.publication_year} year)' for i, book in enumerate(self.__books_list)))
        else:
            return f"There are no books in the library \"{self.__library_name}\""




