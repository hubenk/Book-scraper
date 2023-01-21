""" Module containing Filters class. """

from functools import partial
import operator
import re

OPERATORS = {'>': operator.gt, '<': operator.lt, '=': operator.eq,
             '>=': operator.ge, '<=': operator.le}

PROPERTY = {'choice_1': 'price', 'choice_2': 'rating', 'choice_3': 'available'}
PROPERTY_INDEX = 0
SIGN_INDEX = 1
VALUE_INDEX = 2


class Filters(object):
    """
    Class responsible for making a list of filter function pointers
    and arguments, ordered by priority,
    that later are used to perform a search
    """

    def __init__(self, arg_parser, engine):
        """
        Constructor that build up
        :param arg_parser: passed by an instance of Router
        :param engine: passed by an instance of Router
        """
        self.__arguments = arg_parser
        self.__engine = engine
        self.__ordered_filters = []

    def property_filter_create(self, soup):
        """ Creates a property_filter pointer and arguments,
         and insert it in 0th position in ordered_filters list """
        property_fptr = None
        if self.arguments.filter:
            if self.arguments.filter[PROPERTY_INDEX] == PROPERTY['choice_1']:
                property_fptr = partial(self.engine.get_price, soup)
            if self.arguments.filter[PROPERTY_INDEX] == PROPERTY['choice_2']:
                property_fptr = partial(self.engine.get_rating, soup)
            if self.arguments.filter[PROPERTY_INDEX] == PROPERTY['choice_3']:
                property_fptr = partial(self.engine.get_availability, soup)

        if property_fptr:
            func_ptr = partial(
                self.property_filter, property_fptr,
                self.arguments.filter[VALUE_INDEX],
                self.arguments.filter[SIGN_INDEX])
            self.ordered_filters.insert(0, func_ptr)

    def keyword_filter_create(self, soup):
        """ Creates a keywords_filter pointer and arguments,
         and insert it in 0th position in ordered_filters list """
        property_fptr = None
        if self.arguments.description:
            property_fptr = partial(self.engine.get_description, soup)

        if property_fptr:
            func_ptr = partial(self.keywords_filter, property_fptr,
                               self.arguments.description, match_all=False)
            self.ordered_filters.insert(0, func_ptr)

    def title_filter_create(self, soup):
        """ Creates a title_filter pointer and arguments,
         and insert it in 0th position in ordered_filters list """
        property_fptr = None
        if self.arguments.title:
            property_fptr = partial(self.engine.get_title, soup)

        if property_fptr:
            func_ptr = partial(self.title_filter, property_fptr,
                               self.arguments.title)
            self.ordered_filters.insert(0, func_ptr)

    def create_filter_map(self, soup):
        """
        Responsible for the priority of the elements
        in the ordered filters list
        :param soup: passed by an instance of SearchEngine
        """
        self.__ordered_filters = []
        self.property_filter_create(soup)
        self.title_filter_create(soup)
        self.keyword_filter_create(soup)

    def apply_filters(self, soup):
        """
        Method that apply filters
        :param soup: the current soup passed by an instance of SearchEngine
        :return: boolean (True - all filters pass | False - if any fail
        or there's no filters)
        """
        self.create_filter_map(soup)
        filters_length = len(self.ordered_filters)
        if filters_length > 0:
            for func in self.ordered_filters:
                if not func():
                    return False
        return True

    @staticmethod
    def property_filter(book_property, value_to_compare, operation):
        """ Applies operation and returns boolean """
        if value_to_compare is None or operation is None:
            return True
        return OPERATORS[operation](book_property(), int(value_to_compare))

    @staticmethod
    def title_filter(book_title, expected_titles):
        """ Applies operation and returns boolean """
        if type(expected_titles) is list:
            for title in expected_titles:
                if title.lower() in book_title().lower():
                    return True
            return False
        return expected_titles.lower() in book_title().lower()

    @staticmethod
    def keywords_filter(book_description, keywords_list, match_all=False):
        """ Applies operation and returns boolean """
        if match_all:
            return all(
                word.lower() in re.findall(r"[\w']+", book_description())
                for word in keywords_list)
        return any(word.lower() in keywords_list
                   for word in re.findall(r"[\w']+", book_description()))

    @property
    def arguments(self):
        """ :return: arguments """
        return self.__arguments

    @property
    def ordered_filters(self):
        """ :return: ordered list of filters """
        return self.__ordered_filters

    @property
    def engine(self):
        """ :return: search engine """
        return self.__engine
