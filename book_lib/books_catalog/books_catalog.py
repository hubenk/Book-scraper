""" Module containing BooksCatalog class."""

import json

from book_lib.books_catalog.book import Book

FILENAME = 'scrapped_data.json'


class BooksCatalog(object):
    """
    BooksCatalog class responsible for representing
    a collection of Book objects.
    """

    def __init__(self, sort_params):
        self.__library = []
        self.__sort_params = sort_params

    def add_to_library(self, book):
        """
        :param book:
        :return:
        """
        if isinstance(book, Book):
            self.__library.append(book)

    def library_sort(self, sort_attr, descending=False):
        """
        :param sort_attr:  Book property
        :param descending: True/False
        """
        self.library.sort(key=lambda x: getattr(x, sort_attr),
                          reverse=descending)

    def export_to_json(self):
        """ Exports library to json file"""
        result = [book.to_dict for book in self.library]
        with open(FILENAME, "w") as book_store:
            json.dump(result, book_store)

    def clear_library(self):
        del self.library[:]

    @property
    def library(self):
        """:return: library"""
        return self.__library

    @property
    def library_generator(self):
        """:return: Books generator"""
        for book in self.__library:
            yield book
