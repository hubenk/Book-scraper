""" Module containing Router class."""
import json

from book_lib.search_engine.search_engine import SearchEngine
from book_lib.filters.filters import Filters
from book_lib.command_line_arguments.command_line_arguments \
    import CommandLineArguments
from book_lib.books_catalog.books_catalog import BooksCatalog, FILENAME

SORT_PROPERTY = 0
ORDER = 1
DESCENDING_FLAGS = ['d', 'descending']
DEFAULT_SORT = 'title'


class Router(object):
    """
    Router class is responsible for building and running the app.
    """

    def __init__(self):
        """
        Generate instances of:
        CommandLineArguments
        BookCatalog
        SearchEngine
        and Filters class
        """
        self.__arg_parser = CommandLineArguments().argument_parser
        self.__sort_params = self.arg_parser.sort
        self.__library = BooksCatalog(self.sort_params)
        self.__engine = SearchEngine(self.library, self.arg_parser.number)
        self.__filters = Filters(self.arg_parser, self.engine)

    def start_app(self):
        """
        Method that starts the app
        depending on the filters or/and sorting arguments,
        and export the results into 'scrapped_data.w_json'
        """
        self.library.clear_library()
        if self.arg_parser.json:
            titles = self.read_json_titles(self.arg_parser.json)
            self.arg_parser.title = titles

        if self.arg_parser.genre:
            self.engine.scrape_catalog(self.arg_parser.genre,
                                       filters=self.filters)
        else:
            self.engine.scrape_catalog(filters=self.filters)

        if self.sort_params:
            if len(self.sort_params) == 1:
                self.library.library_sort(self.sort_params[SORT_PROPERTY])
            if len(self.sort_params) == 2:
                self.library.library_sort(
                    self.sort_params[SORT_PROPERTY], descending=True
                    if self.sort_params[ORDER] in DESCENDING_FLAGS else False)
        else:
            self.library.library_sort(DEFAULT_SORT)

        self.library.export_to_json()

    def update_arg_parser(self, new_values_dict):
        self.arg_parser.genre = new_values_dict['genre']
        self.arg_parser.title = new_values_dict['title']
        self.arg_parser.description = new_values_dict['keywords']
        self.arg_parser.number = new_values_dict['book_count']
        self.arg_parser.sort = new_values_dict['sort']
        self.arg_parser.filter = new_values_dict['filter']
        self.__sort_params = self.arg_parser.sort
        self.engine.book_count = self.arg_parser.number

    def print_result(self):
        """ Utility method for printing out the scraping result """
        print len(self.library.library)
        result = self.library.library
        for book in result:
            print(book)

    @staticmethod
    def read_json_titles(filename=FILENAME):
        """ TODO: """
        titles = []
        with open(filename, 'r') as json_file:
            file_data = json.load(json_file)
            for title in file_data:
                titles.append(title['title'].encode('utf-8'))
        return titles

    @property
    def arg_parser(self):
        """:return argument parser """
        return self.__arg_parser

    @property
    def sort_params(self):
        """:return sorted list of arguments """
        return self.__sort_params

    @property
    def library(self):
        """:return library"""
        return self.__library

    @property
    def engine(self):
        """:return engine"""
        return self.__engine

    @property
    def filters(self):
        """:return filters list"""
        return self.__filters
