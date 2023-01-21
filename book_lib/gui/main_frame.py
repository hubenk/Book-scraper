""" Module containing MainFrame class """
import os
import Tkinter as tk

from book_lib.gui.fields.genre import Genre
from book_lib.gui.fields.text_box import TextBox
from book_lib.gui.fields.title import Title
from book_lib.gui.fields.filter import Filter
from book_lib.gui.fields.keywords import Keywords
from book_lib.gui.fields.books_count import BooksCount
from book_lib.gui.fields.sorting import Sorting
from book_lib.gui.buttons.scrape_button import ScrapeButton
from book_lib.gui.buttons.json_button import JsonButton

PATH = os.path.dirname(os.path.abspath(__file__))

FILETYPES = (
    ('json files', '*.json'),
)


class MainFrame(tk.Tk):
    """
    MainFrame class used for Tkinter GUI
    """

    def __init__(self, router):
        """
        constructs the main frame of the GUI
        :param router: Router
        """
        tk.Tk.__init__(self)
        self.geometry("1200x600")
        self.title("Book Scraper")
        self.configure_columns()
        self.configure_rows()

        self.__router = router
        self.__text_box = TextBox(self)
        self.__text_box.grid(
            row=0, column=1, rowspan=50, padx=10, pady=10, sticky="W")
        self.__text_box.config(width=850, height=550, borderwidth=2)
        self.__text_box.txt.config(
            font=("cascadia mono", 10),
            undo=True, wrap='word',
            borderwidth=4,
            relief="groove"
        )

        self.__json_button = JsonButton(self, self.router)
        self.__scrape = ScrapeButton(
            self, self.text_box,
            self.router,
            Genre(self),
            Title(self),
            Filter(self),
            Keywords(self),
            BooksCount(self),
            Sorting(self),
            self.json_button
        )

    def configure_columns(self):
        """ utility function used
         to Configure columns of a grid"""
        for col in range(2):
            self.columnconfigure(col, minsize=300)

    def configure_rows(self):
        """ utility function used
         to Configure rows of a grid"""
        for row in range(25):
            self.rowconfigure(row, minsize=20)

    def get_args(self):
        """
        :return: retrieve input for all fields
                 clear the GUI's text box
                 update the arguments with the collected input
                 scrape and display results on the
                 GUI's text box
        """
        return self.scrape.retrieve_input()

    @property
    def router(self):
        """
        :return: Router
        """
        return self.__router

    @property
    def json_button(self):
        """
        :return: JsonButton
        """
        return self.__json_button

    @property
    def scrape(self):
        """
        :return: ScrapeButton
        """
        return self.__scrape

    @property
    def text_box(self):
        """
        :return: TextBox
        """
        return self.__text_box
