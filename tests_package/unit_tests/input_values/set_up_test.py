from book_lib.books_catalog.books_catalog import BooksCatalog, Book


class SetUpTest(object):
    def __init__(self):
        self.single_test_book = self.make_single_test_book()
        self.test_books = self.make_test_books()
        self.library = self.make_test_catalog_of_books()

    @staticmethod
    def make_single_test_book():
        test_book = Book("Test_Name", 101, 21, "Simple test description", "Drama",
                         3, "a897fe", "Test_book", 99, 304, 201, 78, 5004)
        return test_book

    @staticmethod
    def make_test_books():
        book1 = Book("Test3", 2.00, 14, None, None, 4, None, None, None, None, None, None, None)
        book2 = Book("Test1", 12.00, 214, None, None, 3, None, None, None, None, None, None, None)
        book3 = Book("Test2", 32.00, 1, None, None, 2, None, None, None, None, None, None, None)
        books = (book1, book2, book3)
        return books

    def make_test_catalog_of_books(self):
        test_catalog = BooksCatalog([])
        for book in self.test_books:
            test_catalog.add_to_library(book)
        return test_catalog
