""" Module containing GUI's BooksCount class """
import Tkinter as tk


class BooksCount(object):
    """
    BooksCount class is used to represent a
    section of the gui responsible for
    collecting user input, regarding the
    number of books that should be scraped
    """

    def __init__(self, window):
        """
        :param window: Tk's main frame
        """
        self.__book_count_label = tk.Label(
            window,
            text="Number of books",
            font=('Arial', 10, 'bold'))
        self.__book_count_label.grid(row=12, column=0, padx=10, sticky="W")

        self.value = tk.StringVar(value='0')
        self.value.trace('w', self.check_value)
        self.__book_count_text_box = tk.Entry(
            window,
            textvariable=self.value, relief="groove",
            width=4,
            font=('Arial', 12))
        self.__book_count_text_box.grid(row=12, column=0, padx=150, sticky='W')

    def check_value(self, *args):
        """
        validates whether the value is digit
        """
        if not self.value.get().isdigit():
            self.value.set('0')

    def retrieve_book_count(self):
        """
        :return: book count
        """
        return int(self.__book_count_text_box.get())
