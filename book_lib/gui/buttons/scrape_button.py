""" Module containing GUI's ScrapeButton class """
# -*- coding: utf-8 -*-
import Tkinter as tk
import json
from book_lib.books_catalog.books_catalog import FILENAME


class ScrapeButton(object):
    """
    ScrapeButton class represents a
    call-to-action button (or CTA button)
    """

    def __init__(self, window, text_box,
                 router, genre, title,
                 filter_input, keywords, books_count,
                 sorting, json_button):
        """
        Constructor
        :param window: Tk's main frame
        :param text_box: TextBox
        :param router: Router
        :param genre: Genre
        :param title: Title
        :param filter_input: Filter
        :param keywords: Keywords
        :param books_count: BooksCount
        :param sorting: Sorting
        :param json_button: JsonButton
        """
        self.__scrape_button = tk.Button(
            window,
            activebackground="#6c757d",
            text="Scrape!",
            font=('Arial', 18, 'bold'),
            command=self.retrieve_input)
        self.__scrape_button.grid(row=22, sticky="W", padx=100)

        self.__router = router
        self.__genre = genre
        self.__title = title
        self.__filter = filter_input
        self.__keywords = keywords
        self.__book_count = books_count
        self.__sorting = sorting
        self.__text_box = text_box
        self.__json_button = json_button

    def retrieve_input(self):
        """
        retrieve input for all fields
        clear the GUI's text box
        update the arguments with the collected input
        scrape and display results on the
        GUI's text box
        """
        _input = {
            "genre": self.genre.retrieve_genre(),
            "title": self.title.retrieve_title(),
            "keywords": self.keywords.retrieve_keywords(),
            "book_count": self.book_count.retrieve_book_count(),
            "filter": self.filter.retrieve_filter_data(),
            "sort": self.sorting.retrieve_sorting_data(),
        }
        self.text_box.clear()
        self.router.update_arg_parser(_input)
        self.router.start_app()
        self.display_results()
        self.router.arg_parser.json = None
        self.json_button.clear_selected_label()

    def display_results(self):
        """
        utility function used to display the scraped
        results in the text box of the GUI
        """
        with open(FILENAME, 'r') as json_file:
            file_data = json.load(json_file)
            for book in file_data:
                self.text_box.txt.insert(
                    'end', self.pretty_print(self.decode_dict(book)))

    @staticmethod
    def decode_dict(data):
        """
        :param data: dict
        :return: decoded dict with
        ascii-encoded strings
        """
        result = {}
        for key, value in data.iteritems():
            if isinstance(key, unicode):
                key = key.encode('utf-8')
            if isinstance(value, unicode):
                value = value.encode('utf-8')

            result[key] = value
        return result

    @staticmethod
    def pretty_print(book):
        """
        :param book: dict
        :return: formatted string
        """
        return """
        \n\t\tTitle: {title}
        \n\tPrice: {price}\t\t\t\tAvailability: {available}
        \n\tGenre: {genre}\t\t\t\tRating: {rating}
        \n\tProduct Type: {product_type}\t\t\t\tUPC: {upc}
        \n\tPrice Excl Tax: {price_excl}\t\t\t\tPrice Incl Tax: {price_incl}
        \n\tTax: {tax}\t\t\t\tIn stock: {in_stock}
        \n\tReviews: {reviews}\t\t\t\tDescription: {desc}
        """.format(
            title=book["title"], price=book["price"],
            available=book["available"], genre=book["genre"],
            rating=book["rating"], desc=book["description"],
            upc=book["upc"], product_type=book["product type"],
            price_excl=book["price_incl_tax"], in_stock=book["in_stock"],
            price_incl=book["price_excl_tax"], tax=book["tax"],
            reviews=book["reviews"]).decode('ascii', 'ignore')

    @property
    def scrape_button(self):
        """ :return scrape button """
        return self.__scrape_button

    @property
    def router(self):
        """ :return  router """
        return self.__router

    @property
    def genre(self):
        """ :return  genre """
        return self.__genre

    @property
    def title(self):
        """ :return  title """
        return self.__title

    @property
    def filter(self):
        """ :return  filter """
        return self.__filter

    @property
    def keywords(self):
        """ :return  keywords """
        return self.__keywords

    @property
    def book_count(self):
        """ :return  book count """
        return self.__book_count

    @property
    def sorting(self):
        """ :return sorting """
        return self.__sorting

    @property
    def text_box(self):
        """ :return text box """
        return self.__text_box

    @property
    def json_button(self):
        """ :return json button """
        return self.__json_button
