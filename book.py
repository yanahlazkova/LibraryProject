class Book:
    def __init__(self, book_title, author, page_count, publication_year):
        self.__book_title = book_title
        self.__author = author
        self.__page_count = page_count
        self.__publication_year = publication_year

    @property
    def book_title(self):
        return self.__book_title

    @book_title.setter
    def book_title(self, book_title):
        # self.__book_title = book_title
        print("You can't change the title of the book")
    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        # self.__author = author
        print("You can't change the author of the book")

    @property
    def page_count(self):
        return self.__page_count

    @page_count.setter
    def page_count(self, page_count):
        self.__page_count = page_count

    @property
    def publication_year(self):
        return self.__publication_year

    @publication_year.setter
    def publication_year(self, publication_year):
        self.__publication_year = publication_year

    def __str__(self):
        return (f'Book title: {self.__book_title}\nAutor: {self.__author}\n'
                f'Count of page: {self.page_count}\nYear of publication: {self.publication_year}')
