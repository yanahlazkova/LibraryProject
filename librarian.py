from library import Library


class Librarian:
    def __init__(self, librarian, library_name: Library):
        self.__librarian = librarian
        self.__library_name = library_name

    @property
    def librarian(self):
        return self.__librarian

    @librarian.setter
    def librarian(self, new_librarian):
        self.__librarian = new_librarian

    @property
    def library_name(self):
        return self.__library_name

    @library_name.setter
    def library_name(self, new_library_name):
        self.__library_name = new_library_name
