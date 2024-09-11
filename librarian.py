from library import Library


class Librarian:
    def __init__(self, librarian, library: Library):
        self.__librarian = librarian
        self.__library = library

    @property
    def librarian(self):
        return self.__librarian

    @librarian.setter
    def librarian(self, new_librarian):
        self.__librarian = new_librarian

    @property
    def library(self):
        return self.__library

    @library.setter
    def library_name(self, new_library_name):
        self.__library = new_library_name

    def add_book(self, new_book):
        # Додавання книги до бібліотеки, де працює бібліотекар
        self.__library.add_book(new_book)

    def show_books_list(self):
        return self.__library

    def __str__(self):
        return f'\n\n{' ' * 35}Librarian: {self.__librarian} works in library "{self.__library.library_name}\n\n"'
